"""Regional prehistory: the attach points named in the gap analysis §4.2.

Each region gets a `<region>.prehistory` era holding named cultures, phases and
sites. Industries stay on the global Paleolithic spine and cross-parent into the
region, because an industry is not owned by a modern country.

## The calibration hazard

Two original entities here store UNCALIBRATED radiocarbon and are marked as
such: Jericho's tower and 'Ain Ghazal's statues. Additional regional entries
below make the same status explicit wherever the supplied research calls for it.
The app refuses calendar conversion (see `isCalendarConvertible`).

The opposite trap also appears here: uranium-series, OSL and TL ages are
routinely published as "BP" without being radiocarbon at all. Those need no
calibration and are stored as `geological` sense via their method.
"""

from builders import make_builders

S_DEINO = "deino-2012-olduvai"
S_VIDAL = "vidal-2022-omo"
S_BADER = "bader-2022-msa"
S_JACOBS_B = "jacobs-2006-blombos"
S_KLASIES = "klasies-river-guide"
S_BACKWELL = "backwell-2018-border-cave"
S_MCGEE = "mcgee-2017-ahp"
S_WENDORF = "wendorf-1998-nabta"
S_MALVILLE = "malville-1998-nabta"
S_PPND = "ppnd-summary"
S_OX_NAT = "oxford-natufian"
S_ORTON = "orton-catalhoyuk"
S_HALAF = "halaf-chronology"
S_UBAID = "beyond-the-ubaid"
S_BARYOSEF = "bar-yosef-jericho"
S_PPND_JER = "ppnd-jericho"
S_GRISSOM = "grissom-ain-ghazal"
S_PPND_AG = "ppnd-ain-ghazal"

# Europe and Central Asia
S_SIMA = "arsuaga-2014-sima"
S_HIGHAM = "higham-2014-neanderthal"
S_CHAUVET = "quiles-2016-chauvet"
S_CHAUVET_ALT = "pettitt-bahn-2015-chauvet"
S_LASCAUX = "culture-gouv-lascaux"
S_ALTAMIRA = "garcia-diez-2013-altamira"
S_LBK = "jakucs-2016-lbk"
S_MEGALITH = "schulz-paulsson-2019-megaliths"
S_STONE = "darvill-2012-stonehenge"
S_CORDED = "papac-2021-corded-ware"
S_BEAKER = "olalde-2018-beaker"
S_OTZI = "kutschera-otzi"
S_DENISOVA = "douka-2019-denisova"
S_BOTAI = "taylor-2021-botai"
S_AFAN = "poliakov-2023-afanasievo"
S_ANDRON = "grigoriev-2021-andronovo"
S_BMAC = "lamberg-karlovsky-bmac"
S_YAMNAYA = "lazaridis-2025-yamnaya"

# Asia
S_JOMON = "matsumoto-2017-jomon"
S_KEALLY = "keally-jomon-dates"
S_PEILIGANG = "zhang-2013-peiligang"
S_YANGSHAO = "frontiers-2021-yangshao"
S_HONGSHAN = "cass-hongshan"
S_LONGSHAN = "haidai-longshan"
S_LIANGZHU = "liu-2017-liangzhu"
S_JIAHU = "zhang-1999-jiahu"
S_MEHRGARH = "mutin-2025-mehrgarh"
S_BHIRRANA = "sarkar-2016-bhirrana"
S_BHIRRANA_ASI = "asi-bhirrana-review"
S_RAVI = "kenoyer-2000-ravi"
S_LAHURADEWA = "patel-agnihotri-lahuradewa"
S_HOABINHIAN = "forestier-2013-hoabinhian"
S_HOABINHIAN_OLD = "ji-2016-hoabinhian"
S_BAN_CHIANG = "higham-2015-ban-chiang"
S_NIAH = "barker-2007-niah"
S_RICE = "zheng-2016-rice"

# Americas and Oceania
S_BERINGIA = "pico-2022-beringia"
S_PRE_CLOVIS = "waters-2019-preclovis"
S_WHITE_SANDS = "bennett-2021-white-sands"
S_WHITE_REPLY = "pigati-2023-white-sands"
S_WHITE_CRITIQUE = "madsen-2022-white-sands"
S_CLOVIS = "waters-2020-clovis"
S_CLOVIS_2007 = "waters-stafford-2007-clovis"
S_FOLSOM = "buchanan-2021-folsom"
S_PALEOINDIAN = "cambridge-paleoindian-archaic"
S_ARCHAIC = "nps-archaic"
S_CACTUS = "encyclopedia-virginia-cactus-hill"
S_PAISLEY = "jenkins-paisley-geochronology"
S_SAHUL = "bradshaw-2021-sahul"
S_MADJ = "clarkson-2017-madjedbebe"
S_MUNGO = "bowler-2003-mungo"
S_AHRC = "ahrc-aboriginal-history"
S_LAPITA = "specht-lapita"
S_POLYNESIA = "wilmshurst-2011-polynesia"


def bp(years_before_present):
    astronomical = 1950 - years_before_present
    return astronomical - 1 if astronomical <= 0 else astronomical


def ka(thousands):
    return bp(int(thousands * 1_000))


def ma(millions):
    return bp(int(millions * 1_000_000))


def extend(E, glob):
    _, P, ERA, _, _, _ = make_builders(E)
    paleo = f"{glob}.paleolithic"

    # =========================================================================
    # The Middle Stone Age, on the global spine
    # =========================================================================
    # Still Bay and Howiesons Poort are sub-industries of the MSA, not its
    # siblings, so they move under it. Cross-parented into Africa because that
    # is where all of it is, while the node itself is an industry.
    P("middle-stone-age", "Middle Stone Age", paleo, ka(300), ka(30), "foundational",
      cross_parent_ids=["africa.prehistory"],
      summary="The long African toolmaking tradition during which our own species appeared, "
              "and with it pigment, beads and engraving.",
      dating_method="luminescence", standing="consensus",
      date_note="Roughly 300-30 ka, about 270,000 years. The end is regionally staggered. "
                "Radiocarbon only reaches the terminal MSA; everything older rests on OSL, "
                "TL, ESR and uranium-series, whose ages are quoted as 'BP' but are not "
                "radiocarbon and need no calibration.",
      alternatives=[{
          "label": "Jacobs & Roberts maximum-age chronology",
          "standing": "minority",
          "start_year": ka(300), "end_year": ka(30),
          "dating_method": "luminescence",
          "note": "Single-grain OSL compresses the diagnostic sub-industries into brief "
                  "horizons; TL and ESR readings stretch them.",
          "source_ids": [S_BADER]}],
      source_ids=[S_BADER])

    # =========================================================================
    # AFRICA
    # =========================================================================
    afr = "africa.prehistory"
    ERA("prehistory", "African Prehistory", "africa", ma(3.3), -3000, "foundational",
        dating_method="argon-argon", standing="consensus",
        summary="The continent where the human story begins, and where it stays for most "
                "of its length.",
        date_note="Africa holds the whole span. The hominin species themselves sit under "
                  "Human Prehistory rather than here, because a species is not a region's "
                  "property; this branch holds African sites and cultures.")

    P("olduvai-gorge", "Olduvai Gorge", afr, ma(2.038), ka(800), "foundational",
      summary="A Tanzanian ravine cutting through two million years of deposits, the site "
              "that made early human archaeology a dated science.",
      start_year_min=ma(2.043), start_year_max=ma(2.033),
      dating_method="argon-argon", standing="consensus",
      date_note="Bed I begins immediately above the Naabi Ignimbrite at 2.038 +/- 0.005 Ma. "
                "The sequence runs up through Beds II to IV. Among the best-constrained "
                "chronologies in African prehistory, with errors of a few thousand years.",
      source_ids=[S_DEINO])

    P("omo-kibish", "Omo Kibish", afr, ka(233), None, "intermediate",
      end_precision="unknown",
      summary="The Ethiopian site of Omo I, for decades the oldest known fossil of our own "
              "species.",
      start_year_min=ka(255), start_year_max=ka(211),
      dating_method="argon-argon", standing="consensus",
      date_note="Omo I is older than 233 +/- 22 ka, dated by single-crystal Ar/Ar on "
                "sanidine from the overlying KHS Tuff. A minimum: no robust maximum age "
                "exists. The date changed in 2022 because the anchoring tephra was "
                "reidentified, not because the method improved.",
      source_ids=[S_VIDAL])

    P("blombos-cave", "Blombos Cave", afr, ka(98.9), ka(67.8), "foundational",
      summary="A South African cave holding engraved ochre, shell beads and the oldest "
              "known drawing.",
      start_year_min=ka(103.4), start_year_max=ka(94.4),
      dating_method="luminescence", standing="consensus",
      date_note="Occupation from 98.9 +/- 4.5 ka to a sterile hiatus sand at 67.8 +/- 4.2 ka, "
                "on single-grain OSL. TL on burnt lithics agrees within error.",
      source_ids=[S_JACOBS_B, S_BADER])

    P("klasies-river", "Klasies River Mouth", afr, ka(110), ka(50), "intermediate",
      summary="A South African cave sequence with some of the earliest anatomically modern "
              "human remains outside East Africa.",
      dating_method="uranium-series", standing="consensus",
      date_note="Base dated by uranium-disequilibrium to about 110 ka, the LBS member "
                "corresponding to the Last Interglacial. The top of the MSA sequence is "
                "beyond the radiocarbon limit, so 50 ka is a floor rather than an end.",
      caveats=[{"kind": "contested-existence",
                "text": "The chronology is broadly accepted; what is argued is whether the "
                        "fragmentary human remains are fully modern.",
                "source_ids": [S_KLASIES]}],
      source_ids=[S_KLASIES, S_BADER])

    P("border-cave", "Border Cave", afr, ka(200), None, "intermediate",
      allow_outside_parent_dates=True,
      end_precision="unknown",
      summary="A South African site whose sequence runs from the Middle Stone Age into "
              "the present, including the earliest Later Stone Age toolkit.",
      dating_method="esr", standing="majority",
      date_note="The 200 ka start rests on ESR. The Early Later Stone Age horizon is "
                "44.2-43.0 ka cal BP by AMS radiocarbon. Occupation continues into the "
                "Holocene, so the end here is a convention.",
      alternatives=[{
          "label": "Conventional Later Stone Age onset",
          "standing": "majority",
          "start_year": ka(22),
          "dating_method": "radiocarbon-calibrated",
          "note": "Villa and Beaumont put the LSA onset here at 44-42 ka cal BP, roughly "
                  "20,000 years earlier than the conventional figure elsewhere.",
          "source_ids": ["villa-2012-border-cave"]}],
      source_ids=[S_BACKWELL, "villa-2012-border-cave"])

    P("green-sahara", "Green Sahara", afr, ka(14.5), ka(5), "foundational",
      aliases=["African Humid Period"],
      summary="The window when the Sahara held lakes, rivers and grassland, and people "
              "lived across what is now the largest hot desert on Earth.",
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="Onset about 14.5 ka with the Bolling-Allerod warming. Termination is "
                "time-transgressive rather than a single event: the northern and eastern "
                "Sahara dried after 8-7 ka while other areas stayed wet.",
      alternatives=[{
          "label": "Abrupt termination",
          "standing": "minority",
          "start_year": ka(5.5),
          "dating_method": "radiocarbon-calibrated",
          "note": "deMenocal's marine-core reading has the end as an abrupt step; "
                  "reanalyses argue for a gradual, regionally staggered dry-down.",
          "source_ids": [S_MCGEE]}],
      source_ids=[S_MCGEE])

    P("nabta-playa", "Nabta Playa", afr, ka(10.8), ka(6.2), "intermediate",
      summary="A seasonal lake basin in the Egyptian Sahara with cattle burials and a "
              "megalithic circle, occupied while the desert was green.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="Early Neolithic from 10,800 cal BP; abandoned to hyperaridity at about "
                "6,200 cal BP as the Green Sahara ended.",
      caveats=[{"kind": "contested-existence",
                "text": "The cultural chronology is reasonably settled. The claim that the "
                        "megaliths are astronomically aligned is not.",
                "source_ids": [S_MALVILLE]}],
      source_ids=[S_WENDORF, S_MALVILLE])

    # =========================================================================
    # WEST ASIA
    # =========================================================================
    wa = "west-asia.prehistory"
    ERA("prehistory", "West Asian Prehistory", "west-asia", -13000, -3800, "foundational",
        dating_method="radiocarbon-calibrated", standing="consensus",
        summary="Where farming, villages and monumental building appear first, and hand off "
                "to Sumer.",
        date_note="From the Natufian to the end of the Ubaid. Much of the older literature "
                  "quotes uncalibrated radiocarbon without saying so, which makes published "
                  "dates for this region roughly a millennium too young when read as "
                  "calendar years.")

    P("natufian", "Natufian Culture", wa, -13000, -10000, "foundational",
      summary="Hunter-gatherers of the Levant who settled in one place, built stone houses "
              "and buried their dead with ornaments, before anyone farmed.",
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="Early Natufian 13,000-11,500 cal BC, Late Natufian to about 10,000 cal BC.",
      caveats=[{"kind": "misconception",
                "text": "Often said the Younger Dryas cold snap forced the Natufians into "
                        "farming. Rejected: no moisture decline, no biome retreat, and the "
                        "Early-to-Late shift predates it.",
                "source_ids": [S_OX_NAT]}],
      source_ids=[S_OX_NAT, S_PPND])

    P("ppna", "Pre-Pottery Neolithic A", wa, -9800, -8800, "foundational",
      aliases=["PPNA"],
      summary="The first farming villages, before pottery: round houses, stored grain and "
              "communal building.",
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="9800/9700 to 8800/8700 cal BC in the PPND scheme, from about 800 compiled "
                "radiocarbon dates.",
      source_ids=[S_PPND])

    P("ppnb", "Pre-Pottery Neolithic B", wa, -8600, -6900, "foundational",
      aliases=["PPNB"],
      summary="Rectangular houses, plastered skulls and the first fully domesticated herds "
              "of sheep and goats.",
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="8600 to about 6900 cal BC, the end marked with a question mark in the "
                "source. The PPNA/PPNB boundary is a typological convention, and it may be "
                "a dating artefact: three of PPND's internal breaks fall on steep slopes "
                "and plateaus in the calibration curve rather than on changes in settlement.",
      source_ids=[S_PPND])

    P("catalhoyuk", "\u00c7atalh\u00f6y\u00fck", wa, -7100, -5865, "foundational",
      native="\u00c7atalh\u00f6y\u00fck",
      summary="A densely packed Anatolian town of mud-brick houses entered through the "
              "roof, with wall paintings and burials beneath the floors.",
      end_year_min=-5975, end_year_max=-5865,
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="East Mound from about 7100 cal BC; occupation ceases 5975-5865 cal BC at "
                "95% probability, from 33 AMS determinations on short-life samples. "
                "Mellaart's original 1960s estimate of c. 7100 BC held up against Bayesian "
                "modelling.",
      source_ids=[S_ORTON])

    P("halaf", "Halaf Culture", wa, -6100, -5300, "intermediate",
      summary="Northern Mesopotamian villages known for finely painted polychrome pottery "
              "traded over long distances.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="Proto-Halaf from 6100 cal BC, Early Halaf proper from 5950, Late Halaf "
                "ending 5300 cal BC, followed by a Halaf-Ubaid transition.",
      alternatives=[{
          "label": "Later Halaf end",
          "standing": "minority",
          "start_year": -6100, "end_year": -5100,
          "dating_method": "radiocarbon-calibrated",
          "note": "Roughly two centuries later than the conventional 5300 cal BC end.",
          "source_ids": [S_UBAID]}],
      source_ids=[S_HALAF, S_UBAID])

    P("ubaid", "Ubaid Period", wa, -6500, -3800, "foundational",
      summary="The long southern Mesopotamian prelude to cities: irrigation, temples on "
              "platforms, and the settlement pattern Sumer inherits.",
      dating_method="typological", standing="majority",
      date_note="Southern Mesopotamia about 6500-3800 BC counting Ubaid 0; the northern "
                "sequence is different, roughly 5300-4300 BC. Hands off to the Uruk period. "
                "Rests mainly on ceramic seriation rather than a dense radiocarbon series.",
      caveats=[{"kind": "misconception",
                "text": "No single agreed phase table exists. The term means different "
                        "things north and south, and published schemes disagree by 300-900 "
                        "years per boundary.",
                "source_ids": [S_UBAID]}],
      source_ids=[S_UBAID])

    # --- the two uncalibrated entities ---
    P("jericho-neolithic", "Neolithic Jericho", wa, -8300, -7300, "foundational",
      aliases=["Tell es-Sultan"],
      native="\u0623\u0631\u064a\u062d\u0627",
      summary="The oldest known town wall and stone tower, built by people who farmed but "
              "had not yet made pottery.",
      dating_method="radiocarbon-uncalibrated", standing="majority",
      date_note="STORED AS UNCALIBRATED RADIOCARBON. The familiar 'tower built c. 8300 BC' "
                "is an uncalibrated figure that the source never labels as such. Compared "
                "against calibrated estimates for the same stages it runs 500-900 years "
                "too young, so the tower is roughly a millennium older in calendar terms "
                "than the usual number suggests. The stage dates are also internally "
                "inconsistent: Stage V is older than Stage III despite being later.",
      caveats=[{"kind": "contested-existence",
                "text": "Kenyon read the wall and tower as defensive. Bar-Yosef argues they "
                        "were flood protection and a ritual structure, which would make "
                        "this not a fortification at all.",
                "source_ids": [S_BARYOSEF]}],
      source_ids=[S_BARYOSEF, S_PPND_JER])

    P("ain-ghazal", "'Ain Ghazal", wa, -8400, -6600, "intermediate",
      summary="A large Jordanian village of the pre-pottery Neolithic, known for lime "
              "plaster statues among the oldest large human figures ever made.",
      dating_method="radiocarbon-uncalibrated", standing="majority",
      date_note="STORED AS UNCALIBRATED RADIOCARBON for the statue horizon. Grissom gives "
                "6750 +/- 80 BC uncalibrated against 7580 +/- 110 BC calibrated for the same "
                "material \u2014 an 830-year gap, and both numbers circulate widely. Site "
                "dates are mixed; the two late aceramic phases cannot be separated "
                "radiometrically at all.",
      source_ids=[S_GRISSOM, S_PPND_AG])

    # =========================================================================
    # Europe and Central Asia
    # =========================================================================
    # The two prehistory buckets keep regional traditions discoverable without
    # pretending that populations, technologies, or exchange stopped at borders.
    eu = "europe.prehistory"
    ERA("prehistory", "European Prehistory", "europe", ka(455), -1500, "foundational",
        summary="The deep human past of Europe, from Neanderthals and cave art to farming, monuments, and metal-age cultures.",
        dating_method="uranium-series", standing="consensus",
        date_note="A navigation era. The early boundary follows the oldest securely dated "
                  "Neanderthal evidence at Sima de los Huesos, which is uranium-series and "
                  "luminescence work \u2014 radiocarbon reaches nowhere near it.",
        source_ids=[S_SIMA, S_HIGHAM])

    P("neanderthal-europe", "Neanderthal Europe", eu, ka(430), bp(39260), "foundational",
      summary="Neanderthals lived across Europe for hundreds of thousands of years before disappearing after a period of overlap with modern humans.",
      dating_method="uranium-series", standing="consensus",
      date_note="The 430 ka start is a minimum bound from Sima de los Huesos, dated by "
                "uranium-series and luminescence. The end is the 41,030-39,260 cal BP "
                "Mousterian boundary, which IS radiocarbon \u2014 the two ends of this range "
                "rest on different methods, and only one of them is datable by carbon.",
      alternatives=[{"label": "Older Sima chronology", "standing": "superseded",
                     "start_year": ka(600), "end_year": ka(400),
                     "dating_method": "uranium-series",
                     "note": "Earlier speleothem work placed the Sima hominins at roughly 400-600 ka; later work made them about 100,000 years younger.",
                     "source_ids": [S_SIMA]}],
      cross_parent_ids=["central-asia.prehistory"],
      source_ids=[S_SIMA, S_HIGHAM])

    P("chauvet", "Chauvet Cave Art", eu, ka(37), ka(27.9), "intermediate",
      summary="Artists made charcoal drawings in this French cave during two Upper Paleolithic visits.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The calibrated radiocarbon model places art and occupation in two phases between about 37 and 28 thousand years ago.",
      alternatives=[{"label": "Stylistic late chronology", "standing": "minority",
                     "start_year": ka(22), "end_year": ka(18), "dating_method": "typological",
                     "note": "Some scholars date the black drawings to the Solutrean or Gravettian from style, fauna, and stratigraphy rather than charcoal dates.",
                     "source_ids": [S_CHAUVET_ALT]}],
      caveats=[{"kind": "misconception",
                "text": "The debate is radiocarbon versus stylistic dating, not a claim that the cave paintings are fake or undated.",
                "source_ids": [S_CHAUVET, S_CHAUVET_ALT]}],
      source_ids=[S_CHAUVET, S_CHAUVET_ALT])

    P("lascaux", "Lascaux Cave Art", eu, ka(21.5), ka(21), "foundational",
      summary="This French cave's famous animal paintings were made during a short Upper Paleolithic occupation.",
      dating_method="radiocarbon-uncalibrated", standing="majority",
      date_note="STORED AS UNCALIBRATED RADIOCARBON because the official account mixes conventional BP measurements with calendar-like ranges without consistently labelling them. Do not convert this entry automatically.",
      alternatives=[{"label": "Earlier antler chronology", "standing": "superseded",
                     "start_year": bp(24000), "end_year": bp(23000),
                     "dating_method": "radiocarbon-uncalibrated",
                     "note": "Late-1990s AMS antler results supported a roughly 24,000-23,000 BP attribution before the newer LAsCO programme.",
                     "source_ids": [S_LASCAUX]}],
      source_ids=[S_LASCAUX])

    P("altamira", "Altamira Cave Art", eu, bp(35550), bp(15204), "foundational",
      summary="People added painted and engraved images to Altamira in northern Spain over a very long span.",
      dating_method="uranium-series", standing="majority",
      date_note="The oldest bound is a uranium-series minimum age on calcite over art; the younger black-painting boundary is calibrated radiocarbon.",
      alternatives=[{"label": "Downward U-series revision", "standing": "minority",
                     "start_year": bp(39000), "end_year": bp(35000), "dating_method": "uranium-series",
                     "note": "A methodological critique argues uranium loss or thorium correction could make the oldest Cantabrian calcite ages too old.",
                     "source_ids": [S_ALTAMIRA]}],
      source_ids=[S_ALTAMIRA])

    P("lbk", "Linear Pottery Culture (LBK)", eu, -5500, -4900, "intermediate",
      summary="Europe's first farmers built long timber houses and made band-decorated pottery across a wide central-European belt.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="Bayesian models put the formative start shortly before 5500 cal BC; the conventional 4900 BC ending remains a useful broad boundary rather than a fully modelled terminus.",
      source_ids=[S_LBK])

    P("megalithic", "Atlantic Megalithic Tradition", eu, -4794, -1500, "intermediate",
      summary="Communities built large stone tombs and monuments along Atlantic and Mediterranean coasts.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The first monuments are modelled in the late fifth millennium BC. Later Mediterranean revivals mean the tradition did not end as one clean event.",
      source_ids=[S_MEGALITH])

    P("stonehenge", "Stonehenge Construction", eu, -3000, -1520, "foundational",
      summary="Stonehenge was built and changed in several stages over roughly fifteen centuries.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="Bayesian modelling dates the first earthwork to 3000-2920 cal BC and the final recorded construction activity to about 1520 cal BC.",
      alternatives=[{"label": "Alternative stone-setting order", "standing": "minority",
                     "start_year": -2600, "end_year": -2000, "dating_method": "radiocarbon-calibrated",
                     "note": "Competing Bayesian models reorder parts of the sarsen and bluestone sequence within the same broad construction interval.",
                     "source_ids": [S_STONE]}],
      source_ids=[S_STONE])

    P("corded-ware", "Corded Ware Culture", eu, -2900, -2000, "intermediate",
      summary="A wide European culture known for cord-marked pots and single graves spread from the Rhine to the Baltic.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The broad span is regionally variable. Bohemian direct dates establish an early presence by 2900 BCE, while different regions end centuries apart.",
      alternatives=[{"label": "Swiss short chronology", "standing": "minority",
                     "start_year": -2750, "end_year": -2400, "dating_method": "calendar",
                     "note": "Swiss lake-settlement tree-ring dates restrict Corded Ware there to a shorter 2750-2400 BC span.",
                     "source_ids": [S_CORDED]}],
      source_ids=[S_CORDED])

    P("bell-beaker", "Bell Beaker Culture", eu, -2750, -1800, "intermediate",
      summary="Bell-shaped drinking vessels, new burial customs, and large population movements reshaped much of western Europe.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The conventional 2750-1800 BC span summarizes a regionally uneven archaeological and genetic transformation.",
      source_ids=[S_BEAKER])

    P("otzi", "Ötzi", eu, -3370, -3100, "intermediate",
      summary="The naturally preserved body of a man who died in the Alps gives a close view of Copper Age life.",
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="Radiocarbon places Ötzi's death in the late fourth millennium BC; this range records the published calibrated interval rather than treating a death as a long period.",
      source_ids=[S_OTZI])

    ca = "central-asia.prehistory"
    ERA("prehistory", "Central Asian Prehistory", "central-asia", ka(300), -1400, "foundational",
        summary="The deep history of Inner Asia, including early hominins, horse herding, and the Bronze Age steppe networks.",
        dating_method="luminescence", standing="consensus",
        date_note="This navigation era begins with the Denisova Cave sequence and ends after the latest Bronze Age tradition included here.",
        source_ids=[S_DENISOVA, S_YAMNAYA])

    P("denisova-cave", "Denisova Cave", ca, ka(300), ka(5.3), "foundational",
      summary="A Siberian cave with a long record of Neanderthals, Denisovans, and modern humans.",
      dating_method="luminescence", standing="consensus",
      date_note="The cave sequence combines luminescence, radiocarbon, uranium-series, and genetic evidence; the earliest occupation may reach about 300 ka.",
      source_ids=[S_DENISOVA])

    P("botai", "Botai Culture", ca, -3700, -3100, "intermediate",
      summary="A northern Kazakh settlement tradition famous for early intensive use of horses.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="Botai dates to the fourth millennium BC. Evidence for horse milking and management is strong, but its horses are not the ancestors of modern domestic horses.",
      caveats=[{"kind": "misconception",
                "text": "Botai horse use does not make Botai the direct source of modern domestic horses; ancient-DNA work overturned that popular claim in 2018.",
                "source_ids": [S_BOTAI]}],
      source_ids=[S_BOTAI])

    P("afanasievo", "Afanasievo Culture", ca, -3100, -2500, "intermediate",
      summary="An early pastoral culture of the Altai and Minusinsk Basin with strong ties to western steppe populations.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The culture's third-millennium BC range is based on a refined radiocarbon chronology for the Altai-Sayan region.",
      source_ids=[S_AFAN])

    P("andronovo", "Andronovo Culture", ca, -1900, -1400, "intermediate",
      summary="A Bronze Age network of steppe communities extending across Kazakhstan and southern Siberia.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The label covers related regional traditions whose exact limits vary; this stores the broad nineteenth-to-fifteenth-century BC frame.",
      source_ids=[S_ANDRON])

    P("bmac", "Bactria-Margiana Archaeological Complex", ca, -2200, -1700, "intermediate",
      summary="An oasis-based Bronze Age culture of Central Asia known for planned settlements, irrigation, and long-distance exchange.",
      dating_method="typological", standing="majority",
      date_note="The conventional 2200-1700 BC frame summarizes a complex whose individual oasis sequences do not all begin or end together.",
      source_ids=[S_BMAC])

    P("yamnaya", "Yamnaya Horizon", ca, -3300, -2350, "foundational",
      summary="Mobile pastoral communities of the Pontic-Caspian steppe whose movements had major effects across Europe and Asia.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The horizon is conventionally dated to about 3300-2350 BC; new genome-wide work refines its internal formation and spread.",
      cross_parent_ids=["europe.prehistory"],
      source_ids=[S_YAMNAYA])

    # =========================================================================
    # East, South, and Southeast Asia
    # =========================================================================
    # The national Jomon framework is useful for browsing, but its sub-phases
    # are children of the existing Jomon era because they are not China-wide eras.
    jomon = "east-asia.japan.jomon"
    P("incipient", "Incipient Jōmon", jomon, ka(16), ka(11), "intermediate",
      summary="The earliest Jōmon stage, marked by some of the world's oldest securely dated pottery.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The national framework gives 16,000-11,000 calibrated BP. Regional boundaries can differ substantially.",
      allow_outside_parent_dates=True,
      caveats=[{"kind": "misconception",
                "text": "The popular '13,000 BCE' beginning repeats raw uncalibrated radiocarbon as a calendar date; the secure pottery range is about 16,140-14,920 cal BP.",
                "source_ids": [S_JOMON, S_KEALLY]}],
      source_ids=[S_JOMON, S_KEALLY])
    P("initial", "Initial Jōmon", jomon, ka(11), ka(7), "intermediate",
      summary="A long early Jōmon stage when pottery traditions diversified across the Japanese islands.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The national framework gives 11,000-7,000 calibrated BP; local sequences are not synchronous.",
      source_ids=[S_JOMON])
    P("early", "Early Jōmon", jomon, ka(7), ka(5.3), "intermediate",
      summary="A Jōmon stage of growing regional diversity in settlements and pottery styles.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The national framework gives 7,000-5,300 calibrated BP, while regional pottery phases have different boundaries.",
      source_ids=[S_JOMON])
    P("middle", "Middle Jōmon", jomon, ka(5.3), ka(4.4), "intermediate",
      summary="A Jōmon stage known for large settlements and elaborate pottery in several regions.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The national framework gives 5,300-4,400 calibrated BP; large regional AMS programmes refine this differently by area.",
      source_ids=[S_JOMON])
    P("late", "Late Jōmon", jomon, ka(4.4), ka(3.3), "intermediate",
      summary="A later Jōmon stage before the regionally staggered transition to Yayoi farming communities.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The national framework gives 4,400-3,300 calibrated BP; the Jōmon-to-Yayoi transition occurred earlier in Kyushu than in northern Honshu.",
      source_ids=[S_JOMON])
    P("final", "Final Jōmon", jomon, ka(3.3), ka(2.3), "intermediate",
      summary="The final Jōmon stage, ending at different times in different parts of Japan.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The framework gives 3,300 to 2,500/2,300 calibrated BP, so the stored end uses the later 2,300 BP national bound.",
      source_ids=[S_JOMON])

    cn = "east-asia.china.neolithic"
    ERA("neolithic", "Chinese Neolithic", "east-asia.china", ka(12.5), -1700, "foundational",
        summary="The long transition in China from foraging to farming villages, regional cultures, towns, and large waterworks.",
        dating_method="radiocarbon-calibrated", standing="majority",
        date_note="This navigation era uses the widest dated process in this group, Yangtze rice domestication, as its early edge and the Longshan horizon as its late edge.",
        source_ids=[S_RICE, S_LONGSHAN])

    P("peiligang", "Peiligang Culture", cn, bp(9000), bp(7000), "intermediate",
      summary="An early farming culture of the central Henan plain, associated with millet cultivation and small villages.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The core source explicitly gives 9,000-7,000 calibrated years BP; a commonly repeated 5500-4900 BC type-site range does not state its calibration.",
      source_ids=[S_PEILIGANG])
    P("yangshao", "Yangshao Culture", cn, -5000, -3000, "foundational",
      summary="A major painted-pottery farming tradition of the middle Yellow River valley.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The conventional 5000-3000 BC framework is widely used, but Chinese bare-BP chronologies and regional Bayesian models produce a later start in some areas.",
      alternatives=[{"label": "Shangluo Bayesian chronology", "standing": "minority",
                     "start_year": -4200, "end_year": -2900, "dating_method": "radiocarbon-calibrated",
                     "note": "A regional Bayesian model places Yangshao at about 4200-2900 BC, later and shorter than the conventional span.",
                     "source_ids": [S_YANGSHAO]}],
      source_ids=[S_YANGSHAO])
    P("hongshan", "Hongshan Culture", cn, bp(6500), bp(4800), "intermediate",
      summary="A jade-working and temple-building culture of the West Liao River region in northeast China.",
      dating_method="radiocarbon-uncalibrated", standing="majority",
      date_note="STORED AS UNCALIBRATED RADIOCARBON / UNLABELLED BP. The available sources give only bare BP or 'years ago' dates, and Chinese practice commonly reports radiocarbon that way. Do not convert automatically.",
      alternatives=[{"label": "Classic Hongshan range", "standing": "superseded",
                     "start_year": bp(6000), "end_year": bp(5000), "dating_method": "radiocarbon-uncalibrated",
                     "note": "The older standard places Hongshan at 6,000-5,000 BP; 2025 Zhengjiagou work extends the end to 4,800 years ago.",
                     "source_ids": [S_HONGSHAN]}],
      source_ids=[S_HONGSHAN])
    P("longshan", "Longshan Culture", cn, -2600, -1900, "intermediate",
      summary="A late Neolithic tradition of black pottery, walled settlements, and regional change in the Yellow River basin.",
      dating_method="typological", standing="majority",
      date_note="The conventional 2600-1900 BC sequence is archaeological and broad; Bayesian analysis finds overlapping regional traditions rather than a single clean succession.",
      alternatives=[{"label": "Haidai Bayesian chronology", "standing": "minority",
                     "start_year": -2900, "end_year": -1700, "dating_method": "radiocarbon-calibrated",
                     "note": "Haidai modelling places the start boundary at 2900-2500 BC and the end at 2100-1700 BC, with cultural overlap.",
                     "source_ids": [S_LONGSHAN]}],
      source_ids=[S_LONGSHAN])
    P("liangzhu", "Liangzhu Culture", cn, bp(5300), bp(4300), "intermediate",
      summary="A Yangtze-delta society with a walled centre, jade traditions, and major dams and waterways.",
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="Direct dates on annual plants in dam construction give this culture a particularly strong calibrated chronology of 5,300-4,300 cal BP.",
      source_ids=[S_LIANGZHU])
    P("jiahu", "Jiahu", cn, bp(9000), bp(7800), "intermediate",
      summary="An early Henan village known for rice, bone flutes, and much-debated incised marks.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The calibrated site span is about 9,000-7,800 cal BP; a second source renders the occupation as 7000-5700 BC without stating its calibration.",
      source_ids=[S_JIAHU])

    sa = "south-asia.prehistory"
    ERA("prehistory", "South Asian Prehistory", "south-asia", bp(10899), -1500, "foundational",
        summary="Early farming, rice cultivation, and pre-urban settlement traditions across South Asia.",
        dating_method="radiocarbon-calibrated", standing="majority",
        date_note="The era begins with the Lahuradewa environmental sequence. Some attached sites continue later, so their genuine overlap is explicitly allowed.",
        source_ids=[S_LAHURADEWA])
    P("mehrgarh", "Mehrgarh", sa, -5250, -4650, "foundational",
      summary="A key early farming settlement in the Indus borderlands whose oldest phase has been radically re-dated.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="A 2025 programme directly dating tooth enamel places the aceramic cemetery at 5250-4650 cal BCE, about two thousand years younger than the familiar textbook start.",
      alternatives=[{"label": "Classic early Mehrgarh chronology", "standing": "traditional",
                     "start_year": -7000, "end_year": -4650, "dating_method": "radiocarbon-calibrated",
                     "note": "The older chronology begins the aceramic Neolithic around 7000 BCE and gives it a multi-millennial duration.",
                     "source_ids": [S_MEHRGARH]}],
      caveats=[{"kind": "misconception",
                "text": "The often repeated 7000 BCE start is not the current direct-dating result; the 2025 tooth-enamel model makes the earliest phase roughly 2,000 years younger.",
                "source_ids": [S_MEHRGARH]}],
      source_ids=[S_MEHRGARH])
    P("bhirrana", "Bhirrana", sa, -4000, -850, "intermediate",
      summary="A Haryana settlement with a disputed claim to extraordinarily early South Asian occupation.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The mainstream regional reading begins occupation in the fourth millennium BCE. The much older 9.5 ka sequence is an actively disputed extrapolation.",
      alternatives=[{"label": "Long Bhirrana chronology", "standing": "minority",
                     "start_year": bp(9500), "end_year": bp(2800), "dating_method": "radiocarbon-calibrated",
                     "note": "Sarkar and colleagues propose a Hakra phase from about 9.5 to 8 ka BP and occupation continuing to about 2.8 ka BP.",
                     "source_ids": [S_BHIRRANA]}],
      allow_outside_parent_dates=True,
      source_ids=[S_BHIRRANA_ASI, S_BHIRRANA])
    P("ravi", "Early Harappan Ravi Phase", sa, -3300, -2800, "intermediate",
      summary="The earliest well-dated phase at Harappa, before the later urban Indus city.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The published AMS table distinguishes raw BP measurements from its calibrated BC column and gives the phase a broad 3300-2800 BC frame.",
      source_ids=[S_RAVI])
    P("lahuradewa", "Lahuradewa", sa, bp(10899), None, "intermediate",
      summary="A lake-margin site in the middle Ganges plain with very early rice evidence and a long environmental sequence.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The environmental record begins about 10,899 cal BP and continues to the present. Archaeologists debate whether the earliest rice was domesticated or cultivated wild rice.",
      allow_outside_parent_dates=True,
      source_ids=[S_LAHURADEWA])

    sea = "southeast-asia.prehistory"
    ERA("prehistory", "Southeast Asian Prehistory", "southeast-asia", ka(46), -500, "foundational",
        summary="The long prehistory of mainland and island Southeast Asia, including cave traditions, metal-age communities, and early human remains.",
        dating_method="unknown", standing="majority",
        date_note="This navigation era includes both explicitly uncalibrated conventional Hoabinhian dates and later calibrated chronologies. It cannot be read as one homogeneous dating programme.",
        source_ids=[S_HOABINHIAN, S_BAN_CHIANG])
    P("hoabinhian", "Hoabinhian", sea, bp(23000), bp(3700), "intermediate",
      summary="A long-lived cave and rockshelter tool tradition of mainland Southeast Asia, often identified by worked pebble tools.",
      dating_method="radiocarbon-uncalibrated", standing="majority",
      date_note="STORED AS UNCALIBRATED RADIOCARBON. The conventional 23,000-3,700 BP chronology is explicitly published as non-calibrated; it must not be converted to calendar dates automatically.",
      alternatives=[{"label": "Xiaodong early chronology", "standing": "minority",
                     "start_year": ka(43.5), "end_year": -6000, "dating_method": "radiocarbon-calibrated",
                     "note": "A Yunnan rockshelter claim extends Hoabinhian to 43.5 ka and proposes a southern-China homeland.",
                     "source_ids": [S_HOABINHIAN_OLD]}],
      source_ids=[S_HOABINHIAN, S_HOABINHIAN_OLD])
    P("ban-chiang", "Ban Chiang", sea, -1600, -505, "intermediate",
      summary="A northeast Thai burial site central to the re-dating of Southeast Asian bronze metallurgy.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="Directly dating human bone collagen puts the first burial phase at 1600-1450 BC and the bronze transition at 1050-955 BC; later deposits reach the Iron Age.",
      alternatives=[{"label": "Old long chronology", "standing": "superseded",
                     "start_year": -3600, "end_year": -1600, "dating_method": "radiocarbon-uncalibrated",
                     "note": "The old model put the early Bronze Age at 3600 BC, based on charcoal and crushed-potsherd material now known to bias ages old.",
                     "source_ids": [S_BAN_CHIANG]}],
      caveats=[{"kind": "misconception",
                "text": "Ban Chiang did not show bronze metallurgy from 3600 BC: direct bone-collagen dating revised the key transition to 1050-955 BC.",
                "source_ids": [S_BAN_CHIANG]}],
      source_ids=[S_BAN_CHIANG])
    P("niah", "Niah Caves Deep Skull", sea, ka(46), ka(34), "intermediate",
      summary="A human skull from Borneo's Niah Caves, now accepted as Late Pleistocene rather than a later burial.",
      dating_method="uranium-series", standing="majority",
      date_note="Re-excavation and direct U-series work support a 46-34 ka bracket; a direct cranial U-series age near 35 ka may be an underestimate.",
      alternatives=[{"label": "Intrusive Neolithic burial", "standing": "superseded",
                     "start_year": -6000, "end_year": -2000, "dating_method": "typological",
                     "note": "Earlier critics argued that the skull had intruded from younger Neolithic deposits rather than belonging to the Pleistocene layer.",
                     "source_ids": [S_NIAH]}],
      source_ids=[S_NIAH])
    P("yangtze-rice", "Yangtze Rice Domestication", sea, bp(12500), bp(7000), "intermediate",
      summary="A gradual process in the lower Yangtze in which managed wild rice became fully domesticated rice.",
      dating_method="radiocarbon-uncalibrated", standing="majority",
      date_note="STORED AS UNCALIBRATED RADIOCARBON / CALIBRATION-UNSTATED BP. The main study prints bare BP values and Chinese practice often uses uncalibrated BP; do not convert automatically.",
      alternatives=[{"label": "Early cultivation reading", "standing": "majority",
                     "start_year": bp(9400), "end_year": bp(9000), "dating_method": "radiocarbon-uncalibrated",
                     "note": "A Chinese archaeology review places cultivation at Shangshan and Hehuashan around 9,400-9,000 BP and warns that such BP is usually uncalibrated.",
                     "source_ids": [S_RICE]}],
      source_ids=[S_RICE])

    # =========================================================================
    # Americas and Oceania
    # =========================================================================
    # The American umbrella is intentionally broader than a single tool style:
    # it holds migration hypotheses, periods, and sites whose chronologies overlap.
    am = "americas.prehistory"
    ERA("prehistory", "Americas Prehistory", "americas", ka(36), 500, "foundational",
        summary="The earliest peopling of the Americas and the long sequence of regional traditions that followed.",
        dating_method="radiocarbon-calibrated", standing="majority",
        date_note="This navigation era starts with the re-formed Bering land bridge and extends through regionally late Archaic traditions. Some sites continue beyond it and are marked accordingly.",
        source_ids=[S_BERINGIA, S_ARCHAIC])
    P("beringia", "Bering Land Bridge", am, ka(36), ka(11), "foundational",
      summary="The dry land connection that intermittently linked Siberia and Alaska during the last ice age.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="Sea-level work indicates the strait was open until about 35.7 ka and the last land bridge was flooded between about 13 and 11 ka.",
      source_ids=[S_BERINGIA])
    P("pre-clovis", "Pre-Clovis Horizon", am, ka(16), bp(13400), "foundational",
      summary="The broad label for accepted American sites older than the Clovis tool tradition.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="Most accepted evidence falls around 16,000-15,000 years ago. Claims before the last glacial maximum remain contested rather than forming one settled horizon.",
      alternatives=[{"label": "Pre-LGM long chronology", "standing": "minority",
                     "start_year": ka(24), "end_year": ka(17.5), "dating_method": "radiocarbon-calibrated",
                     "note": "Some claimed sites would push occupation before 20 ka, but the combined genetic and archaeological synthesis does not accept that depth.",
                     "source_ids": [S_PRE_CLOVIS]}],
      source_ids=[S_PRE_CLOVIS])
    P("white-sands", "White Sands Footprints", am, ka(23), ka(21), "foundational",
      summary="Human footprints in New Mexico that may date to the height of the last ice age.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The original aquatic-seed dates of about 23-21 ka were independently supported by terrestrial pollen radiocarbon and quartz OSL, but objections remain active.",
      alternatives=[{"label": "Hard-water reservoir objection", "standing": "minority",
                     "start_year": ka(16), "end_year": ka(13), "dating_method": "radiocarbon-calibrated",
                     "note": "Critics argue aquatic seeds could be 7,000-10,000 years too old because they used ancient dissolved carbon from lake water.",
                     "source_ids": [S_WHITE_CRITIQUE]}],
      caveats=[{"kind": "contested-existence",
                "text": "The dispute has three rounds: 2021 aquatic-seed dates, a 2022 reservoir objection, and 2023 pollen plus OSL confirmation that critics still question.",
                "source_ids": [S_WHITE_SANDS, S_WHITE_CRITIQUE, S_WHITE_REPLY]}],
      source_ids=[S_WHITE_SANDS, S_WHITE_REPLY, S_WHITE_CRITIQUE])
    P("clovis", "Clovis Culture", am, bp(13050), bp(12750), "foundational",
      summary="A short-lived North American tradition of distinctive fluted stone points.",
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="The modern calibrated range is about 13,050-12,750 cal BP. The underlying laboratory ages and older famous ranges are uncalibrated radiocarbon, not calendar dates.",
      alternatives=[{"label": "Traditional long Clovis", "standing": "superseded",
                     "start_year": bp(11500), "end_year": bp(10900), "dating_method": "radiocarbon-uncalibrated",
                     "note": "The former 11,500-10,900 radiocarbon-year BP span was compressed by Waters and Stafford's 2007 reassessment.",
                     "source_ids": [S_CLOVIS_2007]}],
      caveats=[{"kind": "misconception",
                "text": "Clovis was not a millennium-long 11,500-10,900 BCE culture: Waters and Stafford compressed the raw radiocarbon chronology, and calibration shifts it about two millennia older.",
                "source_ids": [S_CLOVIS, S_CLOVIS_2007]}],
      source_ids=[S_CLOVIS, S_CLOVIS_2007])
    P("folsom", "Folsom Culture", am, bp(12910), bp(12125), "intermediate",
      summary="A bison-hunting tradition that followed Clovis across much of the North American plains.",
      dating_method="radiocarbon-calibrated", standing="consensus",
      date_note="IntCal20 Bayesian modelling gives a 95% span from 12,910-12,750 to 12,430-12,125 cal BP.",
      source_ids=[S_FOLSOM])
    P("paleoindian", "Paleoindian Period", am, bp(13200), bp(11450), "intermediate",
      summary="A broad North American label for the earliest widespread post-ice-age traditions, including Clovis and Folsom.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The continental bracket is about 13,200-11,450 cal BP, although regional period labels and boundaries vary.",
      source_ids=[S_PALEOINDIAN])
    P("archaic", "Archaic Period", am, -8500, 500, "intermediate",
      summary="A long, regionally varied North American period of adapting to post-ice-age environments, broad diets, and later early farming.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="The period has no single continental end: one synthesis ends it about 3200 cal BP, while the Southwest carries it as late as AD 500.",
      source_ids=[S_ARCHAIC, S_PALEOINDIAN])
    P("cactus-hill", "Cactus Hill", am, ka(20), None, "specialist",
      end_precision="unknown",
      summary="A Virginia sand-dune site with a possible stone-tool layer below a Clovis level.",
      dating_method="radiocarbon-uncalibrated", standing="minority",
      date_note="STORED AS UNCALIBRATED RADIOCARBON / CALIBRATION-UNSTATED. Available sources report 18,000-20,000 years ago but do not identify a calibration basis; the site sequence continues to contact.",
      caveats=[{"kind": "contested-existence",
                "text": "The deepest Cactus Hill layer is not part of the settled pre-Clovis chronology; the state's defensible claim is only 'more than 15,000 years ago.'",
                "source_ids": [S_CACTUS]}],
      allow_outside_parent_dates=True,
      source_ids=[S_CACTUS])
    P("paisley-caves", "Paisley Caves", am, bp(14300), None, "intermediate",
      end_precision="unknown",
      summary="Oregon caves with early human coprolites, basketry, and a Western Stemmed stone-point tradition.",
      dating_method="radiocarbon-calibrated", standing="majority",
      date_note="Human evidence reaches about 14,300 cal BP, while the cave deposits continue through historic contact. Dates and human attribution have unusually extensive testing.",
      caveats=[{"kind": "contested-existence",
                "text": "The concern is whether soluble DNA and lipids moved into older layers; later fecal-lipid work supports the early human attribution.",
                "source_ids": [S_PAISLEY]}],
      allow_outside_parent_dates=True,
      source_ids=[S_PAISLEY])

    # These records sit with Aboriginal Australia because they document its deep
    # continuity, while Lapita and Polynesian entries retain their own Oceania homes.
    au = "oceania.australia.aboriginal"
    P("sahul", "Sahul", au, ka(75), ka(12), "intermediate",
      summary="The ice-age landmass that joined Australia, Tasmania, and New Guinea when sea levels were lower.",
      dating_method="luminescence", standing="majority",
      date_note="Human entry is modelled between about 65 and 50 ka, with a 75 ka model option. Postglacial sea rise broke the landmass apart; Bass Strait flooded about 12 ka.",
      alternatives=[{"label": "Genetic short chronology", "standing": "minority",
                     "start_year": ka(47), "end_year": ka(12), "dating_method": "unknown",
                     "note": "A genetic and archaeological short chronology places Australian arrival near 47 ka rather than the archaeological long chronology.",
                     "source_ids": [S_SAHUL]}],
      allow_outside_parent_dates=True,
      source_ids=[S_SAHUL])
    P("madjedbebe", "Madjedbebe", au, ka(65), None, "foundational",
      summary="A rock shelter on Mirarr Country in Arnhem Land with very early stone tools and other evidence of occupation.",
      dating_method="luminescence", standing="majority",
      date_note="Single-grain OSL dates the lowest artefact-bearing deposit to 65 ± 6 ka. This is a light-based age, not radiocarbon, and the locality remains culturally meaningful.",
      caveats=[{"kind": "contested-existence",
                "text": "The challenge is not the OSL measurement itself but whether termites and other disturbance moved artefacts down into older sands.",
                "source_ids": [S_MADJ]}],
      source_ids=[S_MADJ])
    P("lake-mungo", "Lake Mungo", au, ka(50), ka(40), "foundational",
      summary="The Willandra Lakes locality of Mungo Lady and Mungo Man, two of Australia's oldest known human burials.",
      dating_method="luminescence", standing="consensus",
      date_note="Current consensus dates the burials to 40 ± 2 ka and local occupation to 50-46 ka from 25 optical ages. These are not radiocarbon dates.",
      alternatives=[{"label": "Thorne 1999 age", "standing": "superseded",
                     "start_year": ka(62), "end_year": ka(56), "dating_method": "uranium-series",
                     "note": "A 1999 U-series/ESR and OSL study claimed 62 ± 6 ka for Mungo Man; it was superseded by the 2003 optical chronology.",
                     "source_ids": [S_MUNGO]}],
      caveats=[{"kind": "misconception",
                "text": "The popular 62 ka age for Mungo Man is superseded; the current 40 ± 2 ka result comes from later OSL dating of the lunette sediments.",
                "source_ids": [S_MUNGO]}],
      source_ids=[S_MUNGO])
