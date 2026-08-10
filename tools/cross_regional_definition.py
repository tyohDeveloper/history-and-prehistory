"""Cross-Regional Empires: say what the category means, and put the empires in it.

Parked five releases ago with "continue as is and revisit". Revisiting.

**The category was almost exactly inverted from its name.** It held nine
genuinely imperial entities -- the caliphates, the Ottomans, the Age of Sail,
the Scramble, decolonization -- and twelve that were not empires at all: two
world wars, the Cold War and its six events, plus the Bronze Age Collapse, the
Axial Age and the Black Death. Meanwhile every actual multi-region empire in the
dataset was filed under a single region: the Mongols under Central Asia, the
Achaemenids under Iran, the Spanish and Portuguese under Western Europe.

The twelve non-empires have moved (see `build_data.py`), and three of them
landed somewhere that was standing empty and waiting:

* the two world wars and the whole Cold War subtree into **global.short-20c**,
  Hobsbawm's short twentieth century, 1914-1991 -- which is precisely their span
  and had no children at all;
* the **Axial Age** into global.classical-antiquity, an exact fit at -800 to -200;
* the **Black Death** into global.middle-ages.

That the misfits fitted the empty eras this neatly is a sign the original
taxonomy was sound and the filing was not.

**The definition, now written down.** An entity belongs here if it is a single
polity whose territory spanned more than one of this dataset's regions, or a
process of imperial expansion or contraction that did the same. A worldwide
event that is nobody's property -- a war, a pandemic, a moon landing -- is
`global`. That test is stated in the entity itself so the next pass does not
have to reconstruct it.

**Empires are cross-linked, not moved.** The Mongol empire is Central Asian in
origin and belongs in Central Asia's tree; it is also, unarguably, cross-regional.
`cross_parent_ids` already existed for exactly this and was in use 22 times.
Moving them would gut the regions and break the breadcrumb that tells a reader
where a polity came from.

Note what this leaves: the Islamic caliphates are the only entities whose
*primary* home is this category, because they are the only ones the dataset
cannot reasonably file anywhere else -- Rashidun through Abbasid governed from
Arabia, Syria and Iraq in turn while ruling from Iberia to Central Asia. That is
a real finding about the caliphates rather than an accident of filing, and it is
the same feature that makes their naming hard, which is still outstanding.
"""

S_BURBANK_COOPER = "burbank-cooper-empires-world-history"
S_OWHE = "oxford-world-history-of-empire"

# Empires whose primary home is a single region but which plainly satisfy the
# test. Rome is included: it governed Europe, North Africa and West Asia, and
# leaving it out because it "feels" Mediterranean is exactly the reflex the
# category exists to correct.
CROSS_LINKED = [
    "central-asia.mongol-empire",
    "central-asia.timurid",
    "west-asia.iran.achaemenid",
    "europe.western.iberia.spanish-empire",
    "europe.western.iberia.portuguese-empire",
    "europe.western.britain.empire",
    "europe.eastern.russian-empire",
    "europe.mediterranean.rome.empire",
]


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}

    cr = by_id.get("cross-regional")
    if cr is not None:
        cr["summary"] = (
            "Empires that spanned more than one world region, and the processes that built "
            "and dismantled them."
        )
        cr["date_note"] = (
            "The test for this category: a single polity whose territory crossed more than one "
            "of this dataset's regions, or a process of imperial expansion or contraction that "
            "did the same. A worldwide event that belongs to nobody -- a war, a pandemic, a "
            "moon landing -- is filed under Global instead. Grouping the caliphates, the "
            "Mongols and the European maritime empires for comparison is a deliberate "
            "scholarly move, not a filing convenience: Burbank and Cooper treat them as "
            "comparable, and the Oxford World History of Empire frames the comparison as a "
            "corrective to older single-region imperial history."
        )
        cr["source_ids"] = sorted(set(list(cr.get("source_ids", [])) +
                                      [S_BURBANK_COOPER, S_OWHE]))
        cr["caveats"] = [c for c in cr.get("caveats", [])
                         if c.get("kind") != "naming-confusion"] + [
            {"kind": "naming-confusion",
             "text": "Most empires here are cross-linked from the region they came from, not "
                     "moved. The caliphates are the exception: they are the only ones with no "
                     "single regional home.",
             "source_ids": [S_BURBANK_COOPER]},
        ]

    for eid in CROSS_LINKED:
        e = by_id.get(eid)
        if e is None:
            continue
        existing = list(e.get("cross_parent_ids", []))
        if "cross-regional" not in existing:
            e["cross_parent_ids"] = existing + ["cross-regional"]
