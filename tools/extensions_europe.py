"""European prehistory 10,000-2,500 BCE: the Mesolithic, and farming's arrival.

`tools/coverage.py` found Europe holding five non-reign entities for the whole
of 10,000-3,000 BCE, and nothing at all between 10,000 and 5,500. The entire
European Mesolithic was missing, and so was every step by which farming crossed
the continent — the dataset went straight from Neanderthals and cave art to the
Linear Pottery Culture.

Research in `docs/europe-research.md` (84 sources).

Two themes run through this pass and are worth stating once.

**Almost everything here has been re-dated recently, and usually later.** Varna
moved ~200 years younger under AMS; Thessaly's Neolithic start moved from 7000
to 6700-6500 cal BC; Lepenski Vir gained a 700-year occupation hiatus that its
original excavator's stratigraphy did not have; Skara Brae turned out not to be
continuously occupied. Where an older figure is still in wide circulation it is
carried as a `superseded` alternative rather than dropped, because the reader
is likely to arrive holding it.

**Farming did not arrive as a wave.** It came by two routes at different
speeds, and — the harder finding — it came substantially as people rather than
as ideas. The ancient-DNA turnover is authored as its own entity because it is
the single largest revision to European prehistory in the last fifteen years
and it does not belong buried in a note on somebody's pottery.

Three items researched here are deliberately absent. The Tardenoisian could not
be pinned down: fetched sources disagree by up to 3,000 years and mix calibrated
with uncalibrated figures. A pan-European Sauveterrian range and a sharp Azilian
end date are likewise unsupportable. Guessing them would be worse than the gap.
"""

from builders import make_builders
from extensions_prehistory import bp

S_MAGLEMOSE_BONE = "maglemose-bone-points-2020"
S_LUNDBY = "lundby-mose-preboreal"
S_NWPOLAND_C14 = "nw-poland-mesolithic-c14"
S_ERTEBOLLE = "ertebolle-southern-scandinavia"
S_AZILIAN = "azilian-radiocarbon-series"
S_ROMAGNANO = "romagnano-sauveterrian-bayesian"
S_STARCARR = "star-carr-structures-2024"
S_LEPENSKI = "boric-2018-lepenski-vir"
S_DOGGERLAND_2026 = "doggerland-inundation-2026"
S_LOST_FRONTIERS = "europes-lost-frontiers"
S_STOREGGA = "bondevik-2024-storegga"
S_WENINGER_STOREGGA = "weninger-2008-storegga"
S_FRANCHTHI = "franchthi-early-cereals-2013"
S_GREEK_NEOLITHIC = "greek-neolithic-recalibration"
S_STARCEVO = "starcevo-central-balkans-demography"
S_SKC_RANGE = "starcevo-koros-cris-range"
S_ZILHAO_2001 = "zilhao-2001-maritime-pioneer"
S_FORT_2024 = "fort-2024-two-routes"
S_VINCA = "vinca-enclosed-settlement"
S_VINCA_BAYES = "vinca-belo-brdo-bayesian"
S_CUCUTENI = "cucuteni-trypillia-subsistence"
S_NEBELIVKA = "nebelivka-megasite-chronology"
S_MAIDANETSKE = "trypillia-megasites-urbanism"
S_VARNA_AMS = "higham-varna-ams"
S_VARNA_KRAUSS = "krauss-varna-analysis"
S_TRB_SWEDEN = "trb-southern-sweden"
S_TRB_UKRAINE = "trb-western-ukraine"
S_MICHELSBERG_DNA = "michelsberg-ancient-dna"
S_MICHELSBERG_PHASES = "michelsberg-hesse-phases"
S_SKARA_BRAE = "skara-brae-redating-2017"
S_BRODGAR = "ness-of-brodgar-bayesian"
S_NEWGRANGE = "newgrange-feasting-isotopes"
S_NEWGRANGE_CAL = "newgrange-calibration-history"
S_HAAK_2015 = "haak-2015-steppe-migration"
S_ADMIXTURE_2022 = "european-holocene-admixture-2022"
S_BEAKER_2026 = "rhine-meuse-forager-ancestry-2026"

EUROPE_SOURCES = [
    {"id": S_MAGLEMOSE_BONE, "kind": "scholarly",
     "citation": "'An integrated analysis of Maglemose bone points reframes the Early Mesolithic of Southern Scandinavia' (2020), Scientific Reports",
     "url": "https://www.nature.com/articles/s41598-020-74258-8",
     "note": "AMS series splitting Early from Late Maglemose at a c. 10,300 cal BP hiatus."},
    {"id": S_LUNDBY, "kind": "scholarly",
     "citation": "'Early Maglemosian culture in the Preboreal landscape: Lundby Mose, Sjaelland'",
     "url": "https://core.ac.uk/download/pdf/82106402.pdf"},
    {"id": S_NWPOLAND_C14, "kind": "scholarly",
     "citation": "'New radiocarbon dates for ornamented Mesolithic objects from northwest Poland', Antiquity",
     "url": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8A12B95243E8043511BC7C6E63D17B22/S0003598X22001429a.pdf/new_radiocarbon_dates_for_ornamented_mesolithic_objects_from_northwest_poland_chronology_and_regional_connections_in_the_western_baltic_region.pdf",
     "note": "Gives Kongemose c. 6500-5400 BC."},
    {"id": S_ERTEBOLLE, "kind": "scholarly",
     "citation": "'Places of Settlement in Southern Scandinavia', Oxford Handbooks",
     "url": "https://academic.oup.com/edited-volume/35019/chapter/298822185",
     "note": "Ertebolle period c. 5400-4000 cal BC."},
    {"id": S_AZILIAN, "kind": "scholarly",
     "citation": "'Divergence in the evolution of Paleolithic symbolic and Mesolithic technological traditions' (radiocarbon table for the French Early Azilian)",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5336238/"},
    {"id": S_ROMAGNANO, "kind": "scholarly",
     "citation": "Bayesian-modelled radiocarbon distributions for the Romagnano rock shelter, PLOS ONE",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12440202/table/pone.0331392.t003/",
     "note": "Italian Sauveterrian phases; diverges from older French typological dating by roughly a millennium."},
    {"id": S_STARCARR, "kind": "scholarly",
     "citation": "'Spatial organisation within the earliest evidence of post-built structures at Star Carr' (2024), PLOS ONE",
     "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0306908"},
    {"id": S_LEPENSKI, "kind": "scholarly",
     "citation": "Boric et al. (2018), 'High-Resolution AMS Dating of Architecture, Boulder Artworks and the Transition to Farming at Lepenski Vir', Scientific Reports",
     "url": "https://www.nature.com/articles/s41598-018-31884-7",
     "note": "111 measurements; establishes a hiatus of at least 700 years the original stratigraphy lacked."},
    {"id": S_DOGGERLAND_2026, "kind": "news",
     "citation": "'New timeline for the drowning of Doggerland', The Past (2026), reporting Bensharada et al., Humans 6(1):5",
     "url": "https://the-past.com/news/new-timeline-for-the-drowning-of-doggerland/",
     "note": "Reports the transitional freshwater-to-marine layer at 10,243-10,199 years ago."},
    {"id": S_LOST_FRONTIERS, "kind": "institutional",
     "citation": "Europe's Lost Frontiers, Volume 1: Context and Methodology",
     "url": "https://www.vliz.be/imisdocs/publications/407325.pdf",
     "note": "Final inundation of the Outer Dowsing Deep cores between 8,200 and 7,200 BP."},
    {"id": S_STOREGGA, "kind": "scholarly",
     "citation": "Bondevik et al. (2024), 'Contamination of 8.2 ka cold climate records by the Storegga tsunami in the Nordic Seas', Nature Communications 15:2904",
     "url": "https://www.nature.com/articles/s41467-024-47347-9",
     "note": "IntCal20/Marine20 recalibration placing the slide within the coldest decades of the 8.2 ka event."},
    {"id": S_WENINGER_STOREGGA, "kind": "scholarly",
     "citation": "Weninger et al. (2008), 'The catastrophic final flooding of Doggerland by the Storegga Slide Tsunami'",
     "url": "https://profmarkcollard.com/wp-content/uploads/2014/09/Weninger_et_al_2008.pdf",
     "note": "Gives 8,100 +/- 100 cal BP, compatible with the 2024 recalibration."},
    {"id": S_FRANCHTHI, "kind": "scholarly",
     "citation": "'Early seventh-millennium AMS dates from domestic seeds in the Initial Neolithic at Franchthi Cave' (2013), Antiquity",
     "url": "https://www.cambridge.org/core/journals/antiquity/article/early-seventhmillennium-ams-dates-from-domestic-seeds-in-the-initial-neolithic-at-franchthi-cave-argolid-greece/73AF10B4F6C3422ABA362FDBAC4D71FB",
     "note": "Cereals earlier in the Argolid than in northern Greece or Bulgaria, against a single inland front."},
    {"id": S_GREEK_NEOLITHIC, "kind": "scholarly",
     "citation": "'Preceramic, Aceramic or Early Ceramic? The radiocarbon-dated beginnings of the Greek Neolithic'",
     "url": "https://scispace.com/pdf/preceramic-aceramic-or-early-ceramic-the-radiocarbon-dated-tqz02xg7wf.pdf",
     "note": "Revises the Thessalian Neolithic start from c. 7000 cal BC to 6700-6500 cal BC."},
    {"id": S_STARCEVO, "kind": "scholarly",
     "citation": "'Demography of the Early Neolithic Population in Central Balkans', PLOS ONE",
     "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0160832"},
    {"id": S_SKC_RANGE, "kind": "scholarly",
     "citation": "Durham University repository, Starcevo-Koros-Cris radiocarbon range c. 6200-5500 cal BC",
     "url": "https://durham-repository.worktribe.com/OutputFile/1319467"},
    {"id": S_ZILHAO_2001, "kind": "scholarly",
     "citation": "Zilhao (2001), 'Radiocarbon evidence for maritime pioneer colonization at the origins of farming in west Mediterranean Europe', PNAS",
     "url": "https://www.pnas.org/doi/10.1073/pnas.241522898",
     "note": "Short-lived samples only, an explicit guard against old-wood bias."},
    {"id": S_FORT_2024, "kind": "scholarly",
     "citation": "Fort & Perez-Losada (2024), 'Interbreeding between farmers and hunter-gatherers along the inland and Mediterranean routes of Neolithic spread in Europe', Nature Communications 15:7032",
     "url": "https://www.nature.com/articles/s41467-024-51335-4",
     "note": "50 km per generation inland against 70 km along the coast; interbreeding rate the same on both."},
    {"id": S_VINCA, "kind": "scholarly",
     "citation": "'A Vinca Culture Enclosed and Fortified Settlement in the Balkans', University of Lancashire repository",
     "url": "https://knowledge.lancashire.ac.uk/id/eprint/21446/13/21446%20vinca%20paper.pdf"},
    {"id": S_VINCA_BAYES, "kind": "scholarly",
     "citation": "'Interwoven strategies: Vinca' (Bayesian dating of Vinca-Belo Brdo), University of Stirling repository",
     "url": "https://dspace.stir.ac.uk/bitstream/1893/23547/1/RESUBMITTED-Interwoven-strategies-Vinca-v7.pdf",
     "note": "Type-site occupation begins 5205-5095 cal BC at 95% probability."},
    {"id": S_CUCUTENI, "kind": "scholarly",
     "citation": "'A complex subsistence regime revealed for Cucuteni-Trypillia sites'",
     "url": "https://ekmair.ukma.edu.ua/server/api/core/bitstreams/1ef22ee0-a636-4443-a6e8-038d70b3070b/content"},
    {"id": S_NEBELIVKA, "kind": "scholarly",
     "citation": "'What was the ecological impact of a Trypillia megasite occupation?' (Nebelivka), Vegetation History and Archaeobotany",
     "url": "https://link.springer.com/article/10.1007/s00334-019-00730-9",
     "note": "c. 80 AMS dates; occupation 3980-3820 to 3870-3750 cal BCE at 95%."},
    {"id": S_MAIDANETSKE, "kind": "scholarly",
     "citation": "'Trypillia Megasites in Context: Independent Urban Development in Chalcolithic Eastern Europe', Cambridge Archaeological Journal",
     "url": "https://www.cambridge.org/core/journals/cambridge-archaeological-journal/article/trypillia-megasites-in-context-independent-urban-development-in-chalcolithic-eastern-europe/C33D85AF4EE4BA2D61AAB77D3E399E4D"},
    {"id": S_VARNA_AMS, "kind": "scholarly",
     "citation": "'AMS Dating of the Late Copper Age Varna Cemetery, Bulgaria', Radiocarbon",
     "url": "https://www.cambridge.org/core/journals/radiocarbon/article/abs/ams-dating-of-the-late-copper-age-varna-cemetery-bulgaria/706A7F638D010BB6C943FBDFC1062749",
     "note": "Cemetery use modelled to 4596-4516 through 4427-4341 cal BC at 95.4%."},
    {"id": S_VARNA_KRAUSS, "kind": "scholarly",
     "citation": "Krauss, Zauner & Pernicka, 'Statistical and Anthropological Analysis of the Varna Necropolis'",
     "url": "https://www.academia.edu/13437312/R_Krau%C3%9F_S_Z%C3%A4uner_E_Pernicka_Statistical_and_Anthropological_Analysis_of_the_Varna_Necropolis",
     "note": "States the AMS chronology runs c. 200 years younger than the traditional one."},
    {"id": S_TRB_SWEDEN, "kind": "scholarly",
     "citation": "'The Early Funnel Beaker Culture in Southern Sweden and Central Europe', Lund University",
     "url": "https://journals.lub.lu.se/lar/article/download/21767/19601/53159",
     "note": "Earliest southern Swedish TRB c. 3950-3900 cal BC, centuries after the central European core."},
    {"id": S_TRB_UKRAINE, "kind": "scholarly",
     "citation": "'Chronology of the Funnel Beaker Culture Settlement in Western Ukraine in the Context of Radiocarbon Dating'",
     "url": "https://www.academia.edu/42194690/Chronology_of_the_Funnel_Beaker_Culture_Settlement_in_Western_Ukraine_in_the_Context_of_Radiocarbon_Dating"},
    {"id": S_MICHELSBERG_DNA, "kind": "scholarly",
     "citation": "'Multi-scale ancient DNA analyses confirm the western origin of Michelsberg farmers', PLOS ONE",
     "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0179742"},
    {"id": S_MICHELSBERG_PHASES, "kind": "scholarly",
     "citation": "Germania (Heidelberg University), Michelsberg phase chronology for Hesse",
     "url": "https://journals.ub.uni-heidelberg.de/index.php/germania/libraryFiles/downloadPublic/763"},
    {"id": S_SKARA_BRAE, "kind": "institutional",
     "citation": "'Skara Brae - the date and extent of the settlement', Ness of Brodgar research project",
     "url": "https://www.nessofbrodgar.co.uk/skarabrae-date-and-extent/",
     "note": "2017 re-evaluation: occupied c. 3300 BC, largely abandoned after 2900, re-occupied 2800-2700, ended c. 2500."},
    {"id": S_BRODGAR, "kind": "scholarly",
     "citation": "'To cut a long story short: formal chronological modelling for the Ness of Brodgar', Cardiff University repository",
     "url": "https://orca.cardiff.ac.uk/id/eprint/96028/1/Ness_paper_text%20v18%20Resubmitted%20(002).pdf",
     "note": "65 measurements; main activity begins 3060-2950 cal BC at 95%."},
    {"id": S_NEWGRANGE, "kind": "scholarly",
     "citation": "'Pigs, pannage, and the solstice: isotopic insights from prehistoric feasting at Newgrange', Proceedings of the Prehistoric Society",
     "url": "https://www.cambridge.org/core/journals/proceedings-of-the-prehistoric-society/article/pigs-pannage-and-the-solstice-isotopic-insights-from-prehistoric-feasting-at-newgrange/ECC3D799B42C21FAA0EDF3045C230F33"},
    {"id": S_NEWGRANGE_CAL, "kind": "reference",
     "citation": "Newgrange.com institutional history, on the uncalibrated-versus-calibrated date confusion",
     "url": "https://www.newgrange.com/newgrange-archaeology-book.htm",
     "note": "Explains why the widely quoted 'c. 2500 bc' is a lab age, not a calendar date."},
    {"id": S_HAAK_2015, "kind": "scholarly",
     "citation": "Haak et al. (2015), 'Massive migration from the steppe was a source for Indo-European languages in Europe', Nature",
     "url": "https://www.nature.com/articles/nature14317",
     "note": "Corded Ware individuals derive c. 75% of their ancestry from Yamnaya."},
    {"id": S_ADMIXTURE_2022, "kind": "scholarly",
     "citation": "'The spatiotemporal patterns of major human admixture events during the European Holocene' (2022)",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9293011/"},
    {"id": S_BEAKER_2026, "kind": "scholarly",
     "citation": "'Lasting Lower Rhine-Meuse forager ancestry shaped Bell Beaker expansion' (2026)",
     "url": "https://research.vu.nl/en/publications/lasting-lower-rhine-meuse-forager-ancestry-shaped-bell-beaker-exp/",
     "note": "70-100% replacement across most of Europe, but a wetland refuge retained c. 50% forager ancestry."},
]

CHECKED = "2026-08-08"
C14 = "radiocarbon-calibrated"


def extend(E, entities):
    _, P, ERA, EVENT, _, FIRST = make_builders(E)
    pre = "europe.prehistory"

    # ---- Mesolithic --------------------------------------------------------
    P("azilian", "Azilian", pre, bp(14900), bp(12200), "specialist",
      summary="The first post-glacial culture of southwest France and northern Spain, with "
              "flat harpoons and painted pebbles.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="French Early Azilian dates cluster at 14,900-12,200 cal BP. Most of it "
                "precedes the Mesolithic proper; the end shown is where the dated series "
                "stops, not a sharp boundary with the Sauveterrian, which the sources "
                "describe only qualitatively.",
      source_ids=[S_AZILIAN])

    P("maglemose", "Maglemosian", pre, bp(11600), bp(8400), "intermediate",
      summary="The founding culture of the northern European Mesolithic, working bone and "
              "antler in the forests and wetlands left by the retreating ice.",
      aliases=["Maglemose culture"],
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="A 2020 AMS study of bone-point series splits this into Early and Late "
                "Maglemose complexes either side of a hiatus of roughly 600 years at c. "
                "10,300 cal BP — older accounts treat it as one uniform culture.",
      source_ids=[S_MAGLEMOSE_BONE, S_LUNDBY])

    P("sauveterrian", "Sauveterrian", pre, -9740, -6771, "specialist",
      summary="A narrow-blade microlithic tradition of France, Italy and Iberia, the southern "
              "counterpart to the Maglemosian.",
      start_dating_method=C14, end_dating_method=C14, standing="minority",
      date_precision="disputed", as_of=CHECKED,
      date_note="REGIONAL, NOT PAN-EUROPEAN. The dates shown are the Bayesian-modelled Italian "
                "sequence at Romagnano. Older French typological dating puts the Sauveterrian "
                "roughly a millennium later. The two have not been reconciled and are not "
                "averaged here; no single European range is defensible.",
      alternatives=[{
          "label": "French typological chronology", "standing": "minority",
          "dating_method": "typological",
          "note": "Places the Sauveterrian around a millennium later than the Italian AMS series.",
          "source_ids": [S_ROMAGNANO]}],
      source_ids=[S_ROMAGNANO])

    P("star-carr", "Star Carr", pre, -9335, -8440, "intermediate",
      summary="A waterlogged Yorkshire site preserving the earliest known built structures in "
              "Britain, along with antler headdresses.",
      start_dating_method=C14, end_dating_method=C14, standing="consensus",
      date_note="Occupation 9335-9275 to 8525-8440 cal BC on Bayesian-modelled AMS dates. "
                "Popular accounts still quote the uncalibrated 1950s figures from Clark's "
                "original excavation.",
      source_ids=[S_STARCARR])

    P("lepenski-vir", "Lepenski Vir", pre, -9900, -5660, "intermediate",
      summary="A Danube Gorges site of trapezoidal houses and carved boulder sculptures, "
              "occupied across the transition to farming.",
      start_dating_method=C14, end_dating_method=C14, standing="consensus",
      date_note="Bayesian modelling of 111 AMS dates gives occupation from 9900-9280 cal BC. "
                "The Mesolithic phase ends 7480-6860 cal BC, then the site is EMPTY for at "
                "least 700 years. The famous trapezoidal buildings and sculptures belong to a "
                "brief later phase, 6170-6070 to 6010-5940 cal BC.",
      alternatives=[{
          "label": "Srejovic's original stratigraphy", "standing": "superseded",
          "dating_method": "typological",
          "note": "The 1969/1972 sequence was continuous and shorter, with no hiatus.",
          "source_ids": [S_LEPENSKI]}],
      source_ids=[S_LEPENSKI])

    P("kongemose", "Kongemose Culture", pre, -6500, -5400, "specialist",
      summary="The middle Mesolithic of southern Scandinavia, between the Maglemosian and the "
              "Ertebolle, turning increasingly to the coast.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Sources vary by several centuries, largely because uncalibrated BP and "
                "calendar BC figures are quoted interchangeably in the secondary literature.",
      source_ids=[S_NWPOLAND_C14])

    P("doggerland-inundation", "The Drowning of Doggerland", pre, bp(10243), bp(7200),
      "foundational",
      summary="The slow submergence of the land connecting Britain to the continent, which "
              "displaced Mesolithic populations and finally made Britain an island.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="A 2026 sediment-core study dates the freshwater-to-marine transition to "
                "10,243-10,199 years ago; the Lost Frontiers cores put final inundation "
                "between 8,200 and 7,200 BP. An active Groningen project states plainly that "
                "the accuracy of several Doggerland radiocarbon dates is in question, so this "
                "is a working chronology rather than a settled one.",
      caveats=[{"kind": "misconception",
                "text": "Doggerland was not destroyed by a tsunami. It drowned gradually over "
                        "three millennia; the Storegga wave was one damaging episode part-way "
                        "through, not the end of it.",
                "source_ids": [S_DOGGERLAND_2026, S_LOST_FRONTIERS]}],
      source_ids=[S_DOGGERLAND_2026, S_LOST_FRONTIERS])

    EVENT("storegga", "Storegga Slide Tsunami", pre, bp(8140), bp(8140), "intermediate",
          summary="One of the largest known Holocene tsunamis, generated by a submarine "
                  "landslide off Norway and striking what remained of Doggerland.",
          start_dating_method=C14, end_dating_method=C14, standing="consensus",
          date_precision="approx",
          date_note="8,140 +/- 55 cal BP on AMS dates from moss killed by the wave, "
                    "recalibrated in 2024 against IntCal20 and Marine20. It falls within the "
                    "coldest decades of the 8.2 ka climate event — and the same study shows "
                    "the slide reworked the sediments from which that event was reconstructed.",
          source_ids=[S_STOREGGA, S_WENINGER_STOREGGA])

    P("ertebolle", "Ertebolle Culture", pre, -5400, -4000, "intermediate",
      summary="Complex coastal foragers of southern Scandinavia who made pottery, built shell "
              "middens, and kept farming at arm's length for centuries.",
      aliases=["Ertebølle"],
      start_dating_method=C14, end_dating_method=C14, standing="consensus",
      date_note="Persists to c. 4000 cal BC, long after the Linear Pottery Culture had ended "
                "further south. The Mesolithic-Neolithic frontier in this region held for "
                "centuries rather than moving as a front.",
      source_ids=[S_ERTEBOLLE])

    # ---- Farming's arrival -------------------------------------------------
    P("franchthi", "Franchthi Cave", pre, bp(38000), bp(6000), "intermediate",
      summary="A cave in the Argolid occupied continuously from the Upper Palaeolithic to the "
              "end of the Neolithic — and an argument that farming reached Greece by sea.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="AMS dates on domesticated seeds put cereal cultivation here in the first half "
                "of the 7th millennium cal BC, EARLIER than northern Greece or Bulgaria. That "
                "ordering is backwards for a single overland front and points to a separate "
                "maritime route into the southern Aegean.",
      source_ids=[S_FRANCHTHI])

    P("sesklo", "Sesklo", pre, -6500, None, "specialist",
      summary="A Thessalian tell settlement, type-site for the Greek Neolithic sequence and "
              "among the earliest farming villages in Europe.",
      start_dating_method=C14, end_precision="unknown", standing="majority",
      date_note="Recalibration moved the Thessalian Neolithic start from an older c. 7000 cal "
                "BC to 6700-6500 cal BC. No end date is asserted here: the fetched sources "
                "give the start rigorously and the end only through figures that trace back to "
                "tertiary summaries.",
      alternatives=[{
          "label": "Older c. 7000 cal BC chronology", "standing": "superseded",
          "start_year": -7000, "dating_method": C14,
          "note": "Pre-recalibration figure, still widely repeated.",
          "source_ids": [S_GREEK_NEOLITHIC]}],
      source_ids=[S_GREEK_NEOLITHIC])

    P("starcevo", "Starcevo-Koros-Cris", pre, -6200, -5300, "intermediate",
      summary="The founding Neolithic complex of the Balkans and Carpathian Basin, ancestral "
              "to both the Linear Pottery Culture and Vinca.",
      aliases=["Starčevo–Körös–Criș", "Starcevo culture"],
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Culture-wide dates run 6200-5300 cal BC, but Bayesian modelling of individual "
                "sites gives much narrower and later windows — Alsonyek in Hungary begins only "
                "5775-5740 cal BC. That spread is real regional variation in when farming "
                "arrived, not disagreement about the same event.",
      source_ids=[S_STARCEVO, S_SKC_RANGE])

    P("cardial", "Cardial and Impressed Ware", pre, -5800, None, "intermediate",
      summary="The Mediterranean route: farming carried west by sea along the northern "
              "Mediterranean coast, from Liguria to Portugal.",
      aliases=["Cardium Pottery", "Impressed Ware"],
      start_dating_method=C14, end_precision="unknown", standing="consensus",
      date_note="Using only short-lived samples — an explicit guard against old-wood bias — "
                "the full Neolithic package appears at c. 5800 cal BC in Liguria, 5600 in "
                "Valencia and 5400 in central Portugal. Roughly 2,000 km in about six "
                "generations. No end is asserted; the dated horizon is the arrival.",
      source_ids=[S_ZILHAO_2001])

    ERA("neolithic-routes", "The Two Routes of Neolithic Spread", pre, -6500, -4000,
        "foundational",
        summary="Farming crossed Europe by an inland Danubian route and a Mediterranean sea "
                "route, at different speeds and with different outcomes.",
        start_dating_method=C14, end_dating_method=C14, standing="majority",
        date_precision="approx",
        date_note="Simulation against haplogroup clines gives the inland route c. 50 km per "
                  "generation and the coastal route c. 70 km. The rate of interbreeding with "
                  "foragers was near-identical on both, at roughly 3.6% of farmers — but the "
                  "sea route was longer, so more admixture events accumulated, which is why "
                  "Iberia ends up with more forager ancestry than northern France.",
        caveats=[{"kind": "misconception",
                  "text": "Not one wave of advance. Two routes, different speeds, and "
                          "different demographic outcomes at their far ends.",
                  "source_ids": [S_FORT_2024, S_ZILHAO_2001]}],
        source_ids=[S_FORT_2024, S_ZILHAO_2001])

    P("vinca", "Vinca Culture", pre, -5400, -4600, "intermediate",
      summary="The major Late Neolithic culture of the central Balkans, with large tell "
              "settlements and some of Europe's earliest copper metallurgy.",
      aliases=["Vinča culture"],
      start_dating_method=C14, end_dating_method=C14, standing="consensus",
      date_note="Unusually well replicated: three independent radiocarbon datasets of 76, 155 "
                "and 600 dates converge on the same phase boundaries. The type-site itself "
                "begins 5205-5095 cal BC at 95% probability.",
      source_ids=[S_VINCA, S_VINCA_BAYES])

    P("michelsberg", "Michelsberg Culture", pre, -4400, -3500, "specialist",
      summary="Causewayed enclosures and flint mines across the Rhineland, the Paris Basin and "
              "the Low Countries.",
      start_dating_method=C14, end_dating_method=C14, standing="consensus",
      date_note="Sub-phases run c. 4340/4200-3960, 3950-3800/3700 and 3800/3700-3500 cal BC.",
      source_ids=[S_MICHELSBERG_DNA, S_MICHELSBERG_PHASES])

    P("varna", "Varna Necropolis", pre, -4596, -4341, "foundational",
      summary="A Black Sea cemetery holding the oldest worked gold known anywhere, and the "
              "earliest clear evidence of concentrated wealth in Europe.",
      start_dating_method=C14, end_dating_method=C14, standing="consensus",
      date_note="AMS Bayesian modelling gives 4596-4516 to 4427-4341 cal BC at 95.4%, a use "
                "life of only 120-260 years.",
      alternatives=[{
          "label": "Traditional pre-AMS chronology", "standing": "superseded",
          "start_year": -4600, "end_year": -4200, "dating_method": C14,
          "note": "About 200 years older than the AMS result, and still the figure most "
                  "popular sources give.",
          "source_ids": [S_VARNA_KRAUSS]}],
      source_ids=[S_VARNA_AMS, S_VARNA_KRAUSS])

    P("cucuteni-trypillia", "Cucuteni-Trypillia", pre, -5050, -3000, "intermediate",
      summary="The great Chalcolithic farming culture of Romania, Moldova and Ukraine, which "
              "built the largest settlements in the prehistoric world.",
      aliases=["Cucuteni–Trypillia", "Tripolye culture"],
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      source_ids=[S_CUCUTENI])

    P("trypillia-megasites", "Trypillia Mega-Sites", "europe.prehistory.cucuteni-trypillia",
      -4300, -3650, "foundational",
      summary="Settlements of up to 320 hectares and perhaps 15,000 people, laid out in "
              "concentric rings with no palace, citadel or centre.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Nebelivka is modelled on c. 80 AMS dates to 3980-3820 through 3870-3750 cal "
                "BCE; Maidanetske to 3990-3640 cal BCE. How long any one mega-site was "
                "occupied is actively disputed — estimates run from under a century to more "
                "than two.",
      caveats=[{"kind": "misconception",
                "text": "Among the largest settlements on Earth at the time, and they show no "
                        "sign of centralised hierarchy — urban scale without a ruling centre.",
                "source_ids": [S_MAIDANETSKE]}],
      source_ids=[S_NEBELIVKA, S_MAIDANETSKE])

    P("funnelbeaker", "Funnelbeaker Culture", pre, -4300, -2800, "intermediate",
      summary="The farming culture of north-central Europe that built the megalithic tombs, "
              "and the last before Corded Ware.",
      aliases=["TRB", "Trichterbecherkultur"],
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Arrival is strongly diachronic: c. 4300 cal BC in the central European core "
                "but not before c. 3950 cal BC in southern Sweden, and 3700/3600 cal BC in "
                "western Ukraine.",
      source_ids=[S_TRB_SWEDEN, S_TRB_UKRAINE])

    P("newgrange", "Newgrange", pre, -3300, -2700, "foundational",
      summary="An Irish passage tomb built to admit the winter solstice sunrise, older than "
              "Stonehenge's standing stones and older than the pyramids.",
      aliases=["Brú na Bóinne"],
      start_dating_method=C14, end_dating_method=C14, standing="consensus",
      date_note="Construction and primary use c. 3300-3000 cal BC, with deposition inside "
                "continuing to c. 2700 cal BC.",
      caveats=[{"kind": "misconception",
                "text": "The often-quoted 'c. 2500 BC' is an uncalibrated laboratory age, not "
                        "a calendar date. Calibrated, it is c. 3200 BC — a difference of "
                        "600-700 years.",
                "source_ids": [S_NEWGRANGE_CAL]}],
      source_ids=[S_NEWGRANGE, S_NEWGRANGE_CAL])

    P("skara-brae", "Skara Brae", pre, -3300, -2500, "foundational",
      summary="The best-preserved Neolithic village in Europe, its stone furniture still "
              "standing in the houses.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="A 2017 re-evaluation puts first occupation at c. 3300 BC, most surviving "
                "buildings at c. 2900 BC, re-occupation at 2800-2700 BC and abandonment at c. "
                "2500 BC.",
      caveats=[{"kind": "misconception",
                "text": "Not continuously inhabited for 600 years. The re-dating found the "
                        "village was largely abandoned and later re-occupied.",
                "source_ids": [S_SKARA_BRAE]}],
      source_ids=[S_SKARA_BRAE])

    P("ness-of-brodgar", "Ness of Brodgar", pre, -3060, -2500, "intermediate",
      summary="A monumental Orkney complex between two stone circles, with buildings larger "
              "than anything else known in Neolithic northwest Europe.",
      start_dating_method=C14, end_dating_method=C14, standing="consensus",
      date_note="Bayesian modelling of 65 measurements gives 3060-2950 cal BC for the main "
                "phase; the hearth in Structure Ten was last used c. 2500 cal BC. Popular "
                "accounts round the start to 3200 BC.",
      source_ids=[S_BRODGAR])

    # ---- The genetic turnover ----------------------------------------------
    ERA("farmer-turnover", "The Anatolian Farmer Turnover", pre, -6500, -4000, "foundational",
        summary="Farming spread into Europe substantially as people, not as ideas: incoming "
                "Anatolian-descended farmers replaced most of the resident forager ancestry.",
        start_dating_method=C14, end_dating_method=C14, standing="consensus",
        date_precision="approx",
        date_note="Anatolian-farmer ancestry is widespread from c. 6400 BCE and present almost "
                  "everywhere in continental Europe and the British Isles by c. 4300 BCE. "
                  "Between 6500 and 4000 BCE it replaced 70-100% of local forager ancestry "
                  "across most of the continent.",
        caveats=[{"kind": "misconception",
                  "text": "Europeans are not mostly Mesolithic foragers who took up farming. "
                          "Pre-2015 cultural-diffusion accounts are substantially wrong: the "
                          "dominant mechanism was demographic replacement.",
                  "source_ids": [S_HAAK_2015, S_ADMIXTURE_2022]},
                 {"kind": "contested-existence",
                  "text": "Replacement was uneven. Wetlands of the Netherlands, Belgium and "
                          "western Germany kept about half their forager ancestry for some "
                          "three thousand years longer than the rest of Europe.",
                  "source_ids": [S_BEAKER_2026]}],
        source_ids=[S_HAAK_2015, S_ADMIXTURE_2022, S_BEAKER_2026])

    EVENT("steppe-influx", "The Steppe Ancestry Influx", pre, -3000, -2900, "foundational",
          summary="A second large population movement, out of the Pontic-Caspian steppe, which "
                  "reshaped northern Europe and is widely tied to the arrival of "
                  "Indo-European languages.",
          start_dating_method=C14, end_dating_method=C14, standing="majority",
          date_precision="approx",
          date_note="Corded Ware individuals in Germany derive roughly 75% of their ancestry "
                    "from Yamnaya-related steppe populations. The admixed population forms "
                    "rapidly, within c. 3000-2900 BCE, across widely separated regions, and "
                    "the ancestry persists in central Europe for at least two millennia.",
          source_ids=[S_HAAK_2015, S_ADMIXTURE_2022])
