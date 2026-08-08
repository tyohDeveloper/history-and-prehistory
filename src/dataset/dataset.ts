// Build-time inlined dataset. There is no runtime fetch() anywhere in this
// app — the CSP in index.html sets connect-src 'none' and would block one,
// and file:// would fail outright. See docs/ARCHITECTURE.md §2.
import entitiesFile from "../data/entities.json";
import calendarsFile from "../data/calendars.json";
import themesFile from "../data/themes.json";
import framesFile from "../data/reference-frames.json";

import type { Entity } from "../entity/entity";

export const entities = entitiesFile.entities as unknown as Entity[];
export const calendars = calendarsFile.calendars as unknown as Calendar[];
export const themes = themesFile.themes as unknown as Theme[];
export const referenceFrames = framesFile.frames as unknown as ReferenceFrame[];

export const datasetVersion: string = entitiesFile.dataset_version;
export const schemaVersion: string = entitiesFile.schema_version;

/**
 * Shapes of the shipped data files, as distinct from the historical entity
 * itself, which lives in `entity/entity.ts`.
 *
 * These four were previously in a file called `types.ts`, which §3.8 prohibits
 * by name: it described the file's shape rather than what it owns.
 */

export interface Calendar {
  id: string;
  name: string;
  [k: string]: unknown;
}

export interface Theme {
  id: string;
  name: string;
  entity_ids: string[];
  [k: string]: unknown;
}

/**
 * A novice orientation anchor: "the Acheulean is about this old".
 *
 * `year` was previously absent from this interface and fell through the index
 * signature as `unknown`, so arithmetic on it did not type-check. The stub was
 * adequate while nothing read the field.
 */
export interface ReferenceFrame {
  id: string;
  name: string;
  /** Historical Gregorian year, negative for BCE. */
  year: number;
  end_year?: number;
  /**
   * `deep-time` is not a culture. The other sets are traditions a reader might
   * already know; before the Holocene there is no such tradition, so those
   * anchors supply scale instead of familiarity.
   */
  anchor_set?:
    | "western" | "east-asian" | "islamic" | "south-asian"
    | "african" | "americas" | "oceanic" | "global" | "deep-time";
  summary?: string;
  entity_id?: string;
}

export interface DataFile<T> {
  schema_version: string;
  dataset_version: string;
  generated_at: string;
  [k: string]: unknown | T[];
}
