"""Shared entity builders for the dataset generators.

Why this module exists
----------------------
`R()` and `P()` were previously defined three separate times, as closures
inside each extension's `extend()` function, each with a hand-written keyword
list::

    def R(slug, name, parent, s, e, tier="specialist", summary=None, aliases=None):

That signature is the whole reason seven schema fields were unused across all
1,305 entities. An author could not populate `date_note`, `sources`,
`calendar_ids` or the uncertainty bounds because the builder physically had
nowhere to put them, and the natural response — adding one more keyword to one
of the three copies — made the divergence worse.

These builders take ``**kw`` and pass it straight through to ``E``, so any
field the schema allows is authorable from anywhere. Unknown keys are rejected
loudly rather than silently dropped, which is the failure mode a passthrough
would otherwise introduce.

See docs/DESIGN.md Q-10 and gap-analysis-v2.1.0.md section 5.1.
"""

import json
from pathlib import Path

# Derived from the schema at import time, so the allowlist cannot drift out of
# sync with what is actually permitted — the failure mode when it was a
# hand-maintained literal. Structural fields E() sets itself are excluded.
#
# The check still happens here rather than at validation time so a typo fails
# where it was written, naming the entity, instead of surfacing later as a JSON
# pointer into a 400 kB generated file.
_SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schemas" / "entity.schema.json"
_STRUCTURAL = {"id", "kind", "name", "parent_id", "start_year", "end_year"}

try:
    with open(_SCHEMA_PATH, encoding="utf-8") as _f:
        ALLOWED_FIELDS = frozenset(json.load(_f)["properties"]) - _STRUCTURAL
        # Authoring shorthands retired from the stored schema but still written by ~30
        # modules. `migrate_dating` converts each into method-and-bounds and strips it, so
        # they never reach the output. Kept accepted here rather than editing 30 modules at
        # once; the validator reports how many remain so this does not become permanent.
        ALLOWED_FIELDS = ALLOWED_FIELDS | {
            "date_precision", "start_precision", "end_precision",
            "standing", "capital", "notable_figures",
        }
except OSError:  # pragma: no cover - schema is committed alongside this file
    ALLOWED_FIELDS = frozenset()



def _check(kw, where):
    unknown = set(kw) - ALLOWED_FIELDS
    if unknown:
        raise TypeError(
            f"{where}: unknown field(s) {sorted(unknown)}. "
            f"Add them to schemas/entity.schema.json and to ALLOWED_FIELDS in "
            f"tools/builders.py, or fix the typo."
        )


def _make_emit(E, id_prefix=None):
    """The shared field-assembling emitter behind every builder.

    Lifted out of ``make_builders`` when the ``city`` kind arrived and needed the
    same behaviour from a separate factory.
    """

    def _emit(kind, slug, name, parent, s, e, tier, summary, aliases, native, kw):
        root = parent if id_prefix is None else id_prefix
        _check(kw, f"{kind} {root}.{slug}")
        fields = dict(kw)
        if summary:
            fields["summary"] = summary
        if aliases:
            fields["aliases"] = aliases
        if native:
            fields["native_name"] = native
        return E(f"{root}.{slug}", kind, name, parent, start=s, end=e, tier=tier, **fields)

    return _emit


def make_builders(E, id_prefix=None):
    """Return (R, P, ERA, EVENT, TAXON, FIRST) bound to an ``E`` entity-emitter.

    ``id_prefix`` overrides where ids are rooted. By default an entity's id is
    ``f"{parent}.{slug}"``, which is what most of the dataset does. Roman
    emperors are the exception: their ids sit flat under ``<rome>.empire``
    while their ``parent_id`` points at whichever dynasty period they belong
    to, so id and parent genuinely diverge there.

    Positional arguments cover the common case; everything else the schema
    allows goes through ``**kw``. ``summary``, ``aliases`` and ``native`` stay
    as named parameters because the existing call sites pass them positionally
    or by those names, and changing that would rewrite 1,305 lines to no
    purpose.
    """

    _emit = _make_emit(E, id_prefix)

    def R(slug, name, parent, s, e, tier="specialist", summary=None, aliases=None,
          native=None, **kw):
        return _emit("reign", slug, name, parent, s, e, tier, summary, aliases, native, kw)

    def P(slug, name, parent, s, e, tier="specialist", summary=None, aliases=None,
          native=None, **kw):
        return _emit("period", slug, name, parent, s, e, tier, summary, aliases, native, kw)

    def ERA(slug, name, parent, s, e, tier="intermediate", summary=None, aliases=None,
            native=None, **kw):
        return _emit("era", slug, name, parent, s, e, tier, summary, aliases, native, kw)

    def EVENT(slug, name, parent, s, e=None, tier="intermediate", summary=None,
              aliases=None, native=None, **kw):
        return _emit("event", slug, name, parent, s, e, tier, summary, aliases, native, kw)

    def TAXON(slug, name, parent, s, e=None, tier="intermediate", summary=None,
              aliases=None, native=None, **kw):
        """A species or population. Not a period: several outlive the eras they
        sit near, and Homo sapiens is extant, so ``e`` defaults to None."""
        return _emit("taxon", slug, name, parent, s, e, tier, summary, aliases, native, kw)

    def FIRST(slug, name, parent, s, tier="intermediate", summary=None,
              aliases=None, native=None, **kw):
        """The earliest known instance of a behaviour.

        A threshold is one-sided. ``s`` is a floor, not an estimate: new
        evidence can only push it older, and the behaviour continues after it.
        So there is no end year to pass, and ``date_precision`` is forced to
        ``minimum`` rather than left to the caller — an "approx" threshold
        would misdescribe the claim being made.
        """
        kw.setdefault("date_precision", "minimum")
        if kw["date_precision"] != "minimum":
            raise ValueError(f"threshold {slug}: date_precision must be 'minimum'")
        return _emit("threshold", slug, name, parent, s, None, tier, summary, aliases, native, kw)

    return R, P, ERA, EVENT, TAXON, FIRST

def make_city_builder(E, id_prefix=None):
    """Return a ``CITY`` builder bound to an ``E`` entity-emitter.

    Deliberately separate from ``make_builders`` rather than a seventh element of
    its return tuple. Forty-two call sites unpack that tuple into exactly six
    names, and widening it to add one kind used by one module would have meant
    editing all forty-two to gain nothing. The cost of the refactor exceeds the
    cost of a second, smaller factory.
    """
    _emit = _make_emit(E, id_prefix)

    def CITY(slug, name, parent, s, e=None, tier="specialist", summary=None,
             aliases=None, native=None, **kw):
        """A city. Not a period, which is why it has its own kind.

        ``e`` defaults to None and that default carries meaning: **a city with no
        end year is inhabited today.** Damascus, Varanasi, Athens and Beijing all
        take the default. Only pass ``e`` for a place that was genuinely abandoned
        and never reoccupied -- Nineveh, Persepolis, Nan Madol, Cahokia.

        Conquest is not an ending and neither is renaming. Constantinople does not
        end in 1453; it becomes Istanbul, which belongs in the summary or an alias,
        not in ``e``. Getting this wrong is the single easiest way for this dataset
        to tell a reader that a living city is dead.
        """
        return _emit("city", slug, name, parent, s, e, tier, summary, aliases, native, kw)

    return CITY
