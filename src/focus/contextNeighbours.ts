import { DEFAULT_WEIGHTS, degreeOfInterest, type DoiContext } from "./degreeOfInterest";
import { extentOf } from "./intervalGap";
import { buildIndex, type TreeIndex } from "../entity/tree";
import type { Entity } from "../entity/entity";

export interface Neighbour {
  entity: Entity;
  score: number;
  /** True when the entity sits outside the focus's own branch. */
  elsewhere: boolean;
}

/**
 * The `budget` most interesting entities around a focus.
 *
 * This is what replaces the detail-tier filter (Q-9). A hard tier filter and a
 * soft degree-of-interest over the same variable double-count: a specialist
 * node far from the focus is penalised once for being specialist and again for
 * being distant. Heian shows the cost — a tier filter suppresses all 88 of its
 * nengō uniformly, while the lens still ranks them by time.
 *
 * So the reader sets how much they want on screen and the lens decides where
 * to spend it.
 */
export function contextNeighbours(
  all: readonly Entity[],
  focus: Entity,
  budget: number,
  index?: TreeIndex,
): Neighbour[] {
  const idx = index ?? buildIndex(all);
  const sortedMidpoints = all
    .map((e) => extentOf(e))
    .filter((x): x is readonly [number, number] => x !== null)
    .map(([a, b]) => (a + b) / 2)
    .sort((a, b) => a - b);
  const ctx: DoiContext = { index: idx, sortedMidpoints, weights: DEFAULT_WEIGHTS };
  const branch = focus.parent_id ?? focus.id;

  return all
    .map((entity) => ({
      entity,
      score: degreeOfInterest(ctx, focus, entity),
      elsewhere: !entity.id.startsWith(branch.split(".").slice(0, 2).join(".")),
    }))
    .filter((n) => Number.isFinite(n.score))
    .sort((a, b) => b.score - a.score)
    .slice(0, budget);
}
