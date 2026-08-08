import { extentOf, intervalGap, type Extent } from "./intervalGap";
import { localGapScale } from "./localGapScale";
import { siblingTierScore } from "./siblingTierScore";
import { treeDistance } from "./treeDistance";
import type { TreeIndex } from "../entity/tree";
import { childrenOf } from "../entity/tree";
import type { Entity } from "../entity/entity";

/**
 * Furnas's degree of interest, calibrated against this dataset.
 *
 *   DOI(x | f) = API(x) − distance(f, x)
 *
 * Three things the prototype pass disproved, all of them the obvious choice:
 *
 * **API is not −depth.** Furnas's canonical tree API ranked "East Asia",
 * "Global" and "Europe" above every real neighbour, because shallow nodes win
 * on depth and undated containers dodged the temporal term. The trunk here is
 * eleven region nodes already permanently visible in the Miller columns, so
 * surfacing them adds nothing. Depth also correlates hard with tier — 0%
 * specialist at depth 0, 59% at depth 5 — so using both double-counts.
 *
 * **Distance is not in years.** See `localGapScale`.
 *
 * **Overlap alone is too generous.** "CE (Common Era)" and "Middle Ages"
 * trivially overlap a seven-year nengō and ranked as its neighbours. An entity
 * three hundred times longer is *containing* the focus, not keeping it
 * company, hence the span term.
 */
export interface DoiWeights {
  tier: number;
  time: number;
  tree: number;
  span: number;
}

/** Placeholders: good on the sampled foci, not yet tuned broadly. See Q-33. */
export const DEFAULT_WEIGHTS: DoiWeights = { tier: 2.5, time: 1, tree: 1, span: 0.6 };

export interface DoiContext {
  index: TreeIndex;
  sortedMidpoints: readonly number[];
  weights: DoiWeights;
}

function spanOf(x: Extent): number {
  return x === null ? 1 : Math.max(x[1] - x[0], 1);
}

export function degreeOfInterest(ctx: DoiContext, focus: Entity, x: Entity): number {
  const fx = extentOf(focus);
  const xx = extentOf(x);
  const gap = intervalGap(fx, xx);
  // An undated container is navigation scaffolding, not content the lens ranks.
  if (gap === null || fx === null || xx === null) return Number.NEGATIVE_INFINITY;

  const w = ctx.weights;
  const api = w.tier * siblingTierScore(x, childrenOf(ctx.index, x.parent_id ?? ""));

  const centre = (fx[0] + fx[1]) / 2;
  const scale = localGapScale(ctx.sortedMidpoints, centre);
  const dTime = Math.log1p(gap / scale);
  const dTree = treeDistance(ctx.index, focus.id, x.id);
  const dSpan = Math.abs(Math.log10(spanOf(xx) / spanOf(fx)));

  // Where temporal neighbours are 75,000 years away the time term says little,
  // so structure carries more; where they are a year away the reverse holds.
  const density = 1 / (1 + Math.log1p(scale));
  return (
    api -
    (w.time * density * dTime + w.tree * (1 - density) * dTree + w.span * dSpan)
  );
}
