#!/usr/bin/env python3
"""Where the dataset is thin, measured rather than guessed.

Why this exists
---------------
Coverage work was being aimed by intuition, and intuition was wrong. The
assumption was that the millennia approaching 1000 BCE needed filling; the
measurement says that window is the DENSEST pre-CE band, and the starved one is
10,000-3,000 BCE. A coverage question that can be answered in two seconds should
not be answered by guessing.

It also settles the sequencing worry that prompted it. Filling the dataset in
chronological slices is safe only if the slices partition on a POINT-valued
attribute. Entities have exactly one start year but a date RANGE, so slicing on
"ends before X" silently drops every long-lived entity that straddles the line
-- and duration correlates with significance, so that is a bias against exactly
the entities most worth having. This report counts by START year for that
reason, and `--spanning` prints the straddlers a naive cut would have lost.

The matrix alone is not enough, which took a missed gap to learn. A childless
era spanning two thousand years counts as ONE entity in ONE band, exactly like a
node that is properly subdivided -- so the Indus Valley Civilisation sat in the
dataset as a single undifferentiated block, 3300-1300 BCE with no children at
all, while the South Asia row looked merely thin rather than structurally empty.
The childless report had been present the whole time behind a flag nobody
passed. It now runs by default, because a report that must be asked for is a
report that gets missed.

It also has to know what is NOT a container. Two kinds of node have no children
because they should not: a synthesis era describing a process, and a navigation
era cross-linking entities that live elsewhere. Both were reported as gaps until
they were excluded, and the second one sent a whole research pass after East
Asian prehistory that was already in the dataset under Japan and China.

Reigns are reported separately throughout. A dynasty with forty kings is forty
entities and close to zero additional coverage of a period, so mixing them in
makes a well-covered century look like a well-covered world.

Usage
-----
    python3 tools/coverage.py                # matrix + structural gaps
    python3 tools/coverage.py --spanning     # entities straddling each boundary
    python3 tools/coverage.py --all
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "src" / "data"

# Boundaries chosen to match how the literature is organised, not round numbers:
# the deep Palaeolithic, the terminal Pleistocene, then millennium bands through
# the Holocene where the density actually changes.
BANDS = [
    ("pre-10k", None, -10000),
    ("10k-6k", -10000, -6000),
    ("6k-4k", -6000, -4000),
    ("4k-3k", -4000, -3000),
    ("3k-2k", -3000, -2000),
    ("2k-1k", -2000, -1000),
    ("1k-1BCE", -1000, 0),
    ("CE", 0, None),
]


def band_of(year: int) -> str:
    for name, lo, hi in BANDS:
        if (lo is None or year >= lo) and (hi is None or year < hi):
            return name
    return "CE"


def load():
    return json.loads((DATA / "entities.json").read_text())["entities"]


def region_of(entity) -> str:
    return entity["id"].split(".")[0]


def matrix(entities, include_reigns: bool):
    rows = defaultdict(Counter)
    for e in entities:
        if e.get("start_year") is None:
            continue
        if not include_reigns and e["kind"] == "reign":
            continue
        rows[region_of(e)][band_of(e["start_year"])] += 1
    return rows


def print_matrix(rows, title):
    names = [b[0] for b in BANDS]
    print(f"\n{title}")
    print("-" * (18 + 9 * len(names) + 7))
    print(f"{'region':<18}" + "".join(f"{n:>9}" for n in names) + f"{'total':>7}")
    totals = Counter()
    for region in sorted(rows, key=lambda r: -sum(rows[r].values())):
        counts = rows[region]
        total = sum(counts.values())
        cells = ""
        for n in names:
            v = counts.get(n, 0)
            totals[n] += v
            # A zero is the point of the report, so make it findable.
            cells += f"{'.' if v == 0 else v:>9}"
        print(f"  {region:<16}" + cells + f"{total:>7}")
    print("-" * (18 + 9 * len(names) + 7))
    print(f"{'TOTAL':<18}" + "".join(f"{totals.get(n, 0):>9}" for n in names)
          + f"{sum(totals.values()):>7}")


def print_spanning(entities):
    """Entities a naive 'ends before X' cut would have dropped."""
    print("\nEntities straddling each band boundary")
    print("-" * 72)
    print("These are why coverage passes must partition on START year. Slicing on")
    print("'ends before the boundary' would silently drop every one of them.\n")
    for name, lo, hi in BANDS:
        if hi is None:
            continue
        straddlers = [
            e for e in entities
            if e.get("start_year") is not None
            and e.get("end_year") is not None
            and e["start_year"] < hi < e["end_year"]
        ]
        if not straddlers:
            continue
        print(f"  {hi:>7} : {len(straddlers):>3} entities cross this line")
        for e in sorted(straddlers, key=lambda x: x["start_year"])[:4]:
            print(f"            {e['start_year']:>8}..{e['end_year']:<7} {e['id']}")
        if len(straddlers) > 4:
            print(f"            ... and {len(straddlers) - 4} more")


def print_childless(entities):
    """Structural nodes promising detail they do not have.

    Split by kind on purpose. A childless `era` is a real gap: an era exists to
    contain things. A childless `period` usually is not -- a cave site or a
    single industry has nothing to sub-divide, and ranking those by span just
    floats the deep Palaeolithic to the top where it is least actionable.
    """
    kids = Counter(e.get("parent_id") for e in entities)

    def span(e):
        end = e.get("end_year")
        return (end - e["start_year"]) if end is not None else 0

    # A synthesis era describes a process rather than containing a sequence --
    # "The Anatolian Farmer Turnover" has nothing to subdivide and reporting it
    # as a gap sends the next pass after work that should not be done. They are
    # recognised by having no children AND carrying caveats, which is what a
    # concept node exists to hold.
    def is_synthesis(e):
        return bool(e.get("caveats")) and e["kind"] == "era"

    # A navigation era is a cross-link, not a container. `east-asia.prehistory`
    # spans 14,000-300 BCE and holds nothing, and this report called it the
    # single biggest gap in the dataset -- while Jomon sat fully subdivided
    # under Japan and the Chinese Neolithic under China, exactly where the
    # node's own summary says they belong. Chasing that "gap" would have
    # duplicated 1,500 years of existing coverage. They are recognised by
    # saying so in `date_note`, which `prehistory_crosslinks.py` writes.
    def is_navigation(e):
        return "navigation era" in (e.get("date_note") or "").lower()

    empty = [
        e for e in entities
        if e["kind"] in ("era", "period")
        and kids.get(e["id"], 0) == 0
        and e.get("start_year") is not None
        and not is_synthesis(e)
        and not is_navigation(e)
    ]
    eras = [e for e in empty if e["kind"] == "era"]

    # An empty REGION outranks anything else and was invisible here until
    # `west-asia.anatolia` turned up holding nothing at all -- no Hittites, no
    # Troy, no Lydia -- while the report happily listed 1,200-year eras. The
    # filter only looked at era/period, so the single worst kind of gap in the
    # dataset could not appear in the report designed to find gaps.
    empty_regions = [
        e for e in entities
        if e["kind"] == "region" and kids.get(e["id"], 0) == 0
    ]
    print("\nEMPTY REGIONS -- a region with nothing in it")
    print("-" * 72)
    for e in sorted(empty_regions, key=lambda x: x["id"]):
        print(f"  {e['id']}")
    if not empty_regions:
        print("  (none)")

    print("\nChildless ERAS -- an era exists to contain things")
    print("-" * 72)
    for e in sorted(eras, key=span, reverse=True)[:15]:
        print(f"  {span(e):>9,} yr  {e['start_year']:>8}..{str(e.get('end_year')):<7} {e['id']}")
    if not eras:
        print("  (none)")

    # Holocene periods only: pre-Holocene childlessness is usually correct.
    holo = [e for e in empty if e["kind"] == "period" and e["start_year"] > -10000]
    print("\nChildless Holocene PERIODS, widest first")
    print("-" * 72)
    for e in sorted(holo, key=span, reverse=True)[:10]:
        print(f"  {span(e):>9,} yr  {e['start_year']:>8}..{str(e.get('end_year')):<7} {e['id']}")

    print(f"\n  {len(empty_regions)} empty regions, {len(eras)} childless eras, "
          f"{len(empty)} childless era/period nodes overall.")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--spanning", action="store_true")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()

    entities = load()
    print(f"{len(entities):,} entities")

    print_matrix(matrix(entities, include_reigns=False),
                 "Coverage by START year, EXCLUDING reigns (period/culture depth)")
    print_matrix(matrix(entities, include_reigns=True),
                 "Same, INCLUDING reigns (shows where ruler lists inflate the picture)")

    # Not behind a flag. The matrix cannot see a childless block, and this is
    # the report that actually names the next thing to work on.
    print_childless(entities)

    if args.spanning or args.all:
        print_spanning(entities)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
