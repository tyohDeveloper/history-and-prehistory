"""Human prehistory: the genus Homo and the stone-tool industries.

Dates, uncertainty bounds, methods and disputes come from
docs/homo-research.md, which carries a source URL beside every value. Where
that report says "n.a." the field is left unset rather than filled with a
plausible number.

Two things worth knowing before editing this file.

**Years are historical Gregorian, not BP.** The dataset's storage convention is
negative-for-BCE with no year zero, so BP values are converted on the way in by
`bp()`. The 1950 datum is noise at Ma scale and real at ka scale, so it is
applied properly rather than approximated. The app converts back for display.

**Species and industries are separate branches.** A taxon is not a period: the
Mousterian is an assemblage type that outlived some of its makers, and
H. sapiens is extant. Filing species under an archaeological era would misstate
both. Species hang from `global.prehistory.origins`, industries from
`global.paleolithic`.
"""

from builders import make_builders

# --- Sources cited below, by id in sources.json ------------------------------
S_SMITHSONIAN = "smithsonian-human-origins"
S_VILLMOARE = "villmoare-2015-ledi-geraru"
S_HAWKS = "hawks-2015-ledi-geraru-dissent"
S_GURUMAHA = "nature-2025-gurumaha-tuff"
S_RIZAL = "rizal-2020-ngandong"
S_FALGUERES = "falgueres-gran-dolina"
S_DOUKA = "douka-2019-denisova"
S_SUTIKNA = "sutikna-2016-flores"
S_NHM_LUZON = "nhm-luzonensis"
S_HUBLIN = "hublin-2017-jebel-irhoud"
S_JI = "ji-2021-homo-longi"
S_FU = "fu-2025-harbin-proteome"
S_LEPRE = "lepre-2011-kokiselei"
S_MARIN = "marin-arroyo-2018-cantabria"
S_BANKS = "banks-2013-aurignacian"
S_RIOS = "rios-garaizar-2022-chatelperronian"
S_CASCALHEIRA = "cascalheira-2015-solutrean"
S_WURZ = "wurz-2013-msa"
S_JACOBS = "jacobs-2008-msa"
S_VILLA = "villa-2012-border-cave"
S_PLOS_ATERIAN = "plos-2022-el-mnasra"


def bp(years_before_present):
    """Historical Gregorian year from a years-BP figure.

    BP counts back from 1950 CE. Historical numbering has no year zero, so the
    conversion goes through astronomical years and then steps over the gap.
    """
    astronomical = 1950 - years_before_present
    return astronomical - 1 if astronomical <= 0 else astronomical


def ma(millions):
    return bp(int(millions * 1_000_000))


def ka(thousands):
    return bp(int(thousands * 1_000))


def extend(E, glob):
    _, P, _, _ = make_builders(E)

    pre = f"{glob}.prehistory"
    E(pre, "era", "Human Prehistory", glob, start=-3300000, end=-3000,
      tier="foundational",
      dating_method="argon-argon",
      summary="From the earliest stone tools to the first written records. Dated by "
              "measurement rather than reckoning, so quoted in years before present.",
      date_note="Begins with the earliest knapped stone at 3.3 Ma, which predates the "
                "genus Homo: the toolmaking record runs continuously across that "
                "taxonomic boundary. Ends diachronously, as writing appears at different "
                "times in different regions.")

    # =========================================================================
    # THE GENUS HOMO
    # =========================================================================
    origins = f"{pre}.origins"
    E(origins, "era", "The Genus Homo", pre,
      start=ma(2.8), end=None, tier="foundational",
      start_year_min=ma(2.80), start_year_max=ma(2.75),
      dating_method="argon-argon",
      standing="consensus",
      summary="Our own genus: a dozen or so named species, most of which overlapped with "
              "others rather than succeeding them in a line.",
      allow_outside_parent_dates=True,
      date_note="The earliest fossil attributed to Homo is LD 350-1 from Ledi-Geraru, "
                "Ethiopia, at 2.80-2.75 Ma, constrained by the Gurumaha Tuff at "
                "2.782 +/- 0.006 Ma. The genus is ongoing, so it outlasts prehistory "
                "rather than ending with it.",
      alternatives=[{
          "label": "LD 350-1 not assignable to Homo",
          "standing": "minority",
          "start_year": ma(2.8),
          "dating_method": "argon-argon",
          "note": "Argues the mandible cannot be unequivocally attributed to Homo, which "
                  "would leave the genus with no securely dated fossil this early.",
          "source_ids": [S_HAWKS],
      }],
      source_ids=[S_VILLMOARE, S_GURUMAHA, S_HAWKS])

    P("homo-habilis", "Homo habilis", origins, ma(2.4), ma(1.4), "foundational",
      summary="An early, small-brained human in Africa from about 2.4 to 1.4 million "
              "years ago, overlapping with other human species.",
      dating_method="argon-argon", standing="consensus",
      date_note="Whether the material forms one species, and whether it belongs in Homo "
                "at all, is still argued. The late specimen KNM-ER 42703 is 1.44 Ma.",
      caveats=[{"kind": "contested-existence",
                "text": "Some researchers would move this material out of Homo entirely, "
                        "which would change where our genus begins.",
                "source_ids": [S_SMITHSONIAN]}],
      source_ids=[S_SMITHSONIAN])

    P("homo-rudolfensis", "Homo rudolfensis", origins, ma(1.9), ma(1.8), "specialist",
      summary="A flat-faced, big-toothed early human from Kenya about 1.9 million years "
              "ago whose place in the human genus is still argued over.",
      dating_method="argon-argon", standing="minority",
      date_note="Type specimen KNM-ER 1470, Koobi Fora. Four hominin species coexisted in "
                "the Turkana Basin between 2.0 and 1.5 Ma.",
      caveats=[{"kind": "contested-existence",
                "text": "Some researchers assign this material to Homo habilis rather than "
                        "to a separate species.",
                "source_ids": [S_SMITHSONIAN]}],
      source_ids=[S_SMITHSONIAN])

    P("homo-erectus", "Homo erectus", origins, ma(1.89), ka(110), "foundational",
      aliases=["Homo ergaster", "Java Man", "Peking Man"],
      summary="The first widely travelled human species, present from about 1.9 million "
              "years ago until roughly 110,000 years ago in Java.",
      end_year_min=ka(117), end_year_max=ka(108),
      dating_method="uranium-series", standing="consensus",
      date_note="Treated here sensu lato, including African material sometimes separated "
                "as H. ergaster. The terminal Ngandong date rests on Bayesian modelling of "
                "52 radiometric estimates.",
      source_ids=[S_SMITHSONIAN, S_RIZAL])

    P("homo-antecessor", "Homo antecessor", origins, ka(857), ka(780), "specialist",
      summary="An early European human from a Spanish cave, about 800,000 years old, "
              "whose status as a separate species is still argued.",
      dating_method="esr", standing="minority",
      date_note="Gran Dolina level TD6 dates to 780-857 ka. The young limit is fixed by "
                "reversed Matuyama polarity, which requires an age greater than 780 ka.",
      source_ids=[S_FALGUERES])

    P("homo-heidelbergensis", "Homo heidelbergensis", origins, ka(700), ka(200), "intermediate",
      summary="A large-brained Middle Pleistocene human in Europe, Africa and the Near "
              "East, roughly 700,000 to 200,000 years ago.",
      start_year_min=ma(1.3), start_year_max=ka(700),
      dating_method="unknown", standing="consensus",
      date_note="Range may reach 1.3 Ma if older Spanish and Italian material is included.",
      caveats=[{"kind": "misconception",
                "text": "Functions partly as a catch-all for Middle Pleistocene humans; "
                        "several proposed splits would dismantle it.",
                "source_ids": [S_SMITHSONIAN]}],
      source_ids=[S_SMITHSONIAN])

    P("homo-naledi", "Homo naledi", origins, ka(335), ka(236), "intermediate",
      summary="A small-brained human found deep in a South African cave system, "
              "surprisingly recent at 335,000 to 236,000 years ago.",
      dating_method="uranium-series", standing="consensus",
      date_note="Its position in the human family tree is unresolved.",
      source_ids=[S_SMITHSONIAN])

    P("homo-neanderthalensis", "Homo neanderthalensis", origins, ka(400), ka(40), "foundational",
      aliases=["Neanderthal"],
      summary="Cold-adapted humans across Europe and western Asia, from about 400,000 "
              "years ago until roughly 40,000 years ago.",
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="The extinction date is not uniform across the range; the associated "
                "Mousterian ends 41,030-39,260 cal BP.",
      source_ids=[S_SMITHSONIAN, S_MARIN])

    P("denisovans", "Denisovans", origins, ka(195), ka(52), "intermediate",
      aliases=["Denisova hominin"],
      summary="A human population known mainly from DNA, identified from fragments in a "
              "Siberian cave and traceable in living people.",
      end_year_min=ka(76), end_year_max=ka(52),
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="Genetically unambiguous but with no formally accepted species name and "
                "no type specimen in the conventional sense.",
      source_ids=[S_DOUKA])

    P("homo-floresiensis", "Homo floresiensis", origins, ka(100), ka(60), "intermediate",
      aliases=["Flores hobbit"],
      summary="A small-bodied human on the Indonesian island of Flores, known from Liang "
              "Bua cave.",
      dating_method="luminescence", standing="consensus",
      date_note="Skeletal remains to about 60 ka, associated artefacts from about 190 ka "
                "and continuing to about 50 ka.",
      alternatives=[{
          "label": "Original 2004 chronology",
          "standing": "superseded",
          "start_year": ka(18), "end_year": ka(12),
          "dating_method": "radiocarbon-calibrated",
          "note": "Withdrawn in 2016: the dated deposits proved to be a younger unit "
                  "unconformably overlying the remains.",
          "source_ids": [S_SUTIKNA]}],
      caveats=[{"kind": "misconception",
                "text": "Often reported as surviving until 12,000 years ago. That date was "
                        "corrected to around 60,000 in 2016.",
                "source_ids": [S_SUTIKNA]}],
      source_ids=[S_SUTIKNA])

    P("homo-luzonensis", "Homo luzonensis", origins, ka(134), None, "specialist",
      summary="A human species known from a handful of bones and teeth in a cave on "
              "Luzon, the Philippines.",
      dating_method="uranium-series", standing="minority",
      end_precision="unknown",
      date_note="Minimum age revised upward to at least 134 ka in 2023. No "
                "youngest-remains date is established; the original 67 ka metatarsal age "
                "is now read as a minimum from the dating method rather than a true age.",
      source_ids=[S_NHM_LUZON])

    P("homo-sapiens", "Homo sapiens", origins, ka(315), None, "foundational",
      aliases=["Anatomically modern humans"],
      summary="Our own species, first recognisable in Africa around 300,000 years ago.",
      start_year_min=ka(349), start_year_max=ka(281),
      dating_method="luminescence", standing="consensus",
      allow_outside_parent_dates=True,
      date_note="315 +/- 34 ka is the thermoluminescence age of heated flints with the "
                "Jebel Irhoud hominins in Morocco. Which fossils count as H. sapiens is "
                "itself part of the disagreement about the date.",
      source_ids=[S_HUBLIN])

    P("homo-longi", "Homo longi", origins, ka(146), None, "specialist",
      aliases=["Dragon Man", "Harbin cranium"],
      summary="A single large skull from Harbin, China, whose identity was overturned by "
              "protein analysis in 2025.",
      dating_method="uranium-series", standing="minority",
      end_precision="unknown",
      date_note="Known from one cranium with a minimum U-series age of about 146 ka, so "
                "there is no species-level range.",
      alternatives=[{
          "label": "Harbin cranium is Denisovan",
          "standing": "majority",
          "start_year": ka(146),
          "dating_method": "uranium-series",
          "note": "Palaeoproteomic analysis in 2025 recovered 95 endogenous proteins and "
                  "clustered the specimen with Denisova 3.",
          "source_ids": [S_FU]}],
      caveats=[{"kind": "contested-existence",
                "text": "Named as a new species in 2021; 2025 protein evidence indicates "
                        "the specimen is a Denisovan.",
                "source_ids": [S_FU]}],
      source_ids=[S_JI, S_FU])

    # =========================================================================
    # STONE TOOL INDUSTRIES
    # =========================================================================
    # Under the Paleolithic era, not under the species: an industry is an
    # assemblage type, and several outlived or crossed their makers.
    paleo = f"{glob}.paleolithic"

    P("oldowan", "Oldowan Industry", paleo, ma(2.6), ma(1.7), "foundational",
      summary="The earliest widely recognised stone tools: sharp flakes struck from "
              "pebble cores.",
      start_year_min=ma(2.618), start_year_max=ma(2.55),
      dating_method="argon-argon", standing="consensus",
      date_note="Usually given as 2.6-1.7 Ma. Older claims exist, but the 3.3 Ma Lomekwi 3 "
                "tools are excluded by classifying them as Lomekwian, so the boundary is "
                "definitional as much as evidential.",
      source_ids=["braun-2019-bokol-dora"])

    P("acheulean", "Acheulean Industry", paleo, ma(1.76), ka(200), "foundational",
      summary="The handaxe tradition: teardrop-shaped tools worked on both faces, made "
              "for well over a million years.",
      end_year_min=ka(250), end_year_max=ka(200),
      dating_method="magnetostratigraphy", standing="consensus",
      date_note="Earliest at Kokiselei 4, West Turkana, Kenya, at 1.76 Ma \u2014 about "
                "350,000 years earlier than previously accepted. The end is diffuse rather "
                "than dated.",
      source_ids=[S_LEPRE])

    P("mousterian", "Mousterian Industry", paleo, ka(130), ka(40), "foundational",
      summary="The flake-tool tradition associated mainly with Neanderthals across Europe "
              "and western Asia.",
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="Hard to separate from the latest Acheulean at the start, so the beginning "
                "is definitional. The end differs by region and by method.",
      source_ids=[S_MARIN])

    P("aterian", "Aterian Industry", paleo, ka(145), ka(40), "intermediate",
      summary="A North African tradition marked by tanged points, made by early modern "
              "humans across the Sahara.",
      start_year_min=ka(154), start_year_max=ka(136),
      dating_method="luminescence", standing="consensus",
      date_note="145 +/- 9 ka is the weighted-mean thermoluminescence age at El Mnasra. "
                "The industry is defined by tool shape rather than by date, so its limits "
                "move with the definition.",
      source_ids=[S_PLOS_ATERIAN])

    P("still-bay", "Still Bay Industry", paleo, ka(75.5), ka(67.8), "specialist",
      summary="A brief South African tradition of finely worked leaf-shaped points, an "
              "early flowering of complex technique.",
      dating_method="luminescence", standing="consensus",
      date_note="Single-grain OSL makes this a short episode of under 5,000 years.",
      alternatives=[{
          "label": "Diepkloof thermoluminescence chronology",
          "standing": "minority",
          "start_year": ka(109),
          "dating_method": "luminescence",
          "note": "TL at Diepkloof puts the Still Bay some 35,000 years earlier than the "
                  "single-grain OSL chronology.",
          "source_ids": [S_WURZ]}],
      source_ids=[S_WURZ, S_JACOBS])

    P("howiesons-poort", "Howiesons Poort Industry", paleo, ka(64.8), ka(59.5), "specialist",
      summary="A South African tradition of small backed blades, hafted as composite "
              "tools, lasting only a few thousand years.",
      dating_method="luminescence", standing="consensus",
      date_note="Single-grain OSL makes this a tight horizon marker; ESR and TL at Klasies "
                "River give a looser 50,000-60,000 years.",
      alternatives=[{
          "label": "Klasies River ESR/TL chronology",
          "standing": "minority",
          "start_year": ka(60), "end_year": ka(50),
          "dating_method": "esr",
          "note": "Looser and younger than the single-grain OSL horizon.",
          "source_ids": [S_WURZ]}],
      source_ids=[S_WURZ, S_JACOBS])

    P("later-stone-age", "Later Stone Age", paleo, ka(44), ka(12), "intermediate",
      summary="The sub-Saharan African tradition of small composite tools that continues "
              "into the historical period.",
      start_year_min=ka(44.2), start_year_max=ka(42.5),
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="Border Cave gives 44.2-43.0 cal BP for the earliest layer. There is no "
                "real end date: the Later Stone Age runs on into recorded history, and the "
                "value here is a convention for the tree rather than a finding.",
      source_ids=[S_VILLA])

    P("chatelperronian", "Ch\u00e2telperronian Industry", paleo, bp(43760), bp(39220), "specialist",
      summary="A short-lived western European tradition made during the overlap between "
              "Neanderthals and modern humans.",
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="In Cantabria it shows no chronological overlap with the local Mousterian, "
                "which complicates the usual reading of it as a Neanderthal response to "
                "arriving modern humans.",
      source_ids=[S_RIOS, S_MARIN])

    P("aurignacian", "Aurignacian Industry", paleo, bp(43300), bp(33100), "foundational",
      summary="The first widespread modern-human tradition in Europe, associated with the "
              "earliest cave art and figurines.",
      start_year_min=bp(43300), start_year_max=bp(40500),
      end_year_min=bp(34600), end_year_max=bp(33100),
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="Arrival dates differ sharply between regional models, from about 43 cal "
                "ka BP in southern Iberia to later elsewhere.",
      alternatives=[{
          "label": "Banks et al. 2013 phase model",
          "standing": "majority",
          "start_year": bp(41500), "end_year": bp(37900),
          "dating_method": "radiocarbon-calibrated",
          "note": "Proto-Aurignacian 41.5-39.9 k cal BP, Early Aurignacian 39.8-37.9 k cal BP.",
          "source_ids": [S_BANKS]}],
      source_ids=[S_MARIN, S_BANKS])

    P("gravettian", "Gravettian Industry", paleo, bp(35340), bp(24230), "intermediate",
      summary="The tradition of the Venus figurines and mammoth-bone dwellings, spanning "
              "Europe through the coldest part of the Ice Age.",
      start_year_min=bp(35340), start_year_max=bp(33595),
      end_year_min=bp(26390), end_year_max=bp(24230),
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="Bayesian boundaries from the Adriatic basin; regional models differ.",
      source_ids=[S_MARIN])

    P("solutrean", "Solutrean Industry", paleo, bp(25000), bp(19000), "specialist",
      summary="An Iberian and French tradition known for slender, finely pressure-flaked "
              "laurel-leaf points.",
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="Bayesian analysis does not confirm the traditional ordering of the "
                "internal phases, so the sub-sequence is less secure than the overall span.",
      source_ids=[S_CASCALHEIRA])

    P("magdalenian", "Magdalenian Industry", paleo, bp(21211), bp(14610), "intermediate",
      summary="The late Ice Age tradition of Lascaux and Altamira, ending as the glaciers "
              "retreated.",
      start_year_min=bp(21211), start_year_max=bp(17988),
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="Preceded by the Badegoulian at 23,092-20,792 cal BP. Regional phase "
                "models disagree on the internal sequence.",
      source_ids=[S_MARIN])

    # =========================================================================
    # SITES — placed under the era they belong to, not under prehistory flat
    # =========================================================================
    P("gobekli-tepe", "G\u00f6bekli Tepe", f"{glob}.neolithic", -9530, -8000, "foundational",
      native="G\u00f6bekli Tepe",
      summary="Monumental enclosures raised by people who were not yet farming, in "
              "southeastern Anatolia.",
      start_year_min=-9745, start_year_max=-9314,
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="Only 11 radiocarbon dates exist. The Layer III/II/I scheme has been "
                "abandoned for at least eight phases, so phase labels in older sources do "
                "not map cleanly.",
      source_ids=["dietrich-2013-gobekli"])

    P("monte-verde", "Monte Verde II", paleo, -14500, -14000, "intermediate",
      summary="A settlement in southern Chile whose age broke the Clovis-first model of "
              "the peopling of the Americas.",
      dating_method="radiocarbon-calibrated", standing="consensus",
      as_of="2026-06-30",
      date_note="Under active challenge: a March 2026 reanalysis proposed a Holocene age, "
                "roughly thirty specialists rebutted it in May, and the authors replied in "
                "June.",
      alternatives=[{
          "label": "Surovell et al. 2026",
          "standing": "minority",
          "start_year": -8200, "end_year": -4200,
          "dating_method": "radiocarbon-calibrated",
          "note": "Argues the dated material is intrusive and the occupation is mid-Holocene.",
          "source_ids": ["surovell-2026-monte-verde"]}],
      source_ids=["dillehay-1997-monte-verde", "surovell-2026-monte-verde"])
