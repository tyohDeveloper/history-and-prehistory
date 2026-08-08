"""The Neolithic transition: centres of origin and the firsts that surround it.

Aimed by `tools/coverage.py`, which found "Agricultural Revolution" spanning
5,500 years with zero children — the most consequential transition in the app's
scope stored as one undifferentiated block, and filed as an `event`.

Three things happen here.

**The node is reframed.** The research is unambiguous that the field has moved
off Childe's "Neolithic Revolution" to a protracted, geographically autonomous,
largely unconscious process lasting on the order of 4,000 years. Calling that an
`event` was wrong twice over — wrong kind, wrong claim. It becomes an era named
"Neolithic Transition", keeping the old names as aliases because that is what
readers arrive holding. The minority position (Abbo and Gopher, who argue for a
rapid conscious core-area process) is carried rather than erased: the dispute is
live, with a published exchange as recent as 2022.

**It gets its centres.** Seven independent centres of domestication, each with
its own sourced onset. How many centres exist is itself unsettled — Harlan
counted 6, Vavilov 12, Purugganan and Fuller 24 — so the count is recorded as a
question rather than asserted.

**The firsts layer is extended past African cereals.** It previously stopped
there, so pottery, cloth, the dog, the wheel and writing had no entry anywhere.
The most useful of these actively contradict the tidy story: pottery predates
farming by ten millennia, fermented drink and the dog are both Palaeolithic, and
the horse's modern lineage is not the one people cite.

Dates that could not be defended are absent, not guessed. The plough, the
Bactrian camel and Yuchanyan pottery were all flagged `n.a.` in research and
none of them appears here.
"""

from builders import make_builders
from extensions_prehistory import bp

S_WU_POTTERY = "wu-2012-xianrendong-pottery"
S_KVAVADZE = "kvavadze-2009-dzudzuana-flax"
S_CATAL_TEXTILE = "catalhoyuk-2021-earliest-textiles"
S_FOUNDER_CROPS = "sw-asian-founder-crops-table"
S_FULLER_PROTRACTED = "fuller-2020-protracted-domestication"
S_ABBO_GOPHER = "abbo-gopher-core-area-critique"
S_FULLER_REPLY = "fuller-2022-reply-to-abbo"
S_NEOLITHIC_TERM = "persistent-controversies-neolithic"
S_RICE_2024 = "science-2024-rice-trajectory"
S_RICE_SHANGSHAN = "antiquity-earliest-rice-domestication"
S_MILLET_PNAS = "pnas-2012-early-millet"
S_MILLET_DISPUTE = "miller-2016-millet-phytolith-dispute"
S_BALSAS_MAIZE = "pnas-2009-balsas-maize"
S_GUILA_MAIZE = "guila-naquitz-ams-maize"
S_POTATO_JISKA = "pnas-2016-jiskairumoko-potato"
S_CAMELIDS = "elife-2021-south-american-camelids"
S_KUK = "denham-2003-kuk-swamp"
S_ENA_SMITH = "smith-eastern-north-america"
S_AMAZONIA = "plos-teotonio-amazonia"
S_DOG_2026 = "nature-2026-palaeolithic-dogs"
S_HORSE_2021 = "nature-2021-horse-origin"
S_HORSE_BOTAI = "science-2018-botai-horses"
S_CHICKEN_2022 = "chicken-2022-southeast-asia"
S_RAQEFET = "liu-2018-raqefet-fermentation"
S_CHOGA_MAMI = "isac-choga-mami-irrigation"
S_WHEEL = "antiquity-earliest-wheeled-vehicles"
S_WRITING_NEA = "oup-origins-of-writing"
S_CENTRES_COUNT = "springer-domestication-centres-review"

NEOLITHIC_SOURCES = [
    {"id": S_WU_POTTERY, "kind": "scholarly",
     "citation": "Wu et al. (2012), 'Early Pottery at 20,000 Years Ago in Xianrendong Cave, China', Science",
     "url": "https://pubmed.ncbi.nlm.nih.gov/22745428/",
     "note": "20,000-19,000 cal BP; pottery predates agriculture in the region by over ten millennia."},
    {"id": S_KVAVADZE, "kind": "scholarly",
     "citation": "Kvavadze, Bar-Yosef et al. (2009), '30,000-Year-Old Wild Flax Fibers', Science",
     "url": "https://ghss.ug.edu.ge/storage/themes/June2025/3ev9ncSLyickvEe40dMm.pdf",
     "note": "Dzudzuana Cave, Georgia. Spun and dyed flax; cordage rather than woven cloth."},
    {"id": S_CATAL_TEXTILE, "kind": "scholarly",
     "citation": "'Multidisciplinary investigation reveals the earliest textiles' (2021), Scientific Reports",
     "url": "https://www.nature.com/articles/s41598-021-01349-5",
     "note": "Catalhoyuk woven cloth, c. 6700-6500 cal BC."},
    {"id": S_FOUNDER_CROPS, "kind": "scholarly",
     "citation": "'Neolithic Foundations for the Evolution of Plant Phenotypic Diversity: Wheat and Barley Domestication', Current Anthropology",
     "url": "https://www.journals.uchicago.edu/doi/abs/10.1086/658367",
     "note": "Einkorn and emmer at Cayonu and Cafer Hoyuk c. 10,600-9,900 cal BP."},
    {"id": S_FULLER_PROTRACTED, "kind": "scholarly",
     "citation": "'Plant domestication in the Neolithic Near East' (2020), Quaternary Science Reviews",
     "url": "https://www.sciencedirect.com/science/article/abs/pii/S0277379120303747",
     "note": "The protracted-autonomous model: millennia-long, multi-focus, largely unconscious."},
    {"id": S_ABBO_GOPHER, "kind": "scholarly",
     "citation": "Abbo, Gopher et al., critical review of the protracted domestication model, Journal of Experimental Botany",
     "url": "https://academic.oup.com/jxb/article/63/12/4333/643435",
     "note": "Minority: argues for a rapid, conscious, core-area domestication."},
    {"id": S_FULLER_REPLY, "kind": "scholarly",
     "citation": "Fuller et al., 'Progress in domestication research: a reply to Abbo and Gopher' (2022)",
     "url": "https://discovery.ucl.ac.uk/id/eprint/10158703/1/Fuller_Reply%20to%20Abbo_v3.3.pdf",
     "note": "Frames the disagreement as active and unresolved."},
    {"id": S_NEOLITHIC_TERM, "kind": "scholarly",
     "citation": "'Persistent Controversies about the Neolithic Revolution'",
     "url": "http://www.bicga.org.uk/docs/Persistent_Controversies_about_the_Neolithic.pdf",
     "note": "Records the terminology shift from Childe's 'revolution' to 'Neolithic transition'."},
    {"id": S_RICE_2024, "kind": "scholarly",
     "citation": "'Rice's trajectory from wild to domesticated: an archaeobotanical perspective' (2024), Science",
     "url": "https://www.science.org/doi/abs/10.1126/science.ade4487",
     "note": "Exploitation from c. 24,000 BP, cultivation c. 13,000 BP, domestication c. 11,000 BP."},
    {"id": S_RICE_SHANGSHAN, "kind": "scholarly",
     "citation": "'The earliest rice domestication in China', Antiquity Project Gallery",
     "url": "https://www.cambridge.org/core/journals/antiquity-project-gallery/article/earliest-rice-domestication-in-china/0F8D71ECFBAE8E8A6201B558500A84AB"},
    {"id": S_MILLET_PNAS, "kind": "scholarly",
     "citation": "'Early millet use in northern China' (2012), PNAS",
     "url": "https://www.pnas.org/doi/10.1073/pnas.1115430109"},
    {"id": S_MILLET_DISPUTE, "kind": "scholarly",
     "citation": "Miller et al. (2016), The Holocene, on the millet phytolith-versus-macrobotanical discrepancy",
     "url": "https://www.sas.upenn.edu/~nmiller0/papers/Miller%20&%20al.%202016%20millet.pdf",
     "note": "Phytolith and seed dates for the same sites disagree by millennia."},
    {"id": S_BALSAS_MAIZE, "kind": "scholarly",
     "citation": "'Starch grain and phytolith evidence for early ninth millennium B.P. maize from the Central Balsas River Valley' (2009), PNAS",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2664021/"},
    {"id": S_GUILA_MAIZE, "kind": "scholarly",
     "citation": "'Documenting domestication: the intersection of genetics and archaeology' (Guila Naquitz AMS maize dates)",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC33375/",
     "note": "Direct AMS cob dates 6,250-6,230 cal BP, c. 2,400 years later than the starch evidence."},
    {"id": S_POTATO_JISKA, "kind": "scholarly",
     "citation": "PNAS (2016), starch-grain evidence for potato processing at Jiskairumoko, Peru",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5137686/",
     "note": "3,400-2,200 cal BC; earlier popular claims are not directly supported."},
    {"id": S_CAMELIDS, "kind": "scholarly",
     "citation": "'Ancient DNA reveals the lost domestication history of South American camelids' (2021), eLife",
     "url": "https://elifesciences.org/articles/63390"},
    {"id": S_KUK, "kind": "scholarly",
     "citation": "Denham et al. (2003), 'Origins of Agriculture at Kuk Swamp in the Highlands of New Guinea', Science",
     "url": "https://faculty.washington.edu/plape/pacificarchaut12/Denham%20et%20al%202003.pdf",
     "note": "Phase 1 10,220-9,910 cal BP; Phase 3 ditched cultivation 4,350-3,980 cal BP."},
    {"id": S_ENA_SMITH, "kind": "scholarly",
     "citation": "Smith (2006), 'Eastern North America as an independent center of plant domestication', PNAS",
     "url": "https://pubmed.ncbi.nlm.nih.gov/16894156/",
     "note": "Squash 5,025 cal BP, sunflower 4,840 cal BP, marsh elder 4,400 BP, chenopod 3,800 BP."},
    {"id": S_AMAZONIA, "kind": "scholarly",
     "citation": "'Ten thousand years of crop cultivation in southwestern Amazonia', PLOS ONE (Teotonio site)",
     "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0199868",
     "note": "Manioc c. 10,350 BP, squash c. 10,250 BP, maize c. 6,850 BP."},
    {"id": S_DOG_2026, "kind": "scholarly",
     "citation": "'Dogs were widely distributed across western Eurasia during the Palaeolithic' (2026), Nature",
     "url": "https://www.nature.com/articles/s41586-026-10170-x",
     "note": "Oldest confirmed genetic evidence, 15,800-14,200 years ago."},
    {"id": S_HORSE_2021, "kind": "scholarly",
     "citation": "'The origins and spread of domestic horses from the Western Eurasian steppes' (2021), Nature",
     "url": "https://www.nature.com/articles/s41586-021-04018-9.pdf",
     "note": "DOM2 lineage from the lower Volga-Don c. 2200 BCE, not Botai."},
    {"id": S_HORSE_BOTAI, "kind": "scholarly",
     "citation": "'Ancient genomes revisit the ancestry of domestic and Przewalski's horses' (2018), Science",
     "url": "https://www.science.org/doi/10.1126/science.aao3297",
     "note": "Botai husbandry remains the earliest known, but is a dead end for modern breeds."},
    {"id": S_CHICKEN_2022, "kind": "scholarly",
     "citation": "'The biocultural origins and dispersal of domestic chickens' (2022), PNAS",
     "url": "https://pubmed.ncbi.nlm.nih.gov/35666876/",
     "note": "Ban Non Wat, Thailand, 1650-1250 BCE; overturns an Indian origin."},
    {"id": S_RAQEFET, "kind": "scholarly",
     "citation": "Liu et al. (2018), 'Fermented beverage and food storage in 13,000 y-old stone mortars at Raqefet Cave'",
     "url": "https://www.sciencedirect.com/science/article/abs/pii/S2352409X18303468",
     "note": "Natufian, and so pre-agricultural."},
    {"id": S_CHOGA_MAMI, "kind": "scholarly",
     "citation": "ISAC, University of Chicago, 'Excavations at Choga Mami, Iraq'",
     "url": "https://isac.uchicago.edu/sites/default/files/uploads/shared/docs/ar/61-70/67-68a/67-68a_Choga_Mami.pdf",
     "note": "Canal irrigation c. 6200-5700 BC, Samarra culture."},
    {"id": S_WHEEL, "kind": "scholarly",
     "citation": "'Earliest evidence of wheeled vehicles in Europe and the Near East', Antiquity",
     "url": "https://www.cambridge.org/core/journals/antiquity/article/abs/earliest-evidence-of-wheeled-vehicles-in-europe-and-the-near-east/4835B594180234DC116F6F0105771573",
     "note": "Uruk pictographs and the Bronocice pot are near-simultaneous, c. 3500-3350 BCE."},
    {"id": S_WRITING_NEA, "kind": "scholarly",
     "citation": "'The Origins of Writing in Northeastern Africa', Oxford Handbook chapter",
     "url": "https://academic.oup.com/edited-volume/61663/chapter/553461749?searchresult=1",
     "note": "Mesopotamian and Egyptian date ranges overlap; the two systems are independent."},
    {"id": S_CENTRES_COUNT, "kind": "scholarly",
     "citation": "Review of independent domestication centres, Genetic Resources and Crop Evolution",
     "url": "https://link.springer.com/article/10.1007/s10722-021-01114-7",
     "note": "Harlan counted 6 centres, Vavilov 12, Purugganan and Fuller 24."},
]

CHECKED = "2026-08-08"


def extend(E, entities):
    _, P, _, _, _, FIRST = make_builders(E)
    by_id = {e["id"]: e for e in entities}
    firsts = "global.prehistory.firsts"

    # ---- Reframe the node itself -------------------------------------------
    #
    # It was an `event` spanning 5,500 years. An event is "a discrete moment";
    # the current model is a 4,000-year unconscious process. Both the kind and
    # the name asserted something the literature has abandoned. The id is left
    # alone so nothing addressing it breaks.
    node = by_id.get("global.neolithic.agricultural-revolution")
    if node is not None:
        node["kind"] = "era"
        node["name"] = "Neolithic Transition"
        node["aliases"] = ["Neolithic Revolution", "Agricultural Revolution",
                           "First Agricultural Revolution"]
        # Extends past the Neolithic label because Eastern North America
        # domesticates far later than the Fertile Crescent. Diachronous, like
        # the end of prehistory itself.
        node["end_year"] = -1800
        node["allow_outside_parent_dates"] = True
        node["standing"] = "majority"
        node["as_of"] = CHECKED
        node["summary"] = ("Independent, and largely unconscious, transitions to farming "
                           "in at least seven regions. A process of millennia, not an event.")
        node["date_note"] = (
            "NOT A REVOLUTION, despite the name it is still filed under. The dominant model "
            "is protracted and geographically autonomous: domestication took on the order of "
            "4,000 years, happened independently at several foci, and was largely unconscious "
            "rather than invented. The field has largely replaced Childe's 'Neolithic "
            "Revolution' with 'Neolithic transition' for that reason. The end date is "
            "diachronous and runs past the Neolithic label itself, because Eastern North "
            "America domesticates thousands of years after the Fertile Crescent."
        )
        node["alternatives"] = [{
            "label": "Rapid, conscious, core-area domestication",
            "standing": "minority",
            "note": "Abbo and Gopher argue for a fast deliberate process in one core area.",
            "source_ids": [S_ABBO_GOPHER],
        }]
        node["caveats"] = [
            {"kind": "misconception",
             "text": "Not a revolution and not an event: the transition took millennia, and "
                     "foraging and farming coexisted throughout much of it.",
             "source_ids": [S_NEOLITHIC_TERM, S_FULLER_PROTRACTED]},
            {"kind": "contested-existence",
             "text": "How many independent centres exist is unsettled: Harlan counted 6, "
                     "Vavilov 12, Purugganan and Fuller 24.",
             "source_ids": [S_CENTRES_COUNT]},
        ]
        node["source_ids"] = [S_FULLER_PROTRACTED, S_FULLER_REPLY, S_NEOLITHIC_TERM,
                              S_CENTRES_COUNT]

    ag = "global.neolithic.agricultural-revolution"

    # ---- The centres -------------------------------------------------------
    P("fertile-crescent", "Fertile Crescent", ag, bp(10600), bp(6600), "foundational",
      summary="Wheat, barley, lentil, pea, sheep, goat, pig and cattle — the package that "
              "reached Europe, North Africa and South Asia.",
      start_dating_method="radiocarbon-calibrated", end_dating_method="radiocarbon-calibrated",
      standing="majority",
      date_note="Earliest definite domesticated einkorn and emmer at Cayonu and Cafer Hoyuk, "
                "10,600-9,900 cal BP. The end shown applies the protracted model's ~4,000-year "
                "duration to that onset; it is a modelled span, not a dated horizon.",
      source_ids=[S_FOUNDER_CROPS, S_FULLER_PROTRACTED])

    P("yangtze", "Yangtze Valley", ag, bp(10000), bp(4300), "foundational",
      summary="Rice, domesticated over roughly six millennia from Shangshan to Liangzhu.",
      start_dating_method="radiocarbon-calibrated", end_dating_method="radiocarbon-calibrated",
      standing="majority",
      date_note="Shangshan at c. 10,000 cal BP holds the earliest cultivation, with both wild "
                "and domesticated-type rachis present, running to Liangzhu at 4,300 BP.",
      alternatives=[{
          "label": "Earlier trajectory (2024)", "standing": "minority",
          "start_year": bp(24000), "dating_method": "radiocarbon-calibrated",
          "note": "Exploitation from c. 24,000 BP, cultivation 13,000 BP, domestication 11,000 BP.",
          "source_ids": [S_RICE_2024]}],
      source_ids=[S_RICE_SHANGSHAN, S_RICE_2024])

    P("yellow-river", "Yellow River Basin", ag, bp(10300), bp(7500), "intermediate",
      summary="Broomcorn and foxtail millet, the dryland counterpart to the Yangtze's rice.",
      start_dating_method="radiocarbon-calibrated", end_dating_method="radiocarbon-calibrated",
      standing="minority",
      date_precision="disputed",
      as_of=CHECKED,
      date_note="METHODOLOGICALLY CONTESTED. Phytolith evidence at Cishan reaches 10,300-8,700 "
                "cal BP, but macrobotanical seed remains from the same sites are as late as "
                "c. 5,900 cal BC. The two methods disagree by millennia and neither has "
                "displaced the other.",
      alternatives=[{
          "label": "Macrobotanical dating only", "standing": "majority",
          "start_year": -5900, "dating_method": "radiocarbon-calibrated",
          "note": "Seed remains, rather than phytoliths, give a far later onset.",
          "source_ids": [S_MILLET_DISPUTE]}],
      source_ids=[S_MILLET_PNAS, S_MILLET_DISPUTE])

    P("mesoamerica", "Mesoamerica", ag, bp(10000), bp(6250), "foundational",
      summary="Squash first, then maize and beans — the squash predates maize by over four "
              "thousand years.",
      start_dating_method="radiocarbon-calibrated", end_dating_method="radiocarbon-calibrated",
      standing="majority",
      date_note="Cucurbita pepo cultivated at Guila Naquitz from 10,000-8,000 cal BP. Maize "
                "appears as starch and phytoliths in the Balsas Valley at c. 8,700 cal BP but "
                "is not directly AMS-dated on cobs until 6,250-6,230 cal BP. The two figures "
                "rest on different evidence and are kept apart rather than averaged.",
      source_ids=[S_BALSAS_MAIZE, S_GUILA_MAIZE])

    P("andes", "Andes", ag, bp(7000), -2200, "foundational",
      summary="Potato, llama, alpaca and guinea pig, domesticated in the high basin around "
              "Lake Titicaca.",
      start_dating_method="radiocarbon-calibrated", end_dating_method="radiocarbon-calibrated",
      standing="majority",
      date_note="Camelid domestication at Telarmachay and comparable sites from c. 7,000-6,000 "
                "BP. The earliest DIRECT evidence for potato is later, 3,400-2,200 cal BC at "
                "Jiskairumoko; broader claims of 8,000-5,000 BCE are not supported by directly "
                "dated material.",
      source_ids=[S_CAMELIDS, S_POTATO_JISKA])

    P("new-guinea", "New Guinea Highlands", ag, bp(10220), bp(3980), "intermediate",
      summary="Taro and banana, cultivated at Kuk Swamp entirely independently of Asia.",
      start_dating_method="radiocarbon-calibrated", end_dating_method="radiocarbon-calibrated",
      standing="consensus",
      date_note="Kuk Swamp phase 1, plant exploitation, 10,220-9,910 cal BP; phase 2 mounded "
                "cultivation of taro and banana 6,950-6,440 cal BP; phase 3 ditched "
                "cultivation 4,350-3,980 cal BP.",
      source_ids=[S_KUK])

    P("eastern-north-america", "Eastern North America", ag, bp(5025), bp(3800), "intermediate",
      summary="Squash, sunflower, marsh elder and chenopod — a fully independent centre, and "
              "one of the latest.",
      start_dating_method="radiocarbon-calibrated", end_dating_method="radiocarbon-calibrated",
      standing="consensus",
      date_note="Squash at Phillips Spring 5,025 cal BP, sunflower at the Hayes site 4,840 cal "
                "BP, marsh elder c. 4,400 BP, chenopod c. 3,800 BP. Roughly five thousand years "
                "after the Fertile Crescent, which is why this node runs past the Neolithic.",
      source_ids=[S_ENA_SMITH])

    P("southwest-amazonia", "Southwest Amazonia", ag, bp(10350), bp(6850), "specialist",
      summary="Manioc and squash cultivated on forest islands of the Llanos de Moxos, far "
              "earlier than Amazonian agriculture was thought to begin.",
      start_dating_method="radiocarbon-calibrated", end_dating_method="radiocarbon-calibrated",
      standing="majority",
      date_note="Phytolith evidence from the Teotonio site: manioc by c. 10,350 BP, squash by "
                "c. 10,250 BP, maize present by c. 6,850 BP.",
      source_ids=[S_AMAZONIA])

    # ---- Firsts, in chronological order ------------------------------------
    FIRST("spun-fibre", "Spun Fibre", firsts, bp(32000), tier="specialist",
          summary="Wild flax from Dzudzuana Cave, Georgia, twisted into cordage and dyed "
                  "turquoise, pink and black.",
          start_dating_method="radiocarbon-calibrated", standing="consensus",
          date_note="Oldest layer 32,000-26,000 BP. Cordage and possible basketry, not woven "
                    "cloth — those are separate thresholds tens of millennia apart.",
          source_ids=[S_KVAVADZE])

    FIRST("pottery", "Pottery", firsts, bp(20000), tier="foundational",
          summary="Ceramic vessels from Xianrendong Cave, Jiangxi — made by hunter-gatherers "
                  "ten thousand years before anyone in the region farmed.",
          start_dating_method="radiocarbon-calibrated", standing="consensus",
          date_note="20,000-19,000 cal BP, some 2,000-3,000 years older than any other East "
                    "Asian pottery.",
          caveats=[{"kind": "misconception",
                    "text": "Pottery is not a marker of farming or settling down. Here it "
                            "predates agriculture in the same region by over ten millennia.",
                    "source_ids": [S_WU_POTTERY]}],
          source_ids=[S_WU_POTTERY])

    FIRST("dog", "Domestic Dog", firsts, bp(15800), tier="foundational",
          summary="The first domesticated animal, and the only one domesticated by "
                  "hunter-gatherers rather than farmers.",
          start_dating_method="radiocarbon-calibrated", standing="majority",
          date_note="Oldest confirmed genetic evidence is 15,800-14,200 years ago, from sites "
                    "in Britain and Turkiye. Successive ancient-genome studies have pushed "
                    "this progressively earlier, and a Palaeolithic origin is now firm even "
                    "though the exact date and place are not.",
          caveats=[{"kind": "misconception",
                    "text": "Not a product of farming: dogs precede agriculture by thousands "
                            "of years and were domesticated by foragers.",
                    "source_ids": [S_DOG_2026]}],
          source_ids=[S_DOG_2026])

    FIRST("fermented-drink", "Fermented Drink", firsts, bp(13700), tier="intermediate",
          summary="Residues of fermented wheat and barley in stone mortars at Raqefet Cave, "
                  "made by Natufian foragers from wild cereals.",
          start_dating_method="radiocarbon-calibrated", standing="majority",
          date_note="13,700-11,700 cal BP. The Natufian is pre-agricultural, so this predates "
                    "domesticated cereals by millennia.",
          source_ids=[S_RAQEFET])

    FIRST("cereal-farming", "Cereal Domestication", firsts, bp(10600), tier="foundational",
          summary="Einkorn and emmer wheat at Cayonu and Cafer Hoyuk: the beginning of the crop "
                  "package that spread across three continents.",
          start_dating_method="radiocarbon-calibrated", standing="majority",
          date_note="10,600-9,900 cal BP for the earliest definite domesticated wheat. Barley "
                    "follows at Tell Aswad, 10,200-9,550 cal BP. A 2025 genetic study puts the "
                    "domestication-associated barley haplotype as much as 27,000 years old, "
                    "which no archaeobotanical evidence supports; that gap is unresolved.",
          source_ids=[S_FOUNDER_CROPS, S_FULLER_PROTRACTED])

    FIRST("woven-cloth", "Woven Cloth", firsts, -6700, tier="intermediate",
          summary="Preserved woven textile from Catalhoyuk — spinning and weaving, as distinct "
                  "from the far older twisting of fibre into cord.",
          start_dating_method="radiocarbon-calibrated", standing="consensus",
          date_note="c. 6700-6500 cal BC.",
          source_ids=[S_CATAL_TEXTILE])

    FIRST("irrigation", "Irrigation", firsts, -6200, tier="intermediate",
          summary="Canals and ditches at Choga Mami in Mesopotamia, the first farming that "
                  "reshaped the land to suit itself.",
          start_dating_method="radiocarbon-calibrated", standing="majority",
          date_note="Samarra culture, c. 6200-5700 BC.",
          source_ids=[S_CHOGA_MAMI])

    FIRST("wheel", "The Wheel", firsts, -3500, tier="foundational",
          summary="Wheeled wagons appear in Mesopotamia and central Europe at nearly the same "
                  "moment, and which came first is unresolved.",
          start_dating_method="typological", standing="majority",
          as_of=CHECKED,
          date_note="Uruk pictographs c. 3500-3350 BCE and the Bronocice pot at 3635-3370 cal "
                    "BCE are effectively contemporaneous. The oldest surviving physical wheel, "
                    "from the Ljubljana Marshes, is later at 3340-3030 cal BC. Near-simultaneous "
                    "appearance is the safest claim; priority is not settled.",
          alternatives=[{
              "label": "Central European priority (Bronocice pot)", "standing": "majority",
              "start_year": -3635, "start_year_max": -3370,
              "dating_method": "radiocarbon-calibrated",
              "note": "Funnelbeaker wagon depiction from Poland, on equal footing with Uruk "
                      "rather than derived from it.",
              "source_ids": [S_WHEEL]}],
          source_ids=[S_WHEEL])

    FIRST("writing", "Writing", firsts, -3400, tier="foundational",
          summary="Proto-cuneiform at Uruk and hieroglyphic tags at Abydos — two independent "
                  "inventions whose dates overlap.",
          start_dating_method="typological", standing="majority",
          as_of=CHECKED,
          date_note="Mesopotamian proto-cuneiform c. 3400-3200 BCE; the Abydos tomb U-j tags "
                    "c. 3320 BCE. The ranges overlap and the two systems developed "
                    "independently, so neither is assigned priority here.",
          alternatives=[{
              "label": "Egyptian priority (Abydos tomb U-j)", "standing": "majority",
              "start_year": -3320, "dating_method": "typological",
              "note": "Bone and ivory tags bearing early hieroglyphic signs, Naqada III.",
              "source_ids": [S_WRITING_NEA]}],
          caveats=[{"kind": "misconception",
                    "text": "Not a single invention that spread: Mesopotamian and Egyptian "
                            "writing arose independently within overlapping date ranges.",
                    "source_ids": [S_WRITING_NEA]}],
          source_ids=[S_WRITING_NEA])

    FIRST("horse-domestication", "Horse Domestication", firsts, -2200, tier="foundational",
          allow_outside_parent_dates=True,
          summary="The ancestry of every modern domestic horse traces to the lower Volga-Don "
                  "steppe, not to the older Botai husbandry once assumed to be its origin.",
          start_dating_method="radiocarbon-calibrated", standing="consensus",
          date_note="The DOM2 lineage emerges c. 2200 BCE and spreads rapidly after 2000 BC. "
                    "Botai horses, c. 3500 BC, remain the earliest known husbandry but are a "
                    "genetic dead end — Przewalski's ancestry, not ours. The two answer "
                    "different questions and conflating them is the usual error.",
          alternatives=[{
              "label": "Botai husbandry, c. 3500 BC", "standing": "superseded",
              "start_year": -3500, "dating_method": "radiocarbon-calibrated",
              "note": "Earliest known horse husbandry, but not ancestral to modern horses.",
              "source_ids": [S_HORSE_BOTAI]}],
          caveats=[{"kind": "misconception",
                    "text": "Botai is still widely cited as the origin of domestic horses; "
                            "genomics showed in 2021 that it is not.",
                    "source_ids": [S_HORSE_2021]}],
          source_ids=[S_HORSE_2021, S_HORSE_BOTAI])

    FIRST("chicken", "Domestic Chicken", firsts, -1650, tier="intermediate",
          allow_outside_parent_dates=True,
          summary="The world's most numerous bird was domesticated in mainland Southeast Asia, "
                  "far later and further east than long assumed.",
          start_dating_method="radiocarbon-calibrated", standing="majority",
          date_note="First unambiguous domestic chicken bones at Ban Non Wat, Thailand, "
                    "1650-1250 BCE. Chickens reach South Asia and Mesopotamia only in the late "
                    "2nd millennium BCE, and Mediterranean Europe around 800 BCE.",
          caveats=[{"kind": "misconception",
                    "text": "Long attributed to an Indian origin; a 2022 reassessment placed "
                            "the earliest secure evidence in Southeast Asia instead.",
                    "source_ids": [S_CHICKEN_2022]}],
          source_ids=[S_CHICKEN_2022])
