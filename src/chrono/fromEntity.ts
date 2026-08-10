/**
 * Adapter from a v2.1.0 `Entity` to the dating and caveat model.
 *
 * The disclosure model is richer than the schema that feeds it, so this is
 * where the two meet. Keeping the translation in one place means the UI never
 * sees v2.1.0's shape, and the eventual schema migration changes this file
 * rather than every consumer.
 *
 * ## Migration is lossy in one specific way
 *
 * v2.1.0 carries `date_note` and `allow_outside_parent_dates` **per entity**,
 * while disclosure attaches **per boundary**. The old schema simply cannot say
 * which end a note is about, and the notes themselves show why that matters —
 * "Oda Nobunaga's rule began 1568, before the formal era start" is clearly
 * about the start, while "nengō 782-806 spans the Nara-Heian boundary" is
 * about neither end in particular.
 *
 * This adapter attaches both to the start boundary, which is right more often
 * than not, and flags them so a migration pass can be reviewed rather than
 * trusted. See `needsBoundaryReview`.
 */

import type { Entity } from "../entity/entity";
import { asHistorical, isoFromHistorical } from "./year";
import type {
  BoundaryDating,
  DatingClaim,
  FuzzyPoint,
  YearValue,
} from "./year";

export interface EntityDates {
  start?: BoundaryDating;
  end?: BoundaryDating;
  /** True when entity-level fields were attached to a boundary by guesswork. */
  needsBoundaryReview: boolean;
}

/**
 * The dataset boundary.
 *
 * `src/data/*.json` stores HISTORICAL years — `-753` means 753 BCE. Internals
 * are ISO astronomical. This function is where the two meet, and after the
 * branded-type refactor it is one of only a handful of places in the codebase
 * that can perform the crossing at all: everything downstream takes `IsoYear`
 * and will not compile against a raw dataset number.
 */
function point(historicalYear: number): FuzzyPoint {
  return { year: isoFromHistorical(asHistorical(historicalYear)) };
}

/**
 * `method` must be carried onto the value, not left on the entity.
 *
 * The frame rule is provenance-driven: a measured date leads in BP and a
 * reckoned one leads in a calendar (see `suggestFrame`). `suggestFrame` reads
 * `v.method`, so dropping it here silently disables the whole rule and leaves
 * only the pre-Holocene age backstop — which is precisely the age-based
 * heuristic the design rejected. Göbekli Tepe is the case that exposes it: a
 * radiocarbon date at 11,480 BP, just under the 11,700 backstop, so it fell
 * through to a calendar reading it should never have had.
 */
function valueFor(
  year: number,
  min: number | undefined,
  max: number | undefined,
  method: Entity["start_dating_method"],
): YearValue {
  const v: YearValue = { consensus: point(year) };
  // In v2.1.0, *_year_min is the earlier end and *_year_max the later one.
  if (min !== undefined) v.earliest = point(min);
  if (max !== undefined) v.latest = point(max);
  if (method !== undefined) v.method = method;
  return v;
}

function claimFor(value: YearValue, entity: Entity): DatingClaim {
  // Was `date_precision === "traditional"`. A traditional date is now identified by the
  // dating METHOD that produced it -- `received` -- which is what it always meant: a figure
  // handed down rather than measured.
  const traditional =
    entity.start_dating_method === "received" || entity.date_standing === "traditional";
  return {
    value,
    label: traditional ? "Traditional date" : "Conventional date",
    standing: traditional ? "traditional" : "consensus",
  };
}

export function datingOf(entity: Entity): EntityDates {
  const result: EntityDates = { needsBoundaryReview: false };

  const carriesEntityLevelFlags =
    entity.date_note !== undefined || entity.allow_outside_parent_dates === true;

  if (entity.start_year !== null) {
    const start: BoundaryDating = {
      primary: claimFor(
        valueFor(
          entity.start_year,
          entity.start_year_min,
          entity.start_year_max,
          entity.start_dating_method,
        ),
        entity,
      ),
    };
    if (entity.date_note !== undefined) start.note = entity.date_note;
    if (entity.allow_outside_parent_dates === true) start.outsideParent = true;
    result.start = start;
    if (carriesEntityLevelFlags) result.needsBoundaryReview = true;
  }

  if (entity.end_year !== null) {
    result.end = {
      primary: claimFor(
        valueFor(
          entity.end_year,
          entity.end_year_min,
          entity.end_year_max,
          // Q-30: the end carries its OWN method, and carries none when the
          // dataset does not record one. Reusing the start's method here was
          // the bug: it labelled a radiocarbon end as argon-argon whenever the
          // start was volcanic, and did so invisibly.
          entity.end_dating_method,
        ),
        entity,
      ),
    };
  }

  return result;
}
