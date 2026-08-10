"""Find places where the dataset implies an entity it does not contain.

Two structural holes were found by accident while doing other work, in unrelated
regions and months apart. The Song was split at 1127 with none of the states that
caused the split; Majapahit stood with no predecessor, so the largest empire in
Javanese history arrived from nowhere. Both are the same shape -- a consequence
present with its cause deleted -- and **no test could have caught either**,
because nothing in a schema can express "this entity implies a missing one".

So this is a report, not a validator. Every heuristic below has honest false
positives: plenty of polities really do appear without a local predecessor, and
plenty of branches really are discontinuous. The output is a list to read, in the
same spirit as the childless-entity report, and the build does not fail on it.

Run: ``python3 tools/report_gaps.py [--top N]``
"""

import argparse
import json
from collections import defaultdict

DATA = "src/data/entities.json"

# A sibling gap smaller than this is ordinary punctuation between periods. Two
# centuries is where "the next thing happened later" turns into "something is
# missing".
GAP_YEARS = 200

# How far back a foundational entity may look for a predecessor before its
# arrival counts as unexplained.
PREDECESSOR_WINDOW = 60


def load():
    with open(DATA, encoding="utf-8") as fh:
        return json.load(fh)["entities"]


def sibling_gaps(entities, by_id):
    """Consecutive siblings with a long unexplained stretch between them.

    Burma showed as 588 years between Pagan and nothing at all. Sorting by start
    year and differencing against the running maximum end handles the common case
    of overlapping siblings, which a naive pairwise diff gets wrong.
    """
    kids = defaultdict(list)
    for e in entities:
        if e.get("parent_id") and e.get("start_year") is not None:
            kids[e["parent_id"]].append(e)

    out = []
    for pid, group in kids.items():
        if len(group) < 2:
            continue
        group.sort(key=lambda x: x["start_year"])
        reach = None
        for e in group:
            if reach is not None and e["start_year"] - reach > GAP_YEARS:
                out.append((e["start_year"] - reach, pid, reach, e["start_year"], e["name"]))
            end = e.get("end_year")
            cand = end if end is not None else e["start_year"]
            reach = cand if reach is None else max(reach, cand)
    return sorted(out, reverse=True)


def unexplained_arrivals(entities, by_id):
    """Foundational entities that begin with nothing ending near them.

    This is the Majapahit test. A major polity whose branch contains nothing
    finishing around the time it starts is either a genuine new arrival or a
    missing predecessor, and the report cannot tell which -- but the list is
    short enough to read.
    """
    kids = defaultdict(list)
    for e in entities:
        if e.get("parent_id"):
            kids[e["parent_id"]].append(e)

    out = []
    for e in entities:
        if e.get("tier") != "foundational" or e.get("start_year") is None:
            continue
        pid = e.get("parent_id")
        if pid is None:
            continue
        start = e["start_year"]
        siblings = [s for s in kids[pid] if s["id"] != e["id"]]
        if not siblings:
            continue
        # Anything ending in the window, or already running when this began,
        # counts as explaining the arrival.
        explained = False
        for s in siblings:
            s_start, s_end = s.get("start_year"), s.get("end_year")
            if s_start is None:
                continue
            if s_end is not None and start - PREDECESSOR_WINDOW <= s_end <= start + 5:
                explained = True
                break
            if s_start < start and (s_end is None or s_end > start):
                explained = True
                break
        if not explained:
            earlier = [s.get("end_year") or s.get("start_year") for s in siblings
                       if s.get("start_year") is not None and s["start_year"] < start]
            if earlier:
                out.append((start - max(earlier), e["id"], e["name"], start, max(earlier)))
    return sorted(out, reverse=True)


def uncovered_spans(entities, by_id):
    """Parents whose children leave a long stretch of the parent's span empty.

    The Song split at 1127 would not show here -- its children do cover it -- but
    a period node whose own dates promise more than its children deliver is the
    other way the same problem appears.
    """
    kids = defaultdict(list)
    for e in entities:
        if e.get("parent_id"):
            kids[e["parent_id"]].append(e)

    out = []
    for pid, group in kids.items():
        p = by_id.get(pid)
        if p is None or p.get("start_year") is None or p.get("end_year") is None:
            continue
        dated = [k for k in group if k.get("start_year") is not None]
        if len(dated) < 2:
            continue
        covered = min(k["start_year"] for k in dated)
        head = covered - p["start_year"]
        if head > GAP_YEARS:
            out.append((head, pid, p["name"], p["start_year"], covered))
    return sorted(out, reverse=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=12)
    args = ap.parse_args()

    entities = load()
    by_id = {e["id"]: e for e in entities}

    print("Structural gap report — suggestions to read, not errors to fix.")
    print(f"{len(entities)} entities.\n")

    gaps = sibling_gaps(entities, by_id)
    print(f"── Long stretches between siblings (>{GAP_YEARS}y) — {len(gaps)} found")
    for span, pid, a, b, name in gaps[:args.top]:
        print(f"  {span:5}y  {pid:44} {a} → {b}  before {name[:28]}")

    arr = unexplained_arrivals(entities, by_id)
    print(f"\n── Foundational entities arriving with no predecessor — {len(arr)} found")
    for span, eid, name, start, prev in arr[:args.top]:
        print(f"  {span:5}y  {name[:30]:32} starts {start}, nothing since {prev}")
        print(f"          {eid}")

    unc = uncovered_spans(entities, by_id)
    print(f"\n── Parents whose children start long after they do — {len(unc)} found")
    for span, pid, name, pstart, cstart in unc[:args.top]:
        print(f"  {span:5}y  {name[:30]:32} {pstart} → first child {cstart}")
        print(f"          {pid}")


if __name__ == "__main__":
    main()
