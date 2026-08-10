"""Adjectival name forms, and the qualified names that separate colliding display names.

Two distinct problems from issue #40, both about names rather than ids.

**"Rome" and "Roman" are the same referent in different grammatical forms** and the model had
nowhere to say so. That was half the cause of a reported bug: searching "Rome" returned no
Roman rulers, because no ancestor of an emperor was named anything a prefix match on "Rome"
could reach -- "Roman Empire" starts "Roman", and "Roman" does not start with "Rome". The
`adjectival` name form closes that, and it generalises: Ptolemaic for the Ptolemies, Achaemenid
for Achaemenid Persia, Byzantine, Carthaginian, Athenian.

**Fifteen display names collide.** Ten Japanese era names romanise identically in pairs, three
Chinese emperors share regnal names across dynasties, and Mesoamerica and Andes each appear at
two points in the region tree. None of these are siblings, so no id collides and the tree reads
correctly in place -- but a search result or a link chip shown out of context is ambiguous. The
qualified name adds the shortest distinguishing context, and it is derived rather than authored
so it cannot drift from the thing it distinguishes.
"""

import collections

# Adjectival forms worth authoring. Restricted to cases where the adjective is what a reader
# is actually likely to type or to encounter in prose, rather than every possible derivation.
ADJECTIVAL = {
    "europe.mediterranean.rome": ["Roman"],
    "europe.mediterranean.rome.empire": ["Roman", "Imperial Roman"],
    "europe.mediterranean.rome.republic": ["Roman Republican"],
    "europe.mediterranean.rome.kingdom": ["Roman"],
    "africa.nile.egypt": ["Egyptian"],
    "africa.nile.egypt.ptolemaic": ["Ptolemaic"],
    "west-asia.iran.achaemenid": ["Achaemenid", "Persian"],
    "west-asia.iran.sasanian": ["Sasanian", "Sassanid"],
    "west-asia.iran.parthian": ["Parthian"],
    "europe.mediterranean.byzantine": ["Byzantine"],
    "europe.mediterranean.greece": ["Greek", "Hellenic"],
    "west-asia.mesopotamia.assyrian": ["Assyrian"],
    "west-asia.mesopotamia.old-babylonian": ["Babylonian"],
    "west-asia.mesopotamia.sumerian": ["Sumerian"],
    "east-asia.china.han": ["Han"],
    "east-asia.china.tang": ["Tang"],
    "east-asia.china.song": ["Song"],
    "east-asia.china.ming": ["Ming"],
    "east-asia.china.qing": ["Qing", "Manchu"],
    "south-asia.maurya": ["Mauryan"],
    "south-asia.gupta": ["Gupta"],
    "americas.mesoamerica.maya": ["Mayan", "Maya"],
    "americas.andes.inca": ["Incan", "Inca"],
}


# Names an entity is genuinely known by, where the dataset carried only one of them. Reported
# from use: the Berlin Conference is also the Congo Conference and the West Africa Conference,
# and a reader arriving with either of those found nothing.
MISSING_ALIASES = {
    "global.multi-regional.berlin-conference": [
        ("Congo Conference", "common"),
        ("West Africa Conference", "common"),
        ("Kongokonferenz", "endonym"),
    ],
}


def _qualifier(entity, by_id):
    """The shortest context that distinguishes this entity from its namesakes."""
    parent = by_id.get(entity.get("parent_id"))
    if parent is not None:
        return parent["name"]
    year = entity.get("start_year")
    if year is not None:
        return f"{abs(year)} {'BCE' if year < 0 else 'CE'}"
    return None


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}

    # ---- adjectival forms -------------------------------------------------
    added = 0
    missing = []
    for eid, adjectives in ADJECTIVAL.items():
        e = by_id.get(eid)
        if e is None:
            missing.append(eid)
            continue
        forms = e.setdefault("name_forms", [])
        have = {f.get("name") for f in forms}
        for adj in adjectives:
            if adj not in have and adj != e["name"]:
                forms.append({"name": adj, "kind": "adjectival"})
                added += 1
    print(f"name_repair: {added} adjectival form(s) added"
          + (f"; {len(missing)} target(s) absent: {missing[:3]}" if missing else ""))

    # ---- alternate names an entity is genuinely known by ------------------
    alias_added = 0
    for eid, forms in MISSING_ALIASES.items():
        e = by_id.get(eid)
        if e is None:
            raise KeyError(f"name_repair: MISSING_ALIASES names a missing id: {eid}")
        existing = {f.get("name") for f in (e.get("name_forms") or [])}
        for value, kind in forms:
            if value not in existing:
                e.setdefault("name_forms", []).append({"name": value, "kind": kind})
                alias_added += 1
    if alias_added:
        print(f"name_repair: {alias_added} alternate name(s) added")

    # ---- qualified names for colliding display names ----------------------
    counts = collections.Counter(e["name"] for e in entities)
    collisions = {n for n, c in counts.items() if c > 1}
    qualified = 0
    unresolved = []
    for e in entities:
        if e["name"] not in collisions:
            continue
        q = _qualifier(e, by_id)
        if q is None or q == e["name"]:
            unresolved.append(e["id"])
            continue
        e["qualified_name"] = f"{e['name']} ({q})"
        qualified += 1

    print(f"name_repair: {qualified} qualified name(s) derived for "
          f"{len(collisions)} colliding display name(s)")
    if unresolved:
        print(f"  no qualifier available for: {unresolved}")
