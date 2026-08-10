import { describe, expect, it } from "vitest";
import {
  buildIndex,
  childrenOf,
  compareEntities,
  foldForSearch,
  formatRange,
  formatYear,
  pathTo,
  searchEntities,
  visibleAtTier,
} from "../src/entity/tree";
import type { Entity } from "../src/entity/entity";

const mk = (p: Partial<Entity> & Pick<Entity, "id">): Entity => ({
  kind: "era",
  name: p.id,
  parent_id: null,
  start_year: null,
  end_year: null,
  tier: "foundational",
  ...p,
});

describe("buildIndex", () => {
  it("indexes by id and collects roots", () => {
    const idx = buildIndex([mk({ id: "a" }), mk({ id: "b", parent_id: "a" })]);
    expect(idx.byId.size).toBe(2);
    expect(idx.roots.map((e) => e.id)).toEqual(["a"]);
  });

  it("places cross-parented entities under both parents", () => {
    const idx = buildIndex([
      mk({ id: "a" }),
      mk({ id: "b" }),
      mk({ id: "c", parent_id: "a", cross_parent_ids: ["b"] }),
    ]);
    expect(childrenOf(idx, "a").map((e) => e.id)).toEqual(["c"]);
    expect(childrenOf(idx, "b").map((e) => e.id)).toEqual(["c"]);
  });

  it("sorts children chronologically, undated last", () => {
    const idx = buildIndex([
      mk({ id: "p" }),
      mk({ id: "late", parent_id: "p", start_year: 1500 }),
      mk({ id: "undated", parent_id: "p", start_year: null }),
      mk({ id: "early", parent_id: "p", start_year: -500 }),
    ]);
    expect(childrenOf(idx, "p").map((e) => e.id)).toEqual(["early", "late", "undated"]);
  });
});

describe("pathTo", () => {
  it("returns the root-to-node chain", () => {
    const idx = buildIndex([
      mk({ id: "r" }),
      mk({ id: "e", parent_id: "r" }),
      mk({ id: "p", parent_id: "e" }),
    ]);
    expect(pathTo(idx, "p").map((e) => e.id)).toEqual(["r", "e", "p"]);
  });

  it("terminates on a parent cycle rather than hanging", () => {
    const idx = buildIndex([
      mk({ id: "x", parent_id: "y" }),
      mk({ id: "y", parent_id: "x" }),
    ]);
    expect(pathTo(idx, "x").length).toBeLessThanOrEqual(2);
  });
});

describe("visibleAtTier", () => {
  const list = [
    mk({ id: "f", tier: "foundational" }),
    mk({ id: "i", tier: "intermediate" }),
    mk({ id: "s", tier: "specialist" }),
  ];
  it("is cumulative", () => {
    expect(visibleAtTier(list, "foundational").map((e) => e.id)).toEqual(["f"]);
    expect(visibleAtTier(list, "intermediate").map((e) => e.id)).toEqual(["f", "i"]);
    expect(visibleAtTier(list, "specialist").map((e) => e.id)).toEqual(["f", "i", "s"]);
  });
});

describe("foldForSearch", () => {
  it("strips diacritics, case, and separators", () => {
    expect(foldForSearch("J\u014dmon")).toBe("jomon");
    expect(foldForSearch("Ala-ud-din")).toBe("alauddin");
    expect(foldForSearch("Ala-ud-din")).toBe(foldForSearch("Alauddin"));
    expect(foldForSearch("  Meiji  ")).toBe("meiji");
  });
});

describe("searchEntities", () => {
  const list = [
    mk({ id: "1", name: "Meiji", tier: "foundational" }),
    mk({ id: "2", name: "Meiji Restoration", tier: "specialist" }),
    mk({ id: "3", name: "Edo", aliases: ["Tokugawa"] }),
  ];
  it("returns nothing for an empty query", () => {
    expect(searchEntities(list, "   ")).toEqual([]);
  });
  it("ranks exact over prefix", () => {
    expect(searchEntities(list, "meiji")[0]?.id).toBe("1");
  });
  it("matches aliases", () => {
    expect(searchEntities(list, "tokugawa").map((e) => e.id)).toEqual(["3"]);
  });
  it("is diacritic-insensitive", () => {
    expect(searchEntities([mk({ id: "j", name: "J\u014dmon" })], "jomon").length).toBe(1);
  });
});

describe("year formatting", () => {
  it("labels BCE and CE without a year zero, and without separators", () => {
    expect(formatYear(-44)).toBe("44 BCE");
    expect(formatYear(1868)).toBe("1868 CE");
    expect(formatYear(null)).toBe("\u2014");
  });
  it("renders ongoing ranges", () => {
    expect(formatRange(mk({ id: "x", start_year: 2019, end_year: null, extant: true }))).toBe("2019 CE \u2013 present");
  });

  it("prints a point event as one date, not as ongoing", () => {
    // The dataset had no point events until 0.16.0.0, so this path was never
    // exercised and defaulted to the wrong one of the three meanings a missing
    // end year can carry. The Narmer Palette rendered as "5,049 BP - present".
    expect(
      formatRange(mk({ id: "narmer", kind: "event", start_year: -3100, end_year: null })),
    ).toBe("3100 BCE");
    // An era with no end is still ongoing, not a point.
    expect(
      formatRange(mk({ id: "era", kind: "era", start_year: -3100, end_year: null, extant: true })),
    ).toBe("3100 BCE \u2013 present");
  });
});

describe("compareEntities", () => {
  it("breaks ties on name", () => {
    const a = mk({ id: "a", name: "Bbb", start_year: 100 });
    const b = mk({ id: "b", name: "Aaa", start_year: 100 });
    expect(compareEntities(a, b)).toBeGreaterThan(0);
  });
});

describe("an absent end year means two different things", () => {
  // These fixtures now say `extant: true` rather than relying on a null end year. That
  // reliance was the bug: "no end year" was read as "still going", so anything whose end was
  // merely undated was rendered as ongoing.
  it("renders an extant taxon as present", () => {
    expect(formatRange(mk({ id: "sapiens", start_year: -313050, end_year: null, extant: true }))).toContain(
      "present",
    );
  });

  it("renders an undated end as unknown, not present", () => {
    // H. luzonensis certainly ended; the youngest remains have never been
    // dated. "present" would assert it is still walking around.
    expect(
      formatRange(
        mk({ id: "luzonensis", start_year: -132050, end_year: null, extant: undefined }),
      ),
    ).toContain("unknown");
  });
});
