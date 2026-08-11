"""Fold the app's existing global.languages branch into the new Languages tree.

Without this, Sanskrit appears in two columns: once under global.languages and once under
languages.indo-european.indo-iranian.indo-aryan. The user asked for exactly one home per language
under Languages, so the old branch has to be absorbed rather than left alongside.

Nothing outside the subtree refers into it -- no links, no cross_parent_ids, no foreign children,
no source_ids -- so this only touches its own 29 rows. Old ids become redirects, since the app
already carries a redirects map for exactly this.

Three of the 28 are whole-language entities spanning every stage, where the roster holds only the
stages. Latin runs 700 BCE to the present in the old data and the roster has Old, Classical, Vulgar
and Medieval Latin; Egyptian runs 3250 BCE to 1700 CE and the roster has Proto-, Old, Middle, Late,
Demotic and Coptic. Each corresponds to a CLADE, not to any one row, so the language becomes the
clade node and brings its name, dates and summary with it. That renames Glottolog's "Latinic" to
"Latin", which is what a reader searches for; the Glottolog label is kept as an alias.

Nahuatl is the exception among the three: there is no Nahuatl clade node to merge into, and Nahuatl
is not Classical Nahuatl -- the first is spoken by over a million people today, the second is a
sixteenth-century literary form. Both are kept, side by side.
"""

# Old id -> the NAME of the row it becomes, resolved against the tree at build time.
#
# This was a map of ids and it broke the moment the tree shifted: Hittite became one of the twelve
# languages merged into their own clade node, so its id moved and the migration failed. Names are
# stable across those rearrangements in a way ids are not, and every one below is unique in the
# tree, which `migrate` asserts.
MOVES = {
    "global.languages.akkadian": "Akkadian",
    "global.languages.ancient-greek": "Ancient Greek (Attic)",
    "global.languages.arabic": "Arabic",
    "global.languages.aramaic": "Aramaic",
    "global.languages.avestan": "Avestan",
    "global.languages.classical-maya": "Classical Maya (Ch'olti'an)",
    "global.languages.elamite": "Elamite",
    "global.languages.etruscan": "Etruscan",
    "global.languages.sumerian": "Sumerian",
    "global.languages.hebrew": "Hebrew",
    "global.languages.hittite": "Hittite",
    "global.languages.old-chinese": "Old Chinese",
    "global.languages.sanskrit": "Sanskrit",
    "global.languages.quechua": "Quechua",
    "global.languages.proto-afroasiatic": "Proto-Afroasiatic",
    "global.languages.proto-semitic": "Proto-Semitic",
    "global.languages.proto-indo-european": "Proto-Indo-European",
    "global.languages.proto-indo-iranian": "Proto-Indo-Iranian",
    "global.languages.proto-uralic": "Proto-Uralic",
    "global.languages.proto-sino-tibetan": "Proto-Sino-Tibetan",
    "global.languages.proto-austronesian": "Proto-Austronesian",
    "global.languages.proto-dravidian": "Proto-Dravidian",
    "global.languages.proto-japonic": "Proto-Japonic",
    "global.languages.proto-koreanic": "Proto-Koreanic",
    "global.languages.proto-bantu": "Proto-Bantu",
}


# The old entity carries its name, dates and summary onto the clade node, which had none.
BECOMES_CLADE = {
    "global.languages.latin": "Latinic",
    "global.languages.egyptian": "Egyptian",
}

# No clade to merge into, and genuinely distinct from the roster's Classical Nahuatl.
KEEP_ALONGSIDE = {
    "global.languages.nahuatl": "Classical Nahuatl",
}


def migrate(entities, tree_by_id, redirects):
    """Rewrite the old rows onto the new tree. Returns the ids to delete."""
    by_id = {e["id"]: e for e in entities}
    drop = set()

    # Names must be unique for this to be safe; say so loudly rather than pick one.
    by_name = {}
    for row in tree_by_id.values():
        by_name.setdefault(row["name"], []).append(row)
    wanted = set(MOVES.values()) | set(BECOMES_CLADE.values()) | set(KEEP_ALONGSIDE.values())
    bad = {n: len(by_name.get(n, [])) for n in wanted if len(by_name.get(n, [])) != 1}
    if bad:
        raise KeyError(f"migrate_existing: destination name(s) not unique in tree: {bad}")
    resolve = {n: by_name[n][0] for n in wanted}

    for old, new in MOVES.items():
        e = by_id.get(old)
        if e is None:
            continue
        target = resolve[new]
        # The tree row is authoritative for placement; the old row is authoritative for the
        # prose and dates a person wrote. Move those across, keep the tree's position.
        for field in ("summary", "date_note", "caveats", "source_ids", "historicity",
                      "date_standing", "search_phrase", "name_forms"):
            if e.get(field) and not target.get(field):
                target[field] = e[field]
        aliases = list(dict.fromkeys((target.get("aliases") or []) + (e.get("aliases") or [])))
        if aliases:
            target["aliases"] = [a for a in aliases if a != target.get("name")]
        redirects[old] = target["id"]
        drop.add(old)

    for old, node_id in BECOMES_CLADE.items():
        e, node = by_id.get(old), resolve.get(node_id)
        if e is None or node is None:
            continue
        glottolog_name = node.get("name")
        node["name"] = e["name"]
        node["start_year"] = e.get("start_year")
        node["end_year"] = e.get("end_year")
        node["start_dating_method"] = e.get("start_dating_method")
        if e.get("end_dating_method"):
            node["end_dating_method"] = e["end_dating_method"]
        if e.get("extant"):
            node["extant"] = True
        for field in ("summary", "date_note", "source_ids", "caveats"):
            if e.get(field):
                node[field] = e[field]
        # Keep Glottolog's own label reachable; a reader may well arrive with it.
        node["aliases"] = [a for a in dict.fromkeys(
            (node.get("aliases") or []) + (e.get("aliases") or []) + [glottolog_name])
            if a and a != node["name"]]
        redirects[old] = node["id"]
        drop.add(old)

    for old, sibling_name in KEEP_ALONGSIDE.items():
        e = by_id.get(old)
        if e is None:
            continue
        # Filed beside its classical form rather than merged into it: Nahuatl is spoken by over a
        # million people today and Classical Nahuatl is a sixteenth-century literary form.
        parent_id = resolve[sibling_name]["parent_id"]
        new_id = f"{parent_id}.{old.rsplit('.', 1)[-1]}"
        e["id"], e["parent_id"] = new_id, parent_id
        redirects[old] = new_id

    # The container itself. Its 15 children have all been relocated above.
    if "global.languages" in by_id:
        redirects["global.languages"] = "languages"
        drop.add("global.languages")

    return drop
