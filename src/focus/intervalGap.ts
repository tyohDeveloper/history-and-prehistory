import type { Entity } from "../entity/entity";

/** Historical-year extent of an entity, or null when it carries no date. */
export type Extent = readonly [number, number] | null;

export function extentOf(e: Entity): Extent {
  if (e.start_year === null) return null;
  return [e.start_year, e.end_year ?? 2026];
}

/**
 * Years between two extents; 0 when they overlap.
 *
 * Midpoint distance was the obvious first choice and it is wrong. A nengō sits
 * wholly inside the Heian period, so the two overlap completely while their
 * midpoints can be nearly two centuries apart — under midpoint distance a node
 * is penalised for being contemporaneous with its own parent. The prototype
 * pass caught this against real data.
 */
export function intervalGap(a: Extent, b: Extent): number | null {
  if (a === null || b === null) return null;
  if (a[0] <= b[1] && b[0] <= a[1]) return 0;
  return b[0] > a[1] ? b[0] - a[1] : a[0] - b[1];
}
