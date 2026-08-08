import { describe, expect, it } from "vitest";
import { MAX_SELECTED, parseSelection, serializeSelection, toggleCalendar } from "../src/calendars/selection";

describe("selection lives in the URL, not in storage", () => {
  it("falls back to the default when the hash is absent or junk", () => {
    expect(parseSelection("")).toEqual(["common"]);
    expect(parseSelection("#cal=")).toEqual(["common"]);
    expect(parseSelection("#cal=not-a-calendar")).toEqual(["common"]);
  });

  it("reads a selection back", () => {
    expect(parseSelection("#cal=common,islamic")).toEqual(["common", "islamic"]);
  });

  it("drops unknown ids but keeps the valid ones", () => {
    expect(parseSelection("#cal=islamic,bogus,hebrew")).toEqual(["islamic", "hebrew"]);
  });

  it("deduplicates and caps a hand-edited URL", () => {
    expect(parseSelection("#cal=islamic,islamic")).toEqual(["islamic"]);
    const many = parseSelection("#cal=common,islamic,hebrew,persian,coptic,ethiopic,julian,indian");
    expect(many).toHaveLength(MAX_SELECTED);
  });

  it("omits the fragment entirely for the default selection", () => {
    expect(serializeSelection(["common"])).toBe("");
    expect(serializeSelection(["common", "islamic"])).toBe("#cal=common,islamic");
  });

  it("round-trips", () => {
    const ids = ["islamic", "hebrew", "julian"];
    expect(parseSelection(serializeSelection(ids))).toEqual(ids);
  });
});

describe("toggling", () => {
  it("adds and removes", () => {
    expect(toggleCalendar(["common"], "islamic")).toEqual(["common", "islamic"]);
    expect(toggleCalendar(["common", "islamic"], "islamic")).toEqual(["common"]);
  });

  it("never empties the readout", () => {
    expect(toggleCalendar(["common"], "common")).toEqual(["common"]);
  });

  it("refuses to exceed the cap", () => {
    const full = ["common", "islamic", "hebrew", "persian", "coptic", "ethiopic"];
    expect(toggleCalendar(full, "julian")).toEqual(full);
  });
});
