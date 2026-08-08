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

import {
  asIso,
  BP_DATUM_YEAR,
  DATUM_LABEL,
  DATUM_YEAR,
  isCalendarConvertible,
  isScientificDating,
  supportOf,
  uncertaintyOf,
  BP_SENSE_LABEL,
  type BpSense,
  type Datum,
  type IsoYear,
  type YearValue,
} from "./year";

export { BP_DATUM_YEAR };

/**
 * Convert a historical Gregorian year to years Before Present.
 *
 * Uses astronomical numbering internally so the absent year zero does not
 * introduce an off-by-one: 1 BCE is 1950 BP, 1 CE is 1949 BP.
 */
/**
 * Years before the datum.
 *
 * One subtraction. Before the ISO refactor this called `toAstronomical` on
 * every invocation, so the year-zero crossing happened inside arithmetic,
 * repeatedly, at every call site that wanted a BP value. Now the crossing
 * happens once when the dataset is loaded and this is just the axis with its
 * origin moved — which is all BP ever was.
 */
export function bpFromYear(year: IsoYear, datum: Datum = "bp"): number {
  return DATUM_YEAR[datum] - (year as number);
}

export function yearFromBp(bp: number, datum: Datum = "bp"): IsoYear {
  return asIso(DATUM_YEAR[datum] - bp);
}

export type BpUnit = "yr" | "ka" | "Ma";

/** Years per unit. Exported so callers can test whether a value fits a unit. */
export const BP_UNIT_DIVISOR: Record<BpUnit, number> = { yr: 1, ka: 1_000, Ma: 1_000_000 };

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
  const divisor = BP_UNIT_DIVISOR[unit];
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
  /** Which sense of "before present" this is; sets the suffix. */
  sense?: BpSense;
  /**
   * Force the unit instead of choosing one from the value's own magnitude.
   *
   * A range must be quoted in a single unit. Left to itself, each end picks
   * its own, and Göbekli Tepe comes out as "11.5 ka – 9,949 BP" — two units in
   * one range, which reads as a change of subject rather than a span. The
   * caller picks the unit from the older end and passes it for both.
   */
  unit?: BpUnit;
}

/**
 * Render a single year as BP at an appropriate resolution.
 * `uncertainty` is a half-width in years, if known.
 */
export function formatBp(
  year: IsoYear,
  uncertainty?: number,
  options: BpFormatOptions & { datum?: Datum } = {},
): string {
  const datum = options.datum ?? "bp";
  const bp = bpFromYear(year, datum);
  if (bp <= 0) {
    // After the datum. "AP" (After Present) is not standard usage, so fall
    // back to plain CE rather than inventing a label.
    return `${(year as number).toLocaleString("en-US")} CE`;
  }
  const unit = options.unit ?? bpUnitFor(bp);
  const magnitude = formatMagnitude(bp, unit, uncertainty);
  if (options.withUnit === false) return magnitude;
  return `${magnitude} ${bpSuffix(unit, options.sense, datum)}`;
}

/**
 * What follows the number: unit plus the sense of "before present".
 *
 * Kept separate from `formatBp` because a range needs the suffix ONCE, not on
 * both ends. "3.3 Ma ago \u2013 2.6 Ma ago" repeats itself; "3.3 \u2013 2.6 Ma ago" does
 * not. Callers formatting a range pass `withUnit: false` for both ends and
 * append this themselves.
 */
export function bpSuffix(
  unit: BpUnit,
  sense: BpSense | undefined,
  datum: Datum = "bp",
): string {
  // b2k is quoted as such whatever the method: the source's datum wins.
  if (datum === "b2k") return unit === "yr" ? DATUM_LABEL.b2k : `${unit} b2k`;
  const s = sense ?? "calendar";
  if (unit === "yr") {
    // "4,949 ago" is not English. A bare count needs the noun.
    return s === "geological" ? "years ago" : BP_SENSE_LABEL[s];
  }
  switch (s) {
    case "geological":
      return `${unit} ago`;
    case "cal":
      return `${unit} cal BP`;
    case "radiocarbon":
      return `${unit} \u00B9\u2074C BP`;
    default:
      return unit;
  }
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
 * Which frame *leads* for a value, and who decides.
 *
 * BP and calendar reckoning are interconvertible for every method here except
 * one, so this is a display decision, never a storage one. Someone reading
 * about Cyrus may legitimately want BP, and nothing should stop them. The
 * automatic choice is a *default* and the user preference normally wins.
 *
 * The exception is uncalibrated radiocarbon, where no calendar equivalent
 * exists to be shown. See `isCalendarConvertible` and `resolveFrame`.
 *
 * The automatic choice is driven by provenance rather than age. Stonehenge
 * (c. 2500 BCE) is a radiocarbon date and leads in BP; Alexander is fixed by
 * king lists and eclipse synchronisms and leads in BCE. Age would get both
 * wrong. Writing "2500 BCE" asserts a position in a calendar nobody was
 * keeping; BP asserts only a count from a datum, which is the right shape for
 * a measurement.
 *
 *   1. quoted natively in a frame  -> that frame
 *   2. measured                    -> BP
 *   3. reckoned                    -> calendar
 *   4. unknown                     -> shape of the uncertainty, not the age
 *   5. backstop                    -> pre-Holocene is BP; no calendar reaches
 *
 * Step 4 uses relative fuzziness as a proxy for provenance: a date whose
 * uncertainty is a large fraction of its own age is doing measurement-shaped
 * work whatever its source. See DESIGN.md Q-17.
 */
/**
 * `b2k` is a display frame in its own right, not a rendering detail of BP.
 * Ice-core literature quotes it directly, and a readout that silently
 * converted b2k to BP would restate the source by 50 years — half the stated
 * counting error on the Younger Dryas termination.
 */
export type DisplayFrame = Datum | "calendar";
export type FramePreference = "auto" | DisplayFrame;

export const HOLOCENE_BACKSTOP_BP = 11_700;
export const UNKNOWN_METHOD_FUZZ_RATIO = 0.05;

/** The default frame for a value, absent any user preference. */
export function suggestFrame(v: YearValue): DisplayFrame {
  // A quoted native frame always wins: it is the only way to reproduce the
  // source's own number, including its datum and its rounding.
  if (v.nativeFrame !== undefined) return v.nativeFrame;
  const bp = bpFromYear(v.consensus.year);
  if (bp >= HOLOCENE_BACKSTOP_BP) return "bp";

  if (!isCalendarConvertible(v)) return "bp";
  if (v.method !== undefined && v.method !== "unknown") {
    return isScientificDating(v) ? "bp" : "calendar";
  }

  const uncertainty = uncertaintyOf(v);
  if (uncertainty === undefined || bp <= 0) return "calendar";
  return uncertainty / bp >= UNKNOWN_METHOD_FUZZ_RATIO ? "bp" : "calendar";
}

/**
 * The frame actually used, given a user preference.
 *
 * An explicit preference beats the automatic choice, including the
 * pre-Holocene backstop. Showing 3.3 Ma as a BCE year is not useful, but it is
 * not our place to refuse a conversion that exists — and the secondary line
 * keeps the other frame visible either way.
 *
 * There is exactly one conversion that does NOT exist, and it is the one case
 * where preference loses. Do not restore "preference always wins" here: this
 * docstring previously claimed it, four lines above the code that refuses.
 */
export function resolveFrame(v: YearValue, preference: FramePreference = "auto"): DisplayFrame {
  // The one case where preference does not win. An uncalibrated radiocarbon
  // age has no calendar equivalent to show, so "calendar" is not a display
  // choice here \u2014 it is a request for a number that does not exist.
  if (preference === "calendar" && !isCalendarConvertible(v)) return "bp";
  return preference === "auto" ? suggestFrame(v) : preference;
}
