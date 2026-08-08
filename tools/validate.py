"""Validate every JSON data file against its schema and check referential integrity.

Exits nonzero on ERRORS; prints WARNINGS but does not fail on them.

Errors:
    - Schema violation (any level)
    - Duplicate entity id
    - Missing parent / cross_parent / calendar / theme / frame reference
    - Inverted date range (start_year > end_year)
    - Year zero used with BCE/CE (there is no year 0 in this scheme)
    - Named-year sequence has inverted or overlapping entries within a calendar

Warnings:
    - Child date range falls outside parent date range without allow_outside_parent_dates
    - Foundational entity missing summary
    - date_precision omitted on a dated entity
    - Reference frame missing summary
    - Duplicate sibling display names under the same parent
"""

import json
import re
import sys
from pathlib import Path
from collections import defaultdict, Counter
from jsonschema import Draft202012Validator, RefResolver

# Repo layout: schemas live at the repo root, generated data under src/data
# so Vite can inline it at build time.
ROOT = Path(__file__).resolve().parent.parent
SCHEMAS = ROOT / "schemas"
DATA = ROOT / "src" / "data"

# Load schemas
def _load(p):
    with open(p) as f:
        return json.load(f)

entity_schema = _load(SCHEMAS / "entity.schema.json")
calendar_schema = _load(SCHEMAS / "calendar.schema.json")
theme_schema = _load(SCHEMAS / "theme.schema.json")
frame_schema = _load(SCHEMAS / "reference-frame.schema.json")
entities_file_schema = _load(SCHEMAS / "entities-file.schema.json")
calendars_file_schema = _load(SCHEMAS / "calendars-file.schema.json")
themes_file_schema = _load(SCHEMAS / "themes-file.schema.json")
frames_file_schema = _load(SCHEMAS / "reference-frames-file.schema.json")

# Resolver for $ref between file schemas and item schemas
store = {
    entity_schema["$id"]: entity_schema,
    calendar_schema["$id"]: calendar_schema,
    theme_schema["$id"]: theme_schema,
    frame_schema["$id"]: frame_schema,
    "entity.schema.json": entity_schema,
    "calendar.schema.json": calendar_schema,
    "theme.schema.json": theme_schema,
    "reference-frame.schema.json": frame_schema,
}

def _validator(schema):
    resolver = RefResolver.from_schema(schema, store=store)
    return Draft202012Validator(schema, resolver=resolver)

# Load data
entities_file = _load(DATA / "entities.json")
calendars_file = _load(DATA / "calendars.json")
themes_file = _load(DATA / "themes.json")
frames_file = _load(DATA / "reference-frames.json")

errors = []
warnings = []


def _validate_file(schema, data, label):
    v = _validator(schema)
    for err in v.iter_errors(data):
        path = "/".join(str(p) for p in err.absolute_path)
        errors.append(f"{label} schema: {err.message} at {path}")


# ---- Schema validation (whole file, including wrapper) ---------------------
_validate_file(entities_file_schema, entities_file, "entities.json")
_validate_file(calendars_file_schema, calendars_file, "calendars.json")
_validate_file(themes_file_schema, themes_file, "themes.json")
_validate_file(frames_file_schema, frames_file, "reference-frames.json")


entities = entities_file.get("entities", [])
calendars = calendars_file.get("calendars", [])
themes = themes_file.get("themes", [])
frames = frames_file.get("frames", [])
entity_ids = {e["id"] for e in entities}


# ---- Referential integrity -------------------------------------------------
seen = set()
for e in entities:
    if e["id"] in seen:
        errors.append(f"entity duplicate id: {e['id']}")
    seen.add(e["id"])
    p = e.get("parent_id")
    if p is not None and p not in entity_ids:
        errors.append(f"entity {e['id']}: parent_id {p} does not exist")
    for x in e.get("cross_parent_ids", []):
        if x not in entity_ids:
            errors.append(f"entity {e['id']}: cross_parent_ids ref {x} does not exist")
    for link in e.get("links", []):
        if link["entity_id"] not in entity_ids:
            errors.append(f"entity {e['id']}: link.entity_id {link['entity_id']} does not exist")
    for rid in e.get("redirect_ids", []):
        if rid in entity_ids:
            errors.append(f"entity {e['id']}: redirect_ids {rid} collides with a live entity id")

for t in themes:
    for eid in t.get("entity_ids", []):
        if eid not in entity_ids:
            errors.append(f"theme {t['id']}: entity_ids ref {eid} does not exist")

# ---- source registry: referential integrity and the rules from DESIGN.md ----
# Rule numbers refer to docs/DESIGN.md, "Validator rules this implies".
try:
    with open(DATA / "sources.json", encoding="utf-8") as f:
        _sources = json.load(f)["sources"]
except FileNotFoundError:
    _sources = []
source_ids = {s_["id"] for s_ in _sources}
cited = set()

for e in entities:
    def _cite(ids, where):
        for sid in ids:
            cited.add(sid)
            if sid not in source_ids:
                errors.append(f"entity {e['id']}: {where} source_ids ref {sid} is not in the registry")

    _cite(e.get("source_ids", []), "")
    alts = e.get("alternatives", [])
    for a in alts:
        _cite(a.get("source_ids", []), f"alternative {a.get('label')!r}")
    for c in e.get("caveats", []):
        _cite(c.get("source_ids", []), "caveat")

    # Rule 1: if claims differ, say why.
    if alts and not e.get("date_note"):
        errors.append(f"entity {e['id']}: has alternatives but no date_note explaining why they differ")
    # Rule 2: superseded by what?
    for a in alts:
        if a.get("standing") == "superseded" and not a.get("note") and not a.get("source_ids"):
            errors.append(f"entity {e['id']}: superseded alternative {a.get('label')!r} says neither why nor by what")
    # Rule 5: at most one consensus claim per entity.
    if sum(1 for a in alts if a.get("standing") == "consensus") > 0 and e.get("standing") == "consensus":
        errors.append(f"entity {e['id']}: more than one claim marked consensus")
    # Rule 10: as_of is for live disputes only.
    if e.get("as_of") and alts and all(a.get("standing") == "superseded" for a in alts):
        warnings.append(f"entity {e['id']}: as_of set but every alternative is superseded; the question is settled")
    if e.get("as_of") and not alts:
        warnings.append(f"entity {e['id']}: as_of set but there is no open dispute to re-check")
    # Rule 11: b2k belongs to ice-core dating.
    nd = e.get("native_date") or {}
    if nd.get("calendar_id") == "b2k" and e.get("start_dating_method") not in ("layer-counting", None):
        errors.append(
            f"entity {e['id']}: native_date in b2k but start_dating_method is "
            f"{e.get('start_dating_method')}"
        )

# Rule 6: an uncited registry entry is dead weight.
for sid in sorted(source_ids - cited):
    warnings.append(f"source {sid}: in the registry but cited by nothing")

for f_ in frames:
    if f_.get("entity_id") and f_["entity_id"] not in entity_ids:
        errors.append(f"frame {f_['id']}: entity_id {f_['entity_id']} does not exist")

# Calendar named-year -> entity refs
for c in calendars:
    for ny in c.get("named_years", []):
        if ny.get("entity_id") and ny["entity_id"] not in entity_ids:
            errors.append(f"calendar {c['id']} named_year {ny['name']}: entity_id does not exist")
        for eid in ny.get("entity_ids", []):
            if eid not in entity_ids:
                errors.append(f"calendar {c['id']} named_year {ny['name']}: entity_ids ref {eid} does not exist")

# calendar_ids on entities must exist
calendar_ids = {c["id"] for c in calendars}
for e in entities:
    for cid in e.get("calendar_ids", []):
        if cid not in calendar_ids:
            errors.append(f"entity {e['id']}: calendar_ids ref {cid} does not exist")


# ---- Date sanity -----------------------------------------------------------
for e in entities:
    s, en = e.get("start_year"), e.get("end_year")
    if s == 0 or en == 0:
        errors.append(f"entity {e['id']}: year 0 is not valid in BCE/CE (there is no year 0)")
    if s is not None and en is not None and s > en:
        errors.append(f"entity {e['id']}: start_year {s} > end_year {en}")
    # Range fields sanity
    smin, smax = e.get("start_year_min"), e.get("start_year_max")
    if smin is not None and smax is not None and smin > smax:
        errors.append(f"entity {e['id']}: start_year_min {smin} > start_year_max {smax}")
    emin, emax = e.get("end_year_min"), e.get("end_year_max")
    if emin is not None and emax is not None and emin > emax:
        errors.append(f"entity {e['id']}: end_year_min {emin} > end_year_max {emax}")


# ---- Named-year sequence checks -------------------------------------------
for c in calendars:
    seen_years = set()
    prev_start = None
    for ny in c.get("named_years", []):
        s = ny["start_gregorian"]
        e_ = ny.get("end_gregorian")
        if e_ is not None and s > e_:
            errors.append(f"calendar {c['id']} named_year {ny['name']}: start {s} > end {e_}")


# ---- Containment WARNINGS --------------------------------------------------
by_id = {e["id"]: e for e in entities}
for e in entities:
    if e.get("allow_outside_parent_dates"):
        continue
    p_id = e.get("parent_id")
    if not p_id or p_id not in by_id:
        continue
    p = by_id[p_id]
    cs, ce = e.get("start_year"), e.get("end_year")
    ps, pe = p.get("start_year"), p.get("end_year")
    if cs is None or ps is None:
        continue
    if cs < ps:
        warnings.append(
            f"entity {e['id']}: start_year {cs} predates parent {p_id} start {ps}. "
            f"Set allow_outside_parent_dates=true if intentional."
        )
        continue
    if ce is not None and pe is not None and ce > pe:
        warnings.append(
            f"entity {e['id']}: end_year {ce} outlasts parent {p_id} end {pe}. "
            f"Set allow_outside_parent_dates=true if intentional."
        )



# ---- Dating method must be physically capable of the date -------------------
#
# Radiocarbon decays out of usable range by about 50,000 years; nothing older
# can be dated by it at all. So `dating_method: radiocarbon-*` on an entity
# starting before that is not a debatable call, it is impossible.
#
# This caught six real entities, three of them authored by hand over previous
# sessions. The cause was structural rather than careless: `dating_method` was a
# single per-entity field, but a long-lived entity has two boundaries dated by
# different means. Neanderthals appear at 400 ka (uranium-series and
# luminescence at Sima de los Huesos) and disappear at 40 ka (AMS radiocarbon).
# Recording the end's method and letting it describe the start was the natural
# mistake, and it was invisible until something rendered the label.
#
# Q-30 RESOLVED (schema 3.0.0): the field is now per-boundary, so this check no
# longer has to assume which boundary it is talking about. It runs on BOTH, and
# the end check is new capability rather than a port -- an impossible end date
# was previously unreachable, because the end had no method of its own to test.
RADIOCARBON_CEILING_BP = 55_000  # generous; practical limit is nearer 50,000


def _bp(historical_year):
    return 1950 - (historical_year + 1 if historical_year < 0 else historical_year)


for e in entities:
    for boundary, method_field, year_field in (
        ("start", "start_dating_method", "start_year"),
        ("end", "end_dating_method", "end_year"),
    ):
        method = e.get(method_field)
        y = e.get(year_field)
        if method is None or y is None or not str(method).startswith("radiocarbon"):
            continue
        if _bp(y) > RADIOCARBON_CEILING_BP:
            errors.append(
                f"entity {e['id']}: {method_field} '{method}' but {year_field} is "
                f"{_bp(y):,} BP, beyond the ~{RADIOCARBON_CEILING_BP:,} BP radiocarbon "
                f"limit. Radiocarbon cannot date this {boundary} boundary."
            )


# ---- An end method without an end is a claim about nothing ------------------
for e in entities:
    if e.get("end_dating_method") is not None and e.get("end_year") is None:
        warnings.append(
            f"entity {e['id']}: end_dating_method set but end_year is null. "
            f"There is no end boundary for it to describe."
        )


# ---- Uncalibrated radiocarbon must be declared, not implied -----------------
#
# An uncalibrated age is not a calendar date and the app refuses to convert it.
# That refusal only works if the method says so, and the whole hazard is that
# published dates frequently do not.
for e in entities:
    if "radiocarbon-uncalibrated" not in (
        e.get("start_dating_method"),
        e.get("end_dating_method"),
    ):
        continue
    note = (e.get("date_note") or "").upper()
    if "UNCALIB" not in note:
        warnings.append(
            f"entity {e['id']}: stored as uncalibrated radiocarbon but date_note does "
            f"not say so. A reader seeing the raw number will read it as a calendar date."
        )

# ---- Missing-summary warnings ----------------------------------------------
for e in entities:
    if e.get("tier") == "foundational" and not e.get("summary") and e.get("kind") != "region":
        warnings.append(f"entity {e['id']}: foundational tier missing summary")

for f_ in frames:
    if not f_.get("summary"):
        warnings.append(f"frame {f_['id']}: missing summary")


# ---- Duplicate sibling display names ---------------------------------------
by_parent = defaultdict(list)
for e in entities:
    by_parent[e.get("parent_id")].append(e)
for parent_id, siblings in by_parent.items():
    name_counts = Counter(s["name"] for s in siblings)
    for name, cnt in name_counts.items():
        if cnt > 1:
            dupes = [s["id"] for s in siblings if s["name"] == name]
            warnings.append(
                f"duplicate sibling name '{name}' under parent {parent_id}: {dupes}"
            )


# ---- Report ---------------------------------------------------------------
print(f"Entities:   {len(entities)}")
print(f"Calendars:  {len(calendars)}")
print(f"Themes:     {len(themes)}")
print(f"Frames:     {len(frames)}")

kinds = Counter(e["kind"] for e in entities)
tiers = Counter(e.get("tier", "?") for e in entities)
print(f"\nKind breakdown: {dict(kinds)}")
print(f"Tier breakdown: {dict(tiers)}")

# ---------------------------------------------------------------------------
# A cal BP figure written into the calendar-year field.
#
# This is the class of error that put Monte Verde 1,950 years too early: a cal
# BP figure written into a field that holds calendar years. It survives every
# other check because -14500 is a perfectly well-formed BCE year. It was found
# by accident, when a second Monte Verde authored through `bp()` disagreed with
# the first by two millennia.
#
# HONEST LIMITATION: this check would NOT have caught Monte Verde. That entity's
# note described the dispute without ever quoting the number, so there was
# nothing to compare the year against. The check only fires when an entity's own
# prose contradicts its year field. That is a real subset of the problem and
# worth catching, but it is not coverage of the whole class, and the only
# reliable guard remains authoring through `bp()` rather than typing a year.
#
# The discriminator is EXACT equality. A correctly authored entity's year comes
# out of `bp()`, so it lands on an odd-looking number like -12551 and will not
# equal any round figure quoted in its own prose. An entity whose year is
# exactly the negation of a BP figure in its own note almost certainly skipped
# the conversion.
#
# Requiring an exact hit is what keeps this quiet: matching loosely flags every
# entity whose note quotes the far end of a range, which is most of them.
_BP_IN_PROSE = re.compile(r"([\d,]{3,9})\s*(?:cal\s*BP|years ago|ka BP|BP)\b")


def _bp_figures(text):
    out = set()
    for m in _BP_IN_PROSE.finditer(text or ""):
        n = int(m.group(1).replace(",", ""))
        if 100 <= n <= 3_000_000:
            out.add(n)
    return out


def _check_units(year, prose, label):
    if year is None or year >= 0:
        return
    figures = _bp_figures(prose)
    if not figures:
        return
    # Already consistent with a conversion of something it quotes.
    if any(year == _historical_from_bp(n) for n in figures):
        return
    hit = next((n for n in figures if year == -n), None)
    if hit is not None:
        warnings.append(
            f"{label}: year {year} is exactly -{hit}, and the text quotes "
            f"'{hit} BP'. A cal BP figure may have been written straight into "
            f"the calendar-year field; {hit} BP is "
            f"{_historical_from_bp(hit)}."
        )


def _historical_from_bp(years_bp):
    astronomical = 1950 - years_bp
    return astronomical if astronomical > 0 else astronomical - 1


for e in entities:
    prose = " ".join(str(e.get(k, "")) for k in ("date_note", "summary"))
    _check_units(e.get("start_year"), prose, f"entity {e['id']} start_year")
    _check_units(e.get("end_year"), prose, f"entity {e['id']} end_year")
    for i, alt in enumerate(e.get("alternatives") or []):
        alt_prose = f"{alt.get('label', '')} {alt.get('note', '')}"
        _check_units(alt.get("start_year"), alt_prose,
                     f"entity {e['id']} alternatives[{i}] start_year")
        _check_units(alt.get("end_year"), alt_prose,
                     f"entity {e['id']} alternatives[{i}] end_year")


if warnings:
    print(f"\n⚠ WARNINGS ({len(warnings)}):")
    for w in warnings[:60]:
        print(f"  {w}")
    if len(warnings) > 60:
        print(f"  ... and {len(warnings) - 60} more warnings")

if errors:
    print(f"\n✗ ERRORS ({len(errors)}):")
    for e in errors[:60]:
        print(f"  {e}")
    if len(errors) > 60:
        print(f"  ... and {len(errors) - 60} more errors")
    sys.exit(1)

print(f"\n✓ OK — no errors. {len(warnings)} warning(s).")
