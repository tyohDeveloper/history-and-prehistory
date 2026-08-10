#!/usr/bin/env python3
"""Merge modern research files into one authoring file.

Inputs (relative to repo root):
  docs/research/usa.json
  docs/research/britain.json
  docs/research/modern-nations.json
  src/data/entities.json        (existing app data, for dedupe + parent resolution)

Outputs:
  docs/research/modern-merged.json
  docs/research/modern-merged-report.md

Re-runnable: python3 docs/research/merge_modern.py
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RESEARCH = ROOT / "docs" / "research"
ENTITIES = ROOT / "src" / "data" / "entities.json"
OUT_JSON = RESEARCH / "modern-merged.json"
OUT_REPORT = RESEARCH / "modern-merged-report.md"

SOURCES = [
    ("usa.json", "americas", "americas.north.usa"),
    ("britain.json", "europe", "europe.western"),
    ("modern-nations.json", None, None),  # region + fallback come from region_hint
]

VALID_KINDS = {
    "region", "era", "polity", "culture", "period", "reign", "event", "city",
    "site", "taxon", "threshold", "person", "people", "network", "tradition",
    "language",
}

# Curated fallbacks for parent hints that name no entity (existing or new):
# geographic groupings, dual-country hints, and modern states the app does not
# model yet. Each maps to the most specific EXISTING ancestor available.
HINT_OVERRIDES = {
    "britain and ireland": "europe.western",
    "indigenous north america": "americas.north",
    "low countries": "europe.western",
    "netherlands": "europe.western.netherlands",
    "scandinavia": "europe.northern",
    "baltic states": "europe.northern",
    "balkans": "europe.eastern",
    "yugoslavia": "europe.eastern",
    "kosovo": "europe.eastern",
    "bohemia": "europe.central",
    "czech lands": "europe.central",
    "iberia": "europe.western",
    "napoleonic europe": "europe",
    "black sea region": "europe.eastern",
    "caucasus": "west-asia",
    "levant": "west-asia.mesopotamia",
    "arabian peninsula": "west-asia.arabia",
    "pahlavi iran": "west-asia.iran",
    "qing china": "east-asia.china",
    "macau": "east-asia.china",
    "northeast asia": "east-asia",
    "tokugawa japan": "east-asia.japan.edo",
    "meiji japan": "east-asia.japan.modern.meiji",
    "afghanistan": "south-asia",
    "punjab": "south-asia",
    "india and pakistan": "south-asia",
    "congo": "africa.central",
    "equatorial guinea": "africa.central",
    "west africa": "africa.west",
    "benin": "africa.west",
    "sierra leone": "africa.west",
    "the gambia": "africa.west",
    "guinea bissau": "africa.west",
    "cote d ivoire": "africa.west",
    "mauritania": "africa.west",
    "western sahara": "africa.west",
    "horn of africa": "africa.east",
    "djibouti": "africa.east",
    "seychelles": "africa.east",
    "libya": "africa.north",
    "south america": "americas",
    "latin america": "americas",
    "the americas": "americas",
    "central america": "americas.mesoamerica",
    "spanish america": "americas",
    "caribbean": "americas",
    "quebec canada": "americas.north",
    "hawaii": "oceania.polynesia.hawaii",
    "papua new guinea": "oceania.melanesia",
    "vanuatu": "oceania.melanesia",
    "nauru": "oceania.micronesia",
    "kiribati": "oceania.micronesia",
    "marshall islands": "oceania.micronesia",
    "palau": "oceania.micronesia",
    "the bahamas": "americas",
    "atlantic world": "global",
    "united states supreme court": "americas.north.usa",
}

ID_RE = re.compile(r"^[a-z0-9]+([.-][a-z0-9]+)*$")
YEAR_WINDOW = 25
MAX_SUMMARY = 299  # "under 300 characters"

OUTPUT_KEYS = [
    "id", "name", "kind", "parent_id", "start_year", "end_year", "extant",
    "start_dating_method", "end_dating_method", "summary", "aliases",
    "confidence", "source_file",
]


# ---------------------------------------------------------------- normalising
def fold(text: str) -> str:
    """Case-fold + diacritic-fold + punctuation-fold a name for matching."""
    if not text:
        return ""
    s = unicodedata.normalize("NFKD", text)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.casefold()
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())


def slugify(text: str) -> str:
    """Sanitise to the id charset. Digits are preserved as digits."""
    s = unicodedata.normalize("NFKD", str(text))
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.casefold().replace("&", "-and-")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    s = re.sub(r"-{2,}", "-", s)
    return s


def strip_paren(text: str) -> str:
    """'France (Medieval to Modern)' -> 'France'."""
    return re.sub(r"\s*\([^)]*\)", "", text or "").strip()


def region_of(entity_id: str) -> str:
    return entity_id.split(".", 1)[0]


def regions_compatible(a: str, b: str) -> bool:
    if not a or not b:
        return True
    if a == b:
        return True
    # "global" spans everything, so it never rules a match out.
    return "global" in (a, b)


def one_line(summary: str) -> str:
    s = re.sub(r"\s+", " ", (summary or "")).strip()
    if len(s) > MAX_SUMMARY:
        cut = s[:MAX_SUMMARY]
        if " " in cut:
            cut = cut[: cut.rfind(" ")]
        s = cut.rstrip(" ,;:-") + "..."
        if len(s) > MAX_SUMMARY:
            s = s[:MAX_SUMMARY]
    return s


# ---------------------------------------------------------------- load inputs
def load_existing():
    data = json.loads(ENTITIES.read_text())
    rows = data["entities"]
    by_id = {r["id"]: r for r in rows}
    name_index = defaultdict(list)   # fold(name/alias) -> [entity]
    loose_index = defaultdict(list)  # fold(name/alias, parentheticals removed)
    for r in rows:
        forms = [r.get("name", "")] + list(r.get("aliases") or [])
        for form in forms:
            k = fold(form)
            if k:
                name_index[k].append(r)
            lk = fold(strip_paren(form))
            if lk and lk != k:
                loose_index[lk].append(r)
    return rows, by_id, name_index, loose_index


def load_research():
    rows = []
    for fname, region, fallback in SOURCES:
        data = json.loads((RESEARCH / fname).read_text())
        for i, r in enumerate(data):
            row = dict(r)
            row["source_file"] = fname
            row["_order"] = (fname, i)
            reg = region or slugify(r.get("region_hint") or "global")
            row["_region"] = reg
            row["_fallback_parent"] = fallback or reg
            rows.append(row)
    return rows


def match_keys(row) -> set[str]:
    keys = {fold(row.get("name", ""))}
    keys |= {fold(a) for a in (row.get("aliases") or [])}
    return {k for k in keys if k}


def years_close(a, b) -> bool:
    if a is None or b is None:
        return False
    return abs(a - b) <= YEAR_WINDOW


# ------------------------------------------------------------------- pipeline
def main() -> int:
    existing_rows, existing_by_id, existing_index, existing_loose = load_existing()
    research = load_research()
    total_in = len(research)

    # --- 1. dedupe against existing entities -----------------------------
    dropped_existing = []
    survivors = []
    for row in research:
        hit = None
        for key in sorted(match_keys(row)):
            for cand in existing_index.get(key, []):
                if not years_close(row.get("start_year"), cand.get("start_year")):
                    continue
                if not regions_compatible(row["_region"], region_of(cand["id"])):
                    continue
                hit = (cand, key)
                break
            if hit:
                break
        if hit:
            cand, key = hit
            dropped_existing.append({
                "name": row["name"],
                "kind": row["kind"],
                "start_year": row.get("start_year"),
                "source_file": row["source_file"],
                "matched_id": cand["id"],
                "matched_name": cand["name"],
                "matched_kind": cand["kind"],
                "matched_start_year": cand.get("start_year"),
                "matched_on": key,
            })
        else:
            survivors.append(row)

    # --- 2. dedupe within/across the research files ----------------------
    dropped_batch = []
    kept = []  # list of rows
    batch_index = defaultdict(list)  # fold key -> [index into kept]

    for row in survivors:
        keys = match_keys(row)
        found = None
        for key in sorted(keys):
            for idx in batch_index.get(key, []):
                other = kept[idx]
                if not years_close(row.get("start_year"), other.get("start_year")):
                    continue
                if not regions_compatible(row["_region"], other["_region"]):
                    continue
                found = (idx, key)
                break
            if found:
                break
        if found is None:
            kept.append(row)
            for key in keys:
                batch_index[key].append(len(kept) - 1)
            continue

        idx, key = found
        incumbent = kept[idx]
        if len(row.get("summary") or "") > len(incumbent.get("summary") or ""):
            winner, loser = row, incumbent
            kept[idx] = row
            for k in match_keys(row):
                if idx not in batch_index[k]:
                    batch_index[k].append(idx)
        else:
            winner, loser = incumbent, row
        dropped_batch.append({
            "dropped_name": loser["name"],
            "dropped_source": loser["source_file"],
            "dropped_start_year": loser.get("start_year"),
            "dropped_summary_len": len(loser.get("summary") or ""),
            "kept_name": winner["name"],
            "kept_source": winner["source_file"],
            "kept_summary_len": len(winner.get("summary") or ""),
            "matched_on": key,
        })

    # --- 3. resolve parents ---------------------------------------------
    # batch lookup: by slug, and by folded name/alias
    by_slug = {}
    by_name = defaultdict(list)
    by_loose = defaultdict(list)
    for i, row in enumerate(kept):
        by_slug.setdefault(row["suggested_id_slug"], i)
        by_slug.setdefault(slugify(row["name"]), i)
        for k in match_keys(row):
            by_name[k].append(i)
        for form in [row["name"]] + list(row.get("aliases") or []):
            lk = fold(strip_paren(form))
            if lk and lk not in match_keys(row):
                by_loose[lk].append(i)

    def existing_lookup(hint: str, region: str):
        cands = existing_index.get(fold(hint), []) or \
            existing_loose.get(fold(strip_paren(hint)), [])
        if not cands:
            return None
        same = [c for c in cands if region_of(c["id"]) == region]
        pool = same or [c for c in cands
                        if regions_compatible(region, region_of(c["id"]))]
        if not pool:
            return None
        # most canonical: shallowest id, then shortest
        pool.sort(key=lambda c: (c["id"].count("."), len(c["id"])))
        return pool[0]["id"]

    def batch_lookup(hint: str, region: str, self_idx: int):
        cands = []
        idx = by_slug.get(slugify(hint))
        if idx is not None:
            cands.append(idx)
        cands += by_name.get(fold(hint), [])
        cands += by_loose.get(fold(strip_paren(hint)), [])
        for i in cands:
            if i == self_idx:
                continue
            if regions_compatible(region, kept[i]["_region"]):
                return i
        return None

    def hint_variants(hint: str):
        """Full hint first; only then split compound hints like 'France and Germany'.
        Splitting last keeps proper names ('Bosnia and Herzegovina') intact."""
        yield hint
        for sep in ("/", " and ", " & ", ", "):
            if sep in hint:
                for part in hint.split(sep):
                    part = part.strip()
                    if part:
                        yield part

    parent_existing = {}   # idx -> existing id
    parent_batch = {}      # idx -> other idx
    unresolved = []
    overridden = []

    for i, row in enumerate(kept):
        hint = (row.get("parent_hint") or "").strip()
        region = row["_region"]
        resolved = None
        via_batch = None
        override = HINT_OVERRIDES.get(fold(hint))
        if override and override in existing_by_id:
            parent_existing[i] = override
            overridden.append({
                "name": row["name"],
                "source_file": row["source_file"],
                "parent_hint": hint,
                "assigned_parent": override,
            })
            continue
        if hint:
            for variant in hint_variants(hint):
                eid = existing_lookup(variant, region)
                if eid:
                    resolved = eid
                    break
                bidx = batch_lookup(variant, region, i)
                if bidx is not None:
                    via_batch = bidx
                    break
        if resolved is not None:
            parent_existing[i] = resolved
        elif via_batch is not None:
            parent_batch[i] = via_batch
        else:
            fallback = row["_fallback_parent"]
            if fallback not in existing_by_id:
                fallback = region if region in existing_by_id else "global"
            parent_existing[i] = fallback
            unresolved.append({
                "name": row["name"],
                "source_file": row["source_file"],
                "parent_hint": hint or "(none)",
                "assigned_parent": fallback,
            })

    # break cycles in batch-parent links (break the node inside the cycle)
    def break_cycles():
        for start in list(parent_batch):
            path = []
            seen = set()
            node = start
            while node in parent_batch:
                if node in seen:
                    # node is the entry point of a cycle: detach it
                    row = kept[node]
                    fallback = row["_fallback_parent"]
                    if fallback not in existing_by_id:
                        fallback = row["_region"] if row["_region"] in existing_by_id else "global"
                    parent_batch.pop(node, None)
                    parent_existing[node] = fallback
                    unresolved.append({
                        "name": row["name"],
                        "source_file": row["source_file"],
                        "parent_hint": (row.get("parent_hint") or "(none)") + " [cyclic]",
                        "assigned_parent": fallback,
                    })
                    break
                seen.add(node)
                path.append(node)
                node = parent_batch[node]

    break_cycles()

    # --- 4. assign ids ---------------------------------------------------
    used_ids = set(existing_by_id)
    assigned = {}   # idx -> id
    collisions = []

    def make_id(idx: int, parent_id: str) -> str:
        row = kept[idx]
        slug = slugify(row["suggested_id_slug"]) or slugify(row["name"])
        candidate = f"{parent_id}.{slug}" if parent_id else slug
        if candidate not in used_ids:
            return candidate
        year = row.get("start_year")
        alts = []
        if year is not None:
            alts.append(f"{candidate}-{abs(year)}" + ("-bce" if year < 0 else ""))
        alts.append(f"{candidate}-{slugify(row['kind'])}")
        alts += [f"{candidate}-{n}" for n in range(2, 60)]
        for alt in alts:
            if alt not in used_ids:
                collisions.append({
                    "name": row["name"],
                    "source_file": row["source_file"],
                    "wanted": candidate,
                    "assigned": alt,
                })
                return alt
        raise RuntimeError(f"cannot disambiguate {candidate}")

    def resolve(idx: int, stack=()):
        if idx in assigned:
            return assigned[idx]
        if idx in stack:  # safety net
            parent_id = kept[idx]["_fallback_parent"]
        elif idx in parent_existing:
            parent_id = parent_existing[idx]
        else:
            parent_id = resolve(parent_batch[idx], stack + (idx,))
        new_id = make_id(idx, parent_id)
        assigned[idx] = new_id
        used_ids.add(new_id)
        kept[idx]["_parent_id"] = parent_id
        return new_id

    sys.setrecursionlimit(10000)
    for i in range(len(kept)):
        resolve(i)

    # --- 5. validate + fix ----------------------------------------------
    fixes = []
    out = []
    for i, row in enumerate(kept):
        rid = assigned[i]
        name = row["name"]
        kind = row["kind"]
        if kind not in VALID_KINDS:
            fixes.append(f"`{rid}` invalid kind `{kind}` -> `period`")
            kind = "period"

        summary = one_line(row.get("summary") or "")
        if summary != (row.get("summary") or ""):
            fixes.append(f"`{rid}` summary normalised to one line under 300 chars")

        extant = bool(row.get("extant"))
        start = row.get("start_year")
        end = row.get("end_year")

        if start == 0:
            start = 1
            fixes.append(f"`{rid}` start_year 0 does not exist -> 1")
        if end == 0:
            end = -1
            fixes.append(f"`{rid}` end_year 0 does not exist -> -1")

        if extant and end is not None:
            fixes.append(f"`{rid}` extant with end_year {end} -> end_year null")
            end = None
        if not extant and end is None:
            extant = True
            fixes.append(f"`{rid}` end_year null but extant false -> extant true")

        if start is not None and end is not None and start > end:
            fixes.append(f"`{rid}` start_year {start} > end_year {end} -> swapped")
            start, end = end, start

        if not ID_RE.match(rid):
            raise RuntimeError(f"id fails pattern: {rid}")

        aliases = [a for a in (row.get("aliases") or []) if a and a.strip()]
        seen, uniq = set(), []
        for a in aliases:
            k = fold(a)
            if k and k != fold(name) and k not in seen:
                seen.add(k)
                uniq.append(a.strip())

        out.append({
            "id": rid,
            "name": name,
            "kind": kind,
            "parent_id": row.get("_parent_id"),
            "start_year": start,
            "end_year": end,
            "extant": extant,
            "start_dating_method": row.get("start_dating_method") or "unknown",
            "end_dating_method": "calendar" if end is not None else None,
            "summary": summary,
            "aliases": uniq,
            "confidence": row.get("confidence"),
            "source_file": row["source_file"],
        })

    out = [{k: r[k] for k in OUTPUT_KEYS} for r in out]
    out.sort(key=lambda r: r["id"])

    # --- self-check (raises if the output would be unsafe to author from) ---
    seen_ids = set()
    all_ids = set(existing_by_id) | {r["id"] for r in out}
    for r in out:
        assert r["id"] not in seen_ids, f"duplicate id {r['id']}"
        seen_ids.add(r["id"])
        assert ID_RE.match(r["id"]), f"bad id {r['id']}"
        assert r["parent_id"] in all_ids, f"dangling parent {r['parent_id']}"
        assert r["id"] == f"{r['parent_id']}.{r['id'].rsplit('.', 1)[1]}", \
            f"id/parent mismatch {r['id']}"
        assert r["kind"] in VALID_KINDS
        assert "\n" not in r["summary"] and len(r["summary"]) < 300
        assert (r["end_year"] is None) == bool(r["extant"])
        assert (r["end_dating_method"] == "calendar") == (r["end_year"] is not None)
        assert r["start_year"] != 0 and r["end_year"] != 0
        if r["start_year"] is not None and r["end_year"] is not None:
            assert r["start_year"] <= r["end_year"]
        assert set(r) == set(OUTPUT_KEYS)
    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")

    # --- 7. report -------------------------------------------------------
    kind_counts = Counter(r["kind"] for r in out)
    region_counts = Counter(region_of(r["id"]) for r in out)
    source_counts = Counter(r["source_file"] for r in out)

    L = []
    L.append("# modern-merged.json build report\n")
    L.append(f"Generated by `docs/research/merge_modern.py` from "
             f"`usa.json`, `britain.json`, `modern-nations.json`.\n")
    L.append("## Method\n")
    L.append("- Duplicate test: case-folded + diacritic-folded + punctuation-folded "
             "match on name or any alias, start years within 25 years, and "
             "compatible top-level region (`global` is compatible with every "
             "region). The region guard is what keeps Alexandria, Egypt distinct "
             "from Alexandria, Virginia.")
    L.append("- Within-batch ties keep the row with the longer summary.")
    L.append("- Parent hints resolve in this order: curated geographic override, "
             "existing entity (exact, then parenthetical-stripped name/alias), "
             "batch row being created in this run, then split of compound hints "
             "(\"France and Germany\"), then the nearest existing ancestor.")
    L.append("- Ids are `<resolved parent id>.<suggested_id_slug>`; event numerals "
             "stay as digits (e.g. `war-of-1812`, `september-11`).")
    L.append("- No uncertainty or bounds fields are emitted.\n")
    L.append("## Totals\n")
    L.append(f"- Total rows in: **{total_in}**")
    L.append(f"- Dropped as duplicates of existing entities: **{len(dropped_existing)}**")
    L.append(f"- Dropped as duplicates within the batch: **{len(dropped_batch)}**")
    L.append(f"- Unresolved parent hints (assigned to nearest existing ancestor): **{len(unresolved)}**")
    L.append(f"- Parent hints resolved via curated geographic overrides: **{len(overridden)}**")
    L.append(f"- Id collisions disambiguated: **{len(collisions)}**")
    L.append(f"- Validation fixes applied: **{len(fixes)}**")
    L.append(f"- **Final count: {len(out)}**\n")

    L.append("## Breakdown by kind\n")
    L.append("| kind | count |\n| --- | --- |")
    for k, v in kind_counts.most_common():
        L.append(f"| {k} | {v} |")
    L.append("")

    L.append("## Breakdown by top-level region\n")
    L.append("| region | count |\n| --- | --- |")
    for k, v in region_counts.most_common():
        L.append(f"| {k} | {v} |")
    L.append("")

    L.append("## Breakdown by source file\n")
    L.append("| source_file | kept |\n| --- | --- |")
    for k, v in source_counts.most_common():
        L.append(f"| {k} | {v} |")
    L.append("")

    L.append(f"## Duplicates dropped against existing entities ({len(dropped_existing)})\n")
    if dropped_existing:
        L.append("| research row | kind | start | source | matched existing id | existing name | existing start | matched on |")
        L.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
        for d in sorted(dropped_existing, key=lambda d: (d["source_file"], d["name"])):
            L.append("| {name} | {kind} | {start_year} | {source_file} | `{matched_id}` | {matched_name} | {matched_start_year} | {matched_on} |".format(**d))
    else:
        L.append("_none_")
    L.append("")

    L.append(f"## Duplicates dropped within the batch ({len(dropped_batch)})\n")
    if dropped_batch:
        L.append("| dropped | source | start | summary len | kept | source | summary len | matched on |")
        L.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
        for d in sorted(dropped_batch, key=lambda d: d["dropped_name"]):
            L.append("| {dropped_name} | {dropped_source} | {dropped_start_year} | {dropped_summary_len} | {kept_name} | {kept_source} | {kept_summary_len} | {matched_on} |".format(**d))
    else:
        L.append("_none_")
    L.append("")

    L.append(f"## Unresolved parents ({len(unresolved)})\n")
    if unresolved:
        agg = Counter((u["parent_hint"], u["assigned_parent"], u["source_file"])
                      for u in unresolved)
        L.append("| parent_hint | source | rows | assigned parent |")
        L.append("| --- | --- | --- | --- |")
        for (hint, parent, src), n in sorted(agg.items(), key=lambda kv: -kv[1]):
            L.append(f"| {hint} | {src} | {n} | `{parent}` |")
        L.append("")
        L.append("<details><summary>Affected rows</summary>\n")
        for u in sorted(unresolved, key=lambda u: (u["parent_hint"], u["name"])):
            L.append(f"- {u['name']} ({u['source_file']}) — hint `{u['parent_hint']}` -> `{u['assigned_parent']}`")
        L.append("\n</details>")
    else:
        L.append("_none_")
    L.append("")

    L.append(f"## Parent hints resolved via curated overrides ({len(overridden)})\n")
    if overridden:
        agg2 = Counter((o["parent_hint"], o["assigned_parent"]) for o in overridden)
        L.append("| parent_hint | rows | assigned parent |")
        L.append("| --- | --- | --- |")
        for (hint, parent), n in sorted(agg2.items(), key=lambda kv: -kv[1]):
            L.append(f"| {hint} | {n} | `{parent}` |")
    else:
        L.append("_none_")
    L.append("")

    L.append(f"## Id collisions disambiguated ({len(collisions)})\n")
    if collisions:
        L.append("| name | source | wanted id | assigned id |")
        L.append("| --- | --- | --- | --- |")
        for c in collisions:
            L.append(f"| {c['name']} | {c['source_file']} | `{c['wanted']}` | `{c['assigned']}` |")
    else:
        L.append("_none_")
    L.append("")

    L.append(f"## Validation fixes ({len(fixes)})\n")
    if fixes:
        for f in fixes[:200]:
            L.append(f"- {f}")
        if len(fixes) > 200:
            L.append(f"- ...and {len(fixes) - 200} more")
    else:
        L.append("_none_ — inputs already satisfied every rule.")
    L.append("")

    OUT_REPORT.write_text("\n".join(L) + "\n")

    print(f"total in: {total_in}")
    print(f"dropped vs existing: {len(dropped_existing)}")
    print(f"dropped within batch: {len(dropped_batch)}")
    print(f"unresolved parents: {len(unresolved)}")
    print(f"curated parent overrides: {len(overridden)}")
    print(f"id collisions: {len(collisions)}")
    print(f"fixes: {len(fixes)}")
    print(f"final: {len(out)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
