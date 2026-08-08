"""Central Asia between the Neolithic and the Bronze Age.

`tools/coverage.py` found this region holding nothing whatever between 10,000
and 3,700 BCE. The dataset went from Denisova Cave straight to Botai, skipping
the arrival of farming in Central Asia entirely.

Research in `docs/centralasia-research.md`.

The organising finding is that crops crossed Asia in the hands of herders, not
farmers. Wheat and barley moved east and broomcorn millet moved west through the
Inner Asian Mountain Corridor, carried by transhumant pastoralists moving between
winter piedmont and summer high pasture — and, at Begash, fed to their sheep.
That happened before steppe-ancestry populations arrived in the region, which
rules out the obvious alternative explanation.

Three entities researched here are deliberately absent, and the reasons differ.
**Kelteminar** has no fetched primary radiocarbon dataset at all; every range in
circulation traces back to tertiary sources without lab numbers. **Altyn-Depe**
inherits the Namazga V uncertainty and has no independent modern dating. **The
Namazga I-VI sequence itself** is the most awkward: it is the standard framework
for the whole region, its phase brackets are quoted everywhere, and essentially
all of them trace back to Soviet-era typology rather than to a published
radiocarbon table. Hiebert found that C14 dates for a single Namazga VI layer
span 1884 to 818 BC. Authoring that sequence would mean importing a chronology
the sources cannot support, so it is left out and said so.
"""

from builders import make_builders
from extensions_prehistory import bp

S_JEITUN_HARRIS = "harris-jeitun-excavations"
S_JEITUN_UCL = "ucl-jeitun-archaeology-international"
S_MONJUKLI = "monjukli-depe-bayesian"
S_BARLEY_PNAS_2025 = "pnas-2025-central-asia-barley"
S_SPENGLER_2014 = "spengler-2014-crop-transmission"
S_HERMES_2019 = "hermes-2019-millet-pastoralism"
S_MILLET_ANTIQUITY = "ventresca-miller-2022-millet-diet"
S_MILLER_1999 = "miller-1999-anau-archaeobotany"
S_GONUR_ZAYTSEVA = "gonur-radiocarbon-zaytseva"
S_GONUR_MARGIANA = "margiana-gonur-depe-report"
S_SARAZM = "unesco-sarazm-dossier"
S_SEIMA_TURBINO = "marchenko-2017-seima-turbino"
S_SEIMA_GRIGORIEV = "grigoriev-2023-seima-turbino"
S_TARIM = "zhang-2021-tarim-mummies"

CENTRAL_ASIA_SOURCES = [
    {"id": S_JEITUN_HARRIS, "kind": "scholarly",
     "citation": "Harris, Gosden & Charles, 'Jeitun: Recent Excavations at an Early Neolithic Site in Southern Turkmenistan'",
     "url": "https://www.academia.edu/102279073/Jeitun_Recent_Excavations_at_an_Early_Neolithic_Site_in_Southern_Turkmenistan",
     "note": "11 AMS dates on individual cereal grains; first occupation slightly before 6000 cal BCE."},
    {"id": S_JEITUN_UCL, "kind": "institutional",
     "citation": "Harris et al., Archaeology International (UCL Press), on Jeitun",
     "url": "https://journals.uclpress.co.uk/ai/article/993/galley/12657/view/",
     "note": "Domestic barley, einkorn, sheep and goat present from first occupation."},
    {"id": S_MONJUKLI, "kind": "scholarly",
     "citation": "Looking Closely: Excavations at Monjukli Depe, Turkmenistan 2010-2014 (Sidestone Press, open access)",
     "url": "https://www.sidestone.com/openaccess/9789088907654.pdf",
     "note": "Bayesian model over 87 AMS dates; finds an 800-900 year hiatus before the Aeneolithic."},
    {"id": S_BARLEY_PNAS_2025, "kind": "scholarly",
     "citation": "Zhou, Spengler et al. (2025), '9,000-year-old barley consumption in the foothills of central Asia', PNAS",
     "url": "https://pnas.org/doi/10.1073/pnas.2424093122"},
    {"id": S_SPENGLER_2014, "kind": "scholarly",
     "citation": "Spengler, Frachetti et al. (2014), 'Early agriculture and crop transmission among Bronze Age mobile pastoralists of Central Eurasia', Proceedings of the Royal Society B",
     "url": "https://royalsocietypublishing.org/doi/10.1098/rspb.2013.3382",
     "note": "Earliest directly dated broomcorn millet outside China, with wheat, in one cremation cist."},
    {"id": S_HERMES_2019, "kind": "scholarly",
     "citation": "Hermes, Frachetti et al. (2019), 'Early integration of pastoralism and millet cultivation in Bronze Age Eurasia', Proceedings of the Royal Society B",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6743000/",
     "note": "Isotopes show millet fed to sheep and goats; predates steppe-ancestry arrival."},
    {"id": S_MILLET_ANTIQUITY, "kind": "scholarly",
     "citation": "Ventresca Miller et al. (2022), 'The integration of millet into the diet of Central Asian populations in the third millennium BC', Antiquity",
     "url": "https://www.cambridge.org/core/journals/antiquity/article/integration-of-millet-into-the-diet-of-central-asian-populations-in-the-third-millennium-bc/1035166AD2FD0E412AE3F3A4C51012D3"},
    {"id": S_MILLER_1999, "kind": "scholarly",
     "citation": "N. Miller (1999), Vegetation History and Archaeobotany 8, on Anau North and Anau South",
     "url": "https://www.sas.upenn.edu/~nmiller0/papers/Miller%201999%20VHA.pdf"},
    {"id": S_GONUR_ZAYTSEVA, "kind": "scholarly",
     "citation": "University of Warsaw anthropology bulletin, citing Zaytseva et al. (2008) on 60 radiocarbon dates from Gonur",
     "url": "https://www.anthropology.uw.edu.pl/07/bne-07-03.pdf",
     "note": "Gonur inhabited 2300-1500 cal BC."},
    {"id": S_GONUR_MARGIANA, "kind": "institutional",
     "citation": "Margiana.su, excavation-affiliated publication on Gonur Depe",
     "url": "https://margiana.su/publication/articles/Art-Urm-2013-Gonur-Depe%20eng%20allFig=.pdf"},
    {"id": S_SARAZM, "kind": "institutional",
     "citation": "UNESCO World Heritage nomination dossier for Sarazm, Republic of Tajikistan",
     "url": "https://whc.unesco.org/uploads/nominations/1141rev.pdf",
     "note": "Reproduces the full radiocarbon table with lab codes and three parallel calibrations."},
    {"id": S_SEIMA_TURBINO, "kind": "scholarly",
     "citation": "Marchenko et al. (2017), 'Radiocarbon Chronology of Complexes With Seima-Turbino Type Objects', Radiocarbon",
     "url": "https://news.tsu.ru/upload/medialibrary/bab/2017_06_marchenko_et_al..pdf",
     "note": "28 AMS samples; moves the phenomenon 500-700 years earlier than the typological estimate."},
    {"id": S_SEIMA_GRIGORIEV, "kind": "scholarly",
     "citation": "Grigoriev (2023), 'Chronology of the Seima-Turbino bronzes, early Shang Dynasty and Santorini eruption', Praehistorische Zeitschrift",
     "url": "https://www.degruyter.com/document/doi/10.1515/pz-2023-2028/html",
     "note": "A third position: 17th-16th century BCE by historical cross-dating."},
    {"id": S_TARIM, "kind": "scholarly",
     "citation": "Zhang, Ning, Cui et al. (2021), 'The genomic origins of the Bronze Age Tarim Basin mummies', Nature 599",
     "url": "https://www.nature.com/articles/s41586-021-04052-7",
     "note": "'Our results do not support previous hypotheses for the origin of the Tarim mummies.'"},
]

CHECKED = "2026-08-08"
C14 = "radiocarbon-calibrated"


def extend(E, entities):
    _, P, ERA, _, _, _ = make_builders(E)
    pre = "central-asia.prehistory"

    P("jeitun", "Jeitun Culture", pre, -6000, -5616, "foundational",
      summary="The earliest farming in Central Asia: mudbrick villages in the Kopet Dag "
              "piedmont, with barley, einkorn, sheep and goat.",
      aliases=["Djeitun"],
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Eleven AMS dates on individual cereal grains put first occupation slightly "
                "before 6000 cal BCE; a Bayesian model over 87 dates at the related site of "
                "Monjukli Depe ends the Neolithic occupation at 5731-5616 cal BCE. The dates "
                "cluster too tightly to resolve the five architectural phases. A hiatus of "
                "800-900 years then follows before the Aeneolithic, so the old model of Jeitun "
                "running straight into Anau IA does not hold.",
      alternatives=[{
          "label": "Long Jeitun period, 6200-4500 BCE", "standing": "superseded",
          "start_year": -6200, "end_year": -4500, "dating_method": C14,
          "note": "Stretched across the gap by assigning undated Middle and Late Jeitun "
                  "material to it.",
          "source_ids": [S_MONJUKLI]}],
      caveats=[{"kind": "misconception",
                "text": "The widely repeated 7200-4500 BC span is not supported by any "
                        "radiocarbon dataset. First occupation is slightly before 6000 cal BCE.",
                "source_ids": [S_JEITUN_HARRIS, S_MONJUKLI]}],
      source_ids=[S_JEITUN_HARRIS, S_JEITUN_UCL, S_MONJUKLI, S_BARLEY_PNAS_2025])

    P("anau", "Anau", pre, -4500, -1700, "specialist",
      summary="The Kopet Dag tell that names the Anau horizon, spanning the Chalcolithic in "
              "its north mound and the Bronze Age in its south.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Anau North 4500-3000 cal BC, Anau South 3000-1700 cal BC. Hiebert's "
                "radiocarbon programme put Anau IA at 4500-4000 BCE, and a later comparative "
                "table at 4350-3900 BCE; these are two renderings of the same dating work, not "
                "independent confirmations, and the underlying table has not been republished.",
      source_ids=[S_MILLER_1999, S_MONJUKLI])

    P("sarazm", "Sarazm", pre, -3500, -2000, "intermediate",
      summary="A Chalcolithic town in the Zeravshan valley of Tajikistan, smelting copper and "
              "trading lapis and turquoise between the steppe, Mesopotamia and the Indus.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="disputed", as_of=CHECKED,
      date_note="The UNESCO dossier reproduces the full radiocarbon table with lab codes and "
                "three parallel calibrations, and flags its own unresolved problem: ceramic "
                "typology ends the site around 2600 BC while the radiocarbon dates run to about "
                "2000 BC. A steppe burial in an Afanasievo-type stone circle ties the site "
                "directly to the pastoralist world to its north.",
      alternatives=[{
          "label": "Ceramic-typological end, c. 2600 BC", "standing": "minority",
          "end_year": -2600, "dating_method": "typological",
          "note": "The dossier states the two lines of evidence are 'not in agreement'.",
          "source_ids": [S_SARAZM]}],
      source_ids=[S_SARAZM])

    ERA("mountain-corridor", "Inner Asian Mountain Corridor", pre, -2840, -1250, "foundational",
        allow_outside_parent_dates=True,
        summary="Wheat and barley moved east and millet moved west across the mountains of "
                "Inner Asia, carried by herders rather than farmers.",
        start_dating_method=C14, end_dating_method=C14, standing="majority",
        date_precision="approx",
        date_note="Directly dated crops run from Tasbas Phase 1 at 2840-2500 BCE and Begash at "
                  "c. 2450-2100 cal BCE, and are "
                  "being locally cultivated at Tasbas by 1450-1250 cal BCE. Transhumant "
                  "movement between piedmont winter grounds and high summer pasture created a "
                  "corridor of contact between Xinjiang and southwest Asia.",
        caveats=[{"kind": "misconception",
                  "text": "Not farmer-to-farmer diffusion. Mobile pastoralists carried the "
                          "crops, and at Begash fed millet to their sheep and goats — the "
                          "exchange predates any steppe-ancestry population in the region.",
                  "source_ids": [S_HERMES_2019]}],
        source_ids=[S_SPENGLER_2014, S_HERMES_2019, S_MILLET_ANTIQUITY])

    P("begash", "Begash", "central-asia.prehistory.mountain-corridor", -2450, -2100,
      "intermediate",
      summary="A Dzhungar Mountains campsite holding the earliest directly dated broomcorn "
              "millet outside China, together with wheat, in a cremation burial.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Two published models that should not be merged: direct AMS calibration gives "
                "Phase 1a at 2450-2100 cal BCE, while OxCal modelling by stratigraphic layer "
                "gives 2345-2080 cal BCE. The difference is method, not new data.",
      alternatives=[{
          "label": "Bayesian model by occupation layer (2019)", "standing": "majority",
          "start_year": -2345, "end_year": -2080, "dating_method": C14,
          "note": "Same evidence, modelled per layer in OxCal rather than calibrated directly.",
          "source_ids": [S_HERMES_2019]}],
      source_ids=[S_SPENGLER_2014, S_HERMES_2019])

    P("tasbas", "Tasbas", "central-asia.prehistory.mountain-corridor", -2840, -1250,
      "specialist",
      summary="A high-altitude Kazakh site where mobile pastoralists were threshing their own "
              "wheat, barley, millet and peas by the late second millennium.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Phase 1 gives 2840-2500 BCE on direct AMS (2655-2480 cal BCE under the 2019 "
                "Bayesian model). Phase 2a, at 1450-1250 cal BCE, has 194 rachises and grain "
                "impressions in mudbrick — the only botanical evidence for local farming among "
                "seasonally mobile pastoralists in second-millennium Central Eurasia.",
      source_ids=[S_SPENGLER_2014, S_HERMES_2019])

    P("gonur-depe", "Gonur Depe", "central-asia.prehistory.bmac", -2300, -1500, "intermediate",
      allow_outside_parent_dates=True,
      summary="The principal city of the Oxus civilisation in the Murghab delta, with palace, "
              "temple and monumental enclosure.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Sixty radiocarbon dates put occupation at 2300-1500 cal BC, with construction "
                "at Gonur North beginning 2300-2250 BC. That runs both earlier and later than "
                "the 2200-1700 BCE bracket carried by the parent Oxus entry, which is a "
                "site-level nuance rather than a correction to it.",
      source_ids=[S_GONUR_ZAYTSEVA, S_GONUR_MARGIANA])

    P("seima-turbino", "Seima-Turbino Phenomenon", pre, -2200, -1900, "foundational",
      summary="A distinctive kit of cast-bronze weapons that appears across five thousand "
              "kilometres of Eurasia without an accompanying culture, pottery or burial rite.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="disputed", as_of=CHECKED,
      date_note="AMS dating of 28 samples places most Seima-Turbino material in the 22nd-20th "
                "centuries cal BCE — Middle Bronze Age, and 500-700 years older than the "
                "typological estimate it replaced. The oldest locus is Pepkinskii Kurgan on the "
                "middle Volga at 26th-21st centuries cal BCE; eastern European finds run "
                "younger, consistent with spread from the east.",
      alternatives=[
          {"label": "Typological cross-dating, 16th-15th c. BCE", "standing": "superseded",
           "start_year": -1600, "end_year": -1400, "dating_method": "typological",
           "note": "Dated by comparison with the Borodino Hoard and Anyang bronzes.",
           "source_ids": [S_SEIMA_TURBINO]},
          {"label": "Historical cross-dating, 17th-16th c. BCE", "standing": "minority",
           "start_year": -1700, "end_year": -1500, "dating_method": "typological",
           "note": "Grigoriev reconciles via the Santorini eruption and early Shang chronology.",
           "source_ids": [S_SEIMA_GRIGORIEV]}],
      source_ids=[S_SEIMA_TURBINO, S_SEIMA_GRIGORIEV])

    P("tarim-mummies", "Tarim Basin Mummies", pre, -2100, -1700, "foundational",
      summary="Naturally desiccated burials in the Taklamakan, long read as evidence of a "
              "western migration into China, and genomically nothing of the kind.",
      aliases=["Xiaohe horizon"],
      start_dating_method=C14, end_dating_method=C14, standing="consensus",
      date_note="AMS dates on the sequenced individuals, calibrated with IntCal20: Gumugou "
                "2135-1939 BCE, Xiaohe 1884-1736 BCE, Beifang 1785-1664 BCE. The contemporary "
                "Dzungarian Basin population further north, at 3000-2800 BCE, is a separate "
                "case and does carry Afanasievo ancestry.",
      caveats=[{"kind": "misconception",
                "text": "Not migrants. The 2021 genomes carry no Afanasievo, Oxus or corridor "
                        "ancestry at all — a local population that borrowed its neighbours' "
                        "wheat and dairying rather than importing them.",
                "source_ids": [S_TARIM]}],
      source_ids=[S_TARIM])
