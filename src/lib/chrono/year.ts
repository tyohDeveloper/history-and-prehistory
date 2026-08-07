/**
 * The year value model.
 *
 * Everything downstream — calendar conversion, BP rendering, the readout —
 * operates on `YearValue` rather than a bare number. Uncertainty is part of
 * the value, not a formatting decision made later.
 *
 * That matters because this app spans six orders of magnitude. A reign is
 * known to the year; a radiocarbon date carries a couple of centuries of
 * confidence interval; an Oldowan boundary is uncertain by hundreds of
 * millennia. A model that can only hold a point estimate forces every one of
 * those to lie about its own precision.
 *
 * ## Year numbering
 *
 * `year` is HISTORICAL proleptic Gregorian: negative is BCE, positive is CE,
 * and there is no year zero. This matches the entity dataset.
 *
 * The Temporal API and ISO 8601 use ASTRONOMICAL numbering, where 1 BCE is
 * year 0 and 2 BCE is year -1. `toAstronomical` / `fromAstronomical` are the
 * only sanctioned crossing points. Mixing the two silently produces
 * off-by-one errors that survive review, so they are never mixed inline.
 */

export type DatingMethod =
  | "calendar"
  | "radiocarbon-calibrated"
  | "radiocarbon-uncalibrated"
  | "potassium-argon"
  | "luminescence"
  | "esr"
  | "typological"
  | "unknown";

/**
 * One anchor of a date, with its own uncertainty.
 *
 * Anchors are independently fuzzy, which is the whole point of the model. In
 * "~3500 BCE (3000 BCE .. ~4500 BCE)" the latest bound is a hard floor, the
 * consensus is soft, and the earliest bound is soft — three anchors, three
 * different certainties. A representation that could not vary fuzziness per
 * anchor (a trapezoid, say) would have to discard one of those facts.
 */
export interface FuzzyPoint {
  /** The stated value, historical Gregorian. Negative = BCE, no year zero. */
  year: number;
  /** Half-width in years. Absent or zero means the anchor is crisp. */
  fuzz?: number;
}

/**
 * The frame a date was *quoted in by its source*.
 *
 * Distinct from how it is displayed. BP and calendar reckoning are exactly
 * interconvertible, so display is free — but the native frame is not
 * recoverable after the fact, and it matters. A source reading "4500 BP" is
 * quoting to the nearest century; re-rendering it as "2550 BCE" silently
 * claims a precision the source never offered. Recording the native frame
 * lets the readout show the source's own number verbatim when asked for it.
 */
export type NativeFrame = "bp" | "calendar";

export interface YearValue {
  /**
   * Best accepted value: what most scholars would call reasonable, at the
   * level an early undergraduate course would teach. Not the research
   * frontier, and not our adjudication of a live dispute — where the field is
   * genuinely split, say so in `note` rather than quietly picking a side.
   */
  consensus: FuzzyPoint;
  /** Oldest plausible bound. */
  earliest?: FuzzyPoint;
  /** Youngest plausible bound. */
  latest?: FuzzyPoint;
  method?: DatingMethod;
  /** The frame the source quoted. Display frame is chosen separately. */
  nativeFrame?: NativeFrame;
  /** Free text for genuine scholarly disagreement, as opposed to imprecision. */
  note?: string;
}

export function isCrisp(p: FuzzyPoint): boolean {
  return p.fuzz === undefined || p.fuzz === 0;
}

/** True when the value is a single crisp anchor with no bounds. */
export function isExact(v: YearValue): boolean {
  return v.earliest === undefined && v.latest === undefined && isCrisp(v.consensus);
}

/**
 * Total span the value could occupy, widened by each bound's own fuzz.
 * Returns `undefined` when no bounds are stated.
 */
export function supportOf(v: YearValue): { earliest: number; latest: number } | undefined {
  if (v.earliest === undefined && v.latest === undefined) return undefined;
  const e = v.earliest ?? v.consensus;
  const l = v.latest ?? v.consensus;
  return {
    earliest: e.year - (e.fuzz ?? 0),
    latest: l.year + (l.fuzz ?? 0),
  };
}

export function toAstronomical(historicalYear: number): number {
  if (historicalYear === 0) {
    throw new RangeError("Year zero does not exist in historical numbering.");
  }
  return historicalYear < 0 ? historicalYear + 1 : historicalYear;
}

export function fromAstronomical(astronomicalYear: number): number {
  return astronomicalYear <= 0 ? astronomicalYear - 1 : astronomicalYear;
}

/** Whole years between two historical years, skipping the absent year zero. */
export function yearsBetween(from: number, to: number): number {
  return toAstronomical(to) - toAstronomical(from);
}

/**
 * Half-width of the overall uncertainty, or `undefined` if unbounded.
 * Drives display rounding: a value is never printed to more resolution than
 * its own uncertainty justifies.
 */
export function uncertaintyOf(v: YearValue): number | undefined {
  const support = supportOf(v);
  if (support === undefined) {
    return v.consensus.fuzz;
  }
  return Math.max(
    Math.abs(v.consensus.year - support.earliest),
    Math.abs(support.latest - v.consensus.year),
  );
}

/**
 * Dating methods that are not calendar-derived. A calibrated radiocarbon date
 * and a historically attested date are not the same kind of claim, and the
 * readout should not present them identically.
 */
const NON_CALENDAR_METHODS: ReadonlySet<DatingMethod> = new Set([
  "radiocarbon-calibrated",
  "radiocarbon-uncalibrated",
  "potassium-argon",
  "luminescence",
  "esr",
  "typological",
]);

export function isScientificDating(v: YearValue): boolean {
  return v.method !== undefined && NON_CALENDAR_METHODS.has(v.method);
}

export const DATING_METHOD_LABEL: Record<DatingMethod, string> = {
  calendar: "Calendar / historically attested",
  "radiocarbon-calibrated": "Radiocarbon, calibrated",
  "radiocarbon-uncalibrated": "Radiocarbon, uncalibrated",
  "potassium-argon": "Potassium-argon",
  luminescence: "Luminescence (OSL/TL)",
  esr: "Electron spin resonance",
  typological: "Typological / stratigraphic",
  unknown: "Unknown",
};

// ---------------------------------------------------------------------------
// Disclosure: what to reveal when a single number is not an honest answer.
// ---------------------------------------------------------------------------

/**
 * A source, held in a normalized registry rather than inlined per entity.
 *
 * Deduplication is the reason. A single chronology reference can be cited by
 * two hundred Egyptian entities; inlining the full citation at each one would
 * multiply it two hundred times in a bundle that must stay under budget. The
 * dataset already normalizes calendars and themes into their own id-keyed
 * files, so this follows the existing shape rather than inventing one.
 */
export type SourceKind =
  /** Peer-reviewed or academic-press work. */
  | "scholarly"
  /** General reference: encyclopedia entries, standard handbooks. */
  | "reference"
  /** A primary document: inscription, king list, chronicle, excavation report. */
  | "primary"
  /** A published dataset or calibration curve. */
  | "dataset";

export interface Source {
  id: string;
  kind: SourceKind;
  /** Rendered as the link text. Never a bare URL — see ARCHITECTURE.md §10. */
  citation: string;
  url?: string;
  note?: string;
}

/**
 * How a claim stands relative to the field.
 *
 * `traditional` is deliberately separate from the rest: "Rome founded in
 * 753 BCE" and "Narmer c. 3100 BCE" are received dates, not findings, and
 * presenting them with the same weight as a measured or attested date is the
 * single most common way a history reference misleads. The dataset already
 * marks a few of these with `date_precision: "traditional"`; this promotes
 * that from a precision flag to a claim about standing, which is what it
 * actually is.
 */
export type ClaimStanding =
  | "consensus"
  | "majority"
  | "minority"
  | "traditional"
  | "superseded";

export interface DatingClaim {
  value: YearValue;
  /** e.g. "Middle chronology", "Radiocarbon (IntCal20)". */
  label: string;
  standing: ClaimStanding;
  /** Ids into the source registry. */
  sourceIds?: string[];
  note?: string;
}

/**
 * Why this boundary needs more than one number.
 *
 * The reason is not decoration: it selects the wording on the marker, so a
 * user can tell what kind of complication awaits before deciding to open it.
 * A generic asterisk makes every complication look alike, and they are not
 * alike — "scholars disagree" and "depends where you draw the line" call for
 * completely different reading.
 */
export type DisclosureReason =
  /** Competing chronological schemes, e.g. Egyptian high/middle/low. */
  | "rival-chronologies"
  /** Methods disagree, e.g. radiocarbon against a king list. */
  | "method-conflict"
  /** Not a dating question at all: the boundary is a matter of definition. */
  | "definitional"
  /** A received or legendary date rather than an established one. */
  | "traditional-date"
  /** Value depends on calibration choice or correlation constant. */
  | "calibration"
  /** No dispute, simply a broad range. */
  | "wide-uncertainty"
  /**
   * The boundary legitimately falls outside its parent's range.
   *
   * The commonest disclosure in the actual dataset — 27 entities carry
   * `allow_outside_parent_dates`. Oda Nobunaga's rule starts before the era
   * named after him; nengō routinely straddle period boundaries. Nothing is
   * disputed and nothing is wrong, but it looks like a data error, so it has
   * to be sayable.
   */
  | "overlaps-parent";

export const DISCLOSURE_LABEL: Record<DisclosureReason, string> = {
  "rival-chronologies": "Chronologies differ",
  "method-conflict": "Methods disagree",
  definitional: "Depends on definition",
  "traditional-date": "Traditional date",
  calibration: "Calibration-dependent",
  "wide-uncertainty": "Broad range",
  "overlaps-parent": "Crosses its period",
};

/**
 * Caveats that belong to an ENTITY rather than to one of its boundaries.
 *
 * Splitting these out was forced by the data. The dataset's `misconceptions`
 * entries are not about dates at all — "the Ghana Empire was not in modern
 * Ghana", "the Maya never formed a single unified empire". Those are
 * geographic and conceptual corrections attached to the subject, and hanging
 * them off a start or end date would be nonsense.
 *
 * They matter disproportionately for a novice-facing tool: a reader who
 * leaves believing the Ghana Empire sat in modern Ghana has been actively
 * misled, which is worse than being left uncertain.
 */
export type EntityCaveatKind =
  /** A widely held belief that is simply wrong. */
  | "misconception"
  /** The name misleads — Ghana, Benin, Holy Roman Empire, Byzantine. */
  | "naming-confusion"
  /** Existence or identity is contested: Gilgamesh, David, Nitocris. */
  | "contested-existence";

export const CAVEAT_LABEL: Record<EntityCaveatKind, string> = {
  misconception: "Common misconception",
  "naming-confusion": "Name is misleading",
  "contested-existence": "Existence contested",
};

export interface EntityCaveat {
  kind: EntityCaveatKind;
  /** One sentence. Brevity is enforced — see MAX_CAVEAT_LENGTH. */
  text: string;
  sourceIds?: string[];
}

/**
 * Cap on caveat and note length.
 *
 * The app is a starting point, not a research tool, and prose is where that
 * scope quietly erodes. A hard limit keeps a caveat to something a reader
 * absorbs in passing and pushes anything longer out to the handoff link,
 * which is where the argument belongs.
 */
export const MAX_CAVEAT_LENGTH = 200;

/**
 * The dating of ONE boundary — a start or an end, not an entity.
 *
 * Attaching disclosure to the entity would be wrong: the Roman Empire's start
 * is not controversial, while its end is one of the most argued dates in the
 * field (476? 480? 1453?) and is a definitional dispute rather than an
 * evidential one. Boundaries carry their own arguments, so they carry their
 * own dating.
 */
export interface BoundaryDating {
  primary: DatingClaim;
  alternatives?: DatingClaim[];
  /** Stated reasons. Combined with inferred ones by `disclosureReasons()`. */
  reasons?: DisclosureReason[];
  /** Why the field is divided, as opposed to merely imprecise. */
  note?: string;
  /**
   * This boundary legitimately falls outside its parent's range.
   * Mirrors the dataset's existing `allow_outside_parent_dates` flag.
   */
  outsideParent?: boolean;
}

/** Uncertainty at or above this fraction of a date's age reads as "broad". */
export const WIDE_UNCERTAINTY_RATIO = 0.1;
/**
 * Reasons to disclose, stated and inferred together.
 *
 * Some reasons are derivable, and deriving them keeps authors from having to
 * restate the obvious: a claim marked `traditional` is self-evidently a
 * traditional date, and a range spanning a tenth of its own age is
 * self-evidently broad. Authoring effort should go to the reasons that
 * genuinely need a human — why two methods conflict, or where a definitional
 * line is being drawn.
 */
export function disclosureReasons(d: BoundaryDating): DisclosureReason[] {
  const out = new Set<DisclosureReason>(d.reasons ?? []);

  if (d.primary.standing === "traditional") out.add("traditional-date");
  if (d.outsideParent === true) out.add("overlaps-parent");

  const alternatives = d.alternatives ?? [];
  if (alternatives.length > 0) {
    const methods = new Set(
      [d.primary, ...alternatives].map((c) => c.value.method ?? "unknown"),
    );
    out.add(methods.size > 1 ? "method-conflict" : "rival-chronologies");
  }

  const uncertainty = uncertaintyOf(d.primary.value);
  const age = Math.abs(d.primary.value.consensus.year);
  if (uncertainty !== undefined && age > 0 && uncertainty / age >= WIDE_UNCERTAINTY_RATIO) {
    out.add("wide-uncertainty");
  }

  return [...out];
}

/**
 * Should the UI render a disclosure marker at all?
 *
 * Undisputed dates must stay completely clean. A marker on every date is the
 * same as no marker: it stops carrying information and becomes visual noise.
 */
export function hasDisclosure(d: BoundaryDating): boolean {
  return disclosureReasons(d).length > 0 || d.note !== undefined;
}

/**
 * One-phrase summary for the marker itself, before anything is opened.
 * Returns the most consequential reason when several apply.
 */
const REASON_PRIORITY: readonly DisclosureReason[] = [
  "definitional",
  "rival-chronologies",
  "method-conflict",
  "traditional-date",
  "overlaps-parent",
  "calibration",
  "wide-uncertainty",
];

/**
 * Display order for competing claims. Primary always leads regardless.
 *
 * `superseded` sorts last but is never hidden: a reader who encountered the
 * old date somewhere else needs to find it here and be told it is old.
 * Silently dropping it leaves them thinking the app is wrong.
 */
const STANDING_ORDER: Record<ClaimStanding, number> = {
  consensus: 0,
  majority: 1,
  minority: 2,
  traditional: 3,
  superseded: 4,
};

export function disclosureSummary(d: BoundaryDating): string | undefined {
  const reasons = new Set(disclosureReasons(d));
  const top = REASON_PRIORITY.find((r) => reasons.has(r));
  return top === undefined ? undefined : DISCLOSURE_LABEL[top];
}

/** Every claim for a boundary: primary first, then the rest by standing. */
export function allClaims(d: BoundaryDating): DatingClaim[] {
  const rest = [...(d.alternatives ?? [])].sort(
    (a, b) => STANDING_ORDER[a.standing] - STANDING_ORDER[b.standing],
  );
  return [d.primary, ...rest];
}

/** Caveats worth surfacing, filtered of any that exceed the length cap. */
export function entityCaveats(caveats: readonly EntityCaveat[] | undefined): EntityCaveat[] {
  return (caveats ?? []).filter((c) => c.text.length > 0);
}
