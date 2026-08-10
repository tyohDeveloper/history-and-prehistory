"""Build the before-and-after graph, and resolve link targets without guessing.

`links` was populated on 15 of 1,765 entities. The application's stated purpose includes
"important before and after links", so this was the largest remaining gap between what it
promises and what it holds.

Three things happen here.

**Resolution that refuses to guess.** An author may write a link target as an id or as any
name, alias, or name form. Ambiguity is a hard failure listing the candidates, never a silent
pick. This matters more in this dataset than in most: fifteen display names collide, so
"Shōwa" and "Emperor Taizong" and "Andes" each identify two different things, and a resolver
that quietly chose one would be wrong half the time and never say so.

**Succession derived from sibling chronology, but only where that is honest.** Consecutive
reigns within a dynasty are a succession -- that is what a dynasty is. Consecutive dynasties
within a polity likewise. The dataset already holds that ordering, so asking authors to
restate it by hand would be asking them to duplicate a fact the tree already knows.

What is *not* derived is the interesting part. Earlier in this project the Five Dynasties
were missing and no tooling noticed, because Liao "covered" 907-960 so there was no date gap
-- yet Tang was not succeeded by Liao. Coverage is not continuity. So derivation is confined
to containers where sequence genuinely means succession, gaps beyond a tolerance are left
alone rather than bridged, and every derived link says in its note that it came from sibling
order rather than from a source. A reader can then tell a researched claim from a structural
one, which they could not do if both looked the same.

**Inverses derived rather than authored.** An author states one direction; the reciprocal is
generated. Authoring both invites exactly the drift that left fourteen `cross_parent_ids`
disagreeing with the "also under" line they were supposed to produce.
"""

import collections

# Reciprocal link types. Authoring one direction and generating the other is the only way the
# two cannot disagree.
INVERSES = {
    "preceded_by": "succeeded_by",
    "succeeded_by": "preceded_by",
    "successor_state_of": "predecessor_state_of",
    "predecessor_state_of": "successor_state_of",
    "part_of": "contains",
    "contains": "part_of",
    "conquered_by": "conquered",
    "conquered": "conquered_by",
    "vassal_of": "suzerain_of",
    "suzerain_of": "vassal_of",
    "descended_from": "ancestor_of",
    "ancestor_of": "descended_from",
    "regent_for": None,          # not symmetric: the ward is not regent for the regent
    "ruled_by_dynasty": None,
    "capital_at": None,
    "split_from": None,
    "merged_into": None,
    "appears_under": None,
    "same_entity_as": "same_entity_as",
    "co_ruler_with": "co_ruler_with",
    "rival_claimant_to": "rival_claimant_to",
    "other": None,
}

# Kinds where being consecutive under the same parent means succeeding. A dynasty is by
# definition a sequence of reigns; a polity's dynasties follow one another.
# Kinds that can be chronologically sequenced within a container. Reigns and periods are
# treated the same way here on purpose, but the CLAIM differs and the notes say so: for reigns
# within a dynasty, sequence is succession, because that is what a dynasty is. For periods and
# eras, sequence is only sequence -- this came before that, in this place.
#
# That distinction is the whole reason `preceded_by`/`succeeded_by` is the right link type and
# `successor_state_of` is not. The Five Dynasties were once missing from this dataset and no
# tooling noticed, because Liao "covered" 907-960 so no date gap existed -- but Tang was not
# succeeded BY Liao as a state. A generic before-and-after link makes the weaker, true claim.
SUCCESSION_KINDS = {"reign", "person", "period", "era", "city"}
SUCCESSION_CONTAINER_KINDS = {"period", "era", "polity", "region", "city"}
POLITICAL_KINDS = {"reign", "person"}

# How large a gap between one end and the next start may be and still read as succession.
# Interregna, disputed years and rounded dates are all real; a century is not a handover.
MAX_GAP_YEARS = 25
# Reigns overlap through co-rule and regency, which is a relationship rather than a break.
MAX_OVERLAP_YEARS = 15


def build_resolver(entities):
    """Return a function from a written target to an id, raising on ambiguity."""
    by_id = {e["id"] for e in entities}
    index = collections.defaultdict(set)
    for e in entities:
        keys = [e["name"]]
        keys += e.get("aliases") or []
        keys += [f["name"] for f in (e.get("name_forms") or [])]
        if e.get("native_name"):
            keys.append(e["native_name"])
        for k in keys:
            index[k.strip().casefold()].add(e["id"])

    def resolve(target, where):
        if target in by_id:
            return target
        hits = index.get(target.strip().casefold(), set())
        if len(hits) == 1:
            return next(iter(hits))
        if not hits:
            raise KeyError(f"{where}: link target {target!r} matches no entity")
        raise KeyError(
            f"{where}: link target {target!r} is ambiguous between "
            f"{sorted(hits)} -- write the id instead"
        )

    return resolve


def _abuts(earlier, later):
    """Does `later` start close enough to where `earlier` ends to read as succession?

    Tolerance scales with the length of what is being compared, because a fixed number of years
    means completely different things at different depths. Two thousand years between the
    Lomekwian and the Oldowan -- each running for the better part of a million years -- is
    abutment; two thousand years between two reigns is not a handover. A first version used a
    flat fifteen-year overlap allowance and rejected the deep-time pairs outright.
    """
    end = earlier.get("end_year")
    start = later.get("start_year")
    if end is None or start is None:
        return False

    spans = [abs((e.get("end_year") or e["start_year"]) - e["start_year"])
             for e in (earlier, later) if e.get("start_year") is not None]
    scale = max(spans) if spans else 0
    gap_allowed = max(MAX_GAP_YEARS, int(scale * 0.01))
    overlap_allowed = max(MAX_OVERLAP_YEARS, int(scale * 0.01))

    gap = start - end
    return gap <= gap_allowed if gap >= 0 else -gap <= overlap_allowed


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}
    resolve = build_resolver(entities)

    # ---- resolve any author-written names to ids -----------------------------
    resolved = 0
    for e in entities:
        for link in e.get("links") or []:
            target = link.get("entity_id")
            if target is None or target in by_id:
                continue
            link["entity_id"] = resolve(target, f"entity {e['id']}")
            resolved += 1
    if resolved:
        print(f"derive_links: resolved {resolved} name-written target(s) to ids")

    # ---- derive succession from sibling chronology ---------------------------
    kids = collections.defaultdict(list)
    for e in entities:
        if e.get("parent_id"):
            kids[e["parent_id"]].append(e)

    derived = 0
    skipped_gap = 0
    for parent_id, group in kids.items():
        parent = by_id.get(parent_id)
        if parent is None or parent["kind"] not in SUCCESSION_CONTAINER_KINDS:
            continue
        run = [e for e in group
               if e["kind"] in SUCCESSION_KINDS and e.get("start_year") is not None]
        if len(run) < 2:
            continue
        run.sort(key=lambda e: (e["start_year"], e.get("end_year") or e["start_year"]))
        for earlier, later in zip(run, run[1:]):
            if not _abuts(earlier, later):
                skipped_gap += 1
                continue
            existing = {(l.get("type"), l.get("entity_id")) for l in (earlier.get("links") or [])}
            if ("succeeded_by", later["id"]) in existing:
                continue
            # A flag rather than a note. The first version wrote a 200-character disclaimer
            # onto every derived link, which repeated the same sentence some eight hundred
            # times and pushed the gzipped bundle 36 kB over its ceiling. The size guard
            # caught it, and it was a presentation problem as much as a size one: boilerplate
            # repeated on every row is boilerplate the reader stops seeing. The UI now
            # explains derivation once, and `derived` marks which rows it applies to.
            earlier.setdefault("links", []).append({
                "type": "succeeded_by",
                "entity_id": later["id"],
                "derived": "sequence" if earlier["kind"] in POLITICAL_KINDS else "chronology",
            })
            derived += 1

    print(f"derive_links: derived {derived} succession link(s); "
          f"left {skipped_gap} sibling pair(s) unlinked because the gap or overlap "
          f"exceeded tolerance")

    # ---- derive inverses ----------------------------------------------------
    added = 0
    for e in list(entities):
        for link in list(e.get("links") or []):
            inverse = INVERSES.get(link.get("type"))
            if inverse is None:
                continue
            target = by_id.get(link.get("entity_id"))
            if target is None or target["id"] == e["id"]:
                continue
            have = {(l.get("type"), l.get("entity_id")) for l in (target.get("links") or [])}
            if (inverse, e["id"]) in have:
                continue
            target.setdefault("links", []).append({
                "type": inverse,
                "entity_id": e["id"],
                "derived": "reciprocal",
            })
            added += 1

    print(f"derive_links: generated {added} reciprocal link(s)")

    with_links = sum(1 for e in entities if e.get("links"))
    print(f"derive_links: {with_links} of {len(entities)} entities now carry at least one link")
