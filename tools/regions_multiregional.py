"""Global & Multi-Regional, and a derived list of the regions an empire actually touched.

Two changes, one of which is smaller than it looks because the app was already
doing it.

**The tree has been a graph for a long time.** `tree.ts` places an entity under
its `parent_id` and under every id in `cross_parent_ids`, and thirty entities
use it. Ptolemaic Egypt already appears under both Egypt and the Hellenistic
world; Yuan China under both China and the Mongol empire; Kushite Egypt under
both Egypt and Kush. So "can the same node show in more than one region" is not
a proposal -- it is existing behaviour that has been working quietly and
inconsistently, applied wherever an author happened to think of it.

What was missing is that nothing said so, and nothing said which regions an
entity spans. This adds a **derived** `regions` list: the set of top-level
geographies an entity is reachable from, computed from `parent_id` and
`cross_parent_ids` rather than hand-authored, so it cannot drift from the tree
the way two authored fields would.

**What it means, precisely, because the obvious reading is wrong.** `regions`
records where an entity is *placed*, not where a polity *ruled*. Those differ.
The Hellenistic world comes out spanning four regions, which is right. The
Mongol empire comes out spanning two, which understates it -- the Ilkhanate and
the Golden Horde are ordinary children of it, so their own cross-links to West
Asia and Europe do not propagate upward, and propagating through every
descendant would make Europe "span" Africa because Ptolemaic Egypt cross-links
into the Hellenistic world.

That gap is not a bug to patch with a wider traversal. It is the difference
between a placement graph and a territorial claim, and only the first is
something the tree knows. A real answer to "which regions did this empire hold"
would have to be authored per entity, with sources, like every other claim
here.

**Global becomes Global & Multi-Regional.** Its old summary read "Cross-regional
and worldwide frames", which conflated the two things the last release spent a
whole pass separating. The new name says what the region actually is: the place
for everything that is not one region, whether because it is everywhere (an
ice age, a pandemic) or because it is several places at once (an empire).

Cross-Regional Empires stays a separate top-level entry rather than being folded
in, for the reason the user gave when this first came up: the world wars do not
belong next to the Abbasid Caliphate. Multi-regional and worldwide are different
claims and merging them loses that. The renamed Global says what it holds; the
neighbouring category says what it holds; and an entity now carries the list of
regions it spans regardless of which one it is filed under.
"""


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}

    g = by_id.get("global")
    if g is not None:
        g["name"] = "Global & Multi-Regional"
        g["summary"] = (
            "Everything that is not one region: worldwide frames and events, and the spans "
            "that cross regional boundaries."
        )
        g["date_note"] = (
            "Renamed from 'Global'. The old summary read 'cross-regional and worldwide "
            "frames', which ran together two different claims -- being everywhere, and being "
            "in several places at once. Empires that span regions are filed in the region "
            "they came from and cross-linked to the others; each entity's `regions` list "
            "records every region it touches."
        )
        g["name_forms"] = [
            {"name": "Global", "kind": "historical",
             "note": "The earlier name, which invited world events and multi-region empires "
                     "into the same bucket."},
        ]

    # ---------------------------------------------------- derive `regions`

    # `global` and `cross-regional` are top-level nodes but they are not
    # geographies, and listing Kublai Khan as spanning "central-asia,
    # cross-regional, east-asia" says one true thing and one category error.
    NOT_GEOGRAPHY = {"global", "cross-regional"}
    roots = {e["id"] for e in entities if e.get("parent_id") is None}
    geographies = roots - NOT_GEOGRAPHY

    # Parent edges, following cross_parent_ids as well as parent_id: the tree is
    # already a graph, so resolving a region means walking every edge.
    parents: dict[str, list[str]] = {}
    for e in entities:
        edges = []
        if e.get("parent_id"):
            edges.append(e["parent_id"])
        edges.extend(e.get("cross_parent_ids", []))
        parents[e["id"]] = edges

    def regions_of(eid: str, seen: frozenset = frozenset()) -> set:
        if eid in roots:
            return {eid}
        if eid in seen:  # defensive: a cycle would otherwise hang the build
            return set()
        out: set = set()
        for p in parents.get(eid, []):
            if p in by_id or p in roots:
                out |= regions_of(p, seen | {eid})
        return out

    # Cross-links point inward as often as outward. Yuan China declares itself
    # part of the Mongol empire, not the reverse, so walking only upward left
    # the Mongol empire looking purely Central Asian while its own khanates
    # spanned four regions. An entity that something cross-links INTO holds
    # that thing's regions too.
    inbound: dict[str, list[str]] = {}
    for e in entities:
        for cp in e.get("cross_parent_ids", []):
            inbound.setdefault(cp, []).append(e["id"])

    def spans(eid: str) -> set:
        out = regions_of(eid) & geographies
        for child in inbound.get(eid, []):
            out |= regions_of(child) & geographies
        return out

    multi = 0
    for e in entities:
        regs = sorted(spans(e["id"]))
        if not regs:
            continue
        # Only worth recording where it says something the parent does not: a
        # single region is already implied by the breadcrumb.
        if len(regs) > 1:
            e["regions"] = regs
            multi += 1

    print(f"Regions: {multi} entities span more than one region")
