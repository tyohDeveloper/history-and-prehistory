import { describe, expect, it } from "vitest";
import { entities } from "../src/dataset/dataset";
import { buildIndex } from "../src/entity/tree";
import {
  DEFAULT_WEIGHTS,
  degreeOfInterest,
  type DoiContext,
} from "../src/focus/degreeOfInterest";
import { extentOf, intervalGap } from "../src/focus/intervalGap";
import { localGapScale } from "../src/focus/localGapScale";
import { siblingTierScore } from "../src/focus/siblingTierScore";

const index = buildIndex(entities);
const byId = new Map(entities.map((e) => [e.id, e]));
const sortedMidpoints = entities
  .map((e) => extentOf(e))
  .filter((x): x is readonly [number, number] => x !== null)
  .map(([a, b]) => (a + b) / 2)
  .sort((a, b) => a - b);
const ctx: DoiContext = { index, sortedMidpoints, weights: DEFAULT_WEIGHTS };

function ranked(focusId: string, n: number): string[] {
  const focus = byId.get(focusId)!;
  return [...entities]
    .map((x) => [x, degreeOfInterest(ctx, focus, x)] as const)
    .filter(([, s]) => Number.isFinite(s))
    .sort((a, b) => b[1] - a[1])
    .slice(0, n)
    .map(([x]) => x.id);
}

describe("interval gap, not midpoint distance", () => {
  it("treats a child inside its parent as zero distance", () => {
    // A nengō sits wholly inside Heian; their midpoints are ~2 centuries
    // apart. Midpoint distance penalised a node for being contemporaneous
    // with its own parent.
    const heian = byId.get("east-asia.japan.heian")!;
    const kohei = byId.get("east-asia.japan.heian.kohei")!;
    expect(intervalGap(extentOf(heian), extentOf(kohei))).toBe(0);
  });

  it("measures the space between disjoint extents", () => {
    expect(intervalGap([100, 200], [250, 300])).toBe(50);
    expect(intervalGap([250, 300], [100, 200])).toBe(50);
  });

  it("returns null for an undated node", () => {
    expect(intervalGap(null, [1, 2])).toBeNull();
  });
});

describe("distance is density-normalized", () => {
  it("scales by four orders of magnitude across the dataset", () => {
    // The whole reason a years-based radius cannot work.
    const deep = localGapScale(sortedMidpoints, -1_000_000);
    const modern = localGapScale(sortedMidpoints, 1950);
    expect(deep / modern).toBeGreaterThan(1000);
  });
});

describe("tier is ranked among siblings, not globally", () => {
  it("returns neutral when every sibling shares a tier", () => {
    // Heian's 88 children are all `specialist`, so the field carries no local
    // information and must not tilt the result.
    const kids = entities.filter((e) => e.parent_id === "east-asia.japan.heian");
    expect(kids.length).toBeGreaterThan(80);
    expect(new Set(kids.map((k) => k.tier)).size).toBe(1);
    expect(siblingTierScore(kids[0]!, kids)).toBe(0.5);
  });

  it("ranks a foundational sibling above a specialist one", () => {
    const kids = entities.filter((e) => e.parent_id === "east-asia.japan.edo");
    const found = kids.find((k) => k.tier === "foundational")!;
    const spec = kids.find((k) => k.tier === "specialist")!;
    expect(siblingTierScore(found, kids)).toBeGreaterThan(siblingTierScore(spec, kids));
  });
});

describe("the lens selects a sensible neighbourhood", () => {
  it("does not rank the trunk", () => {
    // The first prototype put "East Asia", "Global" and "Europe" above every
    // real neighbour. Undated container nodes are excluded outright.
    const top = ranked("east-asia.japan.heian.kohei", 12);
    expect(top).not.toContain("east-asia");
    expect(top).not.toContain("global");
  });

  it("puts immediate temporal neighbours near the top", () => {
    const top = ranked("east-asia.japan.heian.kohei", 6);
    expect(top).toContain("east-asia.japan.heian.kohei");
    expect(top).toContain("east-asia.japan.heian");
  });

  it("surfaces contemporaries from other branches", () => {
    // The payoff, and the reason Q-8 did not need a detached lens: Miller
    // columns can never show what else was happening at the same time.
    // Focused on a Heian nengō the lens reaches Song China and Goryeo Korea,
    // which sit in sibling branches rather than foreign regions - the first
    // version of this test wrongly looked outside `east-asia` entirely.
    const top = ranked("east-asia.japan.heian.kohei", 45);
    const otherBranch = top.filter((id) => !id.startsWith("east-asia.japan"));
    expect(otherBranch).toContain("east-asia.china.song");
    expect(otherBranch.length).toBeGreaterThanOrEqual(3);
  });

  it("demotes containers that merely swallow the focus", () => {
    // "CE (Common Era)" overlaps a seven-year nengō but is 300x longer.
    const top = ranked("east-asia.japan.heian.kohei", 12);
    expect(top.some((id) => id.includes("common-era"))).toBe(false);
  });

  it("works in deep time, where neighbours are 400,000 years away", () => {
    const top = ranked("global.prehistory.hominins.homo-erectus", 6);
    expect(top).toContain("global.prehistory.hominins");
    expect(top.filter((id) => id.includes("hominins.")).length).toBeGreaterThan(1);
  });
});
