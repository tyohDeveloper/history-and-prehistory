import { describe, expect, it } from "vitest";
import { calendars, datasetVersion, entities, referenceFrames, schemaVersion, themes } from "../src/lib/dataset";
import { buildIndex } from "../src/lib/tree";

const idx = buildIndex(entities);

describe("dataset envelope", () => {
  it("is the v2.1.0 baseline on schema 1.0.0", () => {
    expect(datasetVersion).toBe("2.1.0");
    expect(schemaVersion).toBe("1.0.0");
  });

  it("has the expected collection sizes", () => {
    expect(entities.length).toBe(1305);
    expect(calendars.length).toBe(21);
    expect(themes.length).toBe(16);
    expect(referenceFrames.length).toBe(37);
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

describe("known v2.1.0 gaps are still gaps", () => {
  // These assertions document the gap-analysis baseline (docs/gap-analysis-v2.1.0.md).
  // They are expected to FAIL when the corresponding gap is closed — at which
  // point update the number here in the same commit that closes it.
  it("has zero entities carrying sources[]", () => {
    expect(entities.filter((e) => (e.sources?.length ?? 0) > 0).length).toBe(0);
  });

  it("has calendar_ids on only 267 entities", () => {
    expect(entities.filter((e) => (e.calendar_ids?.length ?? 0) > 0).length).toBe(267);
  });

  it("has summaries on only 6 of 43 region nodes", () => {
    const regions = entities.filter((e) => e.kind === "region");
    expect(regions.length).toBe(43);
    expect(regions.filter((e) => e.summary !== undefined).length).toBe(6);
  });
});
