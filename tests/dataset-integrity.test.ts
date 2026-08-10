import { searchQuery } from "../src/research/handoff";
import { displayRange } from "../src/chrono/displayRange";
import entitiesFile from "../src/data/entities.json";
import { describe, expect, it } from "vitest";
import { calendars, datasetVersion, entities, referenceFrames, schemaVersion, sources, themes } from "../src/dataset/dataset";
import type { Entity } from "../src/entity/entity";
import { buildIndex , searchEntities , lookup } from "../src/entity/tree";
import { datingOf } from "../src/chrono/fromEntity";
import { isScientificDating } from "../src/chrono/year";

const idx = buildIndex(entities);

describe("dataset envelope", () => {
  it("is v0.36.0.0 on schema 3.6.0", () => {
    // MAJOR on both. Schema 2.0.0 adds the taxon and threshold kinds, so a
    // consumer switching exhaustively on kind breaks. Dataset 3.0.0 moves the
    // prehistory ids (origins -> hominins) and re-parents the stone ages, so
    // a consumer addressing by id breaks too.
    //
    // Recorded here because 2.2.0 was itself mis-versioned: it re-parented
    // three top-level eras and dropped four ids under a minor bump.
    // Schema 3.0.0 splits dating_method into start_dating_method /
    // end_dating_method (Q-30). MAJOR because a consumer reading the old
    // entity-level field now finds nothing at all.
    expect(datasetVersion).toBe("0.36.0.0");
    // 3.6.0: retired the three precision enums, added extant, historicity, date_standing,
    // search_phrase, qualified_name and redirects, and added the polity, culture, language,
    // tradition, people, network, person and city kinds.
    expect(schemaVersion).toBe("3.6.0");
  });

  it("has the expected collection sizes", () => {
    // The generated corpus includes the historical baseline, the prehistory
    // branch, and the regional prehistory chronology extensions.
    // 3,301 -> 5,507. The modern era was almost absent: 69 entities began in the nineteenth
    // century and 71 in the twentieth, worldwide, and the entire United States subtree was two
    // rows. 2,241 were authored and 215 dropped as duplicates during reconciliation.
    expect(entities.length).toBe(5507);
    expect(calendars.length).toBe(21);
    expect(themes.length).toBe(16);
    expect(referenceFrames.length).toBe(46);
  });
});

describe("referential integrity", () => {
  it("has unique ids", () => {
    expect(new Set(entities.map((e) => e.id)).size).toBe(entities.length);
  });

  it("resolves every parent_id", () => {
    const bad = entities.filter((e) => e.parent_id !== null && !idx.byId.has(e.parent_id));
    expect(bad.map((e) => e.id)).toEqual([]);
  });

  it("resolves every cross_parent_id", () => {
    const bad = entities.flatMap((e) =>
      (e.cross_parent_ids ?? []).filter((c) => !idx.byId.has(c)).map((c) => `${e.id} -> ${c}`),
    );
    expect(bad).toEqual([]);
  });

  it("resolves every theme entity_id", () => {
    const bad = themes.flatMap((t) =>
      t.entity_ids.filter((id) => !idx.byId.has(id)).map((id) => `${t.id} -> ${id}`),
    );
    expect(bad).toEqual([]);
  });

  it("has no parent cycles", () => {
    for (const e of entities) {
      const seen = new Set<string>();
      let cur: string | null = e.id;
      while (cur !== null) {
        if (seen.has(cur)) throw new Error(`cycle at ${e.id}`);
        seen.add(cur);
        cur = idx.byId.get(cur)?.parent_id ?? null;
      }
    }
  });
});

describe("date invariants", () => {
  it("never uses year zero", () => {
    const bad = entities.filter((e) => e.start_year === 0 || e.end_year === 0);
    expect(bad.map((e) => e.id)).toEqual([]);
  });

  it("never ends before it starts", () => {
    const bad = entities.filter(
      (e) => e.start_year !== null && e.end_year !== null && e.end_year < e.start_year,
    );
    expect(bad.map((e) => e.id)).toEqual([]);
  });

  it("keeps children inside parent ranges unless explicitly flagged", () => {
    const bad: string[] = [];
    for (const e of entities) {
      if (e.allow_outside_parent_dates === true || e.parent_id === null) continue;
      const p = idx.byId.get(e.parent_id);
      if (!p || p.start_year === null || e.start_year === null) continue;
      if (e.start_year < p.start_year) bad.push(`${e.id} starts before ${p.id}`);
      if (p.end_year !== null && e.end_year !== null && e.end_year > p.end_year) {
        bad.push(`${e.id} ends after ${p.id}`);
      }
    }
    expect(bad).toEqual([]);
  });
});

describe("gap-analysis baseline", () => {
  // These assertions track docs/gap-analysis-v2.1.0.md. They are designed to
  // FAIL when a gap closes, so a partial backfill cannot drift unnoticed --
  // update the number in the same commit that closes it.
  it("cites sources across the prehistory branch", () => {
    // Was 0/1305 across the whole dataset: the builders could not emit the
    // field at all. Closing that (Q-10) is what made this possible.
    const cited = entities.filter((e) => (e.source_ids?.length ?? 0) > 0);
    expect(cited.length).toBe(585);
  });

  it("carries dating methods and uncertainty bounds", () => {
    // These two numbers are the whole point of retiring the precision enums. Before the
    // migration: 416 entities carried a dating method and 26 carried a lower bound, while
    // 1,493 said `approx` and left the width unstated. A method is now required on every
    // populated endpoint, and bounds are required unless the method is `calendar` (an
    // attested year is not an estimate) or `received` (a traditional figure is the
    // tradition's claim, not a measurement).
    expect(entities.filter((e) => e.start_dating_method !== undefined).length).toBe(5461);
        // 1,036, down from 1,700. The drop is the fix, not a regression: 664 entities dated after
    // 1000 CE had been given plus-or-minus a century by a convention that keyed on abs(year) and
    // so treated 1989 CE like 1989 BCE. The Fall of the Berlin Wall read 1889 to 2089.
    // Down from 2,203 to 71. Every remaining interval was typed by a person: either it sits
    // off-centre, or it is one-sided. The 2,132 that went were produced by a convention that
    // multiplied the year by a fixed percentage -- 316 entities at exactly 6%, 241 at 15%, and
    // 2,193 of 2,218 intervals exactly symmetric. A reader seeing plus-or-minus a century
    // believes somebody measured it, so an invented interval is worse than none. The sourcing
    // pass will write real ones back with a method that says where they came from.
    // 53, not 71: rule 15 then removed 39 degenerate bounds that had been set equal to their own
    // estimate, which asserts the date is known exactly and is the opposite of what recording an
    // interval is for. Those had survived the symmetry test precisely because being equal on one
    // side makes a pair asymmetric.
    expect(entities.filter((e) => e.start_year_min !== undefined).length).toBe(53);
  });

  it("dates each boundary on its own evidence", () => {
    // Q-30, resolved in schema 3.0.0. The end is no longer the start's method
    // reused: 82 ends carry a method, and the two that DIFFER from their start
    // are the cases the question was raised about -- a range whose ends rest on
    // different science. The remainder are unset on purpose, because an end
    // beyond radiocarbon's reach was never dated by the start's method and
    // saying otherwise is the exact error the split exists to prevent.
    const withEnd = entities.filter((e) => e.end_dating_method !== undefined);
    expect(withEnd.length).toBe(4385);

    // The differing set was a hand-listed dozen and is now 233, which is the property working
    // rather than breaking: a city founded in prehistory and abandoned in the documentary era
    // genuinely has its two ends resting on different evidence -- typological for the founding,
    // a calendar record for the abandonment. Asserting the property beats maintaining a list.
    const differing = entities.filter(
      (e) =>
        e.end_dating_method !== undefined &&
        e.end_dating_method !== e.start_dating_method &&
        // "unknown" at one end is an admission, not a different kind of evidence.
        e.end_dating_method !== "unknown" &&
        e.start_dating_method !== "unknown",
    );
    expect(differing.length).toBeGreaterThan(100);

    // The clearest case of the property: a range whose two ends rest on different science.
    const ids = new Set(differing.map((e) => e.id));
    expect(ids.has("global.paleolithic.middle-stone-age")).toBe(true);
    const msa = entities.find((e) => e.id === "global.paleolithic.middle-stone-age")!;
    expect(msa.start_dating_method).toBe("luminescence");
    expect(msa.end_dating_method).toBe("radiocarbon-calibrated");

    // Every differing pair must straddle a real evidential boundary rather than being noise:
    // one end dated by material typology and the other by a written record.
    for (const e of differing) {
      const pair = [e.start_dating_method, e.end_dating_method].sort().join("|");
      expect(pair, `${e.id}`).not.toBe("calendar|calendar");
    }
  });

  it("distinguishes an extant taxon from an undated end", () => {
    // end_year null means "extant" for H. sapiens and "never dated" for
    // H. luzonensis. Conflating them would put a hominin known from foot
    // bones among the living.
    const sapiens = entities.find((e) => e.id === "global.prehistory.hominins.homo-sapiens");
    const luzon = entities.find((e) => e.id === "global.prehistory.hominins.homo-luzonensis");
    // `extant` now carries this distinction outright, instead of it being inferred from the
    // absence of an end_precision -- an inference that defaulted to "present" and so quietly
    // listed anything undated among the living.
    expect(sapiens?.end_year).toBeNull();
    expect(sapiens?.extant).toBe(true);
    expect(luzon?.end_year).toBeNull();
    expect(luzon?.extant).toBeUndefined();
  });

  it("has calendar_ids on only 267 entities", () => {
    expect(entities.filter((e) => (e.calendar_ids?.length ?? 0) > 0).length).toBe(267);
  });

  it("gives every region node a summary", () => {
    // Was a debt marker asserting 5 of 42. Region nodes are the highest-traffic
    // entities in the app -- a reader clicking "China" or "Africa" lands on one -- and
    // they were the emptiest. Now an invariant rather than a record of the gap.
    const regions = entities.filter((e) => e.kind === "region");
    expect(regions.length).toBe(46);
    const missing = regions.filter((e) => (e.summary ?? "").trim() === "").map((e) => e.id);
    expect(missing).toEqual([]);
  });
});

describe("the behavioural gate", () => {
  const byId = new Map(entities.map((e) => [e.id, e]));

  it("floors the app at 3.3 Ma, older than the oldest Homo fossil", () => {
    // The floor is behavioural. Lomekwi 3 knapping predates Ledi-Geraru by
    // ~500 kyr, so a taxonomic floor would exclude the oldest instance of the
    // behaviour the app exists to track.
    const pre = byId.get("global.prehistory");
    const homo = byId.get("global.prehistory.hominins");
    expect(pre?.start_year).toBe(-3300000);
    expect(homo!.start_year!).toBeGreaterThan(pre!.start_year!);
  });

  it("names the hominin branch for its contents, not for the scope rule", () => {
    expect(byId.get("global.prehistory.hominins")?.name).toBe("Hominins");
    expect(byId.has("global.prehistory.origins")).toBe(false);
  });

  it("models the floor as a behaviour with the site as evidence", () => {
    // If an older knapping site is accepted the date moves and scope does not.
    const k = byId.get("global.prehistory.firsts.stone-knapping");
    expect(k?.kind).toBe("threshold");
    // A terminus post quem is now a lower bound with no upper one, rather than an enum value
    // named "minimum". And the year no longer claims more significant digits than its
    // uncertainty supports: 3.3 Ma, not a specific year inside it.
    expect(k?.start_year_min).toBeDefined();
    expect(k?.start_year_max).toBeUndefined();
    expect(k?.start_year).toBe(-3300000);
  });

  it("gives every threshold a minimum precision and no end", () => {
    const t = entities.filter((e) => e.kind === "threshold");
    expect(t.length).toBeGreaterThanOrEqual(10);
    for (const e of t) {
      expect(e.start_year_max).toBeUndefined();
      expect(e.end_year).toBeNull();
    }
  });

  it("keeps species as taxa, not periods", () => {
    const sp = entities.filter((e) => e.parent_id === "global.prehistory.hominins");
    expect(sp.length).toBe(12);
    expect(sp.every((e) => e.kind === "taxon")).toBe(true);
  });

  it("keeps the Lomekwian distinct from the Oldowan", () => {
    // 700 kyr apart, so the extension is real rather than a relabel.
    const lom = byId.get("global.paleolithic.lomekwian");
    const old = byId.get("global.paleolithic.oldowan");
    expect(lom!.start_year!).toBeLessThan(old!.start_year!);
    expect(old!.start_year! - lom!.start_year!).toBeGreaterThan(600000);
  });
});

describe("reference anchors reach the deep-time content", () => {
  it("has anchors before the Holocene", () => {
    // Was a real gap: the eight cultural anchor sets all start in the
    // Holocene, so 42 entities older than 10,000 BCE had nothing to orient
    // against. The set covered 0.35% of the dataset's span.
    const deep = referenceFrames.filter((f) => f.anchor_set === "deep-time");
    expect(deep.length).toBeGreaterThanOrEqual(7);
  });

  it("leaves almost nothing older than its earliest anchor", () => {
    const earliest = Math.min(...referenceFrames.map((f) => f.year));
    const orphans = entities.filter(
      (e) => e.start_year !== null && e.start_year < earliest,
    );
    // Two African sites hold deposits older than the oldest anchor: Turkana
    // Basin bottoms out at 4.1 Ma and Sterkfontein at 3.67 Ma. Both are
    // allow_outside_parent_dates, both are real, and the Laetoli anchor added
    // with the Africa pass brought this back down from seven.
    expect(orphans.length).toBeLessThanOrEqual(3);
  });
});

describe("dating method is physically capable of the date", () => {
  it("never claims radiocarbon beyond its range", () => {
    // Caught six real entities, three authored by hand across earlier
    // sessions. dating_method is one field but a long-lived entity has two
    // boundaries dated by different means: Neanderthals appear at 400 ka by
    // uranium-series and disappear at 40 ka by radiocarbon. Recording the
    // end's method and letting it describe the start is the natural error.
    const CEILING_BP = 55_000;
    const bp = (y: number) => 1950 - (y < 0 ? y + 1 : y);
    const beyondReach = (
      method: string | undefined,
      year: number | null,
    ): boolean =>
      typeof method === "string" &&
      method.startsWith("radiocarbon") &&
      year !== null &&
      bp(year) > CEILING_BP;

    // Both boundaries are checked now. The end check is new reach rather than
    // a port: before schema 3.0.0 the end had no method of its own, so an
    // impossible end date was literally untestable.
    const impossible = entities.filter(
      (e) =>
        beyondReach(e.start_dating_method, e.start_year) ||
        beyondReach(e.end_dating_method, e.end_year),
    );
    expect(impossible.map((e) => e.id)).toEqual([]);
  });

  it("declares uncalibrated radiocarbon in the note", () => {
    // The refusal to convert only helps if the entity says what it is.
    const undeclared = entities.filter(
      (e) =>
        (e.start_dating_method === "radiocarbon-uncalibrated" ||
          e.end_dating_method === "radiocarbon-uncalibrated") &&
        !(e.date_note ?? "").toUpperCase().includes("UNCALIB"),
    );
    expect(undeclared.map((e) => e.id)).toEqual([]);
  });
});

describe("Neolithic transition", () => {
  const NEO = "global.neolithic.agricultural-revolution";
  const node = () => entities.find((e) => e.id === NEO)!;

  it("is an era, not an event", () => {
    // A 4,000-year unconscious process filed as `event` asserted something the
    // literature abandoned. The id stays for stability; the claim does not.
    expect(node().kind).toBe("era");
    expect(node().name).toBe("Neolithic Transition");
    expect(node().aliases).toContain("Agricultural Revolution");
  });

  it("carries the gradualist framing and the dissent from it", () => {
    expect(node().date_note).toMatch(/protracted|NOT A REVOLUTION/);
    // Abbo and Gopher's rapid core-area model is live, not settled against.
    expect(node().alternatives?.some((a) => a.standing === "minority")).toBe(true);
  });

  it("has its independent centres", () => {
    const centres = entities.filter((e) => e.parent_id === NEO);
    expect(centres.length).toBe(8);
    // How many centres exist is itself disputed, so the count is a caveat
    // rather than a claim the node makes.
    expect(node().caveats?.some((c) => c.kind === "contested-existence")).toBe(true);
  });

  it("records pottery as predating farming", () => {
    // The single most useful correction in this layer: ceramics are not a
    // marker of agriculture or sedentism.
    const pot = entities.find((e) => e.id === "global.prehistory.firsts.pottery")!;
    const cereal = entities.find((e) => e.id === "global.prehistory.firsts.cereal-farming")!;
    expect(pot.start_year!).toBeLessThan(cereal.start_year! - 9000);
    expect(pot.caveats?.[0]?.kind).toBe("misconception");
  });

  it("keeps Botai as husbandry and not as ancestry", () => {
    const horse = entities.find((e) => e.id === "global.prehistory.firsts.horse-domestication")!;
    expect(horse.start_year).toBe(-2200);
    const botai = horse.alternatives?.find((a) => a.label.includes("Botai"));
    expect(botai?.standing).toBe("superseded");
  });
});

describe("Europe 10,000-2,500 BCE", () => {
  it("fills the Mesolithic hole", () => {
    // Before this pass Europe had nothing at all between 10,000 and 5,500 BCE.
    const band = entities.filter(
      (e) =>
        e.id.startsWith("europe.prehistory") &&
        e.start_year !== null &&
        e.start_year >= -10000 &&
        e.start_year < -5500,
    );
    expect(band.length).toBeGreaterThanOrEqual(8);
  });

  it("keeps Lepenski Vir's hiatus visible instead of smoothing it", () => {
    const lv = entities.find((e) => e.id === "europe.prehistory.lepenski-vir")!;
    expect(lv.date_note).toMatch(/EMPTY for at least 700 years/);
    expect(lv.alternatives?.[0]?.standing).toBe("superseded");
  });

  it("refuses a single pan-European Sauveterrian date", () => {
    // Italian AMS and French typological dating differ by about a millennium.
    const s = entities.find((e) => e.id === "europe.prehistory.sauveterrian")!;
    // "disputed" was a precision value. The dispute lived in the bounds and the note; the
    // bounds were a symmetric plus-or-minus 200 from the convention generator and went with the
    // rest, so the note and the rival reading now carry it alone until the sourcing pass.
    expect(s.date_standing).toBe("minority");
    expect(s.alternatives?.length).toBeGreaterThan(0);
    expect(s.date_note).toMatch(/REGIONAL, NOT PAN-EUROPEAN/);
  });

  it("does not author the Tardenoisian at all", () => {
    // Sources disagreed by up to 3,000 years and mixed calibrated with
    // uncalibrated figures. A gap is better than a guess.
    expect(entities.some((e) => /tardenois/i.test(e.id))).toBe(false);
  });

  it("carries Varna's superseded traditional chronology", () => {
    const v = entities.find((e) => e.id === "europe.prehistory.varna")!;
    expect(v.start_year).toBe(-4596);
    expect(v.alternatives?.some((a) => a.standing === "superseded")).toBe(true);
  });
});

describe("Holocene Americas", () => {
  it("stores Monte Verde in calendar years, not cal BP", () => {
    // Regression: this entity held -14500..-14000 and its alternative
    // -8200..-4200. Those were cal BP figures written into the BCE field,
    // putting the site 1,950 years too early. 14,500 cal BP is 12,551 BCE.
    const mv = entities.find((e) => e.id === "global.paleolithic.monte-verde")!;
    // -12550 rather than -12551. The trailing digit was an artifact of subtracting the
    // Before-Present epoch, never a measurement, and this entity's own note documents the
    // published range as 14,200-14,900 cal BP. The point of the test stands: a calendar year,
    // not a cal BP figure written into the year field.
    expect(mv.start_year).toBe(-12550);
    expect(mv.start_year).not.toBe(-14500);
    expect(mv.end_year).toBe(-12250);
    const alt = mv.alternatives?.find((a) => a.label.includes("Surovell"))!;
    expect(alt.start_year).toBe(-6251);
    expect(alt.end_year).toBe(-2251);
  });

  it("has exactly one Monte Verde", () => {
    // Two of them, disagreeing by two millennia, is what exposed the bug above.
    expect(entities.filter((e) => /Monte Verde/.test(e.name)).length).toBe(1);
  });

  it("marks uncalibrated dates as uncalibrated", () => {
    // Las Vegas is published in radiocarbon years. The app refuses calendar
    // conversion for these, which only works if the method is recorded.
    const lv = entities.find((e) => e.id === "americas.prehistory.las-vegas-culture")!;
    expect(lv.start_dating_method).toBe("radiocarbon-uncalibrated");
  });

  it("puts American mummification before Egypt's", () => {
    const m = entities.find(
      (e) => e.id === "global.prehistory.firsts.artificial-mummification",
    )!;
    expect(m.start_year).toBeLessThan(-6000);
    expect(m.caveats?.[0]?.kind).toBe("misconception");
  });

  it("reports Cerro Sechin's date as unverified rather than repeating it", () => {
    const cs = entities.find((e) => e.id === "americas.prehistory.cerro-sechin")!;
    expect(cs.start_year).toBe(-1887);
    expect(cs.caveats?.[0]?.text).toMatch(/unverified/);
  });

  it("adds the two later rounds of the White Sands dispute", () => {
    const ws = entities.find((e) => e.id === "americas.prehistory.white-sands")!;
    expect(ws.date_note).toMatch(/three\s+material types, two labs/);
    expect(ws.alternatives?.length).toBeGreaterThanOrEqual(2);
  });
});

describe("Central Asia and the Austronesian world", () => {
  it("fills the Central Asian Neolithic hole", () => {
    // The region held nothing at all between 10,000 and 3,700 BCE.
    const band = entities.filter(
      (e) =>
        e.id.startsWith("central-asia.prehistory") &&
        e.start_year !== null &&
        e.start_year >= -10000 &&
        e.start_year < -3700,
    );
    expect(band.length).toBeGreaterThanOrEqual(2);
  });

  it("carries Namazga as a received convention, not as dates", () => {
    // 0.10.0.0 left this out because its phase brackets trace to Soviet
    // typology rather than to any radiocarbon table. 0.11.0.0 includes it
    // under `standing: "traditional"`, which is only defensible because that
    // standing now leads the readout and marks the picker gutter.
    const n = entities.find((e) => e.id === "central-asia.prehistory.namazga")!;
    expect(n.date_standing).toBe("traditional");
    // The precision enum is retired; `received` as the dating method is what "this is a
    // handed-down figure, not a measurement" now means, and it always was the better signal.
    expect(n.start_dating_method).toBe("received");
    expect(n.date_note).toMatch(/RECEIVED FRAMEWORK, NOT A DATED ONE/);
  });

  it("does not let `traditional` become a loophole", () => {
    // A received convention must declare itself in all three fields: the
    // standing, the precision the banner and picker dagger key off, and now the
    // method that says how the date was arrived at.
    //
    // The method clause was impossible in 0.11.0.0 — the enum had no value for
    // "handed down", and calling Rome's 753 BCE `typological` or `unknown`
    // would have misdescribed a date whose provenance is perfectly well known.
    // Schema 3.1.0 adds `received` and the gap closes.
    for (const e of entities.filter((x) => x.date_standing === "traditional")) {
      expect(e.start_dating_method, `${e.id} method`).toBe("received");
      // A received figure is the tradition's claim rather than an estimate, so it carries no
      // uncertainty bounds -- there is nothing to be uncertain between.
      expect(e.start_year_min, `${e.id} has no bounds`).toBeUndefined();
    }
  });

  it("keeps the widest eras subdivided", () => {
    // The region-by-band matrix cannot see a childless block: two thousand
    // years of Indus Civilisation with no children counted as one entity in
    // one band, exactly like a node that was properly subdivided. It sat that
    // way for ten releases. These are the eras that gap-hunting has since
    // filled, pinned so they cannot quietly empty out again.
    const withKids = new Set(entities.map((e) => e.parent_id).filter(Boolean));
    for (const id of [
      "south-asia.indus",
      "global.neolithic.agricultural-revolution",
    ]) {
      expect(entities.some((e) => e.id === id), `${id} exists`).toBe(true);
      expect(withKids.has(id), `${id} has children`).toBe(true);
    }
  });

  it("does not present a pre-calibration date as a live rival", () => {
    // Agrawal's 550-year Harappan span is Science, February 1964 -- three
    // years before the first calibration curve. It reads like a competing
    // modern chronology and is not one, so it ships as `superseded`.
    const mature = entities.find((e) => e.id === "south-asia.indus.mature")!;
    const alt = mature.alternatives!.find((a) => a.dating_method === "radiocarbon-uncalibrated")!;
    expect(alt.standing).toBe("superseded");
  });

  it("never states a chronology-scheme date as a bare fact", () => {
    // Hammurabi shipped as 1792-1750 for ten releases with no note, no
    // standing and no source. Those are Middle Chronology dates; the rival
    // schemes move the same reign by up to 120 years, and the whole 2nd
    // millennium moves with it. A date that depends on choosing a scheme has
    // to say so, or it is Monte Verde again.
    for (const id of [
      "west-asia.mesopotamia.old-babylonian",
      "west-asia.mesopotamia.old-babylonian.hammurabi",
      "west-asia.anatolia.hittites.sack-of-babylon",
    ]) {
      const e = entities.find((x) => x.id === id)!;
      expect(e, `${id} exists`).toBeDefined();
      // "disputed" was a precision value. A dispute is now carried either by bounds or by
      // named alternatives. Hammurabi is the case that forces the "either": his dates come
      // from rival Mesopotamian chronologies, so the method is `received` and bounds would be
      // meaningless -- the disagreement is between whole schemes, not a width around a number.
      // Bounds were one of the three ways to carry a scheme dispute and are no longer
      // available, the convention generator having supplied most of them. A named scheme in
      // the note is itself the disclosure this test exists to require.
      const carriesDispute =
        (e.alternatives?.length ?? 0) > 0 || /[Cc]hronology/.test(e.date_note ?? "");
      expect(carriesDispute, `${id} carries the dispute`).toBe(true);
      expect(/[Cc]hronology/.test(e.date_note ?? ""), `${id} names the scheme`).toBe(true);
    }
  });

  it("keeps every region populated", () => {
    // west-asia.anatolia was an empty region node -- no Hittites, no Troy, no
    // Lydia -- and the childless-node report could not see it, because that
    // report only examined eras and periods. An empty region is the worst gap
    // the dataset can have, so it is now checked here as well as reported.
    const withKids = new Set(entities.map((e) => e.parent_id).filter(Boolean));
    for (const r of entities.filter((e) => e.kind === "region")) {
      expect(withKids.has(r.id), `${r.id} is empty`).toBe(true);
    }
  });

  it("sources the entities people actually open", () => {
    // The dataset's rigour was inverted: everything authored under the
    // sourcing rule was scrupulous, and everything older was bare -- which
    // meant Namazga had three sources and a dagger while the Roman Republic
    // had nothing. A visitor's first click landed on the weakest part.
    for (const id of [
      "europe.mediterranean.greece",
      "europe.mediterranean.greece.mycenaean",
      "europe.mediterranean.macedon",
      "europe.mediterranean.rome",
      "europe.mediterranean.rome.republic",
      "europe.mediterranean.rome.empire",
      "europe.mediterranean.byzantine",
    ]) {
      const e = entities.find((x) => x.id === id)!;
      expect(e, `${id} exists`).toBeDefined();
      expect((e.source_ids ?? []).length, `${id} is sourced`).toBeGreaterThan(0);
    }
  });

  it("does not present Macedon's legendary founding as its start", () => {
    // Macedon shipped from 808 BCE, a king-list back-calculation to Karanos,
    // a founder Herodotus does not even name. Structurally identical to Rome's
    // 753, and sitting one row away from it in the same tree.
    const mac = entities.find((e) => e.id === "europe.mediterranean.macedon")!;
    expect(mac.start_year).toBe(-700);
    const legend = mac.alternatives!.find((a) => a.start_year === -808)!;
    expect(legend.standing).toBe("traditional");
    expect(legend.dating_method).toBe("received");
  });

  it("keeps multi-regional empires out of the top-level region list", () => {
    // "Cross-Regional Empires" was a top-level peer of real geographies while
    // not being a place, and "cross" implies crossing from one region to
    // another rather than being in several at once. It is now
    // global.multi-regional, and each empire is cross-linked to the regions it
    // held -- so Suleiman is reachable from Anatolia, the Nile and here.
    expect(entities.find((e) => e.id === "cross-regional")).toBeUndefined();
    const mr = entities.find((e) => e.id === "global.multi-regional")!;
    expect(mr.parent_id).toBe("global");
    const ottoman = entities.find((e) => e.id === "global.multi-regional.ottoman")!;
    expect(ottoman.parent_id).toBe("global.multi-regional");
    for (const r of ["west-asia.anatolia", "africa.nile"]) {
      expect(ottoman.cross_parent_ids, `Ottomans reachable from ${r}`).toContain(r);
    }
    // The reach is inherited: cross-linking the empire carries its reigns, so
    // Suleiman spans three regions without his entity being touched.
    const suleiman = entities.find((e) => e.id === "global.multi-regional.ottoman.suleiman")!;
    expect(suleiman.regions).toEqual(["africa", "europe", "west-asia"]);
    const strays = ["ww1", "ww2", "cold-war", "black-death", "axial-age", "bronze-collapse"];
    for (const s of strays) {
      expect(
        entities.find((e) => e.id === `cross-regional.${s}`),
        `${s} is not an empire and should not be filed as one`,
      ).toBeUndefined();
    }
    // ...and they must have landed somewhere, not vanished.
    for (const id of [
      "global.short-20c.ww1",
      "global.short-20c.cold-war",
      "global.middle-ages.black-death",
      "global.classical-antiquity.axial-age",
    ]) {
      expect(entities.find((e) => e.id === id), `${id} exists`).toBeDefined();
    }
    // Empires are cross-linked from their region of origin, never moved: the
    // Mongols are Central Asian and also cross-regional, and the breadcrumb
    // that says where a polity came from is worth keeping.
    const mongols = entities.find((e) => e.id === "central-asia.mongol-empire")!;
    expect(mongols.parent_id).toBe("central-asia");
    expect(mongols.cross_parent_ids).toContain("global.multi-regional");
  });

  it("has a label for every source kind actually present", () => {
    // Three separate notions of "source kind" had drifted apart -- the union in
    // chrono/year.ts, the one in dataset/dataset.ts, and the label map in
    // main.ts -- and none of them matched the data. Eleven primary and press
    // sources rendered their badge as "UNDEFINED" for several releases. A
    // TypeScript Record cannot catch this, because it checks the union, not
    // the JSON. This does.
    const labelled = new Set([
      "scholarly", "reference", "institutional", "news", "primary", "press",
    ]);
    const present = new Set(sources.map((s) => s.kind));
    for (const k of present) {
      expect(labelled.has(k), `source kind "${k}" has no display label`).toBe(true);
    }
  });

  it("does not cram two names into one display name", () => {
    // "Haudenosaunee (Iroquois)", "Iran / Persia", "Habsburg /
    // Austria-Hungary" and "North Africa (Maghreb)" were all one workaround: a
    // second name with nowhere to live. name_forms is where it lives now.
    //
    // Deliberately a named list rather than a pattern. A parenthetical is not
    // reliably a second name -- "Chalcolithic (Anatolia)" is the only thing
    // separating five sibling entities, and "BCE (Before Common Era)" is a
    // gloss. Telling those apart from "Paleolithic (Old Stone Age)" needs
    // judgement, so the test guards the specific regressions instead of
    // pretending to a rule it cannot apply.
    const fixed: Record<string, string> = {
      "west-asia.iran": "Iran",
      "europe.central.habsburg-monarchy": "The Habsburg Monarchy",
      "africa.north": "North Africa",
      "global.paleolithic": "Paleolithic",
      "global.neolithic": "Neolithic",
      "americas.north.haudenosaunee": "Haudenosaunee Confederacy",
      "americas.north.ancestral-puebloan": "Ancestral Puebloan",
    };
    for (const [id, name] of Object.entries(fixed)) {
      const e = entities.find((x) => x.id === id)!;
      expect(e.name, `${id} display name`).toBe(name);
      // The displaced name must survive somewhere findable.
      expect((e.aliases ?? []).length, `${id} kept its other names`).toBeGreaterThan(0);
    }
  });

  it("dates a historical name only when it can cite the change", () => {
    // A `from`/`to` on a name form is a date claim like any other, and this
    // dataset does not ship uncited date claims. Austria-Hungary is recorded
    // with a note and no year for exactly this reason.
    for (const e of entities) {
      for (const f of e.name_forms ?? []) {
        if (f.from === undefined && f.to === undefined) continue;
        if (f.kind !== "historical") continue;
        expect(
          (f.source_ids?.length ?? 0) > 0 || (e.source_ids?.length ?? 0) > 0,
          `${e.id}: "${f.name}" is dated but uncited`,
        ).toBe(true);
      }
    }
  });

  it("keeps every name searchable, including the repudiated ones", () => {
    // "Ancestral Puebloan" is the right name and it had no alias, so a reader
    // arriving with "Anasazi" -- the word in every older book -- got nothing.
    // Correcting a name must never cost findability, so aliases are DERIVED
    // from name_forms at build time and the two cannot drift.
    for (const e of entities) {
      if (e.name_forms === undefined) continue;
      for (const f of e.name_forms) {
        if (f.name === e.name) continue;
        expect(e.aliases ?? [], `${e.id} can be found by "${f.name}"`).toContain(f.name);
      }
    }
    const ap = entities.find((e) => e.id === "americas.north.ancestral-puebloan")!;
    expect(ap.aliases).toContain("Anasazi");
    // ...and the rejected form must still be marked as rejected, not quietly
    // rehabilitated by being searchable.
    expect(ap.name_forms?.find((f) => f.name === "Anasazi")?.kind).toBe("rejected");
  });

  it("does not show the reader the same caveat twice", () => {
    // Rewording an existing caveat rather than replacing it left the Golden
    // Horde displaying two near-identical naming notes. Repeated kinds are
    // legitimate -- Ban Chiang carries two genuinely different misconceptions
    // -- so this compares opening text rather than banning the kind.
    for (const e of entities) {
      const seen = new Map<string, string>();
      for (const c of e.caveats ?? []) {
        const key = `${c.kind}|${c.text.slice(0, 40)}`;
        expect(seen.has(key), `duplicate caveat on ${e.id}: ${c.text.slice(0, 40)}`).toBe(false);
        seen.set(key, c.text);
      }
    }
  });

  it("handles every exonym the same way", () => {
    // 0.18.0.0 renamed the Golden Horde to its endonym while leaving Byzantium
    // -- the identical problem -- named for a city nobody in it invoked. Two
    // matching problems, opposite treatments, same release. The rule now: the
    // display name is what a reader arrives with, the endonym goes in
    // native_name where it renders under the title, and a sourced caveat
    // explains the gap. Neutrality comes from never letting the common name
    // stand alone, not from suppressing it.
    for (const id of [
      "central-asia.mongol-empire.golden-horde",
      "europe.mediterranean.byzantine",
    ]) {
      const e = entities.find((x) => x.id === id)!;
      expect(e.native_name, `${id} shows what it called itself`).toBeTruthy();
      const naming = e.caveats?.find((c) => c.kind === "naming-confusion");
      expect(naming, `${id} explains its exonym`).toBeDefined();
      expect(naming!.source_ids?.length ?? 0).toBeGreaterThan(0);
    }
    // The common names must remain the display names: this is a reference
    // tool, and hiding the term people search for defeats the purpose.
    expect(entities.find((x) => x.id === "central-asia.mongol-empire.golden-horde")!.name)
      .toBe("Golden Horde");
    expect(entities.find((x) => x.id === "europe.mediterranean.byzantine")!.name)
      .toBe("Byzantine Empire");
  });

  it("does not settle a live sovereignty dispute with a bare date", () => {
    // roc was shipped as 1912-1949 with no qualification, which silently
    // adopts the PRC's position over Taiwan's. Unlike an exonym, neither name
    // here is a mistake to correct, so this is contested-existence rather
    // than naming-confusion.
    const roc = entities.find((e) => e.id === "east-asia.china.roc")!;
    expect(roc.caveats?.some((c) => c.kind === "contested-existence")).toBe(true);
    // Bounds were standing in for "this date is qualified", and that was the wrong instrument.
    // 1912 is a documentary date -- the Republic was proclaimed on a known day -- so uncertainty
    // bounds would assert doubt about WHEN rather than about sovereignty. The dispute belongs in
    // `alternatives`, which is what the assertions below check.
    // Both governments' positions must be present, each with a source.
    expect((roc.alternatives ?? []).length).toBeGreaterThanOrEqual(2);
    for (const a of roc.alternatives ?? []) {
      expect(a.source_ids?.length ?? 0, `${a.label} is sourced`).toBeGreaterThan(0);
    }
  });

  it("files contested names under the name the polity used", () => {
    // The dataset had two mechanisms for names and applied them only to the
    // harmless cases -- Cheops, King Tut, Ozymandias. The hard ones, where the
    // common English name embeds somebody's later claim, had neither an alias
    // nor a caveat. The rule now: file under the endonym where one is
    // recoverable, keep the common name as an alias so search still works, and
    // explain the difference in a sourced caveat.
    const h = entities.find((e) => e.id === "central-asia.mongol-empire.golden-horde")!;
    expect(h.name).toBe("Golden Horde");
    // Findability must survive the rename, or this is a regression for every
    // reader who only knows the common name.
    expect(h.aliases).toContain("Ulus of Jochi");
    const naming = h.caveats?.find((c) => c.kind === "naming-confusion");
    expect(naming).toBeDefined();
    expect(naming!.source_ids?.length ?? 0).toBeGreaterThan(0);
  });

  it("does not present the Mesolithic as a settled global category", () => {
    // This was the widest childless era for six passes. The content was never
    // missing -- Maglemose, Kongemose, Ertebolle and the rest live under
    // European prehistory, where the term has content. What is actually at
    // issue is whether the GLOBAL category exists at all, so the node carries
    // the argument instead of pretending to contain the world.
    const m = entities.find((e) => e.id === "global.mesolithic")!;
    expect(m.date_standing).toBe("minority");
    expect((m.source_ids ?? []).length).toBeGreaterThan(0);
    expect(m.caveats?.some((c) => c.kind === "contested-existence")).toBe(true);
    // Regional alternatives must be named, or the entity is still Eurocentric
    // while claiming not to be.
    for (const term of ["Later Stone Age", "Archaic", "Epipalaeolithic"]) {
      expect(m.date_note, `names ${term}`).toContain(term);
    }
  });

  it("does not treat a received date as scientifically dated", () => {
    // isScientificDating() keys off the method, so `received` has to sit with
    // calendar and unknown or the app would claim Rome's 753 BCE was measured.
    const rome = entities.find((e) => e.id === "europe.mediterranean.rome.kingdom")!;
    expect(rome.start_dating_method).toBe("received");
    expect(isScientificDating(datingOf(rome).start!.primary.value)).toBe(false);
  });

  it("keeps Kelteminar off the traditional list, because it has a citation", () => {
    // Different case: a peer-reviewed source does give it a millennium-scale
    // range. Thin, but sourced — so it is a minority claim, not a convention.
    const k = entities.find((e) => e.id === "central-asia.prehistory.kelteminar")!;
    expect(k.date_standing).toBe("minority");
    // Was precision "millennium", then explicit bounds a millennium wide. Those bounds were
    // symmetric and indistinguishable from the generator's output, so what remains is the
    // standing and the source -- which is what made this a minority claim rather than a
    // convention in the first place.
    expect(k.source_ids?.length).toBeGreaterThan(0);
  });

  it("keeps three rival Seima-Turbino chronologies apart", () => {
    const st = entities.find((e) => e.id === "central-asia.prehistory.seima-turbino")!;
    expect(st.alternatives?.length).toBe(2);
    expect(st.alternatives?.some((a) => a.standing === "superseded")).toBe(true);
  });

  it("records that the Tarim mummies were not migrants", () => {
    const t = entities.find((e) => e.id === "central-asia.prehistory.tarim-mummies")!;
    expect(t.caveats?.[0]?.kind).toBe("misconception");
    expect(t.caveats?.[0]?.text).toMatch(/Not migrants/);
  });

  it("gives the Austronesian expansion its stages", () => {
    const kids = entities.filter(
      (e) => e.parent_id === "southeast-asia.prehistory.austronesian-expansion",
    );
    expect(kids.length).toBeGreaterThanOrEqual(3);
  });

  it("gives Ban Chiang the bronze controversy it is famous for", () => {
    const bc = entities.find((e) => e.id === "southeast-asia.prehistory.ban-chiang")!;
    // The 1976 world's-earliest-bronze claim, and the long chronology that is
    // still argued for, must both be visible.
    expect(bc.alternatives?.some((a) => a.standing === "superseded")).toBe(true);
    expect(bc.alternatives?.some((a) => a.standing === "minority")).toBe(true);
    expect(bc.caveats?.some((c) => /world's earliest bronze/.test(c.text))).toBe(true);
  });

  it("does not assert the same rival claim twice", () => {
    // Enriching an existing entity re-added a superseded 3600 BCE Ban Chiang
    // chronology it already carried, so the panel showed the same claim twice
    // at the same date.
    for (const e of entities) {
      const alts = e.alternatives ?? [];
      const keys = alts.map((a) => `${a.standing}|${a.start_year ?? ""}|${a.end_year ?? ""}`);
      expect(new Set(keys).size, `duplicate alternative on ${e.id}`).toBe(keys.length);
    }
  });

  it("marks Lapita's own start as unresolved", () => {
    const l = entities.find((e) => e.id === "oceania.melanesia.lapita")!;
    // The unresolved start is carried by two rival readings and a majority standing rather than
    // by a window, the window having been generated rather than sourced.
    expect(l.date_standing).toBe("majority");
    expect(l.alternatives?.length).toBe(2);
  });
});

describe("typed relations", () => {
  // These were authored and schema-checked for several releases while reaching no
  // part of the interface. Now that they render, they are worth asserting.
  it("every link points at an entity that exists", () => {
    const ids = new Set(entities.map((e) => e.id));
    const broken = entities.flatMap((e) =>
      (e.links ?? [])
        .filter((l) => !ids.has(l.entity_id))
        .map((l) => `${e.id} -> ${l.entity_id}`),
    );
    expect(broken).toEqual([]);
  });

  it("records rival claims on both sides", () => {
    // Symmetric by meaning: if the Fatimids contested the caliphate with the
    // Abbasids, the Abbasids were in the same contest. One-sided would make the
    // readout depend on which entity the reader opened.
    const rivals = new Set<string>();
    for (const e of entities) {
      for (const l of e.links ?? []) {
        if (l.type === "rival_claimant_to") rivals.add(`${e.id}|${l.entity_id}`);
      }
    }
    const oneSided = [...rivals].filter((k) => {
      const [a, b] = k.split("|");
      return !rivals.has(`${b}|${a}`);
    });
    expect(oneSided).toEqual([]);
    expect(rivals.size).toBeGreaterThanOrEqual(8);
  });

  it("marks the caliphates as contested rather than successive", () => {
    // The four caliphates read as a clean succession in the column, because the
    // Fatimids are listed after the Abbasids. They overlapped by 262 years.
    const abbasid = entities.find((e) => e.id === "global.multi-regional.abbasid");
    const fatimid = entities.find((e) => e.id === "global.multi-regional.fatimid");
    expect(abbasid).toBeDefined();
    expect(fatimid).toBeDefined();
    expect(
      abbasid!.links?.some(
        (l) =>
          l.type === "rival_claimant_to" &&
          l.entity_id === "global.multi-regional.fatimid",
      ),
    ).toBe(true);
    // The overlap is the point, so assert it is real.
    expect(fatimid!.start_year!).toBeLessThan(abbasid!.end_year!);
  });

  it("authors the Trinh and Nguyen lords as simultaneous, not successive", () => {
    const trinh = entities.find((e) => e.id === "southeast-asia.mainland.trinh");
    const nguyen = entities.find(
      (e) => e.id === "southeast-asia.mainland.nguyen-lords",
    );
    expect(trinh).toBeDefined();
    expect(nguyen).toBeDefined();
    // Same nominal sovereign, and at war with each other.
    expect(trinh!.parent_id).toBe(nguyen!.parent_id);
    expect(trinh!.start_year!).toBeLessThan(nguyen!.end_year!);
    // Distinct from the later Nguyen Dynasty, which took the throne outright.
    expect(nguyen!.id).not.toBe("southeast-asia.mainland.nguyen");
  });
});

describe("homograph disambiguation", () => {
  // Romanisation collapses distinct kanji into one Latin string: Shōwa 1926 is
  // 昭和 and Shōwa 1312 is 正和. Search rendered two identical rows separated
  // only by dates. Screenshot found it; no test would have.
  it("gives every colliding display name a distinguishing native form", () => {
    const byName = new Map<string, Entity[]>();
    for (const e of entities) {
      const list = byName.get(e.name) ?? [];
      list.push(e);
      byName.set(e.name, list);
    }
    for (const [name, list] of byName) {
      if (list.length < 2) continue;
      // Region-vs-process pairs (Mesoamerica, Andes) are disambiguated by their
      // position in the tree, which the reader can see. Era homographs are not.
      const eras = list.filter((e) => e.id.includes(".japan."));
      if (eras.length >= 2) {
        // Japanese eras: distinct kanji flattened by romanisation, so the native
        // form must be present and must differ.
        const forms = new Set(eras.map((e) => e.native_name));
        expect(forms.has(undefined), `${name} needs kanji to be told apart`).toBe(false);
        expect(forms.size, `${name} native forms must differ`).toBe(eras.length);
      }
      // Chinese temple names are the SAME characters reused by later dynasties,
      // so no native form can separate them -- the parent chain must.
      const han = list.filter((e) => e.id.includes(".china."));
      if (han.length >= 2) {
        expect(new Set(han.map((e) => e.parent_id)).size, `${name} needs distinct dynasties`)
          .toBe(han.length);
      }
    }
  });
});

describe("themes", () => {
  // 121 curated memberships existed for several releases with no UI. An audit that
  // checked only `entity.themes` called the feature empty; membership is on the theme.
  it("resolves every theme membership to a real entity", () => {
    const ids = new Set(entities.map((e) => e.id));
    const broken = themes.flatMap((t) =>
      t.entity_ids.filter((id) => !ids.has(id)).map((id) => `${t.id} -> ${id}`),
    );
    expect(broken).toEqual([]);
  });

  it("keeps every theme non-empty and named", () => {
    expect(themes.length).toBe(16);
    for (const t of themes) {
      expect(t.entity_ids.length).toBeGreaterThan(0);
      expect(t.name.trim()).not.toBe("");
    }
    const total = themes.reduce((n, t) => n + t.entity_ids.length, 0);
    expect(total).toBeGreaterThanOrEqual(121);
  });
});

describe("the Essentials view", () => {
  // foundational = "Essentials" in the UI. It is meant to be the clean overview and
  // was the most broken of the three tiers: three of ten regions were absent from it
  // entirely, so 65 Southeast Asian and 56 Central Asian entities were unreachable.
  it("shows every top-level region", () => {
    const roots = entities.filter((e) => e.parent_id === null);
    const hidden = roots.filter((e) => e.tier !== "foundational").map((e) => e.id);
    expect(hidden).toEqual([]);
    expect(roots.length).toBe(10);
  });

  it("does not strand a foundational entity under a hidden parent", () => {
    // A child cannot be reached by drilling if its parent is filtered out. This is
    // scoped to shallow depths, where unreachability is most damaging; the deeper
    // inversions (famous pharaohs under bookkeeping dynasties) are tracked separately.
    const byId = new Map(entities.map((e) => [e.id, e]));
    const depth = (e: Entity): number => {
      let n = 0;
      let cur = e;
      while (cur.parent_id !== null) {
        cur = byId.get(cur.parent_id)!;
        n += 1;
      }
      return n;
    };
    const stranded = entities
      .filter((e) => e.tier === "foundational" && depth(e) <= 2)
      .filter((e) => {
        const p = e.parent_id === null ? null : byId.get(e.parent_id);
        return p !== null && p !== undefined && p.tier !== "foundational";
      })
      .map((e) => `${e.id} under ${e.parent_id}`);
    expect(stranded).toEqual([]);
  });
});

describe("search", () => {
  // Reported from use: searching "Rome" returned "Domestication of the Dromedary" and none
  // of Rome's rulers, and "rulers of rome" returned nothing at all.
  it("does not match inside a word", () => {
    // Fold "dromedary" and the letters r-o-m-e sit in the middle of it.
    const hits = searchEntities(entities, "Rome").map((e) => e.name);
    expect(hits.some((n) => /dromedar/i.test(n))).toBe(false);
    expect(hits).toContain("Ancient Rome");
  });

  it("reaches descendants through an ancestor's name", () => {
    // The emperors' own names contain nothing resembling "Rome".
    const hits = searchEntities(entities, "Rome").map((e) => e.id);
    expect(hits).toContain("europe.mediterranean.rome");
    expect(hits.some((id) => id.startsWith("europe.mediterranean.rome.empire."))).toBe(true);
    // The city of Rome now takes first place, on an exact whole-name match, and that is the right
    // answer: someone typing "Rome" may well want the city. What matters is that the civilisation
    // and its rulers are reachable in the same result set, which was the original complaint.
    expect(hits[0]).toBe("europe.city-rome");
    expect(hits.slice(0, 4)).toContain("europe.mediterranean.rome");
  });

  it("answers a multi-word query instead of returning nothing", () => {
    const hits = searchEntities(entities, "rulers of rome").map((e) => e.id);
    expect(hits.length).toBeGreaterThan(5);
    expect(hits[0]).toBe("europe.mediterranean.rome");
  });

  it("ignores function words that appear inside real names", () => {
    // "of" alone would otherwise rank "Controlled Use of Fire" and "The Drowning of
    // Doggerland" above anything Roman.
    const hits = searchEntities(entities, "rulers of rome").map((e) => e.name).slice(0, 5);
    expect(hits.some((n) => /Doggerland|Controlled Use of Fire/.test(n))).toBe(false);
  });

  it("ranks entities matching more of the query higher", () => {
    const hits = searchEntities(entities, "tang emperor").map((e) => e.id);
    expect(hits[0] ?? "").toMatch(/^east-asia\.china\.tang/);
  });

  it("still disambiguates identical romanisations", () => {
    // Two distinct Japanese eras romanise to Showa; the native form separates them.
    const hits = searchEntities(entities, "Showa");
    expect(hits.length).toBeGreaterThanOrEqual(2);
    const natives = new Set(hits.map((e) => e.native_name));
    expect(natives.size).toBeGreaterThanOrEqual(2);
  });
});

describe("identity", () => {
  // Issue #40: ids were being guessed because they were not predictable. Within one dynasty
  // Thutmose III sat at `thutmose3` while Thutmose I, II and IV sat at `thutmose-i`,
  // `thutmose-ii` and `thutmose-iv`.
  it("uses Roman regnal numerals in every slug", () => {
    const offenders = entities
      .filter((e) => {
        // An event's numerals are dates, not regnal numbers. "September 11 Attacks" was rewritten
        // to `september-xi` before this exclusion existed, and the earlier guard -- that the slug
        // stem must be the name's first word -- could not catch it, because here it is.
        if (e.kind === "event") return false;
        const slug = e.id.split(".").pop()!;
        const m = /^([a-z][a-z-]*?)-?(\d{1,2})$/.exec(slug);
        if (m === null || Number(m[2]) === 0) return false;
        const first = (e.name.split(" ")[0] ?? "")
          .normalize("NFD")
          .replace(/[\u0300-\u036f]/g, "")
          .toLowerCase()
          .replace(/[^a-z0-9]/g, "");
        return first === m[1]!.replace(/-/g, "");
      })
      .map((e) => e.id);
    expect(offenders).toEqual([]);
  });

  it("publishes a redirect for every id it renamed", () => {
    const redirects = (entitiesFile as { redirects?: Record<string, string> }).redirects ?? {};
    expect(Object.keys(redirects).length).toBeGreaterThanOrEqual(40);
    const ids = new Set(entities.map((e) => e.id));
    // Every redirect must point at something that exists, or a stale link resolves to nothing
    // twice over.
    for (const [from, to] of Object.entries(redirects)) {
      expect(ids.has(to), `${from} -> ${to} resolves`).toBe(true);
      expect(ids.has(from), `${from} is genuinely gone`).toBe(false);
    }
  });

  it("resolves a stale id through the redirect map", () => {
    const idx = buildIndex(entities, new Map(Object.entries(
      (entitiesFile as { redirects?: Record<string, string> }).redirects ?? {},
    )));
    // The id this project actually guessed wrong.
    const viaOld = lookup(idx, "africa.nile.egypt.new-kingdom.dyn18.thutmose3");
    expect(viaOld?.name).toBe("Thutmose III");
  });

  it("gives no two siblings the same name or slug", () => {
    const byParent = new Map<string, Entity[]>();
    for (const e of entities) {
      const key = e.parent_id ?? "(root)";
      byParent.set(key, [...(byParent.get(key) ?? []), e]);
    }
    for (const [parent, kids] of byParent) {
      const names = kids.map((k) => k.name);
      const slugs = kids.map((k) => k.id.split(".").pop()!);
      expect(new Set(names).size, `${parent} sibling names`).toBe(names.length);
      expect(new Set(slugs).size, `${parent} sibling slugs`).toBe(slugs.length);
    }
  });

  it("qualifies display names that collide elsewhere in the tree", () => {
    // Not siblings, so no id collides and the tree reads correctly in place -- but a search
    // result shown out of context would be ambiguous. Two different places called Andes.
    const counts = new Map<string, number>();
    for (const e of entities) counts.set(e.name, (counts.get(e.name) ?? 0) + 1);
    for (const e of entities) {
      if ((counts.get(e.name) ?? 0) > 1) {
        expect(e.qualified_name, `${e.id} is qualified`).toBeDefined();
        expect(e.qualified_name).not.toBe(e.name);
      }
    }
  });

  it("can find the Roman Empire by its adjectival form", () => {
    // "Rome" and "Roman" are the same referent in different grammatical forms, and having
    // nowhere to say so was half the cause of the reported search failure.
    const hits = searchEntities(entities, "Roman").map((e) => e.id);
    expect(hits).toContain("europe.mediterranean.rome.empire");
  });
});

describe("the before-and-after graph", () => {
  const linkIndex = new Map(entities.map((e) => [e.id, e]));
  // `links` was populated on 15 of 1,765 entities while the application's stated purpose
  // includes "important before and after links".
  it("connects far more than the fifteen entities it started with", () => {
    const linked = entities.filter((e) => (e.links?.length ?? 0) > 0);
    expect(linked.length).toBeGreaterThan(1000);
  });

  it("keeps every reciprocal link symmetric", () => {
    const inverses: Record<string, string> = {
      preceded_by: "succeeded_by",
      succeeded_by: "preceded_by",
      part_of: "contains",
      contains: "part_of",
      descended_from: "ancestor_of",
      ancestor_of: "descended_from",
      co_ruler_with: "co_ruler_with",
      rival_claimant_to: "rival_claimant_to",
    };
    for (const e of entities) {
      for (const l of e.links ?? []) {
        const inverse = inverses[l.type];
        if (inverse === undefined) continue;
        const target = linkIndex.get(l.entity_id);
        expect(target, `${e.id} links to ${l.entity_id}`).toBeDefined();
        const back = (target!.links ?? []).some(
          (b: { type: string; entity_id: string }) => b.type === inverse && b.entity_id === e.id,
        );
        expect(back, `${e.id} --${l.type}--> ${l.entity_id} needs ${inverse} back`).toBe(true);
      }
    }
  });

  it("says a derived succession is derived", () => {
    // A reader has to be able to tell a researched claim from a structural one. If both look
    // the same, the structural ones quietly acquire the authority of the researched ones.
    const thutmose = linkIndex.get("africa.nile.egypt.new-kingdom.dyn18.thutmose-iii")!;
    const next = thutmose.links?.find((l) => l.type === "succeeded_by");
    expect(next?.entity_id).toContain("amenhotep-ii");
    // `derived` rather than a note. Writing the explanation onto every link repeated one
    // sentence eight hundred times and cost 36 kB gzipped; the UI explains it once.
    expect(next?.derived).toBe("sequence");
  });

  it("does not claim one culture succeeded another as a state", () => {
    // Coverage is not continuity. Chronological ordering between periods is a weaker claim
    // than political succession, and the note must not overstate it.
    for (const e of entities) {
      if (e.kind !== "period" && e.kind !== "era") continue;
      for (const l of e.links ?? []) {
        if (l.type !== "succeeded_by" || l.derived === undefined) continue;
        // Periods and eras get `chronology`, never `sequence`: ordering between cultures is a
        // weaker claim than succession between rulers, and the flag has to say which.
        expect(l.derived, `${e.id} -> ${l.entity_id}`).toBe("chronology");
      }
    }
  });

  it("refuses to bridge a gap too large to be a handover", () => {
    // Interregna and rounded dates are real; a century is not a handover. Any derived
    // succession must abut within tolerance.
    for (const e of entities) {
      for (const l of e.links ?? []) {
        if (l.type !== "succeeded_by" || l.derived === undefined) continue;
        const target = linkIndex.get(l.entity_id)!;
        if (e.end_year === null || target.start_year === null) continue;
        // Tolerance scales with span, as the deriver's does: two thousand years between two
        // million-year industries is abutment, the same gap between two reigns is not.
        const span = Math.max(
          Math.abs((e.end_year ?? e.start_year!) - e.start_year!),
          Math.abs((target.end_year ?? target.start_year!) - target.start_year!),
        );
        const allowed = Math.max(25, Math.floor(span * 0.01));
        const gap = target.start_year - e.end_year;
        expect(gap, `${e.id} -> ${target.id} gap`).toBeLessThanOrEqual(allowed);
        expect(gap, `${e.id} -> ${target.id} overlap`).toBeGreaterThanOrEqual(-allowed);
      }
    }
  });
});

describe("historicity", () => {
  // The axis `date_standing` could not carry. Before this, Dangun and Hammurabi were reported
  // identically on the question of whether the subject existed.
  it("grades the topic independently of the dating", () => {
    const dangun = entities.find((e) => e.id === "east-asia.korea.gojoseon.dangun")!;
    // A precise, genuine dating convention about a person who very likely never lived.
    expect(dangun.historicity).toBe("mythological");
    expect(dangun.date_standing).toBe("traditional");
    expect(dangun.start_dating_method).toBe("received");

    const hammurabi = entities.find(
      (e) => e.id === "west-asia.mesopotamia.old-babylonian.hammurabi",
    )!;
    // Existence not in question; the dates are, because rival Mesopotamian chronologies
    // disagree by more than a century.
    expect(hammurabi.historicity).toBeUndefined();
    expect((hammurabi.alternatives?.length ?? 0) > 0).toBe(true);
  });

  it("separates the legendary from the mythological", () => {
    // Rome's kings are handed down AS history and doubted; Fuxi is described in the sources
    // themselves as a god-king. Collapsing the two loses the distinction that matters.
    const romulus = entities.find(
      (e) => e.id === "europe.mediterranean.rome.kingdom.romulus",
    )!;
    expect(romulus.historicity).toBe("legendary");
    const fuxi = entities.find((e) => e.id === "east-asia.china.legendary.fuxi")!;
    expect(fuxi.historicity).toBe("mythological");
  });

  it("marks the Xia contested rather than legendary", () => {
    // Specialists actively disagree, which is a different state from tradition-versus-doubt:
    // the Xia-Shang-Zhou Chronology Project dates it while Cambridge starts at the Shang.
    const xia = entities.find((e) => e.id === "east-asia.china.xia")!;
    expect(xia.historicity).toBe("contested");
  });

  it("leaves the accepted majority unmarked", () => {
    // Saying "accepted" on 1,700 entities would be noise, so the default is silence.
    const graded = entities.filter((e) => e.historicity !== undefined);
    expect(graded.length).toBeGreaterThan(25);
    expect(graded.length).toBeLessThan(200);
  });

  it("uses no placeholder text as content", () => {
    // Eleven entities shipped with a contested-existence caveat whose entire text was "omit",
    // imported from a research file where the writer typed the instruction into the field.
    // Cicero and Pompey were told to the reader as figures of doubtful existence.
    const sentinels = new Set(["omit", "none", "n/a", "tbd", "todo", "null", "-", "unknown"]);
    for (const e of entities) {
      for (const c of e.caveats ?? []) {
        expect(sentinels.has(c.text.trim().toLowerCase()), `${e.id}: ${c.text}`).toBe(false);
        expect(c.text.trim().length, `${e.id} caveat length`).toBeGreaterThan(11);
      }
    }
  });

  it("finds Romulus the king before Romulus Augustulus", () => {
    // An exact whole-name match must beat matching one word of a longer name, or the founder
    // of Rome comes second to the man who lost it because the emperor sits at a higher tier.
    const hits = searchEntities(entities, "Romulus").map((e) => e.id);
    expect(hits[0]).toBe("europe.mediterranean.rome.kingdom.romulus");
  });
});

describe("the new kinds", () => {
  // The audit found whole categories absent: not one religion existed as an entity, no trade
  // network did, and 39% of the dataset was individual reigns, which cannot represent a society
  // without kings.
  it("holds all five new kinds", () => {
    for (const kind of ["language", "tradition", "people", "network", "person"]) {
      const of = entities.filter((e) => e.kind === kind);
      expect(of.length, `${kind} entities`).toBeGreaterThan(5);
    }
  });

  it("files languages by descent, not geography", () => {
    // parent_id means linguistic ancestor here. Akkadian's parent is Proto-Semitic, not
    // Mesopotamia -- and ids stay flat so re-subgrouping a family never changes identity.
    const akkadian = entities.find((e) => e.id === "global.languages.akkadian")!;
    expect(akkadian.parent_id).toBe("global.languages.proto-semitic");
    const semitic = entities.find((e) => e.id === "global.languages.proto-semitic")!;
    expect(semitic.parent_id).toBe("global.languages.proto-afroasiatic");
  });

  it("marks proto-languages reconstructed, not doubtful", () => {
    // A reconstructed proto-language is known by inference, which is a different claim from a
    // contested one. Nobody doubts Proto-Indo-European; nobody has heard it either.
    for (const e of entities.filter((x) => x.kind === "language")) {
      if (!e.name.startsWith("Proto-")) continue;
      expect(e.historicity, `${e.id}`).toBe("reconstructed");
      expect(e.start_dating_method, `${e.id}`).toBe("glottochronology");
    }
  });

  it("does not give a living tradition an end year", () => {
    for (const e of entities.filter((x) => x.kind === "tradition")) {
      if (e.end_year !== null) continue;
      expect(e.extant, `${e.id} says it continues`).toBe(true);
    }
  });

  it("requires a network to name the regions it crossed", () => {
    // A network is not in a region, which is the point of the kind; but it has to say which
    // ones it connected or it is untethered.
    for (const e of entities.filter((x) => x.kind === "network")) {
      expect((e.regions ?? []).length, `${e.id} names its regions`).toBeGreaterThan(0);
    }
  });

  it("stops filing cities as periods", () => {
    // Byblos and Tyre were `era`, Tenochtitlan was `period`. A period ends; Damascus does not.
    for (const id of [
      "west-asia.mesopotamia.phoenicia.byblos",
      "west-asia.mesopotamia.phoenicia.tyre",
      "americas.mesoamerica.aztec.tenochtitlan",
    ]) {
      expect(entities.find((e) => e.id === id)?.kind, id).toBe("city");
    }
  });

  it("carries thresholds past 1650 BCE", () => {
    // The kind existed and stopped dead at the domestic chicken, so the dataset held the first
    // controlled fire but not iron, the alphabet, or the transistor.
    const late = entities.filter((e) => e.kind === "threshold" && (e.start_year ?? 0) > -1650);
    expect(late.length).toBeGreaterThan(15);
    const transistor = entities.find((e) => e.id === "global.milestones.transistor")!;
    expect(transistor.kind).toBe("threshold");
    expect(transistor.end_year).toBeNull();
  });

  it("renders a religion in calendar years, not Before Present", () => {
    // Buddhism read as "2,399 BP - present" because its dating method was classed as
    // scientific. BP is a frame built for geology; the test is whether a method yields an
    // absolute calendar year, which first attestation does.
    const buddhism = entities.find((e) => e.id === "global.traditions.buddhism")!;
    expect(displayRange(buddhism).frame).toBe("calendar");
  });
});

describe("search phrases", () => {
  it("gives a bare era name the domain it needs", () => {
    // `Wadō` appears once in the dataset, so the collision-based generator never flagged it and
    // sent the bare word out as the query. In the world it is a coin, a martial arts style and
    // several companies. `Shōwa` appears twice and therefore did get context -- the rule was
    // measuring ambiguity in this dataset rather than in the world.
    const wado = entities.find((e) => e.name === "Wadō")!;
    expect(wado.search_phrase).toBe("Wadō Japanese era name");
  });

  it("separates two things called Apollo 11", () => {
    // A Moon landing and a cave in Namibia holding some of the oldest figurative art known.
    const cave = entities.find((e) => e.id === "africa.prehistory.apollo-11-cave")!;
    expect(cave.search_phrase).toMatch(/Namibia/);
  });

  it("adds no phrase where the name is already the best query", () => {
    // A search_phrase that restates the name is another field to keep in sync for no gain.
    for (const id of [
      "global.networks.silk-road",
      "global.languages.proto-semitic",
      "europe.mediterranean.rome.empire.hadrian",
    ]) {
      expect(entities.find((e) => e.id === id)?.search_phrase, id).toBeUndefined();
    }
  });

  it("never restates the name verbatim as the phrase", () => {
    for (const e of entities) {
      if (e.search_phrase === undefined) continue;
      // Longer was the wrong proxy: the legendary age of China is named "Legendary Age (Three
      // Sovereigns and Five Emperors)" and its phrase drops the framing to search the figures
      // themselves, which is shorter and better. What matters is that it is not a restatement.
      expect(e.search_phrase, `${e.id}`).not.toBe(e.name);
      expect(e.search_phrase.trim().length, `${e.id}`).toBeGreaterThan(3);
    }
  });

  it("prefers an authored phrase over the generated one", () => {
    const idx = buildIndex(entities);
    const dangun = entities.find((e) => e.id === "east-asia.korea.gojoseon.dangun")!;
    expect(searchQuery(dangun, idx)).toBe(dangun.search_phrase);
  });
});

describe("polity, era and culture", () => {
  const find = (id: string) => entities.find((e) => e.id === id)!;

  it("separates a state from a label for a span of time", () => {
    // The Roman Republic had consuls, armies and taxes; the Stone Age had none of those because
    // it is not that sort of thing.
    for (const id of [
      "europe.mediterranean.rome.kingdom",
      "europe.mediterranean.rome.republic",
      "europe.mediterranean.rome.empire",
      "europe.central.hre",
      "east-asia.china.tang",
    ]) {
      expect(find(id).kind, id).toBe("polity");
    }
    for (const id of ["global.bronze-age", "global.iron-age", "global.paleolithic"]) {
      expect(find(id).kind, id).toBe("era");
    }
  });

  it("keeps the two senses of Roman Empire apart", () => {
    // "Roman Empire" means both a state and the whole Roman epoch, as in Gibbon's title. Both
    // senses are real, so both get an entity rather than one being declared correct.
    expect(find("europe.mediterranean.rome").kind).toBe("era");
    expect(find("europe.mediterranean.rome.empire").kind).toBe("polity");
    const caveat = find("europe.mediterranean.rome.empire").caveats?.find(
      (c) => c.kind === "naming-confusion",
    );
    expect(caveat?.text).toMatch(/epoch/i);
  });

  it("does not promote a periodisation that happens to have rulers", () => {
    // Japan's Kamakura and Muromachi Periods have shoguns beneath them and were promoted by a
    // reigns test. They are labels for a span named after where a regime sat; the regime is the
    // shogunate. Egypt's Old, Middle and New Kingdoms are the same case.
    for (const id of [
      "east-asia.japan.kamakura",
      "africa.nile.egypt.old-kingdom",
      "africa.nile.egypt.new-kingdom",
      "east-asia.china.three-kingdoms",
    ]) {
      expect(find(id).kind, id).toBe("era");
    }
  });

  it("claims no government for an archaeological culture", () => {
    // Calling the Olmec a polity asserts a state nobody has demonstrated; calling them an era says
    // they were a span of time.
    for (const id of [
      "americas.mesoamerica.olmec",
      "americas.andes.chavin",
      "oceania.melanesia.lapita",
      "south-asia.indus",
    ]) {
      expect(find(id).kind, id).toBe("culture");
    }
  });

  it("treats the Sea Peoples as a contested culture, not a people", () => {
    // `people` asserts one coherent ethnolinguistic group. The Sea Peoples are a name Egyptian
    // scribes gave to raiders of several origins, and whether they were one phenomenon at all is
    // the disputed question.
    const sp = find("west-asia.culture-sea-peoples");
    expect(sp.kind).toBe("culture");
    expect(sp.historicity).toBe("contested");
  });
});
