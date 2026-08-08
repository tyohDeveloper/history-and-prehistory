// Types mirror schemas/entity.schema.json (schema_version 1.0.0).
// Keep in sync: tests/dataset-integrity.test.ts asserts the JSON conforms.

export type EntityKind = "region" | "era" | "period" | "reign" | "event";
export type Tier = "foundational" | "intermediate" | "specialist";
export type Precision =
  | "year" | "decade" | "century" | "millennium"
  | "approx" | "traditional" | "disputed" | "unknown" | "exact";

export type DatingMethodId =
  | "calendar" | "radiocarbon-calibrated" | "radiocarbon-uncalibrated"
  | "argon-argon" | "potassium-argon" | "luminescence" | "uranium-series"
  | "esr" | "layer-counting" | "magnetostratigraphy" | "typological" | "unknown";

export type StandingId = "consensus" | "majority" | "minority" | "traditional" | "superseded";

export type CaveatKindId = "misconception" | "naming-confusion" | "contested-existence";

export interface Source {
  id: string;
  kind: "scholarly" | "reference" | "primary" | "dataset";
  citation: string;
  url?: string;
  note?: string;
}

export interface Entity {
  id: string;
  kind: EntityKind;
  name: string;
  parent_id: string | null;
  /** Proleptic Gregorian. Negative = BCE. No year zero. null = unknown/ongoing. */
  start_year: number | null;
  end_year: number | null;
  tier: Tier;
  native_name?: string;
  aliases?: string[];
  cross_parent_ids?: string[];
  redirect_ids?: string[];
  start_year_min?: number;
  start_year_max?: number;
  end_year_min?: number;
  end_year_max?: number;
  date_precision?: Precision;
  start_precision?: Precision;
  end_precision?: Precision;
  date_note?: string;
  allow_outside_parent_dates?: boolean;
  summary?: string;
  themes?: string[];
  region_tags?: string[];
  calendar_ids?: string[];
  misconceptions?: string[];
  notable_figures?: string[];
  capital?: string;
  capitals?: string[];
  successor_ids?: string[];
  predecessor_ids?: string[];
  links?: { type: string; entity_id: string; note?: string }[];
  /* --- schema 1.1.0 ------------------------------------------------------ */
  subkind?: string;
  dating_method?: DatingMethodId;
  standing?: StandingId;
  /** ISO date this dating was last checked. Live disputes only. */
  as_of?: string;
  native_date?: {
    calendar_id: string;
    text: string;
    year?: number;
    month?: number;
    day?: number;
    observance?: string;
    conversion_fuzz_days?: number;
  };
  alternatives?: {
    label: string;
    standing: StandingId;
    start_year?: number | null;
    end_year?: number | null;
    dating_method?: DatingMethodId;
    note?: string;
    source_ids?: string[];
  }[];
  caveats?: { kind: CaveatKindId; text: string; source_ids?: string[] }[];
  source_ids?: string[];
  sources?: { title: string; url?: string; note?: string }[];
}

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
export interface ReferenceFrame {
  id: string;
  name: string;
  anchor_set?: string;
  [k: string]: unknown;
}

export interface DataFile<T> {
  schema_version: string;
  dataset_version: string;
  generated_at: string;
  [k: string]: unknown | T[];
}
