/**
 * Before Present (BP) rendering, and the rounding discipline that goes with
 * deep time.
 *
 * ## The datum
 *
 * BP counts backward from **1950 CE**, not from today. That is a convention
 * of radiocarbon dating, fixed so published dates do not drift as the years
 * pass. It is not "years ago" and the difference is worth surfacing: at
 * Holocene scale the ~76-year offset is real, and at Pleistocene scale it is
 * noise. `bpFromYear` is exact regardless.
 *
 * ## Why rounding is a correctness concern, not cosmetics
 *
 * Writing "3,300,000 BP" for the start of the Oldowan asserts seven
 * significant figures for a boundary uncertain by hundreds of millennia. The
 * digits are not merely useless, they are false. So magnitude and
 * uncertainty together decide how a value is rendered:
 *
 *   - under 10,000 BP        -> whole years            "8,200 BP"
 *   - under 1,000,000 BP     -> thousands, "ka"        "12.5 ka"
 *   - at or above 1,000,000  -> millions, "Ma"         "3.3 Ma"
 *
 * and when an explicit uncertainty range is present, the point estimate is
 * rounded to that interval's own resolution so the two never disagree.
 */

import { toAstronomical, type YearValue } from "./year";

/** The BP datum, in historical Gregorian years. */
export const BP_DATUM_YEAR = 1950;

/**
 * Convert a historical Gregorian year to years Before Present.
 *
 * Uses astronomical numbering internally so the absent year zero does not
 * introduce an off-by-one: 1 BCE is 1950 BP, 1 CE is 1949 BP.
 */
export function bpFromYear(historicalYear: number): number {
  return BP_DATUM_YEAR - toAstronomical(historicalYear);
}

export function yearFromBp(bp: number): number {
  const astronomical = BP_DATUM_YEAR - bp;
  return astronomical <= 0 ? astronomical - 1 : astronomical;
}

export type BpUnit = "yr" | "ka" | "Ma";

export function bpUnitFor(bp: number): BpUnit {
  const magnitude = Math.abs(bp);
  if (magnitude >= 1_000_000) return "Ma";
  if (magnitude >= 10_000) return "ka";
  return "yr";
}

/** Round `value` to a step derived from the size of the uncertainty. */
function roundToUncertainty(value: number, uncertainty: number | undefined): number {
  if (uncertainty === undefined || uncertainty <= 0) return value;
  // One significant figure of the uncertainty sets the resolution: an
  // interval of +/-2,400 years is quoted to the nearest 1,000.
  const step = Math.pow(10, Math.floor(Math.log10(uncertainty)));
  return Math.round(value / step) * step;
}

function formatMagnitude(bp: number, unit: BpUnit, uncertainty?: number): string {
  if (unit === "yr") {
    return Math.round(roundToUncertainty(bp, uncertainty)).toLocaleString("en-US");
  }
  const divisor = unit === "Ma" ? 1_000_000 : 1_000;
  const scaled = bp / divisor;
  const scaledUncertainty = uncertainty === undefined ? undefined : uncertainty / divisor;
  // Show enough decimals to resolve the uncertainty, capped at two.
  let decimals = 1;
  if (scaledUncertainty !== undefined && scaledUncertainty > 0) {
    decimals = Math.min(2, Math.max(0, -Math.floor(Math.log10(scaledUncertainty))));
  } else if (scaled >= 100) {
    decimals = 0;
  }
  return scaled.toLocaleString("en-US", {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  });
}

export interface BpFormatOptions {
  /** Append the unit label. Default true. */
  withUnit?: boolean;
}

/**
 * Render a single year as BP at an appropriate resolution.
 * `uncertainty` is a half-width in years, if known.
 */
export function formatBp(
  historicalYear: number,
  uncertainty?: number,
  options: BpFormatOptions = {},
): string {
  const bp = bpFromYear(historicalYear);
  if (bp <= 0) {
    // After the datum. "AP" (After Present) is not standard usage, so fall
    // back to plain CE rather than inventing a label.
    return `${historicalYear.toLocaleString("en-US")} CE`;
  }
  const unit = bpUnitFor(bp);
  const magnitude = formatMagnitude(bp, unit, uncertainty);
  if (options.withUnit === false) return magnitude;
  return unit === "yr" ? `${magnitude} BP` : `${magnitude} ${unit}`;
}

/**
 * Render a `YearValue` as a BP range.
 *
 * When bounds are present they are rendered as the range, because at this
 * scale the range *is* the claim — a point estimate with a 200,000-year
 * interval is not a date, it is the midpoint of one.
 */
export function formatBpRange(v: YearValue): string {
  const hasBounds = v.min !== undefined && v.max !== undefined;
  if (!hasBounds) {
    return formatBp(v.year);
  }
  const older = Math.min(v.min as number, v.max as number);
  const younger = Math.max(v.min as number, v.max as number);
  const olderBp = bpFromYear(older);
  const youngerBp = bpFromYear(younger);
  const halfWidth = (olderBp - youngerBp) / 2;
  const unit = bpUnitFor(Math.max(olderBp, youngerBp));
  const a = formatMagnitude(olderBp, unit, halfWidth);
  const b = formatMagnitude(youngerBp, unit, halfWidth);
  if (a === b) return `${a} ${unit === "yr" ? "BP" : unit}`;
  return `${a}\u2013${b} ${unit === "yr" ? "BP" : unit}`;
}

/**
 * Should this value be presented in BP rather than in calendars?
 *
 * Two triggers, either sufficient:
 *   - the date comes from a scientific dating method rather than a calendar
 *   - it is old enough that calendar reckoning is not meaningful
 *
 * The 10,000 BP threshold is deliberately near the Holocene boundary
 * (~11,700 BP), which is also where the Deep Time app hands off. No calendar
 * in the registry has a meaningful epoch anywhere near it.
 */
export const BP_PREFERRED_THRESHOLD_BP = 10_000;

export function prefersBp(v: YearValue): boolean {
  if (v.method !== undefined && v.method !== "calendar" && v.method !== "unknown") {
    return true;
  }
  return bpFromYear(v.year) >= BP_PREFERRED_THRESHOLD_BP;
}
