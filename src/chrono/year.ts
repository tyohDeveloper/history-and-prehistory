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

// ---------------------------------------------------------------------------
// Year numbering: two schemes, kept apart by the type system.
// ---------------------------------------------------------------------------

/**
 * **ISO astronomical year.** Has a year zero: 1 BCE is 0, 2 BCE is -1.
 *
 * This is the canonical internal representation. Everything downstream —
 * arithmetic, BP, comparison, sorting — operates on it. It is what Temporal
 * uses natively, so nothing has to be converted at the arithmetic boundary,
 * and BP reduces to one subtraction with no special case at the era boundary.
 */
declare const IsoYearBrand: unique symbol;
export type IsoYear = number & { readonly [IsoYearBrand]: true };

/**
 * **Historical year.** No year zero: -753 means 753 BCE, 1 means 1 CE.
 *
 * The authoring scheme. All 1,305 entities in `src/data` use it, and
 * historians write it. It exists only at the edges: JSON in, display out.
 */
declare const HistoricalYearBrand: unique symbol;
export type HistoricalYear = number & { readonly [HistoricalYearBrand]: true };

/**
 * The two schemes differ by one for every BCE date and by nothing for CE
 * dates, which is precisely why this needs a type and not a convention.
 * `-753` and `-752` are both entirely plausible values for the founding of
 * Rome, so a mix-up survives code review indefinitely. Branding makes it a
 * compile error instead.
 *
 * These four functions are the ONLY sanctioned crossings. Everything else
 * takes one type or the other and cannot silently accept the wrong one.
 */
export function isoFromHistorical(year: HistoricalYear): IsoYear {
  if ((year as number) === 0) {
    throw new RangeError("Year zero does not exist in historical numbering.");
  }
  return ((year as number) < 0 ? (year as number) + 1 : (year as number)) as IsoYear;
}

export function historicalFromIso(year: IsoYear): HistoricalYear {
  return ((year as number) <= 0 ? (year as number) - 1 : (year as number)) as HistoricalYear;
}

/** Tag a raw number arriving from the dataset as a historical year. */
export function asHistorical(n: number): HistoricalYear {
  if (n === 0) throw new RangeError("Year zero does not exist in historical numbering.");
  return n as HistoricalYear;
}

/** Tag a raw number as already being an ISO year. Rare; prefer `ce`/`bce`. */
export function asIso(n: number): IsoYear {
  return n as IsoYear;
}

/**
 * Readable constructors for fixtures and literals.
 *
 * `bce(753)` says what it means; `-752` does not, and `-753` is wrong. Using
 * these everywhere a year is written by hand removes the last place the
 * off-by-one can hide.
 */
export function ce(year: number): IsoYear {
  if (year < 1) throw new RangeError(`ce() expects a positive year, got ${year}`);
  return year as IsoYear;
}

export function bce(year: number): IsoYear {
  if (year < 1) throw new RangeError(`bce() expects a positive year, got ${year}`);
  return (1 - year) as IsoYear;
}

export type DatingMethod =
  | "calendar"
  | "radiocarbon-calibrated"
  | "radiocarbon-uncalibrated"
  | "argon-argon"
  | "potassium-argon"
  | "luminescence"
  | "uranium-series"
  | "esr"
  /** Ice-core and varve annual layer counting. Reports a maximum counting error. */
  | "layer-counting"
  | "magnetostratigraphy"
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
  /** The stated value as an ISO astronomical year. Build with `ce` / `bce`. */
  year: IsoYear;
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
export type NativeFrame = Datum | "calendar";

/**
 * Zero point for a "years before" count.
 *
 * Radiocarbon fixed BP at 1950 CE. Ice-core chronologies use **b2k**, before
 * 2000 CE — a 50-year offset that is small but systematic, and one the
 * literature is explicit about not eliding: Walker et al. state it directly
 * when defining the Holocene GSSP, and the advice for datasets is to store
 * b2k, BP, and BCE separately with the offset applied.
 *
 * It matters more than 50 years sounds. The Younger Dryas termination is
 * quoted at 11,703 b2k with a maximum counting error of 99 years; silently
 * treating that as BP moves it by half its own stated uncertainty.
 */
export type Datum = "bp" | "b2k";

export const DATUM_YEAR: Record<Datum, number> = { bp: 1950, b2k: 2000 };

export const DATUM_LABEL: Record<Datum, string> = { bp: "BP", b2k: "b2k" };

/**
 * The date in its own cultural calendar — **the authoritative form**.
 *
 * Where a `NativeValue` is present it is not a fidelity backup for the ISO
 * value. It is the fact, and the ISO value is a derived index. The Battle of
 * Karbala happened on **10 Muharram 61 AH**; that is the date, it is Ashura,
 * and it is observed annually on a Hijri anniversary with no fixed Gregorian
 * counterpart. "13 October 680" is a cross-reference we compute so the event
 * can be sorted and placed beside Tang China — useful, and not what happened.
 *
 * ## The conversion can be less precise than the original
 *
 * This inverts the usual assumption. 10 Muharram 61 AH is exact: one
 * unambiguous day. Its ISO conversion is not — measured against the polyfill,
 * the three Hijri variants disagree by two days:
 *
 *     islamic-umalqura -> 0680-10-13
 *     islamic-civil    -> 0680-10-13
 *     islamic-tbla     -> 0680-10-12
 *
 * Each variant round-trips its own value perfectly, so nothing is broken. The
 * uncertainty is introduced by the conversion; it is not carried by the
 * original. `conversionFuzzDays` records it, so a readout neither presents a
 * derived date as sharper than the derivation allows, nor lets the derivation
 * cast doubt on a native date that has none.
 */
export interface NativeValue {
  /** Calendar id from the registry. */
  calendarId: string;
  /** Verbatim as a source would write it: "10 Muharram 61 AH". */
  text: string;
  year?: number;
  month?: number;
  day?: number;
  /** A culturally salient name for the day: Ashura, Nowruz, Yom Kippur. */
  observance?: string;
  /**
   * Uncertainty introduced by converting to ISO, in days. Independent of —
   * and often larger than — any uncertainty in the native date itself.
   */
  conversionFuzzDays?: number;
}

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
  /**
   * The frame and datum the source quoted in. Display is chosen separately;
   * this exists so a conversion cannot silently restate the source.
   */
  nativeFrame?: NativeFrame;
  /**
   * The authoritative date in its own cultural calendar, where one exists.
   * Present means the native form leads the readout and ISO is the index.
   */
  native?: NativeValue;
  /** Free text for genuine scholarly disagreement, as opposed to imprecision. */
  note?: string;
}

/**
 * Does this value have an authoritative form in another calendar?
 *
 * When true the readout leads with the native date and offers ISO as the
 * cross-reference, not the other way round. A per-entity display decision
 * derived from the data rather than a user preference — see `Q-18`.
 */
export function hasAuthoritativeNative(v: YearValue): boolean {
  return v.native !== undefined;
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
export function supportOf(v: YearValue): { earliest: IsoYear; latest: IsoYear } | undefined {
  if (v.earliest === undefined && v.latest === undefined) return undefined;
  const e = v.earliest ?? v.consensus;
  const l = v.latest ?? v.consensus;
  return {
    earliest: asIso((e.year as number) - (e.fuzz ?? 0)),
    latest: asIso((l.year as number) + (l.fuzz ?? 0)),
  };
}

/**
 * Outer limit of the date regime, in years either side of the ISO epoch.
 *
 * Temporal cannot represent a date beyond roughly +/-271,821 years — asking
 * for 3.3 Ma throws a RangeError, verified against the polyfill. That is not
 * a limitation to work around; it marks a real boundary between two kinds of
 * quantity.
 *
 * Inside it, a value is a **date**: it has a position in every calendar, it
 * round-trips exactly at day precision, and calendar conversion is meaningful.
 * Outside it, a value is a **number of years**. No calendar reaches the
 * Paleolithic, so nothing is lost by treating deep time as a scalar in BP.
 *
 * The seam sits far outside any calendar's meaningful range — the oldest
 * epoch in the registry is Byzantine AM at 5508 BCE — so it never bisects
 * anything a user would expect to convert.
 */
export const DATE_REGIME_LIMIT_YEARS = 271_821;

export function isDateRegime(year: IsoYear): boolean {
  return Math.abs(year as number) <= DATE_REGIME_LIMIT_YEARS;
}

/**
 * The Before Present datum, 1950 CE. Defined here rather than in `bp.ts`
 * because the uncertainty ratio below needs it, and `bp.ts` already imports
 * from this module. Re-exported from `bp.ts` for callers who expect it there.
 */
export const BP_DATUM_YEAR = DATUM_YEAR.bp;

/**
 * Distance from the BP datum, always positive.
 *
 * This is the right denominator for "is this uncertainty large?", and using
 * `|year|` instead was a bug: the denominator collapses toward year zero, so a
 * date of 1 CE with a five-year error scored a ratio of 5.0 and every date
 * near the era boundary looked wildly uncertain. Distance from the datum is
 * monotonic across the whole range and never collapses.
 *
 * It also produces the right *judgement*, not just the right arithmetic: the
 * same fifty-year error is unremarkable on a Bronze Age date and glaring on a
 * Victorian one, which is how historians actually read precision.
 */
export function distanceFromDatum(year: IsoYear): number {
  return Math.max(Math.abs(BP_DATUM_YEAR - (year as number)), 1);
}

/** Whole years between two ISO years. Plain subtraction; no year-zero gap. */
export function yearsBetween(from: IsoYear, to: IsoYear): number {
  return (to as number) - (from as number);
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
    Math.abs((v.consensus.year as number) - (support.earliest as number)),
    Math.abs((support.latest as number) - (v.consensus.year as number)),
  );
}

/**
 * Dating methods that are not calendar-derived. A calibrated radiocarbon date
 * and a historically attested date are not the same kind of claim, and the
 * readout should not present them identically.
 */
/**
 * Methods that produce a measurement rather than a reckoning.
 *
 * Defined as the complement of the calendar-ish ones rather than as a list of
 * the measured ones. The explicit-list version silently omitted argon-argon,
 * uranium-series, magnetostratigraphy and layer-counting \u2014 four of the ten
 * methods in the enum \u2014 which meant `isScientificDating` returned false for an
 * Ar/Ar date. Nothing broke only because everything dated that way is old
 * enough for the pre-Holocene backstop to reach the same answer by luck.
 *
 * As a complement, a method added to the enum later defaults to "measured",
 * which is the safe direction: it leads to BP, which is always expressible.
 */
const CALENDAR_METHODS: ReadonlySet<DatingMethod> = new Set(["calendar", "unknown"]);

/**
 * Which of the three senses of "before present" a method produces.
 *
 * These are not interchangeable and the distinction is not cosmetic:
 *
 * - `cal` \u2014 calendar-equivalent years counted from 1950. Calibrated
 *   radiocarbon and annual layer counts. Freely convertible to CE/BCE.
 * - `radiocarbon` \u2014 UNCALIBRATED radiocarbon years. These are *not* calendar
 *   years. The relationship to real time is the calibration curve, which is
 *   neither linear nor monotonic in its wiggles, so there is no arithmetic
 *   that turns a \u00B9\u2074C year into a CE date. See `isCalendarConvertible`.
 * - `geological` \u2014 "years ago", never referenced to 1950 at all. At Ma scale
 *   the 1950 offset is 0.00006% and numerically ignorable, but the label must
 *   not claim a datum the measurement does not have.
 */
export type BpSense = "cal" | "radiocarbon" | "geological" | "calendar";

const BP_SENSE: Partial<Record<DatingMethod, BpSense>> = {
  calendar: "calendar",
  "radiocarbon-calibrated": "cal",
  "layer-counting": "cal",
  "radiocarbon-uncalibrated": "radiocarbon",
  "argon-argon": "geological",
  "potassium-argon": "geological",
  "uranium-series": "geological",
  luminescence: "geological",
  esr: "geological",
  magnetostratigraphy: "geological",
};

export function bpSenseOf(v: YearValue): BpSense {
  if (v.method === undefined) return "calendar";
  return BP_SENSE[v.method] ?? "calendar";
}

/** Unit-independent label for a sense: what follows the number. */
export const BP_SENSE_LABEL: Record<BpSense, string> = {
  cal: "cal BP",
  radiocarbon: "\u00B9\u2074C BP",
  geological: "ago",
  calendar: "BP",
};

/**
 * Whether a value can honestly be shown as a calendar date.
 *
 * The frame model is built on BP and calendar reckoning being exactly
 * interconvertible, which makes the choice between them purely a display
 * decision. That premise holds for every method here except one.
 *
 * An uncalibrated radiocarbon age is a measurement in \u00B9\u2074C years, and \u00B9\u2074C years
 * are not calendar years \u2014 atmospheric \u00B9\u2074C has varied, so the mapping is an
 * empirical curve, not an offset. Rendering "7,500 \u00B9\u2074C BP" as "5551 BCE" would
 * be inventing a calendar date that the measurement does not support, and the
 * error is centuries in the worst parts of the curve.
 *
 * So this is the one case where the UI must refuse rather than convert, even
 * against an explicit user preference.
 */
export function isCalendarConvertible(v: YearValue): boolean {
  return bpSenseOf(v) !== "radiocarbon";
}

export function isScientificDating(v: YearValue): boolean {
  return v.method !== undefined && !CALENDAR_METHODS.has(v.method);
}

export const DATING_METHOD_LABEL: Record<DatingMethod, string> = {
  calendar: "Calendar / historically attested",
  "radiocarbon-calibrated": "Radiocarbon, calibrated",
  "radiocarbon-uncalibrated": "Radiocarbon, uncalibrated",
  "argon-argon": "Argon-argon (\u2074\u2070Ar/\u00B3\u2079Ar)",
  "potassium-argon": "Potassium-argon",
  luminescence: "Luminescence (OSL/TL)",
  "uranium-series": "Uranium-series",
  esr: "Electron spin resonance",
  "layer-counting": "Annual layer counting",
  magnetostratigraphy: "Magnetostratigraphy",
  typological: "Typological / stylistic",
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
  /**
   * The date was revised, and the argument is over.
   *
   * Critically NOT a live dispute. *Homo floresiensis* moved from ~18 ka to
   * ~60 ka in 2016 and nobody defends the old figure; Neanderthal late
   * survival at 28 ka collapsed once ultrafiltration removed modern-carbon
   * contamination. Marking either as "methods disagree" would be false — they
   * agreed, and one side lost. The old value still has to be reachable
   * because readers meet it in older books, but the reader must be told the
   * question is settled.
   */
  | "revised"
  /** Value depends on calibration choice or correlation constant. */
  | "calibration"
  /**
   * The evidence is challenged, not just the number.
   *
   * Distinct from `method-conflict`, where two techniques give two answers.
   * Here the objection is that the technique does not date the thing at all:
   * the Chauvet critique argues the radiocarbon dates charcoal, not the art
   * on the wall. A reader told "methods disagree" would draw the wrong
   * conclusion, because a rival number is not what is on offer.
   */
  | "evidence-disputed"
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
  "evidence-disputed": "Evidence questioned",
  revised: "Date revised",
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
  /**
   * ISO date at which this dating was last checked against the literature.
   *
   * Live disputes have a shelf life. Monte Verde is under active challenge as
   * of mid-2026 — a March 2026 paper proposed moving it by six thousand years,
   * roughly thirty specialists rebutted it in May, and the authors replied in
   * June. An entry recording that state is useful; an entry recording it
   * without saying when is a trap, because a reader cannot tell whether the
   * argument was resolved last week.
   *
   * Only meaningful where a dispute is genuinely open. Settled dates do not
   * need it and should not carry it.
   */
  asOf?: string;
}

/**
 * Uncertainty at or above this fraction of a date's distance from the datum
 * reads as "broad".
 *
 * Lowered from 0.10 after measuring against real data. At 0.10 the marker was
 * dead code: across eight prehistory cases chosen specifically for being
 * uncertain, plus the three v2.1.0 entities carrying bounds, the observed
 * range was 0.002 to 0.092 and nothing fired.
 *
 *   Ashoka           0.002      Neanderthal end   0.026
 *   Younger Dryas    0.008      Bronze Age        0.057
 *   Gobekli Tepe     0.017      Chauvet Phase I   0.069
 *   Oldowan          0.019      Madjedbebe        0.092
 *
 * Madjedbebe at 65 +/- 6 ka is the clearest case that should fire and the
 * only one above 0.08, so that is where the line sits. Still provisional —
 * eleven samples is not a distribution, and the honest reason for moving it
 * is that a marker which never fires is worse than one calibrated loosely.
 */
export const WIDE_UNCERTAINTY_RATIO = 0.08;
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
    // If every alternative is superseded, the argument is finished. Reporting
    // that as a disagreement would misdescribe a resolved question, so the
    // settled case is checked before the disputed ones.
    if (alternatives.every((c) => c.standing === "superseded")) {
      out.add("revised");
    } else {
      const live = [d.primary, ...alternatives].filter((c) => c.standing !== "superseded");
      const methods = new Set(live.map((c) => c.value.method ?? "unknown"));
      out.add(methods.size > 1 ? "method-conflict" : "rival-chronologies");
    }
  }

  const uncertainty = uncertaintyOf(d.primary.value);
  if (
    uncertainty !== undefined &&
    uncertainty / distanceFromDatum(d.primary.value.consensus.year) >= WIDE_UNCERTAINTY_RATIO
  ) {
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
  "evidence-disputed",
  "definitional",
  "rival-chronologies",
  "method-conflict",
  "revised",
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

/**
 * Disclosure across both boundaries of an entity, deduplicated.
 *
 * Measured against the real dataset, eight entities produce the identical
 * marker on start and end — every legendary founder whose accession and death
 * are both traditional dates. Rendering "Traditional date" twice on one
 * record is noise, and noise is the specific failure mode a disclosure marker
 * cannot afford: a mark that appears everywhere stops being read.
 *
 * When both boundaries say the same thing, say it once against the entity.
 */
export interface DisclosureRollup {
  shared?: string;
  start?: string;
  end?: string;
}

export function rollupDisclosure(
  start: BoundaryDating | undefined,
  end: BoundaryDating | undefined,
): DisclosureRollup {
  const a = start === undefined ? undefined : disclosureSummary(start);
  const b = end === undefined ? undefined : disclosureSummary(end);
  if (a !== undefined && a === b) return { shared: a };
  const out: DisclosureRollup = {};
  if (a !== undefined) out.start = a;
  if (b !== undefined) out.end = b;
  return out;
}

/** Caveats worth surfacing, filtered of any that exceed the length cap. */
export function entityCaveats(caveats: readonly EntityCaveat[] | undefined): EntityCaveat[] {
  return (caveats ?? []).filter((c) => c.text.length > 0);
}
