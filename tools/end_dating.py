"""Per-boundary end dating (Q-30).

Schema 3.0.0 split `dating_method` into `start_dating_method` and
`end_dating_method`. That split creates a question the old shape never had to
answer: what is the END method for the ~110 entities authored when only one
field existed?

Doing nothing is not neutral. The renderer used to apply the single field to
both boundaries, so leaving every end blank would silently delete a true label
from every entity whose boundaries really do share a method -- a Neolithic
culture radiocarbon-dated at both ends is not improved by refusing to say so.

Copying the start method everywhere is also not neutral: that is exactly the
unconditional inheritance Q-30 was raised about, and it is how a radiocarbon
label ended up on dates radiocarbon cannot reach.

So the rule is neither. Propagate only where propagation is PHYSICALLY
POSSIBLE, and leave the rest unset so they read as unrecorded rather than as a
confident wrong answer:

  * `calendar` and `typological` describe how a period as a whole is reckoned,
    not a single measurement, so they carry to the end.
  * `radiocarbon-*` carries only if the end is within radiocarbon's reach.
    Beyond that the carry is the exact error the validator exists to catch.
  * Geochronological methods (argon-argon, luminescence, uranium-series, ESR,
    magnetostratigraphy, potassium-argon, cosmogenic) carry only if the end is
    ALSO beyond radiocarbon range. If the end sits inside radiocarbon range the
    end was almost certainly dated some other way, and guessing which is
    research, not derivation -- so it is left unset.
  * `unknown` and `layer-counting` are never derived.

The difference from the old behaviour is not subtlety, it is auditability: this
runs once, writes a real value into the dataset, and the validator then
re-checks that value independently. Silent inheritance in the render layer
could never be checked, because there was nothing stored to check.

EXPLICIT_END_METHODS holds the cases where the end is documented as resting on
different science from the start. Each is grounded in the entity's own
date_note and cited sources, not inferred here.
"""

RADIOCARBON_CEILING_BP = 55_000

CARRIES_ALWAYS = {"calendar", "typological"}
GEOCHRONOLOGICAL = {
    "argon-argon",
    "potassium-argon",
    "luminescence",
    "uranium-series",
    "esr",
    "magnetostratigraphy",
    "cosmogenic",
}
NEVER_DERIVED = {"unknown", "layer-counting"}

# Ends that rest on different science from their start. Grounded in each
# entity's existing date_note and source_ids -- see the note text quoted.
EXPLICIT_END_METHODS = {
    # "The end is the 41,030-39,260 cal BP Mousterian boundary, which IS
    # radiocarbon -- the two ends of this range rest on different methods."
    # This is the entity Q-30 was written about.
    "europe.prehistory.neanderthal-europe": "radiocarbon-calibrated",
    # "Radiocarbon only reaches the terminal MSA; everything older rests on
    # OSL, TL, ESR and uranium-series."
    "global.paleolithic.middle-stone-age": "radiocarbon-calibrated",
}

# Ends deliberately left unset, with the reason, so a later pass does not
# "helpfully" fill them in. A floor is not an end.
DELIBERATELY_UNSET = {
    "africa.prehistory.klasies-river": (
        "The top of the MSA sequence is beyond the radiocarbon limit, so 50 ka "
        "is a floor rather than a dated end. No method dated it."
    ),
    "oceania.australia.aboriginal.sahul": (
        "The end is a sea-level event (Bass Strait flooding), not a dated "
        "archaeological boundary."
    ),
}


def _bp(historical_year):
    return 1950 - (historical_year + 1 if historical_year < 0 else historical_year)


def apply_end_dating_methods(entities):
    """Fill end_dating_method in place. Returns (explicit, derived, left_unset)."""
    explicit = derived = unset = 0
    for e in entities:
        if e.get("end_dating_method") is not None:
            explicit += 1
            continue

        override = EXPLICIT_END_METHODS.get(e["id"])
        if override is not None:
            e["end_dating_method"] = override
            explicit += 1
            continue

        start_method = e.get("start_dating_method")
        end_year = e.get("end_year")
        if start_method is None or end_year is None:
            continue
        if e["id"] in DELIBERATELY_UNSET or start_method in NEVER_DERIVED:
            unset += 1
            continue

        end_bp = _bp(end_year)
        carries = (
            start_method in CARRIES_ALWAYS
            or (start_method.startswith("radiocarbon") and end_bp <= RADIOCARBON_CEILING_BP)
            or (start_method in GEOCHRONOLOGICAL and end_bp > RADIOCARBON_CEILING_BP)
        )
        if carries:
            e["end_dating_method"] = start_method
            derived += 1
        else:
            unset += 1
    return explicit, derived, unset
