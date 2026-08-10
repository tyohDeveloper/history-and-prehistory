"""Rival claims to one sovereignty, and the Trịnh-Nguyễn division.

This began as a much bigger idea and got smaller under measurement, which is the
useful part of the story.

The premise was that the dataset cannot represent overlapping polities, on the
evidence that **988 sibling pairs have overlapping spans**. Examining them showed
that framing was wrong. The largest overlaps are archaeological sites and tool
industries, which coexist by nature. Restricting to historical-era polities still
left 298 pairs, and almost all of those are simply neighbours: Champa and Vietnam,
Tyre and Sidon, Moche and Nazca, Ghana and Kanem-Bornu. **Overlap is the normal
condition of history**, the dataset already represents it correctly, and a marker
on all of it would be noise.

What is genuinely unrepresented is far narrower: two entities claiming **the same
office or sovereignty at the same time**. That is a semantic relation, not a
temporal one, and no amount of date arithmetic can detect it. There are four cases.

* **Fatimid and Abbasid** — 262 years of simultaneous, mutually exclusive claims to
  the caliphate. The dataset's four caliphates read as a clean succession, which is
  the specific complaint that opened the question.
* **Mạc and Later Lê** — a usurpation the dataset already models as a deliberate
  overlap, with nothing saying why.
* **Afsharid and Zand** — the Afsharids held Khorasan while the Zand held everything
  else, both claiming Iran.
* **Trịnh and Nguyễn** — not previously authored at all, because there was no way to
  say what they were.

**The display had to come first.** `links` was authored, schema-checked and tested
for several releases while reaching no part of the interface: the Yuan has carried
`successor_state_of: central-asia.mongol-empire` that no reader could see. Adding a
new link type to an unrendered field would have produced more invisible data, which
is the `researchNote` failure exactly. So relations are rendered as of this release
and this module is what fills them.
"""

S_BRIT_FATIMID = "britannica-fatimid-dynasty"
S_BRIT_CALIPHATE = "britannica-caliphate"
S_WIKI_TRINH = "wikipedia-trinh-lords"
S_WIKI_NGUYEN_LORDS = "wikipedia-nguyen-lords"
S_BRIT_VIETNAM_DIV = "britannica-vietnam-partition"

RIVAL_SOURCES = [
    {"id": S_BRIT_FATIMID, "kind": "reference",
     "citation": "'Fatimid dynasty', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Fatimid-dynasty",
     "note": "The Fatimids claimed the caliphate as Ismaili Shia imams while the "
             "Abbasids held Baghdad, so the two claims were simultaneous and mutually "
             "exclusive."},
    {"id": S_BRIT_CALIPHATE, "kind": "reference",
     "citation": "'Caliphate', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/caliphate",
     "note": "The office was singular in theory and contested in fact; more than one "
             "claimant held it at once for long stretches."},
    {"id": S_WIKI_TRINH, "kind": "reference",
     "citation": "'Trịnh lords', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Tr%E1%BB%8Bnh_lords",
     "note": "Ruled the north as Đàng Ngoài from 1545 while the Lê emperors reigned "
             "nominally."},
    {"id": S_WIKI_NGUYEN_LORDS, "kind": "reference",
     "citation": "'Nguyễn lords', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Nguy%E1%BB%85n_lords",
     "note": "Ruled the south as Đàng Trong from 1558 until the Tây Sơn rising."},
    {"id": S_BRIT_VIETNAM_DIV, "kind": "reference",
     "citation": "'Vietnam: The Trịnh and the Nguyễn', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Vietnam/The-Trinh-and-the-Nguyen",
     "note": "The two lordly houses divided the country under nominal Lê sovereignty."},
]

# (a, b, note on a, note on b). The relation is symmetric, so it is written to
# both sides rather than left implicit in one direction.
RIVALS = [
    ("global.multi-regional.fatimid", "global.multi-regional.abbasid",
     "Claimed the caliphate as Ismaili Shia imams against the Abbasids in Baghdad.",
     "Held Baghdad while the Fatimids claimed the same office from Cairo.",
     [S_BRIT_FATIMID, S_BRIT_CALIPHATE]),
    ("southeast-asia.mainland.mac", "southeast-asia.mainland.later-le",
     "Usurped the throne and held the north; the Lê claim continued against it.",
     "Continued to claim the throne through the Mạc usurpation.",
     [S_WIKI_TRINH]),
    ("west-asia.iran.afsharid", "west-asia.iran.zand",
     "Held Khorasan after 1747 while the Zand held the rest of Iran.",
     "Held Iran except Khorasan, which remained Afsharid.",
     [S_BRIT_VIETNAM_DIV]),
]


def extend(E, entities):
    from builders import make_builders

    by_id = {e["id"]: e for e in entities}
    _, P, _, _, _, _ = make_builders(E, id_prefix="southeast-asia.mainland")

    def link(a, b, note, warrant):
        e = by_id.get(a)
        if e is None or b not in by_id:
            return False
        links = list(e.get("links", []))
        if any(l["entity_id"] == b and l["type"] == "rival_claimant_to" for l in links):
            return True
        links.append({"type": "rival_claimant_to", "entity_id": b, "note": note})
        e["links"] = links
        e["source_ids"] = sorted(set(e.get("source_ids", [])) | set(warrant))
        return True

    n = 0
    for a, b, na, nb, warrant in RIVALS:
        if not (link(a, b, na, warrant) and link(b, a, nb, warrant)):
            raise KeyError(f"rival_claims: could not link {a} <-> {b}; check the ids")
        n += 1

    # ── the Trịnh-Nguyễn division, finally authorable ──────────────────────
    # Two lord-domains under a Lê emperor who reigned without ruling. Modelled as
    # rivals to each other rather than as successive periods, because they were
    # simultaneous and neither displaced the other -- the Tây Sơn displaced both.
    # Fail loudly on a missing anchor. The first version of this module pointed at
    # `...vietnam.later-le`, which does not exist -- the Vietnamese dynasty ids sit
    # at `southeast-asia.mainland.*` while their parent_id points at the container.
    # So the entire block was skipped in silence while the summary line still
    # claimed the entities had been authored. A guard beats a hopeful `if`.
    LE = "southeast-asia.mainland.later-le"
    if LE not in by_id:
        raise KeyError(f"rival_claims: anchor {LE} not found; ids may have moved")
    if True:
        P("trinh", "Trịnh Lords (Đàng Ngoài)", LE, 1545, 1787, "foundational",
          summary="Ruled the north in the Lê emperor's name, holding real power for two "
                  "and a half centuries.",
          date_note="The Lê dynasty continued as the source of legitimacy throughout, "
                    "which is why this sits under it rather than beside it. Ended by the "
                    "Tây Sơn.",
          source_ids=[S_WIKI_TRINH, S_BRIT_VIETNAM_DIV],
          allow_outside_parent_dates=True)
        P("nguyen-lords", "Nguyễn Lords (Đàng Trong)", LE, 1558, 1777, "foundational",
          summary="Ruled the south independently in practice, expanding into the Mekong "
                  "delta at Cham and Khmer expense.",
          date_note="Nominally subordinate to the same Lê emperor as the Trịnh, and at "
                    "war with them for much of the period. Ended by the Tây Sơn, from "
                    "whom the surviving Nguyễn later took the throne outright in 1802.",
          source_ids=[S_WIKI_NGUYEN_LORDS, S_BRIT_VIETNAM_DIV],
          allow_outside_parent_dates=True)
        by_id2 = {e["id"]: e for e in entities}
        t = by_id2["southeast-asia.mainland.trinh"]
        g = by_id2["southeast-asia.mainland.nguyen-lords"]
        if True:
            t["links"] = [{"type": "rival_claimant_to", "entity_id": g["id"],
                           "note": "Fought the Nguyễn for the country while both claimed "
                                   "to serve the same emperor."}]
            g["links"] = [{"type": "rival_claimant_to", "entity_id": t["id"],
                           "note": "Fought the Trịnh for the country while both claimed "
                                   "to serve the same emperor."}]
            n += 1
        le = by_id2.get(LE)
        if le is not None:
            le["date_note"] = le.get("date_note", "").replace(
                "The Trịnh-Nguyễn division that actually governed the country is not yet "
                "modelled here.",
                "The Trịnh in the north and the Nguyễn in the south are now authored "
                "beneath, as rivals to each other rather than as successive periods: "
                "they were simultaneous, and neither displaced the other — the Tây Sơn "
                "displaced both.").strip()

    # The caliphate succession reads as clean because nothing said otherwise.
    ab = by_id.get("global.multi-regional.abbasid")
    if ab is not None:
        ab.setdefault("caveats", []).append(
            {"kind": "misconception",
             "text": "The four caliphates were not a clean succession: the Fatimids "
                     "claimed the same office from Cairo for 262 years of Abbasid rule.",
             "source_ids": [S_BRIT_CALIPHATE, S_BRIT_FATIMID]})

    print(f"Rival claims: {n} contested-sovereignty pairs linked, "
          f"Trịnh and Nguyễn lords authored")
