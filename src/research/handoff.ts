/**
 * Research handoff.
 *
 * This app is a starting point, not a research tool. It shows how things
 * relate and roughly when they happened; anyone who wants the argument itself
 * has to go and read it. What the app owes them is a good push in the right
 * direction, not a curated bibliography it cannot honestly maintain across
 * 1,305 entities.
 *
 * So links are **generated from the entity**, not authored per entity. That
 * choice buys a lot:
 *
 *   - no 1,305-link curation project, and no link rot to police
 *   - every entity gets a handoff, including ones nobody has edited
 *   - nothing to keep in sync when a name or a parent changes
 *
 * A curated `Source` is still available for the rare case where one specific
 * work *is* the answer — a calibration curve, a named chronology. It is the
 * exception, not the mechanism.
 *
 * ## Offline
 *
 * Opened without a network the link goes nowhere, and that is accepted rather
 * than worked around. The app does not probe for connectivity: `navigator.onLine`
 * is unreliable, and testing it would be a form of environment sniffing this
 * app has no business doing. Instead every handoff exposes its URL as copyable
 * text, and a selection can be exported as a plain-text research note. An
 * offline user writes the search down and runs it later, which is what they
 * were going to do anyway.
 */

import type { Entity } from "../entity/entity";
import { formatRange, pathTo, type TreeIndex } from "../entity/tree";

/** Wikipedia language edition to search. */
export type WikiLang = "en";

export interface HandoffTarget {
  id: string;
  /** Descriptive link text. Never a bare URL — ARCHITECTURE.md §10. */
  label: string;
  url: string;
  /** The same URL, for display and copying when the network is unavailable. */
  displayUrl: string;
}

/**
 * Names that occur more than once in the dataset.
 *
 * Disambiguation is added exactly where ambiguity is known to exist rather
 * than by guesswork. The dataset really does contain two Emperor Taizongs and
 * two Shōwa eras, and those are precisely the searches that need help.
 */
export function ambiguousNames(entities: readonly Entity[]): ReadonlySet<string> {
  const seen = new Set<string>();
  const duplicated = new Set<string>();
  for (const e of entities) {
    if (seen.has(e.name)) duplicated.add(e.name);
    else seen.add(e.name);
  }
  return duplicated;
}

/** Would adding this ancestor's name tell the search engine anything new? */
function addsSignal(context: string, name: string): boolean {
  const a = context.toLowerCase();
  const b = name.toLowerCase();
  return !a.includes(b) && !b.includes(a);
}

/**
 * Build the search query for an entity.
 *
 * Plain name by default. Where the name is ambiguous within the dataset, the
 * nearest ancestor that adds signal is appended — "Emperor Taizong" becomes
 * "Emperor Taizong Tang Dynasty", which is the discriminator a reader would
 * have supplied themselves.
 */
export function searchQuery(
  entity: Entity,
  index: TreeIndex,
  options: { ambiguous?: ReadonlySet<string>; force?: boolean } = {},
): string {
  const needsContext = options.force === true || (options.ambiguous?.has(entity.name) ?? false);
  if (!needsContext) return entity.name;

  const ancestors = pathTo(index, entity.id).slice(0, -1).reverse();
  const context = ancestors.find((a) => addsSignal(a.name, entity.name));
  return context === undefined ? entity.name : `${entity.name} ${context.name}`;
}

/**
 * Wikipedia search URL.
 *
 * `/w/index.php?search=` redirects straight to the article when the query
 * matches one exactly, and falls back to the results page when it does not —
 * so a well-known subject lands on its article and an ambiguous one lands
 * somewhere useful. No tracking parameters are appended.
 */
export function wikipediaSearchUrl(query: string, lang: WikiLang = "en"): string {
  return `https://${lang}.wikipedia.org/w/index.php?search=${encodeURIComponent(query)}`;
}

export function handoffTargets(
  entity: Entity,
  index: TreeIndex,
  options: { ambiguous?: ReadonlySet<string> } = {},
): HandoffTarget[] {
  const query = searchQuery(entity, index, options);
  const url = wikipediaSearchUrl(query);
  return [
    {
      id: "wikipedia",
      label: `Search Wikipedia for \u201C${query}\u201D`,
      url,
      displayUrl: url,
    },
  ];
}

/**
 * A plain-text research note for the current selection.
 *
 * This is the offline answer. Generated client-side and handed to the browser
 * as a download (`Blob` + `URL.createObjectURL`), so nothing leaves the
 * machine and no server is involved — the pattern the standalone-HTML5
 * standard explicitly permits. A user with no network gets the context, the
 * dates, any noted complications, and the search to run later.
 */
export function researchNote(
  entity: Entity,
  index: TreeIndex,
  options: { ambiguous?: ReadonlySet<string>; datasetVersion?: string } = {},
): string {
  const trail = pathTo(index, entity.id).map((e) => e.name);
  const lines: string[] = [
    `# ${entity.name}`,
    "",
    `${trail.join(" > ")}`,
    "",
    `- Kind: ${entity.kind}`,
    `- Dates: ${formatRange(entity)}`,
  ];
  if (entity.native_name !== undefined) lines.push(`- Native name: ${entity.native_name}`);
  if (entity.aliases !== undefined && entity.aliases.length > 0) {
    lines.push(`- Also known as: ${entity.aliases.join(", ")}`);
  }
  if (entity.date_note !== undefined) lines.push(`- Dating note: ${entity.date_note}`);
  lines.push("");
  if (entity.summary !== undefined) lines.push(entity.summary, "");
  lines.push("## Start your research", "");
  for (const t of handoffTargets(entity, index, options)) {
    lines.push(`- ${t.label}: ${t.displayUrl}`);
  }
  lines.push("", "## Notes", "", "");
  const version = options.datasetVersion;
  lines.push(
    "---",
    `Exported from History & Prehistory${version === undefined ? "" : `, dataset ${version}`}.`,
    "Dates are a starting point, not a citation. Verify before relying on them.",
  );
  return lines.join("\n");
}
