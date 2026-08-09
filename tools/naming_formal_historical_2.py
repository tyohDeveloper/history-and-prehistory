"""More formal and historical names: rulers who changed theirs, and a name that is an argument.

A second tranche. The first covered states; this one covers people, peoples and
one event whose name is the whole historiographical dispute in miniature.

**The Indian Rebellion of 1857 is the sharpest naming case in the dataset.**
Every available label is a verdict. The British called it the Sepoy Mutiny,
which says it was a breach of military discipline. Savarkar called it the First
War of Independence in 1909, which says it was a national liberation struggle.
S. N. Sen, writing the official centenary history, concluded it began as a fight
for religion and ended as a war of independence. Punjabi historians object that
the First Anglo-Sikh War has the better claim to "first", South Indian
historians point to the Vellore Mutiny, and the broad modern position is that it
was not nationalist in the modern sense at all. Naming it is taking a side, and
the entity now says so instead of quietly picking one.

**Two rulers changed their own names, on a date.**

* **Octavian became Augustus** when the Senate conferred the title, 16 January
  27 BCE by most accounts and 17 January in the 1911 Britannica. He had
  considered "Romulus" and rejected it -- too close to king. The dataset already
  filed him as "Augustus" with "Octavian" as a flat alias, which flattened a
  deliberate political act into a spelling variant.
* **Amenhotep IV became Akhenaten** in his fifth regnal year, when he made the
  Aten sole god and moved the court to Amarna. The Met traces the change through
  the boundary stelae; UCL's Digital Egypt puts it in year six. Both are
  recorded.

**Caligula never was Caligula.** He was Gaius. "Little boot" was a soldiers'
nickname from his childhood in camp, and the sources say he disliked it. The
dataset had it as the display name with "Gaius" as an alias, which is the right
way round for findability and the wrong way round for accuracy -- so the
nickname stays in the title and now carries a note saying what it is.

**Greek is the reason several Egyptians have two names.** Cheops, Chephren and
Ozymandias are Herodotus and Diodorus rendering Khufu, Khafre and User-maat-re
into Greek, and Europe inherited the Greek. Those are `exonym`, not spelling
variants.

**Java Man and Peking Man** are superseded taxonomic names -- *Pithecanthropus
erectus* and *Sinanthropus pekinensis* -- folded into *Homo erectus*. That is a
third thing again: not an exonym, not a rename, but a classification that lost.
`historical` with a note carries it.

Honorifics get `common` with a note rather than a kind of their own. Mahatma,
Netaji, Quaid-e-Azam and Bangabandhu are titles, not names, and a reader
searching any of them should land on the person -- but adding an `honorific`
kind for four entities would be inventing vocabulary ahead of need.
"""

S_MET_AKHENATEN = "met-amenhotep-iv-akhenaten"
S_ARCE_AKHENATEN = "arce-akhenaten-revolution"
S_UCL_AKHNATON = "ucl-digital-egypt-akhnaton"
S_BRIT_AKHENATEN = "britannica-akhenaten-amarna"
S_AUGUSTUS_TITLE = "augustus-title-27bc"
S_EB1911_AUGUSTUS = "eb1911-augustus"
S_PUNJAB_1857 = "punjab-university-names-1857"
S_NBU_1857 = "nbu-hundred-fifty-years-1857"
S_BROWN_SEPOYS = "brown-insurgent-sepoys-review"

NAMING_2_SOURCES = [
    {"id": S_MET_AKHENATEN, "kind": "institutional",
     "citation": "'Art, Architecture, and the City in the Reign of Amenhotep IV / Akhenaten', The Metropolitan Museum of Art",
     "url": "https://www.metmuseum.org/essays/art-architecture-and-the-city-in-the-reign-of-amenhotep-iv-akhenaten-ca-13531336-b-c",
     "note": "Traces the change through the Amarna boundary stelae: the name had changed by "
             "the time the oath was recorded, early in or just after year five."},
    {"id": S_ARCE_AKHENATEN, "kind": "institutional",
     "citation": "'Akhenaten: The Mysteries of Religious Revolution', American Research Center in Egypt",
     "url": "https://arce.org/resource/akhenaten-mysteries-religious-revolution/",
     "note": "Amenhotep means 'Amun is satisfied'; Akhenaten means 'effective for Aten'. The "
             "change is the religious programme in miniature."},
    {"id": S_UCL_AKHNATON, "kind": "institutional",
     "citation": "'Akhnaton', Digital Egypt for Universities, University College London",
     "url": "https://www.ucl.ac.uk/museums-static/digitalegypt/chronology/akhnaton.html",
     "note": "Places the name change in the sixth regnal year rather than the fifth."},
    {"id": S_BRIT_AKHENATEN, "kind": "reference",
     "citation": "'Akhenaten: Move to Akhetaton', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/biography/Akhenaten/Move-to-Akhetaton"},
    {"id": S_AUGUSTUS_TITLE, "kind": "reference",
     "citation": "'Augustus (title)', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Augustus_(title)",
     "note": "Renamed by the Senate on 16 January 27 BC; 'Romulus' had been considered and "
             "rejected. Full style Imperator Caesar Divi Filius Augustus."},
    {"id": S_EB1911_AUGUSTUS, "kind": "reference",
     "citation": "'Augustus', 1911 Encyclopaedia Britannica",
     "url": "https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica/Augustus",
     "note": "Gives 17 January 27 BCE for the conferral, four days after the civic crown of "
             "13 January."},
    {"id": S_PUNJAB_1857, "kind": "scholarly",
     "citation": "Soharwardi, 'The significance of the different names of the 1857 uprising', University of the Punjab",
     "url": "https://pu.edu.pk/images/journal/pols/pdf-files/Soharwardi_v20_1_2013.pdf",
     "note": "Groups the labels into four families -- mutiny, uprising, war of independence, "
             "revolution -- and treats the choice as political."},
    {"id": S_NBU_1857, "kind": "scholarly",
     "citation": "'Hundred and Fifty years of the Revolt of 1857', University of North Bengal",
     "url": "https://ir.nbu.ac.in/server/api/core/bitstreams/25efaf92-5fe4-4201-82c8-c1411f0f6928/content",
     "note": "Savarkar was probably the first to call it a war of independence; S. N. Sen and "
             "others rejected the label, and a consensus has grown that it was not nationalist "
             "in the modern sense."},
    {"id": S_BROWN_SEPOYS, "kind": "scholarly",
     "citation": "Review of Mazumdar, Insurgent Sepoys: Europe Views the Revolt, e-Journal of Portuguese History (Brown University)",
     "url": "https://www.brown.edu/Departments/Portuguese_Brazilian_Studies/ejph/html/issue19/pdf/v10n1a06.pdf",
     "note": "The event 'has been named in many different ways depending on the perspective of "
             "who is naming it'."},
]

CHECKED = "2026-08-09"


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}

    def forms(eid, name_forms, name=None, native=None, caveat=None, sources=None,
              **extra):
        e = by_id.get(eid)
        if e is None:
            return
        if name is not None:
            e["name"] = name
        if native is not None:
            e["native_name"] = native
        e["name_forms"] = name_forms
        for k, v in extra.items():
            e[k] = v
        if caveat is not None:
            e["caveats"] = [c for c in e.get("caveats", [])
                            if c.get("kind") != caveat["kind"]] + [caveat]
        if sources:
            e["source_ids"] = sorted(set(list(e.get("source_ids", [])) + sources))

    # ------------------------------------------ a name that is an argument

    forms("south-asia.east-india-company.rebellion-1857",
          name_forms=[
              {"name": "Sepoy Mutiny", "kind": "historical",
               "note": "The British name. Calling it a mutiny says it was a breach of military "
                       "discipline rather than a political rising.",
               "source_ids": [S_PUNJAB_1857, S_NBU_1857]},
              {"name": "Indian Mutiny", "kind": "historical",
               "source_ids": [S_PUNJAB_1857]},
              {"name": "First War of Independence", "kind": "common", "from": 1909,
               "note": "Savarkar's name, and the usual one in India and Pakistan. It says the "
                       "rising was a national liberation struggle.",
               "source_ids": [S_NBU_1857]},
              {"name": "Great Rebellion", "kind": "scholarly",
               "source_ids": [S_PUNJAB_1857]},
              {"name": "Revolt of 1857", "kind": "scholarly",
               "note": "Preferred by writers who find both 'mutiny' and 'war of independence' "
                       "tendentious.",
               "source_ids": [S_PUNJAB_1857]},
          ],
          caveat={"kind": "naming-confusion",
                  "text": "Every name for this is a verdict on it. 'Mutiny' makes it "
                          "indiscipline, 'First War of Independence' makes it national "
                          "liberation, and historians have not settled which it was.",
                  "source_ids": [S_PUNJAB_1857, S_NBU_1857, S_BROWN_SEPOYS]},
          as_of=CHECKED,
          date_note="The dates are not in dispute; the name and the interpretation are. The "
                    "alternatives below are positions on what this was, not on when.",
          alternatives=[
              {"label": "Not a war of independence", "standing": "majority",
               "note": "S. N. Sen's official centenary history and most later work hold it "
                       "was not nationalist in the modern sense.",
               "source_ids": [S_NBU_1857]},
              {"label": "Not the first: the Anglo-Sikh War or the Vellore Mutiny",
               "standing": "minority",
               "note": "Punjabi and South Indian historians dispute the word 'first' rather "
                       "than the words after it.",
               "source_ids": [S_NBU_1857]},
          ],
          sources=[S_PUNJAB_1857, S_NBU_1857, S_BROWN_SEPOYS])

    # --------------------------------------- rulers who changed their names

    forms("europe.mediterranean.rome.empire.augustus",
          name_forms=[
              {"name": "Octavian", "kind": "historical", "to": -27,
               "note": "His name until the Senate conferred Augustus on 16 January 27 BCE. "
                       "The 1911 Britannica gives 17 January.",
               "source_ids": [S_AUGUSTUS_TITLE, S_EB1911_AUGUSTUS]},
              {"name": "Gaius Octavius", "kind": "historical", "to": -44,
               "note": "His birth name, before Caesar's will adopted him.",
               "source_ids": [S_AUGUSTUS_TITLE]},
              {"name": "Imperator Caesar Divi Filius Augustus", "kind": "formal", "lang": "la",
               "source_ids": [S_AUGUSTUS_TITLE]},
          ],
          caveat={"kind": "naming-confusion",
                  "text": "Augustus is a title the Senate voted him, not a name he was born "
                          "with. He had considered Romulus and rejected it as too close to "
                          "king.",
                  "source_ids": [S_AUGUSTUS_TITLE]},
          sources=[S_AUGUSTUS_TITLE, S_EB1911_AUGUSTUS])

    forms("africa.nile.egypt.new-kingdom.dyn18.akhenaten",
          name_forms=[
              {"name": "Amenhotep IV", "kind": "historical",
               "note": "His name for the first five years. 'Amun is satisfied' -- which is "
                       "precisely the god he then abolished.",
               "source_ids": [S_ARCE_AKHENATEN, S_BRIT_AKHENATEN]},
              {"name": "Akhenaten", "kind": "endonym",
               "note": "'Effective for the Aten', adopted with the new religion.",
               "source_ids": [S_ARCE_AKHENATEN]},
              {"name": "Amenophis IV", "kind": "exonym", "lang": "grc",
               "note": "The Hellenised form."},
              {"name": "Ikhnaton", "kind": "translation"},
          ],
          caveat={"kind": "naming-confusion",
                  "text": "He changed his own name in regnal year five, from one honouring "
                          "Amun to one honouring the Aten. UCL puts the change in year six.",
                  "source_ids": [S_MET_AKHENATEN, S_UCL_AKHNATON]},
          as_of=CHECKED,
          date_note="The reign dates are conventional New Kingdom chronology. The alternative "
                    "below concerns when within the reign he changed his name, not when the "
                    "reign began.",
          alternatives=[
              {"label": "Name changed in regnal year six", "standing": "minority",
               "note": "UCL's Digital Egypt dates the change a year later than Britannica, "
                       "ARCE and the Met.",
               "source_ids": [S_UCL_AKHNATON]},
          ],
          sources=[S_MET_AKHENATEN, S_ARCE_AKHENATEN, S_UCL_AKHNATON, S_BRIT_AKHENATEN])

    forms("europe.mediterranean.rome.empire.caligula",
          name_forms=[
              {"name": "Gaius", "kind": "endonym",
               "note": "His actual name: Gaius Julius Caesar Augustus Germanicus."},
              {"name": "Caligula", "kind": "common",
               "note": "'Little boot', a soldiers' nickname from his childhood in camp. The "
                       "sources say he disliked it, and it is how history knows him."},
          ])

    forms("europe.mediterranean.macedon.alexander",
          name_forms=[
              {"name": "Alexander III of Macedon", "kind": "formal"},
              {"name": "Alexander the Great", "kind": "common"},
              {"name": "Ἀλέξανδρος", "kind": "endonym", "lang": "grc"},
              {"name": "Iskandar", "kind": "exonym", "lang": "fa",
               "note": "The Persian and later Islamic form, through which he entered a very "
                       "different body of legend."},
          ])

    # ------------------------------------- Greek is why they have two names

    for eid, greek, egyptian in (
        ("africa.nile.egypt.old-kingdom.dyn4.khufu", "Cheops", "Khufu"),
        ("africa.nile.egypt.old-kingdom.dyn4.khafre", "Chephren", "Khafre"),
    ):
        forms(eid, name_forms=[
            {"name": egyptian, "kind": "endonym", "lang": "egy"},
            {"name": greek, "kind": "exonym", "lang": "grc",
             "note": "Herodotus's rendering, which is how Europe learned the name."},
        ])

    forms("africa.nile.egypt.new-kingdom.dyn19.ramesses2",
          name_forms=[
              {"name": "Ramesses II", "kind": "endonym", "lang": "egy"},
              {"name": "Ramesses the Great", "kind": "common"},
              {"name": "Ozymandias", "kind": "exonym", "lang": "grc",
               "note": "A Greek rendering of his throne name User-maat-re, and the name under "
                       "which Shelley made him a byword for ruined ambition."},
          ])

    # --------------------------------------- peoples, places and taxa

    forms("africa.nile.egypt",
          native="Kemet",
          name_forms=[
              {"name": "Kemet", "kind": "endonym", "lang": "egy",
               "note": "'The black land', for the Nile silt as against the red desert."},
              {"name": "Pharaonic Egypt", "kind": "scholarly"},
              {"name": "Nile Valley civilization", "kind": "scholarly"},
              {"name": "Aigyptos", "kind": "exonym", "lang": "grc",
               "note": "The Greek from which every European name for the country descends."},
          ])

    forms("africa.west.ghana",
          name_forms=[
              {"name": "Wagadu", "kind": "endonym",
               "note": "What its own people called it. 'Ghana' was the title of its ruler."},
              {"name": "Ghana Empire", "kind": "common"},
          ])

    forms("africa.nile.kush",
          name_forms=[
              {"name": "Kush", "kind": "endonym"},
              {"name": "Nubia", "kind": "exonym",
               "note": "A regional name rather than a synonym: Nubia is the territory, Kush "
                       "the kingdom."},
              {"name": "Aethiopia", "kind": "exonym", "lang": "grc",
               "note": "The Greek name for the lands south of Egypt, unrelated to modern "
                       "Ethiopia."},
          ])

    forms("west-asia.arabia.pre-islamic.saba",
          name_forms=[
              {"name": "Saba", "kind": "endonym"},
              {"name": "Sheba", "kind": "exonym",
               "note": "The biblical form, which carried the kingdom into European tradition "
                       "attached to a queen the Sabaean sources do not name."},
          ])

    forms("west-asia.anatolia.troy",
          name_forms=[
              {"name": "Ilion", "kind": "endonym", "lang": "grc",
               "note": "The name behind the Iliad; Wilusa in Hittite records."},
              {"name": "Troy", "kind": "common"},
              {"name": "Hisarlik", "kind": "common", "lang": "tr",
               "note": "The modern Turkish name of the mound. Excavation reports use it "
                       "precisely because it does not assume the identification."},
          ])

    forms("south-asia.indus",
          name_forms=[
              {"name": "Harappan Civilization", "kind": "scholarly",
               "note": "Named for the first site excavated, which is convention rather than "
                       "precedence: Harappa was simply dug first."},
              {"name": "Indus Valley Civilization", "kind": "common"},
          ])

    forms("global.prehistory.hominins.homo-erectus",
          name_forms=[
              {"name": "Homo erectus", "kind": "scholarly"},
              {"name": "Pithecanthropus erectus", "kind": "historical",
               "note": "Dubois's 1894 genus for the Java find, later folded into Homo."},
              {"name": "Java Man", "kind": "historical",
               "note": "The popular name for that specimen."},
              {"name": "Sinanthropus pekinensis", "kind": "historical",
               "note": "The Zhoukoudian material, also later folded in."},
              {"name": "Peking Man", "kind": "historical"},
              {"name": "Homo ergaster", "kind": "scholarly",
               "note": "Used by those who separate the African material as its own species."},
          ])

    # ------------------------------- honorifics, filed as common with a note

    for eid, honorific, gloss in (
        ("south-asia.independence.gandhi", "Mahatma", "'Great soul', a title rather than a name"),
        ("south-asia.independence.jinnah", "Quaid-e-Azam", "'Great leader'"),
        ("south-asia.independence.subhas-bose", "Netaji", "'Respected leader'"),
        ("south-asia.independence.mujib", "Bangabandhu", "'Friend of Bengal'"),
    ):
        e = by_id.get(eid)
        if e is None:
            continue
        existing = [a for a in e.get("aliases", []) if a != honorific]
        forms(eid, name_forms=(
            [{"name": a, "kind": "formal"} for a in existing] +
            [{"name": honorific, "kind": "common", "note": f"{gloss}."}]
        ))
