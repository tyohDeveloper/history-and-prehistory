/**
 * Which calendars the readout shows, and where that choice lives.
 *
 * The app stores nothing — no `localStorage`, no cookies. So a selection the
 * user wants to keep goes in `location.hash`, which makes persistence *their*
 * decision: bookmark the URL and the choice survives, close the tab and it
 * does not. That is the only persistence mechanism compatible with both the
 * no-storage rule and running from `file://`.
 */

import { CALENDARS_BY_ID, DEFAULT_CALENDAR_IDS } from "./registry";

const HASH_KEY = "cal";
/** Guard against a hand-edited URL producing an unreadable wall of columns. */
export const MAX_SELECTED = 6;

export function parseSelection(hash: string): string[] {
  const params = new URLSearchParams(hash.replace(/^#/, ""));
  const raw = params.get(HASH_KEY);
  if (raw === null || raw.length === 0) return [...DEFAULT_CALENDAR_IDS];
  const ids = raw.split(",").filter((id) => CALENDARS_BY_ID.has(id));
  const unique = [...new Set(ids)].slice(0, MAX_SELECTED);
  return unique.length > 0 ? unique : [...DEFAULT_CALENDAR_IDS];
}

/** The hash fragment for a selection, or "" when it is just the default. */
export function serializeSelection(ids: readonly string[]): string {
  const isDefault =
    ids.length === DEFAULT_CALENDAR_IDS.length && ids.every((id, i) => id === DEFAULT_CALENDAR_IDS[i]);
  if (isDefault) return "";
  return `#${HASH_KEY}=${ids.join(",")}`;
}

export function toggleCalendar(ids: readonly string[], id: string): string[] {
  if (ids.includes(id)) {
    const next = ids.filter((x) => x !== id);
    // Never leave the readout with nothing to show.
    return next.length > 0 ? next : [...DEFAULT_CALENDAR_IDS];
  }
  if (ids.length >= MAX_SELECTED) return [...ids];
  return [...ids, id];
}
