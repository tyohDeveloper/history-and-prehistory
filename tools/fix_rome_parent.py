"""File the Roman Empire under Ancient Rome, where its own id already said it belonged.

Found by chasing a reported search failure: searching **Rome** returned "Domestication of
the Dromedary" and none of Rome's rulers, and "rulers of rome" returned nothing.

The search matcher was part of it and is fixed separately. But the deeper cause was
structural. `europe.mediterranean.rome.empire` had `parent_id: europe.mediterranean` — so
despite an id saying it sits under Rome, the tree placed the **Roman Empire as a sibling of
Ancient Rome**, while the Kingdom and the Republic were children of it. Ancient Rome runs
753 BCE to 476 CE and the Empire 27 BCE to 476 CE, so containment was never in doubt; the
parent pointer simply disagreed with everything else.

The consequence for a reader was concrete. No ancestor chain from any of the 92 entities
under the Empire passed through a node named "Rome": an emperor's lineage read
Julio-Claudian Dynasty → Roman Empire → Mediterranean → Europe. Since "Roman" is not a
prefix of "Rome", nothing connected the emperors to the word Rome at all, and drilling from
Ancient Rome showed the Kingdom and the Republic and then stopped — the Empire was one
column to the left, looking like a separate civilisation.

This is distinct from the deliberate divergence documented in `builders.py`, where Roman
emperors keep flat ids under `<rome>.empire` while their `parent_id` points at whichever
dynasty they belong to. That one is intentional and stays. This one was an oversight.
"""

ROME = "europe.mediterranean.rome"
EMPIRE = "europe.mediterranean.rome.empire"


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}
    empire = by_id.get(EMPIRE)
    rome = by_id.get(ROME)
    if empire is None or rome is None:
        raise KeyError(f"fix_rome_parent: {EMPIRE} or {ROME} not found")

    if empire.get("parent_id") == ROME:
        print("Rome parent: already correct")
        return

    was = empire.get("parent_id")
    empire["parent_id"] = ROME

    # Ancient Rome ends with the western empire in 476, so the Empire fits inside it and
    # needs no exemption. Assert that rather than assume it.
    assert rome["start_year"] <= empire["start_year"], "Ancient Rome starts after the Empire"
    assert rome["end_year"] >= empire["end_year"], "Ancient Rome ends before the Empire"

    prior = (empire.get("date_note") or "").strip()
    extra = ("Filed under Ancient Rome alongside the Kingdom and the Republic. It previously "
             "sat beside them as a sibling, which left the emperors unreachable from Rome by "
             "either search or drilling.")
    if extra not in prior:
        empire["date_note"] = f"{prior} {extra}".strip()

    moved = sum(1 for e in entities if e["id"].startswith(EMPIRE + "."))
    print(f"Rome parent: Roman Empire reparented from {was} to {ROME}, "
          f"bringing {moved} entities under Rome")
