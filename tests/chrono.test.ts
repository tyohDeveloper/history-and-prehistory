import { describe, expect, it } from "vitest";
import { bpFromYear, formatBp, formatBpRange, resolveFrame, suggestFrame, yearFromBp } from "../src/lib/chrono/bp";
import {
  allClaims,
  asHistorical,
  asIso,
  bce,
  ce,
  historicalFromIso,
  isoFromHistorical,
  entityCaveats,
  disclosureReasons,
  disclosureSummary,
  distanceFromDatum,
  rollupDisclosure,
  hasDisclosure,
  isDateRegime,
  isExact,
  MAX_CAVEAT_LENGTH,
  supportOf,
  uncertaintyOf,
} from "../src/lib/chrono/year";
import type { BoundaryDating, DatingClaim, EntityCaveat, IsoYear } from "../src/lib/chrono/year";
import type { YearValue } from "../src/lib/chrono/year";

// The cases that drove the design. Named so a regression says which idea broke.
const SEPT_11: YearValue = { consensus: { year: ce(2001) }, method: "calendar" };
const ALEXANDER: YearValue = { consensus: { year: bce(323) }, method: "calendar" };
const CYRUS: YearValue = { consensus: { year: bce(530) }, method: "calendar" };
const STONEHENGE: YearValue = {
  consensus: { year: bce(2500), fuzz: 100 },
  method: "radiocarbon-calibrated",
};
const WORKED_EXAMPLE: YearValue = {
  consensus: { year: bce(3500), fuzz: 250 },
  earliest: { year: bce(4500), fuzz: 500 },
  latest: { year: bce(3000) },
};
const OLDOWAN: YearValue = {
  consensus: { year: bce(3300000) },
  earliest: { year: bce(3400000) },
  latest: { year: bce(3200000) },
  method: "potassium-argon",
};

describe("BP datum arithmetic", () => {
  it("is plain subtraction, because ISO has a year zero", () => {
    // The historical scheme's missing year zero is handled once, at the
    // dataset boundary. By the time a value reaches here it is ISO, so BP
    // needs no special case at the era boundary.
    expect(bpFromYear(ce(1950))).toBe(0);
    expect(bpFromYear(ce(1))).toBe(1949);
    expect(bpFromYear(bce(1))).toBe(1950);
    expect(yearFromBp(1950)).toBe(bce(1));
    expect(yearFromBp(1949)).toBe(ce(1));
    // 1 BCE is ISO year 0 -- the value that cannot appear in the dataset.
    expect(bce(1) as number).toBe(0);
  });

  it("crosses the two schemes without an off-by-one", () => {
    expect(isoFromHistorical(asHistorical(-753))).toBe(bce(753));
    expect(historicalFromIso(bce(753)) as number).toBe(-753);
    expect(isoFromHistorical(asHistorical(1492))).toBe(ce(1492));
    expect(() => asHistorical(0)).toThrow(RangeError);
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
    expect(suggestFrame({ consensus: { year: bce(20000) }, method: "calendar" })).toBe("bp");
  });

  it("falls back on relative fuzziness when method is unknown", () => {
    // Tight date, no method: stays in calendar reckoning.
    expect(suggestFrame({ consensus: { year: bce(500), fuzz: 10 } })).toBe("calendar");
    // Uncertainty a large fraction of its own age: reads as measurement-shaped.
    expect(suggestFrame({ consensus: { year: bce(3000), fuzz: 800 } })).toBe("bp");
  });
});

describe("uncertainty is widened by each bound's own fuzz", () => {
  it("extends the support past a fuzzy bound", () => {
    // earliest is 4500 BCE +/- 500, so the support reaches 5000 BCE.
    // Written with the era constructors, the intended values are unambiguous
    // in a way the raw ISO integers -4999 / -2999 are not.
    expect(supportOf(WORKED_EXAMPLE)).toEqual({ earliest: bce(5000), latest: bce(3000) });
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
    expect(formatBp(bce(8000))).toBe("9,949 BP");
    expect(formatBpRange(OLDOWAN)).toBe("3.4\u20133.2 Ma");
  });

  it("rounds a wide range to the resolution of its own uncertainty", () => {
    // Natufian-scale: quoted in ka, not spurious whole years.
    const natufian: YearValue = {
      consensus: { year: bce(11000) },
      earliest: { year: bce(13000) },
      latest: { year: bce(9500) },
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
    const quotedInBp: YearValue = { consensus: { year: bce(2550), fuzz: 50 }, nativeFrame: "bp" };
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
  primary: claim({ value: { consensus: { year: bce(1550) } }, label: "Middle chronology" }),
  alternatives: [
    claim({ value: { consensus: { year: bce(1565) } }, label: "High chronology", standing: "minority" }),
    claim({ value: { consensus: { year: bce(1539) } }, label: "Low chronology", standing: "minority" }),
  ],
  note: "Schemes differ by a few decades; anchoring depends on Sothic dating assumptions.",
};

/** Radiocarbon against a king list — different methods, not just different numbers. */
const METHOD_CLASH: BoundaryDating = {
  primary: claim({
    value: { consensus: { year: bce(1200) }, method: "calendar" },
    label: "Traditional king-list date",
  }),
  alternatives: [
    claim({
      value: { consensus: { year: bce(1260), fuzz: 40 }, method: "radiocarbon-calibrated" },
      label: "Radiocarbon (IntCal20)",
      standing: "majority",
    }),
  ],
};

/** Rome's founding: received, not established. */
const TRADITIONAL: BoundaryDating = {
  primary: claim({
    value: { consensus: { year: bce(753) } },
    label: "Varronian date",
    standing: "traditional",
  }),
};

/** Nengo straddling a period boundary: the commonest real case, and not a dispute. */
const OVERLAPS: BoundaryDating = {
  primary: claim({ value: { consensus: { year: ce(782) } }, label: "Enryaku" }),
  outsideParent: true,
  note: "Nengo 782-806 spans the Nara-Heian boundary (794).",
};

/** Fall of the Western Empire: a definitional argument, not an evidential one. */
const DEFINITIONAL: BoundaryDating = {
  primary: claim({ value: { consensus: { year: ce(476) } }, label: "Deposition of Romulus Augustulus" }),
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
    // The canonical worked example: ~3500 BCE (3000 .. ~4500 BCE). Support
    // runs -5000 to -3000, so uncertainty is 1500 against 5449 years before
    // the datum -- 27%, unambiguously a range wearing a date's clothes.
    const broad: BoundaryDating = {
      primary: claim({
        value: {
          consensus: { year: bce(3500), fuzz: 250 },
          earliest: { year: bce(4500), fuzz: 500 },
          latest: { year: bce(3000) },
        },
      }),
    };
    expect(disclosureReasons(broad)).toContain("wide-uncertainty");
  });

  it("does not call a well-constrained ancient date broad", () => {
    // +/-200 on a 5,450-year-old date is 3.7%: ordinary precision for the
    // period, and flagging it would train the reader to ignore the marker.
    const ordinary: BoundaryDating = {
      primary: claim({ value: { consensus: { year: bce(3500), fuzz: 200 } } }),
    };
    expect(disclosureReasons(ordinary)).not.toContain("wide-uncertainty");
  });

  it("treats equal relative precision equally, however old", () => {
    // Both sit at 9.2% of their distance from the datum. Madjedbebe at
    // 65 +/- 6 ka is the case the threshold was calibrated on, and a
    // Chalcolithic date at +/-500 is the same claim about precision.
    const madjedbebe: BoundaryDating = {
      primary: claim({ value: { consensus: { year: bce(63050), fuzz: 6000 } } }),
    };
    const chalcolithic: BoundaryDating = {
      primary: claim({ value: { consensus: { year: bce(3500), fuzz: 500 } } }),
    };
    expect(disclosureReasons(madjedbebe)).toContain("wide-uncertainty");
    expect(disclosureReasons(chalcolithic)).toContain("wide-uncertainty");
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
      // 300 years on a 1,474-year-old date is 20%: broad as well as definitional.
      primary: claim({ value: { consensus: { year: ce(476), fuzz: 300 } } }),
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

describe("structural overlap is disclosed without implying a dispute", () => {
  it("infers the reason from the outside-parent flag", () => {
    // 27 entities in v2.1.0 carry allow_outside_parent_dates. Nothing is
    // wrong, but it looks wrong, so it has to be sayable.
    expect(disclosureReasons(OVERLAPS)).toContain("overlaps-parent");
    expect(disclosureSummary(OVERLAPS)).toBe("Crosses its period");
  });

  it("does not read as a chronological disagreement", () => {
    expect(disclosureReasons(OVERLAPS)).not.toContain("rival-chronologies");
    expect(disclosureReasons(OVERLAPS)).not.toContain("method-conflict");
  });
});

describe("claim ordering", () => {
  it("keeps the primary first and sorts the rest by standing", () => {
    const d: BoundaryDating = {
      primary: claim({ value: SEPT_11, label: "Primary" }),
      alternatives: [
        claim({ value: SEPT_11, label: "Old view", standing: "superseded" }),
        claim({ value: SEPT_11, label: "Minority view", standing: "minority" }),
        claim({ value: SEPT_11, label: "Most accept", standing: "majority" }),
      ],
    };
    expect(allClaims(d).map((c) => c.label)).toEqual([
      "Primary",
      "Most accept",
      "Minority view",
      "Old view",
    ]);
  });

  it("never hides a superseded claim", () => {
    // A reader who met the old date elsewhere must find it here and be told
    // it is old, rather than concluding the app is wrong.
    const d: BoundaryDating = {
      primary: claim({ value: SEPT_11 }),
      alternatives: [claim({ value: SEPT_11, label: "Older estimate", standing: "superseded" })],
    };
    expect(allClaims(d)).toHaveLength(2);
  });
});

describe("entity caveats are separate from dating disclosure", () => {
  // Drawn verbatim from the dataset's own misconceptions entries.
  const caveats: EntityCaveat[] = [
    { kind: "naming-confusion", text: "Ghana Empire was not located in the modern nation of Ghana." },
    {
      kind: "misconception",
      text: "The Maya never formed a single unified empire; they were a network of city-states.",
    },
  ];

  it("carries corrections that have nothing to do with dates", () => {
    expect(entityCaveats(caveats)).toHaveLength(2);
    expect(entityCaveats(undefined)).toEqual([]);
  });

  it("keeps caveat text inside the brevity cap", () => {
    for (const c of caveats) expect(c.text.length).toBeLessThanOrEqual(MAX_CAVEAT_LENGTH);
  });
});

describe("uncertainty is judged against distance from the datum", () => {
  it("does not blow up near the era boundary", () => {
    // Regression: |year| as denominator gave 1 CE +/-5 a ratio of 5.0, so
    // every date near year zero read as wildly uncertain.
    expect(distanceFromDatum(ce(1))).toBe(1949);
    expect(distanceFromDatum(bce(1))).toBe(1950);
    const nearZero: BoundaryDating = {
      primary: claim({ value: { consensus: { year: ce(1), fuzz: 5 } } }),
    };
    expect(disclosureReasons(nearZero)).not.toContain("wide-uncertainty");
  });

  it("stays positive after the datum", () => {
    expect(distanceFromDatum(ce(2026))).toBeGreaterThan(0);
  });

  it("reads the same error differently by remoteness", () => {
    // +/-50 years is unremarkable on a Bronze Age date...
    const ancient: BoundaryDating = {
      primary: claim({ value: { consensus: { year: bce(3300), fuzz: 50 } } }),
    };
    expect(disclosureReasons(ancient)).not.toContain("wide-uncertainty");
    // ...and glaring on a Victorian one.
    const recent: BoundaryDating = {
      primary: claim({ value: { consensus: { year: ce(1870), fuzz: 50 } } }),
    };
    expect(disclosureReasons(recent)).toContain("wide-uncertainty");
  });
});

describe("rollup avoids marking the same thing twice", () => {
  const traditional = (y: IsoYear): BoundaryDating => ({
    primary: claim({ value: { consensus: { year: y } }, standing: "traditional" }),
  });

  it("collapses identical markers to one entity-level statement", () => {
    // Every legendary founder: accession and death are both traditional.
    expect(rollupDisclosure(traditional(bce(3100)), traditional(bce(3080)))).toEqual({
      shared: "Traditional date",
    });
  });

  it("keeps distinct markers on their own boundaries", () => {
    const r = rollupDisclosure(traditional(bce(753)), {
      primary: claim({ value: { consensus: { year: ce(476) } } }),
      reasons: ["definitional"],
    });
    expect(r.shared).toBeUndefined();
    expect(r.start).toBe("Traditional date");
    expect(r.end).toBe("Depends on definition");
  });

  it("is empty when nothing needs disclosing", () => {
    expect(rollupDisclosure({ primary: claim({ value: SEPT_11 }) }, undefined)).toEqual({});
  });
});

describe("date regime boundary", () => {
  it("puts historical dates inside the regime and deep time outside", () => {
    // Temporal throws beyond ~+/-271,821 years. Verified against the polyfill.
    expect(isDateRegime(bce(9530))).toBe(true);
    expect(isDateRegime(asIso(-271821))).toBe(true);
    expect(isDateRegime(asIso(-271822))).toBe(false);
    expect(isDateRegime(asIso(-3300000))).toBe(false);
  });

  it("keeps every calendar-bearing entity comfortably inside", () => {
    // The seam sits far outside any calendar's meaningful range, so it never
    // bisects something a user would expect to convert.
    for (const y of [bce(5508), bce(3760), bce(3114), bce(2637), bce(776), ce(622), ce(1912)]) {
      expect(isDateRegime(y)).toBe(true);
    }
  });
});
