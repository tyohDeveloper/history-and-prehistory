import { describe, expect, it } from "vitest";
import { bpFromYear, formatBp, formatBpRange, prefersBp, yearFromBp } from "../src/lib/chrono/bp";
import { isExact, supportOf, uncertaintyOf } from "../src/lib/chrono/year";
import type { YearValue } from "../src/lib/chrono/year";

// The cases that drove the design. Named so a regression says which idea broke.
const SEPT_11: YearValue = { consensus: { year: 2001 }, method: "calendar" };
const ALEXANDER: YearValue = { consensus: { year: -323 }, method: "calendar" };
const CYRUS: YearValue = { consensus: { year: -530 }, method: "calendar" };
const STONEHENGE: YearValue = {
  consensus: { year: -2500, fuzz: 100 },
  method: "radiocarbon-calibrated",
};
const WORKED_EXAMPLE: YearValue = {
  consensus: { year: -3500, fuzz: 250 },
  earliest: { year: -4500, fuzz: 500 },
  latest: { year: -3000 },
};
const OLDOWAN: YearValue = {
  consensus: { year: -3300000 },
  earliest: { year: -3400000 },
  latest: { year: -3200000 },
  method: "potassium-argon",
};

describe("BP datum arithmetic", () => {
  it("skips the absent year zero", () => {
    expect(bpFromYear(1950)).toBe(0);
    expect(bpFromYear(1)).toBe(1949);
    expect(bpFromYear(-1)).toBe(1950);
    expect(yearFromBp(1950)).toBe(-1);
    expect(yearFromBp(1949)).toBe(1);
  });
});

describe("frame selection is driven by provenance, not age", () => {
  it("puts measured dates in BP even when recent", () => {
    expect(prefersBp(STONEHENGE)).toBe(true);
  });

  it("keeps reckoned dates in calendar reckoning even when BCE", () => {
    expect(prefersBp(ALEXANDER)).toBe(false);
    expect(prefersBp(CYRUS)).toBe(false);
    expect(prefersBp(SEPT_11)).toBe(false);
  });

  it("puts anything pre-Holocene in BP regardless of method", () => {
    expect(prefersBp({ consensus: { year: -20000 }, method: "calendar" })).toBe(true);
  });

  it("falls back on relative fuzziness when method is unknown", () => {
    // Tight date, no method: stays in calendar reckoning.
    expect(prefersBp({ consensus: { year: -500, fuzz: 10 } })).toBe(false);
    // Uncertainty a large fraction of its own age: reads as measurement-shaped.
    expect(prefersBp({ consensus: { year: -3000, fuzz: 800 } })).toBe(true);
  });
});

describe("uncertainty is widened by each bound's own fuzz", () => {
  it("extends the support past a fuzzy bound", () => {
    // earliest is -4500 +/- 500, so the support reaches -5000.
    expect(supportOf(WORKED_EXAMPLE)).toEqual({ earliest: -5000, latest: -3000 });
  });

  it("treats a bare crisp consensus as exact", () => {
    expect(isExact(SEPT_11)).toBe(true);
    expect(isExact(WORKED_EXAMPLE)).toBe(false);
  });

  it("reports the wider side of an asymmetric range", () => {
    expect(uncertaintyOf(WORKED_EXAMPLE)).toBe(1500);
  });
});

describe("rendering never claims more precision than it has", () => {
  it("scales units by magnitude", () => {
    expect(formatBp(-8000)).toBe("9,949 BP");
    expect(formatBpRange(OLDOWAN)).toBe("3.4\u20133.2 Ma");
  });

  it("rounds a wide range to the resolution of its own uncertainty", () => {
    // Natufian-scale: quoted in ka, not spurious whole years.
    const natufian: YearValue = {
      consensus: { year: -11000 },
      earliest: { year: -13000 },
      latest: { year: -9500 },
    };
    expect(formatBpRange(natufian)).toBe("15\u201311 ka");
  });
});
