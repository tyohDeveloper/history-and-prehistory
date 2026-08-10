"""File recent events where a reader would look for them, and say who fought.

Reported from use: the September 11 attacks and the War on Terror sat only under Global &
Multi-Regional, so drilling into the United States found the Civil War and nothing else. An attack
on New York and Washington belongs under the country it happened in, whatever else is also true
about it.

The War on Terror is the more interesting case and the user put it well: it was exclusively American
in the sense that the United States declared, led, funded and defined it -- while NATO invoked
Article 5 for the first and only time in its history, so the fighting was genuinely multinational.
Neither "American" nor "global" alone is accurate, and the dataset has two separate fields that
together say it exactly: `cross_parent_ids` puts it under the United States as well as the global
branch, and `regions` names the places it was actually fought in.

That distinction is worth keeping straight, because it is the difference between where a thing is
filed and where it happened. Filing is for the reader; regions are a claim about the world.
"""

# entity id -> (also-file-under, regions it actually touched)
PLACEMENTS = {
    "global.contemporary.september-11": (
        ["americas.north.usa"],
        None,
    ),
    "global.contemporary.war-on-terror": (
        ["americas.north.usa"],
        ["americas", "west-asia", "central-asia", "europe", "africa"],
    ),
}

NOTES = {
    "global.contemporary.war-on-terror":
        "Declared and led by the United States; NATO invoked Article 5 for the only time in its "
        "history, so the campaigns were multinational. Filed under both.",
}


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}
    missing = [i for i in PLACEMENTS if i not in by_id]
    if missing:
        raise KeyError(f"contemporary_placement: missing id(s): {missing}")

    for eid, (also_under, regions) in PLACEMENTS.items():
        e = by_id[eid]
        for target in also_under:
            if target not in by_id:
                raise KeyError(f"contemporary_placement: cross-parent {target} does not exist")
            existing = e.setdefault("cross_parent_ids", [])
            if target not in existing:
                existing.append(target)
        if regions:
            e["regions"] = regions
        note = NOTES.get(eid)
        if note:
            prior = (e.get("date_note") or "").strip()
            if note not in prior:
                e["date_note"] = (prior + " " + note).strip()

    print(f"contemporary_placement: {len(PLACEMENTS)} entity/entities also filed "
          "under the country involved")
