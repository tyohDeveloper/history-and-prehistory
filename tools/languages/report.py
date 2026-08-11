"""What needs a decision before the Languages branch can be authored."""
import json, os, collections
LANG = "docs/research/languages"
tree = json.load(open(f"{LANG}/tree.json"))
unplaced = json.load(open(f"{LANG}/unplaced.json"))
meta = json.load(open("docs/research/glottolog/meta.json"))

langs = [r for r in tree if not r.get("is_family_node") and r["id"].count(".") > 1]
fams = [r for r in tree if r.get("is_family_node")]
by_id = {r["id"]: r for r in tree}

L = []
w = L.append
w("# Languages branch — decisions needed\n")
w(f"Built from Tier 1 (521) + Tier 2 (636) = **1,157 languages**, no exclusions applied, "
  f"placed into **{len(fams)} family and subgroup nodes** taken from Glottolog 5.3.\n")
w(f"- Total nodes: **{len(tree)}**")
w(f"- Isolates: **{sum(1 for r in langs if r.get('isolate'))}**")
w(f"- Maximum depth: **{max(r['id'].count('.') for r in tree)}** levels below the root")
w(f"- Pass-through nodes already collapsed: **554**\n")

w("## 1. Depth — the main open question\n")
w("Glottolog subgroups some families far more finely than a reader browsing history needs. "
  "These are the deepest paths. Each intermediate node is a real scholarly clade, so collapsing "
  "them loses information — but reaching French through eleven nodes is not usable either.\n")
deep = sorted(langs, key=lambda r: -r["id"].count("."))[:12]
w("| Language | Depth | Path |")
w("|---|---|---|")
for r in deep:
    parts = r["id"].split(".")[1:-1]
    w(f"| {r['name']} | {r['id'].count('.')} | {' › '.join(parts)} |")
w("")
counts = collections.Counter()
for r in langs:
    top = r["id"].split(".")[1]
    if r["id"].count(".") >= 8:
        counts[top] += 1
w("Branches with languages at depth 8 or more:\n")
for top, n in counts.most_common(10):
    w(f"- **{by_id.get('languages.'+top, {}).get('name', top)}** — {n} languages")
w("")

w("## 2. The 91 proto-languages cannot be placed automatically\n")
w("A reconstruction has no Glottocode, so none of them has a Glottolog path. But **47 of the 91 "
  "correspond directly to a Glottolog family node** — Proto-Germanic is what Glottolog calls the "
  "Germanic family, Proto-Slavic is Slavic, and so on.\n")
w("The natural fix, which also gives every family node the dates it otherwise lacks: **merge each "
  "proto-language into its family node**, so the branch reads Indo-European → Germanic → and the "
  "Germanic node itself carries Proto-Germanic's date range and sources. Without this, family "
  "nodes are undated and invisible on any timeline, and the proto-languages sit in a flat heap.\n")
w("The 44 with no matching family node need placing by hand. Listed below.\n")
protos = [r for r in unplaced if r.get("classification") == "proto_language"]
fam_names = {r["name"].lower() for r in fams}
import re
def base(n): return re.sub(r"^(proto-|common )", "", n.lower())
nomatch = [p for p in protos if base(p["name"]) not in fam_names]
for p in nomatch[:50]:
    w(f"- **{p['name']}** — stated parent: {p.get('parent_name') or '(none)'}")
w("")

w("## 3. Other rows with no path\n")
other = [r for r in unplaced if r.get("classification") != "proto_language"]
w(f"{len(other)} rows have a Glottocode that did not resolve to a Glottolog classification. "
  "They are currently under **Unclassified**, which is wrong for most of them.\n")
for r in other:
    w(f"- **{r['name']}** ({r['classification']}, gc `{r.get('glottocode')}`) — "
      f"stated parent: {r.get('parent_name') or '(none)'}")
w("")

w("## 4. Recorded but not acted on\n")
w("All exclusion rules were dropped as instructed. The criteria are still evaluated per row so "
  "any of them can be reinstated as a filter over this data rather than by re-running research:\n")
w(f"- labelled creole: **8**")
w(f"- Glottolog calls it a dialect: **47**")
w(f"- peak speakers under 10,000: **342**")
w(f"- low documentation (no grammar written): **161**\n")
w("Worth recording why the dialect label is not a safe filter: read literally it removes Biblical "
  "Hebrew, Classical Arabic, Vedic Sanskrit, Mycenaean Greek, Medieval and Vulgar Latin, all three "
  "stages of Egyptian, plus Cantonese, Serbian, Croatian and Luxembourgish. Glottolog's *dialect* "
  "means sub-lect of a language-level node, which is where it files every historical stage — and "
  "those stages are the point of a timeline. Not one of the 47 was a regional variant.\n")

open(f"{LANG}/DECISIONS.md", "w").write("\n".join(L))
print(f"wrote {LANG}/DECISIONS.md ({len(L)} lines)")
