#!/usr/bin/env python3
"""Assert the committed dataset matches what tools/build_data.py produces.

src/data/*.json is generated output committed for reproducible builds without
Python. If someone hand-edits it, or edits the generator without regenerating,
the two drift silently. This check catches that.

`generated_at` is excluded — it is a timestamp, not content.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "src" / "data"
FILES = ["entities.json", "calendars.json", "themes.json", "reference-frames.json"]
VOLATILE = {"generated_at"}


def strip(obj):
    return {k: v for k, v in obj.items() if k not in VOLATILE}


def main() -> int:
    committed = {f: strip(json.loads((DATA / f).read_text())) for f in FILES}

    with tempfile.TemporaryDirectory() as tmp:
        backup = Path(tmp)
        for f in FILES:
            (backup / f).write_bytes((DATA / f).read_bytes())
        try:
            subprocess.run(
                [sys.executable, str(ROOT / "tools" / "build_data.py")],
                check=True,
                capture_output=True,
            )
            regenerated = {f: strip(json.loads((DATA / f).read_text())) for f in FILES}
        finally:
            for f in FILES:
                (DATA / f).write_bytes((backup / f).read_bytes())

    drifted = [f for f in FILES if committed[f] != regenerated[f]]
    if drifted:
        print("DRIFT: committed src/data does not match tools/build_data.py output:")
        for f in drifted:
            print(f"  - {f}")
        print("\nRun `python3 tools/build_data.py` and commit the result.")
        return 1

    print(f"Dataset reproducible: all {len(FILES)} files match generator output.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
