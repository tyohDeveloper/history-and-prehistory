"""Author the modern era, which the dataset had almost entirely skipped.

Reported from use: 9/11 and the War on Terror were filed only under Global, there were no US
presidents, and there was no United Kingdom entity at all despite the Acts of Union being present.
Measuring it was worse than the examples suggested. The whole United States subtree was two rows,
itself and the Civil War. Britain was thirteen. India had ten prime ministers listed and Britain
and the United States had none between them. Across the entire world, 69 entities began in the
nineteenth century and 71 in the twentieth -- the two centuries with the best records anywhere.

The cause was the same one that produced the cities gap: the authoring passes followed the depth
of the prehistoric and ancient material and never came forward.

2,241 rows, enumerated by recall in three passes and then merged, deduplicated against the existing
corpus and against each other, and parent-resolved. 122 were dropped as duplicates of entities
already present and 34 as duplicates within the batch.

Every row here is a documentary date and carries no uncertainty bounds, which is deliberate and
matches the decision taken for the rest of the corpus: an invented interval is worse than none,
and a sourcing pass will add real ones where they belong.
"""

import json
import os

# The ids this module added, so the repair passes that follow only touch rows from this batch.
ADDED = set()

SOURCE = "docs/research/modern-merged.json"

# The merge resolved every parent to something that exists, but it ran against a snapshot. If a
# parent has since been renamed or re-kinded, fail loudly here rather than emitting an orphan.
_ALLOWED_KINDS = {
    "era", "polity", "culture", "period", "reign", "event", "city", "site",
    "person", "people", "network", "tradition", "language",
}


def extend(E, entities):
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), SOURCE)
    if not os.path.exists(path):
        print("author_modern: no merged file, skipping")
        return

    rows = json.load(open(path))
    existing = {e["id"] for e in entities}
    by_id = {e["id"]: e for e in entities}

    # Author parents before children, so a row whose parent is also new is never an orphan.
    rows.sort(key=lambda r: r["id"].count("."))

    added, skipped, orphaned = 0, [], []
    for r in rows:
        if r["id"] in existing:
            skipped.append(r["id"])
            continue
        parent = r.get("parent_id")
        if parent is not None and parent not in existing:
            orphaned.append(f"{r['id']} -> {parent}")
            continue
        if r["kind"] not in _ALLOWED_KINDS:
            raise ValueError(f"author_modern: {r['id']} has kind {r['kind']}")

        entity = {
            "id": r["id"],
            "name": r["name"],
            "kind": r["kind"],
            "parent_id": parent,
            "start_year": r["start_year"],
            # Required-but-nullable: the key must be present even when the entity continues.
            "end_year": r["end_year"],
            # `tier`, not `detail_tier`. Guessing a field name rather than looking it up is
            # the single most repeated mistake in this project's history.
            "tier": _tier(r),
            "start_dating_method": r["start_dating_method"],
        }
        if r.get("end_dating_method"):
            entity["end_dating_method"] = r["end_dating_method"]
        if r.get("extant"):
            entity["extant"] = True
        if r.get("summary"):
            entity["summary"] = r["summary"]
        if r.get("aliases"):
            entity["aliases"] = list(dict.fromkeys(r["aliases"]))

        entities.append(entity)
        ADDED.add(r["id"])
        existing.add(r["id"])
        by_id[r["id"]] = entity
        added += 1

    if orphaned:
        raise KeyError(f"author_modern: {len(orphaned)} row(s) have a missing parent: "
                       + "; ".join(orphaned[:5]))

    print(f"author_modern: added {added} entities"
          + (f", skipped {len(skipped)} already present" if skipped else ""))


def _tier(row):
    """Depth in the tree is the wrong proxy here, because a president sits deep and matters.

    A head of state or government, a war, and a nation are what a reader arrives looking for. The
    long tail of individual battles, court rulings and agencies is specialist.
    """
    kind, name = row["kind"], row["name"]
    if kind == "polity" and row.get("extant"):
        return "foundational"
    if kind == "reign":
        return "intermediate"
    if kind in {"era", "period"}:
        return "intermediate"
    if any(w in name for w in ("War", "Revolution", "Independence", "Partition", "Genocide")):
        return "intermediate"
    return "specialist"
