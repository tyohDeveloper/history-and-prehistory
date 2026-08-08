import type { Extent } from "./extent";

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
