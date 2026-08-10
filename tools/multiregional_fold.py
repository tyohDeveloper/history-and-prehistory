"""Fold Cross-Regional into Global & Multi-Regional, and cross-link the empires to the regions they held.

"Cross" implies crossing from one place to another, which is wrong for a polity
that was simply in several places at once. Multi-regional is the better word and
the top-level peer entry goes away.

**Structure.** The nine entities lose their own top-level region and become
children of `global.multi-regional`, one level under Global & Multi-Regional.
Not children of `global` directly: it already holds fifteen chronological
frames, and putting the Abbasid Caliphate between the Bronze Age and the Middle
Ages mixes polities with periodisation. The intermediate node keeps the
distinction the earlier pass drew -- worldwide versus several-places-at-once --
while removing the misleading top-level entry.

**Nothing is lost, and reach is inherited.** Each empire is cross-linked to the
regions it actually held, and because `tree.ts` places an entity under every
cross-link, its *children* come with it. Cross-linking the Ottoman Empire to
Anatolia and the Nile means Suleiman is reachable at Anatolia → Ottoman →
Suleiman and at Nile Valley → Ottoman → Suleiman, without touching his entity at
all. Nine cross-link lists cover several hundred descendants.

**These are territorial claims, so they are the authored kind.** The previous
pass drew a line: a *derived* `regions` list can say where an entity is placed,
but where a polity ruled has to be asserted deliberately. These lists are that
assertion. They are deliberately coarse -- the region a polity substantially
held, not every province it ever raided -- and the sources already on each entity
carry the extent.

Two judgement calls worth recording. The **Rashidun** caliphate is given West
Asia and Africa but not Central Asia: it reached Khorasan only at the very end
and the eastward push belongs to the Umayyads. **Columbus** is a point event, so
it gets the Americas and Europe rather than a list of everywhere the consequences
reached, which would be the whole dataset.
"""

# Region reach per multi-regional entity. Coarse by design: substantial control
# rather than maximum extent, since the alternative is an argument per province.
REACH = {
    "rashidun": ["west-asia", "africa"],
    "umayyad": ["west-asia", "africa", "europe", "central-asia"],
    "abbasid": ["west-asia", "africa", "central-asia"],
    "fatimid": ["africa", "west-asia"],
    "ottoman": ["west-asia", "africa", "europe"],
    "age-of-sail": ["europe", "africa", "americas", "south-asia", "southeast-asia"],
    "columbus": ["americas", "europe"],
    "scramble-for-africa": ["africa", "europe"],
    "decolonization": ["africa", "south-asia", "southeast-asia", "west-asia"],
}

# Sub-region targets where a whole continent overstates it. Anatolia and the
# Nile are where the Ottomans actually sat; "Europe" for them means the Balkans.
PRECISE = {
    "ottoman": ["west-asia.anatolia", "africa.nile", "europe.eastern"],
    "fatimid": ["africa.nile", "west-asia.mesopotamia"],
    "rashidun": ["west-asia.arabia", "africa.nile"],
    "umayyad": ["west-asia.mesopotamia", "africa.north", "europe.western"],
    "abbasid": ["west-asia.mesopotamia", "central-asia"],
    "scramble-for-africa": ["africa", "europe"],
}


S_BURBANK_COOPER = "burbank-cooper-empires-world-history"
S_OWHE = "oxford-world-history-of-empire"


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}

    mr = by_id.get("global.multi-regional")
    if mr is None:
        return

    # The warrant for comparing caliphates with maritime empires belonged to the
    # retired category and has to move with it, or two good sources become dead
    # registry weight.
    mr["source_ids"] = [S_BURBANK_COOPER, S_OWHE]
    mr["caveats"] = [
        {"kind": "naming-confusion",
         "text": "Called multi-regional, not cross-regional: these polities were in several "
                 "regions at once rather than crossing from one to another.",
         "source_ids": [S_BURBANK_COOPER]},
    ]
    mr["date_note"] = (mr.get("date_note", "") + " Grouping the caliphates, the Mongols and "
                       "the European maritime empires for comparison is a deliberate "
                       "scholarly move: Burbank and Cooper treat them as comparable, and the "
                       "Oxford World History of Empire frames the comparison as a corrective "
                       "to older single-region imperial history.").strip()

    moved = 0
    for slug, regions in REACH.items():
        e = by_id.get(f"global.multi-regional.{slug}")
        if e is None:
            continue
        e["parent_id"] = "global.multi-regional"
        targets = PRECISE.get(slug, regions)
        e["cross_parent_ids"] = sorted(set(list(e.get("cross_parent_ids", [])) + targets))
        moved += 1

    # The eight empires previously cross-linked to `cross-regional` keep their
    # regional homes; the pointer just moves to the surviving node.
    for e in entities:
        cps = e.get("cross_parent_ids")
        if not cps or "cross-regional" not in cps:
            continue
        e["cross_parent_ids"] = sorted({c for c in cps if c != "cross-regional"} |
                                       {"global.multi-regional"})

    # Retire the top-level entry. Keeping an empty region in the picker would be
    # worse than either fixing or removing it.
    for i, e in enumerate(list(entities)):
        if e["id"] == "cross-regional":
            entities.pop(i)
            break

    print(f"Multi-regional: folded {moved} entities out of the top-level category")
