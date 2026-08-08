// Types mirror schemas/entity.schema.json (schema_version 1.0.0).
// Keep in sync: tests/dataset-integrity.test.ts asserts the JSON conforms.

/**
 * `taxon` and `threshold` are schema 2.0.0 additions.
 *
 * A taxon is a species, which is not a period: several outlive the eras they
 * sit near, and Homo sapiens is extant. A threshold is the earliest known
 * instance of a behaviour - a one-sided bound that new evidence can only move
 * older, with the behaviour continuing after it.
 */
export type EntityKind =
  | "region"
  | "era"
  | "period"
  | "reign"
  | "event"
  | "taxon"
  | "threshold";
export type Tier = "foundational" | "intermediate" | "specialist";
export type Precision =
  | "year" | "decade" | "century" | "millennium"
  | "approx" | "traditional" | "disputed" | "unknown" | "exact" | "minimum";

export type DatingMethodId =
  | "calendar" | "radiocarbon-calibrated" | "radiocarbon-uncalibrated"
  | "argon-argon" | "potassium-argon" | "luminescence" | "uranium-series"
  | "esr" | "layer-counting" | "magnetostratigraphy" | "typological" | "unknown";

export type StandingId = "consensus" | "majority" | "minority" | "traditional" | "superseded";

export type CaveatKindId = "misconception" | "naming-confusion" | "contested-existence";

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
  /* --- schema 1.1.0 (see 2.0.0 additions below) ------------------------------------------------------ */
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

