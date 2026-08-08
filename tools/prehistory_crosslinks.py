"""East Asian and Oceanian prehistory: navigation without re-parenting.

The problem
-----------
Seven regions carry a `<region>.prehistory` navigation era. East Asia and
Oceania do not, so a reader browsing prehistory by region silently misses Jomon
Japan, the Chinese Neolithic, Sahul, Madjedbebe and Lake Mungo. That is the same
class of content, reachable in seven regions and unreachable in two.

Why the obvious fix is wrong
----------------------------
Moving those entities under new `.prehistory` parents changes their ids and,
worse, breaks two placements that are deliberately right:

* **Jomon belongs to Japan.** It is Japan's own founding era, continuous with
  everything after it. Filing it under a prehistory bucket would sever a
  14,000-year sequence from the country whose sequence it is.
* **Aboriginal Australia is open-ended on purpose.** The dataset already
  decided that 1788 is a colonial boundary, not an end to living traditions.
  Filing an ongoing culture under "prehistory" would undo that decision and say
  something false about living people.

What this does instead
----------------------
Adds the two missing navigation eras and reaches the existing entities through
`cross_parent_ids`, the mechanism the schema already provides and the dataset
already uses fifteen times. Ids do not change, primary parents do not change,
`pathTo` follows `parent_id` only so breadcrumbs still read "Japan > Jomon", and
containment validation is unaffected because it checks the primary parent. The
entity appears in both columns and is stored once.

Aboriginal Australia itself is deliberately NOT cross-linked -- only its dated
Pleistocene sites are. An era with no end does not belong under prehistory, and
that is the whole point of the decision above.
"""

# Members are listed explicitly rather than matched by date, so adding a Jomon
# phase does not silently change what "East Asian prehistory" means.
EAST_ASIA_MEMBERS = [
    "east-asia.japan.jomon",
    "east-asia.china.neolithic",
]

OCEANIA_MEMBERS = [
    "oceania.australia.aboriginal.sahul",
    "oceania.australia.aboriginal.madjedbebe",
    "oceania.australia.aboriginal.lake-mungo",
    "oceania.melanesia.lapita",
]


def _span(entities_by_id, ids):
    """Derived span of the named members.

    A navigation era makes no dating claim of its own; it reports the extent of
    what it contains.

    A null end is read as UNDATED, not as ongoing. Madjedbebe has no end year
    because nobody has dated one, and propagating that null would have rendered
    Oceanian prehistory as "75.0 ka - present", which says the Pleistocene never
    ended. The dataset draws exactly this distinction elsewhere: Homo sapiens is
    extant and Homo luzonensis is merely undated, and conflating them would put
    a hominin known from foot bones among the living.
    """
    starts = [entities_by_id[i]["start_year"] for i in ids
              if entities_by_id[i].get("start_year") is not None]
    ends = [entities_by_id[i]["end_year"] for i in ids
            if entities_by_id[i].get("end_year") is not None]
    return (min(starts) if starts else None), (max(ends) if ends else None)


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}

    missing = [i for i in EAST_ASIA_MEMBERS + OCEANIA_MEMBERS if i not in by_id]
    if missing:
        raise SystemExit(f"prehistory_crosslinks: unknown member id(s) {missing}")

    ea_start, ea_end = _span(by_id, EAST_ASIA_MEMBERS)
    oc_start, oc_end = _span(by_id, OCEANIA_MEMBERS)

    E("east-asia.prehistory", "era", "East Asian Prehistory", "east-asia",
      start=ea_start, end=ea_end,
      tier="foundational",
      date_precision="approx",
      summary="Jomon Japan and the Chinese Neolithic, gathered here for browsing. Both "
              "also sit in their own national sequences, where they belong.",
      date_note="A navigation era. It makes no dating claim of its own: the span is the "
                "extent of the entries gathered under it, each of which carries its own "
                "dating and sources. Jomon's primary home stays under Japan, because it "
                "is Japan's founding era rather than a detachable prehistoric episode.")

    E("oceania.prehistory", "era", "Oceanian Prehistory", "oceania",
      start=oc_start, end=oc_end,
      tier="foundational",
      date_precision="approx",
      summary="The Pleistocene settlement of Sahul and the Lapita expansion into the "
              "Pacific, gathered here for browsing.",
      date_note="A navigation era making no dating claim of its own. Aboriginal Australia "
                "is deliberately NOT gathered here: it has no end date because the "
                "traditions are living, and filing an ongoing culture under 'prehistory' "
                "would say something false. Its dated Pleistocene sites appear instead.")

    for i in EAST_ASIA_MEMBERS:
        by_id[i].setdefault("cross_parent_ids", []).append("east-asia.prehistory")
    for i in OCEANIA_MEMBERS:
        by_id[i].setdefault("cross_parent_ids", []).append("oceania.prehistory")
