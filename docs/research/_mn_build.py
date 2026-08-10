import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _mn_common
import _mn_europe_west, _mn_europe_east, _mn_russia, _mn_americas
import _mn_asia_east, _mn_asia_south_se, _mn_west_asia, _mn_africa
import _mn_oceania_global

ROWS = _mn_common.ROWS
KEYS = ["suggested_id_slug","name","kind","start_year","end_year","extant",
        "parent_hint","region_hint","start_dating_method","summary","aliases","confidence"]
KINDS = {"reign","polity","era","period","event"}
REGIONS = {"africa","americas","central-asia","east-asia","europe","global",
           "oceania","south-asia","southeast-asia","west-asia"}

seen, out, errs = {}, [], []
for r in ROWS:
    s = r["suggested_id_slug"]
    if s in seen:
        errs.append("dup slug: %s" % s); continue
    seen[s] = r
    if set(r.keys()) != set(KEYS): errs.append("keys %s: %s" % (s, sorted(set(r.keys())^set(KEYS))))
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", s): errs.append("slug format: %s" % s)
    if r["kind"] not in KINDS: errs.append("kind %s: %r" % (s, r["kind"]))
    if r["region_hint"] not in REGIONS: errs.append("region %s: %r" % (s, r["region_hint"]))
    if r["start_dating_method"] != "calendar": errs.append("dating %s" % s)
    if not isinstance(r["start_year"], int): errs.append("start_year %s" % s)
    if r["extant"]:
        if r["end_year"] is not None: errs.append("extant with end_year: %s" % s)
    else:
        if not isinstance(r["end_year"], int): errs.append("non-extant end_year %s: %r" % (s, r["end_year"]))
        elif r["end_year"] < r["start_year"]: errs.append("end<start: %s" % s)
    if "\n" in r["summary"] or "\r" in r["summary"]: errs.append("newline in summary: %s" % s)
    if len(r["summary"]) >= 300: errs.append("summary too long (%d): %s" % (len(r["summary"]), s))
    if not r["summary"] or not r["name"]: errs.append("empty field: %s" % s)
    if not isinstance(r["aliases"], list): errs.append("aliases %s" % s)
    if r["confidence"] not in {"high","medium","low"}: errs.append("confidence %s" % s)
    out.append({k: r[k] for k in KEYS})

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "modern-nations.json")
with open(path, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")

from collections import Counter
print("errors:", len(errs))
for e in errs[:40]: print("  ", e)
print("entries written:", len(out))
print("by region:", dict(sorted(Counter(r["region_hint"] for r in out).items())))
print("by kind:", dict(sorted(Counter(r["kind"] for r in out).items())))
print("extant:", sum(1 for r in out if r["extant"]))
