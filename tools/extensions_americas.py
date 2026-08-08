"""Holocene America: after the Paleoindians, and before the famous civilisations.

`tools/coverage.py` found the Americas holding a single entity — "Archaic
Period", 9,000 years wide — for the whole span between the Paleoindian
traditions and Norte Chico. The Pleistocene end was already well covered (White
Sands, Clovis, Folsom, Paisley Caves, Cactus Hill), so this pass deliberately
does not re-author those; it adds what came after, plus the one glaring
Pleistocene omission.

Research in `docs/americas-research.md`.

That omission is Monte Verde, which the dataset lacked entirely — awkward, given
it is the site that broke Clovis First, and given that a 2026 *Science* paper
now argues it is roughly ten thousand years younger than everyone thought. Both
positions are carried. The dispute is live and this file takes no side.

The rest of the pass is chosen for what it overturns. Great Lakes copper working
is older than most Old World metallurgy. Chilean mummification predates Egypt's
by two thousand years. The oldest pottery in the hemisphere is Amazonian, not
Andean or Mesoamerican. Monumental mound-building at Watson Brake was done by
hunter-gatherers with no agriculture. Each of these is routinely told backwards.

Cerro Sechin is authored as a warning rather than a date. Its widely repeated
7600 BCE occupation could not be confirmed against the Peruvian government's own
excavation report, whose radiocarbon dates are thousands of years younger. That
does not prove the early date wrong — the report may not have sampled the oldest
strata — so the entity records what the primary source actually contains and
says plainly that the popular figure is unverified.

Beringian Standstill durations and Caverna da Pedra Pintada were flagged `n.a.`
in research and are absent here.
"""

from builders import make_builders
from extensions_prehistory import bp

S_MONTE_VERDE = "monte-verde-antiquity-2023"
S_MONTE_VERDE_2026 = "monte-verde-controversy-2026"
S_COOPERS_FERRY = "davis-2019-coopers-ferry"
S_COOPERS_COMMENT = "coopers-ferry-2020-comment"
S_COOPERS_2022 = "coopers-ferry-2022-stemmed"
S_WST = "rosencrance-western-stemmed"
S_MEGAFAUNA_CLIMATE = "stewart-2021-megafauna-climate"
S_MEGAFAUNA_NE = "northeast-megafauna-decline"
S_WHITE_SANDS_2025 = "holliday-2025-white-sands-mud"
S_WHITE_SANDS_RHODE = "rhode-2024-white-sands-critique"
S_WATSON_BRAKE = "saunders-1997-watson-brake"
S_POVERTY_POINT = "unesco-poverty-point"
S_CHINCHORRO = "marquet-2012-chinchorro"
S_CHINCHORRO_UNESCO = "unesco-chinchorro"
S_LAS_VEGAS = "tohoku-coastal-ecuador"
S_VALDIVIA = "kanomata-2019-san-pedro"
S_HUACA_PRIETA = "huaca-prieta-chronology"
S_CABALLO_MUERTO = "huaca-cortada-excavation"
S_CERRO_SECHIN = "mincul-cerro-sechin-report"
S_OLD_COPPER = "pompeani-2021-old-copper"
S_OLD_COPPER_NEWS = "science-2021-great-lakes-copper"
S_TAPERINHA = "roosevelt-1991-taperinha"

AMERICAS_SOURCES = [
    {"id": S_MONTE_VERDE, "kind": "scholarly",
     "citation": "'Monte Verde II: an assessment of new radiocarbon dates and their sedimentological context', Antiquity (2023)",
     "url": "https://www.cambridge.org/core/journals/antiquity/article/monte-verde-ii-an-assessment-of-new-radiocarbon-dates-and-their-sedimentological-context/CF19BDBDE1ECE700EE59C7BF7CF502FF",
     "note": "Median c. 14,530 cal BP; 95.4% range c. 14,200-14,900 cal BP."},
    {"id": S_MONTE_VERDE_2026, "kind": "news",
     "citation": "'Debate explodes over age of key South American archaeological site', Science (2026)",
     "url": "https://www.science.org/content/article/debate-explodes-over-age-key-south-american-archaeological-site",
     "note": "Surovell, Latorre et al. argue the dated wood was redeposited and the site is 4,200-8,200 years old."},
    {"id": S_COOPERS_FERRY, "kind": "scholarly",
     "citation": "Davis et al. (2019), 'Late Upper Paleolithic occupation at Cooper's Ferry, Idaho, USA', Science 365:891-897",
     "url": "https://pubmed.ncbi.nlm.nih.gov/31467216/",
     "note": "Earliest occupation 16,560-15,280 cal BP, before the ice-free corridor opened."},
    {"id": S_COOPERS_COMMENT, "kind": "scholarly",
     "citation": "Comment on 'Late Upper Paleolithic occupation at Cooper's Ferry' (2020), Science",
     "url": "https://www.science.org/doi/10.1126/science.aaz4695",
     "note": "Minority: argues the dates are younger and fit Greenland Interstadial 1."},
    {"id": S_COOPERS_2022, "kind": "scholarly",
     "citation": "'Dating of a large tool assemblage at the Cooper's Ferry site' (2022), Science Advances",
     "url": "https://www.science.org/doi/10.1126/sciadv.ade1248"},
    {"id": S_WST, "kind": "institutional",
     "citation": "Rosencrance, 'The What, Where, and When of the Western Stemmed Tradition', Center for the Study of the First Americans",
     "url": "https://liberalarts.tamu.edu/csfa/wp-content/uploads/sites/14/2025/01/Rosencrance_WST_Abstract.pdf",
     "note": "States plainly that stemmed points are not derived from Clovis."},
    {"id": S_MEGAFAUNA_CLIMATE, "kind": "scholarly",
     "citation": "Stewart, Carleton & Groucutt (2021), 'Climate change, not human population growth, correlates with Late Quaternary megafauna declines in North America', Nature Communications",
     "url": "https://www.nature.com/articles/s41467-021-21201-8"},
    {"id": S_MEGAFAUNA_NE, "kind": "news",
     "citation": "'What Killed the Great Beasts of North America?', Science",
     "url": "https://www.science.org/content/article/what-killed-great-beasts-north-america",
     "note": "Northeastern case study, plus the overkill proponents' rebuttal to it."},
    {"id": S_WHITE_SANDS_2025, "kind": "news",
     "citation": "'Ancient footprints confirmed as oldest evidence of humans in the Americas' (2025), reporting Holliday & Windingstad, Science Advances",
     "url": "https://www.sciencedaily.com/releases/2025/06/250629033438.htm",
     "note": "Radiocarbon on mud, a third independent material, giving 20,700-22,400 years."},
    {"id": S_WHITE_SANDS_RHODE, "kind": "scholarly",
     "citation": "Rhode et al. (2024), critique of the White Sands chronology, Journal of Quaternary Science",
     "url": "https://www.tandfonline.com/doi/full/10.1080/20555563.2024.2345979",
     "note": "Minority: argues for a significantly younger chronology on isotopic and depositional grounds."},
    {"id": S_WATSON_BRAKE, "kind": "news",
     "citation": "'Oldest earthen mounds heighten mystery', Science, reporting Saunders et al. (1997), Science 277:1796-1799",
     "url": "https://www.science.org/content/article/oldest-earthen-mounds-heighten-mystery",
     "note": "Construction begins 5,400-5,300 years ago and continues 400-600 years."},
    {"id": S_POVERTY_POINT, "kind": "institutional",
     "citation": "UNESCO World Heritage listing, Monumental Earthworks of Poverty Point",
     "url": "https://whc.unesco.org/en/list/1435/"},
    {"id": S_CHINCHORRO, "kind": "scholarly",
     "citation": "Marquet, Santoro, Latorre et al. (2012), 'Emergence of social complexity among coastal hunter-gatherers in the Atacama Desert', PNAS",
     "url": "https://www.pnas.org/doi/10.1073/pnas.1116724109",
     "note": "Oldest artificial mummification c. 7-8 ka BP; the practice ends by c. 4.4 ka BP."},
    {"id": S_CHINCHORRO_UNESCO, "kind": "institutional",
     "citation": "UNESCO World Heritage listing, Chinchorro culture settlement and artificial mummification",
     "url": "https://whc.unesco.org/en/list/1634/"},
    {"id": S_LAS_VEGAS, "kind": "institutional",
     "citation": "'Functional Analysis of Prehistoric Artifacts from Coastal Ecuador', Bulletin of the Tohoku University Museum",
     "url": "https://www.museum.tohoku.ac.jp/pdf/press_info/bulletin/No13/bulletin_13_03.pdf",
     "note": "Las Vegas 10,800-6,600 BP, stated explicitly as uncalibrated."},
    {"id": S_VALDIVIA, "kind": "scholarly",
     "citation": "Kanomata et al. (2019), 'New data on early pottery traditions in South America: the San Pedro complex, Ecuador', Antiquity",
     "url": "https://www.cambridge.org/core/journals/antiquity/article/new-data-on-early-pottery-traditions-in-south-america-the-san-pedro-complex-ecuador/8885FD3A582F285F93728325C4945B66"},
    {"id": S_HUACA_PRIETA, "kind": "scholarly",
     "citation": "'Chronology, mound-building and environment at Huaca Prieta', Antiquity supplementary material",
     "url": "https://static.cambridge.org/content/id/urn:cambridge.org:id:article:S0003598X00062451/resource/name/S0003598X00062451sup001.pdf"},
    {"id": S_CABALLO_MUERTO, "kind": "scholarly",
     "citation": "'Excavaciones en Huaca Cortada, complejo de Caballo Muerto', Boletin de Arqueologia PUCP",
     "url": "https://revistas.pucp.edu.pe/index.php/boletindearqueologia/article/download/970/937/0",
     "note": "Huaca Cortada's earliest floor calibrates to 1621-1443 BC."},
    {"id": S_CERRO_SECHIN, "kind": "institutional",
     "citation": "Ministerio de Cultura del Peru, 'Cerro Sechin: informe tecnico de los estudios, analisis y resultados de los materiales arqueologicos'",
     "url": "https://cdn.www.gob.pe/uploads/document/file/4791046/Informe%20t%C3%A9cnico%20de%20los%20estudios,%20an%C3%A1lisis%20y%20resultados%20de%20los%20materiales%20arqueol%C3%B3gicos%20.pdf",
     "note": "2019 AMS dates on five charcoal samples; oldest is 1887-1689 cal BC. No dates at all for Sechin Bajo."},
    {"id": S_OLD_COPPER, "kind": "scholarly",
     "citation": "Pompeani et al. (2021), 'On the Timing of the Old Copper Complex in North America', Radiocarbon 63(2):513-531",
     "url": "https://www.cambridge.org/core/journals/radiocarbon/article/abs/on-the-timing-of-the-old-copper-complex-in-north-america-a-comparison-of-radiocarbon-dates-from-different-archaeological-contexts/E46715993E58EDC94F225CC6FE776CF2",
     "note": "53 radiocarbon dates and six lake-sediment records; mining begins c. 9,500 years ago."},
    {"id": S_OLD_COPPER_NEWS, "kind": "news",
     "citation": "'Great Lakes people among first coppersmiths' (2021), Science",
     "url": "https://www.science.org/doi/10.1126/science.371.6536.1299",
     "note": "Sets the revision against the previous c. 6,000-years-ago consensus."},
    {"id": S_TAPERINHA, "kind": "scholarly",
     "citation": "Roosevelt et al. (1991), 'Eighth Millennium Pottery from a Prehistoric Shell Midden in the Brazilian Amazon', Science 254:1621-1624",
     "url": "https://www.science.org/doi/10.1126/science.254.5038.1621"},
]

CHECKED = "2026-08-08"
C14 = "radiocarbon-calibrated"
C14_RAW = "radiocarbon-uncalibrated"


def extend(E, entities):
    _, P, _, EVENT, _, FIRST = make_builders(E)
    by_id = {e["id"]: e for e in entities}
    pre = "americas.prehistory"

    # ---- The Pleistocene omission ------------------------------------------
    # Monte Verde is NOT authored here. It already exists as
    # `global.paleolithic.monte-verde`. Authoring a second one is how the units
    # bug in that entity was found: two Monte Verdes, 1,950 years apart. The
    # 2023 Antiquity range and the 2026 controversy were merged into the
    # existing entity in extensions_prehistory.py instead.

    P("coopers-ferry", "Cooper's Ferry", pre, bp(16560), bp(15280), "intermediate",
      summary="An Idaho site occupied before the ice-free corridor was passable, which is the "
              "argument for a Pacific coastal route.",
      start_dating_method=C14, end_dating_method=C14, standing="majority", as_of=CHECKED,
      date_note="Earliest occupation 16,560-15,280 cal BP. The corridor was not available "
                "before c. 14,800 cal BP, so if these dates hold the first people did not "
                "come through it.",
      alternatives=[{
          "label": "Younger chronology (2020 comment)", "standing": "minority",
          "start_year": bp(15000), "dating_method": C14,
          "note": "Argues the dates fit Greenland Interstadial 1, c. 15,000 BP.",
          "source_ids": [S_COOPERS_COMMENT]}],
      source_ids=[S_COOPERS_FERRY, S_COOPERS_COMMENT, S_COOPERS_2022])

    P("western-stemmed", "Western Stemmed Tradition", pre, bp(16000), bp(9000), "intermediate",
      summary="A stone-point tradition of the American Far West that runs alongside Clovis "
              "without descending from it.",
      start_dating_method="unknown", end_dating_method="unknown", standing="majority",
      date_precision="approx",
      date_note="Earliest stemmed points c. 16,000 years ago, main florescence c. 13,000-9,000. "
                "The source gives these as round 'years ago' figures without stating a "
                "calibration, so they are NOT of the same standing as the Bayesian-modelled "
                "Clovis and Folsom ranges and the dating method is recorded as unknown.",
      caveats=[{"kind": "misconception",
                "text": "Not a Clovis derivative. Its proposed antecedents are Upper "
                        "Palaeolithic stemmed-point traditions in northeast Asia.",
                "source_ids": [S_WST]}],
      source_ids=[S_WST])

    EVENT("megafaunal-extinction", "North American Megafaunal Extinction", pre,
          bp(13800), bp(11400), "foundational",
          summary="At least 37 genera, some four-fifths of North America's large mammals, "
                  "disappear near the end of the Pleistocene.",
          start_dating_method=C14, end_dating_method=C14, standing="majority",
          date_precision="approx", as_of=CHECKED,
          date_note="16 of the 37 genera have last-appearance dates between 13.8 and 11.4 ka, "
                    "clustering at the Bolling-Allerod to Younger Dryas transition. WHY they "
                    "died is genuinely open: continent-wide Bayesian modelling finds climate, "
                    "not human population size, correlates with the decline, and a "
                    "northeastern study found 75-90% of megafauna already gone before humans "
                    "arrived there. Overkill proponents reply that absence of butchery "
                    "evidence is not evidence of absence, and that humans may have delivered "
                    "the final blow to already-collapsing populations.",
          alternatives=[{
              "label": "Overkill by human hunting", "standing": "minority",
              "note": "Haynes and Surovell: early human presence is under-sampled, and the "
                      "data are consistent with humans finishing off declining populations.",
              "source_ids": [S_MEGAFAUNA_NE]}],
          source_ids=[S_MEGAFAUNA_CLIMATE, S_MEGAFAUNA_NE])

    # ---- Archaic and monumental --------------------------------------------
    P("watson-brake", "Watson Brake", pre, -3500, -3100, "foundational",
      summary="Eleven earthen mounds in Louisiana raised by hunter-gatherers, nineteen "
              "centuries before Poverty Point.",
      start_dating_method=C14, end_dating_method=C14, standing="consensus",
      date_note="Charcoal from soil horizons beneath the mound bases dates construction to "
                "5,400-5,300 years ago, continuing 400-600 years.",
      caveats=[{"kind": "misconception",
                "text": "Monumental building did not require farming or a food surplus. There "
                        "is little evidence of either here.",
                "source_ids": [S_WATSON_BRAKE]}],
      source_ids=[S_WATSON_BRAKE])

    P("poverty-point", "Poverty Point", pre, bp(3700), bp(3100), "intermediate",
      summary="Concentric earthen ridges and mounds in Louisiana, built by a "
              "hunter-fisher-gatherer society with a continental trade reach.",
      start_dating_method=C14, end_dating_method=C14, standing="consensus",
      source_ids=[S_POVERTY_POINT])

    P("chinchorro", "Chinchorro Culture", pre, -5450, -890, "foundational",
      summary="Coastal foragers of the Atacama who deliberately mummified their dead — "
              "including children and the stillborn — for four thousand years.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="UNESCO gives the settlement span as c. 5450-890 BCE. Artificial mummification "
                "itself begins c. 7-8 ka BP and had practically ceased by 4.4 ka BP, as "
                "extreme aridity set in across the central Atacama.",
      source_ids=[S_CHINCHORRO, S_CHINCHORRO_UNESCO])

    FIRST("artificial-mummification", "Artificial Mummification",
          "global.prehistory.firsts", bp(8000), tier="foundational",
          summary="Deliberate preparation of the dead, practised on the Atacama coast two "
                  "thousand years before anyone in Egypt attempted it.",
          start_dating_method=C14, standing="majority",
          date_note="Oldest known example c. 7-8 ka BP, in northern Chile and southern Peru. "
                    "Coastal settlement in the region begins around 10 ka BP.",
          caveats=[{"kind": "misconception",
                    "text": "Egypt did not invent mummification. The Chinchorro were doing it "
                            "roughly two millennia earlier, and they were foragers, not a "
                            "state.",
                    "source_ids": [S_CHINCHORRO]}],
          source_ids=[S_CHINCHORRO, S_CHINCHORRO_UNESCO])

    P("las-vegas-culture", "Las Vegas Culture", pre, bp(10800), bp(6600), "specialist",
      summary="The oldest known archaeological complex on the Ecuadorian coast, with squash "
              "and bottle gourd cultivated by 9,000 years ago.",
      start_dating_method=C14_RAW, end_dating_method=C14_RAW, standing="majority",
      date_precision="approx",
      date_note="UNCALIBRATED. The source states explicitly that 10,800-6,600 BP are "
                "radiocarbon years, not calendar years, so these are not directly comparable "
                "to the calibrated dates elsewhere in this dataset.",
      source_ids=[S_LAS_VEGAS])

    P("valdivia", "Valdivia Culture", pre, -3650, -2350, "intermediate",
      summary="An early ceramic culture of coastal Ecuador, long claimed as the oldest pottery "
              "in the Americas — which it is not.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="disputed", as_of=CHECKED,
      date_note="Valdivia 1 at 3650-2650 BC and Valdivia 2 at 2650-2350 BC per the Antiquity "
                "study. A separate institutional source gives the culture as 5,000-3,500 "
                "UNCALIBRATED radiocarbon years BP, which is not reconcilable with the above "
                "without a conversion the research did not perform. Both are recorded; neither "
                "is averaged into the other.",
      alternatives=[{
          "label": "Uncalibrated 5,000-3,500 BP range", "standing": "minority",
          "dating_method": C14_RAW,
          "note": "Given by the Tohoku University Museum bulletin without calibration.",
          "source_ids": [S_LAS_VEGAS]}],
      source_ids=[S_VALDIVIA, S_LAS_VEGAS])

    P("huaca-prieta", "Huaca Prieta", pre, bp(13700), bp(4000), "intermediate",
      summary="A Peruvian coastal mound with 13,000 years of human presence, cotton by 6,800 "
              "years ago, and mound-building sustained for three and a half millennia.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="First human presence c. 13,700-13,300 cal BP; initial occupation 9,000-8,000; "
                "mound building begins c. 7,500 cal BP and continues c. 3,500 years. Cotton "
                "production from c. 6,800 cal BP, raised fields by c. 4,800.",
      source_ids=[S_HUACA_PRIETA])

    P("caballo-muerto", "Caballo Muerto", pre, -1500, -400, "specialist",
      summary="A complex of monumental adobe platforms in the Moche valley, with friezes "
              "predating the Moche state by a thousand years.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Huaca Cortada's earliest floor gives two AMS dates calibrating to 1666-1442 "
                "and 1628-1418 BC, averaging 1621-1443 BC, so construction begins around 1500 "
                "BC. The complex-wide 1400-400 BC span from the same report is stated as "
                "UNCALIBRATED and should not be read as calendar years.",
      source_ids=[S_CABALLO_MUERTO])

    P("cerro-sechin", "Cerro Sechin", pre, -1887, None, "specialist",
      summary="A Peruvian site famous for granite friezes of dismembered warriors, and for a "
              "widely repeated early date that its own excavation report does not support.",
      start_dating_method=C14, end_precision="unknown", standing="minority",
      date_precision="disputed",
      date_note="The Peruvian Ministry of Culture's technical report gives 2019 AMS dates on "
                "five charcoal samples from the main building. The oldest is 1887-1689 cal BC. "
                "The report contains NO dates for Sechin Bajo at all.",
      caveats=[{"kind": "misconception",
                "text": "The often-cited 7600 BCE occupation is unverified, not established: "
                        "the government excavation report's own dates are thousands of years "
                        "younger, and it has none at all for Sechin Bajo.",
                "source_ids": [S_CERRO_SECHIN]}],
      source_ids=[S_CERRO_SECHIN])

    # ---- Two thresholds that run the wrong way round -----------------------
    P("old-copper-complex", "Old Copper Complex", pre, bp(9500), bp(5400), "foundational",
      summary="Great Lakes peoples working native copper into tools and points — among the "
              "oldest metalworking traditions anywhere on Earth.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Lake-sediment lead records put the start of mining c. 9,500 years ago, some "
                "3,500 years earlier than the previous estimate; the peak falls between 7,000 "
                "and 5,000 years ago and mining ends around 5,400. Organic material on 15 "
                "artefacts dates 8,500-3,580 cal BP, the oldest being a copper point from "
                "Eagle Lake, Wisconsin. Younger dates from mine contexts are now read as "
                "abandonment and infill rather than active mining — earlier workers were "
                "dating the wrong event.",
      caveats=[{"kind": "misconception",
                "text": "Metalworking in the Americas is popularly credited to much later "
                        "Andean and Mesoamerican societies. Great Lakes copper is at least as "
                        "old as the earliest Old World copper-working, and older than most.",
                "source_ids": [S_OLD_COPPER, S_OLD_COPPER_NEWS]}],
      source_ids=[S_OLD_COPPER, S_OLD_COPPER_NEWS])

    P("taperinha", "Taperinha", pre, bp(8000), bp(7000), "intermediate",
      summary="An Amazonian shell midden holding the oldest pottery in the Western Hemisphere.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Calibrated accelerator dates on pottery, charcoal and shell, plus one "
                "thermoluminescence date on a sherd, give c. 8,000-7,000 BP.",
      caveats=[{"kind": "misconception",
                "text": "The hemisphere's oldest pottery is Amazonian, not Andean or "
                        "Mesoamerican, and it precedes Valdivia ceramics by thousands of years.",
                "source_ids": [S_TAPERINHA]}],
      source_ids=[S_TAPERINHA])

    # ---- Enrich White Sands with the two rounds it was missing -------------
    #
    # The entity already carried the 2021 claim, the 2022 reservoir objection
    # and the 2023 pollen/OSL confirmation. Two more rounds have happened since
    # and they cut in opposite directions, which is exactly the state a reader
    # needs to see rather than a tidy resolution.
    ws = by_id.get("americas.prehistory.white-sands")
    if ws is not None:
        ws["as_of"] = CHECKED
        ws["date_note"] = (
            "The original aquatic-seed dates of about 23-21 ka were independently supported by "
            "terrestrial pollen radiocarbon and quartz OSL in 2023, and again in 2025 by "
            "radiocarbon on mud run at an independent lab, giving 20,700-22,400 years — three "
            "material types, two labs. A 2024 critique still argues for a significantly younger "
            "chronology. No stone tools, hearths or settlement debris have ever been found here, "
            "and that objection remains unanswered."
        )
        ws["alternatives"] = list(ws.get("alternatives", [])) + [{
            "label": "Younger chronology (2024 critique)",
            "standing": "minority",
            "dating_method": C14,
            "note": "Rhode et al.: Ruppia carbon isotopes may carry an age offset, the OSL is "
                    "maximum-limiting only, and the pollen may be redeposited.",
            "source_ids": [S_WHITE_SANDS_RHODE],
        }]
        ws["source_ids"] = list(ws.get("source_ids", [])) + [
            S_WHITE_SANDS_2025, S_WHITE_SANDS_RHODE]
