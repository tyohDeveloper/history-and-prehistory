// Pure tree-index functions over the entity list. No DOM, no globals.
// This is the "pure library layer" the architecture standards require to
// carry unit tests; the UI layer is exercised via Playwright instead.

import type { Entity, Tier } from "./types";

export const TIER_ORDER: Record<Tier, number> = {
  foundational: 0,
  intermediate: 1,
  specialist: 2,
};

export interface TreeIndex {
  byId: Map<string, Entity>;
  /** Children keyed by parent id, including cross_parent_ids placements. */
  children: Map<string, Entity[]>;
  roots: Entity[];
}

/** Sort: chronological by start_year, undated last, then name. */
export function compareEntities(a: Entity, b: Entity): number {
  const as = a.start_year;
  const bs = b.start_year;
  if (as === null && bs === null) return a.name.localeCompare(b.name);
  if (as === null) return 1;
  if (bs === null) return -1;
  if (as !== bs) return as - bs;
  return a.name.localeCompare(b.name);
}

export function buildIndex(list: readonly Entity[]): TreeIndex {
  const byId = new Map<string, Entity>();
  for (const e of list) byId.set(e.id, e);

  const children = new Map<string, Entity[]>();
  const push = (parent: string, child: Entity): void => {
    const bucket = children.get(parent);
    if (bucket) bucket.push(child);
    else children.set(parent, [child]);
  };

  for (const e of list) {
    if (e.parent_id !== null) push(e.parent_id, e);
    for (const cp of e.cross_parent_ids ?? []) push(cp, e);
  }
  for (const bucket of children.values()) bucket.sort(compareEntities);

  const roots = list.filter((e) => e.parent_id === null).slice().sort(compareEntities);
  return { byId, children, roots };
}

export function childrenOf(index: TreeIndex, id: string): Entity[] {
  return index.children.get(id) ?? [];
}

/** Root-to-node path. Follows parent_id only (not cross-parents). */
export function pathTo(index: TreeIndex, id: string): Entity[] {
  const out: Entity[] = [];
  const seen = new Set<string>();
  let cur = index.byId.get(id);
  while (cur && !seen.has(cur.id)) {
    seen.add(cur.id);
    out.unshift(cur);
    cur = cur.parent_id === null ? undefined : index.byId.get(cur.parent_id);
  }
  return out;
}

export function visibleAtTier(list: readonly Entity[], maxTier: Tier): Entity[] {
  const limit = TIER_ORDER[maxTier];
  return list.filter((e) => TIER_ORDER[e.tier] <= limit);
}

/**
 * Fold a string for search: lowercase, strip diacritics, drop separators.
 * Makes `Ala-ud-din` match `Alauddin` and `Jōmon` match `jomon`.
 */
export function foldForSearch(s: string): string {
  return s
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "");
}

export function searchEntities(
  list: readonly Entity[],
  query: string,
  limit = 50,
): Entity[] {
  const q = foldForSearch(query);
  if (q.length === 0) return [];
  const scored: { e: Entity; score: number }[] = [];
  for (const e of list) {
    const haystacks = [e.name, e.native_name ?? "", ...(e.aliases ?? [])];
    let best = -1;
    for (const h of haystacks) {
      const f = foldForSearch(h);
      if (f === q) best = Math.max(best, 3);
      else if (f.startsWith(q)) best = Math.max(best, 2);
      else if (f.includes(q)) best = Math.max(best, 1);
    }
    if (best > 0) scored.push({ e, score: best - TIER_ORDER[e.tier] * 0.1 });
  }
  scored.sort((a, b) => b.score - a.score || compareEntities(a.e, b.e));
  return scored.slice(0, limit).map((s) => s.e);
}

/** Format a proleptic-Gregorian year for display. Year 0 does not exist. */
export function formatYear(y: number | null): string {
  if (y === null) return "—";
  // No thousands separators: years are conventionally written unseparated
  // ("1603 CE", "14000 BCE"), and it keeps the readout consistent with the
  // compact ranges in the column gutter. Separators stay for BP and ka
  // counts, which are quantities rather than years.
  return y < 0 ? `${Math.abs(y)} BCE` : `${y} CE`;
}

export function formatRange(e: Entity): string {
  const start = formatYear(e.start_year);
  if (e.end_year === null) return e.start_year === null ? "—" : `${start} – present`;
  return `${start} – ${formatYear(e.end_year)}`;
}
