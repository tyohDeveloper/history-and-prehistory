import { describe, expect, it } from "vitest";
import { entities } from "../src/dataset/dataset";
import { buildIndex } from "../src/entity/tree";
import {
  ambiguousNames,
  handoffTargets,
  researchNote,
  searchQuery,
  wikipediaSearchUrl,
} from "../src/research/handoff";

const index = buildIndex(entities);
const ambiguous = ambiguousNames(entities);
const byId = (id: string) => {
  const e = index.byId.get(id);
  if (!e) throw new Error(`missing fixture entity: ${id}`);
  return e;
};

describe("ambiguity is measured from the dataset, not guessed", () => {
  it("finds the names that actually repeat", () => {
    // Two Emperor Taizongs (Tang and Song) and two Showa eras really exist here.
    expect(ambiguous.has("Emperor Taizong")).toBe(true);
    expect(ambiguous.size).toBeGreaterThan(5);
  });

  it("leaves unique names alone", () => {
    expect(ambiguous.has("Ramesses II")).toBe(false);
  });
});

describe("search queries", () => {
  it("uses the bare name when it is unambiguous", () => {
    const q = searchQuery(byId("east-asia.japan"), index, { ambiguous });
    expect(q).toBe("Japan");
  });

  it("adds a disambiguating ancestor when the name repeats", () => {
    const taizongs = entities.filter((e) => e.name === "Emperor Taizong");
    expect(taizongs.length).toBe(2);
    const queries = taizongs.map((e) => searchQuery(e, index, { ambiguous }));
    // Both get context, and the context distinguishes them from each other.
    for (const q of queries) expect(q.length).toBeGreaterThan("Emperor Taizong".length);
    expect(queries[0]).not.toBe(queries[1]);
  });

  it("skips an ancestor that would only repeat the name", () => {
    // Context is only appended when it carries new information.
    const e = { ...byId("east-asia.japan"), name: "Japan" };
    expect(searchQuery(e, index, { force: true })).not.toContain("Japan Japan");
  });
});

describe("URLs", () => {
  it("encodes the query and adds no tracking parameters", () => {
    const url = wikipediaSearchUrl("Alexander the Great");
    expect(url).toBe("https://en.wikipedia.org/w/index.php?search=Alexander%20the%20Great");
    expect(url).not.toContain("utm_");
  });

  it("handles non-Latin script", () => {
    expect(wikipediaSearchUrl("\u660E\u6CBB")).toContain("%E6%98%8E%E6%B2%BB");
  });

  it("gives descriptive link text rather than a bare URL", () => {
    const [target] = handoffTargets(byId("east-asia.japan"), index, { ambiguous });
    expect(target?.label).toContain("Search Wikipedia");
    expect(target?.label).not.toBe(target?.url);
  });
});

describe("research note is the offline answer", () => {
  const note = researchNote(byId("east-asia.japan"), index, {
    ambiguous,
    datasetVersion: "2.1.0",
  });

  it("carries the hierarchy, the dates, and the search to run later", () => {
    expect(note).toContain("# Japan");
    expect(note).toContain("East Asia > Japan");
    expect(note).toContain("https://en.wikipedia.org/w/index.php?search=");
  });

  it("leaves the user room to write", () => {
    expect(note).toContain("## Notes");
  });

  it("says plainly that it is not a citation", () => {
    expect(note).toContain("not a citation");
    expect(note).toContain("dataset 2.1.0");
  });
});
