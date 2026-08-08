"""The Indus Civilisation subdivided, and the Southern Neolithic added.

`tools/coverage.py --childless` had been reporting this for some time behind a
flag nobody passed: `south-asia.indus` held two thousand years, 3300-1300 BCE,
as a single entity with no children at all. The region x band matrix could not
see it, because an undifferentiated block counts as one entity in one band
exactly like a node that is properly subdivided. The flag is now on by default.

Research in `docs/southasia-research.md`.

Two things are worth stating about how this pass was authored.

**The "shorter chronology" is not a live dispute.** The research returned
Agrawal's 550-year Harappan span, 2300-1750 BC, as a competing modern claim.
It is *Science* 143(3609), published 28 February 1964 -- uncalibrated
radiocarbon from three years before Suess published the first calibration
curve. It is authored here as `superseded`, and kept rather than dropped
because it is the origin of the chronology debate and because a reader who
meets the figure elsewhere deserves to be told why it is short.

**Several researched sites are deliberately absent, for different reasons.**
*Kalibangan* has real published dates but this pass could only reach them
through an exam-cramming site and a course handout. *Ganweriwala* is barely
excavated and its one circulating date traces to Wikipedia. *Ochre Coloured
Pottery* and *Painted Grey Ware* both have genuinely scattered chronologies --
PGW proposals range from 2600 BCE to 1200 BCE, and the disagreement is partly
methodological (Libby versus Cambridge half-lives), which is not something to
paper over with a midpoint. They are left out and said so.

The 2026 Mohenjo-daro re-dating is included, but as an `alternative` rather
than as the entity's date, because it currently rests on press reporting of a
technical briefing rather than on a published paper.
"""

from builders import make_builders

S_HARAPPA_TRENCH = "harappa-test-trench-chronology"
S_KENOYER_2008 = "kenoyer-2008-indus-cities"
S_AGRAWAL_1964 = "agrawal-1964-shorter-chronology"
S_DAWN_2026 = "dawn-2026-mohenjo-daro"
S_ARCHAEOLOGY_2026 = "archaeology-2026-mohenjo-daro"
S_SHINDE_2019 = "shinde-2019-rakhigarhi-genome"
S_NARASIMHAN_2019 = "narasimhan-2019-south-central-asia"
S_RAKHIGARHI_AMS = "kumar-rakhigarhi-radiocarbon"
S_LESHNIK_1968 = "leshnik-1968-lothal-dock"
S_GUPTA_2024 = "gupta-2024-lothal-geomorphology"
S_SENGUPTA_2020 = "sengupta-2020-dholavira"
S_STAUBWASSER_CP = "climate-of-the-past-2019-indus"
S_DROUGHT_2023 = "nature-ceenv-2023-drought-pulses"
S_GIOSAN_2018 = "giosan-2018-indus-neoglacial"
S_DAVE_2017 = "dave-2017-ghaggar-hakra"
S_FARMER_2004 = "farmer-sproat-witzel-2004"
S_RAO_2009 = "rao-2009-entropic-evidence"
S_SPROAT_2010 = "sproat-2010-indus-critique"
S_HARAPPA_WRITING = "harappa-oldest-indus-writing"
S_FULLER_2001 = "fuller-2001-southern-neolithic"
S_INFLIBNET_SN = "inflibnet-southern-neolithic-india"
S_BOIVIN_MPG = "boivin-fuller-korisettar-south-deccan"
S_RADIOCARBON_1965 = "radiocarbon-1965-tf-series"

INDUS_SOURCES = [
    {"id": S_HARAPPA_TRENCH, "kind": "scholarly",
     "citation": "Harappa Archaeological Research Project (Kenoyer & Meadow), 'Test Trench Chronology', harappa.com",
     "url": "https://www.harappa.com/beas/test-trench-chronology",
     "note": "Site-anchored sequence from more than seventy radiocarbon dates at Harappa. "
             "This, not any textbook, is where the familiar 2600-1900 BCE bracket comes from."},
    {"id": S_KENOYER_2008, "kind": "scholarly",
     "citation": "Kenoyer, 'Indus Urbanism: New Perspectives on its Origin and Character' (Sackler Colloquium, 2008)",
     "url": "https://www.harappa.com/sites/default/files/pdf/Kenoyer2008%20Indus%20Cities%20Sackler%20Colloquiumfinalrevised.pdf",
     "note": "'Initial urban development in the Indus region began between approximately "
             "2800 and 2600 BC during Early Harappan Kot Diji phase.'"},
    {"id": S_AGRAWAL_1964, "kind": "scholarly",
     "citation": "Agrawal, 'Harappa Culture: New Evidence for a Shorter Chronology', Science 143(3609), 28 February 1964",
     "url": "https://www.science.org/doi/10.1126/science.143.3609.950",
     "note": "'Radiocarbon dates suggest a total time spread of 550 years, from about 2300 "
             "to 1750 B.C.' Uncalibrated, and published before calibration curves existed."},
    {"id": S_DAWN_2026, "kind": "press",
     "citation": "Dawn, 'Fresh studies trace Mohenjo Daro's urban roots to 3300 BC', 25 March 2026",
     "url": "https://www.dawn.com/news/1985048",
     "note": "Press report of a technical briefing. No peer-reviewed paper had appeared as of this check."},
    {"id": S_ARCHAEOLOGY_2026, "kind": "press",
     "citation": "Archaeology Magazine, 'New Dates Push Back Occupation of Mohenjo-daro', 6 April 2026",
     "url": "https://archaeology.org/news/2026/04/06/new-dates-push-back-occupation-of-mohenjo-daro/"},
    {"id": S_SHINDE_2019, "kind": "scholarly",
     "citation": "Shinde, Narasimhan, Rohland et al., 'An Ancient Harappan Genome Lacks Ancestry from Steppe Pastoralists or Iranian Farmers', Cell 179 (2019)",
     "url": "https://reich.hms.harvard.edu/sites/reich.hms.harvard.edu/files/inline-files/2019_Cell_ShindeNarasimhan_Rakhigarhi_0.pdf",
     "note": "One individual, I6113. Of 61 skeletal samples attempted, only she yielded usable DNA."},
    {"id": S_NARASIMHAN_2019, "kind": "scholarly",
     "citation": "Narasimhan, Patterson, Moorjani et al., 'The formation of human populations in South and Central Asia', Science 365 (2019)",
     "url": "https://reich.hms.harvard.edu/sites/reich.hms.harvard.edu/files/inline-files/eaat7487.full_.pdf",
     "note": "The companion paper. States plainly that 'the path by which this ancestry "
             "arrived in South Asia is uncertain.'"},
    {"id": S_RAKHIGARHI_AMS, "kind": "scholarly",
     "citation": "Kumar et al., AMS radiocarbon dates from Rakhigarhi (Inter University Accelerator Centre, Delhi)",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5821334/"},
    {"id": S_LESHNIK_1968, "kind": "scholarly",
     "citation": "Leshnik, 'The Harappan Port at Lothal: Another View', American Anthropologist 70 (1968)",
     "url": "https://safarmer.com/Indo-Eurasian/Leshnik.pdf",
     "note": "The original argument that the basin was a reservoir rather than a dock."},
    {"id": S_GUPTA_2024, "kind": "scholarly",
     "citation": "Gupta, Prabhakar & Jain, Journal of Archaeological Science 170 (October 2024)",
     "url": "https://www.sciencedirect.com/science/article/abs/pii/S0305440324001146",
     "note": "Argues for the dockyard reading, while stating that 'the debate surrounding "
             "the function of this structure remains unresolved.'"},
    {"id": S_SENGUPTA_2020, "kind": "scholarly",
     "citation": "Sengupta et al., 'Did the Harappan settlement of Dholavira (India) collapse during the onset of Meghalayan stage drought?', Journal of Quaternary Science 35 (2020)",
     "url": "https://ui.adsabs.harvard.edu/abs/2020JQS....35..382S"},
    {"id": S_STAUBWASSER_CP, "kind": "scholarly",
     "citation": "Climate of the Past 15 (2019), NE Arabian Sea oxygen-isotope record",
     "url": "https://cp.copernicus.org/articles/15/73/2019/cp-15-73-2019.pdf"},
    {"id": S_DROUGHT_2023, "kind": "scholarly",
     "citation": "Communications Earth & Environment (2023), drought pulses at 4.19, 4.11 and 4.02 ka",
     "url": "https://www.nature.com/articles/s43247-023-00763-z"},
    {"id": S_GIOSAN_2018, "kind": "scholarly",
     "citation": "Giosan et al., 'Neoglacial climate anomalies and the Harappan metamorphosis', Climate of the Past 14 (2018)",
     "url": "https://discovery.ucl.ac.uk/id/eprint/10047870/7/Goisan_Indus-NeoGlacial_cp-14-1669-2018.pdf"},
    {"id": S_DAVE_2017, "kind": "scholarly",
     "citation": "Dave et al., 'A million-year-old river in the Thar', Scientific Reports 7 (2017)",
     "url": "https://www.nature.com/articles/s41598-017-05745-8",
     "note": "Nd/Sr isotopes on Rann of Kachchh cores: a Himalayan glacier-fed river reached "
             "the sea until roughly 10,000 years ago, well before the Harappan period."},
    {"id": S_FARMER_2004, "kind": "scholarly",
     "citation": "Farmer, Sproat & Witzel, 'The Collapse of the Indus-Script Thesis', Electronic Journal of Vedic Studies 11(2), 2004",
     "url": "https://etana.org/node/7709"},
    {"id": S_RAO_2009, "kind": "scholarly",
     "citation": "Rao, Yadav, Vahia et al., 'Entropic Evidence for Linguistic Structure in the Indus Script', Science 324 (2009)",
     "url": "https://www.science.org/doi/10.1126/science.1170391"},
    {"id": S_SPROAT_2010, "kind": "scholarly",
     "citation": "Sproat, 'Ancient Symbols, Computational Linguistics, and the Reviewing Practices of the General Science Journals', Computational Linguistics 36(4), 2010",
     "url": "https://aclanthology.org/J10-4017.pdf"},
    {"id": S_HARAPPA_WRITING, "kind": "scholarly",
     "citation": "Harappa Archaeological Research Project, 'How old is the oldest ancient Indus writing?'",
     "url": "https://www.harappa.com/answers/how-old-oldest-ancient-indus-writing"},
    {"id": S_FULLER_2001, "kind": "scholarly",
     "citation": "Fuller, 'Ashmounds and hilltop villages: the search for early agriculture in southern India' (EASAA 2001)",
     "url": "https://www.homepages.ucl.ac.uk/~tcrndfu/articles/EASAA2001a.pdf"},
    {"id": S_INFLIBNET_SN, "kind": "reference",
     "citation": "'The Southern Neolithic of India', INFLIBNET e-PG Pathshala chapter",
     "url": "https://ebooks.inflibnet.ac.in/icp02/chapter/87/"},
    {"id": S_BOIVIN_MPG, "kind": "scholarly",
     "citation": "Boivin, Fuller & Korisettar, on the South Deccan Neolithic (Max Planck Society repository)",
     "url": "https://pure.mpg.de/rest/items/item_2248630/component/file_2248629/content",
     "note": "Places the South Deccan Neolithic 'sometime in the 3rd millennium BC' -- "
             "explicitly not among the world's earliest, nor the earliest in South Asia."},
    {"id": S_RADIOCARBON_1965, "kind": "scholarly",
     "citation": "Tata Institute of Fundamental Research radiocarbon date list (TF series), Radiocarbon (1965)",
     "url": "https://journals.uair.arizona.edu/index.php/radiocarbon/article/viewFile/3302/2894",
     "note": "The original published lab table behind the Burzahom chronology."},
]

CHECKED = "2026-08-08"
C14 = "radiocarbon-calibrated"
C14U = "radiocarbon-uncalibrated"


def extend(E, entities):
    _, P, ERA, EVENT, _, _ = make_builders(E)
    ind = "south-asia.indus"
    sa = "south-asia"

    # ---------------------------------------------------------------- phases

    P("kot-diji", "Kot Dijian Phase", ind, -2800, -2600, "intermediate",
      summary="The Early Harappan phase in which the first city walls, the first writing "
              "and the first standardised crafts appear, before the mature cities.",
      aliases=["Early Harappan"],
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="From the Harappa test-trench sequence, which rests on more than seventy "
                "radiocarbon dates at the type site. Urbanism does not begin at 2600 BCE; "
                "it is already underway here.",
      source_ids=[S_HARAPPA_TRENCH, S_KENOYER_2008])

    P("mature", "Mature Harappan Phase", ind, -2600, -1900, "foundational",
      summary="The urban centuries: Mohenjo-daro and Harappa at full extent, with "
              "standardised weights, fired-brick drainage and long-distance trade.",
      aliases=["Integration Era", "Harappan Phase"],
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="Subdivided at Harappa into 3A (2600-2450), 3B (2450-2200) and 3C "
                "(2200-1900 cal BC). A Cambridge scheme starts the preceding Early Harappan "
                "at 3200 rather than 3300 BC; the difference is not resolved here. Note "
                "that older Indus figures are often uncalibrated; calibration alone moves "
                "some site chronologies by centuries, so check the frame before comparing.",
      alternatives=[
          {"label": "Shorter chronology, 2300-1750 BC", "standing": "superseded",
           "start_year": -2300, "end_year": -1750, "dating_method": C14U,
           "note": "Agrawal's 550-year span, from Science in February 1964. Uncalibrated, "
                   "and published three years before the first calibration curve, which is "
                   "why it runs short.",
           "source_ids": [S_AGRAWAL_1964]},
      ],
      source_ids=[S_HARAPPA_TRENCH, S_KENOYER_2008, S_AGRAWAL_1964])

    P("late", "Late Harappan Phase", ind, -1800, -1300, "intermediate",
      summary="The post-urban centuries. The cities empty and the standardised material "
              "culture dissolves into regional styles, but settlement does not stop.",
      aliases=["Localization Era", "Post-urban Harappan"],
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="A transitional phase runs 1900-1800 cal BC between the mature and late "
                "periods at Harappa.",
      caveats=[{"kind": "misconception",
                "text": "Not a collapse into emptiness. Population shifted east and "
                        "settlement continued; what ends is the standardised urban system, "
                        "not occupation of the region.",
                "source_ids": [S_GIOSAN_2018]}],
      source_ids=[S_HARAPPA_TRENCH, S_KENOYER_2008])

    # ----------------------------------------------------------------- sites

    P("harappa", "Harappa", ind, -3300, -1300, "foundational",
      summary="The type site, and the best-dated one: a continuous sequence from the Ravi "
              "phase to Cemetery H, excavated 1986-1996.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="The sequence that anchors the whole field's chronology: Ravi/Hakra "
                "3300-2800, Kot Dijian 2800-2600, Harappan 2600-1900, transitional "
                "1900-1800, Late Harappan 1800-1300 cal BC.",
      source_ids=[S_HARAPPA_TRENCH])

    P("mohenjo-daro", "Mohenjo-daro", ind, -2600, -1900, "foundational",
      summary="The largest mature Harappan city, with the Great Bath, the citadel mound "
              "and a fired-brick drainage system running the length of its streets.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="The site's earliest levels sit below the water table and cannot be reached, "
                "so its own radiocarbon record is much thinner than Harappa's. The 2026 "
                "re-dating below is press reporting of a technical briefing rather than a "
                "published paper, with no lab numbers or calibration details released.",
      alternatives=[
          {"label": "Perimeter wall built 2708-2576 cal BCE", "standing": "minority",
           "start_year": -2708, "end_year": -2576, "dating_method": C14,
           "note": "New dates from the 2025-26 Sindh programme would put the first city "
                   "wall in the Kot Dijian phase, and reassign the structure Wheeler found "
                   "in 1950 from a flood bund to a defensive wall.",
           "source_ids": [S_DAWN_2026, S_ARCHAEOLOGY_2026]},
      ],
      as_of=CHECKED,
      source_ids=[S_HARAPPA_TRENCH, S_DAWN_2026, S_ARCHAEOLOGY_2026])

    P("dholavira", "Dholavira", ind, -3000, -1450, "intermediate",
      summary="A city in a desert with no perennial water, which survived on sixteen "
              "reservoirs covering a fifth of its walled area.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="Bisht's excavation report divides the site into seven stages from about "
                "3000 to 1450 BCE. A 2020 radiocarbon study instead runs the occupation from "
                "roughly 5500 to 3800 years BP, with collapse at 4300-4100 BP at the onset "
                "of the Meghalayan drought. The two do not fully reconcile, largely because "
                "the 2020 study reports 'years BP' without saying whether it is calibrated.",
      source_ids=[S_SENGUPTA_2020])

    P("lothal", "Lothal", ind, -2600, -1900, "intermediate",
      summary="A small Gujarat settlement with a large baked-brick basin that has been "
              "argued over for sixty years: dockyard, or reservoir?",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Dates follow the mature Harappan bracket. The disputed structure is the "
                "basin, not the chronology. Still open: the 2024 paper arguing for the "
                "dockyard says in its own abstract that the function remains unresolved.",
      alternatives=[
          {"label": "The basin is a reservoir, not a dock", "standing": "minority",
           "note": "Leshnik argued in 1968 that it held drinking or irrigation water and "
                   "that ship draught requirements were never met. Possehl noted the absence "
                   "of a hinterland and of shipbuilding remains.",
           "source_ids": [S_LESHNIK_1968]},
      ],
      as_of=CHECKED,
      source_ids=[S_LESHNIK_1968, S_GUPTA_2024])

    P("rakhigarhi", "Rakhigarhi", ind, -2616, -2000, "intermediate",
      summary="The largest Harappan site by area, and the source of the only ancient "
              "genome yet recovered from within the civilisation.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="AMS dates on charcoal at 20.6 m and 9.1 m depth give 2616+/-73 and "
                "2273+/-38 cal BCE. The cemetery is dated 2500-2000 BCE.",
      source_ids=[S_RAKHIGARHI_AMS, S_SHINDE_2019])

    # --------------------------------------------------------------- genomes

    EVENT("rakhigarhi-genome", "The Rakhigarhi Genome", ind, -2800, -2300, "foundational",
          summary="A single woman's DNA, recovered after 61 attempts, showed the Harappans "
                  "carried no steppe ancestry and no Anatolian farmer ancestry.",
          start_dating_method=C14, end_dating_method=C14, standing="majority",
          date_precision="century",
          date_note="Dated by association, not directly. Five attempts to radiocarbon-date "
                    "the individual's own remains failed on carbon-to-nitrogen ratio, so the "
                    "only anchor is seven charcoal dates from the habitation area, 2800-2300 "
                    "BCE. There is no calibrated date for the woman herself. The authors "
                    "caution that one genome cannot characterise a cosmopolitan civilisation, "
                    "and that a fitting model need not be the true source population.",
          caveats=[
              {"kind": "misconception",
               "text": "Widely reported as disproving Indo-Aryan migration. It does not. It "
                       "shows no steppe ancestry in one mature-period individual, which the "
                       "companion paper agrees with.",
               "source_ids": [S_SHINDE_2019, S_NARASIMHAN_2019]},
          ],
          source_ids=[S_SHINDE_2019, S_RAKHIGARHI_AMS])

    P("steppe-ancestry", "Arrival of Steppe Ancestry in South Asia", sa, -1900, -1500,
      "intermediate",
      summary="The window in which steppe pastoralist ancestry entered South Asia, after "
              "the Harappan cities had already emptied.",
      start_dating_method="unknown", end_dating_method="unknown", standing="majority",
      date_precision="disputed",
      date_note="Not an excavated date but a genetic admixture estimate: in Swat individuals "
                "the relevant mixture dates to a 95% interval of roughly 1900-1500 BCE, "
                "26 generations before they lived. Steppe ancestry is undetectable in South "
                "Asia before 2000 BCE. This dates a population mixture, not a language or "
                "an invasion; the authors state the path by which the ancestry arrived is "
                "uncertain, and some archaeologists see too few material-culture links "
                "between the Central Steppe and South Asia to accept a connection at all.",
      source_ids=[S_NARASIMHAN_2019])

    # --------------------------------------------------------------- decline

    P("deurbanisation", "Harappan Deurbanisation", ind, -2200, -1900, "intermediate",
      summary="The cities are abandoned over roughly three centuries as the monsoon "
              "weakens and inundation agriculture stops paying.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="An Arabian Sea isotope record shows rainfall and Indus discharge dropping "
                "abruptly at 4.2 ka, with the sharpest change at 4.1 ka. A 2023 study "
                "resolves this into a 230-year run of drought pulses centred at 4.19, 4.11 "
                "and 4.02 ka.",
      alternatives=[
          {"label": "Gradual decline from about 2500 BCE", "standing": "minority",
           "start_year": -2500, "end_year": -1300, "dating_method": C14,
           "note": "Giosan and colleagues argue the monsoon weakened progressively rather "
                   "than failing at one moment, and that a separate winter-monsoon decline "
                   "around 1300-1000 BCE affected the late phase as well.",
           "source_ids": [S_GIOSAN_2018]},
      ],
      source_ids=[S_STAUBWASSER_CP, S_DROUGHT_2023, S_GIOSAN_2018])

    P("ghaggar-hakra", "The Ghaggar-Hakra Question", ind, -3000, -1400, "specialist",
      summary="Whether a great river dried and took the cities with it. The geology says "
              "the big glacier-fed river was already gone long before the cities existed.",
      aliases=["Sarasvati question"],
      start_dating_method="unknown", end_dating_method="unknown", standing="minority",
      date_precision="disputed",
      date_note="Isotope work on Rann of Kachchh cores puts the last Himalayan glacier-fed "
                "river reaching the sea at roughly 10,000 years ago, which is several "
                "millennia before the Harappan period. Proposed desiccation dates for the "
                "later monsoon-fed channel range from the mid-4th millennium BCE to 1400 "
                "BCE. The timing is unresolved and consequential: a pre-Harappan drying "
                "cannot have caused a collapse that had not happened yet.",
      caveats=[
          {"kind": "misconception",
           "text": "The river did not vanish overnight. The described process is a "
                   "centuries-long shrinkage from a perennial glacier-fed river to an "
                   "intermittent monsoon-fed one.",
           "source_ids": [S_DAVE_2017]},
      ],
      source_ids=[S_DAVE_2017])

    # ---------------------------------------------------------------- script

    P("script", "The Indus Script", ind, -2800, -1900, "foundational",
      summary="Undeciphered, and still argued over at a more basic level: whether the "
              "signs encode language at all.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Earliest writing is attested in the Kot Dijian phase at Harappa, "
                "2800-2600 BCE, with potter's marks earlier still. The developed script "
                "runs through the mature period to about 1900 BCE. The writing question is "
                "still open after twenty years: the most recent work finds the corpus sits "
                "between the linguistic and non-linguistic baselines, matching neither.",
      alternatives=[
          {"label": "Not a writing system", "standing": "minority",
           "note": "Farmer, Sproat and Witzel argued in 2004 that inscriptions are too "
                   "short and that no scribal class or writing equipment has been found. "
                   "Rao replied that entropy resembles language.",
           "source_ids": [S_FARMER_2004, S_RAO_2009, S_SPROAT_2010]},
      ],
      as_of=CHECKED,
      source_ids=[S_HARAPPA_WRITING, S_FARMER_2004, S_RAO_2009, S_SPROAT_2010])

    # ----------------------------------------------------- southern neolithic

    ERA("southern-neolithic", "Southern Neolithic", sa, -2500, -1000, "intermediate",
        summary="A separate Neolithic in the South Deccan, built on cattle, native millets "
                "and enormous mounds of burnt dung.",
        start_dating_method=C14, end_dating_method=C14, standing="majority",
        date_precision="century",
        date_note="Three phases in the Allchin framework: 2500-2000, 2000-1600 and "
                  "1600-1000 BC. A second published scheme gives 2300-1800 and 1800-1200 "
                  "cal BC for the later two. Both are in use; they are not averaged here.",
        caveats=[{"kind": "misconception",
                  "text": "Not among the world's early Neolithic transitions, and not the "
                          "earliest in South Asia. It begins in the 3rd millennium BC, well "
                          "after the northwest.",
                  "source_ids": [S_BOIVIN_MPG]}],
        source_ids=[S_INFLIBNET_SN, S_FULLER_2001, S_BOIVIN_MPG])

    P("ashmounds", "The Ashmounds", f"{sa}.southern-neolithic", -1950, -1750, "intermediate",
      summary="Mounds of burnt cattle dung, some many metres high, built up by repeated "
              "firing of cattle pens over less than two centuries.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="AMS dates and stratigraphy at the Sanganakallu complex put ash formation "
                "between 1950 and 1750 BC, over perhaps less than 200 years. Village "
                "activity then continued on top of the mounds for another 500-700 years. "
                "That the deposits are burnt dung is chemically settled; why the dung was "
                "burned is not, with proposals from disease control in pens to ritual. Only "
                "some mounds are dated: Kudatini and Budihal are placed by settlement "
                "typology rather than radiocarbon, so no dates are stated for them.",
      source_ids=[S_INFLIBNET_SN, S_FULLER_2001])

    P("millets", "South Indian Millet Domestication", f"{sa}.southern-neolithic",
      -2500, -1000, "specialist",
      summary="Browntop and foxtail millet with mung bean and horsegram, argued to be "
              "domesticated in peninsular India rather than introduced.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="The staples are Brachiaria ramosa and Setaria, both native South Indian "
                "species, present with mung bean and horsegram from the earliest levels. "
                "African pearl millet and finger millet arrive later, as introductions.",
      caveats=[{"kind": "misconception",
                "text": "An early claim that sorghum straw appears in ashmound slag near "
                        "Kudatini is rejected by later systematic archaeobotany, which found "
                        "no sorghum at all.",
                "source_ids": [S_FULLER_2001]}],
      source_ids=[S_FULLER_2001, S_INFLIBNET_SN])

    # -------------------------------------------------------------- Kashmir

    P("burzahom", "Burzahom", f"{sa}.prehistory", -3000, -1000, "specialist",
      summary="A Kashmir valley site of pit dwellings cut into loess, with a Neolithic "
              "sequence running into a megalithic phase.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="Eight charcoal dates run at TIFR in 1965-66, MASCA-calibrated, give an "
                "aceramic phase about 3000-2850 BCE, early ceramic 2850-2550, late ceramic "
                "2550-1700, and a megalithic phase 1500-1000 BCE. The raw TF-series figures "
                "are uncalibrated and use a 5730-year half-life; mixing them with the "
                "MASCA-calibrated boundaries shifts the site by centuries.",
      allow_outside_parent_dates=True,
      source_ids=[S_RADIOCARBON_1965])
