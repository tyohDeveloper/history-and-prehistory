import type { Entity } from "../entity/entity";

/** Historical-year extent of an entity, or null when it carries no date. */
export type Extent = readonly [number, number] | null;

export function extentOf(e: Entity): Extent {
  if (e.start_year === null) return null;
  return [e.start_year, e.end_year ?? 2026];
}
