"""Pre-Islamic Arabia: the Gulf, South Arabia, the Nabataeans, and the camel.

Research in `docs/anatolia-arabia-research.md`, gathered alongside the Anatolian
material authored in 0.15.0.0 and deliberately held back to this pass.

`west-asia.arabia.pre-islamic` held 3000 BCE to 610 CE — three and a half
millennia — as a single entity with no children.

The Arabian half of that research is noticeably weaker than the Anatolian half,
and the authoring reflects it. Two entities researched in full are **not**
authored here:

- **Magan**, the copper source that supplied Mesopotamia, because every date
  found for it traces to Wikipedia.
- **Himyar**, because the research pass marked its dates as search-located and
  never confirmed by fetching the pages. The convergence around 110 BCE is
  probably right; "probably right" is not the standard.

What IS authored includes two items worth more than their subject matter.

**The Marib Dam is a clean case of physical evidence contradicting a story
everyone knows.** The dam's collapse is remembered in Arabian and Quranic
tradition as the Sayl al-'Arim, conventionally 570 CE. AMS dating of detrital
charcoal in the basin sediments puts the dam's final period of activity between
roughly 1 CE and the end of the third century — some three hundred years
earlier. The dataset carries both and resolves neither.

**Camel domestication carries a documented correction.** Timna Site 30's camel
bones were long cited as evidence of domestication by the 13th century BCE. The
bones turned out to belong to the site's last occupation phase, not its Late
Bronze Age layers. A direct measurement on one of them, OxA-2165 at 2650 +/- 90
BP, calibrates to 969-600 BCE. This is the same failure class the dataset keeps
finding: not a bad measurement, but a good measurement attached to the wrong
layer.

South Arabian dates are all authored under the **Long Chronology** and say so.
The Short Chronology would move these kingdoms several centuries later, and it
is losing ground rather than dead. Reporting a Sabaean date without naming the
scheme would repeat the Hammurabi mistake fixed in 0.15.0.0.
"""

from builders import make_builders

S_HUMANUM_DILMUN = "ancient-arabia-dictionary-dilmun"
S_BAHRAIN_TIMELINE = "bahrain-authority-history-timeline"
S_DURHAM_THESIS = "durham-thesis-umm-an-nar-wadi-suq"
S_BREWMINATE_SA = "south-arabian-kingdoms-overview"
S_FRANCAVIGLIA = "francaviglia-dating-marib-dam"
S_CAMELS_LEVANT = "introduction-domestic-camels-southern-levant"
S_CAFOSCARI_NAB = "ca-foscari-nabataean-studies"
S_NAVEH_HAIFA = "naveh-nabataean-inscriptions-haifa"
S_JORDAN_DOA = "jordan-antiquities-nabataeans-oriental-trade"
S_ORIENT_INCENSE = "orient-frankincense-and-myrrh"

ARABIA_SOURCES = [
    {"id": S_HUMANUM_DILMUN, "kind": "scholarly",
     "citation": "Ancient Arabia Dictionary (Huma-Num), 'Baḥrayn / Dilmun / Tylos'",
     "url": "https://ancientarabia.huma-num.fr/dictionary/definition/bahrayn-al",
     "note": "States that recent research has moved beyond the older Ancient/Middle/Late "
             "Dilmun scheme in favour of a more granular phasing."},
    {"id": S_BAHRAIN_TIMELINE, "kind": "reference",
     "citation": "Bahrain Authority for Culture and Antiquities, Bahrain History Timeline",
     "url": "https://culture.gov.bh/en/eservices/BahrainHistoryTimeline/"},
    {"id": S_DURHAM_THESIS, "kind": "scholarly",
     "citation": "Durham University doctoral thesis on southeastern Arabian Bronze Age periodisation",
     "url": "http://etheses.dur.ac.uk/11730/1/eThesis.pdf",
     "note": "Gives Umm an-Nar as both 2700-2000 and 2800-2000 BC in different passages of "
             "the same work, which is a fair measure of how firm the start date is."},
    {"id": S_BREWMINATE_SA, "kind": "reference",
     "citation": "Survey history of the South Arabian kingdoms of ancient Yemen",
     "url": "https://brewminate.com/a-history-of-the-south-arabian-kingdoms-of-ancient-yemen/",
     "note": "Adopts the Long Chronology explicitly for its own date reporting, and names the "
             "scholars on each side of the dispute."},
    {"id": S_FRANCAVIGLIA, "kind": "scholarly",
     "citation": "Francaviglia, 'Dating the Ancient Dam of Ma'rib (Yemen)', Journal of Archaeological Science",
     "url": "https://www.academia.edu/57427411/Dating_the_Ancient_Dam_of_Marib_Yemen_",
     "note": "AMS on detrital charcoal in the basin silts puts final dam activity no earlier "
             "than about 1 CE and no later than the end of the 3rd century."},
    {"id": S_CAMELS_LEVANT, "kind": "scholarly",
     "citation": "'The Introduction of Domestic Camels to the Southern Levant'",
     "url": "https://static1.squarespace.com/static/54694fa6e4b0eaec4530f99d/t/65493ec2a05a17007b8c2074/1699299011442/The_Introduction_of_Domestic_Camels_to_t.pdf",
     "note": "OxA-2165, 2650 +/- 90 BP, calibrating to 969-600 BCE at 1 sigma. Shows the "
             "Timna Site 30 camel bones belong to the last occupation phase, not the Late "
             "Bronze Age layers they were long assigned to."},
    {"id": S_CAFOSCARI_NAB, "kind": "scholarly",
     "citation": "Edizioni Ca' Foscari, volume on Nabataean history and epigraphy",
     "url": "https://edizionicafoscari.unive.it/media/pdf/books/978-88-6969-508-7/978-88-6969-508-7_jFP74xP.pdf"},
    {"id": S_NAVEH_HAIFA, "kind": "scholarly",
     "citation": "Naveh, on Nabataean inscriptions (Hecht Museum, University of Haifa)",
     "url": "https://mushecht2.haifa.ac.il/images/catalogues/archeology/Nabateans/Joseph_Naveh.pdf"},
    {"id": S_JORDAN_DOA, "kind": "scholarly",
     "citation": "Jordan Department of Antiquities, 'Nabataeans and Oriental Trade', Studies in the History and Archaeology of Jordan 10",
     "url": "https://publication.doa.gov.jo/uploads/publications/25/SHAJ_10-405-412.pdf"},
    {"id": S_ORIENT_INCENSE, "kind": "scholarly",
     "citation": "'Frankincense and Myrrh', Orient (Society for Near Eastern Studies in Japan)",
     "url": "https://www.jstage.jst.go.jp/article/orient1960/3/0/3_0_21/_pdf/-char/en"},
]

CHECKED = "2026-08-08"
C14 = "radiocarbon-calibrated"
TYPO = "typological"
CAL = "calendar"


def extend(E, entities):
    _, P, ERA, EVENT, _, _ = make_builders(E)
    ar = "west-asia.arabia.pre-islamic"

    # ------------------------------------------------------------- the Gulf

    ERA("dilmun", "Dilmun", ar, -3300, -510, "foundational",
        summary="The Gulf trading power that stood between Mesopotamia and the Indus, and "
                "which Mesopotamian literature remembered as a kind of paradise.",
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_precision="century",
        date_note="Dated from Mesopotamian texts rather than excavation. First mentioned "
                  "about 3300 BCE; a tribal phase 2250-2050 BCE, then state formation on "
                  "Bahrain from 2050; Kassite control in the 15th and 14th centuries; late "
                  "cemeteries cautiously placed 950-700 BCE. Sargon II names King Uperi about "
                  "709 BCE, and the last mention is in a legal contract of about 510 BCE.",
        caveats=[{"kind": "misconception",
                  "text": "The old three-part Early, Middle and Late Dilmun scheme has been "
                          "superseded by the more granular phasing above. The year of that "
                          "revision is not stated in the source.",
                  "source_ids": [S_HUMANUM_DILMUN]}],
        # First textual mention predates the era node's round 3000 BCE start.
        allow_outside_parent_dates=True,
        source_ids=[S_HUMANUM_DILMUN, S_BAHRAIN_TIMELINE])

    P("umm-an-nar", "Umm an-Nar Culture", ar, -2700, -2000, "intermediate",
      summary="The Oman peninsula's Bronze Age of circular stone tower tombs, copper export, "
              "and carnelian carried in from the Indus.",
      start_dating_method=TYPO, end_dating_method=TYPO, standing="majority",
      date_precision="century",
      date_note="Dated by tomb architecture and pottery, not radiocarbon. The start is soft: "
                "the same doctoral thesis gives 2700 BCE in one passage and 2800 in another, "
                "and other academic sources go as late as 2600.",
      source_ids=[S_DURHAM_THESIS])

    P("wadi-suq", "Wadi Suq Period", ar, -2000, -1600, "specialist",
      summary="The southeastern Arabian second millennium, when the tower-tomb tradition "
              "breaks and burial practice changes shape.",
      start_dating_method=TYPO, end_dating_method=TYPO, standing="majority",
      date_precision="century",
      date_note="The 2000-1600 BC bracket was agreed in 1980 and remains the most cited. A "
                "later Bronze Age phase runs about 1600-1250 BC after it.",
      alternatives=[
          {"label": "Split into Classic and Late Wadi Suq", "standing": "minority",
           "start_year": -2000, "end_year": -1300, "dating_method": TYPO,
           "note": "Carter's alternative divides it at 1500 BCE and runs the later phase to "
                   "1300, which removes the need for a separate Late Bronze Age phase.",
           "source_ids": [S_DURHAM_THESIS]},
      ],
      as_of=CHECKED,
      source_ids=[S_DURHAM_THESIS])

    # -------------------------------------------------------- South Arabia

    ERA("saba", "Saba", ar, -800, 275, "foundational",
        summary="The incense kingdom of the Yemeni highlands, the Sheba of later legend, "
                "and the builder of the Marib Dam.",
        aliases=["Sheba"],
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_precision="disputed",
        date_note="These are LONG CHRONOLOGY dates and the choice matters. The Short "
                  "Chronology, proposed by Pirenne in 1955 from art-historical and "
                  "palaeographic comparison with Greece, would start South Arabian "
                  "civilisation in the 5th century BCE instead — several centuries later. The "
                  "one point all schemes agree on is Aelius Gallus's Roman campaign of 25 "
                  "BCE. Contemporary kingdoms under the same scheme: Hadramawt and Ma'in from "
                  "the 8th century, Awsan 800-500, Qataban from the 4th.",
        alternatives=[
            {"label": "Short Chronology: from the 5th century BCE", "standing": "minority",
             "start_year": -500, "end_year": 275, "dating_method": CAL,
             "note": "Pirenne's 1955 scheme, from Greek stylistic and letter-form comparison. "
                     "Not disproven, but losing ground.",
             "source_ids": [S_BREWMINATE_SA]},
        ],
        caveats=[{"kind": "misconception",
                  "text": "South Arabian dates are almost never labelled with their scheme. "
                          "Two sources centuries apart are usually not in conflict; they have "
                          "chosen differently.",
                  "source_ids": [S_BREWMINATE_SA]}],
        as_of=CHECKED,
        source_ids=[S_BREWMINATE_SA])

    P("marib-dam", "The Marib Dam", f"{ar}.saba", -700, 300, "intermediate",
      summary="Sabaean hydraulic engineering on a scale that watered a desert kingdom, and "
              "whose failure became a parable.",
      start_dating_method=CAL, end_dating_method=C14, standing="majority",
      date_precision="disputed",
      date_note="Construction is attributed by inscription to around 700 BCE, in the era of "
                "Karib'il Watar; no scientific date confirms a construction year. The end "
                "date here is radiocarbon: AMS on detrital charcoal in the basin silts puts "
                "the dam's final period of activity no earlier than about 1 CE and no later "
                "than the end of the 3rd century.",
      caveats=[{"kind": "misconception",
                "text": "The famous collapse, the Sayl al-'Arim of about 570 CE, is remembered "
                        "in later tradition. The sediment dating puts the dam's last activity "
                        "roughly three centuries earlier.",
                "source_ids": [S_FRANCAVIGLIA]}],
      # The dam's measured last activity runs past Saba's conventional end date.
      allow_outside_parent_dates=True,
      source_ids=[S_FRANCAVIGLIA, S_BREWMINATE_SA])

    # ---------------------------------------------------------- Nabataeans

    ERA("nabataeans", "The Nabataeans", ar, -312, 106, "foundational",
        summary="Caravan traders who took the northern end of the incense route, cut Petra "
                "out of sandstone, and were annexed by Rome without a fight.",
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_note="The first fixed reference is 312 BCE, when Diodorus records Antigonus's "
                  "general attacking the Nabataean Arabs at a strong but unwalled rock, "
                  "conventionally identified as Petra. The earliest Nabataean inscription "
                  "naming a king, Aretas, is dated on palaeographic grounds to the first half "
                  "of the 2nd century BCE and usually to 168 BCE. Rome annexed the kingdom in "
                  "106 CE.",
        caveats=[{"kind": "naming-confusion",
                  "text": "Assyrian references to Nabatu and biblical Nabaioth are often taken "
                          "for early Nabataeans. Most scholars now hold that none of them can "
                          "be identified with the Nabataeans of Petra.",
                  "source_ids": [S_CAFOSCARI_NAB, S_NAVEH_HAIFA]}],
        source_ids=[S_CAFOSCARI_NAB, S_NAVEH_HAIFA])

    # ------------------------------------------------- camels and incense

    P("camel-domestication", "Domestication of the Dromedary", ar, -1200, -900, "intermediate",
      summary="The pack animal that made the incense route possible, domesticated far later "
              "than the trade routes it is usually credited with opening.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="Most scholars place exploitation as a pack animal no earlier than the 12th "
                "century BCE, with domestic dromedaries in southeast Arabia in the first "
                "third of the 1st millennium. In the Levant the first significant appearance "
                "is no earlier than the last third of the 10th century BCE. Wild camels are "
                "much older: bones at Baynunah in the 5th millennium and at Ra's al-Hadd at "
                "2890-2580 BCE, neither of them domesticated.",
      caveats=[
          {"kind": "misconception",
           "text": "Timna Site 30 was long cited for camels by the 13th century BCE. The bones "
                   "belong to the site's last phase, not its Late Bronze Age layers: OxA-2165 "
                   "calibrates to 969-600 BCE.",
           "source_ids": [S_CAMELS_LEVANT]},
          {"kind": "misconception",
           "text": "Old camel bones are not evidence of domestication. Wild dromedaries were "
                   "present in Arabia for millennia before anyone rode one.",
           "source_ids": [S_CAMELS_LEVANT]},
      ],
      source_ids=[S_CAMELS_LEVANT])

    P("incense-trade", "The Incense Route", ar, -700, 200, "intermediate",
      summary="Frankincense and myrrh moving north out of South Arabia, the trade that paid "
              "for Saba, Qataban and eventually Petra.",
      start_dating_method=CAL, end_dating_method=CAL, standing="majority",
      date_precision="disputed",
      date_note="Conventionally described as flourishing between the 3rd century BCE and the "
                "2nd century CE, but the route is argued to have been in use since at least "
                "the 7th century BCE and possibly the 8th. A radiocarbon date from Hajar bin "
                "Humeid of about 852 BCE with a +/-160 year error supports early South "
                "Arabian urban development, though the range is too wide to pin the trade to.",
      source_ids=[S_JORDAN_DOA, S_ORIENT_INCENSE, S_BREWMINATE_SA])
