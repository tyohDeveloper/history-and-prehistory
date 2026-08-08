import { TIER_ORDER } from "../entity/tree";
import type { Entity } from "../entity/entity";

/**
 * Tier ranked WITHIN its sibling set, in [0, 1].
 *
 * `tier` looks like ready-made a priori importance and is not. It is authored
 * per branch: East Asia is 70% specialist, Central Asia and Southeast Asia 0%,
 * West Asia 3%. A "specialist" nengō and a "specialist" hominin are not
 * comparable quantities — the field records how deeply its own branch was
 * covered. Used raw it would dim East Asia for authoring reasons rather than
 * importance ones.
 *
 * Ranked among siblings it means the same thing everywhere. Where every
 * sibling shares a tier it returns 0.5: the field carries no local information
 * there and must not tilt the result either way. The Heian period forces this —
 * all 88 of its children are `specialist`, so only time can separate them.
 */
export function siblingTierScore(e: Entity, siblings: readonly Entity[]): number {
  const distinct = [...new Set(siblings.map((s) => TIER_ORDER[s.tier]))].sort((a, b) => a - b);
  if (distinct.length <= 1) return 0.5;
  // TIER_ORDER counts up as importance falls, so invert to make high = important.
  return 1 - distinct.indexOf(TIER_ORDER[e.tier]) / (distinct.length - 1);
}
