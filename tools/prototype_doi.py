#!/usr/bin/env python3
"""Prototype the degree-of-interest function against the real dataset.

Not shipped. The point is to find out whether the proposed DOI actually
selects a sensible neighbourhood before any of it is written in TypeScript,
because the two design claims it rests on are both testable:

1. Temporal distance must be density-normalized. Local median gap between
   entity midpoints runs from ~75,000 years in deep time to ~1 year in the
   modern era, a factor of 75,000. Any absolute-years radius is wrong by four
   orders of magnitude at one end.

2. `tier` is NOT global a priori importance, though DESIGN.md claimed it was.
   It is authored per branch: East Asia is 70% specialist, Central Asia 0%.
   Used raw it would dim East Asia for authoring reasons rather than
   importance reasons. Ranked within its sibling set it means the same thing
   everywhere.

Run: python3 tools/prototype_doi.py
"""

from __future__ import annotations

import bisect
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TIER_RANK = {"foundational": 2.0, "intermediate": 1.0, "specialist": 0.0}


def load():
    entities = json.loads((ROOT / "src/data/entities.json").read_text())["entities"]
    return entities, {e["id"]: e for e in entities}


def midpoint(e):
    start = e.get("start_year")
    if start is None:
        return None
    end = e.get("end_year")
    return (start + (end if end is not None else 2026)) / 2.0


def interval(e):
    """(start, end) in historical years, or None for an undated node."""
    start = e.get("start_year")
    if start is None:
        return None
    end = e.get("end_year")
    return (start, end if end is not None else 2026)


def interval_gap(a, b):
    """Years between two intervals; 0 when they overlap.

    Midpoint distance was the first attempt and it is wrong. A neng\u014d sits
    wholly inside the Heian period, so the two overlap completely, yet their
    midpoints can be nearly two centuries apart. Under midpoint distance a
    node was penalised for being contemporaneous with its own parent.
    """
    if a is None or b is None:
        return None
    if a[0] <= b[1] and b[0] <= a[1]:
        return 0.0
    return float(b[0] - a[1] if b[0] > a[1] else a[0] - b[1])


def depth_of(e, by_id):
    d, parent = 0, e.get("parent_id")
    while parent and parent in by_id:
        d += 1
        parent = by_id[parent].get("parent_id")
    return d


def ancestry(e, by_id):
    chain, parent = [e["id"]], e.get("parent_id")
    while parent and parent in by_id:
        chain.append(parent)
        parent = by_id[parent].get("parent_id")
    return chain


def tree_distance(a, b, by_id):
    """Hops between two nodes through their lowest common ancestor."""
    up_a = ancestry(a, by_id)
    up_b = ancestry(b, by_id)
    index_b = {nid: i for i, nid in enumerate(up_b)}
    for i, nid in enumerate(up_a):
        if nid in index_b:
            return i + index_b[nid]
    return len(up_a) + len(up_b)


def local_gap_scale(sorted_mids, year, window=25):
    """Median gap between entity midpoints near `year`.

    This is the density normalizer. Dividing a raw year-distance by it turns
    "500 years away" into "about n neighbours away", which means the same
    thing over the Pleistocene and over the Cold War.
    """
    i = bisect.bisect_left(sorted_mids, year)
    lo, hi = max(0, i - window), min(len(sorted_mids), i + window)
    slice_ = sorted_mids[lo:hi]
    if len(slice_) < 3:
        return 1000.0
    gaps = [b - a for a, b in zip(slice_, slice_[1:]) if b > a]
    return max(statistics.median(gaps), 0.5) if gaps else 1000.0


def sibling_tier_score(e, siblings):
    """Tier ranked WITHIN its sibling set, in [0, 1].

    Returns 0.5 when every sibling shares a tier: the field carries no local
    information there, so it should not tilt the result either way. The Heian
    period is the case that forces this - 88 children, all `specialist`.
    """
    tiers = {s["tier"] for s in siblings}
    if len(tiers) <= 1:
        return 0.5
    values = sorted(TIER_RANK[t] for t in tiers)
    return values.index(TIER_RANK[e["tier"]]) / (len(values) - 1)


def build_doi(entities, by_id):
    kids = defaultdict(list)
    for e in entities:
        kids[e.get("parent_id")].append(e)
    mids = {e["id"]: midpoint(e) for e in entities}
    sorted_mids = sorted(m for m in mids.values() if m is not None)
    depths = {e["id"]: depth_of(e, by_id) for e in entities}

    intervals = {e["id"]: interval(e) for e in entities}

    def doi(focus, x, w_time=1.0, w_tree=1.0, w_span=0.6, lam=2.5):
        # API is the sibling-normalized tier ALONE. The first version added
        # Furnas's canonical -depth term and the result ranked the trunk:
        # "East Asia", "Global", "Europe" outscored every actual neighbour,
        # because shallow nodes win on depth and undated nodes dodged the
        # temporal penalty. Two reasons -depth is wrong here specifically:
        # the trunk is 11 region nodes already permanently visible in the
        # Miller columns, so it carries no information the lens can add; and
        # depth already correlates hard with tier (depth 0 is 0% specialist,
        # depth 5 is 59%), so using both double-counts the same signal.
        api = lam * sibling_tier_score(x, kids[x.get("parent_id")])

        gap = interval_gap(intervals[focus["id"]], intervals[x["id"]])
        if gap is None:
            return float("-inf")  # undated container: scaffolding, not content
        fm = mids[focus["id"]]
        scale = local_gap_scale(sorted_mids, fm)
        d_time = math.log1p(gap / scale)

        # Span-mismatch penalty. Overlap alone is too generous: "CE (Common
        # Era)" and "Middle Ages" trivially overlap a seven-year neng\u014d and
        # were ranking as temporal neighbours. An entity three hundred times
        # longer than the focus is containing it, not keeping it company.
        f_span = max(intervals[focus["id"]][1] - intervals[focus["id"]][0], 1)
        x_span = max(intervals[x["id"]][1] - intervals[x["id"]][0], 1)
        d_span = abs(math.log10(x_span / f_span))

        d_tree = tree_distance(focus, x, by_id)
        # Sparse neighbourhoods make temporal distance uninformative, so
        # structure should carry more weight there, and less where entities
        # are packed a year apart.
        density = 1.0 / (1.0 + math.log1p(local_gap_scale(sorted_mids, fm)))
        return api - (
            w_time * density * d_time
            + w_tree * (1 - density) * d_tree
            + w_span * d_span
        )

    return doi


def report(focus_id, entities, by_id, doi, n=12):
    focus = by_id[focus_id]
    scored = sorted(entities, key=lambda x: -doi(focus, x))
    fm = midpoint(focus)
    print(f"\n{'=' * 74}")
    print(f"FOCUS: {focus['name']}  ({focus_id})")
    print(f"       midpoint {fm:,.0f}   tier {focus['tier']}   depth {depth_of(focus, by_id)}")
    print(f"{'=' * 74}")
    for x in scored[:n]:
        xm = midpoint(x)
        g = interval_gap(interval(focus), interval(x))
        gap = "overlaps" if g == 0 else (f"{g:,.0f} yr" if g is not None else "n/a")
        print(
            f"  {doi(focus, x):7.2f}  {x['name'][:34]:36} {x['tier'][:5]:6}"
            f" hops={tree_distance(focus, x, by_id):2}  {gap:>14}"
        )


def main():
    entities, by_id = load()
    doi = build_doi(entities, by_id)
    for fid in [
        "east-asia.japan.heian",       # 88 identically-tiered children
        "global.prehistory.hominins.homo-erectus",  # deep time, very sparse
        "europe.mediterranean.byzantine",
        "west-asia.prehistory.natufian",
    ]:
        if fid in by_id:
            report(fid, entities, by_id, doi)
        else:
            print(f"\n!! missing {fid}")


if __name__ == "__main__":
    main()
