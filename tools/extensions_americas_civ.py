"""The American civilisations: structured names, and 45 entities with no sources.

(Holocene prehistory lives in `extensions_americas.py`; this module is the
post-Archaic civilisations, which were a separate and completely unsourced
problem.)

Research in `docs/americas-research.md`.

Two things were true of this region at once. `americas.prehistory` was the most
rigorously sourced branch in the dataset -- 23 of 23 entities cited. Everything
else, all 45 entities, had **zero sources**. Every archaeological site was
scrupulous; every actual civilization was bare. The same inversion the
Mediterranean had, but total.

And it is the densest concentration of the naming problem anywhere in the
dataset. Before this pass it was being handled four different ways at once:

* `Ancestral Puebloan` -- corrected name, no alias, so **"Anasazi" found
  nothing**. The correction is right and it made the entity invisible to
  precisely the readers holding older books.
* `Haudenosaunee (Iroquois)` -- both names crammed into the display name.
* `Aztec Empire` -- alias `Mexica Triple Alliance`.
* `Inca Empire` -- `native_name` Tawantinsuyu.

Four strategies, one problem. That is what `name_forms` is for: every name is
indexed for search, and the UI groups them by what kind of name each one is,
because the difference between a name a people chose and a name imposed on them
is content, not metadata.

The cases here are unusually clear.

**Olmec** is the best-documented misnomer in the dataset. It is a Nahuatl word
meaning "rubber people", which the Mexica used for the Gulf Coast inhabitants
who were their own contemporaries in the 15th and 16th centuries. Hermann Beyer
borrowed it in 1929 for an archaeological culture that had ended roughly two
thousand years earlier. No endonym survives.

**Anasazi** is Navajo, glossed as "enemy ancestors", and Pueblo peoples have
rejected it since the early 1990s. The National Park Service states plainly that
"no one knows what they called themselves"; the Hopi term for their own
ancestors is Hisatsinom. It is filed as `rejected` -- struck through in the
readout, still fully searchable, which is the whole point.

**Haudenosaunee** loses its parenthetical. The Confederacy's founding is a real
dispute and now reads as one: Snow and the archaeological mainstream in the
1450s, against Mann and Fields' 1142, argued from oral tradition plus a solar
eclipse -- with the published rebuttal recorded rather than omitted.

**Toltec** keeps its dates and gains a `contested-existence` caveat, because
whether Tula supported a real empire or whether "Toltec" is substantially a
Mexica retrospective construct is unresolved and the dataset should not pick.

Deliberately NOT authored: the **Columbian Exchange and contact-era
depopulation**. The estimates run from roughly 8 million to over 100 million and
the disagreement is methodological rather than evidentiary; it needs its own
pass with the competing estimation methods named, not a single number wedged
into a summary line.
"""

S_BRIT_AZTEC = "britannica-aztec"
S_BRIT_INCA = "britannica-inca"
S_NPS_MESA_VERDE = "nps-mesa-verde-history"
S_ARCHAEOLOGY_ANASAZI = "archaeology-magazine-anasazi"
S_HAUD_OFFICIAL = "haudenosaunee-confederacy-official"
S_NYSM_MOHAWK = "nysm-mohawk-iroquois"
S_BRIT_OLMEC = "britannica-olmec"
S_BRIT_SAN_LORENZO = "britannica-san-lorenzo"
S_BRIT_TOLTEC = "britannica-toltec"
S_BRIT_MAYA = "britannica-maya-people"
S_SMARTHISTORY_MAYA = "smarthistory-maya-intro"
S_BRIT_TEOTIHUACAN = "britannica-teotihuacan"
S_BRIT_MONTE_ALBAN = "britannica-monte-alban"
S_BRIT_TENOCHTITLAN = "britannica-tenochtitlan"
S_HAAS_NATURE = "haas-creamer-ruiz-2004-norte-chico"
S_BRIT_CHAVIN = "britannica-chavin"
S_BRIT_MOCHE = "britannica-moche"
S_BRIT_HUARI = "britannica-huari"
S_BRIT_CHIMU = "britannica-chimu"
S_BRIT_ANCESTRAL_PUEBLO = "britannica-ancestral-pueblo"
S_BRIT_CHACO = "britannica-chaco-culture"
S_BRIT_CAHOKIA = "britannica-cahokia"
S_UNESCO_QHAPAQ = "unesco-qhapaq-nan"
S_ESCHOLARSHIP_MYTH = "escholarship-myth-astronomically-dated"
S_MANN_FIELDS = "mann-fields-sign-in-the-sky"

AMERICAS_CIV_SOURCES = [
    {"id": S_BRIT_AZTEC, "kind": "reference", "citation": "'Aztec', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Aztec",
     "note": "The people called themselves Mexica, more precisely Culhua-Mexica."},
    {"id": S_BRIT_INCA, "kind": "reference", "citation": "'Inca', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Inca",
     "note": "Inca is properly a ruler's title in Quechua, applied by convention to the whole "
             "state and population."},
    {"id": S_NPS_MESA_VERDE, "kind": "reference",
     "citation": "Mesa Verde administrative history, US National Park Service",
     "url": "https://www.nps.gov/parkhistory/online_books/smith/chap13.htm",
     "note": "States plainly that no one knows what the Ancestral Puebloans called themselves."},
    {"id": S_ARCHAEOLOGY_ANASAZI, "kind": "scholarly",
     "citation": "'What's in a Name? The Anasazi', Archaeology Magazine",
     "url": "https://archive.archaeology.org/0607/news/insider.html",
     "note": "Records a live disagreement within Navajo scholarship over how negative the "
             "term's connotation actually is."},
    {"id": S_HAUD_OFFICIAL, "kind": "primary",
     "citation": "Haudenosaunee Confederacy, official site",
     "url": "https://www.haudenosauneeconfederacy.com/",
     "note": "Haudenosaunee means 'people of the longhouse'."},
    {"id": S_NYSM_MOHAWK, "kind": "reference",
     "citation": "Mohawk Iroquois resources, New York State Museum",
     "url": "https://nysm.nysed.gov/mohawk-iroquois",
     "note": "Reports the derivation of 'Iroquois' from a Huron term for adders or black "
             "snakes, originating with an enemy nation."},
    {"id": S_BRIT_OLMEC, "kind": "reference", "citation": "'Olmec', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Olmec"},
    {"id": S_BRIT_SAN_LORENZO, "kind": "reference",
     "citation": "'San Lorenzo', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/San-Lorenzo-archaeological-site-Mexico"},
    {"id": S_BRIT_TOLTEC, "kind": "reference", "citation": "'Toltec', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Toltec"},
    {"id": S_BRIT_MAYA, "kind": "reference", "citation": "'Maya', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Maya-people"},
    {"id": S_SMARTHISTORY_MAYA, "kind": "reference",
     "citation": "'Introduction to the Maya', Smarthistory",
     "url": "https://smarthistory.org/maya-intro/"},
    {"id": S_BRIT_TEOTIHUACAN, "kind": "reference",
     "citation": "'Teotihuacan', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Teotihuac%C3%A1n"},
    {"id": S_BRIT_MONTE_ALBAN, "kind": "reference",
     "citation": "'Monte Alban', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Monte-Alban"},
    {"id": S_BRIT_TENOCHTITLAN, "kind": "reference",
     "citation": "'Tenochtitlan', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Tenochtitlan"},
    {"id": S_HAAS_NATURE, "kind": "scholarly",
     "citation": "Haas, Creamer & Ruiz, 'Dating the Late Archaic occupation of the Norte Chico region in Peru', Nature (2004)",
     "url": "https://www.nature.com/articles/nature03146",
     "note": "Radiocarbon programme establishing monumental construction in the third "
             "millennium BCE."},
    {"id": S_BRIT_CHAVIN, "kind": "reference", "citation": "'Chavin', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Chavin"},
    {"id": S_BRIT_MOCHE, "kind": "reference", "citation": "'Moche', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Moche"},
    {"id": S_BRIT_HUARI, "kind": "reference", "citation": "'Huari', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Huari"},
    {"id": S_BRIT_CHIMU, "kind": "reference", "citation": "'Chimu', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Chimu"},
    {"id": S_BRIT_ANCESTRAL_PUEBLO, "kind": "reference",
     "citation": "'Ancestral Pueblo culture', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Ancestral-Pueblo-culture"},
    {"id": S_BRIT_CHACO, "kind": "reference",
     "citation": "'Chaco Culture National Historical Park', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Chaco-Culture-National-Historical-Park"},
    {"id": S_BRIT_CAHOKIA, "kind": "reference",
     "citation": "'Cahokia Mounds', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Cahokia-Mounds"},
    {"id": S_UNESCO_QHAPAQ, "kind": "reference",
     "citation": "'Qhapaq Nan, Andean Road System', UNESCO World Heritage Centre",
     "url": "https://whc.unesco.org/en/list/1459/"},
    {"id": S_MANN_FIELDS, "kind": "scholarly",
     "citation": "Mann & Fields, 'A Sign in the Sky: Dating the League of the Haudenosaunee', American Indian Culture and Research Journal (1997)",
     "url": "https://escholarship.org/uc/item/34s5f7qm",
     "note": "Argues from oral tradition plus a solar eclipse for a founding in 1142."},
    {"id": S_ESCHOLARSHIP_MYTH, "kind": "scholarly",
     "citation": "'Can a Myth Be Astronomically Dated?', American Indian Culture and Research Journal (1999)",
     "url": "https://escholarship.org/uc/item/0f04m96b",
     "note": "Direct published rebuttal to the Mann and Fields eclipse dating."},
]

CHECKED = "2026-08-09"
C14 = "radiocarbon-calibrated"
DENDRO = "dendrochronology"
CAL = "calendar"
TYP = "typological"


def extend(E, entities):
    from builders import make_builders
    _, P, ERA, EVENT, _, _ = make_builders(E)
    by_id = {e["id"]: e for e in entities}

    def enrich(eid, **kw):
        e = by_id.get(eid)
        if e is None:
            return None
        cav = kw.pop("caveats", None)
        for k, v in kw.items():
            e[k] = v
        if cav:
            e["caveats"] = list(e.get("caveats", [])) + cav
        return e

    # ------------------------------------------------- Mesoamerica: names

    enrich("americas.mesoamerica.olmec",
           name="Olmec Civilization",
           name_forms=[
               {"name": "Olmeca", "kind": "exonym", "lang": "nah",
                "note": "Nahuatl for 'rubber people'. The Mexica used it for the Gulf Coast "
                        "inhabitants of their own time, two millennia later than this "
                        "civilization.",
                "source_ids": [S_BRIT_OLMEC]},
               {"name": "Tenocelome", "kind": "scholarly",
                "note": "'Mouth of the jaguar', proposed by some scholars to avoid the "
                        "misnomer. Not widely adopted.",
                "source_ids": [S_BRIT_OLMEC]},
           ],
           start_year=-1200, end_year=-400,
           start_dating_method=C14, end_dating_method=C14,
           standing="majority", date_precision="century",
           date_note="San Lorenzo, the earliest major centre, dates to about 1150 BCE.",
           source_ids=[S_BRIT_OLMEC, S_BRIT_SAN_LORENZO],
           caveats=[
               {"kind": "naming-confusion",
                "text": "The name is borrowed and wrong. Hermann Beyer applied a Nahuatl word "
                        "for a much later people to this culture in 1929. No self-designation "
                        "survives.",
                "source_ids": [S_BRIT_OLMEC]},
           ])

    enrich("americas.mesoamerica.aztec",
           name="Aztec Empire",
           native_name="Excan Tlatoloyan",
           name_forms=[
               {"name": "Mexica", "kind": "endonym", "lang": "nah",
                "note": "What the people called themselves, more precisely Culhua-Mexica.",
                "source_ids": [S_BRIT_AZTEC]},
               {"name": "Excan Tlatoloyan", "kind": "formal", "lang": "nah",
                "note": "The Triple Alliance of Tenochtitlan, Texcoco and Tlacopan, which is "
                        "what the polity actually was.",
                "source_ids": [S_BRIT_AZTEC]},
               {"name": "Triple Alliance", "kind": "scholarly",
                "source_ids": [S_BRIT_AZTEC]},
               {"name": "Aztec", "kind": "exonym",
                "note": "Popularised as a civilizational label by Humboldt in the 19th "
                        "century; never a general self-designation.",
                "source_ids": [S_BRIT_AZTEC]},
           ],
           start_dating_method=CAL, end_dating_method=CAL,
           standing="majority", date_precision="year",
           date_note="The Triple Alliance was formed in 1428 under Itzcoatl against "
                     "Azcapotzalco, and fell with Tenochtitlan on 13 August 1521.",
           source_ids=[S_BRIT_AZTEC, S_BRIT_TENOCHTITLAN],
           caveats=[
               {"kind": "naming-confusion",
                "text": "'Aztec Empire' is a 19th-century construct for what was an alliance "
                        "of three city-states. Its people were Mexica.",
                "source_ids": [S_BRIT_AZTEC]},
           ])

    # The dataset ended the Zapotec at 800, which is the end of Monte Alban's
    # Classic floruit rather than of the civilisation -- Zapotec polities
    # persisted to the conquest. Extending the parent rather than truncating
    # the capital.
    enrich("americas.mesoamerica.zapotec",
           end_year=1521,
           start_dating_method=C14, end_dating_method=CAL,
           standing="majority", date_precision="century",
           date_note="Runs to the Spanish conquest. The often-quoted end around 800 CE is "
                     "the close of Monte Alban's Classic florescence, not of the Zapotec.",
           source_ids=[S_BRIT_MONTE_ALBAN])

    enrich("americas.mesoamerica.purepecha",
           name="Purépecha Empire",
           name_forms=[
               {"name": "Purépecha", "kind": "endonym"},
               {"name": "Tarascan", "kind": "exonym",
                "note": "A Spanish-era name of disputed and possibly disparaging origin."},
           ],
           start_dating_method=CAL, end_dating_method=CAL,
           standing="majority", date_precision="approx",
           date_note="Founded by Tariacuri with a capital at Patzcuaro around 1300; some "
                     "sources give 1325.")

    enrich("americas.mesoamerica.toltec",
           start_dating_method=TYP, end_dating_method=TYP,
           # No `as_of`: what is disputed is whether the polity existed, which is
           # carried as a caveat. There is no rival chronology to re-check.
           standing="minority", date_precision="disputed",
           date_note="These dates describe the archaeological horizon centred on Tula. "
                     "Whether they describe an empire is exactly what is disputed.",
           source_ids=[S_BRIT_TOLTEC],
           caveats=[
               {"kind": "contested-existence",
                "text": "Historicists hold that Tula supported a real Toltec state. Sceptics "
                        "hold that 'Toltec' is substantially a Mexica retrospective ideal. "
                        "Unresolved.",
                "source_ids": [S_BRIT_TOLTEC]},
           ])

    enrich("americas.mesoamerica.teotihuacan",
           start_dating_method=C14, end_dating_method=C14,
           standing="majority", date_precision="century",
           date_note="The city's monumental florescence. Its inhabitants' own name for it is "
                     "unknown; 'Teotihuacan' is what the Mexica called the ruins centuries "
                     "later.",
           source_ids=[S_BRIT_TEOTIHUACAN],
           name_forms=[
               {"name": "Teotihuacan", "kind": "exonym", "lang": "nah",
                "note": "Nahuatl, roughly 'birthplace of the gods', applied by the Mexica to "
                        "a city already long abandoned.",
                "source_ids": [S_BRIT_TEOTIHUACAN]},
           ])

    for eid, src in (("americas.mesoamerica.maya", S_BRIT_MAYA),
                     ("americas.mesoamerica.maya.classic", S_SMARTHISTORY_MAYA),
                     ("americas.mesoamerica.maya.postclassic", S_BRIT_MAYA)):
        enrich(eid, start_dating_method=C14, end_dating_method=C14,
               standing="majority", source_ids=[src, S_BRIT_MAYA])

    enrich("americas.mesoamerica.maya.postclassic",
           date_precision="disputed", as_of=CHECKED,
           date_note="The end depends on which ending is meant: first Spanish contact in "
                     "1519, the fall of the northern polities, or Nojpeten in 1697.",
           alternatives=[
               {"label": "Ends 1519 (first Spanish contact)", "standing": "majority",
                "end_year": 1519,
                "note": "Dates the end from contact rather than from the last independent "
                        "Maya polity.",
                "source_ids": [S_BRIT_MAYA]},
           ])

    # ------------------------------------------------------------- Andes

    enrich("americas.andes.inca",
           name="Inca Empire",
           native_name="Tawantinsuyu",
           name_forms=[
               {"name": "Tawantinsuyu", "kind": "endonym", "lang": "qu",
                "note": "Quechua for 'the four regions together'.",
                "source_ids": [S_BRIT_INCA]},
               {"name": "Tahuantinsuyu", "kind": "translation", "lang": "qu"},
               {"name": "Inca", "kind": "exonym",
                "note": "Properly a ruler's title, extended by convention to the whole state "
                        "and its people.",
                "source_ids": [S_BRIT_INCA]},
           ],
           start_dating_method=CAL, end_dating_method=CAL,
           standing="majority", date_precision="year",
           date_note="1438 is the earliest date confidently assignable to imperial history, "
                     "when Pachacuti took the throne.",
           source_ids=[S_BRIT_INCA],
           caveats=[
               {"kind": "naming-confusion",
                "text": "'Inca' was the title of the ruler and his class, perhaps 40,000 "
                        "people. It now names an empire of millions.",
                "source_ids": [S_BRIT_INCA]},
           ])

    for eid, src, meth in (
        ("americas.andes.norte-chico", S_HAAS_NATURE, C14),
        ("americas.andes.chavin", S_BRIT_CHAVIN, C14),
        ("americas.andes.moche", S_BRIT_MOCHE, C14),
        ("americas.andes.wari", S_BRIT_HUARI, C14),
        ("americas.andes.chimu", S_BRIT_CHIMU, C14),
    ):
        enrich(eid, start_dating_method=meth, end_dating_method=meth,
               standing="majority", date_precision="century", source_ids=[src])

    enrich("americas.andes.norte-chico",
           name_forms=[{"name": "Caral", "kind": "common",
                        "note": "Often named for its largest excavated site.",
                        "source_ids": [S_HAAS_NATURE]},
                       {"name": "Caral-Supe", "kind": "scholarly"}],
           date_note="Monumental construction in the third millennium BCE, established by a "
                     "radiocarbon programme published in Nature.")

    enrich("americas.andes.moche", end_year=800,
           date_note="Britannica gives the 1st to 8th century CE; the dataset previously "
                     "ended this a century early.")

    # -------------------------------------------------- North America

    enrich("americas.north.ancestral-puebloan",
           name="Ancestral Puebloan",
           # Tree rings, not radiocarbon. Douglass developed dendrochronology on
           # exactly this material in the 1920s, and Southwest sites are dated
           # to the year -- offering the reader "cal BP" here would understate
           # the precision by orders of magnitude.
           name_forms=[
               {"name": "Anasazi", "kind": "rejected",
                "note": "Navajo, glossed as 'enemy ancestors'. Pueblo peoples have rejected "
                        "it since the early 1990s, and the National Park Service dropped it.",
                "source_ids": [S_NPS_MESA_VERDE, S_ARCHAEOLOGY_ANASAZI]},
               {"name": "Hisatsinom", "kind": "endonym", "lang": "hop",
                "note": "The Hopi term for their own ancestors. No general self-designation "
                        "for the whole culture is recoverable.",
                "source_ids": [S_NPS_MESA_VERDE]},
               {"name": "Ancestral Pueblo culture", "kind": "scholarly",
                "source_ids": [S_BRIT_ANCESTRAL_PUEBLO]},
           ],
           start_dating_method=DENDRO, end_dating_method=DENDRO,
           standing="majority", date_precision="century",
           source_ids=[S_BRIT_ANCESTRAL_PUEBLO, S_NPS_MESA_VERDE, S_ARCHAEOLOGY_ANASAZI],
           caveats=[
               {"kind": "naming-confusion",
                "text": "The National Park Service states that no one knows what these people "
                        "called themselves. Every name for them is somebody else's.",
                "source_ids": [S_NPS_MESA_VERDE]},
           ])

    enrich("americas.north.haudenosaunee",
           name="Haudenosaunee Confederacy",
           name_forms=[
               {"name": "Haudenosaunee", "kind": "endonym",
                "note": "'People of the longhouse'.",
                "source_ids": [S_HAUD_OFFICIAL]},
               {"name": "Iroquois", "kind": "exonym",
                "note": "A French colonial coinage with no settled etymology; the commonest "
                        "derivation is a Huron term used by an enemy nation.",
                "source_ids": [S_NYSM_MOHAWK]},
               {"name": "Iroquois Confederacy", "kind": "historical", "to": 1990},
               {"name": "Six Nations", "kind": "common"},
           ],
           start_dating_method=TYP,
           standing="majority", date_precision="disputed", as_of=CHECKED,
           date_note="The founding date is genuinely unresolved. The archaeological mainstream "
                     "places it in the 1450s; Mann and Fields argued for 1142 from oral "
                     "tradition and a solar eclipse, and drew a published rebuttal.",
           source_ids=[S_HAUD_OFFICIAL, S_NYSM_MOHAWK, S_MANN_FIELDS, S_ESCHOLARSHIP_MYTH],
           alternatives=[
               {"label": "Founded 1142 (eclipse dating)", "standing": "minority",
                "start_year": 1142,
                "note": "Mann and Fields, from oral tradition plus the August 1142 solar "
                        "eclipse. A dedicated rebuttal disputes the method.",
                "source_ids": [S_MANN_FIELDS, S_ESCHOLARSHIP_MYTH]},
           ])

    enrich("americas.north.mississippian",
           start_dating_method=C14, end_dating_method=C14,
           standing="majority", date_precision="century",
           source_ids=[S_BRIT_CAHOKIA])

    # --------------------------------------------- the childless capitals

    P("cahokia", "Cahokia", "americas.north.mississippian", 950, 1350, "foundational",
      summary="The largest pre-Columbian settlement north of Mexico, and the reason "
              "'Mississippian' names a civilization rather than a pottery style.",
      start_dating_method=C14, end_dating_method=C14,
      standing="majority", date_precision="century",
      date_note="First occupied around 700 CE, with the florescence conventionally placed "
                "between about 950 and 1350.",
      source_ids=[S_BRIT_CAHOKIA])

    P("chaco", "Chaco Canyon", "americas.north.ancestral-puebloan", 850, 1250, "foundational",
      summary="The administrative and ceremonial centre of the Ancestral Puebloan world, "
              "linked by engineered roads across the San Juan Basin.",
      start_dating_method=DENDRO, end_dating_method=DENDRO,
      standing="majority", date_precision="century",
      date_note="Chaco's great houses are dated by tree rings, often to the year and "
                "sometimes to the felling season -- among the most precisely dated "
                "architecture anywhere before written records.",
      source_ids=[S_BRIT_CHACO])

    P("tenochtitlan", "Tenochtitlan", "americas.mesoamerica.aztec", 1325, 1521, "foundational",
      native="Mēxihco-Tenōchtitlan",
      summary="The island capital of the Mexica, and one of the largest cities in the world "
              "when Cortés reached it.",
      start_dating_method=CAL, end_dating_method=CAL,
      standing="majority", date_precision="year",
      date_note="1325 is the traditional founding date. The city fell on 13 August 1521. It "
                "predates the Triple Alliance by a century: the capital is older than the "
                "empire it came to head.",
      allow_outside_parent_dates=True,
      caveats=[{"kind": "misconception",
                "text": "1325 is a traditional date from Mexica accounts, not an "
                        "archaeological one.",
                "source_ids": [S_BRIT_TENOCHTITLAN]}],
      source_ids=[S_BRIT_TENOCHTITLAN])

    P("monte-alban", "Monte Albán", "americas.mesoamerica.zapotec", -500, 900, "intermediate",
      summary="The Zapotec capital on a levelled mountaintop above the Oaxaca valley.",
      start_dating_method=C14, end_dating_method=C14,
      standing="majority", date_precision="century",
      date_note="Rose to regional prominence around 500 BCE with its Classic floruit between "
                "about 300 and 900 CE.",
      source_ids=[S_BRIT_MONTE_ALBAN])

    P("tikal", "Tikal", "americas.mesoamerica.maya.classic", 600, 900, "intermediate",
      summary="The largest excavated Classic Maya city, and the clearest single illustration "
              "that the Maya were never one empire.",
      start_dating_method=C14, end_dating_method=C14,
      standing="majority", date_precision="century",
      source_ids=[S_SMARTHISTORY_MAYA, S_BRIT_MAYA])

    P("machu-picchu", "Machu Picchu", "americas.andes.inca", 1450, 1572, "intermediate",
      summary="A royal estate on the Vilcabamba ridge, built under Pachacuti and abandoned "
              "within a century of Spanish arrival.",
      start_dating_method=C14, end_dating_method=CAL,
      standing="majority", date_precision="approx",
      date_note="Construction is conventionally placed around 1450, in Pachacuti's reign. "
                "The site outlasts the empire: it is tied to Vilcabamba, which held out "
                "until 1572.",
      allow_outside_parent_dates=True,
      source_ids=[S_BRIT_INCA])

    P("qhapaq-nan", "Qhapaq Ñan", "americas.andes.inca", 1438, 1533, "intermediate",
      native="Qhapaq Ñan",
      summary="The Andean road network that made the empire governable, running some 30,000 "
              "kilometres across six modern countries.",
      start_dating_method=CAL, end_dating_method=CAL,
      standing="majority", date_precision="approx",
      date_note="Built largely under the empire but incorporating far older routes, which is "
                "why the inscribed network is described as a cultural route rather than an "
                "Inca invention.",
      source_ids=[S_UNESCO_QHAPAQ])
