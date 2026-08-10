"""Apply the high-confidence corrections from the six-way correctness review.

136 patches over 120 entities, extracted from 4,702 lines of findings and verified against the
corpus before being written: every `from` value was checked to match what the data actually said,
and every field name and enum value against the schema.

The review produced 449 finding blocks, of which 115 were graded high confidence. 20 of those had
already been fixed by the bounds deletion and the frame change, and 38 needed a judgement this
pass deliberately does not make -- entity splits and merges, id renames, and findings that offered
two candidate values without choosing. A correction that is wrong is worse than one omitted.

This runs late, after normalisation, because it names entities by id.
"""

import json
import os

SOURCE = "docs/review/corrections.json"


def extend(E, entities):
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), SOURCE)
    if not os.path.exists(path):
        print("apply_corrections: no corrections file, skipping")
        return

    patches = json.load(open(path))
    by_id = {e["id"]: e for e in entities}
    applied, missing, stale = 0, [], []

    for p in patches:
        e = by_id.get(p["id"])
        if e is None:
            missing.append(p["id"])
            continue
        field, want = p["field"], p["to"]
        # If the current value no longer matches what the reviewer saw, something else has
        # changed it since. Report rather than overwrite: a stale patch is how a correction
        # silently undoes a later fix.
        if field in e and e.get(field) != p.get("from"):
            stale.append(f"{p['id']}.{field}")
            continue
        if want is None and field in ("end_year",):
            # Required-but-nullable: the key stays, the value goes.
            e[field] = None
        elif want is None:
            e.pop(field, None)
        else:
            e[field] = want
        applied += 1

        # An endpoint that gains a year must gain a method with it. The Great Schism was filed as
        # a living tradition with no end; correcting it to a dated event supplied the year and
        # left the endpoint unable to say how it was dated.
        if field == "end_year" and want is not None and not e.get("end_dating_method"):
            e["end_dating_method"] = e.get("start_dating_method") or "calendar"

    if missing:
        raise KeyError(f"apply_corrections: {len(missing)} unknown id(s): {missing[:5]}")
    print(f"apply_corrections: applied {applied} of {len(patches)} patches"
          + (f", skipped {len(stale)} stale" if stale else ""))
    if stale:
        for s in stale[:8]:
            print(f"    stale: {s}")


# Corrections move dates, and a moved date can put a child outside a parent that was fine before.
# The 11th Dynasty's start was corrected -- it had been dated 70 years before the reunification it
# is named for -- and its first three rulers now sit outside it, which is true and worth showing
# rather than an error to suppress by moving them back.
LEGITIMATE_OVERRUN = {
    "africa.nile.egypt.middle-kingdom.dyn11.intef-i":
        "Reigned from Thebes before the 11th Dynasty's corrected start, which now dates from the reunification.",
    "africa.nile.egypt.middle-kingdom.dyn11.intef-ii":
        "Reigned from Thebes before the 11th Dynasty's corrected start.",
    "africa.nile.egypt.middle-kingdom.dyn11.intef-iii":
        "Reigned from Thebes before the 11th Dynasty's corrected start.",
    "east-asia.japan.kenmu.kenmu-era":
        "The Northern Court kept counting Kenmu to 1338, past the end of the Kenmu Restoration itself.",
    "east-asia.china.yuan.huizong-yuan":
        "Toghon Temur reigned on in Mongolia after the Ming took Dadu in 1368, as the Northern Yuan.",
}


def flag_overruns(E, entities):
    by_id = {e["id"]: e for e in entities}
    flagged = 0
    for eid, why in LEGITIMATE_OVERRUN.items():
        e = by_id.get(eid)
        if e is None:
            continue
        e["allow_outside_parent_dates"] = True
        prior = (e.get("date_note") or "").strip()
        if why not in prior:
            e["date_note"] = (prior + " " + why).strip()
        flagged += 1

    # A node may not outrank the branch it hangs from. The modern pass marked every surviving
    # state foundational, which made Nauru and Kiribati more prominent than Micronesia itself and
    # left them stranded: a foundational node whose parent is not one has no path to it through
    # the tiers a reader is browsing by.
    order = {"foundational": 0, "intermediate": 1, "specialist": 2}
    demoted = 0
    for e in sorted(entities, key=lambda x: (x.get("id") or "").count(".")):
        parent = by_id.get(e.get("parent_id") or "")
        if parent is None:
            continue
        if order.get(e.get("tier"), 2) < order.get(parent.get("tier"), 2):
            e["tier"] = parent["tier"]
            demoted += 1
    print(f"apply_corrections: flagged {flagged} legitimate overrun(s), "
          f"demoted {demoted} entity/entities to their parent's tier")
