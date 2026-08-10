"""Author rulers from researched JSON, for polities that had none.

Reign coverage was wildly uneven — south-asia 159, east-asia 154, africa 152, europe 137,
but west-asia 19, americas 8, central-asia 7, southeast-asia 3, oceania 2. Inside the
well-covered regions it was still patchy: the **Roman Kingdom had no children at all**,
none of the seven traditional kings, and the **Republic had three period nodes and not one
person**. Korea had ten dynasties and zero rulers.

This module reads `docs/research/*.json` produced by the research briefs in
`docs/briefs/` and authors reigns from it. Keeping the researched facts in data files
rather than inline in Python means the citations stay auditable against what was actually
found, and a re-run cannot quietly drift from the source.

Two editorial decisions are encoded here rather than left to the research.

**The Republic is not a reign sequence.** Five hundred years of paired annual consuls is
roughly a thousand magistrates, which is not what a reader wants and would bury the
twelve people who actually changed the Republic's direction. So Republic figures are
authored as selected notable figures with their years of office or command, and each
carries a `role` note saying what capacity they held. `kind: "reign"` is used because it
is what the schema has, but the summary and the role note both make clear these were
magistrates, not monarchs — the missing `subkind` field would have covered this properly.

**Legendary sequences stay legendary.** The seven kings of Rome come from Livy and
Dionysius writing centuries after the fact, with reign lengths that look schematic. They
are authored with `date_precision: traditional` and `received` dating, so they lead with
the dagger marker and read as convention rather than finding — the same treatment given to
Gojoseon's Dangun date and the Chinese Five Emperors.
"""

from __future__ import annotations

import json
import pathlib

RESEARCH = pathlib.Path(__file__).resolve().parent.parent / "docs" / "research"

# Where each researched group is filed. A missing key is an error rather than a skip:
# a silent skip is how an entire authored block once vanished while the summary line
# still reported success.
ROME_KINGDOM = "europe.mediterranean.rome.kingdom"
ROME_REPUBLIC = "europe.mediterranean.rome.republic"

KOREA_PARENTS = {
    "gojoseon": "east-asia.korea.gojoseon",
    "three-kingdoms": "east-asia.korea.three-kingdoms",
    "unified-silla": "east-asia.korea.unified-silla",
    "goryeo": "east-asia.korea.goryeo",
    "joseon": "east-asia.korea.joseon",
}

# Source kinds the schema allows, mapped from what the research reports.
KIND_MAP = {
    "reference": "reference",
    "institutional": "institutional",
    "scholarly": "scholarly",
    "museum": "institutional",
    "university": "institutional",
    "encyclopaedia": "reference",
    "encyclopedia": "reference",
    "wikipedia": "reference",
}


# Populated by extend(). build_data.py registers this after the module has run, which is
# safe because every sources.extend() call there happens after the extend() calls.
RESEARCH_REIGN_SOURCES: list[dict] = []


def _load(name: str):
    path = RESEARCH / name
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _sources_from(rows, prefix: str):
    """Collect the distinct sources the research cited, keyed deterministically."""
    seen: dict[str, dict] = {}
    for row in rows:
        src = row.get("source")
        if not src or not src.get("url"):
            continue
        url = src["url"]
        if url in seen:
            continue
        sid = f"{prefix}-{len(seen) + 1:02d}"
        note = (src.get("note") or row.get("date_agreement") or "").strip()
        if len(note) > 240:
            note = note[:237] + "..."
        seen[url] = {
            "id": sid,
            "kind": KIND_MAP.get((src.get("kind") or "reference").lower(), "reference"),
            "citation": src["citation"],
            "url": url,
            **({"note": note} if note else {}),
        }
    return seen


# Titles are not names. "King Sejong the Great" and "Sejong the Great" are one person.
_TITLES = {
    "king", "queen", "emperor", "empress", "prince", "princess", "shah", "sultan",
    "caliph", "tsar", "czar", "duke", "khan", "pharaoh", "lord", "lady", "saint",
    "the", "of", "and",
}


def _tokens(name: str) -> set[str]:
    import re
    import unicodedata
    flat = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    return {w for w in re.findall(r"[a-z]+", flat) if w not in _TITLES}


def _find_existing(row, parent, entities, by_top):
    """Return an existing entity for this person, or None.

    This exists because the audit that motivated the whole pass was wrong. It reported
    that the Roman Republic had "three period nodes and not one person" and that Korea had
    "ten dynasties and zero rulers". Both were false: Julius Caesar was already filed under
    `rome.republic.late`, one level deeper than the direct-children check looked, and King
    Sejong the Great was already under Joseon. Authoring from that audit created two
    duplicate people before this guard existed.

    Matching is deliberately narrow -- every significant token of the shorter name must
    appear in the longer one, AND the date ranges must overlap, AND both must sit in the
    same top-level region. Name similarity alone is far too loose: Romulus collides with
    Romulus Augustulus and Tiberius Gracchus with the emperor Tiberius, and only the date
    check separates them.
    """
    want = _tokens(row["name"])
    if not want:
        return None
    region = by_top.get(parent)
    lo, hi = row["start_year"], row["end_year"]
    for cand in entities:
        if cand["kind"] != "reign" or by_top.get(cand["id"]) != region:
            continue
        have = _tokens(cand["name"])
        if not have:
            continue
        if not (want <= have or have <= want):
            continue
        cs, ce = cand.get("start_year"), cand.get("end_year")
        if cs is None or ce is None:
            continue
        if lo < ce and cs < hi or (lo == hi and cs <= lo <= ce):
            return cand
    return None


def _fold_across_polities(rows, parents):
    """One person whose reign straddles two polities becomes one entity, not two.

    The Korea research returned Munmu of Silla twice: 661-668 under the Three Kingdoms
    and 668-681 under Unified Silla. That is not two people. He completed the unification
    in 668, so his single reign genuinely spans the boundary, and splitting him in two
    would make the dataset assert that Silla had two kings of the same name in sequence.

    Folded into one entity spanning both, filed under the polity where the reign began,
    with `cross_parent_ids` pointing at the other so it is reachable from both branches.
    That is what `cross_parent_ids` is for -- a strict tree cannot say "this belongs in two
    places", and until now only one reign in the entire dataset used it.
    """
    groups: dict[str, list[dict]] = {}
    for row in rows:
        groups.setdefault(row["name"], []).append(row)

    folded, notes = [], []
    for name, members in groups.items():
        if len(members) == 1:
            folded.append(members[0])
            continue
        members.sort(key=lambda r: r["start_year"])
        first, rest = members[0], members[1:]
        merged = dict(first)
        merged["end_year"] = max(m["end_year"] for m in members)
        merged["cross_parent_ids"] = [parents[m["polity"]] for m in rest
                                      if m.get("polity") in parents]
        # The folded span necessarily outlasts the polity the reign began in -- that is
        # the whole reason the fold is needed, not a defect.
        merged["allow_outside_parent_dates"] = True
        spans = ", ".join(f"{m['polity']} {m['start_year']}-{m['end_year']}"
                          for m in members)
        merged["_fold_note"] = (
            f"One reign spanning {len(members)} periods in this dataset ({spans}), "
            f"authored once and reachable from both.")
        folded.append(merged)
        notes.append(f"{name} folded across {len(members)} polities")
    return folded, notes


def _emit_rows(R, rows, parent, url_to_sid, *, legendary: bool, tier: str,
              entities=None, by_top=None, enriched=None):
    made = 0
    for row in rows:
        # Enrich, never duplicate. A second Julius Caesar is worse than no new Caesar.
        if entities is not None:
            existing = _find_existing(row, parent, entities, by_top)
            if existing is not None:
                sid = url_to_sid.get((row.get("source") or {}).get("url"))
                if sid is not None:
                    existing["source_ids"] = sorted(
                        set(existing.get("source_ids", [])) | {sid})
                if not (existing.get("summary") or "").strip() and row.get("summary"):
                    existing["summary"] = row["summary"]
                if row.get("aliases"):
                    existing["aliases"] = sorted(
                        set(existing.get("aliases", [])) | set(row["aliases"]))
                if enriched is not None:
                    enriched.append(f"{row['name']} -> existing {existing['id']}")
                continue
        src = row.get("source") or {}
        sid = url_to_sid.get(src.get("url"))
        # A row with no source is authored anyway. Two thirds of this dataset carries no
        # citation and the readout says so on the entity; dropping a real figure for want
        # of a URL would hide the gap instead of showing it.
        kw: dict = {"source_ids": [sid]} if sid is not None else {}
        precision = row.get("date_precision") or ("traditional" if legendary else "approx")
        kw["date_precision"] = precision
        if precision == "traditional":
            # `received` makes the readout lead with the dagger and the
            # "convention, not a finding" banner, which is the honest presentation.
            kw["start_dating_method"] = "received"
            kw["end_dating_method"] = "received"
            kw["standing"] = "traditional"

        caveats = []
        contested = (row.get("contested") or "").strip()
        # A research brief tells the researcher to omit a field when it does not apply, and one
        # wrote the word "omit" into the field instead of leaving it out. Taken literally, that
        # produced eleven caveats of kind `contested-existence` whose entire text was "omit" --
        # on Cicero, Pompey, Sulla and Marius, asserting to the reader that their existence is
        # in doubt. It shipped, because a four-character string is structurally valid.
        #
        # Any importer reading human-written JSON needs this: the sentinels a writer reaches for
        # to mean "nothing here" are not content.
        if contested.lower() in ("omit", "none", "n/a", "na", "tbd", "-", "null", "false"):
            contested = ""
        if contested:
            if len(contested) > 200:
                contested = contested[:197] + "..."
            caveats.append({"kind": "contested-existence", "text": contested,
                            "source_ids": [sid]})
        if caveats:
            kw["caveats"] = caveats

        # Republic figures were magistrates, not monarchs. Say so in the record.
        role = (row.get("role") or "").strip()
        notes = []
        if role:
            notes.append(f"Held office as {role}; dates are of office or command, not "
                         f"of birth and death.")
        agreement = (row.get("date_agreement") or "").strip()
        if agreement and not agreement.lower().startswith("matches"):
            notes.append(agreement)
        fold = (row.get("_fold_note") or "").strip()
        if fold:
            notes.append(fold)
        if row.get("cross_parent_ids"):
            kw["cross_parent_ids"] = row["cross_parent_ids"]
        if row.get("allow_outside_parent_dates"):
            kw["allow_outside_parent_dates"] = True
        if notes:
            kw["date_note"] = " ".join(notes)

        R(row["slug"], row["name"], parent,
          row["start_year"], row["end_year"], tier,
          summary=row.get("summary"),
          aliases=row.get("aliases") or None,
          native=row.get("native") or None,
          **kw)
        made += 1
    return made


def extend(E, entities):
    from builders import make_builders

    by_id = {e["id"]: e for e in entities}
    total = 0
    all_sources: list[dict] = []
    enriched: list[str] = []

    def _top(eid):
        cur = by_id.get(eid)
        while cur is not None and cur.get("parent_id") is not None:
            cur = by_id.get(cur["parent_id"])
        return cur["id"] if cur is not None else None

    by_top = {e["id"]: _top(e["id"]) for e in entities}

    # ── Rome ────────────────────────────────────────────────────────────────
    rome = _load("rome.json")
    if rome is not None:
        rows = (rome if isinstance(rome, list)
                else rome.get("rulers") or rome.get("entries", []))
        # Split on the traditional founding of the Republic. Every king reigned before
        # -509 and every Republic figure held office after it, so this needs no extra
        # field from the research and cannot silently misfile anyone.
        kings = [r for r in rows if r["start_year"] < -509]
        republic = [r for r in rows if r["start_year"] >= -509]
        assert len(kings) + len(republic) == len(rows)
        for required in (ROME_KINGDOM, ROME_REPUBLIC):
            if required not in by_id:
                raise KeyError(f"reigns_from_research: {required} not found")

        srcs = _sources_from(rows, "rome-rulers")
        all_sources += list(srcs.values())
        url_to_sid = {u: s["id"] for u, s in srcs.items()}

        Rk, _, _, _, _, _ = make_builders(E, id_prefix=ROME_KINGDOM)
        total += _emit_rows(Rk, kings, ROME_KINGDOM, url_to_sid,
                            legendary=True, tier="intermediate",
                            entities=entities, by_top=by_top, enriched=enriched)
        Rr, _, _, _, _, _ = make_builders(E, id_prefix=ROME_REPUBLIC)
        total += _emit_rows(Rr, republic, ROME_REPUBLIC, url_to_sid,
                            legendary=False, tier="intermediate",
                            entities=entities, by_top=by_top, enriched=enriched)

    # ── Korea ───────────────────────────────────────────────────────────────
    korea = _load("korea.json")
    if korea is not None:
        rows = (korea if isinstance(korea, list)
                else korea.get("rulers") or korea.get("entries", []))
        srcs = _sources_from(rows, "korea-rulers")
        all_sources += list(srcs.values())
        url_to_sid = {u: s["id"] for u, s in srcs.items()}
        rows, fold_notes = _fold_across_polities(rows, KOREA_PARENTS)
        for note in fold_notes:
            print(f"  {note}")
        for group, parent in KOREA_PARENTS.items():
            if parent not in by_id:
                raise KeyError(f"reigns_from_research: {parent} not found")
            group_rows = [r for r in rows if r.get("polity") == group]
            if not group_rows:
                continue
            Rg, _, _, _, _, _ = make_builders(E, id_prefix=parent)
            total += _emit_rows(Rg, group_rows, parent, url_to_sid,
                                legendary=False, tier="intermediate",
                                entities=entities, by_top=by_top, enriched=enriched)

    for line in enriched:
        print(f"  already present, enriched instead: {line}")

    RESEARCH_REIGN_SOURCES.clear()
    RESEARCH_REIGN_SOURCES.extend(all_sources)
    print(f"Reigns from research: {total} rulers authored, "
          f"{len(all_sources)} sources")
