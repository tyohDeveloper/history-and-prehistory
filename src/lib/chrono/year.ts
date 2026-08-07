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

export interface YearValue {
  /** Point estimate, historical Gregorian. Negative = BCE, no year zero. */
  year: number;
  /** Lower bound of the plausible range, if known. Inclusive. */
  min?: number;
  /** Upper bound of the plausible range, if known. Inclusive. */
  max?: number;
  method?: DatingMethod;
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
 * Half-width of the uncertainty interval, or `undefined` if unbounded.
 * Used to decide how hard to round a value before displaying it.
 */
export function uncertaintyOf(v: YearValue): number | undefined {
  if (v.min === undefined || v.max === undefined) return undefined;
  return Math.max(Math.abs(v.year - v.min), Math.abs(v.max - v.year));
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
