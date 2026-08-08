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
S_HARMAND = "harmand-2015-lomekwi"


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
    _, P, _, _, TAXON, FIRST = make_builders(E)

    pre = f"{glob}.prehistory"
    E(pre, "era", "Human Prehistory", glob, start=-3300000, end=-3000,
      tier="foundational",
      dating_method="argon-argon",
      standing="consensus",
      summary="From the earliest stone toolmaking to the first written records. Dated by "
              "measurement rather than reckoning, so quoted in years before present.",
      date_note="SCOPE GATE. This app begins where human-like BEHAVIOUR begins, not where a "
                "taxon does. The floor is the earliest knapped stone \u2014 currently Lomekwi 3 at "
                "3.3 Ma, which predates the oldest Homo fossil by about 500,000 years. A "
                "taxonomic floor would exclude the oldest instance of the very behaviour this "
                "app exists to track, and taxonomy is the least stable line available: "
                "H. habilis placement is disputed and the Ledi-Geraru mandible is unnamed. "
                "Knapping is the line rather than tool use, because tool use extends to "
                "chimpanzees and orangutans and so runs past the ~7 Ma common ancestor, which "
                "would make any floor arbitrary. The end is diachronous: writing appears at "
                "different times in different regions.",
      caveats=[{"kind": "misconception",
                "text": "The floor is a behaviour, not a site. If an older knapping site is "
                        "accepted, this date moves and the app's scope does not change.",
                "source_ids": [S_HARMAND]}],
      source_ids=[S_HARMAND])

    # =========================================================================
    # STRAND 1 of 3 - WHO: the hominins
    # =========================================================================
    # Named for its contents, not for the scope rule. The behavioural gate is
    # on the prehistory root above; repeating it here as a branch title would
    # misdescribe a branch that holds twelve species. Physical anthropology is
    # in this app's domain - it is the study of proto-humans and near-humans -
    # while the Deep Time app treats the genus as a single clade node.
    origins = f"{pre}.hominins"
    E(origins, "era", "Hominins", pre,
      start=ma(2.8), end=None, tier="foundational",
      start_year_min=ma(2.80), start_year_max=ma(2.75),
      dating_method="argon-argon",
      standing="consensus",
      summary="Humans, proto-humans and near-humans: a dozen or so named species, most of "
              "which overlapped with others rather than succeeding them in a line.",
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

    TAXON("homo-habilis", "Homo habilis", origins, ma(2.4), ma(1.4), "foundational",
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

    TAXON("homo-rudolfensis", "Homo rudolfensis", origins, ma(1.9), ma(1.8), "specialist",
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

    TAXON("homo-erectus", "Homo erectus", origins, ma(1.89), ka(110), "foundational",
      aliases=["Homo ergaster", "Java Man", "Peking Man"],
      summary="The first widely travelled human species, present from about 1.9 million "
              "years ago until roughly 110,000 years ago in Java.",
      end_year_min=ka(117), end_year_max=ka(108),
      dating_method="uranium-series", standing="consensus",
      date_note="Treated here sensu lato, including African material sometimes separated "
                "as H. ergaster. The terminal Ngandong date rests on Bayesian modelling of "
                "52 radiometric estimates.",
      source_ids=[S_SMITHSONIAN, S_RIZAL])

    TAXON("homo-antecessor", "Homo antecessor", origins, ka(857), ka(780), "specialist",
      summary="An early European human from a Spanish cave, about 800,000 years old, "
              "whose status as a separate species is still argued.",
      dating_method="esr", standing="minority",
      date_note="Gran Dolina level TD6 dates to 780-857 ka. The young limit is fixed by "
                "reversed Matuyama polarity, which requires an age greater than 780 ka.",
      source_ids=[S_FALGUERES])

    TAXON("homo-heidelbergensis", "Homo heidelbergensis", origins, ka(700), ka(200), "intermediate",
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

    TAXON("homo-naledi", "Homo naledi", origins, ka(335), ka(236), "intermediate",
      summary="A small-brained human found deep in a South African cave system, "
              "surprisingly recent at 335,000 to 236,000 years ago.",
      dating_method="uranium-series", standing="consensus",
      date_note="Its position in the human family tree is unresolved.",
      source_ids=[S_SMITHSONIAN])

    TAXON("homo-neanderthalensis", "Homo neanderthalensis", origins, ka(400), ka(40), "foundational",
      aliases=["Neanderthal"],
      summary="Cold-adapted humans across Europe and western Asia, from about 400,000 "
              "years ago until roughly 40,000 years ago.",
      dating_method="unknown", standing="consensus",
      date_note="No method is stated for the 400 ka appearance. The END is radiocarbon: the "
                "associated Mousterian closes 41,030-39,260 cal BP by AMS with Bayesian "
                "modelling across 40 sites. Radiocarbon cannot reach the start, so the two "
                "boundaries rest on different evidence.",
      source_ids=[S_SMITHSONIAN, S_MARIN])

    TAXON("denisovans", "Denisovans", origins, ka(195), ka(52), "intermediate",
      aliases=["Denisova hominin"],
      summary="A human population known mainly from DNA, identified from fragments in a "
              "Siberian cave and traceable in living people.",
      end_year_min=ka(76), end_year_max=ka(52),
      dating_method="unknown", standing="consensus",
      date_note="Genetically unambiguous but with no formally accepted species name and "
                "no type specimen in the conventional sense. The chronology is a Bayesian "
                "model combining radiocarbon, uranium-series and luminescence ages, so no "
                "single method describes it; radiocarbon alone cannot reach 195 ka.",
      source_ids=[S_DOUKA])

    TAXON("homo-floresiensis", "Homo floresiensis", origins, ka(100), ka(60), "intermediate",
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

    TAXON("homo-luzonensis", "Homo luzonensis", origins, ka(134), None, "specialist",
      summary="A human species known from a handful of bones and teeth in a cave on "
              "Luzon, the Philippines.",
      dating_method="uranium-series", standing="minority",
      end_precision="unknown",
      date_note="Minimum age revised upward to at least 134 ka in 2023. No "
                "youngest-remains date is established; the original 67 ka metatarsal age "
                "is now read as a minimum from the dating method rather than a true age.",
      source_ids=[S_NHM_LUZON])

    TAXON("homo-sapiens", "Homo sapiens", origins, ka(315), None, "foundational",
      aliases=["Anatomically modern humans"],
      summary="Our own species, first recognisable in Africa around 300,000 years ago.",
      start_year_min=ka(349), start_year_max=ka(281),
      dating_method="luminescence", standing="consensus",
      allow_outside_parent_dates=True,
      date_note="315 +/- 34 ka is the thermoluminescence age of heated flints with the "
                "Jebel Irhoud hominins in Morocco. Which fossils count as H. sapiens is "
                "itself part of the disagreement about the date.",
      source_ids=[S_HUBLIN])

    TAXON("homo-longi", "Homo longi", origins, ka(146), None, "specialist",
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
      dating_method="unknown", standing="consensus",
      date_note="Hard to separate from the latest Acheulean at the start, so the beginning "
                "is definitional and no single method fixes it. The end differs by region "
                "and by method, and is radiocarbon where it can be reached.",
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
    # Primary parent is the region; it stays visible under the global Neolithic
    # through cross_parent_ids, which is what that field is for.
    P("gobekli-tepe", "G\u00f6bekli Tepe", "west-asia.prehistory", -9530, -8000, "foundational",
      cross_parent_ids=[f"{glob}.neolithic"],
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

    # =========================================================================
    # STRAND 3 of 3 - WHAT THEY FIRST DID: behavioural thresholds
    # =========================================================================
    # Below ~2.6 Ma there are no named industries to hang nodes on, so these
    # carry the record on their own. Each is a ONE-SIDED bound: the earliest
    # KNOWN instance. New evidence moves a threshold older, never younger, so
    # date_precision is 'minimum' and there is no end year - the behaviour
    # continues after the first trace of it.
    #
    # Tool USE is deliberately absent. It extends to chimpanzees and
    # orangutans and so runs past the ~7 Ma common ancestor, which would make
    # any floor arbitrary and turn this into a primatology timeline. Knapping
    # is the line: a manufacturing behaviour with a preservable record.
    firsts = f"{pre}.firsts"
    E(firsts, "era", "Behavioural Firsts", pre, start=-3390000, end=None,
      tier="foundational",
      allow_outside_parent_dates=True,
      dating_method="argon-argon",
      summary="The earliest known evidence for each human behaviour \u2014 toolmaking, fire, "
              "pigment, burial, art, seafaring. Each date is a floor, not an estimate.",
      date_note="Starts with the contested Dikika cut marks at 3.39 Ma, which is older than "
                "the app's 3.3 Ma floor because the floor tracks the oldest ACCEPTED "
                "behaviour and Dikika is not accepted.")

    FIRST("stone-knapping", "Stone Knapping", firsts, ma(3.3), "foundational",
      aliases=["Lomekwian", "Earliest lithic technology"],
      summary="The first deliberate shaping of stone into tools \u2014 the behaviour this app "
              "uses to mark where human prehistory begins.",
      start_year_min=ma(3.44), start_year_max=ma(3.31),
      dating_method="argon-argon", standing="consensus",
      date_note="THE SCOPE FLOOR, defined as a behaviour rather than as a site. Lomekwi 3 is "
                "the present evidence, not the definition: the artefacts lie above the Toroto "
                "Tuff at 3.31 +/- 0.02 Ma, within the Mammoth reverse subchron. If an older "
                "knapping site is accepted, this date moves and the app's scope does not "
                "change. Predates the oldest Homo fossil by about 500,000 years, which is why "
                "the floor is behavioural and not taxonomic.",
      alternatives=[{
          "label": "Assemblage not in primary context",
          "standing": "minority",
          "start_year": ma(3.27),
          "dating_method": "argon-argon",
          "note": "Argues the stratigraphic association with the dated tuff is not "
                  "established. Offers no alternative date; the implied age is essentially "
                  "the same. The excavators replied in 2019.",
          "source_ids": ["dominguez-rodrigo-2016-lomekwi"]}],
      caveats=[{"kind": "contested-existence",
                "text": "A minority reads the flakes as naturally fractured stone rather than "
                        "deliberate knapping.",
                "source_ids": ["dominguez-rodrigo-2016-lomekwi"]}],
      source_ids=[S_HARMAND, "dominguez-rodrigo-2016-lomekwi"])

    FIRST("butchery", "Butchery of Animals", firsts, ma(2.6), "intermediate",
      summary="Cutting meat from bone with stone tools, which opened a food source that "
              "had been out of reach.",
      dating_method="argon-argon", standing="majority",
      date_note="The secure record begins 2.6-2.5 Ma at Gona and Bouri, Ethiopia. A claim "
                "for 3.39 Ma at Dikika is the older candidate and is not accepted.",
      alternatives=[{
          "label": "Dikika cut marks",
          "standing": "minority",
          "start_year": ma(3.39),
          "dating_method": "argon-argon",
          "note": "Marks on two bones claimed as butchery before 3.39 Ma. Critics read "
                  "them as trampling: 96% of experimental trampling grooves are broad and "
                  "open, against 4% of genuine cut marks.",
          "source_ids": ["mcpherron-2010-dikika", "dominguez-rodrigo-2010-dikika"]}],
      caveats=[{"kind": "contested-existence",
                "text": "The 3.39 Ma Dikika claim is widely read as trampling damage rather "
                        "than butchery.",
                "source_ids": ["dominguez-rodrigo-2010-dikika"]}],
      source_ids=["mcpherron-2010-dikika", "dominguez-rodrigo-2010-dikika"])

    FIRST("controlled-fire", "Controlled Use of Fire", firsts, ma(1.0), "foundational",
      summary="Keeping and using fire on purpose, which changed diet, safety and how far "
              "north people could live.",
      start_year_min=ma(1.27), start_year_max=ka(810),
      dating_method="magnetostratigraphy", standing="majority",
      date_note="Wonderwerk Cave Stratum 10 is the standard secure minimum, bracketed by "
                "cosmogenic burial ages of 1.27 +/- 0.19 and 0.98 +/- 0.19 Ma. Older claims "
                "exist and the field has not settled.",
      alternatives=[
          {"label": "Wonderwerk Stratum 11",
           "standing": "minority",
           "start_year": ma(1.79), "end_year": ma(1.07),
           "dating_method": "magnetostratigraphy",
           "note": "A 2026 reanalysis pushes burning at the same cave back to 1.79-1.07 Ma.",
           "source_ids": ["plos-2026-wonderwerk-st11"]},
          {"label": "Gesher Benot Ya'aqov",
           "standing": "majority",
           "start_year": ka(790),
           "dating_method": "magnetostratigraphy",
           "note": "The best-evidenced repeated hearth use, fixed by the Matuyama-Brunhes "
                   "reversal at 0.79 Ma. Younger than Wonderwerk but less contested.",
           "source_ids": ["zohar-2022-cooking"]}],
      source_ids=["berna-2012-wonderwerk", "plos-2026-wonderwerk-st11"])

    FIRST("cooking", "Cooking of Food", firsts, ka(780), "intermediate",
      summary="Applying controlled heat to food, evidenced by fish teeth heated to a "
              "temperature that implies cooking rather than burning.",
      dating_method="magnetostratigraphy", standing="consensus",
      date_note="Gesher Benot Ya'aqov, from eight sequential horizons correlated to marine "
                "isotope stages 18-20. Note the long gap between the earliest fire and the "
                "earliest cooking: the two are not the same behaviour.",
      source_ids=["zohar-2022-cooking"])

    FIRST("pigment-use", "Use of Pigment", firsts, ka(300), "intermediate",
      aliases=["Ochre use"],
      summary="Collecting and working coloured earth, the earliest hint of decoration or "
              "marking.",
      dating_method="argon-argon", standing="consensus",
      date_note="Secure from about 300 ka in both Africa and Europe. Between 1.5 Ma and "
                "300 ka the evidence is sparse and equivocal. Kapthurin GnJh-15 in Kenya is "
                "the earliest well-dated assemblage at 0.284 +/- 0.012 Ma.",
      alternatives=[{
          "label": "Olorgesailie worked pigment",
          "standing": "majority",
          "start_year": ka(320), "end_year": ka(305),
          "dating_method": "argon-argon",
          "note": "Described as the oldest clearly worked pigment.",
          "source_ids": ["brooks-2018-olorgesailie"]}],
      source_ids=["deino-2002-kapthurin", "brooks-2018-olorgesailie"])

    FIRST("deliberate-burial", "Deliberate Burial", firsts, ka(430), "foundational",
      summary="Placing the dead somewhere on purpose rather than leaving them where they "
              "fell.",
      start_year_min=ka(448), start_year_max=ka(427),
      dating_method="uranium-series", standing="majority",
      date_note="Sima de los Huesos in Spain holds over 7,000 bones from at least 29 "
                "individuals, a minimum age since the dated speleothem formed directly on "
                "the deposit. Whether accumulation counts as burial is the argument. Qafzeh "
                "in Israel at 90-100 ka is the earliest undisputed grave.",
      alternatives=[
          {"label": "Qafzeh, earliest undisputed grave",
           "standing": "consensus",
           "start_year": ka(100), "end_year": ka(90),
           "dating_method": "luminescence",
           "note": "A modern-human burial with fallow-deer antlers placed on the chest, cut "
                   "into bedrock. Thermoluminescence on burnt flint.",
           "source_ids": ["valladas-1988-qafzeh", "smithsonian-qafzeh-burial"]},
          {"label": "Homo naledi burial claim",
           "standing": "minority",
           "start_year": ka(335), "end_year": ka(139),
           "dating_method": "esr",
           "note": "A 2023 claim of deliberate burial by a small-brained hominin at Rising "
                   "Star, formally rebutted and not accepted.",
           "source_ids": [S_SMITHSONIAN]}],
      caveats=[{"kind": "contested-existence",
                "text": "Whether the Sima accumulation is burial or another process is "
                        "unresolved; the Homo naledi claim is rejected by most reviewers.",
                "source_ids": ["arnold-2014-sima"]}],
      source_ids=["arnold-2014-sima", "valladas-1988-qafzeh"])

    FIRST("shell-beads", "Personal Ornaments", firsts, ka(142), "intermediate",
      aliases=["Shell beads"],
      summary="Shells pierced and strung to be worn, which means signalling something "
              "about yourself to other people.",
      start_year_min=ka(171), start_year_max=ka(120),
      dating_method="uranium-series", standing="majority",
      date_note="Bizmoune Cave, Morocco: 33 pierced Tritia gibbosula shells, dated by "
                "uranium-series on a speleothem to 142,290 +29,300/-22,060 years at 2 sigma. "
                "Explicitly a minimum. Single-grain OSL on the same layer gives ages as "
                "young as 57,800 +/- 7,200, which is unresolved.",
      alternatives=[{
          "label": "Bizmoune OSL chronology",
          "standing": "minority",
          "start_year": ka(57.8),
          "dating_method": "luminescence",
          "note": "Optically stimulated luminescence on layer 4c returns a far younger age "
                  "than the uranium-series speleothem date.",
          "source_ids": ["sehasseh-2021-bizmoune"]}],
      source_ids=["sehasseh-2021-bizmoune"])

    FIRST("symbolic-engraving", "Abstract Engraving", firsts, ka(77), "intermediate",
      summary="Deliberate cross-hatched patterns cut into ochre \u2014 marks that mean "
              "something without depicting anything.",
      start_year_min=ka(83), start_year_max=ka(71),
      dating_method="luminescence", standing="consensus",
      date_note="Blombos Cave, South Africa: 77 +/- 6 ka by thermoluminescence on burnt "
                "lithics for the engraved ochre, with a drawn cross-hatch in ochre crayon at "
                "about 73 ka from the same site.",
      alternatives=[{
          "label": "Trinil engraved shell",
          "standing": "minority",
          "start_year": ka(540), "end_year": ka(430),
          "dating_method": "argon-argon",
          "note": "A zigzag engraved on a freshwater mussel shell from Java, attributed to "
                  "Homo erectus. If accepted it moves this threshold back by 350,000 years.",
          "source_ids": ["joordens-2015-trinil"]}],
      source_ids=["henshilwood-2002-blombos", "henshilwood-2018-blombos-drawing"])

    FIRST("seafaring", "Intentional Seafaring", firsts, ka(65), "foundational",
      summary="Crossing open water on purpose, out of sight of the far shore, which "
              "requires planning and a built craft.",
      start_year_min=ka(71), start_year_max=ka(59.3),
      dating_method="luminescence", standing="majority",
      date_note="The colonisation of Sahul recorded at Madjedbebe, Australia: 65 +/- 6 ka at "
                "95.4% by single-grain OSL with Bayesian modelling. Reaching Australia "
                "required repeated open-water crossings, so the site dates the voyage as "
                "well as the landfall.",
      alternatives=[{
          "label": "Sceptical reading of the Madjedbebe chronology",
          "standing": "minority",
          "start_year": ka(57), "end_year": ka(49),
          "dating_method": "luminescence",
          "note": "Critics read the same OSL data as about 53 +/- 4 ka, arguing artefacts "
                  "moved down through the sand.",
          "source_ids": ["clarkson-2018-reply"]}],
      source_ids=["clarkson-2017-madjedbebe", "clarkson-2018-reply"])

    FIRST("figurative-art", "Figurative Art", firsts, ka(51.2), "foundational",
      summary="Pictures of recognisable things \u2014 animals and people \u2014 rather than "
              "patterns.",
      dating_method="uranium-series", standing="consensus",
      date_note="A narrative scene at Leang Karampuang, Sulawesi: a warty pig with human "
                "figures, dated by laser-ablation uranium-series on the overlying "
                "carbonate. A minimum, since the art is older than the crust that formed on "
                "it. The 2024 laser-ablation method also pushed the neighbouring Leang "
                "Bulu' Sipong 4 scene from 44 ka to about 48 ka.",
      alternatives=[{
          "label": "European Upper Palaeolithic art",
          "standing": "majority",
          "start_year": bp(37000), "end_year": bp(33500),
          "dating_method": "radiocarbon-calibrated",
          "note": "Chauvet's first occupation is 37,000-33,500 cal BP and the Hohle Fels "
                  "ivory figurine at least 35,000 years old. Long taken as the earliest "
                  "figurative art until the Sulawesi dates.",
          "source_ids": ["oktaviana-2024-sulawesi"]}],
      caveats=[{"kind": "misconception",
                "text": "Often said to begin in Ice Age Europe. The oldest known figurative "
                        "art is in Indonesia and predates Chauvet by some 14,000 years.",
                "source_ids": ["oktaviana-2024-sulawesi"]}],
      source_ids=["oktaviana-2024-sulawesi"])

    # The Lomekwian as an INDUSTRY, distinct from the knapping threshold above.
    # The threshold says when the behaviour starts; this says what the toolkit
    # is called. Oldowan begins 700 kyr later, so this is not a relabel.
    P("lomekwian", "Lomekwian Industry", paleo, ma(3.3), ma(2.6), "specialist",
      summary="The oldest known stone toolkit: large, heavy cores and flakes struck with "
              "techniques unlike the later Oldowan.",
      start_year_min=ma(3.44), start_year_max=ma(3.31),
      dating_method="argon-argon", standing="consensus",
      date_note="Named from Lomekwi 3. Kept separate from the Oldowan because the knapping "
                "technique differs, which is also why the Oldowan's 2.6 Ma start is a "
                "definitional boundary rather than the start of toolmaking.",
      source_ids=[S_HARMAND, "dominguez-rodrigo-2016-lomekwi"])
