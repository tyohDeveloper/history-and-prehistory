import { describe, expect, it } from "vitest";
import { calendars, datasetVersion, entities, referenceFrames, schemaVersion, themes } from "../src/dataset/dataset";
import { buildIndex } from "../src/entity/tree";

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
    expect(datasetVersion).toBe("0.7.0.0");
    expect(schemaVersion).toBe("3.0.0");
  });

  it("has the expected collection sizes", () => {
    // The generated corpus includes the historical baseline, the prehistory
    // branch, and the regional prehistory chronology extensions.
    expect(entities.length).toBe(1461);
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
    expect(cited.length).toBe(155);
  });

  it("carries dating methods and uncertainty bounds", () => {
    expect(entities.filter((e) => e.start_dating_method !== undefined).length).toBe(163);
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
    expect(withEnd.length).toBe(115);

    const differing = entities
      .filter(
        (e) =>
          e.end_dating_method !== undefined &&
          e.end_dating_method !== e.start_dating_method,
      )
      .map((e) => e.id)
      .sort();
    // Four, and each is a range whose ends genuinely rest on different
    // science: Neanderthals (uranium-series in, radiocarbon out), the Middle
    // Stone Age (luminescence in, radiocarbon out), Rising Star (OSL in,
    // US-ESR on teeth out) and Sterkfontein (cosmogenic in, U-Pb out). Under
    // the old single field every one of these was mislabelled at one end.
    expect(differing).toEqual([
      "africa.prehistory.rising-star",
      "africa.prehistory.sterkfontein",
      "europe.prehistory.neanderthal-europe",
      "global.paleolithic.middle-stone-age",
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

  it("still has summaries on only 6 of 43 region nodes", () => {
    const regions = entities.filter((e) => e.kind === "region");
    expect(regions.length).toBe(43);
    expect(regions.filter((e) => e.summary !== undefined).length).toBe(6);
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
