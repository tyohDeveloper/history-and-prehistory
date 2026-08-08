"""Southeast Asia and Oceania: the Austronesian expansion and what surrounded it.

`tools/coverage.py` found Southeast Asia with almost nothing between 10,000 and
1,600 BCE, and Oceania with nothing whatever between 10,000 and 1,500 BCE. The
largest maritime migration in human prehistory was absent from the dataset.

Research in `docs/seasia-oceania-research.md`.

The Austronesian expansion is authored as a spine with its stages hanging off
it, because the interesting thing about it is not that it happened but that it
did not happen the way it is usually told. It stalled — centuries between the
Philippines and the Marianas, more before Lapita. The domesticates did not
travel as a set: pigs reach northern Luzon two thousand years before dogs do.
Pottery appears in Borneo and the northern Philippines at the same time rather
than in sequence. And the crop words that matter in Oceania do not reconstruct
to Proto-Austronesian, which suggests they were picked up en route.

Two existing entities are enriched rather than duplicated. **Ban Chiang** gets
the bronze controversy it is famous for and did not carry: a 1976 claim of the
world's earliest bronze at 3600 BC, abandoned in 1982, and a long-versus-short
chronology dispute still live in 2022. **Lapita** gets the unresolved 3550-3200
cal BP range for its own beginning.

Rock art is deliberately absent. Dating claims were plentiful in search results
and thin in fetched primary sources, and the research pass marked them `n.a.`
rather than assert them.
"""

from builders import make_builders
from extensions_prehistory import bp

S_DABENKENG = "carson-hung-2022-luzon"
S_OOT_OXFORD = "austronesian-archaeolinguistics"
S_OOT_GENOMIC = "early-austronesians-taiwan"
S_ISEA_POTTERY = "isea-pottery-bayesian-2021"
S_MARIANAS = "unai-bapot-marianas"
S_COCHRANE_HUNT = "cochrane-hunt-isea-dispersal"
S_NUSANTAO = "solheim-nusantao-review"
S_ADNA_ACCULTURATION = "austronesian-dispersal-human-biology"
S_DA_BUT = "da-but-vietnam-neolithic"
S_THACH_LAC = "thach-lac-transition-2025"
S_MAN_BAC = "man-bac-aberdeen-thesis"
S_NON_NOK_THA = "non-nok-tha-jipa"
S_KHOK_PHANOM_DI = "khok-phanom-di-higham"
S_BAN_NON_WAT = "higham-2009-ban-non-wat"
S_HIGHAM_2015 = "higham-2015-bronze-chronology"
S_WHITE_LONG = "white-hamilton-long-chronology"
S_BRONZE_LIVE = "origins-bronze-age-msea-2022"
S_MCCOLL = "mccoll-2018-peopling-sea"
S_OBSIDIAN = "bismarck-obsidian-seafaring"
S_OBSIDIAN_OSTI = "bismarck-obsidian-report"
S_TORRES_BADU = "badu-15-torres-strait"
S_TORRES_DABANGAY = "dabangay-mabuyag"
S_TORRES_ORMI = "ormi-dauar-geoarchaeology-2025"
S_DINGO_FOSSIL = "balme-2018-dingo-madura-cave"
S_DINGO_GENOME = "dingo-ancient-dna-2024"
S_BACKED_ARTEFACTS = "backed-artefacts-holocene-climate"
S_AUS_POP_2011 = "australian-population-proxy-2011"
S_AUS_POP_2013 = "australian-population-curve-2013"
S_TOALEAN = "sulawesi-toalean-chronology"
S_LEANG_PANNINGE = "carlhoff-2021-leang-panninge"
S_LAPITA_RIETH = "rieth-athens-2017-lapita"
S_LAPITA_DEBATE = "debating-lapita-volume"

SEASIA_OCEANIA_SOURCES = [
    {"id": S_DABENKENG, "kind": "scholarly",
     "citation": "Carson & Hung (2022), 'Preceramic riverside hunter-gatherers and the arrival of Neolithic farmers in northern Luzon', Antiquity",
     "url": "https://www.cambridge.org/core/journals/antiquity/article/preceramic-riverside-huntergatherers-and-the-arrival-of-neolithic-farmers-in-northern-luzon/018B349F98B18C1668C944B0B287A678",
     "note": "Dabenkeng begins c. 5500-5000 BP; directly dated domestic pig at Nagsabaran 4448-4246 cal BP."},
    {"id": S_OOT_OXFORD, "kind": "scholarly",
     "citation": "Austronesian archaeolinguistics, Oxford Handbooks",
     "url": "https://academic.oup.com/edited-volume/60672/chapter/526636737",
     "note": "Expansion out of Taiwan into the northern Philippines dated to c. 4200/4000 BP."},
    {"id": S_OOT_GENOMIC, "kind": "scholarly",
     "citation": "'Early Austronesians: Into and Out of Taiwan'",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3951936/",
     "note": "Genomic simulation converges independently on 4.1-4.2 kya for the Out-of-Taiwan pulse."},
    {"id": S_ISEA_POTTERY, "kind": "scholarly",
     "citation": "'The first quantitative assessment of radiocarbon chronologies for Island Southeast Asian pottery' (2021)",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8171956/",
     "note": "Pottery appears contemporaneously in Borneo and the northern Philippines, against a staged sequence."},
    {"id": S_MARIANAS, "kind": "scholarly",
     "citation": "Excavation report on Unai Bapot, Saipan (Archaeopress)",
     "url": "https://www.archaeopress.com/Archaeopress/DMS/2B0B85F6AB3A4C7C806880BCE401AE48/9781784916657-sample.pdf",
     "note": "Oldest reported layer cal 1612-1558 BC."},
    {"id": S_COCHRANE_HUNT, "kind": "scholarly",
     "citation": "'The Austronesian Dispersal in Island Southeast Asia', Oxford Handbooks",
     "url": "https://academic.oup.com/edited-volume/34645/chapter/295205670",
     "note": "Pigs reach northern Luzon by 4500-4000 BP but dogs not until c. 2500 BP; crop words do not reconstruct to Proto-Austronesian."},
    {"id": S_NUSANTAO, "kind": "reference",
     "citation": "Review of Solheim's Nusantao Maritime Trading and Communication Network against Out-of-Taiwan",
     "url": "https://www.academia.edu/10134524/The_Austronesians_the_Nusantao_and_the_Lapita_Cultural_Complex_A_Review_of_Neolithic_migration_in_SEA_and_Oceania",
     "note": "Secondary review; frames Out-of-Taiwan as the dominant model and Nusantao as a minority critique."},
    {"id": S_ADNA_ACCULTURATION, "kind": "scholarly",
     "citation": "'Human biology of the Austronesian dispersal' (2015), Human Genetics",
     "url": "https://link.springer.com/article/10.1007/s00439-015-1620-z",
     "note": "Beyond the Philippines, acculturation rather than demographic replacement."},
    {"id": S_DA_BUT, "kind": "scholarly",
     "citation": "'The Neolithic of Vietnam', Oxford Handbooks",
     "url": "https://academic.oup.com/edited-volume/42054/chapter/355844411"},
    {"id": S_THACH_LAC, "kind": "scholarly",
     "citation": "Thach Lac transition study (2025), Journal of Island and Coastal Archaeology",
     "url": "https://www.tandfonline.com/doi/full/10.1080/15564894.2025.2474945",
     "note": "Notes no directly dated Da But site is younger than 3500 BCE, against the accepted 2500 BCE end."},
    {"id": S_MAN_BAC, "kind": "scholarly",
     "citation": "University of Aberdeen thesis, radiocarbon chronology for Man Bac",
     "url": "https://aura.abdn.ac.uk/server/api/core/bitstreams/a81db0e6-787c-4786-92e9-c53c59550fff/content",
     "note": "2066-1523 cal BCE on seven charcoal and four human-bone samples."},
    {"id": S_NON_NOK_THA, "kind": "scholarly",
     "citation": "'The Chronology and Status of Non Nok Tha', Journal of Indo-Pacific Archaeology",
     "url": "https://journals.lib.washington.edu/index.php/JIPA/article/view/14719",
     "note": "Neolithic occupation in the 14th century BC, earliest Bronze Age in the 10th."},
    {"id": S_KHOK_PHANOM_DI, "kind": "scholarly",
     "citation": "Higham, on Khok Phanom Di, Journal of the Siam Society",
     "url": "https://thesiamsociety.org/wp-content/uploads/2004/03/JSS_092_0c_Higham_OpposedHumanFigureAtKhokPhnaomDi.pdf"},
    {"id": S_BAN_NON_WAT, "kind": "scholarly",
     "citation": "Higham & Higham (2009), 'A new chronological framework for prehistoric Southeast Asia, based on a Bayesian model from Ban Non Wat', Antiquity",
     "url": "https://www.cambridge.org/core/journals/antiquity/article/new-chronological-framework-for-prehistoric-southeast-asia-based-on-a-bayesian-model-from-ban-non-wat/4AA644BD284B1522DF1B4D193422600D",
     "note": "75 radiocarbon dates; the pivot to the short chronology."},
    {"id": S_HIGHAM_2015, "kind": "scholarly",
     "citation": "Higham, Douka & Higham (2015), 'A New Chronology for the Bronze Age of Northeastern Thailand', PLOS ONE",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4575132/",
     "note": "Ban Chiang's Neolithic-to-Bronze transition at 1050-955 BC; earliest bronze artefact 1025-935 BC."},
    {"id": S_WHITE_LONG, "kind": "scholarly",
     "citation": "White & Hamilton, the long-chronology model for Ban Chiang",
     "url": "https://os.pennds.org/archaeobib_filestore/pdf_articles/bookchapters/2014_WhiteHamilton.pdf",
     "note": "Bronze as a developed technology by c. 2000 BC, argued to derive from Seima-Turbino."},
    {"id": S_BRONZE_LIVE, "kind": "scholarly",
     "citation": "'The Origins of the Bronze Age in Mainland Southeast Asia' (2022), Oxford Handbooks",
     "url": "https://academic.oup.com/edited-volume/42054/chapter/355846103?searchresult=1",
     "note": "Calls the long-versus-short debate 'close to resolution' — not resolved."},
    {"id": S_MCCOLL, "kind": "scholarly",
     "citation": "McColl et al. (2018), 'The prehistoric peopling of Southeast Asia', Science",
     "url": "https://www.science.org/doi/10.1126/science.aat3628",
     "note": "Neither simple layer model fits; ancestry changes by ~4 ka, with further waves after."},
    {"id": S_OBSIDIAN, "kind": "scholarly",
     "citation": "National Museum of Ethnology (Japan), Late Pleistocene-Holocene seafaring and obsidian in the Bismarcks",
     "url": "https://minpaku.repo.nii.ac.jp/record/2000374/files/KH_049_3_02.pdf",
     "note": "Talasea obsidian reaches New Ireland by c. 20,000 BP."},
    {"id": S_OBSIDIAN_OSTI, "kind": "institutional",
     "citation": "Archaeological report on Bismarck Archipelago obsidian sourcing (OSTI AU9917997)",
     "url": "https://www.osti.gov/etdeweb/servlets/purl/347110"},
    {"id": S_TORRES_BADU, "kind": "scholarly",
     "citation": "'Badu 15 and the Papuan-Austronesian settlement of Torres Strait', ANU Open Research",
     "url": "https://openresearch-repository.anu.edu.au/items/2eb1ae78-2587-49b5-beb6-9bf3e7d82720",
     "note": "Permanent occupation 8000-6000 cal BP, a fleeting presence 6000-3500, then renewed settlement."},
    {"id": S_TORRES_DABANGAY, "kind": "scholarly",
     "citation": "Wright et al., re-excavation of Dabangay, Mabuyag, Australian Archaeology",
     "url": "https://australianarchaeologicalassociation.com.au/wp-content/uploads/2013/06/AA76-Dabangay-Wright-200dpi.pdf",
     "note": "Sustained settlement 7239-4901 cal BP; dugong and turtle hunting by 6480-6256 cal BP."},
    {"id": S_TORRES_ORMI, "kind": "scholarly",
     "citation": "Geoarchaeological study at Ormi, Dauar (2025), Environmental Archaeology",
     "url": "https://www.tandfonline.com/doi/full/10.1080/14614103.2025.2522542",
     "note": "Eastern Torres Strait occupation from 2600-2250 cal BP, with no evidence of Pleistocene use."},
    {"id": S_DINGO_FOSSIL, "kind": "scholarly",
     "citation": "Balme et al. (2018), 'New dates on dingo bones from Madura Cave', Scientific Reports",
     "url": "https://www.nature.com/articles/s41598-018-28324-x",
     "note": "3348-3081 cal BP, the oldest reliable direct date for the dingo in Australia."},
    {"id": S_DINGO_GENOME, "kind": "news",
     "citation": "'Ancient DNA analysis reveals dingoes have been in Australia thousands of years' (2024), Science",
     "url": "https://www.science.org/content/article/ancient-dna-analysis-reveals-dingoes-have-been-australia-thousands-years",
     "note": "42 ancient genomes; arrival window of 3,000-8,000 years ago."},
    {"id": S_BACKED_ARTEFACTS, "kind": "institutional",
     "citation": "'The changing abundance of backed artefacts in south-eastern Australia: a response to Holocene climate change', Australian Museum",
     "url": "https://publications.australian.museum/the-changing-abundance-of-backed-artefacts-in-south-eastern-australia-a-response-to-holocene-climate-change/",
     "note": "Present from at least 8,500 years ago; the increase in number falls at 4,000-3,500."},
    {"id": S_AUS_POP_2011, "kind": "scholarly",
     "citation": "'Reconstructing the dynamics of ancient human populations' (2011)",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3203495/",
     "note": "Growth negligible before 5,000 years ago, faster after."},
    {"id": S_AUS_POP_2013, "kind": "scholarly",
     "citation": "'A new population curve for prehistoric Australia' (2013)",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3652441/",
     "note": "Growth in pulses from c. 12 ka, not a single mid-Holocene acceleration."},
    {"id": S_TOALEAN, "kind": "scholarly",
     "citation": "Toalean chronology, PLOS ONE (2021), following Bulbeck et al. 2000",
     "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0251138",
     "note": "Early Toalean 7500-5500 BP, Late Preceramic 5500-3500, Ceramic 3500-2000."},
    {"id": S_LEANG_PANNINGE, "kind": "scholarly",
     "citation": "Carlhoff et al. (2021), 'Genome of a middle Holocene hunter-gatherer from Wallacea', Nature",
     "url": "https://www.nature.com/articles/s41586-021-03823-6",
     "note": "A previously unknown divergent lineage, split c. 37,000 years ago, with ~2.2% Denisovan ancestry."},
    {"id": S_LAPITA_RIETH, "kind": "scholarly",
     "citation": "Rieth & Athens (2017), Bayesian model for Late Holocene human expansion into Remote Oceania",
     "url": "https://iarii.org/wp-content/uploads/2018/03/Rieth__Athens_2017-Late-Holocene-Human-Expansion.pdf",
     "note": "Lapita emergence 3535-3234 cal BP at 95% probability."},
    {"id": S_LAPITA_DEBATE, "kind": "scholarly",
     "citation": "Debating Lapita: Distribution, Chronology, Society and Subsistence (ANU Press, open access)",
     "url": "https://library.oapen.org/bitstream/id/a0ef75fa-3f03-4d94-b680-70cb781c03a5/book%20(1).pdf",
     "note": "Other groups favour a later start of 3300-3200 cal BP."},
]

CHECKED = "2026-08-08"
C14 = "radiocarbon-calibrated"


def extend(E, entities):
    _, P, ERA, EVENT, _, _ = make_builders(E)
    by_id = {e["id"]: e for e in entities}
    sea = "southeast-asia.prehistory"
    oce = "oceania.prehistory"

    # ---- The Austronesian expansion ----------------------------------------
    ERA("austronesian-expansion", "The Austronesian Expansion", sea,
        bp(5500), -1130, "foundational",
        summary="From Taiwan to the edge of Remote Oceania: the widest maritime dispersal in "
                "prehistory, and one that kept stopping.",
        start_dating_method=C14, end_dating_method=C14, standing="majority",
        date_precision="approx", as_of=CHECKED,
        date_note="Taiwan settled from the southeast China coast c. 5000 BP; out into the "
                  "northern Philippines c. 4200-4000 BP, a figure archaeology and genomic "
                  "simulation reach independently; Palau and the Marianas c. 3500 BP; Lapita "
                  "in the Bismarcks c. 3300 BP; Vanuatu 3250-3100 BP.",
        alternatives=[{
            "label": "Nusantao maritime network (Solheim)", "standing": "minority",
            "note": "Places the origin in the southern Philippines and eastern Indonesia, with "
                    "multidirectional spread by trade rather than a farming migration.",
            "source_ids": [S_NUSANTAO]}],
        caveats=[
            {"kind": "misconception",
             "text": "Not an express train to Polynesia. The expansion stalled for centuries "
                     "between the Philippines and the Marianas, and again before Lapita.",
             "source_ids": [S_OOT_OXFORD, S_COCHRANE_HUNT]},
            {"kind": "contested-existence",
             "text": "The domesticates did not travel as a package: pigs reach northern Luzon "
                     "by 4500-4000 BP but dogs not until c. 2500 BP.",
             "source_ids": [S_COCHRANE_HUNT]}],
        source_ids=[S_OOT_OXFORD, S_OOT_GENOMIC, S_COCHRANE_HUNT, S_ADNA_ACCULTURATION])

    aus = "southeast-asia.prehistory.austronesian-expansion"

    P("dabenkeng", "Dabenkeng Culture", aus, bp(5500), -2200, "intermediate",
      summary="Taiwan's founding Neolithic, with cord-marked pottery, polished stone and "
              "millet — the archaeological anchor of the Austronesian homeland.",
      aliases=["Dapenkeng", "Tapenkeng"],
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Begins c. 5500-5000 BP, with the main phase ending c. 4600-4200 BP and a late "
                "regional phase persisting to c. 2200 BC.",
      source_ids=[S_DABENKENG])

    EVENT("isea-pottery", "Pottery Reaches Island Southeast Asia", aus, bp(5430), bp(4290),
          "intermediate",
          summary="Pottery appears in Borneo and the northern Philippines at the same time, "
                  "not one after the other.",
          start_dating_method=C14, end_dating_method=C14, standing="majority",
          date_precision="approx",
          date_note="A Bayesian synthesis across 20 sites in six island regions puts pottery "
                    "entering the northern Philippine record at 5430-4290 cal BP, and finds "
                    "Borneo contemporaneous rather than downstream.",
          caveats=[{"kind": "misconception",
                    "text": "Contemporaneous appearance in Borneo and Luzon does not fit a "
                            "single staged wave south from Taiwan, and the authors say so.",
                    "source_ids": [S_ISEA_POTTERY]}],
          source_ids=[S_ISEA_POTTERY])

    P("marianas", "Settlement of the Marianas", aus, -1612, -1130, "intermediate",
      summary="The first crossing into Remote Oceania — some 2,000 km of open ocean, the "
              "longest voyage anyone had yet made.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="disputed", as_of=CHECKED,
      alternatives=[{
          "label": "Hardwater-corrected Bayesian model", "standing": "minority",
          "start_year": -1250, "end_year": -1130, "dating_method": C14,
          "note": "Correcting shell dates for hardwater effects moves first arrival "
                  "three centuries later.",
          "source_ids": [S_MARIANAS]}],
      date_note="The oldest layer at Unai Bapot on Saipan calibrates to 1612-1558 BC. A "
                "Bayesian re-analysis correcting for hardwater effects in shell instead gives "
                "first arrival at 3200-3080 cal BP, roughly 1250-1130 BC. Both are live; the "
                "span shown brackets them rather than choosing.",
      source_ids=[S_MARIANAS])

    # ---- Neolithic mainland ------------------------------------------------
    P("da-but", "Da But Culture", sea, -5000, -3500, "specialist",
      summary="Shell-midden communities in northern Vietnam with basket-marked pottery, "
              "conventionally marking the end of the Hoabinhian way of life.",
      aliases=["Đa Bút"],
      start_dating_method=C14, end_dating_method=C14, standing="minority",
      date_precision="disputed", as_of=CHECKED,
      alternatives=[{
          "label": "Long chronology, 7000-2000 BC", "standing": "minority",
          "start_year": -7000, "end_year": -2000, "dating_method": C14,
          "note": "Includes an early cave phase and runs to the Vietnamese accepted end date.",
          "source_ids": [S_DA_BUT]}],
      date_note="GENUINELY UNRESOLVED and never Bayesian-modelled as a whole. Published starts "
                "run from 7000 BC for the early cave phase to c. 4500 BC for the middens; ends "
                "from 3500 BCE to 2000 BC. The chronology Vietnamese archaeologists accept runs "
                "to 2500 BCE, but the same 2025 study notes no directly dated Da But site is "
                "younger than 3500 BCE. The range shown is the defensible core, not a consensus.",
      source_ids=[S_DA_BUT, S_THACH_LAC])

    P("man-bac", "Man Bac", sea, -2066, -1523, "intermediate",
      summary="A northern Vietnamese cemetery whose 85 burials hold both resident foragers and "
              "incoming farmers, side by side.",
      aliases=["Mán Bạc"],
      start_dating_method=C14, end_dating_method=C14, standing="consensus",
      date_note="2066-1523 cal BCE on seven charcoal and four human-bone samples.",
      source_ids=[S_MAN_BAC])

    P("khok-phanom-di", "Khok Phanom Di", sea, -2000, -1500, "intermediate",
      summary="An estuarine mound on the Gulf of Siam with a seven-stage mortuary sequence "
              "built up in only five centuries.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="The standard range is c. 2000-1500 BC. A revision using human bone and shell "
                "rather than charcoal reports an earlier occupation, but the revised figures "
                "were not available in the fetched source and are not guessed at here.",
      source_ids=[S_KHOK_PHANOM_DI])

    P("ban-non-wat", "Ban Non Wat", sea, -1700, -1000, "foundational",
      summary="The Thai site whose 75 modelled radiocarbon dates rebuilt the chronology of "
              "Southeast Asian prehistory.",
      start_dating_method=C14, end_dating_method=C14, standing="consensus",
      date_note="Initial Neolithic settlement in the 17th century BC, transition into the "
                "Bronze Age in the late 11th, and a 'starburst' of hierarchical activity "
                "around 1000 BC.",
      source_ids=[S_BAN_NON_WAT, S_HIGHAM_2015])

    P("non-nok-tha", "Non Nok Tha", sea, -1500, -600, "specialist",
      summary="With Ban Chiang, one of the two sites behind the claim that Southeast Asia "
              "invented bronze first — and behind its collapse.",
      start_dating_method=C14, end_dating_method=C14, standing="consensus",
      date_note="Bayesian re-dating puts initial Neolithic settlement at 1500-1300 BC and the "
                "earliest socketed copper-base axe at 980-900 BC. The original excavation "
                "claimed a fourth-millennium BC date.",
      alternatives=[{
          "label": "Original fourth-millennium BC claim", "standing": "superseded",
          "start_year": -4000, "dating_method": "typological",
          "note": "The 1960s-70s dating, comprehensively replaced.",
          "source_ids": [S_NON_NOK_THA]}],
      source_ids=[S_NON_NOK_THA, S_HIGHAM_2015])

    EVENT("neolithic-migration-sea", "Neolithic Migration into Southeast Asia", sea,
          bp(4000), bp(4000), "foundational",
          summary="East Asian farming populations move south and mix with resident "
                  "Hoabinhian-descended foragers rather than replacing them.",
          start_dating_method=C14, standing="majority", date_precision="approx",
          date_note="Ancient genomes show ancestry changing by about 4,000 years ago. The old "
                    "two-layer model survives as a skeleton, but the 2018 genomes add a "
                    "further Bronze Age pulse from China, and work through 2026 subdivides the "
                    "second layer into as many as five southward waves.",
          caveats=[{"kind": "misconception",
                    "text": "Neither pure replacement nor pure continuity. Both Hoabinhian "
                            "foragers and East Asian farmers contribute to modern Southeast "
                            "Asian ancestry.",
                    "source_ids": [S_MCCOLL]}],
          source_ids=[S_MCCOLL])

    P("toalean", "Toalean Culture", sea, bp(8000), -451, "specialist",
      allow_outside_parent_dates=True,
      summary="A hunter-gatherer tradition confined to a corner of South Sulawesi, which "
              "outlasted the arrival of farming around it by millennia.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Early Toalean 7500-5500 BP, Late Preceramic 5500-3500 with the distinctive "
                "Maros points, Ceramic Toalean 3500-2000 BP.",
      caveats=[{"kind": "misconception",
                "text": "The one sequenced Toalean individual, buried 7.3-7.2 kyr cal BP, "
                        "belongs to a previously unknown lineage that split around 37,000 "
                        "years ago and carries about 2.2% Denisovan ancestry.",
                "source_ids": [S_LEANG_PANNINGE]}],
      source_ids=[S_TOALEAN, S_LEANG_PANNINGE])

    # ---- Oceania -----------------------------------------------------------
    P("bismarck-obsidian", "Bismarck Obsidian Network", oce, bp(20000), bp(3000),
      "foundational",
      summary="Obsidian moved 600 km between islands of the Bismarck Archipelago for some "
              "seventeen thousand years — among the longest-running exchange networks known.",
      start_dating_method=C14, end_dating_method=C14, standing="consensus",
      date_note="Talasea obsidian reaches Buang Merabak on New Ireland by c. 20,000 BP and "
                "Lou Island obsidian reaches Manus by 13,000 BP. Talasea dominates every "
                "Bismarck assemblage in the Early Lapita phase at 3300-3000 BP.",
      caveats=[{"kind": "misconception",
                "text": "Near Oceania was not waiting to be discovered by Lapita voyagers. It "
                        "had been trading across open water for seventeen millennia already.",
                "source_ids": [S_OBSIDIAN, S_OBSIDIAN_OSTI]}],
      source_ids=[S_OBSIDIAN, S_OBSIDIAN_OSTI])

    P("torres-strait", "Torres Strait Settlement", oce, bp(8000), bp(2250), "intermediate",
      allow_outside_parent_dates=True,
      summary="The island chain between New Guinea and Australia, settled at very different "
              "times at its two ends.",
      start_dating_method=C14, end_dating_method=C14, standing="minority",
      date_precision="disputed", as_of=CHECKED,
      date_note="REGIONALLY SPLIT, and not to be reduced to one figure. In the west, Badu 15 "
                "shows permanent occupation 8000-6000 cal BP, only a fleeting presence "
                "6000-3500, then renewed settlement; Dabangay on Mabuyag gives 7239-4901 cal BP "
                "with dugong hunting by 6480-6256. In the east, Ormi on Dauar begins only "
                "2600-2250 cal BP, and that study finds no Pleistocene or early Holocene "
                "occupation at all.",
      alternatives=[{
          "label": "Eastern Torres Strait, from c. 2500 BP", "standing": "majority",
          "start_year": bp(2600), "end_year": bp(2250), "dating_method": C14,
          "note": "The widely quoted '2,500 years' figure, accurate for the eastern islands.",
          "source_ids": [S_TORRES_ORMI]}],
      source_ids=[S_TORRES_BADU, S_TORRES_DABANGAY, S_TORRES_ORMI])

    EVENT("dingo-arrival", "Arrival of the Dingo", oce, bp(3348), bp(3081), "intermediate",
          summary="A dog carried to Australia by sea, and the clearest evidence of outside "
                  "contact before Europeans.",
          start_dating_method=C14, end_dating_method=C14, standing="majority",
          date_precision="approx", as_of=CHECKED,
          date_note="The oldest directly dated specimen, from Madura Cave on the Nullarbor, "
                    "gives 3348-3081 cal BP. A 2024 study of 42 ancient genomes puts lineage "
                    "divergence anywhere in 3,000-8,000 years ago — an upper bound on ancestry, "
                    "not a second arrival date. Older molecular-clock figures of 5,000 to "
                    "18,000 years are superseded.",
          alternatives=[{
              "label": "Genomic divergence window (2024)", "standing": "minority",
              "start_year": bp(8000), "end_year": bp(3000), "dating_method": "unknown",
              "note": "Lineage divergence from 42 ancient genomes; does not overturn the "
                      "c. 3,000 BP fossil floor.",
              "source_ids": [S_DINGO_GENOME]}],
          source_ids=[S_DINGO_FOSSIL, S_DINGO_GENOME])

    ERA("australian-intensification", "Australian Mid-Holocene Intensification", oce,
        bp(5000), bp(2000), "intermediate", allow_outside_parent_dates=True,
        summary="More people, more sites and far more backed artefacts across Australia, "
                "tracking the onset of a more variable climate.",
        start_dating_method=C14, end_dating_method=C14, standing="minority",
        date_precision="disputed", as_of=CHECKED,
        date_note="Backed artefacts, present from at least 8,500 years ago, multiply sharply "
                  "at 4,000-3,500 cal BP and again at 3,300-1,970, tracking intensified ENSO "
                  "variability. The population signal is disputed: one radiocarbon-density "
                  "model finds negligible growth before 5,000 BP and acceleration after, "
                  "another finds pulsed growth from about 12,000 BP with one pulse at "
                  "4,400-3,700. Both are peer-reviewed and use different datasets.",
        alternatives=[{
            "label": "Pulsed growth from the terminal Pleistocene", "standing": "minority",
            "start_year": bp(12000), "dating_method": C14,
            "note": "Growth in pulses from c. 12 ka rather than one mid-Holocene acceleration.",
            "source_ids": [S_AUS_POP_2013]}],
        caveats=[{"kind": "misconception",
                  "text": "Backed artefacts did not appear at 4,000 BP. They had been made for "
                          "at least four thousand years already; what changed was how many.",
                  "source_ids": [S_BACKED_ARTEFACTS]}],
        source_ids=[S_BACKED_ARTEFACTS, S_AUS_POP_2011, S_AUS_POP_2013])

    # ---- Enrich two existing entities --------------------------------------
    #
    # Ban Chiang is famous for a claim the dataset did not record: that Southeast
    # Asia invented bronze before anyone else. That claim is dead, but the
    # chronology that replaced it is still argued over, and the entity said
    # nothing about either.
    bc = by_id.get("southeast-asia.prehistory.ban-chiang")
    if bc is not None:
        bc["as_of"] = CHECKED
        bc["date_precision"] = "disputed"
        bc["date_note"] = (
            "Bayesian modelling on human and animal bone puts the Neolithic-to-Bronze "
            "transition here at 1050-955 BC, with the earliest bronze artefact — a socketed "
            "spear from Burial 76 — at 1025-935 BC. Across five Khorat Plateau sites the "
            "transition falls in the late 11th or 10th centuries BC. The rival long chronology "
            "puts bronze at c. 2000-1800 BC on seven AMS dates from rice phytoliths and organic "
            "temper, methods the short-chronology camp rejects as unreliable."
        )
        bc["standing"] = "majority"
        # The entity already carried an "Old long chronology" superseded entry at
        # 3600 BCE, which is the same 1976 claim. Only the still-live White and
        # Hamilton position is new here; adding the 1976 one again produced two
        # alternatives asserting the same thing at the same date.
        bc["alternatives"] = list(bc.get("alternatives", [])) + [
            {"label": "Long chronology (White & Hamilton)", "standing": "minority",
             "start_year": -2100, "end_year": -1500, "dating_method": C14,
             "note": "Bronze already developed by c. 2000 BC, argued to derive from "
                     "Seima-Turbino rather than from Shang China.",
             "source_ids": [S_WHITE_LONG]},
        ]
        bc["caveats"] = list(bc.get("caveats", [])) + [
            {"kind": "misconception",
             "text": "Not the world's earliest bronze. That 1976 claim was abandoned by "
                     "archaeology in 1982, and Near Eastern and Chinese bronze both predate "
                     "Ban Chiang on either surviving chronology.",
             "source_ids": [S_HIGHAM_2015, S_BRONZE_LIVE]},
        ]
        bc["source_ids"] = list(bc.get("source_ids", [])) + [
            S_HIGHAM_2015, S_WHITE_LONG, S_BRONZE_LIVE]

    # Lapita's own start date is unsettled by roughly three centuries.
    lap = by_id.get("oceania.melanesia.lapita")
    if lap is not None:
        lap["as_of"] = CHECKED
        lap["date_precision"] = "disputed"
        lap["alternatives"] = list(lap.get("alternatives", [])) + [
            {"label": "Later emergence, c. 3300-3200 cal BP", "standing": "minority",
             "start_year": bp(3300), "dating_method": C14,
             "note": "Kirch and others hold the Bismarck dates are no earlier than 3200 BP.",
             "source_ids": [S_LAPITA_DEBATE]},
        ]
        lap["caveats"] = list(lap.get("caveats", [])) + [
            {"kind": "contested-existence",
             "text": "When Lapita begins is unresolved across roughly three centuries: Bayesian "
                     "models give 3535-3234 cal BP, others no earlier than 3200.",
             "source_ids": [S_LAPITA_RIETH, S_LAPITA_DEBATE]},
        ]
        lap["source_ids"] = list(lap.get("source_ids", [])) + [S_LAPITA_RIETH, S_LAPITA_DEBATE]
