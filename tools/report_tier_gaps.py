"""Gaps that exist only because the entity filling them is hidden at a lower tier.

Issue #13 was filed as a China problem: at foundational tier the Tang ends in 907 and
the Song begins in 960, and the Five Dynasties period that fills the gap is two tiers
down. Measuring the same shape everywhere shows it is **not a China problem**. It is
systemic, and China is where it happened to be noticed.

The check: for each parent, take the children visible at a given tier, sort them, and
look for a gap between consecutive siblings. If a LOWER-tier sibling spans that gap,
the gap is an artefact of tier assignment rather than missing research. The data is
there; the default view hides it.

Two populations are excluded, both because including them buries the real findings.

**Prehistoric branches.** A "gap" between Olduvai Gorge and Blombos Cave is not a
hole; archaeological sites are not a continuous sequence.

**Ruler sequences.** A gap between two reigns means some rulers are filed deeper, not
that history is missing. Under `east-asia.japan.edo` the visible children are
individual shoguns, and "promoting" Tokugawa Ietsuna to close a 29-year gap would be
absurd -- the tier system is working exactly as designed there. So a gap is skipped
when either side is a `reign`, and a `reign` is never offered as a filler.

Both exclusions are the same lesson twice over: raw counts across a mixed population
mislead. Reading all 988 overlapping spans as a representational failure was the first
instance; the unfiltered version of this check reports 149 candidates whose tail is
Byzantine emperors and Japanese era names.

    python3 tools/report_tier_gaps.py
    python3 tools/report_tier_gaps.py --all      # include prehistory
"""

from __future__ import annotations

import argparse
import json
import pathlib
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
RANK = {"foundational": 0, "intermediate": 1, "specialist": 2}
PREHISTORIC = ("prehistor", "paleolithic", "neolithic", "mesolithic")
MIN_HOLE = 40


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--all", action="store_true",
                    help="include prehistoric branches, where gaps are usually not holes")
    ap.add_argument("--min", type=int, default=MIN_HOLE, help="smallest gap to report")
    args = ap.parse_args()

    with open(ROOT / "src" / "data" / "entities.json", encoding="utf-8") as fh:
        entities = json.load(fh)["entities"]
    by = {e["id"]: e for e in entities}

    def lineage(e):
        out, cur = [], e
        while cur.get("parent_id"):
            cur = by[cur["parent_id"]]
            out.append(cur["id"])
        return out

    kids = defaultdict(list)
    for e in entities:
        if e.get("parent_id"):
            kids[e["parent_id"]].append(e)

    found = []
    for pid, children in kids.items():
        parent = by.get(pid)
        if parent is None:
            continue
        if not args.all:
            branch = [pid] + lineage(parent)
            if any(tag in node for node in branch for tag in PREHISTORIC):
                continue
        for tier in ("foundational", "intermediate"):
            visible = [c for c in children
                       if RANK[c["tier"]] <= RANK[tier]
                       and c.get("start_year") is not None
                       and c.get("end_year") is not None]
            if len(visible) < 2:
                continue
            visible.sort(key=lambda c: c["start_year"])
            for left, right in zip(visible, visible[1:]):
                hole = right["start_year"] - left["end_year"]
                if hole < args.min:
                    continue
                # A gap between two reigns is unlisted rulers, not missing history.
                if not args.all and "reign" in (left["kind"], right["kind"]):
                    continue
                fillers = [c for c in children
                           if RANK[c["tier"]] > RANK[tier]
                           and c.get("start_year") is not None
                           and c.get("end_year") is not None
                           and c["start_year"] < right["start_year"]
                           and c["end_year"] > left["end_year"]
                           and (args.all or c["kind"] != "reign")]
                if fillers:
                    found.append((hole, tier, pid, left, right, fillers))

    found.sort(key=lambda row: -row[0])
    scope = "all branches" if args.all else "historical sequences"
    print(f"{len(found)} tier-visibility gaps in {scope}\n")
    print("A reader at the stated tier sees a hole. The entity that fills it exists,")
    print("filed one or more tiers down.\n")
    for hole, tier, pid, left, right, fillers in found:
        print(f"  {hole:5}y  at {tier:12} under {pid}")
        print(f"          {left['name']} ({left['end_year']}) "
              f"-> {right['name']} ({right['start_year']})")
        for f in fillers[:4]:
            print(f"          hidden: {f['name']} [{f['tier']}] "
                  f"{f['start_year']}..{f['end_year']}")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
