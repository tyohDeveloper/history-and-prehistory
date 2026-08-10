"""Export the dataset as a compact inventory for an outside audit.

Written because gap-finding by web search does not work. A search engine can confirm a
fact you already suspect; it cannot tell you what you failed to think of. A model that
knows world history can read a list of 1,765 entities and say "there is no Sogdiana here",
which is the actual question.

The output is deliberately terse — one line per entity — so a whole worldview fits in a
single context window without summarising away the holes.
"""

import json
from collections import Counter, defaultdict

SRC = "src/data/entities.json"
OUT = "docs/inventory.txt"


def main():
    entities = json.load(open(SRC))["entities"]
    by_id = {e["id"]: e for e in entities}
    kids = defaultdict(list)
    for e in entities:
        kids[e.get("parent_id")].append(e)

    def yr(v):
        if v is None:
            return "—"
        return f"{abs(v)}BC" if v < 0 else f"{v}"

    lines = []
    lines.append(f"# {len(entities)} entities. Format: indent = tree depth.")
    lines.append("# name [kind] start..end (tier)")
    lines.append("")

    def walk(parent, depth):
        for e in sorted(kids[parent], key=lambda x: (x.get("start_year") is None,
                                                     x.get("start_year") or 0, x["name"])):
            lines.append(f"{'  ' * depth}{e['name']} [{e['kind']}] "
                         f"{yr(e.get('start_year'))}..{yr(e.get('end_year'))} ({e['tier'][:4]})")
            walk(e["id"], depth + 1)

    walk(None, 0)

    # Distribution by century, so thin stretches are visible without counting by hand.
    buckets = Counter()
    for e in entities:
        s = e.get("start_year")
        if s is None:
            continue
        if s < -10000:
            buckets["before 10000 BCE"] += 1
        else:
            century = (s // 100) * 100
            buckets[century] += 1

    lines.append("")
    lines.append("# ── entity count by start century ──")
    lines.append(f"before 10000 BCE: {buckets.pop('before 10000 BCE', 0)}")
    for c in sorted(k for k in buckets if isinstance(k, int)):
        label = f"{abs(c)} BCE" if c < 0 else f"{c} CE"
        lines.append(f"{label}: {buckets[c]}")

    lines.append("")
    lines.append("# ── kinds ──")
    for k, n in Counter(e["kind"] for e in entities).most_common():
        lines.append(f"{k}: {n}")

    lines.append("")
    lines.append("# ── top-level regions and their sizes ──")
    for r in sorted(kids[None], key=lambda x: x["name"]):
        n = sum(1 for e in entities if e["id"].startswith(r["id"] + "."))
        lines.append(f"{r['name']}: {n}")

    open(OUT, "w").write("\n".join(lines) + "\n")
    print(f"wrote {OUT}: {len(lines)} lines, {len(entities)} entities")


if __name__ == "__main__":
    main()
