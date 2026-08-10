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
  | "calendar" | "dendrochronology" | "radiocarbon-calibrated" | "radiocarbon-uncalibrated"
  | "argon-argon" | "potassium-argon" | "luminescence" | "uranium-series"
  | "esr" | "cosmogenic" | "layer-counting" | "magnetostratigraphy"
  | "received" | "typological" | "unknown";

export type StandingId = "consensus" | "majority" | "minority" | "traditional" | "superseded";

export type CaveatKindId = "misconception" | "naming-confusion" | "contested-existence";

/** A name this entity is or was known by, and what kind of name it is.
 *
 * A flat string list could not say why a name differs, who uses it, when it
 * applied, or whether descendants repudiate it. That is why the easy cases got
 * aliases (Cheops, King Tut) while the loaded ones went unfilled. */
export interface NameForm {
  name: string;
  kind:
    | "endonym"
    | "exonym"
    | "formal"
    | "common"
    | "translation"
    | "scholarly"
    | "historical"
    | "rejected";
  lang?: string;
  from?: number;
  to?: number;
  note?: string;
  source_ids?: string[];
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
  name_forms?: NameForm[];
  cross_parent_ids?: string[];
  /** DERIVED at build time, never authored: the top-level geographies this
   *  entity is reachable from, following parent_id and cross_parent_ids in both
   *  directions. Present only when more than one. Records where an entity is
   *  PLACED, not where a polity RULED. */
  regions?: string[];
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
  calendar_ids?: string[];
  notable_figures?: string[];
  capital?: string;
  links?: { type: string; entity_id: string; note?: string }[];
  /* --- schema 1.1.0 (see 2.0.0 additions below) ------------------------------------------------------ */
  /**
   * Per-boundary dating (schema 3.0.0, resolving Q-30).
   *
   * One field cannot describe an entity whose boundaries rest on different
   * science. Neanderthals appear at ~400 ka by uranium-series and disappear at
   * ~40 ka by radiocarbon. The end is deliberately NOT inherited from the
   * start: silent inheritance is what produced the mislabelling in the first
   * place, so an unrecorded end method reads as unknown rather than as a
   * confident wrong answer.
   */
  start_dating_method?: DatingMethodId;
  end_dating_method?: DatingMethodId;
  standing?: StandingId;
  /** ISO date this dating was last checked. Live disputes only. */
  as_of?: string;
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
}

