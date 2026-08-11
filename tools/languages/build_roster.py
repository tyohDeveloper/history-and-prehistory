"""Join the two tier rosters to Glottolog and apply the inclusion rules.

The two research files disagree about where their dates live, which cost a wrong conclusion once
already: Tier 1 carries `yearsSpoken` in its JSON and nothing in its spreadsheet, while Tier 2
carries Start/End columns in its spreadsheet and nothing in its JSON. Both tiers are fully dated;
neither single format shows it. This module reads dates from whichever file actually has them.

Glottolog 5.3 (CC-BY 4.0) supplies what the rosters cannot:

- `classification` — the full ancestor chain per languoid, which is the evolution hierarchy.
- `level` — family, language or dialect, so "no dialects" is a filter rather than a judgement.
- `Is_Isolate` — a language with no demonstrable relatives, for the standalone category.
- `med` — Most Extensive Description, the documentation depth the speaker rule needs. Note the
  scale is INVERTED: 0 is a long grammar and 4 is a wordlist or less, so poorly documented is high.

Inclusion rules, from the user:
  - no creoles, no dialects
  - drop peak speakers under 10,000 ONLY where documentation is also low; a small language with a
    real grammar stays, which is what keeps Church Slavonic and Medieval Latin (both nominally zero
    speakers, both exhaustively documented) in the roster
  - some things must survive the rule regardless; those are listed rather than guessed at
"""

import csv
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
HP = os.path.dirname(os.path.dirname(HERE))
GLOTTO = os.path.join(HP, "docs/research/glottolog")
ROSTER = os.path.expanduser(
    "/home/user/workspace/memory/sessions/2026-08-10_2026-08-16/1deda0c7/ai_outputs"
)

SPEAKER_FLOOR = 10_000
# med 3 = phonology or text only, 4 = wordlist or less. Both mean nobody has written a grammar.
LOW_DOC_MED = 3

CREOLE = re.compile(r"\bcreole\b|\bpidgin\b|\bpatois\b|papiamento|tok pisin|\bkrio\b", re.I)


def load_glottolog():
    meta = json.load(open(os.path.join(GLOTTO, "meta.json")))
    paths = json.load(open(os.path.join(GLOTTO, "classification.json")))
    ma = json.load(open(os.path.join(GLOTTO, "med_aes.json")))
    med = {k: int(v) for k, v in ma["med"].items()}
    return meta, paths, med


def load_tier1():
    d = json.load(open(os.path.join(ROSTER, "tier1-languages.json")))
    out = []
    for r in d["languages"]:
        ys = r.get("yearsSpoken") or {}
        out.append({
            "roster_id": r["id"],
            "name": r["name"],
            "tier": 1,
            "classification": r["classification"],
            "glottocode": r.get("glottocode"),
            "parent_name": (r.get("descent") or {}).get("parentName"),
            "peak": (r.get("peakSpeakers") or {}).get("estimate"),
            "confidence": (r.get("peakSpeakers") or {}).get("confidence"),
            "area": r.get("areaSpoken"),
            "start_lower": ys.get("startLowerYear"),
            "start_upper": ys.get("startUpperYear"),
            "start_basis": ys.get("startBasis"),
            "end_lower": ys.get("endLowerYear"),
            "end_upper": ys.get("endUpperYear"),
            "end_basis": ys.get("endBasis"),
            "living": bool(ys.get("endIsPresent")),
            "sources": r.get("sources") or [],
        })
    return out


_YEAR = re.compile(r"(\d+)\s*(BCE|CE)", re.I)


def _parse_range(text):
    """'3000 BCE - 1600 CE' -> (-3000, 1600); 'present' -> (None, None); '1930 CE' -> (1930, 1930)."""
    if not text or "present" in str(text).lower():
        return None, None
    found = _YEAR.findall(str(text))
    if not found:
        return None, None
    years = [(-int(n) if era.upper() == "BCE" else int(n)) for n, era in found]
    return years[0], years[-1] if len(years) > 1 else years[0]


def load_tier2():
    import openpyxl
    wb = openpyxl.load_workbook(os.path.join(ROSTER, "Tier-2-Language-Roster.xlsx"), read_only=True)
    ws = wb["All Tier 2"]
    rows = list(ws.iter_rows(min_row=4, values_only=True))
    hdr = list(rows[0])
    idx = {name: hdr.index(name) for name in hdr if name}
    out = []
    for r in rows[1:]:
        name = r[idx["Exemplar"]]
        if not name:
            continue
        sl, su = _parse_range(r[idx["Start (range)"]])
        el, eu = _parse_range(r[idx["End (range)"]])
        living = "present" in str(r[idx["End (range)"]] or "").lower()
        out.append({
            "roster_id": None,
            "name": str(name).strip(),
            "tier": 2,
            "classification": "genus_exemplar",
            "glottocode": r[idx["Glottocode"]],
            "parent_name": r[idx["Parent (Glottolog node)"]],
            "genus": r[idx["Genus"]],
            "peak": r[idx["Peak speakers"]] if isinstance(r[idx["Peak speakers"]], int) else None,
            "confidence": r[idx["Confidence"]],
            "exemplar_rationale": r[idx["Exemplar rationale"]],
            "area": r[idx["Area spoken"]],
            "start_lower": sl, "start_upper": su, "start_basis": r[idx["Start basis"]],
            "end_lower": el, "end_upper": eu, "end_basis": r[idx["End basis"]],
            "living": living,
            "sources": [s for s in str(r[idx["Sources"]] or "").split() if s.startswith("http")],
        })
    return out


def main():
    meta, paths, med = load_glottolog()
    rows = load_tier1() + load_tier2()

    kept, dropped, flagged = [], [], []
    for r in rows:
        gc = r.get("glottocode")
        g = meta.get(gc) if gc else None
        r["glotto_level"] = g["level"] if g else None
        r["isolate"] = bool(g and g["isolate"])
        r["med"] = med.get(gc)
        # Glottolog writes the ancestor chain slash-separated, root first: "indo1319/clas1257/...".
        # Splitting on whitespace left each chain as one opaque string, so 664 of 769 family nodes
        # silently failed to resolve and the tree came out three levels deep instead of twelve.
        r["path"] = [a for a in paths.get(gc, "").split("/") if a] if gc else []

        # All exclusion rules dropped at the user's instruction: every row goes in. The
        # criteria are still evaluated and recorded per row, because they are useful as labels --
        # `is_creole`, `low_documentation`, `below_speaker_floor` -- and because reinstating any
        # of them later should be a filter over this file rather than a re-run of the research.
        #
        # Worth keeping the reason on record: the one rule that looked most mechanical was the
        # most wrong. "No dialects" read as Glottolog's `level == dialect` deleted Biblical Hebrew,
        # Classical Arabic, Vedic Sanskrit, Mycenaean Greek, Medieval Latin, all three stages of
        # Egyptian, and Cantonese, Serbian and Croatian -- 47 rows, not one of them a regional
        # variant. Glottolog's "dialect" means sub-lect of a language-level node, which is where
        # it files historical stages, and those are the whole point of a timeline.
        r["is_creole"] = bool(CREOLE.search(r["name"]))
        r["glotto_dialect"] = r["glotto_level"] == "dialect"
        r["below_speaker_floor"] = isinstance(r.get("peak"), int) and r["peak"] < SPEAKER_FLOOR
        r["low_documentation"] = r.get("med") is not None and r["med"] >= LOW_DOC_MED

        kept.append(r)

    os.makedirs(os.path.join(HP, "docs/research/languages"), exist_ok=True)
    out = os.path.join(HP, "docs/research/languages")
    json.dump(kept, open(os.path.join(out, "kept.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(dropped, open(os.path.join(out, "dropped.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(flagged, open(os.path.join(out, "flagged.json"), "w"), indent=1, ensure_ascii=False)

    print(f"in: {len(rows)}  kept: {len(kept)} (no exclusions applied)")
    print(f"  labelled creole: {sum(1 for k in kept if k['is_creole'])}"
          f" · Glottolog dialect: {sum(1 for k in kept if k['glotto_dialect'])}"
          f" · below speaker floor: {sum(1 for k in kept if k['below_speaker_floor'])}"
          f" · low documentation: {sum(1 for k in kept if k['low_documentation'])}")
    print(f"  isolates among kept: {sum(1 for k in kept if k['isolate'])}")
    print(f"  kept with no Glottolog path: {sum(1 for k in kept if not k['path'])}")
    print(f"  kept with no dates: {sum(1 for k in kept if k['start_lower'] is None)}")


if __name__ == "__main__":
    main()
