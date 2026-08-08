/**
 * The entity range as the reader should see it.
 *
 * `tree.formatRange` is the naive formatter: it prints the stored historical
 * year with a CE/BCE suffix. That is correct for the calendar era and wrong
 * for everything older, because it will happily render the origin of our genus
 * as "2798051 BCE" — a seven-digit position in a calendar that did not exist,
 * implying a precision of one year on a date whose real uncertainty is tens of
 * thousands.
 *
 * The chrono layer already knows how to choose a frame (`suggestFrame`) and
 * how to render BP at an honest resolution (`formatBpRange`). This module is
 * the join: it takes an `Entity`, runs it through the dataset adapter, and
 * asks the frame layer what to print. The frame choice is driven by
 * provenance, so an argon-argon date leads in Ma and a king-list date leads
 * in BCE regardless of which is older.
 */

import type { Entity } from "./types";
import { formatRange as naiveRange } from "./tree";
import { datingOf } from "./chrono/fromEntity";
import { bpSenseOf } from "./chrono/year";
import {
  BP_UNIT_DIVISOR,
  bpFromYear,
  bpUnitFor,
  formatBp,
  resolveFrame,
  type FramePreference,
} from "./chrono/bp";

/** Rendered range plus the frame it was rendered in, for the secondary line. */
export interface DisplayRange {
  text: string;
  frame: string;
}

function endLabel(e: Entity): string | undefined {
  if (e.end_year !== null) return undefined;
  // Absent end year is two claims, not one. See tree.formatRange.
  return e.end_precision === "unknown" ? "unknown" : "present";
}

export function displayRange(e: Entity, preference: FramePreference = "auto"): DisplayRange {
  if (e.start_year === null) return { text: "\u2014", frame: "calendar" };

  const dates = datingOf(e);
  const startValue = dates.start?.primary.value;
  if (startValue === undefined) return { text: naiveRange(e), frame: "calendar" };

  const frame = resolveFrame(startValue, preference);
  if (frame === "calendar") return { text: naiveRange(e), frame: "calendar" };

  // Deep time: both ends as counts from the datum.
  //
  // A shared unit reads best ("2.4 Ma \u2013 1.4 Ma"), but only when both ends
  // actually live in that band. Human Prehistory runs 3.3 Ma to 4,950 BP, and
  // forcing the younger end into Ma yields "0.0 Ma" \u2014 a real span rendered as
  // zero. So the shared unit is used only when the younger end is at least 1
  // in it; otherwise each end takes its own, and the explicit labels keep the
  // range unambiguous ("3.3 Ma \u2013 4,950 BP").
  const startBp = bpFromYear(startValue.consensus.year, frame);
  const olderUnit = bpUnitFor(startBp);
  const endValue = dates.end?.primary.value;
  const endBp = endValue === undefined ? undefined : bpFromYear(endValue.consensus.year, frame);
  const shared =
    endBp !== undefined && endBp / BP_UNIT_DIVISOR[olderUnit] >= 1 ? olderUnit : undefined;

  const sense = bpSenseOf(startValue);
  const startText = formatBp(startValue.consensus.year, startValue.consensus.fuzz, {
    datum: frame,
    sense,
    ...(shared !== undefined ? { unit: shared } : {}),
  });
  const tail = endLabel(e);
  if (tail !== undefined) return { text: `${startText} \u2013 ${tail}`, frame };
  if (endValue === undefined) return { text: startText, frame };

  const endText = formatBp(endValue.consensus.year, endValue.consensus.fuzz, {
    datum: frame,
    sense,
    ...(shared !== undefined ? { unit: shared } : {}),
  });
  return { text: `${startText} \u2013 ${endText}`, frame };
}
