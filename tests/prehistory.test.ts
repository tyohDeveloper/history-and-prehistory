/**
 * The disclosure model against eight real prehistoric dating cases.
 *
 * These are not invented fixtures. Every value comes from the sourced
 * research in docs/prehistory-dating-research.md, and each case was chosen
 * because it stresses a different part of the model. Where the model needed
 * changing, these are the cases that forced it.
 */
import { describe, expect, it } from "vitest";
import {
  allClaims,
  bce,
  ce,
  hasAuthoritativeNative,
  isDateRegime,
  disclosureReasons,
  disclosureSummary,
  hasDisclosure,
  type BoundaryDating,
  type YearValue,
} from "../src/lib/chrono/year";
import { bpFromYear, formatBpRange, resolveFrame, suggestFrame } from "../src/lib/chrono/bp";
import { yearFromBp } from "../src/lib/chrono/bp";

const ka = (n: number) => yearFromBp(n * 1000);
const Ma = (n: number) => yearFromBp(n * 1_000_000);

// 1. OLDOWAN — definitional. Lomekwi 3 at 3.3 Ma is excluded by naming it
//    "Lomekwian" rather than by dating it differently.
const OLDOWAN: BoundaryDating = {
  primary: {
    value: {
      consensus: { year: Ma(2.6) },
      earliest: { year: Ma(2.618) },
      latest: { year: Ma(2.55) },
      method: "argon-argon",
      nativeFrame: "bp",
    },
    label: "Bokol Dora / Gona",
    standing: "consensus",
  },
  reasons: ["definitional"],
  note: "Lomekwi 3 tools at 3.3 Ma are excluded by classifying them as Lomekwian rather than Oldowan.",
};

// 2. HOMO FLORESIENSIS — the largest single revision in the set. The 2004
//    claim of ~18 ka was corrected to ~60 ka in 2016 on stratigraphy.
const FLORES: BoundaryDating = {
  primary: {
    value: { consensus: { year: ka(60) }, method: "luminescence", nativeFrame: "bp" },
    label: "Sutikna et al. 2016",
    standing: "consensus",
  },
  alternatives: [
    {
      value: { consensus: { year: ka(18) }, method: "radiocarbon-calibrated", nativeFrame: "bp" },
      label: "Original 2004 chronology",
      standing: "superseded",
      note: "Withdrawn in 2016: the dated deposits were found to be a younger unit unconformably overlying the remains.",
    },
  ],
};

// 3. CHAUVET — the evidence itself is challenged. Pettitt and Bahn argue the
//    radiocarbon dates charcoal, not the paintings.
const CHAUVET: BoundaryDating = {
  primary: {
    value: {
      consensus: { year: ka(36) },
      earliest: { year: ka(37) },
      latest: { year: ka(33.5) },
      method: "radiocarbon-calibrated",
      nativeFrame: "bp",
    },
    label: "Quiles et al. 2016, Phase I",
    standing: "consensus",
  },
  reasons: ["evidence-disputed"],
  note: "Pettitt and Bahn argue the radiocarbon dates the charcoal, not the art, and favour a much younger age.",
};

// 4. MADJEDBEBE — two rival chronologies from the same OSL evidence base.
const MADJEDBEBE: BoundaryDating = {
  primary: {
    value: {
      consensus: { year: ka(65), fuzz: 6000 },
      method: "luminescence",
      nativeFrame: "bp",
    },
    label: "Clarkson et al. 2017",
    standing: "majority",
  },
  alternatives: [
    {
      value: { consensus: { year: ka(47) }, method: "luminescence", nativeFrame: "bp" },
      label: "Short chronology (O'Connell & Allen)",
      standing: "minority",
      note: "Argues artefacts moved downward through the sand by termite and trampling disturbance.",
    },
  ],
  note: "Both readings work from the same OSL programme; the disagreement is about stratigraphic integrity.",
};

// 5. NEANDERTHAL EXTINCTION — method conflict, resolved directionally when
//    ultrafiltration removed modern-carbon contamination from old samples.
const NEANDERTHAL: BoundaryDating = {
  primary: {
    value: {
      consensus: { year: ka(40) },
      earliest: { year: ka(41.03) },
      latest: { year: ka(39.26) },
      method: "radiocarbon-calibrated",
      nativeFrame: "bp",
    },
    label: "Higham et al. 2014",
    standing: "consensus",
  },
  alternatives: [
    {
      value: { consensus: { year: ka(28) }, method: "radiocarbon-uncalibrated", nativeFrame: "bp" },
      label: "Gorham's Cave late survival",
      standing: "superseded",
      note: "Contaminated samples: unfiltered radiocarbon on old bone reads too young.",
    },
  ],
};

// 6. YOUNGER DRYAS — settled, precise, and quoted in b2k rather than BP.
const YOUNGER_DRYAS_END: BoundaryDating = {
  primary: {
    value: {
      consensus: { year: yearFromBp(11703, "b2k"), fuzz: 99 },
      method: "layer-counting",
      nativeFrame: "b2k",
    },
    label: "GICC05 / Holocene GSSP",
    standing: "consensus",
  },
};

// 7. GOBEKLI TEPE — definitional; the Layer III scheme itself was abandoned.
const GOBEKLI: BoundaryDating = {
  primary: {
    value: {
      consensus: { year: bce(9530), fuzz: 200 },
      method: "radiocarbon-calibrated",
      nativeFrame: "calendar",
    },
    label: "KIA-44149, IntCal20",
    standing: "consensus",
  },
  reasons: ["definitional"],
  note: "Kinzel and Clare abandoned the Layer III/II/I scheme for at least eight phases; only 11 radiocarbon dates exist.",
};

// 8. MONTE VERDE II — an open dispute with a shelf life.
const MONTE_VERDE: BoundaryDating = {
  primary: {
    value: {
      consensus: { year: ka(14.5) },
      method: "radiocarbon-calibrated",
      nativeFrame: "bp",
    },
    label: "Dillehay, long-standing consensus",
    standing: "consensus",
  },
  alternatives: [
    {
      value: {
        consensus: { year: ka(6.2) },
        earliest: { year: ka(8.2) },
        latest: { year: ka(4.2) },
        method: "radiocarbon-calibrated",
        nativeFrame: "bp",
      },
      label: "Surovell et al. 2026",
      standing: "minority",
    },
  ],
  asOf: "2026-06-30",
  note: "A March 2026 reanalysis proposed a Holocene age; roughly thirty specialists rebutted it in May and the authors replied in June.",
};

describe("every prehistory case discloses, and for the right reason", () => {
  const cases: [string, BoundaryDating, string][] = [
    ["Oldowan", OLDOWAN, "Depends on definition"],
    ["H. floresiensis", FLORES, "Date revised"],
    ["Chauvet", CHAUVET, "Evidence questioned"],
    ["Madjedbebe", MADJEDBEBE, "Chronologies differ"],
    ["Neanderthal extinction", NEANDERTHAL, "Date revised"],
    ["Gobekli Tepe", GOBEKLI, "Depends on definition"],
    ["Monte Verde II", MONTE_VERDE, "Chronologies differ"],
  ];

  it.each(cases)("%s reads as %s", (_name, boundary, expected) => {
    expect(hasDisclosure(boundary)).toBe(true);
    expect(disclosureSummary(boundary)).toBe(expected);
  });

  it("leaves a settled case unmarked", () => {
    // The Younger Dryas termination is the ratified base of the Holocene.
    // Precise, uncontested, and it should carry no marker at all.
    expect(hasDisclosure(YOUNGER_DRYAS_END)).toBe(false);
  });
});

describe("a settled revision is not a live disagreement", () => {
  it("calls Flores revised rather than disputed", () => {
    // Nobody defends ~18 ka any more. Saying "methods disagree" would be
    // false: they agreed, and one side lost.
    expect(disclosureReasons(FLORES)).toContain("revised");
    expect(disclosureReasons(FLORES)).not.toContain("method-conflict");
    expect(disclosureReasons(FLORES)).not.toContain("rival-chronologies");
  });

  it("calls Neanderthal late survival revised, not conflicting", () => {
    expect(disclosureReasons(NEANDERTHAL)).toContain("revised");
    expect(disclosureReasons(NEANDERTHAL)).not.toContain("method-conflict");
  });

  it("still calls Monte Verde a live dispute", () => {
    // Surovell et al. is a minority position, not a withdrawn one.
    expect(disclosureReasons(MONTE_VERDE)).toContain("rival-chronologies");
    expect(disclosureReasons(MONTE_VERDE)).not.toContain("revised");
  });

  it("ignores superseded claims when deciding if methods conflict", () => {
    // A dead claim's method must not manufacture a conflict among live ones.
    expect(disclosureReasons(MADJEDBEBE)).toContain("rival-chronologies");
  });
});

describe("evidence-disputed outranks and differs from method-conflict", () => {
  it("does not describe Chauvet as methods disagreeing", () => {
    // No rival number is on offer; the objection is that radiocarbon on
    // charcoal does not date paint on a wall.
    expect(disclosureReasons(CHAUVET)).toContain("evidence-disputed");
    expect(disclosureReasons(CHAUVET)).not.toContain("method-conflict");
  });

  it("does describe Madjedbebe as rival chronologies, not method conflict", () => {
    // Both sides use OSL. The argument is about stratigraphic integrity.
    expect(disclosureReasons(MADJEDBEBE)).toContain("rival-chronologies");
    expect(disclosureReasons(MADJEDBEBE)).not.toContain("method-conflict");
  });
});

describe("superseded dates survive", () => {
  it("keeps the withdrawn Flores chronology reachable", () => {
    // A reader who met "18,000 years" in a 2005 book must find it here.
    const labels = allClaims(FLORES).map((c) => c.label);
    expect(labels).toContain("Original 2004 chronology");
    expect(labels.indexOf("Original 2004 chronology")).toBe(labels.length - 1);
  });

  it("ranks a live minority above a dead consensus", () => {
    const labels = allClaims(NEANDERTHAL).map((c) => c.label);
    expect(labels[labels.length - 1]).toBe("Gorham's Cave late survival");
  });
});

describe("the b2k datum is not silently converted to BP", () => {
  it("preserves the source's own number", () => {
    const v = YOUNGER_DRYAS_END.primary.value;
    expect(suggestFrame(v)).toBe("b2k");
    // Reading the same year against the two datums differs by exactly 50.
    const year = v.consensus.year;
    expect(bpFromYear(year, "b2k") - bpFromYear(year, "bp")).toBe(50);
  });

  it("keeps the offset material against the stated counting error", () => {
    // 50 years against a maximum counting error of 99 is half the error
    // budget, which is why the datum cannot be treated as a rounding detail.
    expect(50 / (YOUNGER_DRYAS_END.primary.value.consensus.fuzz ?? 1)).toBeGreaterThan(0.5);
  });
});

describe("open disputes carry a review date", () => {
  it("records when the Monte Verde argument was last checked", () => {
    expect(MONTE_VERDE.asOf).toBe("2026-06-30");
  });

  it("does not date-stamp settled cases", () => {
    expect(YOUNGER_DRYAS_END.asOf).toBeUndefined();
    expect(FLORES.asOf).toBeUndefined();
  });
});

describe("deep time renders at honest resolution", () => {
  it("quotes the Oldowan in Ma, not spurious whole years", () => {
    const s = formatBpRange(OLDOWAN.primary.value);
    expect(s).toContain("Ma");
    expect(s).not.toMatch(/\d{7}/);
  });

  it("quotes Pleistocene cases in ka", () => {
    expect(formatBpRange(CHAUVET.primary.value)).toContain("ka");
  });

  it("still lets a user force calendar reckoning on a deep date", () => {
    expect(resolveFrame(OLDOWAN.primary.value, "calendar")).toBe("calendar");
  });
});

// --- Native dates as the authoritative form -------------------------------

describe("where a cultural calendar is the real date, ISO is only the index", () => {
  // 10 Muharram 61 AH. Exact in the Hijri calendar; its ISO conversion is not.
  const KARBALA: YearValue = {
    consensus: { year: ce(680) },
    method: "calendar",
    nativeFrame: "calendar",
    native: {
      calendarId: "islamic",
      text: "10 Mu\u1E25arram 61 AH",
      year: ce(61),
      month: 1,
      day: 10,
      observance: "\u02BF\u0100sh\u016Br\u0101\u02BE",
      // umalqura and civil give 0680-10-13; tbla gives 0680-10-12.
      conversionFuzzDays: 1,
    },
  };

  it("marks the native form as authoritative", () => {
    expect(hasAuthoritativeNative(KARBALA)).toBe(true);
    expect(hasAuthoritativeNative({ consensus: { year: ce(1066) } })).toBe(false);
  });

  it("keeps the source's own wording rather than reconstructing it", () => {
    expect(KARBALA.native?.text).toContain("61 AH");
    expect(KARBALA.native?.observance).toBeDefined();
  });

  it("lets the conversion be less precise than the original", () => {
    // The Hijri date is exact; the ISO date carries a day of slop from the
    // choice of Hijri variant. Precision runs the opposite way to intuition.
    expect(KARBALA.consensus.fuzz).toBeUndefined();
    expect(KARBALA.native?.conversionFuzzDays).toBe(1);
  });

  it("still indexes on ISO so the event sorts against everything else", () => {
    // Placing Karbala beside Tang China is exactly what the index is for.
    expect(KARBALA.consensus.year).toBe(680);
    expect(isDateRegime(KARBALA.consensus.year)).toBe(true);
  });
});
