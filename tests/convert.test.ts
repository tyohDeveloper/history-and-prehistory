import { describe, expect, it } from "vitest";
import { readYear, readYearIn } from "../src/calendars/convert";
import { CALENDARS } from "../src/calendars/registry";
import { asIso, bce, ce } from "../src/chrono/year";

describe("a Gregorian year reads as a span", () => {
  it("spans two Islamic years, because the Hijri year does not start in January", () => {
    const r = readYear(ce(1492), "islamic");
    expect(r.from).toBe(897);
    expect(r.to).toBe(898);
    expect(r.label).toBe("897\u2013898 AH");
  });

  it("spans two Hebrew years", () => {
    const r = readYear(ce(2026), "hebrew");
    expect(r.to).toBe((r.from ?? 0) + 1);
  });

  it("does not span for calendars that start on 1 January", () => {
    const r = readYear(ce(1492), "common");
    expect(r.from).toBe(r.to);
  });
});

describe("validity travels with the reading", () => {
  it("flags a date before the calendar's epoch rather than printing a number", () => {
    // The polyfill will happily return Persian year -3921 here.
    const r = readYear(bce(3300), "persian");
    expect(r.validity).toBe("proleptic");
    expect(r.note).toContain("epoch");
  });

  it("accepts a date inside the window", () => {
    expect(readYear(ce(1500), "islamic").validity).toBe("ok");
  });

  it("flags a calendar that had fallen out of use", () => {
    expect(readYear(ce(1900), "roman-auc").validity).toBe("proleptic");
  });

  it("refuses deep time for every calendar", () => {
    for (const c of CALENDARS) {
      const r = readYear(asIso(-3_300_000), c.id);
      expect(r.validity).toBe("deep-time");
      expect(r.label).toBe("\u2014");
    }
  });

  it("never throws, whatever it is asked", () => {
    for (const c of CALENDARS) {
      for (const y of [asIso(-270000), bce(5000), bce(1), ce(1), ce(2026), asIso(270000)]) {
        expect(() => readYear(y, c.id)).not.toThrow();
      }
    }
  });
});

describe("arithmetic calendars", () => {
  it("counts AUC from the founding of Rome", () => {
    // Caesar was assassinated in 44 BCE, AUC 710.
    expect(readYear(bce(44), "roman-auc").from).toBe(710);
    expect(readYear(bce(753), "roman-auc").from).toBe(1);
  });

  it("numbers Olympiads in four-year cycles from 776 BCE", () => {
    expect(readYear(bce(776), "olympiad").label).toBe("Ol. 1.1");
    expect(readYear(ce(1), "olympiad").label).toBe("Ol. 195.1");
  });

  it("places the sexagenary cycle with 4 CE as jiazi", () => {
    expect(readYear(ce(4), "chinese-sexagenary").label).toContain("Jia-Zi");
    expect(readYear(ce(64), "chinese-sexagenary").label).toContain("Jia-Zi");
  });

  it("counts Juche from 1912", () => {
    expect(readYear(ce(2026), "juche").from).toBe(115);
  });

  it("renders a Maya Long Count", () => {
    expect(readYear(ce(2012), "maya-long-count").label).toMatch(/^\d+\.\d+\.\d+\.\d+\.\d+$/);
  });

  it("needs no year-zero correction, because the offset absorbs it", () => {
    // AUC 1 is 753 BCE = ISO -752, and -752 + 753 = 1. Adding a second
    // correction for AUC's own missing year zero would double-count.
    expect(readYear(bce(753), "roman-auc").from).toBe(1);
    expect(readYear(bce(752), "roman-auc").from).toBe(2);
    // Same on the other side of the ISO year zero.
    expect(readYear(bce(1), "roman-auc").from).toBe(753);
    expect(readYear(ce(1), "roman-auc").from).toBe(754);
  });

  it("counts Byzantine Anno Mundi from its 5509 BCE epoch", () => {
    expect(readYear(bce(5508), "byzantine-am").from).toBe(1);
    expect(readYear(ce(1), "byzantine-am").from).toBe(5509);
  });
});

describe("Julian", () => {
  it("diverges from Gregorian by the expected amount", () => {
    // Temporal has no julian calendar; this goes through the JDN module.
    expect(readYear(ce(1500), "julian").validity).toBe("ok");
    expect(readYear(ce(1500), "julian").from).toBe(1499);
  });

  it("reports Revised Julian as unsupported outside its window", () => {
    expect(readYear(ce(1000), "revised-julian").validity).toBe("outside-range");
    expect(readYear(ce(2000), "revised-julian").validity).toBe("ok");
  });
});

describe("reading many calendars at once", () => {
  it("returns one reading per requested calendar, in order", () => {
    const ids = ["common", "islamic", "hebrew"];
    const rs = readYearIn(ce(1492), ids);
    expect(rs.map((r) => r.calendarId)).toEqual(ids);
  });
});

describe("origin views are not routed through Temporal", () => {
  it("marks the era, so a BCE year cannot read as a CE one", () => {
    // Regression: reading eraYear off a Gregorian conversion returned 2900 for
    // 2900 BCE with the era in a separate field, so it rendered as "2900".
    expect(readYear(bce(2900), "common").label).toBe("2900 BCE");
    expect(readYear(ce(1603), "common").label).toBe("1603 CE");
    expect(readYear(bce(44), "gregorian").label).toBe("44 BC");
    expect(readYear(ce(1066), "gregorian").label).toBe("1066 AD");
  });

  it("shows ISO its own signed year, year zero included", () => {
    expect(readYear(bce(1), "iso8601").label).toBe("0");
    expect(readYear(bce(2), "iso8601").label).toBe("-1");
    expect(readYear(ce(1), "iso8601").label).toBe("1");
  });

  it("uses no thousands separators in years", () => {
    expect(readYear(ce(1603), "common").label).not.toContain(",");
    expect(readYear(bce(14000), "common").label).toBe("14000 BCE");
  });
});

describe("pre-epoch readings say so instead of printing a negative year", () => {
  it("replaces an extrapolated negative with a plain statement", () => {
    const persian = readYear(bce(2900), "persian");
    expect(persian.validity).toBe("proleptic");
    expect(persian.label).toBe("before epoch");
    expect(persian.label).not.toContain("-");
  });

  it("does the same for offset calendars", () => {
    const auc = readYear(bce(2900), "roman-auc");
    expect(auc.label).toBe("before epoch");
  });

  it("still prints real numbers inside the valid range", () => {
    expect(readYear(ce(1500), "persian").label).toMatch(/^\d+/);
    expect(readYear(bce(44), "roman-auc").label).toBe("710 AUC");
  });
});

describe("pre-epoch is detected from the epoch, not the sign", () => {
  it("catches Islamic Before-Hijra, which counts down from a positive year", () => {
    // Temporal returns era "bh" with eraYear 3630 falling to 3629, so a naive
    // sign check misses it and it renders as the broken range "3630-3629 AH".
    const r = readYear(bce(2900), "islamic");
    expect(r.validity).toBe("proleptic");
    expect(r.label).toBe("before epoch");
  });

  it("catches Persian, which counts up from a negative year", () => {
    expect(readYear(bce(2900), "persian").label).toBe("before epoch");
  });
});
