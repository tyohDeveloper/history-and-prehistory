"""Show and update the pinned test baselines, so they stop being transcribed by hand.

Sixteen numbers are pinned across the two test files -- entity count, cited count,
dating-method counts, region count, the dataset and app versions. **The brittleness
is deliberate and stays.** A pinned count is a tripwire: it forces you to notice
when a pass changed more than it meant to, and several real problems have been
caught by exactly that.

The *transcription* is the risk, and it has misfired twice:

* One release set the `cited` baseline to 620, because that was the number a
  throwaway script printed -- but the test counts *entities carrying a source*, not
  *distinct sources cited*, and the right answer was 440.
* Another set the `end_dating_method` count to 332 when the pass had added no end
  methods at all, on a misread of an unrelated figure. The real value was unchanged
  at 328.

Both failed loudly and were fixed. The failure that does **not** announce itself is
a baseline set to a wrong-but-passing value, which silently disables the tripwire
it exists to be. That is what this removes: the judgement stays human, the
arithmetic stops being manual, and a baseline change shows up in `git diff` as a
reviewable line instead of a number typed from memory.

    python3 tools/baselines.py            # print committed vs current
    python3 tools/baselines.py --update   # rewrite the drifted ones

**It refuses to write when a pattern does not match.** A silent no-op edit is how a
validator rule got "tested" earlier in this project while never actually being in
the file, so a missing anchor is a hard error here rather than a skipped entry.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "src" / "data"
UNIT = ROOT / "tests" / "dataset-integrity.test.ts"
E2E = ROOT / "tests" / "e2e" / "picker.e2e.ts"


def _json(name: str):
    with open(DATA / name, encoding="utf-8") as fh:
        return json.load(fh)


def _load():
    ents = _json("entities.json")
    with open(ROOT / "package.json", encoding="utf-8") as fh:
        pkg = json.load(fh)
    return {
        "entities": ents["entities"],
        "dataset_version": ents["dataset_version"],
        "schema_version": ents["schema_version"],
        "app_version": pkg["version"],
        "calendars": _json("calendars.json")["calendars"],
        "themes": _json("themes.json")["themes"],
        "frames": _json("reference-frames.json")["frames"],
    }


def _n(pred):
    return lambda d: str(sum(1 for e in d["entities"] if pred(e)))


# Each entry pairs ONE regex with exactly one capture group -- the pinned value --
# against a function computing the truth. The regex is the contract: if it stops
# matching, the tool fails rather than quietly skipping the baseline.
BASELINES: list[dict] = [
    {"name": "datasetVersion", "file": UNIT,
     "re": r'expect\(datasetVersion\)\.toBe\("([^"]+)"\)',
     "get": lambda d: d["dataset_version"]},
    {"name": "schemaVersion", "file": UNIT,
     "re": r'expect\(schemaVersion\)\.toBe\("([^"]+)"\)',
     "get": lambda d: d["schema_version"]},
    {"name": "entity count", "file": UNIT,
     "re": r"expect\(entities\.length\)\.toBe\((\d+)\)",
     "get": lambda d: str(len(d["entities"]))},
    {"name": "calendar count", "file": UNIT,
     "re": r"expect\(calendars\.length\)\.toBe\((\d+)\)",
     "get": lambda d: str(len(d["calendars"]))},
    {"name": "theme count", "file": UNIT,
     "re": r"expect\(themes\.length\)\.toBe\((\d+)\)",
     "get": lambda d: str(len(d["themes"]))},
    {"name": "reference frames", "file": UNIT,
     "re": r"expect\(referenceFrames\.length\)\.toBe\((\d+)\)",
     "get": lambda d: str(len(d["frames"]))},
    # Named to say what it measures, because misreading this one is what produced
    # the 620-instead-of-440 error: it counts ENTITIES that carry a source, not
    # distinct sources cited.
    {"name": "entities carrying a source", "file": UNIT,
     "re": r"expect\(cited\.length\)\.toBe\((\d+)\)",
     "get": _n(lambda e: bool(e.get("source_ids")))},
    {"name": "start_dating_method set", "file": UNIT,
     "re": r"e\.start_dating_method !== undefined\)\.length\)\.toBe\((\d+)\)",
     "get": _n(lambda e: e.get("start_dating_method") is not None)},
    {"name": "start_year_min set", "file": UNIT,
     "re": r"e\.start_year_min !== undefined\)\.length\)\.toBe\((\d+)\)",
     "get": _n(lambda e: e.get("start_year_min") is not None)},
    {"name": "end_dating_method set", "file": UNIT,
     "re": r"expect\(withEnd\.length\)\.toBe\((\d+)\)",
     "get": _n(lambda e: e.get("end_dating_method") is not None)},
    {"name": "entities with calendars", "file": UNIT,
     "re": r"e\.calendar_ids\?\.length \?\? 0\) > 0\)\.length\)\.toBe\((\d+)\)",
     "get": _n(lambda e: len(e.get("calendar_ids") or []) > 0)},
    {"name": "region count", "file": UNIT,
     "re": r"expect\(regions\.length\)\.toBe\((\d+)\)",
     "get": _n(lambda e: e["kind"] == "region")},
    {"name": "app version (e2e)", "file": E2E,
     "re": r'toContainText\("v([0-9.]+)"\)',
     "get": lambda d: d["app_version"]},
    {"name": "dataset version (e2e)", "file": E2E,
     "re": r'toContainText\("data ([0-9.]+)"\)',
     "get": lambda d: d["dataset_version"]},
    {"name": "entity count (e2e footer)", "file": E2E,
     "re": r'toContainText\("([\d,]+) entities"\)',
     "get": lambda d: f"{len(d['entities']):,}"},
]

# Deliberately NOT automated: `sp.length` (the split-dating-method catalogue) is a
# hand-curated registry whose whole point is that a human decides what belongs in
# it. Computing it here would defeat it. Same for the gap-analysis counts, which
# are assertions about known debt rather than measurements of the current build.
EXCLUDED = {
    "split-dating-method catalogue (tests/dataset-integrity.test.ts, sp.length)":
        "hand-curated registry; a human decides membership",
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--update", action="store_true",
                    help="rewrite baselines that have drifted")
    args = ap.parse_args()

    data = _load()
    texts = {UNIT: UNIT.read_text(encoding="utf-8"),
             E2E: E2E.read_text(encoding="utf-8")}

    missing = [b["name"] for b in BASELINES
               if re.search(b["re"], texts[b["file"]]) is None]
    if missing:
        print("✗ pattern did not match, refusing to continue:")
        for name in missing:
            print(f"    {name}")
        print("\n  A baseline whose anchor has moved must be fixed by hand. Skipping "
              "it silently is how an edit becomes a no-op.")
        return 2

    drift = []
    print(f"{'baseline':32} {'committed':>12} {'current':>12}")
    print("-" * 60)
    for b in BASELINES:
        m = re.search(b["re"], texts[b["file"]])
        assert m is not None
        committed, current = m.group(1), b["get"](data)
        flag = "" if committed == current else "  <-- drift"
        print(f"  {b['name']:30} {committed:>12} {current:>12}{flag}")
        if committed != current:
            drift.append((b, committed, current))

    if not drift:
        print("\n✓ all baselines match the current build.")
        return 0

    if not args.update:
        print(f"\n{len(drift)} baseline(s) have drifted. Review the numbers above, "
              f"then run with --update.")
        return 1

    for b, committed, current in drift:
        text = texts[b["file"]]
        m = re.search(b["re"], text)
        assert m is not None
        start, end = m.span(1)
        texts[b["file"]] = text[:start] + current + text[end:]
    for path, text in texts.items():
        path.write_text(text, encoding="utf-8")
    print(f"\n✓ updated {len(drift)} baseline(s). Check `git diff` before committing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
