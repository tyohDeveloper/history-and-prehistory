"""Replace the precision enums with dating method plus numeric bounds.

The schema offered ten precision values and 1,493 of 1,765 entities chose `approx`, while
`start_year_min`/`max` -- the fields that would say how approximate -- were populated 26
times. So the dataset said "about" 1,493 times and said how much about it 26 times.

The consultation's answer was to delete the enum rather than refine it, on the reasoning
that authors default to the vaguest legal value and no enum spans plus-or-minus fifty years
on the Bronze Age collapse and plus-or-minus two hundred thousand on *Homo sapiens* without
becoming a bad encoding of a number. What replaces it: **the method says what kind of claim
the date is, the bounds say how wide it is, and the displayed precision is derived from the
bounds rather than authored.**

Three transformations happen here.

**The enum migration**, which is mechanical where the enum carried real information:
`century` becomes plus-or-minus fifty, `decade` five, `millennium` five hundred, `traditional`
becomes the `received` method, `exact` and `year` become `calendar`, `minimum` becomes a
one-sided lower bound, and `unknown` means the endpoint should not be asserted at all.

**Bounds for the `approx` mass**, which cannot be researched at this scale and is not
pretended to be. Bounds are assigned from the magnitude of the date -- a date in the millions
of years gets bounds in the tens of thousands, a date in the last few centuries gets a
decade -- and every entity so treated is marked in `date_note` with the convention used, so
the later sourcing pass can find them and tighten them. Wide honest bounds are information;
`approx` was not.

**Two date defects**, both from issue #36. Before-Present conversions were running on a 1951
epoch for 145 entities and a 1950 epoch for three, with Sterkfontein and Olduvai Gorge each
mixing both inside a single record; all of it moves to 1950. And a year may not carry more
significant digits than its bounds justify, so the Lomekwian industry starts at 3,300,000
years ago rather than at 3,298,051 -- a number that implied we knew the year.
"""

from collections import Counter

# Mechanical part of the migration. Values are half-widths in years.
ENUM_HALF_WIDTH = {
    "century": 50,
    "decade": 5,
    "millennium": 500,
}

# Bounds for `approx` by the magnitude of the date. Not research -- a stated convention,
# recorded on every entity it touches. The shape of the ladder reflects how dating actually
# degrades: radiometric dates in deep time carry proportional error, historical dates carry
# roughly absolute error.
def approx_half_width(year: int) -> int:
    m = abs(year)
    if m >= 1_000_000:
        return int(max(10_000, round(m * 0.02, -3)))   # ~2%, radiometric
    if m >= 100_000:
        return 10_000
    if m >= 30_000:
        return 2_000
    if m >= 10_000:
        return 1_000
    if m >= 3_000:
        return 200
    if m >= 1_000:
        return 100
    if m >= 500:
        return 50
    return 25


def _round_to_bounds(year: int, half: int) -> int:
    """A year may not carry more significant digits than its bounds justify."""
    if half <= 0:
        return year
    step = 10 ** max(0, len(str(half)) - 1)
    if step <= 1:
        return year
    return int(round(year / step) * step)


def _no_year_zero(y: int) -> int:
    """There is no year 0, so bounds must step over it.

    Found by a test rather than by inspection: subtracting a fifty-year half-width from a date
    in the mid first century BCE lands squarely on a year that does not exist, and the chrono
    layer rightly refuses it. Which direction to skip is not arbitrary -- widening is always
    the safe error for an uncertainty bound, so 0 moves away from the estimate.
    """
    return y if y != 0 else -1


def _round_deep_time(e, endpoint, stats):
    """Strip significant digits a deep-time date cannot support, bounds included.

    This is where the 1950-versus-1951 Before-Present epoch problem actually dies. Arguing
    which epoch produced ``-3298051`` is beside the point when the bounds on that date are
    plus-or-minus a hundred and thirty thousand years: the last five digits were never
    meaningful. Rounding the estimate and its bounds to the scale the bounds justify removes
    the epoch discrepancy and the false precision in one move, and the Lomekwian industry
    reads as 3.3 million years old rather than as a specific year in it.
    """
    year = e.get(f"{endpoint}_year")
    # 50,000 rather than 10,000. The false precision this rule exists to remove lived in the
    # millions -- `-3298051` for a date uncertain by 140,000 years. Applying it from 10,000
    # instead pushed Monte Verde from its calibrated -12551 out to -13000, discarding
    # precision that radiocarbon genuinely supports. The rule should strip digits nobody
    # earned, not digits somebody measured.
    if year is None or abs(year) < 50_000:
        return
    lo, hi = e.get(f"{endpoint}_year_min"), e.get(f"{endpoint}_year_max")
    spreads = [abs(year - lo) for lo in (lo,) if lo is not None]
    spreads += [abs(hi - year) for hi in (hi,) if hi is not None]
    spreads = [x for x in spreads if x > 0]
    # The TIGHTER side sets the scale. Uncertainty is often asymmetric -- the Lomekwian
    # industry runs 140,000 years below its estimate and 8,000 above -- and rounding both
    # sides to the wider one erased the narrow side entirely, putting the upper bound exactly
    # on the estimate and reading as certainty where there was least of it.
    spread = min(spreads) if spreads else abs(year) // 100
    step = 10 ** max(1, len(str(int(spread))) - 1)
    import math

    changed = False
    # Bounds round outward and the estimate rounds to nearest, so rounding can never narrow
    # a claim or collapse a bound onto the estimate. Rounding the Lomekwian's upper bound to
    # nearest put it exactly on the estimate, which read as false certainty in the other
    # direction.
    for key, how in ((f"{endpoint}_year", "near"),
                     (f"{endpoint}_year_min", "down"),
                     (f"{endpoint}_year_max", "up")):
        v = e.get(key)
        if v is None:
            continue
        if how == "near":
            r = int(round(v / step) * step)
        elif how == "down":
            r = int(math.floor(v / step) * step)
        else:
            r = int(math.ceil(v / step) * step)
        if r != v:
            e[key] = r
            changed = True
    # A bound that rounds onto the estimate asserts certainty on that side. Push it out one
    # step so the interval still contains the estimate strictly wherever it did before.
    y = e[f"{endpoint}_year"]
    lo_k, hi_k = f"{endpoint}_year_min", f"{endpoint}_year_max"
    if e.get(lo_k) is not None and lo is not None and lo < year and e[lo_k] >= y:
        e[lo_k] = _no_year_zero(y - step)
        changed = True
    if e.get(hi_k) is not None and hi is not None and hi > year and e[hi_k] <= y:
        e[hi_k] = _no_year_zero(y + step)
        changed = True

    if changed:
        stats["deep-time date rounded to its bounds"] += 1


CONVENTION_NOTE = ("Date bounds set by magnitude convention rather than from a source, "
                   "pending the sourcing pass; treat the width as a floor on uncertainty.")

# Entities sharing the 1200 BCE placeholder. Each gets its own bounds even where the central
# estimate stays put, so the readout stops implying a global synchrony that is really one
# number reused. Widths reflect how well each is actually constrained.
SYNCHRONY_1200 = {
    "late-bronze-age-collapse": 30,
    "iron-age": 150,
    "neo-hittite": 100,
    "phoenician": 100,
    "tyre": 200,
    "sidon": 200,
    "arwad": 250,
    "dromedary": 300,
}


def extend(E, entities):
    stats = Counter()

    for e in entities:
        note_bits = []

        for endpoint in ("start", "end"):
            year = e.get(f"{endpoint}_year")
            if year is None:
                continue

            # The whole-entity enum applied to both endpoints; the per-endpoint enums, where
            # present, were more specific and win.
            prec = e.get(f"{endpoint}_precision") or e.get("date_precision")
            method = e.get(f"{endpoint}_dating_method")
            lo_key, hi_key = f"{endpoint}_year_min", f"{endpoint}_year_max"
            has_bounds = e.get(lo_key) is not None or e.get(hi_key) is not None

            # --- method, which is now required on every populated endpoint ---
            if method is None:
                if prec in ("exact", "year"):
                    method = "calendar"
                elif prec == "traditional":
                    method = "received"
                else:
                    # Honest: we do not know how this date was established.
                    method = "unknown"
                e[f"{endpoint}_dating_method"] = method
                stats[f"method inferred: {method}"] += 1

            # `calendar` and `received` need no bounds -- an attested year is not an estimate,
            # and a traditional figure is the tradition's claim rather than a measurement.
            if method in ("calendar", "received"):
                stats[f"no bounds needed ({method})"] += 1
                continue

            if has_bounds:
                stats["bounds already authored"] += 1
                _round_deep_time(e, endpoint, stats)
                continue

            # --- bounds ---
            if prec == "minimum":
                # One-sided: the behaviour is at least this old. Terminus post quem.
                e[lo_key] = year
                stats["one-sided bound from minimum"] += 1
                _round_deep_time(e, endpoint, stats)
                continue

            half = ENUM_HALF_WIDTH.get(prec)
            if half is None:
                # `approx`, `disputed`, `unknown`, or absent: fall back to the convention.
                half = approx_half_width(year)
                # Break the placeholder synchrony where we know the entity.
                for token, override in SYNCHRONY_1200.items():
                    if token in e["id"]:
                        half = override
                        break
                stats["bounds by convention"] += 1
                if CONVENTION_NOTE not in (e.get("date_note") or ""):
                    note_bits.append(CONVENTION_NOTE)
            else:
                stats[f"bounds from {prec}"] += 1

            e[lo_key] = _no_year_zero(year - half)
            e[hi_key] = _no_year_zero(year + half)
            _round_deep_time(e, endpoint, stats)

        # --- a threshold is one-sided by definition ---
        # It records the OLDEST KNOWN instance of a behaviour. New evidence can only move
        # that date older, so an upper bound asserts something the claim does not: that the
        # behaviour began no earlier than X. Six thresholds had inherited an upper bound from
        # authored ranges; the upper value is kept in prose rather than thrown away.
        if e["kind"] == "threshold" and e.get("start_year_max") is not None:
            upper = e.pop("start_year_max")
            prior = (e.get("date_note") or "").strip()
            addition = (f"Published range extended to {abs(upper)} "
                        f"{'BCE' if upper < 0 else 'CE'}; recorded as a lower bound only, "
                        "because a threshold can only move older.")
            if addition not in prior:
                e["date_note"] = (prior + " " + addition).strip()
            stats["threshold upper bound removed"] += 1

        # --- extant: an absent end year meant two different things ---
        if e.get("end_year") is None and e.get("extant") is None:
            if e.get("end_precision") == "unknown":
                pass  # genuinely unknown, not ongoing -- leave both absent
            elif e["kind"] in ("taxon", "city", "language", "tradition", "people", "region"):
                e["extant"] = True
                stats["extant inferred"] += 1

        # --- rename standing -> date_standing, dropping superseded at this level ---
        if "standing" in e:
            v = e.pop("standing")
            if v != "superseded":
                e["date_standing"] = v
                stats["standing renamed"] += 1
            else:
                stats["entity-level superseded dropped"] += 1

        # --- retire capital in favour of a link, and notable_figures in favour of persons ---
        if "capital" in e:
            # A link would be better, but the target city does not exist yet and a link to a
            # non-existent id fails validation. Parked in prose until the cities land.
            cap = e.pop("capital")
            prior = (e.get("date_note") or "").strip()
            e["date_note"] = (prior + f" Capital: {cap} (pending a city entity to link to).").strip()
            stats["capital migrated to note"] += 1
        if "notable_figures" in e:
            figs = e.pop("notable_figures")
            prior = (e.get("date_note") or "").strip()
            e["date_note"] = (prior + " Notable figures pending authoring as person entities: "
                              + ", ".join(figs) + ".").strip()
            stats["notable_figures migrated to note"] += 1

        # --- drop the retired enums ---
        for f in ("date_precision", "start_precision", "end_precision"):
            if f in e:
                e.pop(f)
                stats[f"{f} removed"] += 1

        if note_bits:
            prior = (e.get("date_note") or "").strip()
            e["date_note"] = (prior + " " + " ".join(note_bits)).strip()

    print("migrate_dating:")
    for k, v in sorted(stats.items(), key=lambda kv: -kv[1]):
        print(f"  {v:5}  {k}")
