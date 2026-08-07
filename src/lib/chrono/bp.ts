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

import { isScientificDating, supportOf, toAstronomical, uncertaintyOf, type YearValue } from "./year";

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
 * When bounds are present the range is rendered, because at this scale the
 * range *is* the claim — a point estimate carrying a 200,000-year interval is
 * not a date, it is the midpoint of one.
 */
export function formatBpRange(v: YearValue): string {
  const support = supportOf(v);
  if (support === undefined) {
    return formatBp(v.consensus.year, v.consensus.fuzz);
  }
  const olderBp = bpFromYear(support.earliest);
  const youngerBp = bpFromYear(support.latest);
  const halfWidth = (olderBp - youngerBp) / 2;
  const unit = bpUnitFor(Math.max(olderBp, youngerBp));
  const label = unit === "yr" ? "BP" : unit;
  const a = formatMagnitude(olderBp, unit, halfWidth);
  const b = formatMagnitude(youngerBp, unit, halfWidth);
  if (a === b) return `${a} ${label}`;
  return `${a}\u2013${b} ${label}`;
}

/**
 * Which frame should lead for this value: BP or calendar reckoning?
 *
 * Age is the wrong axis. Stonehenge (c. 2500 BCE) is a radiocarbon date and
 * belongs in BP; Alexander (also BCE) is fixed by king lists and eclipse
 * synchronisms and belongs in BCE. What separates them is where the number
 * came from.
 *
 * Writing "2500 BCE" asserts a position in a calendar nobody was keeping — a
 * back-projection, sometimes well anchored by attested records and sometimes
 * borrowed authority. BP asserts no calendar at all; it is a count from a
 * datum, which is the right shape for a measurement.
 *
 *   1. measured (radiocarbon, luminescence, K-Ar, ESR)  -> BP
 *   2. reckoned (calendar, attested)                     -> BCE/CE
 *   3. unknown  -> fall back on the shape of the uncertainty, not the age
 *   4. backstop -> pre-Holocene is always BP; no calendar reaches there
 *
 * Step 3 uses relative fuzziness as a proxy for provenance: a date whose
 * uncertainty is a large fraction of its own age is doing measurement-shaped
 * work whatever its source. See DESIGN.md Q-17 — the ratio wants checking
 * against real cases before it is treated as settled.
 */
export const HOLOCENE_BACKSTOP_BP = 11_700;
export const UNKNOWN_METHOD_FUZZ_RATIO = 0.05;

export function prefersBp(v: YearValue): boolean {
  const bp = bpFromYear(v.consensus.year);
  if (bp >= HOLOCENE_BACKSTOP_BP) return true;

  if (v.method !== undefined && v.method !== "unknown") {
    return isScientificDating(v);
  }

  const uncertainty = uncertaintyOf(v);
  if (uncertainty === undefined || bp <= 0) return false;
  return uncertainty / bp >= UNKNOWN_METHOD_FUZZ_RATIO;
}
