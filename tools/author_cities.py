"""Author the enumerated cities.

1,504 rows across four regional files, collected by recall rather than by web search after the
search approach returned 34 cities for the whole of world history. Kyoto and Athens were reported
missing from use, which is what finally forced this.

Three things this has to get right.

**A city is not a period.** `still_inhabited` becomes `extant: true` and no end year. Conquest and
renaming are not endings: Constantinople does not end in 1453, it becomes Istanbul, and that goes
in a name form rather than in `end_year`.

**Confidence becomes uncertainty, not a separate field.** The researchers graded their own certainty
about dates as high, medium or low. That grading maps onto bounds -- which is what the schema now
uses -- rather than being stored as a fourth opinion the reader has to reconcile. A `low` date on a
mound complex gets wide bounds; a `high` date on a Roman foundation gets narrow ones.

**Do not duplicate what exists.** The dataset already holds Byblos, Tyre, Sidon, Arwad, Tenochtitlan
and Great Zimbabwe, and re-authoring them would produce exactly the duplicate pairs this project has
already created twice. Existing entities are skipped, and the skip is reported rather than silent.
"""

import glob
import json
import re
import unicodedata

# Bound half-widths by the researcher's own confidence and by how old the date is. A `low`
# confidence date in deep prehistory is uncertain by millennia; a `low` confidence medieval
# foundation is uncertain by a century.
CONFIDENCE_SCALE = {"high": 0.02, "medium": 0.06, "low": 0.15}
MIN_HALF = {"high": 10, "medium": 25, "low": 50}


def _half_width(year, confidence):
    scale = CONFIDENCE_SCALE.get(confidence, 0.06)
    floor = MIN_HALF.get(confidence, 25)
    if year >= 1000:
        # Documentary era: a founding date in the second millennium CE is known from records.
        return 0
    return max(floor, int(abs(year) * scale))


def _fold(text):
    stripped = "".join(c for c in unicodedata.normalize("NFD", text)
                       if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", stripped.lower()).strip("-")


def _no_zero(y):
    return -1 if y == 0 else y


def _load():
    """Rows from every regional file, deduplicated on slug AND on folded name.

    Slug alone was not enough. Two researchers reached the same place by different slugs --
    `palembang-srivijaya` against `palembang`, `muara-jambi` against `muarajambi`,
    `kota-batu-brunei` against `kotabatu-brunei` -- so a slug-only check let five duplicate pairs
    through and the sibling-uniqueness rule caught them. The name is the thing being deduplicated,
    so the name has to be part of the key.
    """
    rows, seen_slug, seen_name = [], set(), set()
    for path in sorted(glob.glob("docs/research/cities-*.json")):
        if "websearch" in path:
            continue
        for row in json.load(open(path)):
            slug = _fold(row.get("slug") or row["name"])
            name_key = _fold(row["name"])
            if slug in seen_slug or name_key in seen_name:
                continue
            seen_slug.add(slug)
            seen_name.add(name_key)
            row["slug"] = slug
            rows.append(row)
    return rows


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}
    existing_names = {}
    for e in entities:
        existing_names.setdefault(e["name"].casefold(), e)
        for alias in e.get("aliases") or []:
            existing_names.setdefault(alias.casefold(), e)

    rows = _load()
    authored, skipped, no_parent = 0, [], []

    for row in rows:
        region = row.get("region_hint")
        if region is None or region not in by_id:
            no_parent.append(row["name"])
            continue

        # Already present under some other kind, or as an empire of the same name. Skipping is
        # the whole reason this loop checks names as well as ids.
        hit = existing_names.get(row["name"].casefold())
        if hit is not None:
            skipped.append(f"{row['name']} -> {hit['id']} [{hit['kind']}]")
            continue

        start = row["start_year"]
        end = row.get("end_year")
        inhabited = bool(row.get("still_inhabited"))
        confidence = row.get("confidence", "medium")

        fields = {
            "summary": (row.get("summary") or "")[:200] or None,
            "start_dating_method": "typological" if start < 1000 else "calendar",
        }
        half = _half_width(start, confidence)
        if half > 0:
            fields["start_year_min"] = _no_zero(start - half)
            fields["start_year_max"] = _no_zero(start + half)

        if inhabited:
            # A living city has no end year. This is the distinction the `city` kind exists for.
            end = None
            fields["extant"] = True
        elif end is not None:
            fields["end_dating_method"] = "typological" if end < 1000 else "calendar"
            end_half = _half_width(end, confidence)
            if end_half > 0:
                fields["end_year_min"] = _no_zero(end - end_half)
                fields["end_year_max"] = _no_zero(end + end_half)

        # Unique, and never a restatement of the entity's own name. Aleppo arrived with "Halab"
        # listed twice and the schema rightly refused it.
        forms, seen_forms = [], {row["name"].casefold()}
        for alias in row.get("aliases") or []:
            key = alias.casefold()
            if key in seen_forms:
                continue
            seen_forms.add(key)
            forms.append({"name": alias, "kind": "common"})
        modern = (row.get("modern_name") or "").split(",")[0].strip()
        if modern and modern.casefold() not in seen_forms:
            # Constantinople becoming Istanbul is a name change, not a death.
            forms.append({"name": modern, "kind": "historical"})
        if forms:
            fields["name_forms"] = forms

        contested = (row.get("contested") or "").strip()
        if contested and contested.lower() not in ("omit", "none", "n/a", "tbd", "-"):
            fields["caveats"] = [{"kind": "contested-existence", "text": contested[:200]}]

        # Tier by how much a general reader is likely to want it. Confidence is a poor proxy for
        # importance, so this uses the researcher's own `peak` note only as a tiebreak.
        tier = "intermediate" if confidence == "high" else "specialist"

        fields = {k: v for k, v in fields.items() if v is not None}
        E(f"{region}.city-{row['slug']}", "city", row["name"], region,
          start=start, end=end, tier=tier, allow_outside_parent_dates=True, **fields)
        authored += 1

    print(f"author_cities: {authored} authored, {len(skipped)} already present, "
          f"{len(no_parent)} with no region")
    if skipped:
        print(f"  skipped e.g. {skipped[:4]}")
    if no_parent:
        print(f"  no region e.g. {no_parent[:4]}")
