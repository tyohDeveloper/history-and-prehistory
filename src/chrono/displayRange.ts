/**
 * The entity range as the reader should see it.
 *
 * `tree.formatRange` is the naive formatter: it prints the stored historical
 * year with a CE/BCE suffix. That is right for the calendar era and wrong for
 * everything older, because it renders the origin of our genus as "2798051
 * BCE" — a seven-digit position in a calendar that did not exist, implying
 * one-year precision on a date uncertain by tens of thousands.
 *
 * The chrono layer already knows how to pick a frame (`suggestFrame`) and how
 * to render BP honestly (`formatBp`). This module is the join.
 */

import type { Entity } from "../entity/entity";
import { formatRange as naiveRange, formatYear } from "../entity/tree";
import { datingOf } from "./fromEntity";
import { bpSenseOf } from "./year";
import {
  BP_UNIT_DIVISOR,
  bpFromYear,
  bpSuffix,
  bpUnitFor,
  formatBp,
  resolveFrame,
  type FramePreference,
} from "./bp";

export interface DisplayRange {
  text: string;
  frame: string;
}

/**
 * A threshold is a one-sided bound, so it has no range at all.
 *
 * "Stone Knapping 3.3 Ma ago – present" reads as an interval that happens to
 * reach today. The actual claim is narrower and stranger: this is the OLDEST
 * KNOWN instance, the behaviour continues, and new evidence can only move the
 * date older. "from 3.3 Ma ago" says that; a range does not.
 */
function isThreshold(e: Entity): boolean {
  // Was `kind === "threshold" || date_precision === "minimum"`. The precision enum is gone;
  // a one-sided bound is now expressed as it should always have been -- a lower bound with
  // no upper one, which is exactly what a terminus post quem is.
  const oneSided =
    e.start_year_min !== undefined && e.start_year_max === undefined && e.end_year === null;
  return e.kind === "threshold" || oneSided;
}

/**
 * A point event: a battle, a sack, an invention. It has no end year because it
 * is a moment, not because it is open-ended.
 *
 * This is the THIRD formatter in the codebase to need the distinction, after
 * `formatRange` in `entity/tree` and `shortRange` in `main`. The dataset had no
 * point events until 0.16.0.0, so all three quietly treated a missing end as
 * "ongoing", and the Narmer Palette rendered as "5,049 BP - present". That
 * three separate places format a range is the more interesting finding, and is
 * left recorded here rather than fixed under cover of a data release.
 */
function isPoint(e: Entity): boolean {
  // A point event has no end because it is a moment. Distinguished from an ongoing thing by
  // `extant`, which is the field that exists to end this ambiguity.
  return e.kind === "event" && e.end_year === null && e.extant !== true;
}

/**
 * A missing end year means two different things. For Homo sapiens it means
 * extant; for Homo luzonensis it means the youngest remains were never dated.
 * See `tree.formatRange`.
 */
function openEndLabel(e: Entity): string | undefined {
  if (e.end_year !== null) return undefined;
  // `extant` replaces the inference this used to make from `end_precision === "unknown"`.
  // The old default was "present", so an undated final appearance read as though the thing
  // were still with us -- which for Homo luzonensis it is not.
  return e.extant === true ? "present" : "unknown";
}

export function displayRange(e: Entity, preference: FramePreference = "auto"): DisplayRange {
  if (e.start_year === null) return { text: "\u2014", frame: "calendar" };

  const dates = datingOf(e);
  const startValue = dates.start?.primary.value;
  if (startValue === undefined) return { text: naiveRange(e), frame: "calendar" };

  // BP is the idiom of radiometric measurement, and quoting a received
  // convention in it lends the convention that authority — "4800 BCE" becomes
  // "6,749 BP", which reads as measured and gains a digit it never had. When
  // the user has asked for a frame they get it; on `auto` a traditional date
  // stays in the calendar reckoning it was actually handed down in.
  // The extant override that used to sit here is gone. It existed because Athens rendered as
  // "4,949 BP - present", mixing two frames in one range; the 5000 BCE boundary now sends Athens
  // to calendar on age alone, so the override no longer has a case to fix -- and it had started
  // fighting the boundary, holding Homo sapiens at "310000 BCE" where the rule says 310 ka.
  const frame =
    preference === "auto" && e.date_standing === "traditional"
      ? "calendar"
      : resolveFrame(startValue, preference);

  if (frame === "calendar") {
    if (isThreshold(e)) return { text: `from ${formatYear(e.start_year)}`, frame };
    return { text: naiveRange(e), frame };
  }

  const sense = bpSenseOf(startValue);
  const startBp = bpFromYear(startValue.consensus.year, frame);

  if (isThreshold(e)) {
    const text = formatBp(startValue.consensus.year, startValue.consensus.fuzz, {
      datum: frame,
      sense,
    });
    return { text: `from ${text}`, frame };
  }

  if (isPoint(e)) {
    const text = formatBp(startValue.consensus.year, startValue.consensus.fuzz, {
      datum: frame,
      sense,
    });
    return { text, frame };
  }

  const tail = openEndLabel(e);
  const endValue = dates.end?.primary.value;
  const endBp = endValue === undefined ? undefined : bpFromYear(endValue.consensus.year, frame);

  // A shared unit reads best ("2.4 – 1.4 Ma ago"), but only where both ends
  // live in it. Human Prehistory runs 3.3 Ma to 4,950 BP, and forcing the
  // younger end into Ma gives "0.0 Ma" — a real span rendered as zero. So the
  // shared unit is used only when the younger end is at least 1 in it;
  // otherwise each end takes its own and the labels carry the meaning.
  const olderUnit = bpUnitFor(startBp);
  const shared =
    endBp !== undefined && endBp / BP_UNIT_DIVISOR[olderUnit] >= 1 ? olderUnit : undefined;

  if (shared !== undefined && endValue !== undefined && tail === undefined) {
    // One unit, one suffix, at the end of the whole range.
    const a = formatBp(startValue.consensus.year, startValue.consensus.fuzz, {
      datum: frame, sense, unit: shared, withUnit: false,
    });
    const b = formatBp(endValue.consensus.year, endValue.consensus.fuzz, {
      datum: frame, sense, unit: shared, withUnit: false,
    });
    return { text: `${a} \u2013 ${b} ${bpSuffix(shared, sense, frame)}`, frame };
  }

  const startText = formatBp(startValue.consensus.year, startValue.consensus.fuzz, {
    datum: frame,
    sense,
  });
  if (tail !== undefined) return { text: `${startText} \u2013 ${tail}`, frame };
  if (endValue === undefined) return { text: startText, frame };
  const endText = formatBp(endValue.consensus.year, endValue.consensus.fuzz, {
    datum: frame,
    sense,
  });
  return { text: `${startText} \u2013 ${endText}`, frame };
}
