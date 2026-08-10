"""Assemble a consultation pack: schema, real field usage, and hard cases.

For an outside architecture review. The point of including real entities rather than a
prose description of the schema is that the schema and the practice have drifted, and the
drift is the interesting part. `date_precision` offers ten values and 85% of the dataset
uses one of them. A reviewer given only the enum would call it expressive; a reviewer given
the histogram sees the problem.

The hard cases are chosen to break things: a 3.3 Ma lithic industry, a legendary founder,
a traditional dating, a co-rulership, a still-inhabited city, a contested reign, and a
modern event dated to the day.
"""

import json
from collections import Counter

ENT = "src/data/entities.json"
SCHEMA = "schemas/entity.schema.json"
OUT = "docs/consult-pack.md"

# Chosen because each one strains the schema in a different direction. Ids are verified
# against the dataset at runtime rather than trusted -- guessing ids has bitten this
# project repeatedly.
HARD_CASES = [
    # deep time, huge uncertainty, radiometric dating
    ("Lomekwi", "lithic industry at 3.3 Ma -- the project's start point"),
    ("Oldowan", "long-running industry, typological dating"),
    ("Homo sapiens", "a taxon that is extant, so no end year"),
    # legendary and traditional
    ("Dangun", "legendary founder; existence contested, date traditional"),
    ("Fuxi", "mythic culture hero recorded as tradition, not finding"),
    ("Xia", "dynasty whose historicity is itself disputed"),
    # rival claims and contested dates
    ("Erlitou", "archaeological site attached to a disputed dynasty"),
    ("Qajar", "reign whose start date sources disagree on"),
    # co-rulership and overlapping authority
    ("Marcus Aurelius", "co-rule, needs a link not a date trick"),
    ("Munmu", "one person folded across two polities"),
    # cities, the newest kind
    ("Byblos", "city currently mis-kinded as era; inhabited today"),
    ("Tenochtitlan", "city mis-kinded as period; destroyed 1521"),
    # precise modern
    ("Apollo 11", "dated to the day"),
    ("Chernobyl", "modern event, exact calendar date"),
    # periodisation scaffolding
    ("Axial Age", "empty container; a thesis rather than a period"),
    ("Iron Age", "European periodisation applied globally"),
    ("Bronze Age Collapse", "systems event sharing a placeholder date with 9 others"),
]


def main():
    data = json.load(open(ENT))
    entities = data["entities"]
    sources = {s["id"]: s for s in data.get("sources", [])}
    schema = json.load(open(SCHEMA))
    props = schema.get("properties") or schema.get("items", {}).get("properties", {})

    out = []
    out.append("# Consultation pack: History & Prehistory dataset")
    out.append("")
    out.append(f"{len(entities)} entities, {len(sources)} sources, {len(props)} entity fields.")
    out.append("")

    # ---- field usage, which is where schema and practice diverge -------------
    out.append("## Field usage")
    out.append("")
    out.append("How often each field is actually populated. A field offered by the schema and "
               "used twice is a different thing from a field used everywhere.")
    out.append("")
    out.append("| field | populated | of | notes |")
    out.append("|---|---|---|---|")
    n = len(entities)
    for k in sorted(props):
        used = sum(1 for e in entities if e.get(k) not in (None, [], "", False))
        note = ""
        if "enum" in props[k]:
            vals = Counter(e.get(k) for e in entities if e.get(k))
            top = ", ".join(f"{v}:{c}" for v, c in vals.most_common(4))
            unused = [x for x in props[k]["enum"] if x not in vals]
            note = top
            if unused:
                note += f" — never used: {', '.join(map(str, unused))}"
        out.append(f"| `{k}` | {used} | {n} | {note} |")
    out.append("")

    # ---- the enums in full -------------------------------------------------
    out.append("## Controlled vocabularies")
    out.append("")
    for k in sorted(props):
        if "enum" in props[k]:
            out.append(f"- **`{k}`**: {', '.join(map(str, props[k]['enum']))}")
    # link types and caveat kinds live in nested schemas
    for path, label in [(("links", "items", "properties", "type"), "link `type`"),
                        (("caveats", "items", "properties", "kind"), "caveat `kind`"),
                        (("alternatives", "items", "properties", "standing"), "alternative `standing`"),
                        (("name_forms", "items", "properties", "kind"), "name_form `kind`")]:
        node = props
        for step in path:
            node = (node or {}).get(step) if isinstance(node, dict) else None
            if node is None:
                break
        if isinstance(node, dict) and "enum" in node:
            out.append(f"- **{label}**: {', '.join(map(str, node['enum']))}")
    out.append("")

    # ---- hard cases as real JSON ------------------------------------------
    out.append("## Worked examples: the hard cases")
    out.append("")
    out.append("Real records, verbatim. Each strains the schema differently.")
    out.append("")
    by_name = {}
    for e in entities:
        by_name.setdefault(e["name"].lower(), e)
    missing = []
    for needle, why in HARD_CASES:
        hit = None
        for nm, e in by_name.items():
            if needle.lower() in nm:
                hit = e
                break
        if hit is None:
            missing.append(needle)
            continue
        rec = {k: v for k, v in hit.items() if v not in (None, [], "")}
        if rec.get("source_ids"):
            rec["_sources_resolved"] = [
                {k: v for k, v in sources[s].items() if k in ("title", "publisher", "url", "kind")}
                for s in rec["source_ids"] if s in sources
            ]
        out.append(f"### {hit['name']} — {why}")
        out.append("")
        out.append("```json")
        out.append(json.dumps(rec, indent=2, ensure_ascii=False))
        out.append("```")
        out.append("")
    if missing:
        out.append(f"> Not found in the dataset, which is itself a finding: {', '.join(missing)}")
        out.append("")

    open(OUT, "w").write("\n".join(out) + "\n")
    print(f"wrote {OUT}")
    if missing:
        print(f"absent hard cases: {missing}")


if __name__ == "__main__":
    main()
