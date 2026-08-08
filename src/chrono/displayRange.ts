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
  return e.kind === "threshold" || e.date_precision === "minimum";
}

/**
 * A missing end year means two different things. For Homo sapiens it means
 * extant; for Homo luzonensis it means the youngest remains were never dated.
 * See `tree.formatRange`.
 */
function openEndLabel(e: Entity): string | undefined {
  if (e.end_year !== null) return undefined;
  return e.end_precision === "unknown" ? "unknown" : "present";
}

export function displayRange(e: Entity, preference: FramePreference = "auto"): DisplayRange {
  if (e.start_year === null) return { text: "\u2014", frame: "calendar" };

  const dates = datingOf(e);
  const startValue = dates.start?.primary.value;
  if (startValue === undefined) return { text: naiveRange(e), frame: "calendar" };

  const frame = resolveFrame(startValue, preference);

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
