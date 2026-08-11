"""Build the Languages branch: family nodes from Glottolog, languages beneath them.

Shape requested:

    Languages
      <family>            e.g. Indo-European
        <subfamily>...    the full descent chain, as deep as Glottolog goes
          <language>
      Isolates            languages with no demonstrable relatives
      Unclassified        languages the evidence cannot place

Two structural jobs beyond the copying.

**Collapse runs of pass-through nodes.** Glottolog's tree is built for linguistics, not reading, and
it contains long single-child chains that carry no information for a reader -- the user's example is
Ancient Latin -> Latin -> Vulgar Latin, three nodes describing one thing. A node is collapsed when
it has exactly one child and no language of its own sits at that level, which removes the padding
without ever merging two things a reader could tell apart. Chains are collapsed toward the NAMED
end, so the surviving node keeps the name a reader would search for.

**Anything that will not fit is listed, not guessed at.** 251 rows have no Glottolog path at all --
every proto-language, since a reconstruction has no glottocode, plus the ancient languages whose
codes did not resolve. Those are placed by their stated parent name where that resolves and reported
where it does not.
"""

import json
import os
import re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
HP = os.path.dirname(os.path.dirname(HERE))
GLOTTO = os.path.join(HP, "docs/research/glottolog")
LANG = os.path.join(HP, "docs/research/languages")

ROOT = "languages"


# Words that qualify a family name without changing which family it is.
_QUALIFIER = re.compile(
    r"\b(imperial|classical|common|proto|nuclear|core|greater|central|eastern|western|northern|"
    r"southern|old|middle|modern|early|late|inner|outer)\b", re.I)


def _stem(name):
    """Reduce a family name to the root a reader would recognise."""
    s = _QUALIFIER.sub("", str(name)).strip().lower()
    s = re.sub(r"[^a-z ]+", "", s).strip()
    # Family-forming suffixes: Latinic -> latin, Italic -> ital, Bantoid -> bant.
    s = re.sub(r"(ic|oid|ian|an|ese|ish|id)$", "", s)
    return s


def _same_stem(a, b):
    sa, sb = _stem(a), _stem(b)
    if not sa or not sb:
        return False
    # Exact stem equality only. `startswith` merged Latino-Faliscan into Imperial Latin, because
    # "latino falisc" starts with "latin" -- and Latino-Faliscan genuinely contains Faliscan as
    # well as Latin, so that merge destroyed a real distinction and hung all of Romance off a node
    # called Imperial Latin.
    return sa == sb


def slug(text):
    s = re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")
    return re.sub(r"-+", "-", s) or "unnamed"


def main():
    meta = json.load(open(os.path.join(GLOTTO, "meta.json")))
    paths = json.load(open(os.path.join(GLOTTO, "classification.json")))
    kept = json.load(open(os.path.join(LANG, "kept.json")))

    # ---- which family nodes are actually needed -----------------------------
    needed = set()
    for r in kept:
        for gc in r.get("path") or []:
            needed.add(gc)

    # ---- collapse pass-through chains --------------------------------------
    # Count, among needed nodes only, how many needed children each has, and whether any kept
    # language sits directly at that node.
    child_of = {}
    for gc in needed:
        p = [a for a in paths.get(gc, "").split("/") if a]
        child_of[gc] = p[-1] if p else None
    kids = defaultdict(set)
    for gc, parent in child_of.items():
        if parent:
            kids[parent].add(gc)
    lang_at = defaultdict(int)
    for r in kept:
        p = r.get("path") or []
        if p:
            lang_at[p[-1]] += 1

    # Collapse maps a node that DISAPPEARS to the node that absorbs it. The direction matters and
    # the first attempt had it backwards: collapsing a parent into its only child deleted
    # "Indo-European" in favour of "Classical Indo-European", and a reader searching the tree looks
    # for the famous short name. So a redundant CHILD is absorbed upward into its parent, and the
    # parent's name survives.
    collapsed = {}
    for gc in needed:
        parent = child_of.get(gc)
        if parent is None or parent not in needed:
            continue
        # This node is the parent's only child and holds no language of its own: it is padding
        # between its parent and its own descendants.
        if len(kids.get(parent, ())) == 1 and lang_at.get(gc, 0) == 0 and gc in kids.get(parent, ()):
            collapsed[gc] = parent
            continue
        # The user's Latin case, which the rule above cannot reach. Glottolog's chain there is
        # Latino-Faliscan -> Latinic -> Imperial Latin -> Latin, and a language sits at two of
        # those levels, so none of them is a pass-through. They are still three nodes saying
        # "Latin" to a reader. A node collapses into its single family child when the two share a
        # name stem, which merges Latinic and Imperial Latin into Latin while never merging two
        # nodes a reader could tell apart -- Italic does not share a stem with Latino-Faliscan and
        # survives, as does Latino-Faliscan itself, which really does contain Faliscan too.
        # Same-stem neighbours: Latinic and Imperial Latin both reduce to "latin", so the lower
        # one is absorbed into the higher and one node named Latin survives instead of three.
        if gc in meta and parent in meta and _same_stem(meta[gc]["name"], meta[parent]["name"]):
            collapsed[gc] = parent

    def resolve(gc):
        """Follow the collapse map to the node that survives."""
        seen = set()
        while gc in collapsed and gc not in seen:
            seen.add(gc)
            gc = collapsed[gc]
        return gc

    surviving = {gc for gc in needed if gc not in collapsed}

    # ---- emit -------------------------------------------------------------
    out = []
    out.append({
        "id": ROOT, "name": "Languages", "kind": "region", "parent_id": None,
        "summary": "The languages of the world, arranged by descent. Families and their "
                   "subgroups contain the languages that descend from them; isolates and "
                   "unclassified languages sit apart, since no descent can be shown for them.",
    })
    for special, label, why in (
        ("isolates", "Isolates",
         "A language isolate has no demonstrable relatives. That is a statement about the "
         "evidence, not about the language: Basque, Korean and Sumerian are isolates."),
        ("disputed", "Disputed Groupings",
         "Reconstructions of families that are proposed rather than accepted. Altaic, Amerind and "
         "Nostratic are the famous cases: each has been argued for and none commands agreement, so "
         "Glottolog recognises no such family and there is no clade for the reconstruction to sit "
         "at the root of. Recorded because the proposal is part of the history of the field."),
        ("unclassified", "Unclassified",
         "Attested too thinly to place in any family. Distinct from an isolate, where the "
         "evidence is good and the relatives simply are not there."),
    ):
        out.append({"id": f"{ROOT}.{special}", "name": label, "kind": "region",
                    "parent_id": ROOT, "summary": why})

    emitted = {}
    for gc in sorted(surviving, key=lambda g: len(paths.get(g, "").split("/"))):
        m = meta.get(gc)
        if m is None:
            continue
        chain = [resolve(a) for a in paths.get(gc, "").split("/") if a]
        chain = [c for c in chain if c in surviving and c != gc]
        parent = emitted.get(chain[-1]) if chain else ROOT
        if parent is None:
            parent = ROOT
        eid = f"{parent}.{slug(m['name'])}"
        emitted[gc] = eid
        out.append({
            "id": eid, "name": m["name"], "kind": "language", "parent_id": parent,
            "glottocode": gc, "is_family_node": True, "macroarea": m.get("macroarea"),
        })

    # A proto-language has no Glottocode, because a reconstruction is not an attested variety, so
    # it has no Glottolog path and cannot be placed by the loop below. But 58 of the 91 correspond
    # exactly, and strictly one-to-one, to a family node: Proto-Germanic is the language at the root
    # of the clade Glottolog calls Germanic.
    #
    # They stay SEPARATE entities, filed as the family node's first child, rather than merged into
    # it. Merging looks tidier and is wrong: Proto-Germanic was spoken from about 500 BCE to 200 CE
    # and then broke up, while the Germanic family runs to the present -- fifteen of its
    # twenty-seven languages are alive. Putting the proto's dates on the node would assert that
    # Germanic ended in 200 CE and would put all twenty-seven descendants outside their parent's
    # span. Keeping them apart also preserves the breakup as the dateable event it is.
    # Glottolog's name for a family is often not the one the roster used. These are the same
    # clades under different labels, which is normal -- Niger-Congo as traditionally named is
    # Glottolog's Atlantic-Congo, and Na-Dene is Athabaskan-Eyak-Tlingit.
    FAMILY_ALIAS = {
        "afroasiatic": "Afro-Asiatic",
        "niger-congo": "Atlantic-Congo",
        "na-dene": "Athabaskan-Eyak-Tlingit",
        "northeast caucasian": "Nakh-Daghestanian",
        "northwest caucasian": "Abkhaz-Adyge",
        "oto-manguean": "Otomanguean",
        "trans-new-guinea": "Nuclear Trans New Guinea",
        "algonquian": "Algic",
        "quechua": "Quechuan",
        "khoe": "Khoe-Kwadi",
        # Bantu was collapsed into Bantoid as a same-stem neighbour, so the proto lands there.
        "bantu": "Bantoid",
        "southern bantoid": "Bantoid",
    }

    fam_by_name = {}
    for gc in surviving:
        m = meta.get(gc)
        if m:
            fam_by_name.setdefault(m["name"].lower(), gc)

    def proto_home(row):
        base = re.sub(r"^(proto-|common )", "", row["name"].lower()).strip()
        base = re.sub(r"\s*\([^)]*\)\s*", "", base).strip()
        gc = fam_by_name.get(base)
        if gc is None:
            alias = FAMILY_ALIAS.get(base)
            if alias:
                gc = fam_by_name.get(alias.lower())
        return emitted.get(gc) if gc else None

    unplaced = []
    for r in kept:
        path = [resolve(a) for a in (r.get("path") or [])]
        path = [p for p in path if p in surviving]
        if r.get("classification") == "proto_language" and not path:
            parent = proto_home(r)
        elif r["isolate"]:
            parent = f"{ROOT}.isolates"
        elif path:
            parent = emitted.get(path[-1], ROOT)
        else:
            parent = None
        if parent is None:
            unplaced.append(r)
            parent = f"{ROOT}.unclassified"
        r["parent_id"] = parent
        r["entity_id"] = f"{parent}.{slug(r['name'])}"
        out.append(r | {"id": r["entity_id"], "kind": "language", "is_family_node": False})

    # Record every collapse so it can be reviewed and reversed one at a time.
    collapse_rows = []
    for gone, into in sorted(collapsed.items()):
        g, i = meta.get(gone, {}), meta.get(resolve(into), {})
        collapse_rows.append({
            "absorbed": g.get("name"), "absorbed_glottocode": gone, "absorbed_level": g.get("level"),
            "into": i.get("name"), "into_glottocode": resolve(into),
            "reason": ("same name stem" if _same_stem(g.get("name", ""), i.get("name", ""))
                       else "only child, held no language of its own"),
            "languages_below": sum(1 for r in kept
                                   if gone in (r.get("path") or [])),
        })
    json.dump(collapse_rows, open(os.path.join(LANG, "collapsed.json"), "w"),
              indent=1, ensure_ascii=False)

    # The rows with no Glottolog path all state a parent by NAME, and almost every one of those
    # names is something already in the tree -- Proto-Albanian says Proto-Indo-European, Old
    # Bengali says Gaudi Prakrit. Resolving by name takes several passes, because a row's stated
    # parent is sometimes itself still unplaced at the time we look.
    def _norm(n):
        n = re.sub(r"\s*[-—]\s*(Wikipedia|Glottolog).*$", "", str(n or ""), flags=re.I)
        n = re.sub(r"\s*\([^)]*\)\s*", " ", n)
        n = n.split("/")[0]
        return re.sub(r"[^a-z]+", "", n.lower())

    for _pass in range(6):
        known = {}
        for row in out:
            nm = row.get("name")
            if nm:
                known.setdefault(_norm(nm), row["id"])
        moved = 0
        for r in list(unplaced):
            target = known.get(_norm(r.get("parent_name")))
            if target is None or target == r["entity_id"]:
                continue
            new_id = f"{target}.{slug(r['name'])}"
            for row in out:
                if row.get("id") == r["entity_id"]:
                    row["parent_id"], row["id"] = target, new_id
                    break
            r["parent_id"], r["entity_id"] = target, new_id
            unplaced.remove(r)
            moved += 1
        if moved == 0:
            break

    # A historical stage whose stated parent is an intermediate nobody recorded -- Old Bengali says
    # Gaudi Prakrit, Old Tibetan says Proto-Bodish -- can still be placed, because its own modern
    # descendant IS in the tree. Strip the stage qualifier, find that language, and file the stage
    # alongside it.
    #
    # One trap this must not fall into: Ancient Macedonian is not an ancestor of Macedonian. The
    # first is Hellenic, the second is Slavic, and they share only a place name. Anything whose
    # candidate parent sits in a different top-level family is refused.
    # Verified by hand: the stage really is an earlier form of the modern language it names.
    # Ancient Macedonian is deliberately absent -- see the guard below.
    VOUCHED_STAGES = {
        "Early Assamese", "Old Bengali (Charyapada)", "Old Gujarati", "Old Kashmiri",
        "Old Latvian", "Old Malayalam", "Old Nepali", "Old Odia", "Old Punjabi", "Old Sindhi",
    }
    STAGE = re.compile(r"^(old|classical|ancient|early|middle|literary|elu)\b[\s(]*", re.I)
    by_name = {}
    for row in out:
        if row.get("name") and not row.get("is_family_node"):
            by_name.setdefault(_norm(row["name"]), row)

    refused = []
    for r in list(unplaced):
        stem = STAGE.sub("", re.sub(r"\s*\([^)]*\)\s*", " ", r["name"])).strip()
        modern = by_name.get(_norm(stem))
        if modern is None or modern.get("id") == r["entity_id"]:
            continue
        target = modern.get("parent_id")
        if not target:
            continue
        # Same top-level family, or refuse.
        # The guard has to hold when the row has NO Glottolog path too, which is exactly when it
        # is needed: Ancient Macedonian has no glottocode, so `path` is empty, so an earlier
        # version skipped the check and filed it under South Slavic beside modern Macedonian. The
        # two share a place name and nothing else -- one is Hellenic, the other Slavic. A row with
        # no path has no family to compare against, so it must be placed explicitly or not at all.
        if not r.get("path"):
            # Explicitly vouched for: each was checked against the modern language's own parent and
            # really is its earlier stage. There is nothing to verify mechanically, because a row
            # without a glottocode has no Glottolog path to compare -- which is precisely why
            # Ancient Macedonian must be refused here and placed by hand instead.
            if r["name"] not in VOUCHED_STAGES:
                refused.append(r["name"])
                continue
            # Vouched: fall through and place it.
        elif target.split(".")[1] != r["path"][0]:
            refused.append(r["name"])
            continue
        new_id = f"{target}.{slug(r['name'])}"
        for row in out:
            if row.get("id") == r["entity_id"]:
                row["parent_id"], row["id"] = target, new_id
                break
        r["parent_id"], r["entity_id"] = target, new_id
        unplaced.remove(r)
    # The last few, by hand. Ten are stages whose modern descendant is absent from the roster, so
    # the descendant heuristic had nothing to find; two are families the roster named in the
    # singular. Each is stated rather than inferred.
    MANUAL = {
        "Classical K'iche'": "Mayan", "Classical Mixtec": "Otomanguean",
        "Classical Newar (Nepal Bhasa)": "Sino-Tibetan", "Classical Zapotec": "Otomanguean",
        "Elu (Old Sinhala)": "Indo-Aryan", "Old Balinese": "Malayo-Polynesian",
        "Old Siamese (Sukhothai Thai)": "Tai-Kadai", "Old Tibetan": "Sino-Tibetan",
        "Dogon": "Atlantic-Congo", "Quechua": "Quechuan",
        # Usually classed with Greek, and emphatically not with the Slavic language that shares
        # the place name.
        "Ancient Macedonian": "Graeco-Phrygian",
        # Aquitanian is generally read as ancestral to Basque, which is an isolate, so it belongs
        # beside it rather than in a family.
        "Aquitanian": None,
    }
    # Proposed macro-families with no accepted clade to attach to.
    DISPUTED = {"Proto-Altaic", "Proto-Amerind", "Proto-Nostratic", "Proto-Nilo-Saharan",
                "Proto-Basque (Proto-Vasconic)"}

    fam_id_by_name = {}
    for row in out:
        if row.get("is_family_node"):
            fam_id_by_name.setdefault(row["name"], row["id"])

    for r in list(unplaced):
        if r["name"] in DISPUTED:
            target = f"{ROOT}.disputed"
        elif r["name"] in MANUAL:
            fam = MANUAL[r["name"]]
            target = fam_id_by_name.get(fam) if fam else f"{ROOT}.isolates"
        else:
            continue
        if target is None:
            continue
        new_id = f"{target}.{slug(r['name'])}"
        for row in out:
            if row.get("id") == r["entity_id"]:
                row["parent_id"], row["id"] = target, new_id
                if r["name"] in DISPUTED:
                    row["historicity"] = "contested"
                break
        r["parent_id"], r["entity_id"] = target, new_id
        unplaced.remove(r)

    if refused:
        print(f"  refused {len(refused)} stage placement(s) across family lines: {refused}")

    # Eleven glottocodes came out as BOTH a family node and a language, which is not a collision
    # between two things: it is one thing seen twice. Glottolog assigns family level to any
    # languoid that has sub-varieties, so Sanskrit is a family because it contains Vedic and
    # Classical Sanskrit, and Italian is a family because it contains its dialects. The language
    # carries the dates and the sources; the node carries nothing but the name. So the language
    # becomes the node, and whatever hung below the node now hangs below the language.
    #
    # This is the opposite call from the proto-languages, and for a reason. Proto-Germanic and the
    # Germanic clade have different spans -- the proto ended when it broke up, the clade runs to
    # the present -- so merging them would state something false. Sanskrit the language and the
    # Sanskrit clade are the same span, because the clade is nothing but Sanskrit and its own
    # stages.
    seen = {}
    dupes = []
    for row in out:
        prior = seen.get(row.get("id"))
        if prior is None:
            seen[row["id"]] = row
            continue
        node = prior if prior.get("is_family_node") else row
        lang = row if prior.get("is_family_node") else prior
        if node.get("glottocode") != lang.get("glottocode"):
            raise ValueError(f"id collision that is not one entity: {row['id']}")
        dupes.append(node)
        seen[row["id"]] = lang
    out[:] = [r for r in out if id(r) not in {id(d) for d in dupes}]

    # The same situation one level down, which the id check above cannot see: the clade node is
    # `mongolic.mongolian` and the language became `mongolic.mongolian.mongolian`, so the ids differ
    # while the entity is still doubled. A language whose parent is a family node of the same name
    # is that node.
    by_id_now = {r["id"]: r for r in out}
    absorbed = []
    for row in out:
        if row.get("is_family_node"):
            continue
        parent = by_id_now.get(row.get("parent_id") or "")
        if parent is None or not parent.get("is_family_node"):
            continue
        if parent.get("name") != row.get("name"):
            continue
        for other in out:
            if other.get("parent_id") == row["id"]:
                other["parent_id"] = parent["id"]
        row["id"], row["parent_id"] = parent["id"], parent.get("parent_id")
        absorbed.append(parent)
    out[:] = [r for r in out if id(r) not in {id(a) for a in absorbed}]
    print(f"  merged {len(dupes)} language(s) into their own clade node"
          + (f", {len(absorbed)} into a same-named parent" if absorbed else ""))

    # Two rows were parented onto a row that later moved: Literary Vietnamese onto Old Vietnamese,
    # and Proto-Eastern Sudanic onto Proto-Nilo-Saharan, both of which were relocated by the
    # passes above. Following the mover is the fix; the alternative is to order the passes so this
    # cannot happen, which is fragile in a different way.
    moved_ids = {}
    for row in out:
        for old in row.get("_former_ids", []) or []:
            moved_ids[old] = row["id"]
    present = {r["id"] for r in out}
    healed = 0
    for row in out:
        parent = row.get("parent_id")
        if parent and parent not in present:
            # Find the row whose id ends with the missing parent's last segment.
            tail = parent.rsplit(".", 1)[-1]
            cand = [r for r in out if r["id"].rsplit(".", 1)[-1] == tail]
            if len(cand) == 1:
                row["parent_id"] = cand[0]["id"]
                row["id"] = f"{cand[0]['id']}.{row['id'].rsplit('.', 1)[-1]}"
                healed += 1
    if healed:
        print(f"  re-attached {healed} row(s) whose parent had moved")

    json.dump(out, open(os.path.join(LANG, "tree.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(unplaced, open(os.path.join(LANG, "unplaced.json"), "w"), indent=1, ensure_ascii=False)

    fam = sum(1 for r in out if r.get("is_family_node"))
    print(f"tree: {len(out)} nodes = {fam} family/subgroup nodes + "
          f"{len(out) - fam - 3} languages + 3 containers")
    print(f"  collapsed {len(collapsed)} pass-through node(s) of {len(needed)} needed")
    print(f"  isolates: {sum(1 for r in kept if r['isolate'])}")
    print(f"  could not place: {len(unplaced)}")
    depths = [r["id"].count(".") for r in out]
    print(f"  max depth: {max(depths)}")


if __name__ == "__main__":
    main()
