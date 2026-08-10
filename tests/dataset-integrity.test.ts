import { describe, expect, it } from "vitest";
import { calendars, datasetVersion, entities, referenceFrames, schemaVersion, sources, themes } from "../src/dataset/dataset";
import { buildIndex } from "../src/entity/tree";
import { datingOf } from "../src/chrono/fromEntity";
import { isScientificDating } from "../src/chrono/year";

const idx = buildIndex(entities);

describe("dataset envelope", () => {
  it("is v0.5.0.1 on schema 2.0.0", () => {
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
    expect(datasetVersion).toBe("0.26.0.0");
    expect(schemaVersion).toBe("3.4.0");
  });

  it("has the expected collection sizes", () => {
    // The generated corpus includes the historical baseline, the prehistory
    // branch, and the regional prehistory chronology extensions.
    expect(entities.length).toBe(1648);
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
    expect(cited.length).toBe(397);
  });

  it("carries dating methods and uncertainty bounds", () => {
    expect(entities.filter((e) => e.start_dating_method !== undefined).length).toBe(396);
    expect(entities.filter((e) => e.start_year_min !== undefined).length).toBe(26);
  });

  it("dates each boundary on its own evidence", () => {
    // Q-30, resolved in schema 3.0.0. The end is no longer the start's method
    // reused: 82 ends carry a method, and the two that DIFFER from their start
    // are the cases the question was raised about -- a range whose ends rest on
    // different science. The remainder are unset on purpose, because an end
    // beyond radiocarbon's reach was never dated by the start's method and
    // saying otherwise is the exact error the split exists to prevent.
    const withEnd = entities.filter((e) => e.end_dating_method !== undefined);
    expect(withEnd.length).toBe(328);

    const differing = entities
      .filter(
        (e) =>
          e.end_dating_method !== undefined &&
          e.end_dating_method !== e.start_dating_method,
      )
      .map((e) => e.id)
      .sort();
    // Six, and each is a range whose ends genuinely rest on different
    // evidence: Neanderthals (uranium-series in, radiocarbon out), the Middle
    // Stone Age (luminescence in, radiocarbon out), Rising Star (OSL in,
    // US-ESR on teeth out) and Sterkfontein (cosmogenic in, U-Pb out). Under
    // the old single field every one of these was mislabelled at one end.
    //
    // The last three cross the boundary between science and history. Susa's
    // earliest occupation is radiocarbon-dated and its end is Cyrus taking the
    // city in 539 BCE, a calendar date from written record. Phrygia's start
    // comes off the Gordion tree-ring sequence and its end is typological.
    //
    // The Marib Dam runs the other way: its construction is known only from an
    // inscription, while its END is radiocarbon on charcoal in the basin silts,
    // putting the dam's last activity three centuries before the collapse
    // tradition remembers.
    //
    // The clearest cases arrived with the Mediterranean citation pass. Rome and
    // the Republic both begin on `received` dates -- Varro's back-calculations,
    // which the Oxford Classical Dictionary calls artificial manipulation --
    // and end on calendar dates for events that actually happened. One method
    // field would have flattened a legend and a datable event into the same
    // kind of claim, which is the whole reason the field was split.
    expect(differing).toEqual([
      "africa.prehistory.rising-star",
      "africa.prehistory.sterkfontein",
      // Both dug at the start and conquered at the end: the archaeology dates
      // the building, a written date ends it.
      "americas.andes.inca.machu-picchu",
      "americas.mesoamerica.zapotec",
      "europe.mediterranean.greece",
      "europe.mediterranean.rome",
      "europe.mediterranean.rome.republic",
      "europe.prehistory.neanderthal-europe",
      "global.paleolithic.middle-stone-age",
      "west-asia.anatolia.phrygia",
      "west-asia.arabia.pre-islamic.saba.marib-dam",
      "west-asia.iran.elam.susa",
    ]);

    // An end method with no end boundary would describe nothing.
    expect(withEnd.every((e) => e.end_year !== null)).toBe(true);
  });

  it("distinguishes an extant taxon from an undated end", () => {
    // end_year null means "extant" for H. sapiens and "never dated" for
    // H. luzonensis. Conflating them would put a hominin known from foot
    // bones among the living.
    const sapiens = entities.find((e) => e.id === "global.prehistory.hominins.homo-sapiens");
    const luzon = entities.find((e) => e.id === "global.prehistory.hominins.homo-luzonensis");
    expect(sapiens?.end_year).toBeNull();
    expect(sapiens?.end_precision).toBeUndefined();
    expect(luzon?.end_year).toBeNull();
    expect(luzon?.end_precision).toBe("unknown");
  });

  it("has calendar_ids on only 267 entities", () => {
    expect(entities.filter((e) => (e.calendar_ids?.length ?? 0) > 0).length).toBe(267);
  });

  it("still has summaries on only 5 of 42 region nodes", () => {
    const regions = entities.filter((e) => e.kind === "region");
    expect(regions.length).toBe(42);
    expect(regions.filter((e) => e.summary !== undefined).length).toBe(5);
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
    expect(k?.date_precision).toBe("minimum");
    expect(k?.start_year).toBe(-3298051);
  });

  it("gives every threshold a minimum precision and no end", () => {
    const t = entities.filter((e) => e.kind === "threshold");
    expect(t.length).toBeGreaterThanOrEqual(10);
    for (const e of t) {
      expect(e.date_precision).toBe("minimum");
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
    expect(s.date_precision).toBe("disputed");
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
    expect(mv.start_year).toBe(-12551);
    expect(mv.end_year).toBe(-12251);
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
    expect(n.standing).toBe("traditional");
    expect(n.date_precision).toBe("traditional");
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
    for (const e of entities.filter((x) => x.standing === "traditional")) {
      expect(e.date_precision, `${e.id} precision`).toBe("traditional");
      expect(e.start_dating_method, `${e.id} method`).toBe("received");
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
      expect(e.date_precision, `${id} precision`).toBe("disputed");
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
    expect(roc.date_precision).toBe("disputed");
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
    expect(m.standing).toBe("minority");
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
    expect(k.standing).toBe("minority");
    expect(k.date_precision).toBe("millennium");
  });

  it("keeps three rival Seima-Turbino chronologies apart", () => {
    const st = entities.find((e) => e.id === "central-asia.prehistory.seima-turbino")!;
    expect(st.date_precision).toBe("disputed");
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
    expect(l.date_precision).toBe("disputed");
  });
});
