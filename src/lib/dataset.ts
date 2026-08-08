// Build-time inlined dataset. There is no runtime fetch() anywhere in this
// app — the CSP in index.html sets connect-src 'none' and would block one,
// and file:// would fail outright. See docs/ARCHITECTURE.md §2.
import entitiesFile from "../data/entities.json";
import calendarsFile from "../data/calendars.json";
import themesFile from "../data/themes.json";
import framesFile from "../data/reference-frames.json";

import type { Calendar, Entity, ReferenceFrame, Theme } from "./types";

export const entities = entitiesFile.entities as unknown as Entity[];
export const calendars = calendarsFile.calendars as unknown as Calendar[];
export const themes = themesFile.themes as unknown as Theme[];
export const referenceFrames = framesFile.frames as unknown as ReferenceFrame[];

export const datasetVersion: string = entitiesFile.dataset_version;
export const schemaVersion: string = entitiesFile.schema_version;
