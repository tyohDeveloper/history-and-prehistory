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
  /** Old id to current id, so a stale link resolves instead of failing. Optional so existing
   * callers that build an index by hand, including tests, do not have to supply one. */
  redirects?: ReadonlyMap<string, string>;
}

/** Sort: chronological by start_year, undated last, then name. */
/**
 * Top-level branches that are classifications rather than places, and so read last.
 *
 * The ten geographic regions carry no date, and the comparator sorts undated entities after dated
 * ones, so Languages jumped to the head of the list the moment it inherited 50,000 BCE from the
 * earliest language beneath it. A reader opening the app landed on a language taxonomy before any
 * history. Its own date is now null, which is truthful -- a taxonomy does not begin in a year --
 * and this set carries it past the regions rather than into the middle of them alphabetically.
 */
const APPENDIX_ROOTS = new Set(["languages"]);

export function compareEntities(a: Entity, b: Entity): number {
  const aa = APPENDIX_ROOTS.has(a.id);
  const ba = APPENDIX_ROOTS.has(b.id);
  if (aa !== ba) return aa ? 1 : -1;
  const as = a.start_year;
  const bs = b.start_year;
  if (as === null && bs === null) return a.name.localeCompare(b.name);
  if (as === null) return 1;
  if (bs === null) return -1;
  if (as !== bs) return as - bs;
  return a.name.localeCompare(b.name);
}

export function buildIndex(
  list: readonly Entity[],
  redirects?: ReadonlyMap<string, string>,
): TreeIndex {
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
  return { byId, children, roots, redirects };
}

export function childrenOf(index: TreeIndex, id: string): Entity[] {
  return index.children.get(id) ?? [];
}

/** Root-to-node path. Follows parent_id only (not cross-parents). */
/**
 * Look up an entity, resolving a stale id through the redirect map.
 *
 * Ids are frozen, but 46 were normalised once so regnal numbers use Roman numerals. A
 * bookmarked link or a hand-typed id from before that change should still land on the entity
 * rather than on nothing.
 */
export function lookup(index: TreeIndex, id: string): Entity | undefined {
  const direct = index.byId.get(id);
  if (direct !== undefined) return direct;
  const redirected = index.redirects?.get(id);
  return redirected === undefined ? undefined : index.byId.get(redirected);
}

export function pathTo(index: TreeIndex, id: string): Entity[] {
  const out: Entity[] = [];
  const seen = new Set<string>();
  let cur = lookup(index, id);
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
interface SearchIndex {
  own: Map<string, string[]>;
  lineage: (id: string) => string[];
}

/** Own words per entity, plus a memoised walk up the ancestor chain. */
function buildSearchIndex(list: readonly Entity[]): SearchIndex {
  const byId = new Map(list.map((e) => [e.id, e]));
  const own = new Map<string, string[]>();
  for (const e of list) {
    own.set(
      e.id,
      [
        e.name,
        e.native_name ?? "",
        ...(e.aliases ?? []),
        // name_forms was indexed by nothing, so the endonyms, exonyms and scholarly variants
        // already authored on 99 entities were unreachable. It now also carries `adjectival`
        // forms, so "Roman" finds the Roman Empire directly and not only via its ancestors.
        ...(e.name_forms ?? []).map((f) => f.name),
      ].flatMap(foldToWords),
    );
  }
  const cache = new Map<string, string[]>();
  const lineage = (id: string): string[] => {
    const hit = cache.get(id);
    if (hit !== undefined) return hit;
    const parentId = byId.get(id)?.parent_id ?? null;
    const words =
      parentId === null ? [] : [...(own.get(parentId) ?? []), ...lineage(parentId)];
    cache.set(id, words);
    return words;
  };
  return { own, lineage };
}

/** Score one entity against the query terms, or null when nothing matched. */
function scoreEntity(e: Entity, terms: string[], idx: SearchIndex): number | null {
  const own = idx.own.get(e.id) ?? [];
  const inherited = idx.lineage(e.id);
  let total = 0;
  let matchedOwn = false;
  let matched = 0;
  for (const term of terms) {
    if (own.some((w) => w === term)) {
      total += 3;
      matchedOwn = true;
      matched += 1;
    } else if (own.some((w) => w.startsWith(term))) {
      total += 2;
      matchedOwn = true;
      matched += 1;
    } else if (inherited.some((w) => w === term || w.startsWith(term))) {
      total += 0.4;
      matched += 1;
    }
    // A word matching nothing is ignored rather than disqualifying the entity: requiring
    // every word to match meant "rulers of rome" returned nothing at all.
  }
  if (matched === 0) return null;
  // An exact whole-name match beats matching one word of a longer name. Searching "Romulus"
  // put Romulus Augustulus first -- both contain the word, and the emperor sits at a more
  // prominent tier -- so the founder of Rome came second to the man who lost it.
  const exact = foldToWords(e.name).join(" ") === terms.join(" ") ? 4 : 0;
  const coverage = (matched / terms.length) * 2;
  // Entities found only through an ancestor rank below every direct match.
  return (matchedOwn ? total : total - 2) + coverage + exact - TIER_ORDER[e.tier] * 0.1;
}

export function searchEntities(
  list: readonly Entity[],
  query: string,
  limit = 50,
): Entity[] {
  const raw = foldToWords(query);
  const stripped = raw.filter((w) => !SEARCH_STOPWORDS.has(w));
  const terms = stripped.length > 0 ? stripped : raw;
  if (terms.length === 0) return [];

  const idx = buildSearchIndex(list);
  const scored: { e: Entity; score: number }[] = [];
  for (const e of list) {
    const score = scoreEntity(e, terms, idx);
    if (score !== null) scored.push({ e, score });
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
