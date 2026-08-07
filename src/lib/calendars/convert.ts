/**
 * Reading an ISO year in another calendar.
 *
 * ## Why a year reads as a span
 *
 * Only calendars whose year begins on 1 January map one Gregorian year to one
 * of theirs. Everything else straddles: measured across a century, **100 of
 * 100** Gregorian years span two Islamic, Hebrew, Persian and Chinese years.
 * So the unit of conversion here is a *span*, not a point. Rendering a lunar
 * year as one number would be wrong about half the time.
 *
 * Byzantine AM (September start), Olympiad (midsummer) and French Republican
 * (autumn equinox) have the same property for a different reason.
 *
 * ## Why validity is part of the answer
 *
 * Every conversion below is *computable* far outside the range where it means
 * anything. Ask the polyfill for a Persian date in 3300 BCE and it returns
 * year -3921 without complaint. The registry's `validFrom`/`validTo` window is
 * what lets a reading say "before this calendar existed" instead of printing a
 * confident absurdity, so validity travels with every result rather than being
 * checked by callers who might forget.
 */

import { Temporal } from "../temporal/temporal";
import {
  gregorianToJDN,
  isInRevisedJulianEquivalenceWindow,
  jdnToGregorian,
  jdnToJulian,
} from "../temporal/julianJdn";
import { DATE_REGIME_LIMIT_YEARS, historicalFromIso, type IsoYear } from "../chrono/year";
import { getCalendar, type CalendarDef } from "./registry";

export type Validity =
  /** Inside the calendar's meaningful range. */
  | "ok"
  /** Computable, but before the calendar existed. Extrapolated backwards. */
  | "proleptic"
  /** Outside the range this build can compute at all. */
  | "outside-range"
  /** Beyond the date regime entirely — deep time has no calendars. */
  | "deep-time";

export interface CalendarReading {
  calendarId: string;
  /** Short name for the calendar, from the registry. */
  short: string;
  /** Display string, already spanned and labelled: "AH 897\u2013898". */
  label: string;
  /** Numeric year at the start of the ISO year, where meaningful. */
  from?: number;
  /** Numeric year at the end of the ISO year. Differs from `from` on a span. */
  to?: number;
  validity: Validity;
  /** Why the reading is qualified, when it is. */
  note?: string;
}

const SEXAGENARY_STEMS = ["Jia","Yi","Bing","Ding","Wu","Ji","Geng","Xin","Ren","Gui"];
const SEXAGENARY_BRANCHES = ["Zi","Chou","Yin","Mao","Chen","Si","Wu","Wei","Shen","You","Xu","Hai"];
/** GMT correlation. Competing correlations shift Long Count dates materially. */
const MAYA_CORRELATION_JDN = 584283;

function eraYearOf(d: Temporal.PlainDate): number {
  // Exotic calendars expose eraYear; cyclic ones (chinese, dangi) expose only
  // a related ISO year, which is the best available handle for a year label.
  return d.eraYear ?? d.year;
}

function temporalSpan(isoYear: number, temporalId: string): { from: number; to: number } {
  const jan = Temporal.PlainDate.from({ year: isoYear, month: 1, day: 1, calendar: "iso8601" });
  const dec = Temporal.PlainDate.from({ year: isoYear, month: 12, day: 31, calendar: "iso8601" });
  return {
    from: eraYearOf(jan.withCalendar(temporalId)),
    to: eraYearOf(dec.withCalendar(temporalId)),
  };
}

/**
 * Year in an epoch-offset calendar.
 *
 * Plain addition against the ISO year, deliberately *without* a year-zero
 * correction. It is tempting to add one, since AUC and Anno Mundi have no
 * year zero either — but the offset is defined against ISO, which does, so the
 * two cancel. AUC 1 is 753 BCE, which is ISO -752, and -752 + 753 = 1 exactly.
 * Applying a second correction shifts every count by one below the epoch.
 *
 * Results at or below zero mean the date precedes the epoch, and the validity
 * window reports that rather than this function inventing a negative year.
 */
function offsetYear(isoYear: number, offset: number): number {
  return isoYear + offset;
}

function spanLabel(from: number, to: number, suffix: string): string {
  const body = from === to ? String(from) : `${from}\u2013${to}`;
  return suffix.length > 0 ? `${body} ${suffix}` : body;
}

/**
 * Origin views — CE/BCE, AD/BC, raw ISO — are handled here rather than through
 * Temporal.
 *
 * They are not structural calendars: they are the ISO axis with its origin
 * moved and a label attached, so routing them through `withCalendar` buys
 * nothing and costs correctness. Reading `eraYear` off a Gregorian conversion
 * returns 2900 for 2900 BCE with the era in a separate field, which is how a
 * BCE date came to render indistinguishably from a CE one.
 */
function originView(isoYear: number, calendarId: string): { from: number; to: number; label: string } {
  if (calendarId === "iso8601") {
    // ISO shows its own signed year, year zero included. That is the point of
    // offering it: it is the only view where the internal value is visible.
    return { from: isoYear, to: isoYear, label: String(isoYear) };
  }
  const historical = historicalFromIso(isoYear as IsoYear) as number;
  const magnitude = Math.abs(historical);
  const suffix =
    calendarId === "gregorian"
      ? historical < 0 ? "BC" : "AD"
      : historical < 0 ? "BCE" : "CE";
  return { from: magnitude, to: magnitude, label: `${magnitude} ${suffix}` };
}

function validityFor(
  def: CalendarDef,
  isoYear: number,
): { validity: Validity; note?: string; beforeEpoch?: boolean } {
  const historical = historicalFromIso(isoYear as IsoYear) as number;
  if (def.validFrom !== null && historical < def.validFrom) {
    return {
      validity: "proleptic",
      beforeEpoch: true,
      note: `Extrapolated: this calendar's epoch is ${Math.abs(def.validFrom)} ${def.validFrom < 0 ? "BCE" : "CE"}.`,
    };
  }
  if (def.validTo !== null && historical > def.validTo) {
    return { validity: "proleptic", note: "After this calendar fell out of use." };
  }
  return { validity: "ok" };
}

/**
 * Read one ISO year in one calendar.
 *
 * Never throws. A calendar that cannot represent the year returns a reading
 * with a validity flag and no numbers, because a caller rendering a table of
 * twenty-six calendars should not have to guard each cell.
 */
export function readYear(isoYear: IsoYear, calendarId: string): CalendarReading {
  const def = getCalendar(calendarId);
  if (def === undefined) {
    return { calendarId, short: calendarId, label: "\u2014", validity: "outside-range",
      note: "Unknown calendar." };
  }
  const y = isoYear as number;
  const base = { calendarId, short: def.short };

  if (Math.abs(y) > DATE_REGIME_LIMIT_YEARS) {
    return { ...base, label: "\u2014", validity: "deep-time",
      note: "Deep time is measured in years before present; no calendar reaches here." };
  }

  const { validity, note, beforeEpoch } = validityFor(def, y);
  const b = def.backend;

  try {
    switch (b.kind) {
      case "temporal": {
        if (def.id === "common" || def.id === "gregorian" || def.id === "iso8601") {
          return { ...base, ...originView(y, def.id), validity, note };
        }
        // A pre-epoch extrapolation is meaningless however it is spelled, and
        // it is spelled two different ways: Persian returns a negative year
        // (-3521), while Islamic returns a positive one in a Before-Hijra era
        // and counts DOWN (3630 to 3629), which reads as a broken range. The
        // flag already says extrapolated; a number on top of it is noise
        // dressed as data. Checked against the epoch, not the sign.
        if (beforeEpoch === true) {
          return { ...base, label: "before epoch", validity, note };
        }
        const { from, to } = temporalSpan(y, b.temporalId);
        return { ...base, ...spanReading(from, to, def), validity, note };
      }
      case "julian": {
        const jan = jdnToJulian(gregorianToJDN(y, 1, 1));
        const dec = jdnToJulian(gregorianToJDN(y, 12, 31));
        return { ...base, ...spanReading(jan.year, dec.year, def), validity, note };
      }
      case "revised-julian": {
        if (!isInRevisedJulianEquivalenceWindow(y, 6, 1)) {
          return { ...base, label: "\u2014", validity: "outside-range",
            note: "This build computes Revised Julian only between 1600 and 2800 CE." };
        }
        const g = jdnToGregorian(gregorianToJDN(y, 6, 1));
        return { ...base, ...spanReading(g.year, g.year, def), validity, note };
      }
      case "offset": {
        const from = offsetYear(y, b.offset);
        if (beforeEpoch === true || from <= 0) {
          return { ...base, label: "before epoch", validity: "proleptic", note };
        }
        return { ...base, from, to: from, label: spanLabel(from, from, b.suffix), validity, note };
      }
      case "olympiad": {
        // Olympiad 1 begins 776 BCE (ISO -775). Each cycle is four years and
        // begins in midsummer, so a Gregorian year straddles two positions.
        const n = y + 776;
        if (n < 1) return { ...base, label: "\u2014", validity: "proleptic",
          note: "Before the first Olympiad, 776 BCE." };
        const ol = Math.floor((n - 1) / 4) + 1;
        const within = ((n - 1) % 4) + 1;
        return { ...base, from: ol, to: ol, label: `Ol. ${ol}.${within}`, validity, note };
      }
      case "sexagenary": {
        // 4 CE is jiazi, the first year of the cycle.
        const idx = (((y - 4) % 60) + 60) % 60;
        const name = `${SEXAGENARY_STEMS[idx % 10]}-${SEXAGENARY_BRANCHES[idx % 12]}`;
        return { ...base, from: idx + 1, to: idx + 1, label: `${name} (${idx + 1}/60)`, validity, note };
      }
      case "maya": {
        const days = gregorianToJDN(y, 1, 1) - MAYA_CORRELATION_JDN;
        if (days < 0) return { ...base, label: "\u2014", validity: "proleptic",
          note: "Before the Long Count epoch, 3114 BCE." };
        const baktun = Math.floor(days / 144000);
        const katun = Math.floor((days % 144000) / 7200);
        const tun = Math.floor((days % 7200) / 360);
        const uinal = Math.floor((days % 360) / 20);
        const kin = days % 20;
        return { ...base, label: `${baktun}.${katun}.${tun}.${uinal}.${kin}`, validity, note };
      }
    }
  } catch {
    return { ...base, label: "\u2014", validity: "outside-range",
      note: "Outside the range this calendar can represent." };
  }
}

function spanReading(from: number, to: number, def: CalendarDef): { from: number; to: number; label: string } {
  const suffix = def.backend.kind === "offset" ? def.backend.suffix : def.short;
  const showSuffix = def.id === "common" || def.id === "gregorian" || def.id === "iso8601" ? "" : suffix;
  return { from, to, label: spanLabel(from, to, showSuffix) };
}

export function readYearIn(isoYear: IsoYear, calendarIds: readonly string[]): CalendarReading[] {
  return calendarIds.map((id) => readYear(isoYear, id));
}
