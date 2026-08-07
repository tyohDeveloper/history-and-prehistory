/**
 * The ISO refactor's safety net.
 *
 * Converting 1,305 entities from historical to ISO numbering is a change
 * where every wrong answer looks plausible — -753 and -752 are both credible
 * for the founding of Rome. Branded types stop the two being mixed at compile
 * time; these tests check the conversion itself is right, against real data.
 */
import { describe, expect, it } from "vitest";
import { entities } from "../src/lib/dataset";
import { datingOf } from "../src/lib/chrono/fromEntity";
import {
  asHistorical,
  bce,
  ce,
  historicalFromIso,
  isoFromHistorical,
} from "../src/lib/chrono/year";
import { bpFromYear } from "../src/lib/chrono/bp";

describe("scheme conversion", () => {
  it("round-trips every dated boundary in the dataset", () => {
    let checked = 0;
    for (const e of entities) {
      for (const y of [e.start_year, e.end_year]) {
        if (y === null) continue;
        const back = historicalFromIso(isoFromHistorical(asHistorical(y)));
        expect(back as number).toBe(y);
        checked += 1;
      }
    }
    expect(checked).toBeGreaterThan(2000);
  });

  it("shifts BCE by one and leaves CE alone", () => {
    expect(isoFromHistorical(asHistorical(-1)) as number).toBe(0);
    expect(isoFromHistorical(asHistorical(-753)) as number).toBe(-752);
    expect(isoFromHistorical(asHistorical(1)) as number).toBe(1);
    expect(isoFromHistorical(asHistorical(2026)) as number).toBe(2026);
  });

  it("refuses year zero on the historical side", () => {
    expect(() => asHistorical(0)).toThrow(RangeError);
  });

  it("agrees with the era constructors", () => {
    expect(isoFromHistorical(asHistorical(-753))).toBe(bce(753));
    expect(isoFromHistorical(asHistorical(1492))).toBe(ce(1492));
  });
});

describe("the adapter converts at the boundary", () => {
  it("produces ISO years for every entity it touches", () => {
    let n = 0;
    for (const e of entities) {
      const d = datingOf(e);
      if (e.start_year !== null && d.start) {
        expect(d.start.primary.value.consensus.year as number).toBe(
          e.start_year < 0 ? e.start_year + 1 : e.start_year,
        );
        n += 1;
      }
    }
    expect(n).toBeGreaterThan(1000);
  });

  it("keeps BP consistent across the era boundary", () => {
    // Consecutive historical years 1 BCE and 1 CE are one year apart, and BP
    // must reflect that despite the dataset having no year zero between them.
    const a = datingOf({ ...entities[0]!, start_year: -1, end_year: null });
    const b = datingOf({ ...entities[0]!, start_year: 1, end_year: null });
    const bpA = bpFromYear(a.start!.primary.value.consensus.year);
    const bpB = bpFromYear(b.start!.primary.value.consensus.year);
    expect(bpA - bpB).toBe(1);
  });
});
