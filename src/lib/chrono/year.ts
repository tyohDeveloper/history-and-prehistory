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
 * Dating methods that are not calendar-derived. Anything in this set should
 * be rendered in BP and should carry a visible method flag: a calibrated
 * radiocarbon date and a historically attested date are not the same kind of
 * claim, and the readout should not present them identically.
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
