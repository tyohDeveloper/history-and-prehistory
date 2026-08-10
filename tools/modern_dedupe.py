"""Reconcile the modern batch against people the corpus already had.

The merge deduplicated on folded names and caught 122 collisions. It could not catch these,
because "Reign of Napoleon I" and "Napoleon I" are not the same string, and neither are
"Premiership of Jawaharlal Nehru" and "Jawaharlal Nehru". Validator rule 9, which compares people
by overlapping dates within a region rather than by name, caught all 24.

Three different things are tangled together in what it found, and they need different answers.

**A tenure filed twice.** Napoleon, Babur, Aurangzeb, Ivan IV, Peter the Great, Nehru, Jinnah and
the rest already existed. The new row is dropped and anything it carried that the old row lacks --
a summary, an alias, a modern name -- is moved across rather than thrown away.

**One person, two crowns.** James VI of Scotland and James I of England are one man, and so are
Charles I, Charles II, Mary II and James VII/II. Filing both is not a duplicate in the sloppy sense;
it is the Union of the Crowns being real. The Scottish row is dropped and its regnal name kept as
an alias, so a reader searching "James VI" still arrives.

**Not a duplicate at all.** Charles II of Spain and Charles II of England were different men who
reigned at the same time in the same continent, which is exactly the shape rule 9 looks for. The
answer there is to make the display names say which is which, not to delete either.
"""

import re

_TENURE = re.compile(
    r"^(?:Reign|Rule|Government|Leadership|Presidency|Premiership|Ministry|Term) of\s+", re.I
)
_SUFFIX = re.compile(r"\s+(?:Premiership|Presidency|Rule|Reign)$", re.I)

# The Scottish half of a dual monarchy: drop, keeping the Scottish regnal name searchable.
DUAL_CROWNS = {
    "europe.western.kingdom-of-scotland.james-vi-scotland": "europe.western.kingdom-of-england.james-i-england",
    "europe.western.kingdom-of-scotland.james-vii-scotland": "europe.western.kingdom-of-england.james-ii",
    "europe.western.kingdom-of-scotland.charles-i-scotland": "europe.western.kingdom-of-england.charles-i",
    "europe.western.kingdom-of-scotland.charles-ii-scotland": "europe.western.kingdom-of-england.charles-ii",
    "europe.western.kingdom-of-scotland.william-ii-mary-ii-scotland":
        "europe.western.kingdom-of-england.mary-ii",
}

# Same regnal number, same century, different men. Disambiguate rather than delete.
DISAMBIGUATE = {
    "europe.western.kingdom-of-england.charles-ii": "Charles II of England",
    "europe.western.kingdom-of-england.charles-i": "Charles I of England",
}

# `radiocarbon` is not in the schema's method list; the calibrated form is what was meant.
METHOD_FIXES = {"radiocarbon": "radiocarbon-calibrated"}


def _base_name(name):
    """The person's name, with the tenure wrapper removed."""
    return _SUFFIX.sub("", _TENURE.sub("", name)).strip()


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}
    fixed_methods = 0

    for e in entities:
        for ep in ("start", "end"):
            key = f"{ep}_dating_method"
            if e.get(key) in METHOD_FIXES:
                e[key] = METHOD_FIXES[e[key]]
                fixed_methods += 1

    # --- tenures filed twice -------------------------------------------------
    # Index the pre-existing rows by folded person name. Only rows NOT from the modern batch can
    # be the survivor, which is what `_is_new` decides: a batch row is one whose name is wrapped.
    wrapped = [e for e in entities if _TENURE.search(e["name"]) or _SUFFIX.search(e["name"])]
    plain = {}
    for e in entities:
        if e in wrapped:
            continue
        plain.setdefault(_fold(e["name"]), []).append(e)

    drop, merged = set(), 0
    for e in wrapped:
        base = _fold(_base_name(e["name"]))
        for other in plain.get(base, []):
            if not _same_person(e, other):
                continue
            _absorb(other, e)
            drop.add(e["id"])
            merged += 1
            break

    # --- dual crowns ---------------------------------------------------------
    crowns = 0
    for scot_id, eng_id in DUAL_CROWNS.items():
        scot, eng = by_id.get(scot_id), by_id.get(eng_id)
        if scot is None or eng is None:
            continue
        _absorb(eng, scot, keep_name_as_alias=True)
        drop.add(scot_id)
        crowns += 1

    # --- disambiguation ------------------------------------------------------
    renamed = 0
    for eid, name in DISAMBIGUATE.items():
        e = by_id.get(eid)
        if e is not None and e["name"] != name:
            e.setdefault("aliases", [])
            if e["name"] not in e["aliases"]:
                e["aliases"].append(e["name"])
            e["name"] = name
            renamed += 1

    if drop:
        # Reparent anything filed beneath a row about to disappear, so no branch is orphaned.
        for e in entities:
            if e.get("parent_id") in drop:
                gone = by_id[e["parent_id"]]
                e["parent_id"] = gone.get("parent_id")
        entities[:] = [e for e in entities if e["id"] not in drop]

    print(f"modern_dedupe: merged {merged} duplicate tenure(s), folded {crowns} dual crown(s), "
          f"disambiguated {renamed} name(s), fixed {fixed_methods} dating method(s)")


def _fold(text):
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def _same_person(a, b):
    """Overlapping tenures for the same name are the same person."""
    a0, a1 = a.get("start_year"), a.get("end_year") or a.get("start_year")
    b0, b1 = b.get("start_year"), b.get("end_year") or b.get("start_year")
    if None in (a0, b0):
        return False
    return a0 <= (b1 if b1 is not None else b0) and b0 <= (a1 if a1 is not None else a0)


def _absorb(keeper, doomed, keep_name_as_alias=False):
    """Move anything the doomed row has and the keeper lacks."""
    if not keeper.get("summary") and doomed.get("summary"):
        keeper["summary"] = doomed["summary"]
    extra = list(doomed.get("aliases") or [])
    if keep_name_as_alias:
        extra.append(doomed["name"])
    if extra:
        have = list(keeper.get("aliases") or [])
        keeper["aliases"] = [n for n in dict.fromkeys(have + extra) if n != keeper["name"]]


# The merge resolved a hint naming a country to whichever entity carried that country's name, and
# for many countries the only such entity is the CURRENT state. So Ethiopia's whole history was
# filed inside a republic founded in 1991, and the Oyo Empire of 1608 inside a Nigeria founded in
# 1960. A modern state is one polity in a sequence, not the container for everything before it.
# A place is not a container for a country. The merge matched a hint naming a nation to whichever
# entity carried a similar name, and for several nations the nearest match was an ancient city on
# the same ground: the Republic of Singapore was filed inside Temasek, Bahrain inside Dilmun,
# North Macedonia inside Stobi, Iceland inside Skalholt and Brunei inside Kota Batu.
_NOT_A_PARENT = {"city", "site"}


def reparent_off_places(E, entities):
    from author_modern import ADDED
    by_id = {e["id"]: e for e in entities}
    moved = 0
    for e in entities:
        if e["id"] not in ADDED:
            continue
        guard = 0
        while guard < 12:
            guard += 1
            parent = by_id.get(e.get("parent_id") or "")
            if parent is None or parent["kind"] not in _NOT_A_PARENT:
                break
            # A city may legitimately contain a site, and nothing else.
            if e["kind"] == "site" and parent["kind"] == "city":
                break
            e["parent_id"] = parent.get("parent_id")
            moved += 1
    print(f"modern_dedupe: lifted {moved} entity/entities out of a city or site")


def reparent_anachronisms(E, entities):
    # Only rows from this batch. Applied corpus-wide, this rule lifted Akkadian off Proto-Semitic,
    # because a language family is a descent claim rather than a chronological container and a
    # daughter language is attested long before the reconstruction date of its parent. The merge's
    # filing errors are the problem being solved; the rest of the tree was already correct.
    from author_modern import ADDED
    by_id = {e["id"]: e for e in entities}
    moved = 0
    for e in entities:
        if e["id"] not in ADDED:
            continue
        start = e.get("start_year")
        if start is None:
            continue
        guard = 0
        while guard < 12:
            guard += 1
            parent = by_id.get(e.get("parent_id") or "")
            if parent is None:
                break
            p_start = parent.get("start_year")
            # A region has no dates and is always a valid home.
            if p_start is None or p_start <= start:
                break
            # The parent begins after its child does, so the child belongs a level up.
            e["parent_id"] = parent.get("parent_id")
            moved += 1
    # The same again for the far end. A child outliving its parent is the same filing error seen
    # from the other side: the Velvet Divorce cannot sit inside Czechoslovakia and end after it.
    for e in entities:
        if e["id"] not in ADDED:
            continue
        end = e.get("end_year")
        if end is None:
            continue
        guard = 0
        while guard < 12:
            guard += 1
            parent = by_id.get(e.get("parent_id") or "")
            if parent is None:
                break
            p_end = parent.get("end_year")
            if p_end is None or p_end >= end:
                break
            e["parent_id"] = parent.get("parent_id")
            moved += 1
    print(f"modern_dedupe: lifted {moved} entity/entities out of a parent that postdates them")


# Same person, filed under the Norman dynasty and again under the kingdom. The dynasty entry is
# the older one and keeps its place; the batch row's fuller name becomes an alias.
LATE_DUPLICATES = {
    "europe.western.kingdom-of-england.william-the-conqueror": "europe.western.england.norman.william-i",
}

# Two rows may not present a reader with the same words under the same parent.
SIBLING_RENAMES = {
    "americas.north.mississippian.cahokia-1050": "Cahokia (Mississippian Phase)",
}


def resolve_collisions(E, entities):
    by_id = {e["id"]: e for e in entities}
    drop = set()
    for doomed_id, keeper_id in LATE_DUPLICATES.items():
        doomed, keeper = by_id.get(doomed_id), by_id.get(keeper_id)
        if doomed is None or keeper is None:
            continue
        _absorb(keeper, doomed, keep_name_as_alias=True)
        drop.add(doomed_id)

    renamed = 0
    for eid, name in SIBLING_RENAMES.items():
        e = by_id.get(eid)
        if e is not None:
            e.setdefault("aliases", [])
            if e["name"] not in e["aliases"]:
                e["aliases"].append(e["name"])
            e["name"] = name
            renamed += 1

    # Anything still sharing a name with a sibling gets its parent's name in parentheses, which is
    # the disambiguation a reader can actually act on.
    seen = {}
    for e in entities:
        if e["id"] in drop:
            continue
        seen.setdefault((e.get("parent_id"), e["name"]), []).append(e)
    for (parent_id, _name), group in seen.items():
        if len(group) < 2:
            continue
        for e in group[1:]:
            tail = e["id"].rsplit(".", 1)[-1].replace("-", " ").title()
            e.setdefault("aliases", [])
            if e["name"] not in e["aliases"]:
                e["aliases"].append(e["name"])
            e["name"] = f"{e['name']} ({tail})"
            renamed += 1

    if drop:
        for e in entities:
            if e.get("parent_id") in drop:
                e["parent_id"] = by_id[e["parent_id"]].get("parent_id")
        entities[:] = [e for e in entities if e["id"] not in drop]

    print(f"modern_dedupe: resolved {len(drop)} late duplicate(s), {renamed} sibling name clash(es)")


def resolve_cross_tree_names(E, entities):
    """A new row sharing a name with an existing one is either a duplicate or needs qualifying.

    Overlapping dates settle it. The Oyo Empire, Clovis, Folsom, Moundville, Acoma, British Burma,
    the Kingdom of Hawaii and the Indian Rebellion of 1857 already existed elsewhere in the tree,
    and the merge missed them because it compared names only within a compatible region -- the
    guard that correctly keeps Alexandria in Egypt apart from Alexandria in Virginia.

    The three that are not duplicates are the interesting ones. The State of Japan constituted in
    1947 is not the region called Japan; the American Early Republic is not Rome's; Constantine II
    of Scotland is not the Roman emperor. Those get their names qualified rather than deleted.
    """
    from author_modern import ADDED

    by_id = {e["id"]: e for e in entities}
    old_by_name = {}
    for e in entities:
        if e["id"] not in ADDED:
            old_by_name.setdefault(e["name"], []).append(e)

    drop, qualified = set(), 0
    for e in list(entities):
        if e["id"] not in ADDED:
            continue
        for other in old_by_name.get(e["name"], []):
            if _overlaps(e, other):
                _absorb(other, e)
                drop.add(e["id"])
            else:
                # Distinct things that happen to share words. The parent's name is the
                # disambiguation a reader can act on.
                # The DISPLAY name has to differ, not just the qualified form. Setting only
                # qualified_name left both rows still called "Japan", so the search index went on
                # treating the name as ambiguous and started qualifying the region too.
                parent = by_id.get(e.get("parent_id") or "")
                context = parent["name"] if parent else e["id"].split(".")[0].title()
                e.setdefault("aliases", [])
                if e["name"] not in e["aliases"]:
                    e["aliases"].append(e["name"])
                e["name"] = f"{e['name']} ({context})"
                e["qualified_name"] = e["name"]
                qualified += 1
            break

    if drop:
        for e in entities:
            if e.get("parent_id") in drop:
                e["parent_id"] = by_id[e["parent_id"]].get("parent_id")
        entities[:] = [e for e in entities if e["id"] not in drop]

    print(f"modern_dedupe: dropped {len(drop)} cross-tree duplicate(s), "
          f"qualified {qualified} shared name(s)")


def _overlaps(a, b):
    a0, a1 = a.get("start_year"), a.get("end_year")
    b0, b1 = b.get("start_year"), b.get("end_year")
    if a0 is None or b0 is None:
        return False
    return a0 <= (b1 if b1 is not None else b0) and b0 <= (a1 if a1 is not None else a0)
