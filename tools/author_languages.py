"""Author the Languages branch into the dataset.

1,157 languages on 1,182 Glottolog family nodes, plus Isolates, Disputed Groupings and
Unclassified. The existing global.languages branch is folded in rather than left beside it, so no
language appears in two columns under Languages.

Dates come from the two research files, which disagree about which format carries them: Tier 1 has
yearsSpoken in its JSON, Tier 2 has Start/End columns in its spreadsheet. Both are fully dated.

Family nodes get no dates of their own from Glottolog, which dates nothing. Rather than leave 1,182
nodes undated and therefore invisible on a timeline, each takes the hull of its descendants: a clade
begins when its earliest member begins and continues while any member survives. That is what a
family's temporal extent means, and it is why the proto-languages are kept separate -- Proto-Germanic
ended when it broke up, Germanic did not.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "languages"))

TREE = "docs/research/languages/tree.json"

# Bounds are deliberately absent everywhere: the dataset deleted its fabricated intervals, and a
# researched range like "3000 BCE - 1600 CE" for a divergence estimate is a claim about the estimate,
# not a measurement. It is recorded in date_note instead, where it reads as what it is.
# Authored handoff phrases, keyed by name rather than id: a language's id changes whenever the
# clades above it are merged or collapsed, and Old Chinese changed three times in one afternoon.
_SEARCH_PHRASES = {
    "Old Chinese": "Old Chinese reconstruction Shijing rhymes",
    "Classical Maya (Ch'olti'an)": "Classical Maya script decipherment",
}

_BASIS_METHOD = {
    "attestation": "first-attestation",
    "periodization": "received",
    "divergence": "glottochronology",
    "unity": "glottochronology",
    "breakup": "glottochronology",
    "extinction_record": "received",
    "living": "calendar",
    "calendar": "calendar",
}


def _method(basis, year):
    m = _BASIS_METHOD.get(str(basis or "").strip().lower())
    if m is None:
        return "calendar" if (year is not None and year >= 1500) else "unknown"
    # An attestation is a written one, and writing does not reach back past the fourth millennium
    # BCE anywhere. Karankawa and Kusunda are both dated to 4000 BCE from a basis the roster calls
    # attestation, which cannot be what happened -- the date is a guess at time-depth for an
    # isolate, so it takes the method that says so. Rule 15 caught both.
    if m == "first-attestation" and year is not None and year < -3400:
        return "glottochronology"
    return m


def extend(E, entities):
    root = os.path.dirname(HERE)
    path = os.path.join(root, TREE)
    if not os.path.exists(path):
        print("author_languages: no tree, skipping")
        return {}

    from migrate_existing import migrate
    from cross_parents import extend as apply_cross_parents

    tree = json.load(open(path))
    existing = {e["id"] for e in entities}

    # An empty container dead-ends a reader who drills into it. Every row found a home, so
    # Unclassified has no members and is dropped rather than shipped hollow.
    has_children = {r.get("parent_id") for r in tree}
    out = []
    for row in tree:
        eid = row["id"]
        if row.get("kind") == "region" and eid != "languages" and eid not in has_children:
            continue
        is_family = bool(row.get("is_family_node")) or row.get("kind") == "region"
        e = {
            "id": eid,
            "name": row["name"],
            "kind": "region" if row.get("kind") == "region" else "language",
            "parent_id": row.get("parent_id"),
            "tier": "foundational" if eid.count(".") <= 1 else (
                "intermediate" if is_family or row.get("tier") == 1 else "specialist"),
        }
        if row.get("summary"):
            e["summary"] = row["summary"]

        if not is_family:
            lo, hi = row.get("start_lower"), row.get("start_upper")
            e["start_year"] = lo
            e["end_year"] = None if row.get("living") else row.get("end_upper")
            e["start_dating_method"] = _method(row.get("start_basis"), lo)
            if e["end_year"] is not None:
                e["end_dating_method"] = _method(row.get("end_basis"), e["end_year"])
            if row.get("living"):
                e["extant"] = True
            notes = []
            if lo is not None and hi is not None and hi != lo:
                notes.append(f"Start estimated between {_yr(lo)} and {_yr(hi)}.")
            el, eu = row.get("end_lower"), row.get("end_upper")
            if el is not None and eu is not None and el != eu and not row.get("living"):
                notes.append(f"End estimated between {_yr(el)} and {_yr(eu)}.")
            if notes:
                e["date_note"] = " ".join(notes)
            # Glottolog is the authority for placement, so any row it classified cites it. Rows
            # with no glottocode -- reconstructions and a handful of ancient stages -- were placed
            # by hand, and rule 7 requires a citation from anything that cross-links into another
            # region, since that is a claim about where a language was spoken.
            e["source_ids"] = ["glottolog-5-3"] if row.get("glottocode") else ["roster-tier-1"]
            # In this branch parent_id means linguistic ancestor, and descent is not containment:
            # a daughter language begins when its parent stops being spoken and carries on long
            # after. Burgundian outlives Proto-East-Germanic by construction, which is what
            # descent means. Twenty-eight rows tripped the containment rule for this reason, and
            # the rule is right about history and wrong about genealogy.
            e["allow_outside_parent_dates"] = True
            phrase = _SEARCH_PHRASES.get(row["name"])
            if phrase:
                e["search_phrase"] = phrase
            if row.get("aliases"):
                e["aliases"] = [a for a in dict.fromkeys(row["aliases"]) if a != row["name"]]
            if row.get("historicity"):
                e["historicity"] = row["historicity"]
            # A reconstruction is known by inference, which is a different claim from a contested
            # one: nobody doubts Proto-Indo-European and nobody has heard it either. The existing
            # test for this caught that the authored protos carried no historicity at all.
            if row["name"].startswith("Proto-") or row.get("classification") == "proto_language":
                e.setdefault("historicity", "reconstructed")
                e["start_dating_method"] = "glottochronology"
                if e.get("end_year") is not None:
                    e["end_dating_method"] = "glottochronology"
        else:
            # Filled in below, once every descendant is present.
            e["start_year"] = None
            e["end_year"] = None
        out.append(e)

    needs_review = _flag_fallback_dates(out)
    # Regrouping BEFORE the migration, because regrouping moves ids. Run the other way round,
    # the redirects were written against ids that then changed -- Dravidian turned out to be a
    # one-language family and moved, leaving global.languages.proto-dravidian pointing at nothing.
    _group_singletons(out)

    by_id = {e["id"]: e for e in out}

    # Fold the old branch in before the hull is computed, so a migrated entity's dates count.
    redirects = {}
    drop = migrate(entities, by_id, redirects)
    entities[:] = [e for e in entities if e["id"] not in drop]

    _fill_hulls(out, by_id)

    # Twenty-five family nodes end up with no descendants at all -- Glottolog clades whose only
    # members are languages the roster does not carry. A node a reader can drill into and find
    # nothing is worse than no node, so they go, repeatedly, since removing one can empty its
    # parent.
    for _ in range(20):
        parents = {e.get("parent_id") for e in out}
        dead = [e for e in out
                if e["kind"] == "region" and e["id"] != "languages" and e["id"] not in parents]
        if not dead:
            break
        gone = {e["id"] for e in dead}
        out[:] = [e for e in out if e["id"] not in gone]
    by_id.clear()
    by_id.update({e["id"]: e for e in out})

    clash = [e["id"] for e in out if e["id"] in existing]
    if clash:
        raise KeyError(f"author_languages: {len(clash)} id(s) already exist: {clash[:5]}")

    entities.extend(out)
    apply_cross_parents(E, entities, out)
    # Published as a theme, so the set is a worklist a reader (or the next dating pass) can open,
    # rather than a note buried on eighteen separate entities.
    globals()["NEEDS_DATING_REVIEW"] = sorted(e["id"] for e in out if id(e) in needs_review)

    fam = sum(1 for e in out if e.get("start_dating_method") is None)
    print(f"author_languages: added {len(out)} entities "
          f"({len(out) - fam} languages, {fam} family/container nodes), "
          f"migrated {len(drop)} from global.languages")
    return redirects


def _yr(y):
    return f"{abs(y)} {'BCE' if y < 0 else 'CE'}"


def _fill_hulls(out, by_id):
    """A clade begins with its earliest member and continues while any member survives."""
    kids = {}
    for e in out:
        kids.setdefault(e.get("parent_id"), []).append(e)

    def walk(node):
        starts, ends, living = [], [], False
        if node.get("start_year") is not None:
            starts.append(node["start_year"])
            if node.get("extant"):
                living = True
            elif node.get("end_year") is not None:
                ends.append(node["end_year"])
        for child in kids.get(node["id"], ()):
            s, en, lv = walk(child)
            starts += s
            ends += en
            living = living or lv
        if node.get("start_dating_method") is None and starts:
            node["start_year"] = min(starts)
            # A clade's start rests on whatever its earliest member rests on, which is a
            # reconstruction in almost every case.
            node["start_dating_method"] = "glottochronology"
            if living:
                node["end_year"] = None
                node["extant"] = True
            elif ends:
                node["end_year"] = max(ends)
                node["end_dating_method"] = "received"
        return starts, ends, living

    for e in out:
        if e.get("parent_id") is None:
            walk(e)
            # The root of a taxonomy has no date of its own. Taking the hull gave it 50,000 BCE,
            # from whichever reconstruction reaches furthest back, which is not a fact about
            # "Languages" and sorted the whole branch above the geographic regions.
            e["start_year"] = None
            e["end_year"] = None
            e.pop("start_dating_method", None)
            e.pop("end_dating_method", None)
            e.pop("extant", None)
    # Any node still undated has no dated descendant at all, so it becomes a pure container. A
    # region node is the highest-traffic kind in the app and must carry a summary, so say what the
    # node is rather than leaving a reader who lands on it with a bare name.
    for e in out:
        if e.get("start_dating_method") is None and e["kind"] == "language":
            e["kind"] = "region"
            e.setdefault(
                "summary",
                f"A subgroup within the {e['id'].split('.')[1].replace('-', ' ').title()} family. "
                "No language in this roster is placed directly here; it exists to keep the descent "
                "path intact.")


# A top-level family holding exactly one language adds no branching a reader can use, and there
# were 135 of them -- half the Languages column was Greater Kwerba, Pahoturi, Mailuan and their
# kind, each a real Glottolog family represented here by a single Tier 2 exemplar.
#
# They are NOT isolates and must not be filed as such. An isolate has no known relatives, which is
# a claim about the evidence; these have relatives that this roster simply does not carry, which is
# a claim about the roster. Conflating the two would assert something false about Abkhaz-Adyge.
SINGLETON_ID = "languages.one-language-families"
SINGLETON_NAME = "Families With One Language Here"


def _group_singletons(out):
    by_parent = {}
    for e in out:
        by_parent.setdefault(e.get("parent_id"), []).append(e)

    def languages_below(eid):
        n = 0
        for child in by_parent.get(eid, ()):
            if child["kind"] == "language":
                n += 1
            n += languages_below(child["id"])
        return n

    tops = [e for e in out if e.get("parent_id") == "languages"
            and e["id"] not in {"languages.isolates", "languages.disputed",
                                "languages.unclassified"}]
    movers = [e for e in tops if languages_below(e["id"]) <= 1
              and e["id"] != SINGLETON_ID]
    if not movers:
        return

    out.append({
        "id": SINGLETON_ID,
        "name": SINGLETON_NAME,
        "kind": "region",
        "parent_id": "languages",
        # Every node needs a tier; the demotion pass in apply_corrections reads it unguarded.
        "tier": "foundational",
        "summary": ("Families represented in this dataset by a single language. They are not "
                    "isolates: each has relatives, which this roster does not carry. Grouped so "
                    "the top of the tree shows the families that branch."),
    })
    moved = 0
    for e in movers:
        old = e["id"]
        e["parent_id"] = SINGLETON_ID
        e["id"] = f"{SINGLETON_ID}.{old.rsplit('.', 1)[-1]}"
        for other in out:
            if other.get("parent_id") == old:
                other["parent_id"] = e["id"]
                other["id"] = f"{e['id']}.{other['id'].rsplit('.', 1)[-1]}"
        moved += 1
    print(f"author_languages: grouped {moved} one-language famil(ies) under {SINGLETON_NAME!r}")


# Nineteen languages start at exactly 50,000 BCE and six at 40,000 BCE. Those are not dates for
# those languages: where no divergence estimate existed, the research fell back to when the region
# was first settled, which says when PEOPLE arrived and nothing about when a language began. The
# clustering on round numbers is the tell -- real estimates do not land 19 deep on one figure.
#
# The dates stay, at the user's instruction, but they say what they are, and the entities are
# collected into a theme so the set is a worklist rather than a footnote nobody reads.
_FALLBACK_FLOOR = -20000


def _flag_fallback_dates(out):
    flagged = set()
    for e in out:
        y = e.get("start_year")
        if y is None or y > _FALLBACK_FLOOR or e["kind"] != "language":
            continue
        note = ("Start is a regional settlement estimate, not a date for this language: no "
                "divergence estimate exists for it. Treat as a floor on time-depth, not a "
                "beginning.")
        prior = (e.get("date_note") or "").strip()
        if note not in prior:
            e["date_note"] = (prior + " " + note).strip()
        e.setdefault("historicity", "reconstructed")
        flagged.add(id(e))
    print(f"author_languages: flagged {len(flagged)} date(s) as regional fallback")
    return flagged
