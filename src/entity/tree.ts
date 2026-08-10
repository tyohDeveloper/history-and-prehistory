// Pure tree-index functions over the entity list. No DOM, no globals.
// This is the "pure library layer" the architecture standards require to
// carry unit tests; the UI layer is exercised via Playwright instead.

import type { Entity, Tier } from "./entity";

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

/** Fold to lowercase words, keeping word boundaries that `foldForSearch` throws away. */
function foldToWords(s: string): string[] {
  return s
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .split(/[^a-z0-9]+/)
    .filter((w) => w.length > 0);
}

/**
 * Words dropped from a query, because they appear inside real names and match everything.
 *
 * Without this, "rulers of rome" ranked "Controlled Use of Fire" and "The Drowning of
 * Doggerland" above the Roman entities -- they matched on "of". These are only stripped
 * from the QUERY; entity names keep their own words, so "Year of the Four Emperors" is
 * still findable by its distinctive words.
 */
const SEARCH_STOPWORDS = new Set([
  "a", "an", "and", "are", "as", "at", "by", "did", "do", "for", "from", "in", "is",
  "of", "on", "or", "the", "to", "was", "were", "what", "which", "who", "whom", "whose",
  "with",
]);

/**
 * Search names, aliases, and the names of ancestors.
 *
 * The previous version folded away word boundaries and then used `includes`, which had
 * two consequences a user hit immediately. Searching **Rome** returned "Domestication of
 * the Dromedary" — fold "dromedary" and the letters r-o-m-e sit right there in the middle
 * — and it returned neither the Roman Kingdom, the Republic, the Empire, nor any of the
 * seventy-odd Roman rulers. "rulers of rome" returned nothing at all, because a
 * multi-word query was folded into one long token that matched no single name.
 *
 * Three changes:
 *
 * **Words, not substrings.** A query word must match a whole haystack word or its start.
 * That kills Dromedary without any special-casing.
 *
 * **Every query word must match somewhere.** So multi-word queries work, and "rulers of
 * rome" finds things under Rome instead of nothing.
 *
 * **Ancestors count, at a lower score.** A reader searching "Rome" wants the city, the
 * kingdom, the republic and the emperors — and the emperors' own names contain none of
 * that. Matching against the ancestor chain reaches them, ranked below anything whose own
 * name matches, so Ancient Rome still comes first and the rulers follow.
 */
export function searchEntities(
  list: readonly Entity[],
  query: string,
  limit = 50,
): Entity[] {
  const raw = foldToWords(query);
  // Keep stopwords only if the query is nothing but stopwords, so searching "the" still
  // does something rather than silently returning nothing.
  const stripped = raw.filter((w) => !SEARCH_STOPWORDS.has(w));
  const terms = stripped.length > 0 ? stripped : raw;
  if (terms.length === 0) return [];

  const byId = new Map(list.map((e) => [e.id, e]));
  const ownWords = new Map<string, string[]>();
  for (const e of list) {
    ownWords.set(
      e.id,
      [e.name, e.native_name ?? "", ...(e.aliases ?? [])].flatMap(foldToWords),
    );
  }

  // Ancestor words, memoised: an entity deep in the tree would otherwise walk its whole
  // lineage once per search term.
  const lineageWords = new Map<string, string[]>();
  const lineageOf = (id: string): string[] => {
    const cached = lineageWords.get(id);
    if (cached !== undefined) return cached;
    const entity = byId.get(id);
    const parentId = entity?.parent_id ?? null;
    const words =
      parentId === null || parentId === undefined
        ? []
        : [...(ownWords.get(parentId) ?? []), ...lineageOf(parentId)];
    lineageWords.set(id, words);
    return words;
  };

  const hits = (word: string, haystack: string[]): boolean =>
    haystack.some((w) => w === word || w.startsWith(word));

  const scored: { e: Entity; score: number }[] = [];
  for (const e of list) {
    const own = ownWords.get(e.id) ?? [];
    const inherited = lineageOf(e.id);
    let total = 0;
    let matchedOwn = false;
    let matchedTerms = 0;
    for (const term of terms) {
      if (own.some((w) => w === term)) {
        total += 3;
        matchedOwn = true;
        matchedTerms += 1;
      } else if (own.some((w) => w.startsWith(term))) {
        total += 2;
        matchedOwn = true;
        matchedTerms += 1;
      } else if (hits(term, inherited)) {
        // Reachable through an ancestor, which is weaker than matching on its own name.
        total += 0.4;
        matchedTerms += 1;
      }
      // A word that matches nothing is ignored rather than disqualifying the entity.
      // Requiring every word to match meant "rulers of rome" returned nothing at all,
      // because no entity is named "rulers" and none is named "of". People type
      // questions into search boxes, and answering with an empty list is the wrong
      // response to a query that names a real thing.
    }
    if (matchedTerms === 0) continue;
    // Matching more of the query outranks matching one word strongly, so "tang emperor"
    // puts Tang emperors above everything that merely contains "emperor".
    const coverage = matchedTerms / terms.length;
    // An entity found only through its ancestors ranks below every direct match.
    const score =
      (matchedOwn ? total : total - 2) + coverage * 2 - TIER_ORDER[e.tier] * 0.1;
    scored.push({ e, score });
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

/**
 * A missing end year means three different things and they must not read alike.
 *
 * For Homo sapiens it means *extant*. For Homo luzonensis it means the youngest
 * remains have never been dated — the species certainly ended, we just cannot
 * say when. Rendering both as "present" would assert that a hominin known from
 * a handful of foot bones is still walking around. `end_precision: "unknown"`
 * separates those two.
 *
 * The third case only appeared in 0.16.0.0, when the dataset acquired its first
 * point events — the sack of Babylon, Kadesh, the invention of coinage, the
 * Narmer Palette. A battle has no end year because it is a moment, not because
 * it is ongoing, and the readout was rendering the Narmer Palette as
 * "5,049 BP – present". An `event` with no end is a point in time, so it prints
 * as one date and nothing else.
 */
export function formatRange(e: Entity): string {
  const start = formatYear(e.start_year);
  if (e.end_year === null) {
    if (e.start_year === null) return "—";
    if (e.kind === "event" && e.extant !== true) return start;
    // `extant` decides this now. The old default was "present", so anything whose end was
    // merely undated was rendered as ongoing.
    return e.extant === true ? `${start} – present` : `${start} – unknown`;
  }
  return `${start} – ${formatYear(e.end_year)}`;
}
