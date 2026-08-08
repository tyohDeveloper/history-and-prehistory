#!/usr/bin/env python3
"""Measure the codebase against docs/CODING-STANDARDS.md §3.

Reports rather than gates, for now. The point of the first run is to size the
compliance debt honestly instead of scoping a checker around the part that
already passes, which §16.1 calls out by name.

Layer roles come from §0 of that document, which each repository fills in for
its own paths.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

# §0 path mapping. Order matters: the most specific prefix wins.
#
# This table went stale the moment src/lib was dismantled, and the checker
# silently stopped classifying most of the tree - the violation count fell from
# 20 to 8 with no code improved. That is §16.1 happening to the tool written to
# enforce §16.1: enforcement that quietly narrows its own coverage is not
# enforcement. Keep this in step with §0 of docs/CODING-STANDARDS.md.
LAYERS = [
    ("PURE-CORE", ("src/calendars/", "src/chrono/", "src/temporal/"), 100),
    ("PURE", ("src/entity/", "src/dataset/", "src/research/"), 150),
]
VIEW_LIMIT = 250


FUNC_LIMIT = 20


def layer_of(rel: str) -> tuple[str, int]:
    for name, prefixes, limit in LAYERS:
        if any(rel.startswith(p) for p in prefixes):
            return name, limit
    # VIEW is top-level src/*.ts only. A file one level down belongs to a
    # domain, and an unrecognised domain is a mapping gap worth surfacing
    # rather than a file to wave through.
    if rel.startswith("src/"):
        rest = rel[len("src/"):]
        return ("VIEW", VIEW_LIMIT) if "/" not in rest else ("UNMAPPED-DOMAIN", 150)
    return "UNMAPPED", 10**9


def countable_lines(text: str) -> int:
    """Lines that count toward §3.3. Comment-only lines do not."""
    n = 0
    in_block = False
    for raw in text.splitlines():
        s = raw.strip()
        if in_block:
            if "*/" in s:
                in_block = False
            continue
        if s.startswith("/*"):
            if "*/" not in s:
                in_block = True
            continue
        if not s or s.startswith("//"):
            continue
        n += 1
    return n


def exported_function_bodies(text: str) -> list[tuple[str, int]]:
    """(name, body_line_count) for each `export function`, excluding comments."""
    out: list[tuple[str, int]] = []
    lines = text.splitlines()
    for i, raw in enumerate(lines):
        m = re.match(r"\s*export\s+(?:async\s+)?function\s+(\w+)", raw)
        if not m:
            continue
        depth = 0
        started = False
        body: list[str] = []
        for line in lines[i:]:
            depth += line.count("{") - line.count("}")
            if not started and "{" in line:
                started = True
                continue
            if started:
                if depth <= 0:
                    break
                body.append(line)
        out.append((m.group(1), countable_lines("\n".join(body))))
    return out


# Rule 3.8 prohibits names that describe a file's SHAPE rather than what it
# owns, "including as leaf names inside an otherwise well-named directory".
SHAPE_NAMES = {
    "helpers", "utils", "misc", "common", "shared", "handlers", "setters",
    "getters", "stuff", "things", "lib", "index", "types", "useHelpers",
    "useHandlers", "useSetters",
}

RE_EXPORT = re.compile(r"^\s*export\s+(?:\*|type\s*\{|\{)")
EXCEPTION_TAG = re.compile(r"EXCEPTION \[coding-standards §3\.[89]\]")


def shape_named_paths() -> list[tuple[str, str]]:
    """Files and directories under src/ named for shape instead of domain."""
    out: list[tuple[str, str]] = []
    for path in sorted(SRC.rglob("*")):
        if path.name.startswith("."):
            continue
        stem = path.stem if path.is_file() else path.name
        if stem in SHAPE_NAMES:
            rel = path.relative_to(ROOT).as_posix()
            kind = "file" if path.is_file() else "directory"
            out.append((rel, kind))
    return out


def barrel_files() -> list[tuple[str, int, int]]:
    """(path, re_export_count, substantive_lines) for un-excepted barrels.

    A single-symbol source-selection shim is a permitted exception, but only
    when it carries the EXCEPTION tag - otherwise the carve-out is indis-
    tinguishable from an oversight.
    """
    out: list[tuple[str, int, int]] = []
    for path in sorted(SRC.rglob("*.ts")):
        text = path.read_text(encoding="utf-8")
        if EXCEPTION_TAG.search(text):
            continue
        reexports = sum(1 for line in text.splitlines() if RE_EXPORT.match(line))
        if reexports == 0:
            continue
        out.append((path.relative_to(ROOT).as_posix(), reexports, countable_lines(text)))
    return out


def main() -> int:
    file_rows: list[tuple[str, str, int, int]] = []
    func_rows: list[tuple[str, str, int]] = []
    export_rows: list[tuple[str, int, list[str]]] = []

    for path in sorted(SRC.rglob("*.ts")):
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        layer, limit = layer_of(rel)
        n = countable_lines(text)
        if n > limit:
            file_rows.append((rel, layer, n, limit))
        for name, body in exported_function_bodies(text):
            if body > FUNC_LIMIT:
                func_rows.append((rel, name, body))
        if layer.startswith("PURE"):
            fns = re.findall(r"^export\s+(?:async\s+)?function\s+(\w+)", text, re.M)
            if len(fns) > 1:
                export_rows.append((rel, len(fns), fns))

    print("=" * 72)
    print("RULE 3.3 — file length by layer role")
    print("=" * 72)
    for rel, layer, n, limit in sorted(file_rows, key=lambda r: r[3] - r[2]):
        print(f"  {rel:44} {layer:10} {n:5} / {limit}   over by {n - limit}")
    print(f"  -> {len(file_rows)} files over limit")

    print()
    print("=" * 72)
    print(f"RULE 3.1 — exported function body <= {FUNC_LIMIT} lines")
    print("=" * 72)
    for rel, name, body in sorted(func_rows, key=lambda r: -r[2])[:15]:
        print(f"  {rel:40} {name:26} {body:4} lines")
    print(f"  -> {len(func_rows)} exported functions over limit")

    print()
    print("=" * 72)
    print("RULE 3.2 — one exported function per PURE file")
    print("=" * 72)
    for rel, count, fns in sorted(export_rows, key=lambda r: -r[1])[:12]:
        print(f"  {rel:44} {count:3} exports  e.g. {', '.join(fns[:3])}")
    print(f"  -> {len(export_rows)} PURE files with more than one function export")

    shape = shape_named_paths()
    print()
    print("=" * 72)
    print("RULE 3.8 — name for responsibility, not shape")
    print("=" * 72)
    for rel, kind in shape:
        print(f"  {rel:44} {kind}")
    print(f"  -> {len(shape)} shape-named paths")

    barrels = barrel_files()
    print()
    print("=" * 72)
    print("RULE 3.9 — no barrel files (untagged)")
    print("=" * 72)
    for rel, n, total_lines in barrels:
        print(f"  {rel:44} {n} re-export(s) in {total_lines} lines")
    print(f"  -> {len(barrels)} untagged re-exporting files")

    total = len(file_rows) + len(func_rows) + len(export_rows) + len(shape) + len(barrels)
    print()
    print(f"TOTAL §3 violations: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
