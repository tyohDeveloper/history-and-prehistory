"""Split the dataset into reviewable batches for a correctness pass.

Every guard this project has works on structure and consistency. None of them knows whether a
claim is TRUE. That is how plus-or-minus a century got onto the Fall of the Berlin Wall, how the
September 11 attacks became `september-xi`, and how eleven caveats reading "omit" told readers that
Cicero's existence was in doubt: each was structurally valid and factually absurd, and in every case
the only thing that caught it was a person glancing at one entity.

So the batches are shaped for judgement rather than for validation. Each row carries what a reader
would see -- name, kind, dates, uncertainty, dating method, historicity, summary, placement -- and
the question asked is whether it is plausibly wrong.
"""

import json
import math
import os

BATCH_SIZE = 120
OUT_DIR = "docs/review"


def main():
    entities = json.load(open("src/data/entities.json"))["entities"]
    by_id = {e["id"]: e for e in entities}

    def crumb(e):
        parts, seen, cur = [], set(), e
        while cur is not None and cur["id"] not in seen:
            seen.add(cur["id"])
            parts.append(cur["name"])
            cur = by_id.get(cur.get("parent_id"))
        return " < ".join(parts[1:]) or "(root)"

    rows = []
    for e in entities:
        if e["kind"] == "region":
            continue
        rows.append({
            "id": e["id"],
            "name": e["name"],
            "kind": e["kind"],
            "under": crumb(e),
            "start": e.get("start_year"),
            "end": e.get("end_year"),
            "extant": e.get("extant"),
            "bounds": [e.get("start_year_min"), e.get("start_year_max")],
            "dated_by": e.get("start_dating_method"),
            "historicity": e.get("historicity"),
            "date_standing": e.get("date_standing"),
            "summary": e.get("summary"),
            "aliases": e.get("aliases"),
            "sourced": bool(e.get("source_ids")),
        })

    # Grouped by domain rather than sliced arbitrarily. A reviewer holding all 690 reigns can
    # notice that a dynasty's regnal lengths do not add up; a reviewer holding rows 841-960 of an
    # alphabetical list cannot notice anything.
    GROUPS = {
        "reigns": {"reign", "person"},
        "cities-a": {"city"},          # split by region below, since there are 1,438
        "polities": {"polity", "culture", "era"},
        "periods": {"period"},
        "concepts": {"language", "tradition", "people", "network", "threshold", "event", "taxon"},
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    written = []
    for label, kinds in GROUPS.items():
        chunk = [r for r in rows if r["kind"] in kinds]
        if label.startswith("cities"):
            # Two halves, split on the region prefix so each reviewer sees whole regions.
            chunk.sort(key=lambda r: r["id"])
            half = len(chunk) // 2
            for n, part in enumerate((chunk[:half], chunk[half:]), start=1):
                path = f"{OUT_DIR}/cities-{n}.json"
                json.dump(part, open(path, "w"), indent=1, ensure_ascii=False)
                written.append((f"cities-{n}", len(part)))
            continue
        chunk.sort(key=lambda r: r["id"])
        path = f"{OUT_DIR}/{label}.json"
        json.dump(chunk, open(path, "w"), indent=1, ensure_ascii=False)
        written.append((label, len(chunk)))

    for label, n in written:
        print(f"  {label}: {n} rows")


if __name__ == "__main__":
    main()
