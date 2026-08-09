"""Predynastic Egypt: the Naqada sequence, and how fast a state can appear.

Research in `docs/egypt-research.md`.

`africa.nile.egypt.predynastic` held 6000-3100 BCE with no children, which meant
the dataset had Narmer but nothing he came out of.

The organising finding is Dee et al.'s 2013 Bayesian radiocarbon model: 186
dates across ten linked sub-models, which compressed the whole run from
pre-state to unified state into roughly **600-700 years**, and set that beside
Southwest Asia, where the same journey from cereal agriculture to statehood took
about **4,000-5,000**. The dataset can now show both ends of that comparison,
because the Uruk period was authored one release earlier. At the finest
resolution the model resolves the assimilation of Upper and Lower Egyptian
funerary practice to about five or six generations.

That model also moved dates. The Badarian ended in the 38th century BC, two to
three hundred years later than typological estimates had it, and the Naqada
IB/IC transition moved by centuries too. Where a museum round number and a
modelled radiocarbon range disagree here, the modelled range wins and the round
number is recorded as what it is.

**The Narmer Palette is authored as iconography, not as a record of conquest.**
It is one of the most over-read objects in archaeology. Scholarship is genuinely
split between a historical-event reading and a ceremonial one, Tell el-Farkha
shows no invasion layer in the Delta, and the Maadi-Buto material culture had
already been absorbed centuries earlier and gradually. The palette proves a
kingship ideology existed by about 3100 BC. It does not date a unification, or
establish that unification was an event.

Already in the dataset and therefore NOT authored again: the Green Sahara, Nabta
Playa with its three sub-phases, and the Fayum Neolithic. The East Asia pass
taught this lesson — check what exists before authoring from a brief.

Deliberately NOT authored: any single Merimde range, because published
radiocarbon for that site genuinely varies by several centuries across research
groups, so it ships with a wide range and says why.
"""

from builders import make_builders

S_DEE_2013 = "dee-2013-absolute-chronology-early-egypt"
S_ROYAL_SOC = "royal-society-2013-early-egyptian-timeline"
S_WENGROW_UCL = "wengrow-radiocarbon-naqada-relative-chronology"
S_UCL_DIGITAL = "ucl-digital-egypt-predynastic-chronology"
S_BM_EARLY_EGYPT = "british-museum-early-egypt-gallery"
S_SESHAT_NAQADA = "seshat-naqada-polity"
S_DAI_ABYDOS = "dai-abydos-radiocarbon"
S_CAMB_STATE = "cambridge-emergence-egyptian-state"
S_SMARTHISTORY = "smarthistory-narmer-palette"
S_BAS_NARMER = "bas-narmers-enigmatic-palette"
S_ONE_PALETTE = "one-palette-two-lands"
S_RAFFAELE = "raffaele-dynasty-0"
S_UEE_CHRON = "ucla-encyclopedia-egyptology-chronology"
S_FAHMY_HK6 = "fahmy-hierakonpolis-hk6-archaeobotany"
S_NEKHEN_NEWS = "hierakonpolis-nekhen-news"
S_ROWLAND_MERIMDE = "rowland-merimde-new-perspectives"
S_VIENNA_OMARI = "vienna-el-omari-radiocarbon"
S_MAADI_BUTO = "maadi-buto-dissertation"

EGYPT_SOURCES = [
    {"id": S_DEE_2013, "kind": "scholarly",
     "citation": "Dee, Wengrow, Shortland, Stevenson, Brock, Girdland Flink & Bronk Ramsey, 'An absolute chronology for early Egypt using radiocarbon dating and Bayesian statistical modelling', Proceedings of the Royal Society A 469 (2013)",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3780825/",
     "note": "186 radiocarbon dates in ten linked OxCal sub-models. Concludes the pre-state "
             "to state transition took 600-700 years, against roughly 4,000-5,000 in "
             "Southwest Asia."},
    {"id": S_ROYAL_SOC, "kind": "press",
     "citation": "The Royal Society, 'Early Egyptian timeline' news release (2013)",
     "url": "https://royalsociety.org/news/2013/early-egyptian-timeline/"},
    {"id": S_WENGROW_UCL, "kind": "scholarly",
     "citation": "Wengrow et al., 'Radiocarbon Dating and the Naqada Relative Chronology' (UCL Discovery)",
     "url": "https://discovery.ucl.ac.uk/"},
    {"id": S_UCL_DIGITAL, "kind": "reference",
     "citation": "UCL Digital Egypt, 'Predynastic chronology' and 'Sequence Dates'",
     "url": "https://www.ucl.ac.uk/museums-static/digitalegypt/naqadan/chronology.html",
     "note": "Petrie's Sequence Dating is a relative seriation on an SD 30-80 scale, not an "
             "absolute calendar."},
    {"id": S_BM_EARLY_EGYPT, "kind": "reference",
     "citation": "British Museum, 'Early Egypt' gallery",
     "url": "https://www.britishmuseum.org/collection/galleries/early-egypt"},
    {"id": S_SESHAT_NAQADA, "kind": "reference",
     "citation": "Seshat Global History Databank, Naqada polity",
     "url": "https://www.seshat-db.com/core/polity/511"},
    {"id": S_DAI_ABYDOS, "kind": "scholarly",
     "citation": "German Archaeological Institute, radiocarbon dates from Abydos Cemetery U, Radiocarbon",
     "url": "https://journals.uair.arizona.edu/index.php/radiocarbon/article/download/3738/3163",
     "note": "The excavators' own First Dynasty dates came out 100-150 years earlier than the "
             "standard king-list chronology while staying internally consistent."},
    {"id": S_CAMB_STATE, "kind": "scholarly",
     "citation": "'The Emergence of the Egyptian State', in The Cambridge World Prehistory",
     "url": "https://www.cambridge.org/core/books/abs/cambridge-world-prehistory/emergence-of-the-egyptian-state/EFC256E863656A77F3A534D93A78FA74"},
    {"id": S_SMARTHISTORY, "kind": "reference",
     "citation": "Smarthistory, 'Palette of King Narmer'",
     "url": "https://smarthistory.org/palette-of-king-narmer/"},
    {"id": S_BAS_NARMER, "kind": "scholarly",
     "citation": "Biblical Archaeology Society Library, 'Narmer's Enigmatic Palette'",
     "url": "https://library.biblicalarchaeology.org/article/narmers-enigmatic-palette/",
     "note": "Baines reads it as ritual affirmation of conquest rather than a real event; "
             "Yurco reads Narmer as conqueror of the Delta."},
    {"id": S_ONE_PALETTE, "kind": "scholarly",
     "citation": "'One Palette, Two Lands', on the Narmer Palette and unification",
     "url": "https://www.academia.edu/10220097/",
     "note": "Notes Tell el-Farkha shows no invasion layer in the Delta."},
    {"id": S_RAFFAELE, "kind": "scholarly",
     "citation": "Raffaele, 'Dynasty 0', Aegyptiaca Helvetica 17",
     "url": "https://digilander.libero.it/peribsen/Dynasty0-Raffaele_AH17.pdf"},
    {"id": S_UEE_CHRON, "kind": "scholarly",
     "citation": "UCLA Encyclopedia of Egyptology, chronology resource",
     "url": "https://www.uee.ucla.edu/chronology"},
    {"id": S_FAHMY_HK6, "kind": "scholarly",
     "citation": "Fahmy et al., archaeobotany of the HK6 cemetery at Hierakonpolis, Archéo-Nil",
     "url": "https://www.archeonil.com/images/revue%202008%202010/AN2008-11-Fahmy%20et%20al.pdf"},
    {"id": S_NEKHEN_NEWS, "kind": "scholarly",
     "citation": "Hierakonpolis Expedition, Nekhen News (1998)",
     "url": "http://www.hierakonpolis-online.org/nekhennews/nn-10-1998.pdf"},
    {"id": S_ROWLAND_MERIMDE, "kind": "scholarly",
     "citation": "Rowland, 'New Perspectives and Methods' on Merimde Beni Salama (University of Edinburgh)",
     "url": "https://www.pure.ed.ac.uk/ws/portalfiles/portal/265345066/RowlandJ2020NewPerspectives.pdf"},
    {"id": S_VIENNA_OMARI, "kind": "scholarly",
     "citation": "University of Vienna repository, on the Lower Egyptian Neolithic sequence",
     "url": "https://uscholar.univie.ac.at/detail/o:1079992.pdf",
     "note": "Places el-Omari at the end of the northern Early Neolithic, 4600-4400 cal BC."},
    {"id": S_MAADI_BUTO, "kind": "scholarly",
     "citation": "Dissertation on the Maadi-Buto culture (German National Library)",
     "url": "https://d-nb.info/1337905968/34"},
]

CHECKED = "2026-08-08"
C14 = "radiocarbon-calibrated"
TYPO = "typological"


def extend(E, entities):
    _, P, ERA, EVENT, _, _ = make_builders(E)
    pre = "africa.nile.egypt.predynastic"

    # -------------------------------------------------- Upper Egypt sequence

    P("badarian", "Badarian Culture", pre, -4350, -3730, "intermediate",
      summary="The earliest well-defined farming culture of Upper Egypt, and the first "
              "casualty of the 2013 radiocarbon model.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="Bayesian radiocarbon gives a start of 4407-4308 and an end of 3800-3667 BCE "
                "at 68% probability, with a modelled duration of 529-709 years.",
      caveats=[{"kind": "misconception",
                "text": "The Badarian ended in the 38th century BC, two to three hundred years "
                        "later than typological estimates had it. Ranges like 4800-4200 BC "
                        "still circulate on museum material.",
                "source_ids": [S_DEE_2013, S_WENGROW_UCL]}],
      source_ids=[S_DEE_2013, S_WENGROW_UCL])

    P("naqada-i", "Naqada I", pre, -3800, -3550, "intermediate",
      summary="The first phase of the Naqada sequence: black-topped pottery, white "
              "cross-lined ware, and the beginnings of a distinctly Upper Egyptian world.",
      aliases=["Amratian"],
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="Petrie's Sequence Dating placed this at SD 31-37, which is a relative "
                "seriation and not a calendar at all. Bayesian radiocarbon pins the Naqada "
                "IB/IC transition to 3690-3605 BCE, centuries later than typological "
                "estimates.",
      caveats=[{"kind": "misconception",
                "text": "Round figures like 4000-3500 BC are conversions of a relative "
                        "seriation, not measurements. They are still printed on museum "
                        "education material.",
                "source_ids": [S_UCL_DIGITAL, S_DEE_2013]}],
      source_ids=[S_DEE_2013, S_UCL_DIGITAL, S_SESHAT_NAQADA, S_BM_EARLY_EGYPT])

    P("naqada-ii", "Naqada II", pre, -3550, -3325, "intermediate",
      summary="Trade networks widen, burials grow unequal, and Upper Egyptian material "
              "culture starts moving north into the Delta.",
      aliases=["Gerzean"],
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="The IID/IIIA transition is modelled at 3352-3297 BCE. The interval spanning "
                "the visible assimilation of Upper and Lower Egyptian funerary practice lasted "
                "about five or six generations.",
      source_ids=[S_DEE_2013, S_SESHAT_NAQADA, S_BM_EARLY_EGYPT])

    P("naqada-iii", "Naqada III", pre, -3325, -3085, "foundational",
      summary="State formation proper: walled towns, royal-scale tombs, the first writing, "
              "and the kings who came before the First Dynasty.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      allow_outside_parent_dates=True,
      date_note="Ends with the modelled accession of Aha at 3111-3045 BCE, median 3085. "
                "Before this model, published estimates for the foundation of the Egyptian "
                "state ranged across 3400-2900 BCE.",
      caveats=[{"kind": "misconception",
                "text": "Even radiocarbon programmes disagree. The Abydos excavators' own "
                        "First Dynasty dates came out 100-150 years earlier than the king-list "
                        "chronology, while staying internally consistent.",
                "source_ids": [S_DAI_ABYDOS]}],
      source_ids=[S_DEE_2013, S_DAI_ABYDOS, S_SESHAT_NAQADA])

    EVENT("state-formation", "The Speed of Egyptian State Formation", pre, -3800, -3085,
          "foundational",
          summary="Egypt went from pre-state to unified state in six or seven centuries, "
                  "where the same journey in Southwest Asia took four or five millennia.",
          start_dating_method=C14, end_dating_method=C14, standing="majority",
          date_precision="century",
          allow_outside_parent_dates=True,
          date_note="From a Bayesian model over 186 radiocarbon dates. The paper's conclusion "
                    "is comparative rather than merely chronological: prehistoric societies in "
                    "Africa and Asia followed very different trajectories to political "
                    "centralisation, and Egypt's was extraordinarily quick.",
          caveats=[{"kind": "misconception",
                    "text": "The contrast is with Southwest Asia measured the same way, from "
                            "cereal agriculture to state. Egypt started farming much later, so "
                            "it is the pace that differs, not the finish line.",
                    "source_ids": [S_DEE_2013]}],
          source_ids=[S_DEE_2013, S_ROYAL_SOC])

    # ------------------------------------------------------ places and things

    P("hierakonpolis", "Hierakonpolis", pre, -3700, -3050, "intermediate",
      summary="An Upper Egyptian power centre with monumental elite tombs, industrial-scale "
              "brewing, and buried elephants.",
      aliases=["Nekhen"],
      start_dating_method=TYPO, end_dating_method=TYPO, standing="majority",
      date_precision="century",
      date_note="The HK6 elite cemetery runs from about Naqada IIA through Naqada IIIC1. "
                "Dating is by Naqada-phase placement rather than radiocarbon, so sub-century "
                "precision for individual tombs should not be trusted.",
      caveats=[{"kind": "misconception",
                "text": "Predynastic Egypt is often told as one centre rising. Hierakonpolis, "
                        "Abydos and Naqada were competing or complementary centres, not a "
                        "single seat of authority.",
                "source_ids": [S_FAHMY_HK6, S_NEKHEN_NEWS]}],
      allow_outside_parent_dates=True,
      source_ids=[S_FAHMY_HK6, S_NEKHEN_NEWS])

    P("tomb-uj", "Tomb U-j at Abydos", pre, -3320, -3150, "foundational",
      summary="The richest tomb at Abydos before the First Dynasty, holding the earliest "
              "known Egyptian writing.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="Radiocarbon on wood from the tomb: Hd-12953 at 4470+/-30 BP calibrating to "
                "3310-3230, 3180-3160 and 3120-3030 cal BC; Hd-12954 at 4595+/-25 BP giving "
                "3490-3470 and 3380-3330 cal BC. Related Naqada IIIa2 tombs cluster around "
                "3510-3100 cal BC.",
      caveats=[{"kind": "misconception",
                "text": "Whether Egyptian writing was invented independently or prompted by "
                        "contact with Mesopotamia is not settled. The dates are close enough "
                        "that neither priority nor influence can be demonstrated.",
                "source_ids": [S_DAI_ABYDOS]}],
      source_ids=[S_DAI_ABYDOS])

    P("dynasty-0", "Dynasty 0", pre, -3200, -3085, "intermediate",
      summary="The rulers before the First Dynasty — Iry-Hor, Ka, Narmer — and the best "
              "argument that unification was a process rather than a moment.",
      start_dating_method=TYPO, end_dating_method=TYPO, standing="majority",
      date_precision="century",
      allow_outside_parent_dates=True,
      date_note="A modern historiographic label, not an Egyptian one, correlated with Naqada "
                "IIIB. The succession Iry-Hor, then Ka, then Narmer may include overlapping "
                "reigns.",
      caveats=[{"kind": "naming-confusion",
                "text": "Dynasty 0 and Dynasty 00 are not standardised. Scholars draw the "
                        "boundaries differently, and the order of the earliest rulers, known "
                        "mainly from serekhs on pots, is not secure.",
                "source_ids": [S_RAFFAELE, S_UEE_CHRON]}],
      source_ids=[S_RAFFAELE, S_UEE_CHRON])

    EVENT("narmer-palette", "The Narmer Palette", pre, -3100, None, "foundational",
          summary="A carved schist palette showing a king smiting an enemy, and probably the "
                  "most over-read object in Egyptology.",
          start_dating_method=TYPO, standing="majority", date_precision="century",
          allow_outside_parent_dates=True,
          date_note="Placed at Naqada IIIC1, about 3100 BC, on typological grounds.",
          alternatives=[
              {"label": "Records an actual conquest of the Delta", "standing": "minority",
               "note": "The historical-event reading, associated with Yurco. Long treated as "
                       "conclusive evidence for military unification under Narmer.",
               "source_ids": [S_BAS_NARMER, S_SMARTHISTORY]},
          ],
          caveats=[
              {"kind": "misconception",
               "text": "It does not date a unification or show one happened as an event. It "
                       "shows a smiting-and-dual-crown kingship ideology existed by about "
                       "3100 BC.",
               "source_ids": [S_CAMB_STATE, S_SMARTHISTORY]},
              {"kind": "misconception",
               "text": "Tell el-Farkha shows no invasion layer in the Delta, and Lower "
                       "Egyptian material culture had already been absorbed gradually, "
                       "centuries earlier.",
               "source_ids": [S_ONE_PALETTE, S_MAADI_BUTO]},
          ],
          as_of=CHECKED,
          source_ids=[S_CAMB_STATE, S_SMARTHISTORY, S_BAS_NARMER, S_ONE_PALETTE])

    # ------------------------------------------------------- Lower Egypt

    P("merimde", "Merimde Beni Salama", pre, -4900, -4200, "specialist",
      summary="One of the largest Neolithic settlements of the Delta, and a site whose "
              "published dates disagree by five hundred years.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="disputed",
      date_note="Published ranges include 5300-4200, 4900-4000, 4880-4250 and 4750-4250 BC "
                "across different research groups and sample series. The wide range here is "
                "deliberate: no tighter figure is defensible.",
      source_ids=[S_ROWLAND_MERIMDE])

    P("el-omari", "El-Omari", pre, -4600, -4400, "specialist",
      summary="A Lower Egyptian Neolithic settlement near Helwan, plainer in its material "
              "culture than its Upper Egyptian contemporaries.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Published radiocarbon places it at the end of the northern Early Neolithic "
                "sequence, between 4600 and 4400 cal BC, with some sources extending to 4300.",
      source_ids=[S_VIENNA_OMARI])

    P("maadi-buto", "Maadi-Buto Culture", pre, -3900, -3200, "intermediate",
      summary="The last independent culture of Lower Egypt, absorbed into the expanding "
              "Naqada world well before any king unified anything.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="Radiocarbon places the culture at roughly 3900-3300/3200 BC, with Buto I "
                "about 3900-3800 and the Maadi phase about 3800-3600. The transitional layer "
                "in which Naqada material replaces it falls about 3300-3200 BC.",
      caveats=[{"kind": "misconception",
                "text": "This replacement is often told as the unification, coincident with "
                        "Narmer. The excavated dates put it centuries earlier and show it "
                        "happening gradually.",
                "source_ids": [S_MAADI_BUTO]}],
      source_ids=[S_MAADI_BUTO])
