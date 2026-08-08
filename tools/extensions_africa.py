"""African prehistory depth.

Africa held 8 prehistory nodes against Europe's 11, for the continent where
roughly 3.0 of the app's 3.3 million years happened. That imbalance is not
neutral: the dataset already carries a `misconception` caveat warning readers
that figurative art did not begin in Europe, while the node counts quietly
implied the opposite. This module closes that gap.

Sourcing
--------
Every numeric date here traces to a source in the registry with a real URL, per
the rule the regional-prehistory pass set. Where the research could not confirm
a figure from a primary source, no entity claims it -- the site is authored
with the boundary it can defend, or the number is carried as an `alternative`
rather than promoted to the main claim.

Two intended entities were dropped on contact with the tree: Nabta Playa and the
African Humid Period (as "Green Sahara") already existed, authored with their
own sources. They are left untouched rather than overwritten. The cattle
misconception the research turned up for Nabta Playa is carried on the cattle
threshold below instead, where it belongs.

Placement
---------
New nodes are flat `period` children of `africa.prehistory`, matching the five
that already live there. Introducing sub-regional era groupings would re-parent
existing entities, which is a tree change rather than added depth, and was
explicitly out of scope for this pass.

Disputes
--------
Three entries are genuinely unresolved in the literature and are authored as
`contested` with both chronologies carried as alternatives rather than one
being silently chosen: Sterkfontein (cosmogenic ~3.4-3.7 Ma vs U-Pb ~2.0-2.6 Ma,
a gap of over a million years), Melka Kunture (whether the earliest Acheulean
is ~1.95 Ma), and Ishango (three incompatible figures). These carry `as_of` so
a reader can tell when the dispute was last checked.
"""

from builders import make_builders
from extensions_prehistory import bp, ka, ma

# --- Sources added by this pass, by id --------------------------------------
S_MCDOUGALL = "mcdougall-1985-koobi-fora"
S_BROWN_1985 = "brown-1985-turkana-boy"
S_GRANGER_2015 = "granger-2015-sterkfontein"
S_GRANGER_2022 = "granger-2022-sterkfontein-m4"
S_PICKERING_2020 = "pickering-2020-sterkfontein-m4"
S_WALKER_2006 = "walker-2006-stw573-upb"
S_KUMAN_2021 = "kuman-2021-swartkrans"
S_GRANGER_2014_SK = "granger-2014-swartkrans"
S_DIRKS_2017 = "dirks-2017-rising-star"
S_IHO_LUCY = "iho-asu-lucy"
S_MASAO_2016 = "masao-2016-laetoli"
S_RICHTER_2017 = "richter-2017-jebel-irhoud"
S_HUBLIN_2017 = "hublin-2017-jebel-irhoud"
S_BERKELEY_HERTO = "berkeley-2003-herto"
S_GRUN_2020 = "grun-2020-kabwe"
S_CLARK_1994_BODO = "clark-1994-bodo"
S_SEMAW_1997 = "semaw-1997-gona"
S_SEMAW_2003 = "semaw-2003-gona-ogs"
S_PERINI_2023 = "perini-2023-melka-kunture"
S_MELKA_SKEPTIC = "melka-kunture-age-model-critique"
S_MORGAN_2012 = "morgan-2012-melka-kunture"
S_DEINO_2018 = "deino-2018-olorgesailie"
S_BARHAM_2023 = "barham-2023-kalambo"
S_JACOBS_SIBUDU = "jacobs-2008-sibudu-post-hp"
S_PP_2025 = "asu-2025-pinnacle-point"
S_PP_2017 = "pinnacle-point-2017-chronology"
S_TEXIER_2010 = "texier-2010-diepkloof"
S_RIFKIN_2015 = "rifkin-2015-apollo-11"
S_AMBROSE_EYM = "ambrose-enkapune-ya-muto"
S_BARTON_2013 = "barton-2013-taforalt"
S_VANDELOOSDRECHT_2018 = "vandeloosdrecht-2018-taforalt"
S_WENDORF_1984 = "wendorf-1984-kubbaniya-cereals"
S_ISHANGO_HIST = "ishango-dating-history"
S_GOBERO_2026 = "gobero-2026-dental"
S_LINSEELE_2014 = "linseele-2014-fayum"
S_FAYUM_LAKE = "fayum-lake-core-cereal"
S_ESH_SHAHEINAB = "esh-shaheinab-2024"
S_JACKES_LUBELL = "jackes-lubell-capsian"
S_BRASS_2017_CATTLE = "brass-2017-cattle-reassessment"
S_EDINBURGH_CATTLE = "edinburgh-african-cattle-genome"
S_MANNING_MILLET = "manning-pearl-millet"
S_WINCHELL_SORGHUM = "winchell-sorghum"
S_OUP_BANTU = "oup-bantu-expansion"
S_CAMBRIDGE_BANTU = "cambridge-2023-bantu"
S_OUP_NOK = "oup-nok-culture"
S_TARUGA_FURNACES = "taruga-furnace-dates"

AFRICA_SOURCES = [
    {"id": "shanahan-2012-ahp", "kind": "scholarly",
     "citation": "Shanahan, McKay, Hughen et al., 'The time-transgressive termination of the African Humid Period', Nature Geoscience",
     "url": "https://www.whoi.edu/cms/files/shanahan12nat_220305.pdf",
     "note": "About 14,800 to 5,500 years ago; termination explicitly time-transgressive."},
    {"id": "noaa-ahp-summary", "kind": "institutional",
     "citation": "NOAA National Centers for Environmental Information, 'End of the African Humid Period' (2021)",
     "url": "https://www.ncei.noaa.gov/sites/default/files/2021-11/5%20End%20of%20the%20Africian%20Humid%20Period%20-Final_OCT%202021.pdf"},
    {"id": "malville-nabta-playa", "kind": "scholarly",
     "citation": "Malville et al., 'Astronomy at Nabta Playa, Egypt'",
     "url": "https://sci-hub.se/tree/0d/9d/0d9d5f6a6886bcdabc6a0d081c704ab0.pdf",
     "note": "Phase structure reported as raw radiocarbon BP: Middle Neolithic 8,100-7,600, Late 7,400-6,600, Terminal 6,600-5,400."},
    {"id": S_MCDOUGALL, "kind": "scholarly",
     "citation": "McDougall (1985), 'K-Ar and 40Ar/39Ar dating of the hominid-bearing Pliocene-Pleistocene sequence at Koobi Fora, Lake Turkana, northern Kenya', GSA Bulletin 96(2):159",
     "url": "https://pubs.geoscienceworld.org/gsa/gsabulletin/article-abstract/96/2/159/191263/K-Ar-and-40Ar-39Ar-dating-of-the-hominid-bearing",
     "note": "Tuff framework: Moiti 4.10+/-0.07 Ma, KBS 1.88+/-0.02 Ma, Silbo 0.74+/-0.01 Ma."},
    {"id": S_BROWN_1985, "kind": "scholarly",
     "citation": "Brown, Harris, Leakey & Walker (1985), 'Early Homo erectus skeleton from west Lake Turkana, Kenya', Nature 316:788-792",
     "url": "https://doi.org/10.1038/316788a0"},
    {"id": S_GRANGER_2015, "kind": "scholarly",
     "citation": "Granger, Gibbon, Kuman, Clarke, Bruxelles & Caffee (2015), 'New cosmogenic burial ages for Sterkfontein Member 2 Australopithecus and Member 5 Oldowan', Nature 522:85-88",
     "url": "https://pubmed.ncbi.nlm.nih.gov/25830884/",
     "note": "Little Foot 3.67+/-0.16 Ma by 26Al/10Be isochron burial dating."},
    {"id": S_GRANGER_2022, "kind": "scholarly",
     "citation": "Granger et al. (2022), cosmogenic dating of Sterkfontein Member 4, PNAS",
     "url": "https://pubmed.ncbi.nlm.nih.gov/35759668/",
     "note": "Member 4 at 3.41-3.49 Ma; Jacovec Cavern 3.61+/-0.09 Ma."},
    {"id": S_PICKERING_2020, "kind": "scholarly",
     "citation": "Pickering & Herries (2020), 'A new multidisciplinary age of 2.61-2.07 Ma for the Sterkfontein Member 4 australopiths'",
     "url": "https://opal.latrobe.edu.au/articles/chapter/A_new_multidisciplinary_age_of_2_61_2_07_Ma_for_the_Sterkfontein_Member_4_australopiths/28432415",
     "note": "Competing chronology: U-Pb, ESR and palaeomagnetism combined."},
    {"id": S_WALKER_2006, "kind": "scholarly",
     "citation": "Walker, Pickering & Kramers, 'U-Pb Isotopic Age of the StW 573 Hominid from Sterkfontein, South Africa', Science",
     "url": "https://www.science.org/doi/10.1126/science.1132916",
     "note": "Competing U-Pb flowstone ages of 2.17+/-0.17 Ma for Little Foot."},
    {"id": S_KUMAN_2021, "kind": "scholarly",
     "citation": "Kuman et al. (2021), 'A new absolute date from Swartkrans Cave for the oldest occurrences of Paranthropus robustus and Oldowan stone tools in South Africa'",
     "url": "https://pubmed.ncbi.nlm.nih.gov/34020297/"},
    {"id": S_GRANGER_2014_SK, "kind": "scholarly",
     "citation": "Granger et al. (2014), 'Cosmogenic nuclide burial dating of hominin-bearing Pleistocene cave deposits at Swartkrans, South Africa', Quaternary Geochronology 24:10",
     "url": "https://ui.adsabs.harvard.edu/abs/2014QuGeo..24...10G/abstract"},
    {"id": S_DIRKS_2017, "kind": "scholarly",
     "citation": "Dirks, Roberts, Hilbert-Wolf et al. (2017), 'The age of Homo naledi and associated sediments in the Rising Star Cave, South Africa', eLife 6:e24231",
     "url": "https://elifesciences.org/articles/24231"},
    {"id": S_IHO_LUCY, "kind": "institutional",
     "citation": "Institute of Human Origins, Arizona State University, 'About Lucy'",
     "url": "https://iho.asu.edu/aboutLucy",
     "note": "Gives 'just less than 3.18 million years'; argon-argon on Kada Hadar tuffs."},
    {"id": S_MASAO_2016, "kind": "scholarly",
     "citation": "Masao et al. (2016), 'New footprints from Laetoli (Tanzania) provide evidence for marked body size variation in Australopithecus afarensis', eLife",
     "url": "https://elifesciences.org/articles/19568",
     "note": "3.66 Ma for Sites G and S, following the Deino (2011) recalibration."},
    {"id": S_RICHTER_2017, "kind": "scholarly",
     "citation": "Richter, Grun, Joannes-Boyau et al. (2017), 'The age of the hominin fossils from Jebel Irhoud, Morocco, and the origins of the Middle Stone Age', Nature 546:293-296",
     "url": "https://pubmed.ncbi.nlm.nih.gov/28593953/",
     "note": "315+/-34 ka by thermoluminescence on heated flints."},
    {"id": S_HUBLIN_2017, "kind": "scholarly",
     "citation": "Hublin, Ben-Ncer, Bailey et al. (2017), 'New fossils from Jebel Irhoud (Morocco) and the pan-African origin of Homo sapiens', Nature 546:289-292",
     "url": "https://doi.org/10.1038/nature22336"},
    {"id": S_BERKELEY_HERTO, "kind": "institutional",
     "citation": "UC Berkeley news release (2003) on Homo sapiens idaltu, Middle Awash, Ethiopia",
     "url": "https://newsarchive.berkeley.edu/news/media/releases/2003/06/11_idaltu.shtml",
     "note": "160-154 ka by argon-argon with tephra correlation."},
    {"id": S_GRUN_2020, "kind": "scholarly",
     "citation": "Grun, Pomeroy, Stringer et al. (2020), 'Dating the skull from Broken Hill, Zambia, and its position in human evolution', Nature 580:372-375",
     "url": "https://pubmed.ncbi.nlm.nih.gov/32296179/",
     "note": "299+/-25 ka, replacing the long-quoted ~500 ka figure."},
    {"id": S_CLARK_1994_BODO, "kind": "scholarly",
     "citation": "Clark, de Heinzelin, Schick et al. (1994), 'African Homo erectus: Old Radiometric Ages and Young Oldowan Assemblages in the Middle Awash Valley, Ethiopia', Science",
     "url": "https://www.science.org/doi/10.1126/science.8009220",
     "note": "Bodo weighted mean 0.64+/-0.03 Ma by laser-fusion 40Ar/39Ar."},
    {"id": S_SEMAW_1997, "kind": "scholarly",
     "citation": "Semaw, Renne, Harris et al. (1997), '2.5-million-year-old stone tools from Gona, Ethiopia', Nature 385:333-336",
     "url": "https://doi.org/10.1038/385333a0"},
    {"id": S_SEMAW_2003, "kind": "scholarly",
     "citation": "Semaw et al. (2003), '2.6-Million-year-old stone tools and associated bones from OGS-6 and OGS-7, Gona, Afar, Ethiopia', Journal of Human Evolution",
     "url": "https://scholarblogs.emory.edu/stoutlab/files/2013/07/Semaw-et-al-2003.pdf"},
    {"id": S_PERINI_2023, "kind": "scholarly",
     "citation": "Perini et al. (2023), 'Isotopic insights into the Early Acheulean (1.95 Ma-1.66 Ma) high-elevation paleoenvironments at Melka Kunture', Archaeological and Anthropological Sciences",
     "url": "https://link.springer.com/article/10.1007/s12520-023-01879-1",
     "note": "Claims the earliest Acheulean technocomplex, on magnetostratigraphy."},
    {"id": S_MELKA_SKEPTIC, "kind": "scholarly",
     "citation": "'Claims for 1.9-2.0 Ma old early Acheulian and Oldowan occupations at Melka Kunture are not supported by a robust age model'",
     "url": "https://ouci.dntb.gov.ua/en/works/9ZQp3Pal/",
     "note": "Directly disputes the 1.95 Ma claim."},
    {"id": S_MORGAN_2012, "kind": "scholarly",
     "citation": "Morgan et al. (2012), argon-argon chronology for Gombore II, Melka Kunture",
     "url": "https://www.melkakunture.it/biblio/download/Morgan-al-2012.pdf",
     "note": "Gombore II bracketed 0.875+/-0.010 to 0.709+/-0.013 Ma."},
    {"id": S_DEINO_2018, "kind": "scholarly",
     "citation": "Deino, Behrensmeyer, Brooks et al. (2018), 'Chronology of the Acheulean to Middle Stone Age transition in eastern Africa', Science 360",
     "url": "https://www.science.org/doi/10.1126/science.aao2216"},
    {"id": S_BARHAM_2023, "kind": "scholarly",
     "citation": "Barham, Duller, Candy et al. (2023), 'Evidence for the earliest structural use of wood at least 476,000 years ago', Nature 622:107-111",
     "url": "https://www.nature.com/articles/s41586-023-06557-9"},
    {"id": S_JACOBS_SIBUDU, "kind": "scholarly",
     "citation": "Jacobs et al., 'New ages for the post-Howieson's Poort, late and final Middle Stone Age at Sibudu Cave, South Africa', Journal of Archaeological Science 35:1790-1807",
     "url": "https://digitalcommons.usf.edu/cgi/viewcontent.cgi?article=6191&context=kip_articles",
     "note": "Post-HP 58.5+/-1.4 ka, late MSA 47.7+/-1.4 ka, final MSA 38.6+/-1.9 ka."},
    {"id": S_PP_2025, "kind": "institutional",
     "citation": "Arizona State University (2025) on the high-resolution Pinnacle Point 5-6 chronology, Quaternary Science Reviews",
     "url": "https://news.asu.edu/b/20250528-archaeologists-use-sediment-and-sunlight-date-important-site-south-african-coast"},
    {"id": S_PP_2017, "kind": "scholarly",
     "citation": "Pinnacle Point 5-6 stratigraphic chronology (2017)",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5371328/",
     "note": "Unit ages from 96+/-6 ka down to 52+/-3 ka."},
    {"id": S_TEXIER_2010, "kind": "scholarly",
     "citation": "Texier, Porraz, Parkington et al. (2010), 'A Howiesons Poort tradition of engraving ostrich eggshell containers dated to 60,000 years ago at Diepkloof Rock Shelter, South Africa', PNAS",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC2851956/"},
    {"id": S_RIFKIN_2015, "kind": "scholarly",
     "citation": "Rifkin, Dayet, Queffelec et al. (2015), Apollo 11 Cave report, South African Archaeological Bulletin",
     "url": "https://rhinoresourcecenter.com/wp-content/uploads/2026/01/Rifkinetal.2015Apollo11SAABReportfinalsmall.pdf",
     "note": "AMS 29.0+/-0.4 ka BP and OSL 29.4+/-1.4 ka; calibration basis not stated."},
    {"id": S_AMBROSE_EYM, "kind": "institutional",
     "citation": "University of Illinois release on Ambrose's Enkapune Ya Muto ostrich-eggshell beads",
     "url": "https://www.eurekalert.org/news-releases/1016533",
     "note": "Beads radiocarbon-dated to about 40,000 years; blade industry at least 46,000."},
    {"id": S_BARTON_2013, "kind": "scholarly",
     "citation": "Barton, Bouzouggar, Hogue, Lee, Collcutt & Ditchfield (2013), 'Origins of the Iberomaurusian in NW Africa: new AMS radiocarbon dating of the Middle and Later Stone Age deposits at Taforalt Cave, Morocco', Journal of Human Evolution 65(3):266-281",
     "url": "https://pubmed.ncbi.nlm.nih.gov/23891007/"},
    {"id": S_VANDELOOSDRECHT_2018, "kind": "scholarly",
     "citation": "van de Loosdrecht et al. (2018), supplementary material, 'Pleistocene North African genomes link Near Eastern and sub-Saharan African human populations', Science",
     "url": "https://www.science.org/action/downloadSupplement?doi=10.1126/science.aar8380&file=aar8380_vandeloosdrecht_sm.pdf",
     "note": "Seven directly dated Taforalt burials, 15,077 to 13,892 cal BP."},
    {"id": S_WENDORF_1984, "kind": "scholarly",
     "citation": "Wendorf, Schild, Close et al. (1984), 'New radiocarbon dates on the cereals from Wadi Kubbaniya', Science 225(4662):645-646",
     "url": "https://pubmed.ncbi.nlm.nih.gov/17729851/",
     "note": "Showed the celebrated cereal remains were modern contaminants."},
    {"id": S_ISHANGO_HIST, "kind": "scholarly",
     "citation": "Historical review of Ishango dating, noting volcanic disruption of the local carbon reservoir and absence of charcoal for cross-checking",
     "url": "https://www.bibnum.education.fr/sites/default/files/64-ishango-answer.pdf",
     "note": "Records a third figure of about 22,000 years, attributed to Alison Brooks."},
    {"id": S_GOBERO_2026, "kind": "scholarly",
     "citation": "Early to Middle Holocene hunter-fisher-gatherers from the Green Sahara (Gobero, Niger): dental evidence for regional African affinities",
     "url": "https://researchonline.ljmu.ac.uk/id/eprint/28668/7/Early%20to%20Middle%20Holocene%20Hunter%E2%80%90Fisher%E2%80%90Gatherers%20From%20the%20Green%20Sahara%20(Gobero,%20Niger)%20Dental%20Evidence%20for%20Regional%20African%20Affinities.pdf",
     "note": "Kiffian 9.6-7.4 kBP, Tenerian 6.6-4.8 kBP, recalibrated to IntCal20."},
    {"id": S_LINSEELE_2014, "kind": "scholarly",
     "citation": "Linseele, Marinova, Van Neer & Vermeersch (2014), 'New Archaeozoological Data from the Fayum Neolithic with a Critical Assessment of the Evidence for Early Stock Keeping in Egypt', PLOS ONE",
     "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0108517"},
    {"id": S_FAYUM_LAKE, "kind": "scholarly",
     "citation": "'Earliest cereal cultivation in Egypt recorded in the Faiyum Oasis lake sediments', Geological Quarterly",
     "url": "https://gq.pgi.gov.pl/article/view/33599",
     "note": "About 7.8 cal ka BP from laminated lake sediment, radiocarbon and pollen."},
    {"id": S_ESH_SHAHEINAB, "kind": "scholarly",
     "citation": "'Esh-Shaheinab: the archetype of the Sudanese Neolithic' (2024)",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11527226/",
     "note": "Early Khartoum dated 8800-8500 to 5000 BCE; Khartoum Neolithic 5,720-5,550 uncal BP."},
    {"id": S_JACKES_LUBELL, "kind": "scholarly",
     "citation": "Jackes & Lubell, Capsian chronology, Journal of African Archaeology",
     "url": "http://www.arts.uwaterloo.ca/~mkjackes/JASR%203a7.pdf",
     "note": "Capsian dated between about 10,000 and 6,000 cal BP."},
    {"id": S_BRASS_2017_CATTLE, "kind": "scholarly",
     "citation": "'Early North African Cattle Domestication and Its Ecological Setting: A Reassessment' (2017), Journal of World Prehistory",
     "url": "https://link.springer.com/article/10.1007/s10963-017-9112-9",
     "note": "Argues the early Holocene Bos at Nabta Playa were hunted aurochs, not domesticates."},
    {"id": S_EDINBURGH_CATTLE, "kind": "scholarly",
     "citation": "'The mosaic genome of indigenous African cattle as a unique genetic resource for African pastoralism', University of Edinburgh",
     "url": "https://www.pure.ed.ac.uk/ws/files/172727489/The_mosaic_genome_of_indigenous_African_cattle_as_a_unique_genetic_resource_for_African_pastoralism.pdf",
     "note": "Oldest uncontroversial domestic cattle c. 5750-4550 BC at Nabta-Kiseiba."},
    {"id": S_MANNING_MILLET, "kind": "scholarly",
     "citation": "Manning & Fuller on pearl millet domestication in the Tilemsi Valley, Mali",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7937602/",
     "note": "Charred grains and ceramic impressions c. 2500-2000 BC."},
    {"id": S_WINCHELL_SORGHUM, "kind": "scholarly",
     "citation": "Winchell et al. (2017, 2018) and Beldados et al. (2018) on Butana Group sorghum, African Archaeological Review",
     "url": "https://link.springer.com/article/10.1007/s10437-018-9314-2",
     "note": "Domestication under way in eastern Sudan by the fourth millennium BC."},
    {"id": S_OUP_BANTU, "kind": "scholarly",
     "citation": "'The Bantu Expansion', Oxford Handbook chapter",
     "url": "https://academic.oup.com/edited-volume/61663/chapter/553463850",
     "note": "Proto-Bantu forms in the Grassfields between 6,000-7,000 and 4,000-5,000 years ago."},
    {"id": S_CAMBRIDGE_BANTU, "kind": "scholarly",
     "citation": "'Moving histories: Bantu language expansions, eclectic economies and mobilities' (2023), Journal of African History",
     "url": "https://www.cambridge.org/core/journals/journal-of-african-history/article/moving-histories-bantu-language-expansions-eclectic-economies-and-mobilities/F9F92F9C6A16A9633E75508E836C9C46",
     "note": "Competing synthesis: proto-Bantu forms 3000-2000 BCE."},
    {"id": S_OUP_NOK, "kind": "scholarly",
     "citation": "'The Archaeology of Nok Culture in Nigeria (2nd/1st Millennium BCE)', Oxford Handbook chapter",
     "url": "https://academic.oup.com/edited-volume/61663/chapter/553397313",
     "note": "Earliest Nok iron-smelting furnaces calibrated to about 800-550 BCE; notes the calibration plateau."},
    {"id": S_TARUGA_FURNACES, "kind": "scholarly",
     "citation": "Published radiocarbon determinations for the Taruga iron-smelting furnaces",
     "url": "http://www.diaspora.illinois.edu/news0311/news0311-5.pdf",
     "note": "Four samples spanning 920 BCE to 280 BCE."},
]

# The dispute entries carry a checked-on date, per Q-23: a date-stamped open
# dispute is useful, an undated one is a trap.
CHECKED = "2026-08-08"


def extend(E, glob):
    _, P, _, _, TAXON, FIRST = make_builders(E)
    afr = "africa.prehistory"

    # ---- Behavioural first, authored from sources already in the registry --
    #
    # The Dikika sources (McPherron 2010 and the Dominguez-Rodrigo critique)
    # have been in the registry since the prehistory pass, and the Behavioural
    # Firsts era is already dated to 3.39 Ma to accommodate this node -- but
    # the node itself was never written. This is that gap, not new research.
    FIRST("cut-marks", "Cut-Marked Bone", f"{glob}.prehistory.firsts", ma(3.39),
          tier="specialist",
          summary="Bones from Dikika, Ethiopia bearing marks read as stone-tool butchery, "
                  "roughly 800,000 years before the oldest known stone tools.",
          start_dating_method="argon-argon",
          standing="minority",
          as_of=CHECKED,
          date_note="CONTESTED, and deliberately filed as a minority claim. If the marks are "
                    "butchery they predate the oldest known knapped stone by about 90,000 years "
                    "and sit outside this app's 3.3 Ma scope floor. The competing reading is "
                    "trampling damage, which requires no tools at all.",
          alternatives=[
              {"label": "Trampling damage, not butchery", "standing": "majority",
               "note": "Marks attributed to sediment abrasion rather than stone tools.",
               "source_ids": ["dominguez-rodrigo-2010-dikika"]},
          ],
          caveats=[{"kind": "contested-existence",
                    "text": "Whether these marks were made by tools at all is unresolved; the "
                            "majority reading is trampling.",
                    "source_ids": ["dominguez-rodrigo-2010-dikika"]}],
          source_ids=["mcpherron-2010-dikika", "dominguez-rodrigo-2010-dikika"])

    FIRST("wood-structure", "Structural Use of Wood", f"{glob}.prehistory.firsts", ka(476),
          tier="intermediate",
          summary="Two interlocking notched logs from Kalambo Falls, Zambia: the oldest known "
                  "wooden structure, built before Homo sapiens appears in the record.",
          start_dating_method="luminescence",
          standing="consensus",
          date_note="Reported as at least 476+/-23 ka, by single-grain quartz OSL and "
                    "post-IR IRSL on feldspars. A floor, not an estimate.",
          caveats=[{"kind": "misconception",
                    "text": "The claim is the oldest worked wood STRUCTURE, joined and notched, "
                            "not merely the oldest worked wood.",
                    "source_ids": [S_BARHAM_2023]}],
          source_ids=[S_BARHAM_2023])

    P("laetoli", "Laetoli", afr, ma(3.66), None,
      tier="foundational",
      allow_outside_parent_dates=True,
      end_precision="unknown",
      summary="Tanzanian site preserving the oldest confirmed hominin footprints, showing "
              "upright walking 350,000 years before the first stone tools.",
      start_dating_method="argon-argon",
      standing="consensus",
      date_note="3.66 Ma follows the Deino (2011) recalibration of the tuffs. Filed as a site "
                "rather than as a behavioural first: this app gates its floor on knapping, and "
                "admitting bipedalism as a threshold would move the floor to 3.66 Ma on an "
                "anatomical trait rather than a manufacturing behaviour.",
      caveats=[{"kind": "misconception",
                "text": "Not a single small-bodied group: the Site S prints, found in 2016, "
                        "show a much larger individual at the same horizon.",
                "source_ids": [S_MASAO_2016]}],
      source_ids=[S_MASAO_2016])


    # ---- East African Rift ------------------------------------------------
    P("turkana-basin", "Turkana Basin", afr, ma(4.10), ma(0.74),
      tier="foundational",
      allow_outside_parent_dates=True,
      summary="The most continuous tuff-dated hominin sequence in East Africa, spanning "
              "Koobi Fora, Nariokotome and Kokiselei on both shores of Lake Turkana.",
      start_dating_method="argon-argon", end_dating_method="argon-argon",
      standing="consensus",
      date_note="Bracketed by dated tuffs: Moiti 4.10+/-0.07 Ma at the base, Silbo "
                "0.74+/-0.01 Ma at the top, with KBS at 1.88+/-0.02 Ma between them.",
      notable_figures=["Turkana Boy (KNM-WT 15000), c. 1.6 Ma"],
      caveats=[{"kind": "naming-confusion",
                "text": "Not one site but a multi-locality complex with different tuff "
                        "sequences on each shore; it cannot be dated as a single horizon.",
                "source_ids": [S_MCDOUGALL]}],
      source_ids=[S_MCDOUGALL, S_BROWN_1985])

    P("hadar", "Hadar", afr, ma(3.18), None,
      tier="foundational",
      summary="The Afar site that produced AL 288-1, 'Lucy', the Australopithecus afarensis "
              "skeleton that made early bipedalism concrete.",
      start_dating_method="argon-argon",
      end_precision="unknown",
      standing="consensus",
      date_note="Argon-argon on Kada Hadar tuffs gives just under 3.18 Ma. The original "
                "1970s potassium-argon figure of about 3 Ma +/- 200,000 was affected by "
                "contaminants and is superseded.",
      caveats=[{"kind": "misconception",
                "text": "The familiar '3.2 million years' is an older rounding; the current "
                        "figure is slightly younger.",
                "source_ids": [S_IHO_LUCY]}],
      source_ids=[S_IHO_LUCY])

    P("gona", "Gona", afr, ma(2.6), ma(2.5),
      tier="intermediate",
      summary="Afar locality holding some of the oldest securely dated Oldowan stone tools, "
              "anchoring the industry's 2.6 Ma start.",
      start_dating_method="argon-argon", end_dating_method="argon-argon",
      standing="consensus",
      date_note="Single-crystal laser fusion on the overlying tuff gives 2.53+/-0.15 Ma, "
                "with the underlying Gauss-Matuyama boundary at 2.58 Ma bracketing below.",
      caveats=[{"kind": "misconception",
                "text": "No longer uniquely the oldest: Bokol Dora 1 at Ledi-Geraru dates to "
                        "2.61-2.58 Ma, so Gona is among the earliest rather than first.",
                "source_ids": ["braun-2019-bokol-dora"]}],
      source_ids=[S_SEMAW_1997, S_SEMAW_2003])

    P("melka-kunture", "Melka Kunture", afr, ma(1.7), ka(200),
      tier="specialist",
      summary="A high-altitude Ethiopian sequence running from Oldowan to Middle Stone Age, "
              "and the site of a live dispute over the world's earliest Acheulean.",
      start_dating_method="argon-argon",
      standing="majority",
      date_precision="disputed",
      as_of=CHECKED,
      date_note="The Oldowan at Garba IV is about 1.7 Ma. Whether Garba IVD holds the "
                "earliest Acheulean at 1.95 Ma is actively disputed: the claim rests on "
                "magnetostratigraphy and has been challenged as lacking a robust age model. "
                "Gombore II, later in the sequence, is securely bracketed at 0.875-0.709 Ma.",
      alternatives=[
          {"label": "Earliest Acheulean at 1.95 Ma", "standing": "minority",
           "start_year": ma(1.95), "end_year": ma(1.66), "dating_method": "magnetostratigraphy",
           "note": "Perini et al.: claimed earliest Acheulean technocomplex.",
           "source_ids": [S_PERINI_2023]},
          {"label": "Age model not robust", "standing": "majority",
           "note": "Rejects the 1.9-2.0 Ma Acheulean and Oldowan occupation claims.",
           "source_ids": [S_MELKA_SKEPTIC]},
      ],
      source_ids=[S_PERINI_2023, S_MELKA_SKEPTIC, S_MORGAN_2012])

    P("olorgesailie", "Olorgesailie", afr, ka(615), ka(305),
      tier="intermediate",
      summary="A Kenyan rift basin recording the Acheulean-to-Middle Stone Age transition, "
              "tied to Middle Pleistocene environmental instability.",
      start_dating_method="argon-argon", end_dating_method="argon-argon",
      standing="consensus",
      date_note="Late Acheulean assemblages run 615-499 ka. The Middle Stone Age onset is "
                "most likely by about 320 ka and at least by 305 ka, which is the youngest "
                "boundary this node claims.",
      source_ids=[S_DEINO_2018])

    P("herto", "Herto", afr, ka(160), ka(154),
      tier="intermediate",
      summary="Middle Awash locality that produced Homo sapiens idaltu, among the oldest "
              "near-modern human fossils.",
      start_dating_method="argon-argon", end_dating_method="argon-argon",
      standing="consensus",
      date_note="Dated by argon-argon with tephra chemical correlation.",
      caveats=[{"kind": "misconception",
                "text": "Not the oldest Homo sapiens: Jebel Irhoud at about 315 ka and Omo "
                        "Kibish are both older.",
                "source_ids": [S_BERKELEY_HERTO]}],
      source_ids=[S_BERKELEY_HERTO])

    P("bodo", "Bodo", afr, ka(640), None,
      tier="specialist",
      summary="Middle Awash cranium anchoring the mid-Pleistocene African record, bearing "
              "cut marks suggestive of deliberate defleshing.",
      start_dating_method="argon-argon",
      end_precision="unknown",
      standing="consensus",
      date_note="Weighted mean 0.64+/-0.03 Ma by laser-fusion argon-argon on vitric tephra. "
                "The age is settled; the taxonomic assignment is not.",
      caveats=[{"kind": "naming-confusion",
                "text": "Assigned to Homo heidelbergensis, or to a proposed 'Homo bodoensis'. "
                        "That argument is taxonomic, not chronological.",
                "source_ids": [S_CLARK_1994_BODO]}],
      source_ids=[S_CLARK_1994_BODO])

    P("enkapune-ya-muto", "Enkapune Ya Muto", afr, ka(46), ka(40),
      tier="specialist",
      summary="Kenyan rock shelter with a claim to the earliest Later Stone Age blade "
              "technology in Africa, and the oldest directly dated ornaments anywhere.",
      start_dating_method="radiocarbon-uncalibrated",
      end_dating_method="radiocarbon-uncalibrated",
      standing="minority",
      date_note="STORED AS UNCALIBRATED RADIOCARBON. Excavation reports give bare BP without "
                "stating a calibration basis, so these are not calendar dates. The blade "
                "industry is reported as at least 46,000 and possibly 50,000 years old; the "
                "ostrich-eggshell beads at about 40,000.",
      caveats=[{"kind": "misconception",
                "text": "Usually summarised as '40,000-year-old beads', which hides the older "
                        "and far more contested claim about the blade industry beneath them.",
                "source_ids": [S_AMBROSE_EYM]}],
      source_ids=[S_AMBROSE_EYM])

    P("kabwe", "Kabwe", afr, ka(299), None,
      tier="intermediate",
      aliases=["Broken Hill"],
      end_precision="unknown",
      summary="Zambian cranium once called Homo rhodesiensis, and the clearest case in "
              "African palaeoanthropology of a textbook number being wrong by 200,000 years.",
      start_dating_method="uranium-series",
      start_year_min=ka(324), start_year_max=ka(274),
      standing="consensus",
      date_note="299+/-25 ka at two sigma, from direct uranium-series dating of the skull "
                "itself. Other bones from the assemblage span roughly 301-102 ka, which points "
                "to multiple individuals or reworked deposits; the site was destroyed by "
                "quarrying, so several associated dates are minimum ages only.",
      caveats=[{"kind": "misconception",
                "text": "Routinely given as about 500,000 years old for most of the twentieth "
                        "century. Direct dating in 2020 made it roughly 200,000 years younger.",
                "source_ids": [S_GRUN_2020]}],
      source_ids=[S_GRUN_2020])


    # ---- Southern Africa ---------------------------------------------------
    P("sterkfontein", "Sterkfontein", afr, ma(3.67), ma(2.07),
      tier="foundational",
      allow_outside_parent_dates=True,
      summary="Cradle of Humankind cave system holding 'Mrs Ples' and 'Little Foot', and the "
              "most actively contested chronology in African palaeoanthropology.",
      start_dating_method="cosmogenic", end_dating_method="uranium-series",
      start_year_min=ma(3.83), start_year_max=ma(3.51),
      standing="majority",
      date_precision="disputed",
      as_of=CHECKED,
      date_note="Two independent methods disagree by over a million years for the SAME "
                "deposits. Cosmogenic 26Al/10Be burial dating puts Little Foot at "
                "3.67+/-0.16 Ma and Member 4 at 3.41-3.61 Ma; U-Pb flowstone, ESR and "
                "palaeomagnetic work puts Member 4 at 2.61-2.07 Ma and Little Foot at "
                "2.17+/-0.17 Ma. Unresolved as of 2024. The span stored here deliberately "
                "covers both, and neither end should be read as a settled figure.",
      alternatives=[
          {"label": "Cosmogenic burial dating", "standing": "majority",
           "start_year": ma(3.67), "dating_method": "cosmogenic",
           "note": "Little Foot 3.67+/-0.16 Ma; Member 4 3.41-3.49 Ma.",
           "source_ids": [S_GRANGER_2015, S_GRANGER_2022]},
          {"label": "U-Pb, ESR and palaeomagnetism", "standing": "minority",
           "start_year": ma(2.61), "end_year": ma(2.07), "dating_method": "uranium-series",
           "note": "Member 4 at 2.61-2.07 Ma; StW 573 at 2.17+/-0.17 Ma.",
           "source_ids": [S_PICKERING_2020, S_WALKER_2006]},
      ],
      caveats=[{"kind": "misconception",
                "text": "Popular accounts quote 3.67 Ma for Little Foot as settled; a U-Pb "
                        "counter-chronology roughly 1.5 million years younger is still live.",
                "source_ids": [S_WALKER_2006]}],
      source_ids=[S_GRANGER_2015, S_GRANGER_2022, S_PICKERING_2020, S_WALKER_2006])

    P("swartkrans", "Swartkrans", afr, ma(2.22), ka(960),
      tier="intermediate",
      summary="Cradle of Humankind cave with the earliest well-dated Paranthropus robustus "
              "and among the oldest Oldowan tools in southern Africa.",
      start_dating_method="cosmogenic", end_dating_method="cosmogenic",
      standing="consensus",
      date_note="Member 1 Lower Bank at 2.22+/-0.09 Ma by cosmogenic isochron burial dating, "
                "agreeing within one sigma with a U-Pb flowstone age of 2.25+/-0.08 Ma. "
                "Member 3 at 0.96+/-0.09 Ma.",
      caveats=[{"kind": "misconception",
                "text": "Older faunal-correlation ages are superseded by isochron cosmogenic "
                        "and U-Pb dating; sources quoting only faunal ages are out of date.",
                "source_ids": [S_KUMAN_2021]}],
      source_ids=[S_KUMAN_2021, S_GRANGER_2014_SK])

    P("rising-star", "Rising Star Cave", afr, ka(335), ka(236),
      tier="intermediate",
      summary="The Dinaledi Chamber, source of the Homo naledi fossils, whose surprisingly "
              "young age placed a small-brained hominin alongside early Homo sapiens.",
      start_dating_method="luminescence", end_dating_method="esr",
      standing="consensus",
      date_note="A combined 236-335 ka estimate: OSL on sediment with uranium-thorium and "
                "palaeomagnetism on flowstones for the older bound, US-ESR on teeth for the "
                "younger. The age is settled; the claim of deliberate burial is not.",
      caveats=[{"kind": "misconception",
                "text": "Its primitive anatomy suggested a Pliocene age, but naledi is Middle "
                        "Pleistocene and contemporary with early Homo sapiens.",
                "source_ids": [S_DIRKS_2017]}],
      source_ids=[S_DIRKS_2017])

    P("sibudu", "Sibudu Cave", afr, ka(77), ka(38.6),
      tier="specialist",
      summary="KwaZulu-Natal shelter with the finest-resolution Middle Stone Age sequence in "
              "southern Africa, from pre-Still Bay through Howiesons Poort to the final MSA.",
      start_dating_method="luminescence", end_dating_method="luminescence",
      standing="consensus",
      date_note="Single-grain OSL throughout. Post-Howiesons Poort, late and final MSA phases "
                "have weighted means of 58.5+/-1.4, 47.7+/-1.4 and 38.6+/-1.9 ka, separated by "
                "two occupational hiatuses. Whether the Howiesons Poort was a short episode or "
                "persisted to about 50 ka is an open regional debate.",
      source_ids=[S_JACOBS_SIBUDU])

    P("pinnacle-point", "Pinnacle Point", afr, ka(92), ka(49),
      tier="specialist",
      summary="Southern Cape caves with early evidence for marine resource use, heat treatment "
              "of stone and pigment, and one of the most precisely dated MSA sequences.",
      start_dating_method="luminescence", end_dating_method="luminescence",
      standing="consensus",
      date_note="PP5-6 re-dated in 2025 by single-grain OSL with Bayesian age modelling over "
                "169 samples, giving about 92-49 ka. Individual units run from 96+/-6 ka down "
                "to 52+/-3 ka.",
      source_ids=[S_PP_2025, S_PP_2017])

    P("diepkloof", "Diepkloof Rock Shelter", afr, ka(65), ka(55),
      tier="specialist",
      summary="Western Cape shelter whose engraved ostrich eggshell containers are among the "
              "earliest deliberately produced graphic marks known.",
      start_dating_method="luminescence", end_dating_method="luminescence",
      standing="consensus",
      date_note="The engraving tradition is placed securely between 55 and 65 ka by OSL, with "
                "a thermoluminescence estimate of 61+/-4 ka for one layer boundary. A later "
                "paper from the same group gives a much wider 100-52 ka range; that "
                "discrepancy is unreconciled, so the narrower sourced window is used here.",
      source_ids=[S_TEXIER_2010])

    P("apollo-11-cave", "Apollo 11 Cave", afr, ka(30), ka(29),
      tier="intermediate",
      summary="Namibian shelter holding seven painted stone plaques, four figurative, among "
              "the oldest known figurative art in Africa.",
      start_dating_method="luminescence", end_dating_method="luminescence",
      standing="consensus",
      date_note="OSL gives 29.4+/-1.4 ka and the uppermost MSA layer 29.8+/-1.1 ka. An AMS "
                "radiocarbon date of 29.0+/-0.4 ka BP accompanies these, but the published "
                "report does not state whether it is calibrated, so the OSL ages are used as "
                "the boundary and the radiocarbon is not converted. A frequently quoted "
                "25,500-23,500 BC almost certainly reflects that calibration ambiguity rather "
                "than a competing measurement.",
      caveats=[{"kind": "misconception",
                "text": "The two circulating figures are dating conventions, probably "
                        "calibrated versus uncalibrated, not rival scientific claims.",
                "source_ids": [S_RIFKIN_2015]}],
      source_ids=[S_RIFKIN_2015])

    # ---- North Africa and the Sahara ---------------------------------------
    P("jebel-irhoud", "Jebel Irhoud", afr, ka(315), None,
      tier="foundational",
      summary="Moroccan site holding the oldest securely dated Homo sapiens fossils, which "
              "moved the species' origin back by roughly 100,000 years.",
      start_dating_method="luminescence",
      start_year_min=ka(349), start_year_max=ka(281),
      end_precision="unknown",
      standing="consensus",
      date_note="315+/-34 ka, a weighted average from thermoluminescence on heated flints "
                "cross-checked by uranium-series and ESR on teeth. The Irhoud 3 mandible "
                "dates separately to 286+/-32 ka.",
      caveats=[{"kind": "misconception",
                "text": "Originally classified as archaic or Neanderthal-related and dated to "
                        "about 40,000 years; both the age and the classification were wrong.",
                "source_ids": [S_RICHTER_2017]}],
      source_ids=[S_RICHTER_2017, S_HUBLIN_2017])

    P("taforalt", "Taforalt", afr, bp(21160), bp(13892),
      tier="intermediate",
      aliases=["Grotte des Pigeons"],
      summary="The most extensively radiocarbon-dated Later Stone Age site in North Africa, "
              "and the location of the continent's oldest known cemetery.",
      start_dating_method="radiocarbon-calibrated",
      end_dating_method="radiocarbon-calibrated",
      start_precision="minimum",
      standing="consensus",
      date_note="The Iberomaurusian appears from at least 21,160 cal BP, after a Middle Stone "
                "Age industry persisting to about 24.5 ka cal BP and an occupational gap. "
                "Bayesian-modelled from 54 AMS dates. At least 34 burials are directly dated "
                "to between 15,077 and 13,892 cal BP.",
      caveats=[{"kind": "misconception",
                "text": "Older work spread the burials across 23,000-10,800 BP; direct AMS "
                        "dating narrows the burial episode to about 1,200 years.",
                "source_ids": [S_VANDELOOSDRECHT_2018]}],
      source_ids=[S_BARTON_2013, S_VANDELOOSDRECHT_2018])

    P("wadi-kubbaniya", "Wadi Kubbaniya", afr, bp(19000), bp(17000),
      tier="specialist",
      summary="Late Palaeolithic sites near Aswan, once thought to hold the world's earliest "
              "cereal cultivation, and a cautionary case in contamination.",
      start_dating_method="radiocarbon-uncalibrated",
      end_dating_method="radiocarbon-uncalibrated",
      standing="consensus",
      date_note="STORED AS UNCALIBRATED RADIOCARBON. The published site dates are conventional "
                "BP without a stated calibration basis, so they are not calendar years. A "
                "later synthesis of the broader aggradation sequence gives about 25,650-22,650 "
                "cal BP, which refers to different stratigraphic units rather than "
                "contradicting these.",
      caveats=[{"kind": "misconception",
                "text": "The barley, lentils and wheat found here were shown by AMS dating to "
                        "be modern contaminants. This is not an early-agriculture site.",
                "source_ids": [S_WENDORF_1984]}],
      source_ids=[S_WENDORF_1984])

    P("gobero", "Gobero", afr, bp(9600), bp(4800),
      tier="specialist",
      allow_outside_parent_dates=True,
      summary="The largest and oldest known Stone Age cemetery in the Sahara, preserving two "
              "distinct Holocene populations either side of a drought.",
      start_dating_method="radiocarbon-calibrated",
      end_dating_method="radiocarbon-calibrated",
      standing="consensus",
      date_note="Kiffian hunter-fisher-gatherers 9.6-7.4 kBP, then a gap of about 800 years, "
                "then Tenerian pastoralists 6.6-4.8 kBP. Recalibrated to IntCal20, which "
                "narrowed the gap originally reported as roughly a millennium.",
      source_ids=[S_GOBERO_2026])

    P("capsian", "Capsian Culture", afr, bp(10000), bp(6000),
      tier="specialist",
      summary="Epipalaeolithic to early Neolithic tradition of the eastern Maghreb, known for "
              "its shell-and-ash mound sites and later pressure-flaked bladelets.",
      start_dating_method="radiocarbon-calibrated",
      end_dating_method="radiocarbon-calibrated",
      standing="consensus",
      date_note="About 10,000 to 6,000 cal BP. The Typical-to-Upper Capsian transition falls "
                "near the 8,200 cal BP cold event, after which pressure technique dominates.",
      caveats=[{"kind": "misconception",
                "text": "Not purely a foraging tradition throughout: pottery appears in a "
                        "hunter-gatherer context by 8,000 cal BP and herding by 7,400 cal BP.",
                "source_ids": [S_JACKES_LUBELL]}],
      source_ids=[S_JACKES_LUBELL])

    P("khartoum-mesolithic", "Khartoum Mesolithic", afr, -8800, -5000,
      tier="specialist",
      aliases=["Early Khartoum"],
      summary="Pottery-using but pre-agricultural hunter-fisher-gatherers of the central Nile, "
              "known for wavy-line and dotted-wavy-line ceramics.",
      start_dating_method="radiocarbon-calibrated",
      end_dating_method="radiocarbon-calibrated",
      standing="consensus",
      date_note="Dated between 8800-8500 and 5000 BCE. Note that at the type site "
                "Esh-Shaheinab the Mesolithic levels were never directly dated at all; their "
                "placement rests on typological cross-dating of the Dotted Wavy Line horizon.",
      caveats=[{"kind": "naming-confusion",
                "text": "Distinct from the later Khartoum Neolithic, which is a stock-keeping "
                        "and cultivating tradition, not merely a later phase of this one.",
                "source_ids": [S_ESH_SHAHEINAB]}],
      source_ids=[S_ESH_SHAHEINAB])

    P("fayum-neolithic", "Fayum Neolithic", afr, -5700, -4200,
      tier="intermediate",
      summary="One of the earliest well-documented farming and herding sequences in the Nile "
              "Valley, following the Qarunian foragers of the same oasis.",
      start_dating_method="radiocarbon-calibrated",
      end_dating_method="radiocarbon-calibrated",
      standing="consensus",
      date_note="About 5700-4200 cal BC, preceded by the Fayum Epipalaeolithic (Qarunian) at "
                "roughly 7100-6000 cal BC. Different lines of evidence give different figures: "
                "about 5800 BC for earliest cereal cultivation from lake cores, 5400 BC for the "
                "first domestic animals, and 4650-4350 BC for the Kom K and Kom W settlements.",
      caveats=[{"kind": "misconception",
                "text": "The three commonly quoted dates refer to different evidence at "
                        "different locations in the oasis and should not be merged into one.",
                "source_ids": [S_LINSEELE_2014, S_FAYUM_LAKE]}],
      source_ids=[S_LINSEELE_2014, S_FAYUM_LAKE])

    P("ishango", "Ishango", afr, bp(20000), bp(8500),
      tier="specialist",
      summary="A Semliki River site in the DRC, famous for a notched bone sometimes read as an "
              "early tally device, and unusually hard to date.",
      start_dating_method="radiocarbon-uncalibrated",
      end_dating_method="radiocarbon-uncalibrated",
      standing="minority",
      date_precision="disputed",
      as_of=CHECKED,
      date_note="STORED AS UNCALIBRATED RADIOCARBON, and genuinely unresolved. Local volcanic "
                "activity altered the carbon reservoir and no charcoal was available for "
                "cross-checking. Three incompatible figures circulate: roughly 8,500-11,000 "
                "years from the original assessment, about 20,000 from later review, and about "
                "22,000 attributed to Alison Brooks. The stored span covers them rather than "
                "choosing between them.",
      alternatives=[
          {"label": "Original assessment, 9000-6500 BCE", "standing": "minority",
           "start_year": -9000, "end_year": -6500,
           "dating_method": "radiocarbon-uncalibrated",
           "note": "Earliest published framing; radiocarbon compromised by volcanism.",
           "source_ids": [S_ISHANGO_HIST]},
          {"label": "About 22,000 years", "standing": "minority",
           "start_year": bp(22000), "dating_method": "radiocarbon-uncalibrated",
           "note": "Third figure in circulation, attributed to Alison Brooks.",
           "source_ids": [S_ISHANGO_HIST]},
      ],
      caveats=[{"kind": "misconception",
                "text": "Popular writing gives a confident '20,000 years'; the technical "
                        "literature calls the radiocarbon unreliable and offers three figures.",
                "source_ids": [S_ISHANGO_HIST]}],
      source_ids=[S_ISHANGO_HIST])

    # ---- Domestication and metallurgy --------------------------------------
    FIRST("african-cattle", "Cattle Herding in Africa", afr, -5750,
          tier="intermediate",
          summary="The oldest uncontroversial domestic cattle in Africa, in Egypt's Western "
                  "Desert -- introduced from the Near East rather than domesticated locally.",
          start_dating_method="unknown",
          standing="minority",
          date_note="Dated archaeozoologically and cross-checked against population genomics "
                    "rather than by a single radiometric method on the animals themselves. "
                    "A 2017 reassessment argues the long-standing hypothesis of independent "
                    "early Holocene domestication in northeast Africa should be abandoned.",
          alternatives=[
              {"label": "Independent African domestication, 10,000-8,000 BP",
               "standing": "superseded", "start_year": bp(10000), "end_year": bp(8000),
               "dating_method": "unknown",
               "note": "Long-dominant model; the eastern Saharan Bos are now read as aurochs.",
               "source_ids": [S_BRASS_2017_CATTLE]},
          ],
          caveats=[{"kind": "misconception",
                    "text": "Nabta Playa's early Holocene cattle bones are widely cited as "
                            "early domestication; they are argued to be hunted wild aurochs.",
                    "source_ids": [S_BRASS_2017_CATTLE]}],
          source_ids=[S_BRASS_2017_CATTLE, S_EDINBURGH_CATTLE])

    FIRST("african-cereals", "African Cereal Domestication", afr, -4000,
          tier="intermediate",
          summary="Pearl millet in the West African Sahel and sorghum in eastern Sudan: two "
                  "independent African domestications of indigenous cereals.",
          start_dating_method="radiocarbon-calibrated",
          standing="consensus",
          date_note="Sorghum domestication is under way in eastern Sudan by the fourth "
                    "millennium BC on Butana Group pottery impressions; pearl millet is "
                    "attested in the Tilemsi Valley by about 2500-2000 BC, with a single "
                    "directly dated grain at 2621-2464 BCE.",
          caveats=[{"kind": "misconception",
                    "text": "Neither crop has a domestication date: both were gradual "
                            "processes running centuries, with cultivation preceding "
                            "morphological domestication.",
                    "source_ids": [S_MANNING_MILLET, S_WINCHELL_SORGHUM]}],
          source_ids=[S_MANNING_MILLET, S_WINCHELL_SORGHUM])

    P("bantu-homeland", "Bantu Homeland Phase", afr, bp(7000), bp(4000),
      tier="intermediate",
      allow_outside_parent_dates=True,
      summary="The long local development of proto-Bantu in the Cameroon Grassfields, before "
              "any outward expansion across the continent.",
      start_dating_method="unknown", end_dating_method="unknown",
      standing="majority",
      date_precision="disputed",
      as_of=CHECKED,
      date_note="Dated by historical linguistics and ceramic typology cross-referenced with "
                "population genetics, not by a single method. Two syntheses disagree by 1,000 "
                "to 2,000 years on when proto-Bantu itself formed: 6,000-7,000 to 4,000-5,000 "
                "years ago, versus 3000-2000 BCE.",
      alternatives=[
          {"label": "Proto-Bantu forms 3000-2000 BCE", "standing": "majority",
           "start_year": -3000, "end_year": -2000, "dating_method": "unknown",
           "note": "Cambridge synthesis; Grassfields ancestral group predates 3000 BCE.",
           "source_ids": [S_CAMBRIDGE_BANTU]},
      ],
      caveats=[{"kind": "misconception",
                "text": "The Bantu expansion was not a sudden migration; this homeland phase "
                        "alone ran more than two millennia before any outward spread.",
                "source_ids": [S_OUP_BANTU]}],
      source_ids=[S_OUP_BANTU, S_CAMBRIDGE_BANTU])

    P("nok", "Nok Culture", afr, -1500, -1,
      tier="intermediate",
      allow_outside_parent_dates=True,
      summary="Central Nigerian culture producing sub-Saharan Africa's earliest large-scale "
              "sculptural tradition, and some of its earliest iron smelting.",
      start_dating_method="radiocarbon-calibrated",
      end_dating_method="radiocarbon-calibrated",
      standing="majority",
      date_precision="disputed",
      as_of=CHECKED,
      date_note="An early phase begins around the middle of the second millennium BC; the main "
                "phase with terracottas and iron production runs from the 9th to the 4th "
                "century BC. Iron-smelting dates are genuinely imprecise: the earliest Nok "
                "furnaces calibrate to about 800-550 BCE, but a radiocarbon calibration plateau "
                "near 2450 BP makes this window resistant to sharpening by more dating.",
      alternatives=[
          {"label": "Taruga furnace determinations, 920-280 BCE", "standing": "minority",
           "start_year": -920, "end_year": -280,
           "dating_method": "radiocarbon-uncalibrated",
           "note": "Four raw samples from one site spanning nearly a millennium.",
           "source_ids": [S_TARUGA_FURNACES]},
      ],
      caveats=[{"kind": "misconception",
                "text": "Single confident dates for 'the start of iron smelting' hide a "
                        "calibration plateau that no amount of further dating will resolve.",
                "source_ids": [S_OUP_NOK]}],
      source_ids=[S_OUP_NOK, S_TARUGA_FURNACES])
