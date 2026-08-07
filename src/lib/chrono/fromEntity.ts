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

import type { Entity } from "../types";
import type {
  BoundaryDating,
  DatingClaim,
  EntityCaveat,
  EntityCaveatKind,
  FuzzyPoint,
  YearValue,
} from "./year";

export interface EntityDates {
  start?: BoundaryDating;
  end?: BoundaryDating;
  /** True when entity-level fields were attached to a boundary by guesswork. */
  needsBoundaryReview: boolean;
}

function point(year: number): FuzzyPoint {
  return { year };
}

function valueFor(
  year: number,
  min: number | undefined,
  max: number | undefined,
): YearValue {
  const v: YearValue = { consensus: point(year) };
  // In v2.1.0, *_year_min is the earlier end and *_year_max the later one.
  if (min !== undefined) v.earliest = point(min);
  if (max !== undefined) v.latest = point(max);
  return v;
}

function claimFor(value: YearValue, entity: Entity): DatingClaim {
  const traditional = entity.date_precision === "traditional";
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
        valueFor(entity.start_year, entity.start_year_min, entity.start_year_max),
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
        valueFor(entity.end_year, entity.end_year_min, entity.end_year_max),
        entity,
      ),
    };
  }

  return result;
}

/**
 * Split a free-text misconception into a caveat kind.
 *
 * Heuristic, and deliberately conservative: it only promotes to
 * `naming-confusion` on an explicit name-versus-place construction, and
 * otherwise leaves the entry as a plain misconception. Getting this wrong in
 * the safe direction costs a slightly generic label; getting it wrong in the
 * other direction would put a factual correction under a heading that
 * misdescribes it.
 *
 * Intended for a one-time migration pass whose output is reviewed, not as a
 * permanent classifier. Once the field is authored directly, delete this.
 */
export function classifyCaveat(text: string): EntityCaveatKind {
  const t = text.toLowerCase();
  const namePattern =
    /(not (located )?in the modern|not the modern|despite the name|is a misnomer|named after|confused with the modern)/;
  if (namePattern.test(t)) return "naming-confusion";
  return "misconception";
}

export function caveatsOf(entity: Entity): EntityCaveat[] {
  const out: EntityCaveat[] = [];
  for (const text of entity.misconceptions ?? []) {
    out.push({ kind: classifyCaveat(text), text });
  }
  // "(legendary)" and "(traditional)" in a display name are the dataset's
  // existing way of hedging existence. Promote it to a real caveat.
  if (/\((legendary|traditional)\)/i.test(entity.name)) {
    out.push({
      kind: "contested-existence",
      text: `${entity.name.replace(/\s*\((legendary|traditional)\)/i, "")} is known from tradition rather than contemporary record.`,
    });
  }
  return out;
}
