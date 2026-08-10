"""Phoenicia: a 961-year block, an exonym, and a wrong end date.

`tools/coverage.py` flagged Phoenician City-States as the widest childless era in
the dataset: 1500-539 BCE with nothing inside it. Filling it turned up two
problems the block was hiding.

**The end date was wrong.** 539 BCE is the Persian conquest, and it marks a change
of imperial overlord, not the end of anything Phoenician. Tyre, Sidon and Byblos
kept their kings, their fleets and independent political agency for two more
centuries under Achaemenid rule -- Sidon revolted, Tyre held out against Alexander
for seven months. The end of homeland Phoenician independence is **332 BCE**, the
fall of Tyre. Corrected, with 539 kept as the sourced alternative it deserves to
be.

**The name is a Greek exonym with no known native equivalent**, and this one goes
deeper than the Byzantine or Golden Horde cases. There, an outside name displaced
a self-designation that is known. Here there may be no self-designation to
recover: the evidence -- tombstones, coinage, the near-total loss of Phoenician
literature -- shows people identifying as Tyrian, Sidonian or Byblian, by city and
by family, and Josephine Quinn has argued that "the Phoenicians" as a
self-conscious people is substantially a modern scholarly construction. Others
treat Canaanite as the plausible collective self-term. Both positions are
recorded; neither is adopted.

**It was never a state.** Britannica, the Met, Lipiński and Quinn agree: no empire,
no confederation, only shifting informal primacy from Byblos to Sidon to Tyre. So
the node is a container for independent competing cities, and says so.

**One gap is closed and a smaller one opened.** Phoenicia leaves the childless-era
report; Byblos immediately joins it, as a single 2,668-year block. The tool is
right to flag it -- that is the same shape of problem one level down -- but the
research gathered here covers the city's phases only lightly, and inventing
subdivisions to satisfy a report would be worse than leaving a visible gap. Noted
rather than hidden.

**Phoenician versus Punic is a modern distinction too.** Prag and Quinn both note
the ancient sources do not make the split the way modern scholarship does, so the
existing Carthage entity is linked and annotated rather than renamed.
"""

S_BRIT_PHOENICIA = "britannica-phoenicia"
S_BRIT_LEBANON_ASSYR = "britannica-lebanon-assyrian-babylonian"
S_BRIT_BYBLOS = "britannica-byblos"
S_BRIT_TYRE = "britannica-tyre"
S_BRIT_SIDON = "britannica-sidon"
S_BRIT_ARWAD = "britannica-jazirat-arwad"
S_MET_PHOENICIA = "met-phoenicia"
S_QUINN = "quinn-in-search-of-the-phoenicians"
S_BMCR_QUINN = "bmcr-review-quinn-phoenicians"
S_BRIT_CARTHAGE = "britannica-carthage"
S_BRIT_ALEXANDER_TYRE = "britannica-siege-of-tyre"

PHOENICIA_SOURCES = [
    {"id": S_BRIT_PHOENICIA, "kind": "reference",
     "citation": "'Phoenicia', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Phoenicia",
     "note": "Phoenicia was never a unified state: a set of independent city-states "
             "with shifting primacy, and the name is Greek."},
    {"id": S_BRIT_LEBANON_ASSYR, "kind": "reference",
     "citation": "'Lebanon: Assyrian and Babylonian domination of Phoenicia', "
                 "Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Lebanon/Assyrian-and-Babylonian-domination-of-Phoenicia",
     "note": "The successive imperial overlordships -- Assyrian, Babylonian, then "
             "Persian -- under which the cities retained their kings."},
    {"id": S_BRIT_BYBLOS, "kind": "reference",
     "citation": "'Byblos', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Byblos",
     "note": "The oldest continuously occupied of the cities and dominant in the "
             "earliest period, trading with Egypt from the third millennium."},
    {"id": S_BRIT_TYRE, "kind": "reference",
     "citation": "'Tyre', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Tyre",
     "note": "Dominant from roughly the tenth century; founded the western colonies; "
             "fell to Alexander in 332 BCE after a seven-month siege."},
    {"id": S_BRIT_SIDON, "kind": "reference",
     "citation": "'Sidon', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Sidon",
     "note": "Held primacy between the Byblian and Tyrian phases, and revolted against "
             "Persia in the fourth century."},
    {"id": S_BRIT_ARWAD, "kind": "reference",
     "citation": "'Jazirat Arwad', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Jazirat-Arwad",
     "note": "The northernmost city, on an island off the Syrian coast."},
    {"id": S_MET_PHOENICIA, "kind": "reference",
     "citation": "'The Phoenicians', The Metropolitan Museum of Art",
     "url": "https://www.metmuseum.org/toah/hd/phoe/hd_phoe.htm",
     "note": "Treats Canaanite as the plausible self-designation, and frames the "
             "Phoenician period as roughly 1500-300 BCE."},
    {"id": S_QUINN, "kind": "scholarly",
     "citation": "Quinn, In Search of the Phoenicians (Princeton, 2018)",
     "url": "https://press.princeton.edu/books/hardcover/9780691175270/in-search-of-the-phoenicians",
     "note": "Argues that a collective Phoenician identity is substantially a modern "
             "construction, and that the ancient evidence shows self-identification by "
             "city and family rather than by people."},
    {"id": S_BMCR_QUINN, "kind": "scholarly",
     "citation": "Bryn Mawr Classical Review, review of Quinn",
     "url": "https://bmcr.brynmawr.edu/2015/2015.09.53/",
     "note": "Academic engagement with the argument, indicating it is contested rather "
             "than settled in either direction."},
    {"id": S_BRIT_CARTHAGE, "kind": "reference",
     "citation": "'Carthage', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Carthage-ancient-city-Tunisia",
     "note": "Traditionally founded from Tyre in 814 BCE; archaeology converges on the "
             "late ninth century."},
    {"id": S_BRIT_ALEXANDER_TYRE, "kind": "reference",
     "citation": "'Siege of Tyre', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Siege-of-Tyre-332-BCE",
     "note": "332 BCE, the end of Tyrian and effectively of homeland Phoenician "
             "independence."},
]


def extend(E, entities):
    from builders import make_builders

    by_id = {e["id"]: e for e in entities}
    _, P, ERA, _, _, _ = make_builders(E, id_prefix="west-asia.mesopotamia.phoenicia")
    PH = "west-asia.mesopotamia.phoenicia"

    ph = by_id.get(PH)
    if ph is None:
        return

    # The correction: 539 changed the overlord, not the polity.
    ph["end_year"] = -332
    ph["tier"] = "foundational"
    ph["summary"] = ("Independent Canaanite-speaking city-states on the Levantine "
                     "coast, never politically unified.")
    ph["date_note"] = (
        "Previously ended at 539 BCE, the Persian conquest. That marks a change of "
        "imperial overlord rather than an end: under Achaemenid rule Tyre, Sidon and "
        "Byblos kept their own kings and fleets, Sidon revolted, and Tyre withstood "
        "Alexander for seven months. Homeland independence ends in 332 BCE with the "
        "fall of Tyre. The start is approximate and marks the Late Bronze Age "
        "Canaanite phase from which these cities emerge, not a founding.")
    ph["date_precision"] = "approx"
    ph["source_ids"] = [S_BRIT_PHOENICIA, S_MET_PHOENICIA, S_BRIT_LEBANON_ASSYR,
                        S_BRIT_ALEXANDER_TYRE]
    ph["alternatives"] = [
        {"label": "539 BCE, the Persian conquest", "standing": "minority",
         "end_year": -539,
         "note": "A change of overlord; the cities kept their kings for two more "
                 "centuries.",
         "source_ids": [S_BRIT_LEBANON_ASSYR]},
    ]
    ph["caveats"] = [
        {"kind": "naming-confusion",
         "text": "Phoenicia is Greek. No native collective equivalent is known: people "
                 "identified as Tyrian, Sidonian or Byblian.",
         "source_ids": [S_BRIT_PHOENICIA, S_MET_PHOENICIA]},
        {"kind": "contested-existence",
         "text": "Quinn argues a collective Phoenician identity is largely a modern "
                 "construction; others treat Canaanite as the self-designation. The "
                 "question is open.",
         "source_ids": [S_QUINN, S_BMCR_QUINN, S_MET_PHOENICIA]},
        {"kind": "contested-existence",
         "text": "Never a state, an empire or a confederation -- independent competing "
                 "cities under shifting informal primacy.",
         "source_ids": [S_BRIT_PHOENICIA, S_MET_PHOENICIA]},
    ]
    ph["name_forms"] = [
        {"name": "Phoenicia", "kind": "exonym", "lang": "grc",
         "note": "From Greek phoinix. The name a reader arrives with, and an outsider's.",
         "source_ids": [S_BRIT_PHOENICIA]},
        {"name": "Canaanite", "kind": "endonym",
         "note": "The plausible self-term per the Met; Quinn rejects even this as a "
                 "collective identity.",
         "source_ids": [S_MET_PHOENICIA, S_QUINN]},
    ]

    # ── periodisation ─────────────────────────────────────────────────────
    P("canaanite-phase", "Late Bronze Age Canaanite Phase", PH, -1500, -1200,
      "intermediate",
      summary="The cities under Egyptian and Hittite overlordship, before the collapse "
              "that freed them.",
      source_ids=[S_MET_PHOENICIA], date_precision="approx")
    P("independence", "Phoenician Independence", PH, -1200, -883, "foundational",
      summary="Three centuries of genuine autonomy after the Bronze Age Collapse "
              "removed the empires above them — the period of the alphabet and the "
              "western voyages.",
      date_note="Begins with the collapse rather than with any Phoenician event. Ends "
                "as Assyrian pressure resumes under Ashurnasirpal II.",
      source_ids=[S_BRIT_PHOENICIA, S_BRIT_LEBANON_ASSYR], date_precision="approx")
    P("assyrian-period", "Under Assyria", PH, -883, -612, "intermediate",
      summary="Tributary to Assyria, with the cities retaining their kings.",
      source_ids=[S_BRIT_LEBANON_ASSYR])
    P("babylonian-period", "Under Babylon", PH, -612, -539, "intermediate",
      summary="Nebuchadnezzar II besieged Tyre for thirteen years.",
      source_ids=[S_BRIT_LEBANON_ASSYR])
    P("persian-period", "Under Persia", PH, -539, -332, "foundational",
      summary="Achaemenid subjects supplying the imperial navy, still ruled by their own "
              "kings — which is why 539 is the wrong place to end Phoenicia.",
      source_ids=[S_BRIT_LEBANON_ASSYR, S_BRIT_ALEXANDER_TYRE])

    # ── the cities ────────────────────────────────────────────────────────
    ERA("byblos", "Byblos", PH, -3000, -332, "foundational",
        native="𐤂𐤁𐤋",
        summary="The oldest of the cities and the earliest to dominate, trading cedar "
                "with Egypt from the third millennium.",
        date_note="Occupied far earlier than the Phoenician period proper; the start "
                  "marks its Egyptian trade rather than a founding.",
        source_ids=[S_BRIT_BYBLOS], date_precision="approx",
        allow_outside_parent_dates=True)
    ERA("sidon", "Sidon", PH, -1200, -332, "foundational",
        summary="Held primacy between the Byblian and Tyrian phases, and revolted "
                "against Persia in the 350s.",
        source_ids=[S_BRIT_SIDON], date_precision="approx")
    ERA("tyre", "Tyre", PH, -1200, -332, "foundational",
        summary="Dominant from the tenth century, founded Carthage and the western "
                "colonies, and fell to Alexander after a seven-month siege.",
        source_ids=[S_BRIT_TYRE, S_BRIT_ALEXANDER_TYRE], date_precision="approx")
    ERA("arwad", "Arwad", PH, -1200, -332, "intermediate",
        summary="The northernmost city, on an island off the Syrian coast.",
        source_ids=[S_BRIT_ARWAD], date_precision="approx")

    # ── Carthage: link, annotate, do not rename ───────────────────────────
    c = by_id.get("africa.north.carthage")
    if c is not None:
        c["source_ids"] = sorted(set(c.get("source_ids", [])) | {S_BRIT_CARTHAGE,
                                                                 S_BRIT_TYRE})
        c["cross_parent_ids"] = sorted(set(c.get("cross_parent_ids", [])) | {PH})
        c["date_note"] = (
            "Founded from Tyre; the traditional date is 814 BCE and archaeology "
            "converges on the late ninth century. Punic is a modern term for the "
            "western Phoenicians rather than an ancient distinction the sources "
            "themselves draw.").strip()
        c["alternatives"] = [
            {"label": "814 BCE, the traditional founding", "standing": "traditional",
             "start_year": -814,
             "source_ids": [S_BRIT_CARTHAGE]},
        ]
        c.setdefault("caveats", []).append(
            {"kind": "naming-confusion",
             "text": "Punic and Phoenician are a modern scholarly split, not one the "
                     "ancient sources make consistently.",
             "source_ids": [S_QUINN, S_BRIT_CARTHAGE]})

    print("Phoenicia: end corrected 539 -> 332 BCE, five periods, four cities")
