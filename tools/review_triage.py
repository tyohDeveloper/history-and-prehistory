"""Apply the corrections from the six-way correctness review that are not judgement calls.

The review found far more than this module fixes. What is here is the subset where the data
contradicts itself, so no historical opinion is needed to see the error:

1. **Fifty-seven entities of kind `city` whose own summary says they are not cities.** Delphi,
   Olympia, Nemea, Epidaurus, Eleusis and Isthmia are Panhellenic sanctuaries; My Son is a temple
   valley; Konark is a temple; Honaunau is a place of refuge; Moundville is a mound centre. The
   authoring pass took an enumeration of "important places" and filed all of them as cities. They
   now take a new kind, `site` -- a place that mattered without being a town.

2. **Fifty-one Japanese nengo carrying a fabricated plus-or-minus 25 years and `dated_by: unknown`.**
   A nengo is a proclaimed calendar era recorded in court documents; its dates are exact. Shucho
   lasted three months in 686 and was given a window of 661 to 711. The remaining 197 Japanese rows
   are correctly `calendar` with no bounds, so the file contradicted itself.

3. **The Netherlands filed as kind `reign`** -- a country recorded as a person's tenure, with the
   Dutch East India Company beneath it.

Everything else from the review needs a decision and is deliberately left alone.
"""

import re

# A summary that denies its own kind. Matched against `city` rows only.
_DENIES_CITY = re.compile(
    r"not (?:a|an) (?:city|urban|town|settlement)|rather than a (?:true )?city"
    r"|was not urban|not itself a city|sanctuary, not|monument and port shrine"
    r"|a sanctuary complex, not|and games site rather than",
    re.I,
)

# Rows whose summary does not say "not a city" in so many words but which are plainly not towns.
FORCE_SITE = {
    "americas.city-moundville",
    "americas.city-etowah",
    "americas.city-spiro",
    "oceania.city-honaunau",
    "south-asia.city-konark",
    "southeast-asia.city-myson",
    # These four say it plainly, but in wording the pattern above does not reach. Note that most
    # rows mentioning a sanctuary ARE cities that happen to contain one -- Cerveteri, Praeneste,
    # Mecca, Aquae Sulis -- and are deliberately left as cities.
    "europe.city-dodona",           # "sanctuary rather than city"
    "europe.city-pantalica",        # a rock-cut necropolis
    "west-asia.city-shiloh",        # a pre-monarchic sanctuary
    "west-asia.city-takht-e-soleyman",  # "largely ceremonial"
}

FORCE_KIND = {
    "europe.western.netherlands": "polity",
}


def _is_nengo(entity):
    """A Japanese court era: proclaimed, documented, and exactly dated."""
    return (
        entity["kind"] == "period"
        and entity["id"].startswith("east-asia.japan.")
        and (entity.get("start_year") or 0) >= 500
    )


def extend(E, entities):
    to_site, unbounded, rekinded = [], [], []

    for e in entities:
        if e["kind"] == "city" and (
            _DENIES_CITY.search(e.get("summary") or "") or e["id"] in FORCE_SITE
        ):
            e["kind"] = "site"
            to_site.append(e["id"])

        # A proclaimed era has no measurement error. Stripping the invented window leaves the
        # date standing on the record it actually came from.
        if _is_nengo(e) and e.get("start_year_min") is not None:
            # These keys are optional rather than required-but-nullable, unlike end_year, so the
            # absence of a bound is expressed by removing the key rather than by setting it null.
            for k in ("start_year_min", "start_year_max", "end_year_min", "end_year_max"):
                e.pop(k, None)
            e["start_dating_method"] = "calendar"
            if e.get("end_year") is not None:
                e["end_dating_method"] = "calendar"
            unbounded.append(e["id"])

        forced = FORCE_KIND.get(e["id"])
        if forced is not None and e["kind"] != forced:
            e["kind"] = forced
            rekinded.append(e["id"])

    missing = set(FORCE_KIND) - {e["id"] for e in entities}
    if missing:
        raise KeyError(f"review_triage: missing id(s): {sorted(missing)}")

    print(f"review_triage: {len(to_site)} non-cities re-kinded to site, "
          f"{len(unbounded)} nengo stripped of invented uncertainty, "
          f"{len(rekinded)} kind correction(s)")
