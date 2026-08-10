"""Delete every uncertainty bound that was computed rather than recorded.

The measurements that forced this, taken across the whole dataset:

- `dated_by` was a perfect function of whether bounds existed. Every method that appeared with
  bounds appeared ONLY with bounds, and every method without appeared ONLY without, in all 3,301
  entities. The field therefore carried no information about evidence; it restated bounds-nullity.
- Bounds were a fixed percentage of the year: 316 entities at exactly 6% of the start year, 241 at
  15%, 112 at 2%, 61 at 25%. That is arithmetic on a magnitude, with no input from any source.
- 2,193 of 2,218 two-sided bounds were exactly symmetric. Real scholarly ranges almost never are.

The consequences were visible to any reader who looked: Kyiv at 482 CE recorded as more precisely
known than Knossos; the sack of Babylon, which its own summary calls the hinge the Bronze Age
chronology turns on, given no bounds at all; the Arab conquest bounded 608 to 658 on a start of
633, where the lower bound predates Islam.

Fabricated uncertainty is worse than absent uncertainty, because a reader seeing plus-or-minus a
century believes somebody measured it. A later sourcing pass will put real intervals on the dates
that warrant them; until then the honest state is silence.

The dating note that announced the convention goes too, and it had been appended twice to some
entities, so the readout printed the same sentence to the reader in succession.
"""

CONVENTION_MARKERS = (
    "magnitude convention",
    "bounds set by magnitude",
    "pending the sourcing pass",
)

BOUND_KEYS = ("start_year_min", "start_year_max", "end_year_min", "end_year_max")


def _is_authored(entity):
    """True when an interval sits off-centre, which the convention generator never produced."""
    for ep in ("start", "end"):
        year = entity.get(f"{ep}_year")
        lo, hi = entity.get(f"{ep}_year_min"), entity.get(f"{ep}_year_max")
        if lo is None and hi is None:
            continue
        # One-sided is authored by definition. The generator only ever emitted a centred pair, so
        # a lower bound standing alone is a terminus post quem somebody meant: the Kenyan stone
        # tools are "at least 3.3 Ma", which is a claim, not a window.
        if lo is None or hi is None:
            return True
        if year is None:
            continue
        if (year - lo) != (hi - year):
            return True
    return False


def _strip_note(text):
    """Remove the convention sentence(s) from a date note, keeping anything else it says."""
    if not text:
        return None
    kept = [
        part.strip()
        for part in text.split(". ")
        if part.strip() and not any(m in part.lower() for m in CONVENTION_MARKERS)
    ]
    if not kept:
        return None
    joined = ". ".join(kept)
    return joined if joined.endswith(".") else joined + "."


def extend(E, entities):
    dropped, notes, kept = 0, 0, 0

    for e in entities:
        if _is_authored(e):
            # Twenty-five intervals survive, and symmetry is what identifies them. The generator
            # could only ever produce a centred plus-or-minus, so an interval that sits off-centre
            # was typed by a person reading a source: Gobekli Tepe at -9530 within -9745 to -9314,
            # the Oldowan at -2600000 within -2620000 to -2540000, and the Aurignacian, Gravettian
            # and Magdalenian ranges. Deleting those would throw away the only real uncertainty
            # data in the file along with the invented kind.
            kept += 1
            continue

        had = [k for k in BOUND_KEYS if e.get(k) is not None]
        if had:
            for k in BOUND_KEYS:
                e.pop(k, None)
            dropped += 1

        cleaned = _strip_note(e.get("date_note"))
        if cleaned != e.get("date_note"):
            if cleaned is None:
                e.pop("date_note", None)
            else:
                e["date_note"] = cleaned
            notes += 1

    print(f"drop_derived_bounds: cleared bounds on {dropped} entities, "
          f"kept {kept} hand-authored interval(s), cleaned {notes} date note(s)")
