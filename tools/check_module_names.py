"""Refuse to let a new extension module silently overwrite an existing one.

This exists because the same mistake has now been made twice. An agent wrote
`tools/extensions_americas.py` over a 370-line module that was already there, and
later wrote `tools/extensions_central_asia.py` over a 249-line one. Both were
caught, the first by noticing the diff and the second because the new entities
did not appear in the build -- which is luck, not process. A file write does not
warn you that the name is taken.

The second failure had a quieter half that luck would not have caught: the new
module also declared `CENTRAL_ASIA_SOURCES`, a name the original already used, so
even after the file was restored the two collided at import.

So this checks two things across `tools/`:

1. Every `extensions_*.py` module is imported by `build_data.py`. An orphan
   module is usually the wreckage of an overwrite, or dead code.
2. No name is imported into `build_data.py` from two different modules. That is
   the collision above: it fails at import, and the error names the symbol rather
   than the two files fighting over it.

Only *imported* names are checked. Modules keep private constants like `CHECKED`
and `ROOT` by local convention and those never collide, so flagging them would
bury the real signal in noise -- the first version of this script reported 37
problems of which one was real.

Run before committing new extension modules::

    python3 tools/check_module_names.py
"""

import pathlib
import re
import sys

TOOLS = pathlib.Path(__file__).parent
IMPORT = re.compile(r"^from (\w+) import ([^\n]+)", re.M)


def main() -> int:
    build = (TOOLS / "build_data.py").read_text(encoding="utf-8")
    problems = []

    modules = sorted(p for p in TOOLS.glob("extensions_*.py"))
    for path in modules:
        if f"from {path.stem} import" not in build:
            problems.append(
                f"{path.name} is not imported by build_data.py "
                f"({len(path.read_text(encoding='utf-8').splitlines())} lines). "
                "Either wire it in or delete it -- an orphan module is usually "
                "the remains of an overwrite."
            )

    seen: dict[str, str] = {}
    for mod, names in IMPORT.findall(build):
        for raw in names.split(","):
            name = raw.split("#")[0].strip()
            if " as " in name:
                name = name.split(" as ")[-1].strip()
            if not name:
                continue
            if name in seen and seen[name] != mod:
                problems.append(
                    f"build_data.py imports {name} from both {seen[name]} and {mod}. "
                    "Rename one; the second import silently wins."
                )
            seen.setdefault(name, mod)

    if problems:
        print(f"✗ {len(problems)} problem(s):")
        for p in problems:
            print(f"  {p}")
        return 1
    print(f"✓ {len(modules)} extension modules, all wired in, no constant collisions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
