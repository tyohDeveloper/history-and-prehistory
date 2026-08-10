import json, sys, importlib.util, os
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)

import build_britain_1 as p1
ENTRIES = p1.ENTRIES
E = p1.E

import build_britain_2 as p2
p2.add(ENTRIES, E)

try:
    import build_britain_3 as p3
    p3.add(ENTRIES, E)
except ImportError:
    pass

# validation
KEYS = ["suggested_id_slug","name","kind","start_year","end_year","extant","parent_hint",
        "start_dating_method","summary","aliases","confidence"]
seen = {}
problems = []
for i, o in enumerate(ENTRIES):
    if list(o.keys()) != KEYS:
        problems.append(("keys", o.get("name"), list(o.keys())))
    s = o["suggested_id_slug"]
    if s in seen:
        problems.append(("dup-slug", s))
    seen[s] = 1
    if len(o["summary"]) >= 300:
        problems.append(("long-summary", s, len(o["summary"])))
    if "\n" in o["summary"] or "\r" in o["summary"]:
        problems.append(("newline", s))
    if o["kind"] not in ("reign","polity","era","period","event"):
        problems.append(("kind", s, o["kind"]))
    if o["start_year"] is not None and o["start_year"] >= 1066 and o["start_dating_method"] != "calendar":
        problems.append(("dating", s, o["start_dating_method"]))
    if o["start_dating_method"] not in ("calendar","received","first-attestation"):
        problems.append(("dm-bad", s, o["start_dating_method"]))
    if o["extant"] and o["end_year"] is not None:
        problems.append(("extant-end", s))
    if (not o["extant"]) and o["end_year"] is None:
        problems.append(("null-end-not-extant", s))
    if o["end_year"] is not None and o["start_year"] is not None and o["end_year"] < o["start_year"]:
        problems.append(("order", s))
    if o["confidence"] not in ("high","medium","low"):
        problems.append(("conf", s))

from collections import Counter
print("count:", len(ENTRIES))
print("kinds:", Counter(o["kind"] for o in ENTRIES))
print("problems:", len(problems))
for p in problems[:40]:
    print("  ", p)

out = os.path.join(D, "britain.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(ENTRIES, f, indent=1, ensure_ascii=False)
print("wrote", out)
