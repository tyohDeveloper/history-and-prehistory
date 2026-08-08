"""West Asia: the Uruk period, Elam subdivided, and Anatolia given a history.

Research in `docs/mesopotamia-research.md` and `docs/anatolia-arabia-research.md`.

West Asia was the thinnest major region in the dataset relative to its
importance — 63 entities for the place where farming, cities and writing were
invented, against 114 for Europe — and the shape of the thinness was worse than
the count.

**`west-asia.anatolia` was an empty region node.** No Hittites, no Troy, no
Lydia, no Urartu, nothing at all. The childless-node report could not see it,
because that report only examined eras and periods. An empty REGION is the most
severe gap the dataset can have and it was invisible in the report built to find
gaps. `coverage.py` now lists empty regions first.

**The Uruk period was entirely absent.** The dataset went from Ubaid straight to
the Early Dynastic at 2900 BCE, skipping the first cities and the invention of
writing. The container era was already there and said so in its own summary —
"the LC1-LC5 sequence that ends with the first cities and the first writing" —
and held nothing.

Three things worth stating about how this was authored.

**Uruk's chronology is authored from ARCANE, not from the round numbers.** Four
frameworks are in circulation and they disagree: CDLI's 4000-3000 BC, ARCANE's
radiocarbon-based scheme, ISAC's LC-phase scheme, and Unicode's script-phase
scheme. They are not averaged. ARCANE also notes that the widely quoted early
figures for Uruk IVa rest on uncalibrated readings — the same failure class as
Monte Verde, in the literature rather than in this dataset.

**The size of Uruk is left at CDLI's 100 hectares.** Figures from 250 to 600 ha
circulate freely. Only CDLI's is traceable to an institution, and the population
estimates everyone quotes are not traceable to anything, so no population figure
is authored at all.

**The token hypothesis is not authored as the origin of writing.** It is the
most popular account and it is under sustained, specific, statistical attack —
Zimansky showed the "sheep" token has fifteen attestations in total. The
proto-cuneiform entity carries the accounting function, which the tablets
themselves support, and carries the token story as a contested alternative.

Deliberately NOT authored: Eridu (its founding date could not be traced to the
excavation report); the Hittite Middle Kingdom (the literature calls it an
ill-defined dark age and declines to bound it, so this does too); Urartu's
collapse date; and pre-Islamic Arabia, whose research is archived in
`docs/anatolia-arabia-research.md` and which is the obvious next pass.
"""

from builders import make_builders

S_CDLI_URUK = "cdli-uruk-warka"
S_CDLI_LATE_URUK = "cdli-late-uruk-period"
S_ARCANE = "sallaberger-schrakamp-2015-arcane"
S_ISAC_SUREZHA = "isac-surezha-lc-chronology"
S_UNICODE_PROTO = "unicode-2019-proto-cuneiform"
S_ANTIQUITY_SEALS = "antiquity-2025-seals-and-signs"
S_ZIMANSKY = "zimansky-1993-before-writing-review"
S_BENNISON_CHAPMAN = "bennison-chapman-2023-tokens"
S_READING_JN = "reading-jemdet-nasr"
S_ISAC_BABYLON = "isac-dating-fall-of-babylon"
S_CAMB_PROTOELAMITE = "cambridge-elements-proto-elamite"
S_DESSET_2022 = "desset-2022-linear-elamite"
S_DAHL_ORA = "dahl-schismogenesis-linear-elamite"
S_IRANICA_SUSA = "iranica-susa-elamite-period"
S_UNESCO_ZANBIL = "unesco-tchogha-zanbil"
S_POTTS_NEOELAM = "potts-2015-neo-elamite"
S_CULTURE_SUSA = "france-culture-susa-6000-years"
S_BRILL_HITTITE = "brill-hittite-civilisation"
S_CORNELL_DROUGHT = "cornell-2023-hittite-drought"
S_BRYCE_ASSYRIA = "bryce-absorption-by-assyria"
S_NOVAK_MITANNI = "novak-2007-mittani-chronology"
S_MET_URARTU = "met-urartu"
S_PENN_GORDION = "penn-digital-gordion-midas"
S_MET_MIDAS = "met-phrygia-gordion-midas"
S_BM_MONEY = "british-museum-money-gallery"
S_OEAW_LYDIAN = "oeaw-early-lydian-coinage"
S_PEARSON_2020 = "pearson-2020-gordion-dendro"
S_PEARSON_REPLY = "pearson-reply-gordion-745bc"
S_OXFORD_ANATOLIA = "oxford-anatolian-chronology"
S_BRITANNICA_TROY = "britannica-troy"

WEST_ASIA_SOURCES = [
    {"id": S_CDLI_URUK, "kind": "scholarly",
     "citation": "Cuneiform Digital Library Initiative, 'Uruk (modern Warka)'",
     "url": "https://cdli.ox.ac.uk/wiki/doku.php?id=uruk_mod._warka",
     "note": "States plainly that it does NOT assign absolute calendar dates to the "
             "individual Eanna levels, only their stratigraphic order."},
    {"id": S_CDLI_LATE_URUK, "kind": "scholarly",
     "citation": "Cuneiform Digital Library Initiative, 'The Late Uruk Period'",
     "url": "https://cdli.ox.ac.uk/wiki/doku.php?id=the_late_uruk_period"},
    {"id": S_ARCANE, "kind": "scholarly",
     "citation": "Sallaberger & Schrakamp, ARCANE Vol. 1: Associated Regional Chronologies for the Ancient Near East (2015)",
     "url": "https://www.assyriologie.uni-muenchen.de/personen/professoren/sallaberger/publ_sallaberger/wasa_schrakamp_2015_arcane1.pdf",
     "note": "Uruk IVa Temple C samples cluster at cal. 3510-3370 BC. Notes that older "
             "quoted figures for Uruk IVa rest on uncalibrated or incorrect readings."},
    {"id": S_ISAC_SUREZHA, "kind": "scholarly",
     "citation": "Institute for the Study of Ancient Cultures (Chicago), Surezha excavation report",
     "url": "https://isac.uchicago.edu/sites/default/files/uploads/shared/docs/ar/11-20/13-14/ar2013-14_Surezha.pdf"},
    {"id": S_UNICODE_PROTO, "kind": "reference",
     "citation": "Unicode Technical Report on Proto-Cuneiform (2019)",
     "url": "https://www.unicode.org/L2/L2019/19284-proto-cuneiform.pdf"},
    {"id": S_ANTIQUITY_SEALS, "kind": "scholarly",
     "citation": "'Seals and signs: tracing the origins of writing in ancient South-west Asia', Antiquity (2025)",
     "url": "https://www.cambridge.org/core/journals/antiquity/article/seals-and-signs-tracing-the-origins-of-writing-in-ancient-southwest-asia/B3C2D400F3F80A7A0162D9035C9C2804"},
    {"id": S_ZIMANSKY, "kind": "scholarly",
     "citation": "Zimansky, review of Schmandt-Besserat's 'Before Writing', Journal of Field Archaeology (1993)",
     "url": "https://kieranhealy.org/files/misc/jfa93.pdf",
     "note": "Only 18% of claimed token subtypes have more than four members, and the "
             "'sheep' token has fifteen attestations across all periods."},
    {"id": S_BENNISON_CHAPMAN, "kind": "scholarly",
     "citation": "Bennison-Chapman, Bulletin of the American Society of Overseas Research 390 (2023)",
     "url": "https://www.journals.uchicago.edu/doi/10.1086/727776",
     "note": "Calls the 'writing replaced tokens' narrative a gross oversimplification; "
             "tokens continue alongside writing into the 1st millennium BC."},
    {"id": S_READING_JN, "kind": "reference",
     "citation": "University of Reading, Jemdet Nasr period",
     "url": "https://www.reading.ac.uk/ure/subject/mesopotamia.php"},
    {"id": S_ISAC_BABYLON, "kind": "scholarly",
     "citation": "Institute for the Study of Ancient Cultures (Chicago), 'Dating the Fall of Babylon'",
     "url": "https://isac.uchicago.edu/dating-fall-babylon",
     "note": "The Venus Tablet of Ammi-saduqa is astronomically periodic, so it fits several "
             "real years. That is where the High/Middle/Low/Ultra-Low split comes from."},
    {"id": S_CAMB_PROTOELAMITE, "kind": "scholarly",
     "citation": "Cambridge Elements, 'Proto-Elamite'",
     "url": "https://www.cambridge.org/core/elements/protoelamite/3684B7262E21A8B6AF8657D948A5B1A6",
     "note": "Precision is limited by a plateau in the calibration curve — a physical limit, "
             "not a shortage of samples."},
    {"id": S_DESSET_2022, "kind": "scholarly",
     "citation": "Desset, Tabibzadeh, Kervran, Basello & Marchesi, 'The Decipherment of Linear Elamite Writing', Zeitschrift für Assyriologie 112 (2022)",
     "url": "https://orbi.uliege.be/handle/2268/334018?wpmobileexternal=true"},
    {"id": S_DAHL_ORA, "kind": "scholarly",
     "citation": "Dahl, on Linear Elamite and schismogenesis (Oxford ORA)",
     "url": "https://ora.ox.ac.uk/objects/uuid:51adb1c2-61de-438c-9b29-125addf3d2a1/files/r6w924c626",
     "note": "Argues the Proto-Elamite resemblance is deliberate archaising by later scribes, "
             "not descent."},
    {"id": S_IRANICA_SUSA, "kind": "scholarly",
     "citation": "Encyclopaedia Iranica, 'Susa ii. History during the Elamite period'",
     "url": "https://www.iranicaonline.org/articles/susa-ii-history-during-the-elamite-period/",
     "note": "Follows the short chronology of Gasche et al. (1998). Notes Elamite history is "
             "'to some extent a prisoner of the Assyrian royal inscriptions'."},
    {"id": S_UNESCO_ZANBIL, "kind": "reference",
     "citation": "UNESCO World Heritage Centre, 'Tchogha Zanbil'",
     "url": "https://whc.unesco.org/en/list/113/"},
    {"id": S_POTTS_NEOELAM, "kind": "scholarly",
     "citation": "Potts, 'The Neo-Elamite period', in The Archaeology of Elam (Cambridge, 2015)",
     "url": "https://www.cambridge.org/core/books/abs/archaeology-of-elam/neoelamite-period/054799B680BFE4F9897D0F521CAA46E8"},
    {"id": S_CULTURE_SUSA, "kind": "reference",
     "citation": "French Ministry of Culture, 'Susa: 6,000 years of history'",
     "url": "https://archeologie.culture.gouv.fr/jacques-morgan/en/susa-6000-years-history"},
    {"id": S_BRILL_HITTITE, "kind": "scholarly",
     "citation": "Brill, chapter on Hittite civilisation",
     "url": "https://brill.com/display/book/9789004548633/BP000005.xml",
     "note": "Reports that current German Archaeological Institute evidence does NOT support "
             "violent destruction at Hattusa; buildings were deliberately emptied."},
    {"id": S_CORNELL_DROUGHT, "kind": "press",
     "citation": "Cornell Chronicle, 'Rare drought coincided with Hittite empire collapse' (February 2023)",
     "url": "https://news.cornell.edu/stories/2023/02/rare-drought-coincided-hittite-empire-collapse",
     "note": "Tree-ring width plus stable carbon isotopes in Gordion juniper give a severe "
             "drought at 1198-1196 BCE."},
    {"id": S_BRYCE_ASSYRIA, "kind": "scholarly",
     "citation": "Bryce, 'Absorption by Assyria (8th century)', Oxford Academic",
     "url": "https://academic.oup.com/book/9649/chapter/156739759"},
    {"id": S_NOVAK_MITANNI, "kind": "scholarly",
     "citation": "Novák, 'Mittani Empire and the Question of Absolute Chronology' (Heidelberg, 2007)",
     "url": "https://archiv.ub.uni-heidelberg.de/propylaeumdok/1295/1/Novak_Mittani_Empire_2007.pdf"},
    {"id": S_MET_URARTU, "kind": "reference",
     "citation": "Metropolitan Museum of Art, 'Urartu'",
     "url": "https://www.metmuseum.org/essays/urartu"},
    {"id": S_PENN_GORDION, "kind": "scholarly",
     "citation": "Penn Museum, Digital Gordion",
     "url": "https://www.penn.museum/sites/gordion/articles/myth-religion/320-2/"},
    {"id": S_MET_MIDAS, "kind": "reference",
     "citation": "Metropolitan Museum of Art, 'Phrygia, Gordion, and King Midas in the Late Eighth Century B.C.'",
     "url": "https://www.metmuseum.org/essays/phrygia-gordion-and-king-midas-in-the-late-eighth-century-b-c"},
    {"id": S_BM_MONEY, "kind": "reference",
     "citation": "British Museum, Money Gallery (Room 68) gallery guide",
     "url": "https://www.britishmuseum.org/sites/default/files/2021-05/Money_Gallery_LPG_2020_Room_68.pdf"},
    {"id": S_OEAW_LYDIAN, "kind": "scholarly",
     "citation": "Austrian Academy of Sciences, 'Early Lydian Coinage and Chronology'",
     "url": "https://www.oeaw.ac.at/en/oeai/research/classical-studies/numismatics/early-lydian-coinage-and-chronology"},
    {"id": S_PEARSON_2020, "kind": "scholarly",
     "citation": "Pearson et al., 'Annual radiocarbon record indicates 16th century BCE date for the Thera eruption' and the Gordion sequence, PNAS 117 (2020)",
     "url": "https://www.pnas.org/doi/10.1073/pnas.1917445117"},
    {"id": S_PEARSON_REPLY, "kind": "scholarly",
     "citation": "Pearson et al., 'Reply to Manning: Dating of the Gordion tree-ring sequence still stands within a year of 745 BC', PNAS",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7414178/"},
    {"id": S_OXFORD_ANATOLIA, "kind": "scholarly",
     "citation": "Oxford Handbook of Ancient Anatolia, chronology chapter",
     "url": "https://academic.oup.com/edited-volume/36332/chapter/318715466?searchresult=1"},
    {"id": S_BRITANNICA_TROY, "kind": "reference",
     "citation": "Encyclopaedia Britannica, 'Troy (ancient city, Turkey)'",
     "url": "https://www.britannica.com/place/Troy-ancient-city-Turkey"},
]

CHECKED = "2026-08-08"
C14 = "radiocarbon-calibrated"
TYPO = "typological"
CAL = "calendar"


def extend(E, entities):
    _, P, ERA, EVENT, _, _ = make_builders(E)
    lc = "west-asia.prehistory.late-chalcolithic-mesopotamia"
    elam = "west-asia.iran.elam"
    ana = "west-asia.anatolia"

    # ============================================================ URUK

    ERA("uruk-period", "Uruk Period", lc, -4000, -3100, "foundational",
        summary="The centuries in which southern Mesopotamia produced the first cities, the "
                "first bureaucracy, and the first writing.",
        start_dating_method=C14, end_dating_method=C14, standing="majority",
        date_precision="century",
        date_note="Four frameworks are in circulation and disagree: CDLI gives 4000-3000 BC "
                  "on stratigraphy; ARCANE gives Early and Middle Uruk 4200-3800 and Late "
                  "Uruk 3800-3000 on calibrated radiocarbon; ISAC's LC scheme gives Middle "
                  "Uruk 3700-3400 and Late Uruk 3400-3100; Unicode's script phases run "
                  "3500-3000. They are not averaged here.",
        caveats=[{"kind": "misconception",
                  "text": "Older literature dates Uruk IVa as late as 2815 BC. ARCANE notes "
                          "those figures rest on uncalibrated or incorrect readings; the "
                          "calibrated cluster is around 3450 BC.",
                  "source_ids": [S_ARCANE]}],
        source_ids=[S_CDLI_URUK, S_ARCANE, S_ISAC_SUREZHA, S_UNICODE_PROTO])

    P("uruk-city", "Uruk", f"{lc}.uruk-period", -4000, -3100, "foundational",
      summary="The first city: about 100 hectares by the end of the period, holding more "
              "than half the settled area of southern Mesopotamia around it.",
      aliases=["Warka", "Unug"],
      start_dating_method=TYPO, end_dating_method=TYPO, standing="majority",
      date_precision="century",
      date_note="Sizes are from archaeological survey, not radiocarbon. Uruk grows from "
                "under 10 ha before the period to about 70 ha at its start and about 100 ha "
                "at its end, reaching roughly 400 ha in the Early Dynastic period.",
      caveats=[{"kind": "misconception",
                "text": "Figures of 250 to 600 hectares and populations of 40,000 circulate "
                        "widely. Only the CDLI survey figures trace to an institution, and no "
                        "population estimate traces to anything.",
                "source_ids": [S_CDLI_URUK]}],
      source_ids=[S_CDLI_URUK])

    P("uruk-expansion", "The Uruk Expansion", f"{lc}.uruk-period", -3700, -3100, "intermediate",
      summary="Uruk material culture appears across Syria and into Anatolia, and scholars "
              "have argued for forty years about what that means.",
      start_dating_method=TYPO, end_dating_method=TYPO, standing="majority",
      date_precision="century",
      date_note="Dated by the appearance and disappearance of southern Mesopotamian material "
                "at northern sites, not independently. Four readings are current: "
                "colonisation, peaceful trade, displaced migration, and rejection of the "
                "whole model in favour of independent northern development.",
      alternatives=[
          {"label": "Not an expansion: independent northern development", "standing": "minority",
           "note": "Holds that northern complexity arose on its own and the shared material "
                   "reflects contact rather than any southern system.",
           "source_ids": [S_CDLI_LATE_URUK]},
      ],
      as_of=CHECKED,
      source_ids=[S_CDLI_LATE_URUK, S_ARCANE])

    P("proto-cuneiform", "Proto-Cuneiform", f"{lc}.uruk-period", -3350, -3000, "foundational",
      summary="The earliest known writing: numerals and word-signs pressed into clay at "
              "Uruk, used almost entirely for accounting.",
      start_dating_method=TYPO, end_dating_method=TYPO, standing="majority",
      date_precision="century",
      date_note="Dated to Uruk IV and III script phases, c. 3350-3000 BC. The basis is "
                "stratigraphic inference plus palaeography, not excavation context: nearly "
                "5,000 archaic tablets came out of rubbish and fill deposits beneath Level "
                "III construction, so they must predate it, and no tablets occur below Level "
                "IV. Sign-form evolution does the rest of the work. Writing outlasts the "
                "Uruk period proper, continuing into Jemdet Nasr.",
      allow_outside_parent_dates=True,
      alternatives=[
          {"label": "Descended from clay accounting tokens", "standing": "minority",
           "note": "Schmandt-Besserat's model: tokens, then sealed clay envelopes, then "
                   "numerical tablets, then writing. Popular, and under sustained statistical "
                   "attack.",
           "source_ids": [S_ZIMANSKY, S_BENNISON_CHAPMAN]},
      ],
      caveats=[
          {"kind": "misconception",
           "text": "The earliest tablets were not found in use-contexts. They came from "
                   "rubbish and fill, so their date is inferred from the layers above them "
                   "and from sign shapes.",
           "source_ids": [S_CDLI_LATE_URUK]},
          {"kind": "misconception",
           "text": "Tokens were not replaced by writing. They continue in use alongside "
                   "tablets, seals and tags into the 1st millennium BC.",
           "source_ids": [S_BENNISON_CHAPMAN]},
      ],
      as_of=CHECKED,
      source_ids=[S_ANTIQUITY_SEALS, S_CDLI_LATE_URUK, S_CDLI_URUK, S_UNICODE_PROTO,
                  S_ZIMANSKY, S_BENNISON_CHAPMAN])

    P("jemdet-nasr", "Jemdet Nasr Period", lc, -3200, -2900, "intermediate",
      summary="The short period between Uruk and the Early Dynastic, in which writing "
              "spreads beyond Uruk and becomes recognisably cuneiform.",
      start_dating_method=TYPO, end_dating_method=TYPO, standing="majority",
      date_precision="century",
      allow_outside_parent_dates=True,
      source_ids=[S_READING_JN, S_UNICODE_PROTO])

    # ============================================================ ELAM

    P("proto-elamite", "Proto-Elamite", elam, -3300, -2900, "intermediate",
      summary="Southwestern Iran's own writing system, invented within a century or two of "
              "Mesopotamia's and still undeciphered.",
      aliases=["Susa III"],
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="Roughly 3300-2900 BCE. Precision beyond that is not currently achievable: "
                "the relevant radiocarbon dates fall on a plateau in the calibration curve, "
                "which is a physical limit rather than a shortage of samples. The tablet "
                "sub-phases are relative only. It begins slightly before the Elam era node, "
                "which starts at the conventional 3200 BCE.",
      allow_outside_parent_dates=True,
      source_ids=[S_CAMB_PROTOELAMITE])

    P("linear-elamite", "Linear Elamite", elam, -2300, -1880, "intermediate",
      summary="A later Iranian script, claimed in 2022 to have been deciphered as the "
              "oldest purely phonographic writing known.",
      start_dating_method=TYPO, end_dating_method=TYPO, standing="majority",
      date_precision="century",
      date_note="Dated by the royal names appearing in the texts. The core corpus is often "
                "given as 2100-1900 BC; the 2022 decipherment paper uses 2300-1880 BCE.",
      alternatives=[
          {"label": "Not descended from Proto-Elamite", "standing": "minority",
           "note": "Dahl argues later scribes deliberately built an archaising script from "
                   "recovered Proto-Elamite tablets, as differentiation from Mesopotamia, "
                   "rather than inheriting one.",
           "source_ids": [S_DAHL_ORA]},
      ],
      caveats=[{"kind": "misconception",
                "text": "Widely reported as deciphered. Acceptance is qualified rather than "
                        "universal, and no fetched source reports a consensus statement.",
                "source_ids": [S_DESSET_2022, S_DAHL_ORA]}],
      as_of=CHECKED,
      source_ids=[S_DESSET_2022, S_DAHL_ORA])

    ERA("old-elamite", "Old Elamite Period", elam, -2400, -1450, "intermediate",
        summary="Elam's first documented dynasties — Awan, Simaški, Sukkalmah — locked in "
                "alternating war and marriage with Akkad, Ur and Babylon.",
        aliases=["Paleo-Elamite"],
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_precision="disputed",
        date_note="Two incompatible schemes are in current use. The dates here follow Gasche "
                  "et al.'s short chronology as used by Encyclopaedia Iranica, 2400-1450 "
                  "BCE. The traditional scheme labels the same span 'Old Elamite' at "
                  "2700-1500 BCE. Reconstruction rests on a Babylonian king-list tablet found "
                  "at Susa listing twelve Awan then twelve Simashkean kings.",
        source_ids=[S_IRANICA_SUSA])

    ERA("middle-elamite", "Middle Elamite Period", elam, -1450, -1050, "intermediate",
        summary="Elam at its most powerful, building Chogha Zanbil and carrying Babylonian "
                "monuments home as loot — including the Code of Hammurabi.",
        aliases=["Meso-Elamite"],
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_precision="disputed",
        date_note="Iranica's short chronology gives 1450-1050 BCE, UNESCO gives 1400-1100, "
                  "and other reference works give 1500-1100. Three institutional sources, "
                  "three ranges, not reconciled and not averaged.",
        source_ids=[S_IRANICA_SUSA, S_UNESCO_ZANBIL])

    P("chogha-zanbil", "Chogha Zanbil", f"{elam}.middle-elamite", -1250, -640, "intermediate",
      summary="A royal city built around the best-preserved ziggurat in Iran, abandoned "
              "unfinished with thousands of unused bricks still on site.",
      aliases=["Dur-Untash", "Tchogha Zanbil"],
      start_dating_method=CAL, end_dating_method=CAL, standing="majority",
      date_precision="century",
      allow_outside_parent_dates=True,
      date_note="Founded about 1250 BCE by Untash-Napirisha and destroyed by Ashurbanipal "
                "about 640 BCE. The ziggurat was 105.2 m per side and about 53 m tall; "
                "24.75 m survives.",
      alternatives=[
          {"label": "Untash-Napirisha reigned c. 1340-1300 BCE", "standing": "minority",
           "start_year": -1340, "end_year": -1300, "dating_method": CAL,
           "note": "Follows from Iranica's cross-date to Burnaburiaš II. UNESCO instead gives "
                   "1275-1240. Which is right depends on which Kassite king the Berlin Letter "
                   "means.",
           "source_ids": [S_IRANICA_SUSA]},
      ],
      as_of=CHECKED,
      source_ids=[S_UNESCO_ZANBIL, S_IRANICA_SUSA])

    ERA("neo-elamite", "Neo-Elamite Period", elam, -1050, -539, "intermediate",
        summary="Elam's last independent centuries, spent largely in coalition against "
                "Assyria, and known mostly through Assyrian accounts of defeating it.",
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_precision="disputed",
        date_note="Potts gives 1000-539 BC and Iranica 1050-539. The internal boundaries "
                  "differ more: the Neo-Elamite I/II line is placed at 744, 770 or 743 BC "
                  "depending on the scholar. Susa fell to Ashurbanipal in 646 BC and the "
                  "period ends with Cyrus in 539.",
        caveats=[{"kind": "misconception",
                  "text": "Elamite history here is written almost entirely from Assyrian "
                          "royal inscriptions and Babylonian chronicles. Iranica calls the "
                          "reconstruction a prisoner of those sources.",
                  "source_ids": [S_IRANICA_SUSA, S_POTTS_NEOELAM]}],
        source_ids=[S_POTTS_NEOELAM, S_IRANICA_SUSA])

    P("susa", "Susa", elam, -4200, -539, "foundational",
      summary="Occupied for six thousand years, capital of Elam, and the place the Code of "
              "Hammurabi was found — because the Elamites took it there.",
      aliases=["Shush", "Šuš"],
      start_dating_method=C14, end_dating_method=CAL, standing="majority",
      date_precision="century",
      allow_outside_parent_dates=True,
      date_note="Remains span 4200 BCE to the Islamic period; Acropolis buildings date to at "
                "least 4000 BCE. Iranica frames the specifically Elamite phase as 2400-539 "
                "BCE, which is the range that matches this entity's parent.",
      source_ids=[S_CULTURE_SUSA, S_IRANICA_SUSA])

    # ========================================================= ANATOLIA

    ERA("hittites", "The Hittites", ana, -1650, -1180, "foundational",
        summary="An Anatolian empire that fought Egypt to a draw at Kadesh and left the "
                "oldest surviving international peace treaty.",
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_precision="century",
        date_note="About 1650-1190 BCE. The basis is textual — royal annals and the Telipinu "
                  "Proclamation, cross-referenced to Mesopotamian synchronisms — not "
                  "radiocarbon, so the whole sequence shifts with whichever Mesopotamian "
                  "chronology is adopted.",
        source_ids=[S_BRILL_HITTITE])

    P("hittite-old-kingdom", "Hittite Old Kingdom", f"{ana}.hittites", -1650, -1500,
      "intermediate",
      summary="Hattusa becomes the capital and Hittite armies reach Babylon.",
      start_dating_method=CAL, end_dating_method=CAL, standing="majority",
      date_precision="century",
      date_note="The Middle Kingdom that follows is deliberately not authored: the literature "
                "describes it as an ill-defined dark age between Telipinu and Suppiluliuma I "
                "and declines to bound it.",
      source_ids=[S_BRILL_HITTITE])

    EVENT("sack-of-babylon", "Mursili I Sacks Babylon", f"{ana}.hittites", -1595, None,
          "intermediate",
          summary="A Hittite raid ends Hammurabi's dynasty, and the date it happened is the "
                  "hinge the whole Bronze Age chronology turns on.",
          start_dating_method=CAL, standing="majority", date_precision="disputed",
          date_note="1595 BCE on the Middle Chronology, which is the usual default. The "
                    "competing schemes put it at 1736, 1651, 1587, 1531 or 1499 BCE — a "
                    "spread of 237 years. Nothing about this event is independently dated; "
                    "it is a king-list synchronism.",
          alternatives=[
              {"label": "Long Chronology, 1651 BCE", "standing": "minority",
               "start_year": -1651, "dating_method": CAL,
               "note": "Favoured by some astronomical reconstructions of the Venus Tablet.",
               "source_ids": [S_ISAC_BABYLON]},
              {"label": "Short Chronology, 1531 BCE", "standing": "minority",
               "start_year": -1531, "dating_method": CAL,
               "note": "One of the lower readings of the same Venus observations.",
               "source_ids": [S_ISAC_BABYLON]},
          ],
          caveats=[{"kind": "misconception",
                    "text": "1595 BCE is quoted almost everywhere as simply the date. It is "
                            "one scheme's answer to a periodic astronomical record that fits "
                            "several real years equally well.",
                    "source_ids": [S_ISAC_BABYLON]}],
          as_of=CHECKED,
          source_ids=[S_ISAC_BABYLON, S_BRILL_HITTITE])

    P("hattusa", "Hattusa", f"{ana}.hittites", -1650, -1180, "intermediate",
      summary="The Hittite capital, source of the royal archives, and — contrary to the "
              "story everyone tells — probably not sacked.",
      start_dating_method=TYPO, end_dating_method=TYPO, standing="majority",
      date_precision="century",
      caveats=[{"kind": "misconception",
                "text": "Hattusa is usually said to have been burned at the empire's end. "
                        "German Archaeological Institute evidence does not support violent "
                        "destruction; buildings were deliberately emptied first.",
                "source_ids": [S_BRILL_HITTITE]}],
      source_ids=[S_BRILL_HITTITE])

    EVENT("kadesh", "Battle of Kadesh", f"{ana}.hittites", -1274, None, "intermediate",
          summary="Hittites and Egyptians fight the best-documented battle of the Bronze Age "
                  "to a stalemate, then sign a treaty a copy of which hangs at the UN.",
          start_dating_method=CAL, standing="majority", date_precision="disputed",
          date_note="Year 5 of Ramesses II, which is 1274 BCE on the Egyptian Low Chronology "
                    "and about twenty years earlier on the High. The treaty follows in his "
                    "Year 21, usually 1259 BCE.",
          source_ids=[S_BRILL_HITTITE])

    P("hittite-collapse", "Collapse of the Hittite Empire", f"{ana}.hittites", -1200, -1180,
      "intermediate",
      summary="The empire dissolves in the first quarter of the 12th century, during a "
              "drought that tree rings date to three specific years.",
      start_dating_method=CAL, end_dating_method=CAL, standing="majority",
      date_precision="decade",
      date_note="The political collapse is dated textually. The drought is not: tree-ring "
                "widths and stable carbon isotopes in Gordion juniper place a severe "
                "multi-year dry event at 1198-1196 BCE, which is a far more precise date "
                "than anything in the political record it is being matched to.",
      source_ids=[S_CORNELL_DROUGHT, S_BRILL_HITTITE])

    ERA("neo-hittite", "Neo-Hittite States", ana, -1180, -708, "intermediate",
        summary="Luwian- and Aramaic-speaking successor kingdoms that kept Hittite "
                "hieroglyphs alive for four centuries after the empire died.",
        aliases=["Syro-Hittite states"],
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_note="The end is unusually well dated because Assyria recorded each annexation: "
                  "Til Barsip 856, Arpad 740, Patin 738, Damascus 732, Hamath 720, Carchemish "
                  "717, Malatya 712, Gurgum 711, and Kummuh last in 708 BCE.",
        source_ids=[S_BRYCE_ASSYRIA])

    ERA("mitanni", "Mitanni", ana, -1600, -1260, "intermediate",
        summary="A Hurrian kingdom of northern Syria, rival and then in-law to both Egypt "
                "and Hatti, which left the world's oldest horse-training manual.",
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_precision="disputed",
        date_note="Published ranges run from 1650-1275 to 1500-1360 BCE. Its foundation is "
                  "anchored relative to the sack of Babylon — one or two generations before "
                  "it — so the uncertainty is inherited wholesale from the Mesopotamian "
                  "chronology problem rather than being about Mitanni at all.",
        source_ids=[S_NOVAK_MITANNI])

    ERA("urartu", "Urartu", ana, -840, -590, "intermediate",
        summary="An Iron Age kingdom around Lake Van, Assyria's most persistent northern "
                "rival, built on fortresses and irrigation.",
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_precision="disputed",
        date_note="Dated from Urartian royal inscriptions synchronised to Assyrian annals. "
                  "Sarduri I's reign is given as 844-828, 840-830, 835-825 or 834-828 BCE "
                  "across reputable sources. The collapse date could not be confirmed against "
                  "a fetched source and the end year here should be treated as approximate.",
        source_ids=[S_MET_URARTU])

    ERA("phrygia", "Phrygia", ana, -900, -540, "intermediate",
        summary="An Anatolian kingdom centred on Gordion whose king Midas turns out to be "
                "documented in Assyrian records.",
        start_dating_method=C14, end_dating_method=TYPO, standing="majority",
        date_note="Midas appears as Mita of Mushki in Sargon II's annals in 717 and 709 BCE, "
                  "so he is a historically attested king rather than only a legend. Gordion's "
                  "absolute chronology rests on a tree-ring sequence whose end date has been "
                  "revised repeatedly: 751 BCE on a decadal wiggle-match in 2010, then 745 "
                  "+/- 4 BCE on annual radiocarbon in 2020.",
        caveats=[{"kind": "misconception",
                  "text": "The Midas Mound Tumulus is not Midas's tomb. Its timber dates to "
                          "about 740 BCE and Assyrian records show Midas still alive in 709.",
                  "source_ids": [S_PENN_GORDION, S_PEARSON_2020]}],
        source_ids=[S_PENN_GORDION, S_MET_MIDAS, S_PEARSON_2020, S_PEARSON_REPLY])

    ERA("lydia", "Lydia", ana, -680, -546, "intermediate",
        summary="A western Anatolian kingdom rich enough on electrum to invent coined money, "
                "ending when Cyrus took Sardis.",
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_precision="century",
        source_ids=[S_BM_MONEY, S_OEAW_LYDIAN])

    EVENT("coinage", "The Invention of Coinage", f"{ana}.lydia", -650, None, "foundational",
          summary="Struck electrum pieces of guaranteed weight appear in Lydia, and money "
                  "stops having to be weighed out.",
          start_dating_method=TYPO, standing="majority", date_precision="approx",
          date_note="About 650 BCE. The basis is numismatic rather than scientific: hoard "
                    "finds, chiefly the foundation deposit under the Temple of Artemis at "
                    "Ephesus, combined with die and style sequencing.",
          caveats=[{"kind": "misconception",
                    "text": "Croesus did not invent coinage. Electrum coin began under "
                            "Alyattes or earlier; Croesus introduced a bimetallic pure gold "
                            "and silver standard a century later.",
                    "source_ids": [S_BM_MONEY, S_OEAW_LYDIAN]}],
          source_ids=[S_BM_MONEY, S_OEAW_LYDIAN])

    P("troy", "Troy", ana, -3000, 500, "foundational",
      summary="Nine cities stacked on one mound at Hisarlik, one of which may or may not be "
              "Homer's.",
      aliases=["Ilion", "Hisarlik"],
      start_dating_method=TYPO, end_dating_method=TYPO, standing="majority",
      date_precision="century",
      date_note="Levels I to IX span roughly 3000 BCE to 500 CE. The basis is ceramic "
                "cross-dating to Mycenaean imports, supported by over 160 radiocarbon "
                "measurements, but the site's own published table warns that precise absolute "
                "dates are not always possible. Troy VIIa's destruction is bracketed to "
                "1260-1240 BCE on imported pottery.",
      alternatives=[
          {"label": "Homeric Troy is level VI, not VIIa", "standing": "minority",
           "start_year": -1750, "end_year": -1300, "dating_method": TYPO,
           "note": "VI has the monumental fortifications but appears to end in an earthquake. "
                   "VIIa is a poorer rebuild showing crowding and a violent destruction, which "
                   "is why Blegen preferred it.",
           "source_ids": [S_BRITANNICA_TROY, S_OXFORD_ANATOLIA]},
      ],
      caveats=[{"kind": "contested-existence",
                "text": "Whether any Trojan War happened at all, as against a poetic composite "
                        "of several conflicts, is a separate and equally unresolved question.",
                "source_ids": [S_OXFORD_ANATOLIA]}],
      as_of=CHECKED,
      source_ids=[S_BRITANNICA_TROY, S_OXFORD_ANATOLIA])
