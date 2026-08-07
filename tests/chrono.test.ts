import { describe, expect, it } from "vitest";
import { bpFromYear, formatBp, formatBpRange, resolveFrame, suggestFrame, yearFromBp } from "../src/lib/chrono/bp";
import {
  allClaims,
  disclosureReasons,
  disclosureSummary,
  hasDisclosure,
  isExact,
  supportOf,
  uncertaintyOf,
} from "../src/lib/chrono/year";
import type { BoundaryDating, DatingClaim } from "../src/lib/chrono/year";
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
    expect(suggestFrame(STONEHENGE)).toBe("bp");
  });

  it("keeps reckoned dates in calendar reckoning even when BCE", () => {
    expect(suggestFrame(ALEXANDER)).toBe("calendar");
    expect(suggestFrame(CYRUS)).toBe("calendar");
    expect(suggestFrame(SEPT_11)).toBe("calendar");
  });

  it("puts anything pre-Holocene in BP regardless of method", () => {
    expect(suggestFrame({ consensus: { year: -20000 }, method: "calendar" })).toBe("bp");
  });

  it("falls back on relative fuzziness when method is unknown", () => {
    // Tight date, no method: stays in calendar reckoning.
    expect(suggestFrame({ consensus: { year: -500, fuzz: 10 } })).toBe("calendar");
    // Uncertainty a large fraction of its own age: reads as measurement-shaped.
    expect(suggestFrame({ consensus: { year: -3000, fuzz: 800 } })).toBe("bp");
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

describe("display frame is a UI choice, not a property of the data", () => {
  it("lets an explicit preference override the automatic choice", () => {
    // Cyrus defaults to calendar, but BP is always available on request.
    expect(resolveFrame(CYRUS, "auto")).toBe("calendar");
    expect(resolveFrame(CYRUS, "bp")).toBe("bp");
    // ...and the reverse, including against the pre-Holocene backstop.
    expect(resolveFrame(OLDOWAN, "auto")).toBe("bp");
    expect(resolveFrame(OLDOWAN, "calendar")).toBe("calendar");
  });

  it("honours the frame a source quoted in", () => {
    const quotedInBp: YearValue = { consensus: { year: -2550, fuzz: 50 }, nativeFrame: "bp" };
    expect(suggestFrame(quotedInBp)).toBe("bp");
  });
});


// --- Disclosure -----------------------------------------------------------
// Cases drawn from real chronological arguments, so a failure names the idea.

const claim = (over: Partial<DatingClaim> & Pick<DatingClaim, "value">): DatingClaim => ({
  label: "Conventional",
  standing: "consensus",
  ...over,
});

/** Undisputed: a date nobody argues about. */
const PLAIN: BoundaryDating = { primary: claim({ value: SEPT_11 }) };

/** Egyptian New Kingdom: three rival schemes, same evidence base. */
const EGYPTIAN: BoundaryDating = {
  primary: claim({ value: { consensus: { year: -1550 } }, label: "Middle chronology" }),
  alternatives: [
    claim({ value: { consensus: { year: -1565 } }, label: "High chronology", standing: "minority" }),
    claim({ value: { consensus: { year: -1539 } }, label: "Low chronology", standing: "minority" }),
  ],
  note: "Schemes differ by a few decades; anchoring depends on Sothic dating assumptions.",
};

/** Radiocarbon against a king list — different methods, not just different numbers. */
const METHOD_CLASH: BoundaryDating = {
  primary: claim({
    value: { consensus: { year: -1200 }, method: "calendar" },
    label: "Traditional king-list date",
  }),
  alternatives: [
    claim({
      value: { consensus: { year: -1260, fuzz: 40 }, method: "radiocarbon-calibrated" },
      label: "Radiocarbon (IntCal20)",
      standing: "majority",
    }),
  ],
};

/** Rome's founding: received, not established. */
const TRADITIONAL: BoundaryDating = {
  primary: claim({
    value: { consensus: { year: -753 } },
    label: "Varronian date",
    standing: "traditional",
  }),
};

/** Fall of the Western Empire: a definitional argument, not an evidential one. */
const DEFINITIONAL: BoundaryDating = {
  primary: claim({ value: { consensus: { year: 476 } }, label: "Deposition of Romulus Augustulus" }),
  reasons: ["definitional"],
  note: "Some date the end to 480, others to 1453; the boundary is a matter of definition.",
};

describe("disclosure fires only when a single number would mislead", () => {
  it("stays silent on undisputed dates", () => {
    expect(hasDisclosure(PLAIN)).toBe(false);
    expect(disclosureSummary(PLAIN)).toBeUndefined();
  });

  it("distinguishes rival schemes from clashing methods", () => {
    // Same method throughout: the schemes differ, not the evidence type.
    expect(disclosureReasons(EGYPTIAN)).toContain("rival-chronologies");
    expect(disclosureReasons(EGYPTIAN)).not.toContain("method-conflict");
    // Different methods: that is the more informative thing to say.
    expect(disclosureReasons(METHOD_CLASH)).toContain("method-conflict");
  });

  it("infers a traditional date from claim standing", () => {
    expect(disclosureReasons(TRADITIONAL)).toContain("traditional-date");
    expect(disclosureSummary(TRADITIONAL)).toBe("Traditional date");
  });

  it("infers a broad range without the author saying so", () => {
    const broad: BoundaryDating = {
      primary: claim({ value: { consensus: { year: -3500, fuzz: 500 } } }),
    };
    expect(disclosureReasons(broad)).toContain("wide-uncertainty");
  });

  it("carries a stated reason that cannot be inferred", () => {
    // Nothing about the numbers reveals that 476 is a definitional choice.
    expect(disclosureReasons(DEFINITIONAL)).toContain("definitional");
  });
});

describe("the marker says what kind of complication it is", () => {
  it("surfaces the most consequential reason when several apply", () => {
    // Definitional outranks the wide range that also applies here.
    const both: BoundaryDating = {
      primary: claim({ value: { consensus: { year: 476, fuzz: 100 } } }),
      reasons: ["definitional"],
    };
    expect(disclosureReasons(both).length).toBeGreaterThan(1);
    expect(disclosureSummary(both)).toBe("Depends on definition");
  });

  it("names the disagreement rather than showing a generic mark", () => {
    expect(disclosureSummary(EGYPTIAN)).toBe("Chronologies differ");
    expect(disclosureSummary(METHOD_CLASH)).toBe("Methods disagree");
  });
});

describe("claims", () => {
  it("returns every claim with the primary first", () => {
    expect(allClaims(EGYPTIAN).map((c) => c.label)).toEqual([
      "Middle chronology",
      "High chronology",
      "Low chronology",
    ]);
    expect(allClaims(PLAIN)).toHaveLength(1);
  });

  it("treats a note alone as grounds for disclosure", () => {
    expect(hasDisclosure({ primary: claim({ value: SEPT_11 }), note: "why" })).toBe(true);
  });
});
