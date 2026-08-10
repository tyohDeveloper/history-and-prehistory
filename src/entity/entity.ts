// Types mirror schemas/entity.schema.json (schema_version 1.0.0).
// Keep in sync: tests/dataset-integrity.test.ts asserts the JSON conforms.

/**
 * `taxon` and `threshold` are schema 2.0.0 additions.
 *
 * A taxon is a species, which is not a period: several outlive the eras they
 * sit near, and Homo sapiens is extant. A threshold is the earliest known
 * instance of a behaviour - a one-sided bound that new evidence can only move
 * older, with the behaviour continuing after it.
 *
 * `city` is a schema 3.6.0 addition, and it exists because the alternative was
 * lying. Cities had been filed as whatever period-like kind was nearest to
 * hand: Byblos and Tyre as `era`, Tenochtitlan as `period`. A city is not a
 * span of time, and the mislabelling had consequences beyond tidiness. A period
 * ends; Damascus does not. Filing a living city as a period invites an end year
 * where none belongs, and reading 1453 as the end of Constantinople rather than
 * the moment it became Istanbul is exactly the error the kind is meant to
 * prevent. A `city` with a null end year is inhabited today.
 */
export type EntityKind =
  | "region"
  | "era"
  | "period"
  | "reign"
  | "event"
  | "city"
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

  /**
   * True when the entity continues to the present.
   *
   * Exists because an absent `end_year` meant two different things and the reader could not
   * tell which: Homo sapiens is extant, Homo luzonensis simply has no dated final
   * appearance. The old code inferred "present" by default, so undated became immortal.
   * Never set alongside `end_year`.
   */
  extant?: boolean;

  /**
   * How much standing the topic itself has, as distinct from its dating.
   *
   * The two vary independently and conflating them was a real loss of information. Dangun's
   * existence is `mythological` while his date is a `traditional` reckoning; the Lomekwian
   * industry is `accepted` and its 3.3 Ma date is genuinely argued. Omitted means `accepted`.
   */
  historicity?: "interpretive" | "reconstructed" | "contested" | "legendary" | "mythological";

  /**
   * Standing of the primary dating. Renamed from `standing` so it cannot be mistaken for a
   * claim about the topic, which is now `historicity`. Absent reads as `majority`.
   * `superseded` lives only in `alternatives[].standing`.
   */
  date_standing?: "consensus" | "majority" | "minority" | "traditional";

  /**
   * The phrase a reader would search to research this further.
   *
   * Explicitly not an identifier and never a link key: display names collide fifteen times
   * in this dataset, including two distinct places called Andes, so anything keyed on a
   * human-readable phrase resolves ambiguously. Links key on `id`.
   */
  search_phrase?: string;

  /**
   * Display name plus the shortest distinguishing context, for showing out of context.
   *
   * Derived by the build, never authored. Fifteen display names collide -- ten Japanese era
   * names in pairs, three Chinese regnal names across dynasties, and Mesoamerica and Andes
   * each at two points in the region tree. None are siblings, so the tree reads correctly in
   * place; a search result or a link chip does not.
   */
  qualified_name?: string;
  date_note?: string;
  allow_outside_parent_dates?: boolean;
  summary?: string;
  calendar_ids?: string[];
  /**
   * Typed relations. `derived` marks a link the build generated rather than an author
   * asserting it, so a reader can tell a researched claim from a structural one:
   * `sequence` for succession between consecutive reigns in a dynasty, `chronology` for
   * before-and-after ordering between periods -- which is NOT a claim that one state or
   * culture succeeded another -- and `reciprocal` for a generated inverse.
   */
  links?: {
    type: string;
    entity_id: string;
    note?: string;
    derived?: "sequence" | "chronology" | "reciprocal";
  }[];
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

