"""East Asia: the Chinese Neolithic filled in, Korea given a prehistory, and Erlitou.

Research in `docs/eastasia-research.md`.

**This pass began from a false positive, and that is worth recording.** The
childless-node report named `east-asia.prehistory` the single biggest gap in
the dataset: 13,700 years, no children. It is a navigation era. Its own summary
says the Jomon and the Chinese Neolithic "also sit in their own national
sequences, where they belong," and they do — Jomon is fully subdivided into six
phases under Japan, and the Chinese Neolithic had six cultures under China.
Filling it would have duplicated coverage that already existed. `coverage.py`
now excludes navigation eras, alongside the synthesis eras it already skipped.

What the corrected report showed is that the real East Asian gaps were
elsewhere and quite different in character:

- **Korea had no prehistory at all.** Eight children under `east-asia.korea`,
  all of them states, the earliest being Gojoseon. No Chulmun, no Mumun, no
  arrival of millet or rice. An entire peninsula started at 2333 BCE.
- **The Chinese Neolithic had six cultures** and was missing most of the rest.
- **`east-asia.china.legendary` was childless across 3,400 years** — the node
  that carries the Xia — while Erlitou, the site the whole Xia argument is
  actually about, was absent from the dataset entirely.

Three authoring decisions worth stating.

**Erlitou is parented under `legendary`, not under the Neolithic.** That is the
node the Xia question belongs to, and putting the site there puts the evidence
next to the tradition instead of in a separate wing of the tree.

**The Xia identification is not adjudicated here.** Both fetched academic
sources describe a genuine split: most Chinese scholars read Erlitou as Xia,
most overseas scholars hold that it cannot be confirmed without contemporaneous
writing, and there is an internal middle position preferring "the Erlitou
State". The dataset carries all three with their standings and picks no winner.
Note that the empirical driver of the dispute is not ideology but successive
re-dating: Erlitou's span has been revised later and narrower across at least
three episodes, from a comfortable fit with textual Xia dates toward a range
that begins near the traditional END of Xia.

**Xianrendong's 20,000 cal BP pottery is authored as contested.** The Science
paper is peer-reviewed, and so are the two independent re-analyses that dispute
it. Yuchanyan, which a previous pass declined to author because sources
conflicted, is authored now on the strength of the dedicated 2009 PNAS study,
with the older and younger lab results carried as an alternative.

Deliberately NOT authored: Majiabang (best figures are municipal government
pages); Fukui Cave (pre-AMS dates with no calibrated equivalent in any fetched
source); the Sorori "quasi-rice" claim, which its own source describes as
disputed; and any single settled Jomon-Yayoi boundary date, because the field
has not converged on one.
"""

from builders import make_builders

S_FRONTIERS_C14 = "frontiers-2023-chinese-radiocarbon"
S_PNAS_CISHAN = "pnas-2009-north-china-millet"
S_PNAS_MILLET = "pnas-2012-early-millet-use"
S_ZHAO_OXFORD = "zhao-oxford-millet-critique"
S_ANTIQUITY_NE = "antiquity-northeast-china-sequence"
S_DAWENKOU_BAYES = "bayesian-chronology-neolithic-china"
S_HEMUDU_UCL = "ucl-hemudu-review"
S_HEMUDU_PALEO = "zheng-2021-hemudu-paleomagnetic"
S_DAXI_CA = "current-anthropology-yangtze-rice"
S_SHIJIAHE = "shijiahe-ams-chronology"
S_QIJIA_BA = "mei-china-central-asia-bronze"
S_MOGOU = "mogou-bioarchaeology-antiquity"
S_LIANGZHU_PNAS = "pnas-2017-liangzhu-hydraulic"
S_LIANGZHU_ANTIQ = "liangzhu-complex-society-antiquity"
S_LIANGZHU_UNESCO = "unesco-liangzhu-inscription"
S_LILIU_2009 = "li-liu-2009-xia-erlitou-debate"
S_CHEN_CHUN = "chen-chun-erlitou-xia-dispute"
S_LAWLER_SCIENCE = "lawler-science-founding-dynasty"
S_ESCHOLAR_ERLITOU = "escholarship-erlitou-wiggle-match"
S_XIANRENDONG = "wu-2012-xianrendong-pottery"
S_YANSHINA = "yanshina-2019-earliest-pottery"
S_KUZMIN_POTTERY = "kuzmin-origins-of-pottery-east-asia"
S_YUCHANYAN = "boaretto-2009-yuchanyan"
S_KEALLY_C14 = "keally-radiocarbon-east-asia"
S_TIANYUAN = "tianyuan-cave-radiocarbon"
S_KOREANIC = "cambridge-koreanic-farming-dispersal"
S_KOREA_CA = "current-anthropology-korea-foraging"
S_STEVENS_FULLER = "stevens-fuller-agriculture-east-asia"
S_KYUSHU_NEASIA = "kyushu-initial-spread-agriculture"
S_MUMUN_HANYANG = "hanyang-middle-mumun-isotopes"
S_BALE_THESIS = "bale-mumun-thesis"
S_SANNAI_HABU = "habu-2008-sannai-maruyama"
S_JOMON_PLOS = "plos-2016-jomon-population"
S_SHODA_2010 = "shoda-2010-yayoi-dating"
S_SHODA_SEAA = "shoda-seaa-yayoi-controversy"

EAST_ASIA_SOURCES = [
    {"id": S_FRONTIERS_C14, "kind": "scholarly",
     "citation": "'Radiocarbon dating and its applications in Chinese archaeology', Frontiers in Earth Science 11 (2023)",
     "url": "https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2023.1064717/full"},
    {"id": S_PNAS_CISHAN, "kind": "scholarly",
     "citation": "Lu et al., 'Earliest domestication of common millet in East Asia', PNAS 106 (2009)",
     "url": "https://www.pnas.org/doi/10.1073/pnas.0903375106"},
    {"id": S_PNAS_MILLET, "kind": "scholarly",
     "citation": "'Early millet use in northern China', PNAS 109 (2012)",
     "url": "https://www.pnas.org/doi/10.1073/pnas.1115430109"},
    {"id": S_ZHAO_OXFORD, "kind": "scholarly",
     "citation": "Oxford doctoral thesis reporting Zhao's (2011) critique of the earliest Cishan millet dates",
     "url": "https://ora.ox.ac.uk/objects/uuid:b265f3b2-402a-46fc-ba13-bee750c9a185/files/rbk1289975",
     "note": "Calls the earliest Lu et al. dates 'highly controversial' on sample-context grounds, "
             "and gives 5670-5610 BCE as the earliest DIRECT date on millet grains, at Xinglongwa."},
    {"id": S_ANTIQUITY_NE, "kind": "scholarly",
     "citation": "Antiquity supplementary material, northeast China cultural sequence",
     "url": "https://static.cambridge.org/content/id/urn:cambridge.org:id:article:S0003598X20002367/resource/name/S0003598X20002367sup001.pdf"},
    {"id": S_DAWENKOU_BAYES, "kind": "scholarly",
     "citation": "Bayesian chronological modelling of Chinese Neolithic cultures, Journal of Archaeological Science: Reports",
     "url": "https://www.sciencedirect.com/science/article/abs/pii/S2352409X16305648"},
    {"id": S_HEMUDU_UCL, "kind": "scholarly",
     "citation": "Fuller et al., Hemudu review (University College London)",
     "url": "http://www.homepages.ucl.ac.uk/~tcrndfu/articles/Hemudu%20review.pdf"},
    {"id": S_HEMUDU_PALEO, "kind": "scholarly",
     "citation": "Zheng et al. (2021), paleomagnetic chronology of the Hemudu culture",
     "url": "https://www.sciencedirect.com/science/article/abs/pii/S0031018221000821"},
    {"id": S_DAXI_CA, "kind": "scholarly",
     "citation": "Current Anthropology, on the establishment of rice agriculture in the middle Yangtze",
     "url": "https://www.journals.uchicago.edu/doi/full/10.1086%2F659308"},
    {"id": S_SHIJIAHE, "kind": "scholarly",
     "citation": "AMS chronology of the Shijiahe culture (PMC, 2017)",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5438134/"},
    {"id": S_QIJIA_BA, "kind": "scholarly",
     "citation": "Mei, 'China, Central Asia and the Bronze Age' (British Academy)",
     "url": "https://www.thebritishacademy.ac.uk/documents/3098/Mei-China-central-asia-bronze-age.pdf"},
    {"id": S_MOGOU, "kind": "scholarly",
     "citation": "'The Mogou bioarchaeology project', Antiquity",
     "url": "https://www.cambridge.org/core/journals/antiquity/article/mogou-bioarchaeology-project-exploring-health-in-the-chinese-bronze-age/53F1F32DA8EB7B3E5FC73F86F5C9ACAE"},
    {"id": S_LIANGZHU_PNAS, "kind": "scholarly",
     "citation": "Liu et al., 'Earliest hydraulic enterprise in China, 5,100 years ago', PNAS 114 (2017)",
     "url": "https://www.pnas.org/doi/10.1073/pnas.1710516114",
     "note": "AMS on grass in the dam sandbags. The dams predate most of the walled city."},
    {"id": S_LIANGZHU_ANTIQ, "kind": "scholarly",
     "citation": "'The emergence of complex society in China: the case of Liangzhu', Antiquity",
     "url": "https://www.cambridge.org/core/journals/antiquity/article/abs/emergence-of-complex-society-in-china-the-case-of-liangzhu/0D4FD61E9460755CED69047FAD7FA2AD",
     "note": "Proposes Liangzhu 'may be the earliest state society in East Asia.'"},
    {"id": S_LIANGZHU_UNESCO, "kind": "reference",
     "citation": "UNESCO World Heritage Committee, Decision 43COM 8B.15, Baku, 6 July 2019",
     "url": "https://whc.unesco.org/en/list/1592/documents/"},
    {"id": S_LILIU_2009, "kind": "scholarly",
     "citation": "Li Liu, 'Academic freedom, political correctness, and early civilisation in Chinese archaeology: the debate on Xia-Erlitou relations', Antiquity 83 (2009)",
     "url": "https://www.cambridge.org/core/journals/antiquity/article/academic-freedom-political-correctness-and-early-civilisation-in-chinese-archaeology-the-debate-on-xiaerlitou-relations/C5AB38AAD524216D82B9B31F713F6D22",
     "note": "'Most scholars in the West have reservations regarding interpretations "
             "identifying Erlitou with the material culture of an early dynasty.'"},
    {"id": S_CHEN_CHUN, "kind": "scholarly",
     "citation": "Chen Chun, 'Erlitou and Xia: A Dispute between Chinese and Overseas Scholars'",
     "url": "https://www.sociostudies.org/journal/articles/1843103/",
     "note": "Sets out all three positions, including Bagley's point that Shang oracle bones "
             "show no sign of a Xia concept and the name first appears in Zhou texts."},
    {"id": S_LAWLER_SCIENCE, "kind": "press",
     "citation": "Lawler, 'Founding Dynasty or Myth?', Science (2009)",
     "url": "https://www.andrewlawler.com/scimag2010jandynasty/",
     "note": "Reports Wu Xiaohong's 2007 dates pushing Erlitou's start later, to c. 1750 BCE."},
    {"id": S_ESCHOLAR_ERLITOU, "kind": "scholarly",
     "citation": "UC eScholarship, citing Qiu, Cai & Zhang (2006) wiggle-matched dates for Erlitou",
     "url": "https://escholarship.org/content/qt9df4w6kn/qt9df4w6kn_noSplash_a8c2cbb73ce509220814d06ba4327e0f.pdf"},
    {"id": S_XIANRENDONG, "kind": "scholarly",
     "citation": "Wu et al., 'Early Pottery at 20,000 Years Ago in Xianrendong Cave, China', Science 336 (2012)",
     "url": "https://www.science.org/doi/10.1126/science.1218643"},
    {"id": S_YANSHINA, "kind": "scholarly",
     "citation": "Yanshina, on the age of the earliest South China pottery, Kunstkamera (2019)",
     "url": "https://journal.kunstkamera.ru/en/archive/2019_3/yanshina_ov_o_vozraste_drevnejshej_keramiki_yuzhnogo_kitaya",
     "note": "The dates 'have an obscure context, contradict the TL-datings of the ceramics "
             "themselves, and are in poor agreement with the paleoclimatic data.'"},
    {"id": S_KUZMIN_POTTERY, "kind": "scholarly",
     "citation": "Kuzmin, 'The origins of pottery in East Asia and neighbouring regions'",
     "url": "https://core.ac.uk/download/pdf/287445762.pdf",
     "note": "'The claim for earlier pottery in South China at the Xianrendong Cave, supposedly "
             "dated to ca. 20,000 cal BP, cannot be substantiated.'"},
    {"id": S_YUCHANYAN, "kind": "scholarly",
     "citation": "Boaretto et al., 'Radiocarbon dating of charcoal and bone collagen associated with early pottery at Yuchanyan Cave', PNAS 106 (2009)",
     "url": "https://www.pnas.org/doi/10.1073/pnas.0900539106"},
    {"id": S_KEALLY_C14, "kind": "scholarly",
     "citation": "Keally, on early pottery chronology in East Asia, Radiocarbon (University of Arizona)",
     "url": "https://journals.uair.arizona.edu/index.php/radiocarbon/article/viewFile/4273/3698"},
    {"id": S_TIANYUAN, "kind": "scholarly",
     "citation": "Late Pleistocene East Asian radiocarbon comparison table, Radiocarbon (University of Arizona)",
     "url": "https://journals.uair.arizona.edu/index.php/radiocarbon/article/viewFile/16936/pdf"},
    {"id": S_KOREANIC, "kind": "scholarly",
     "citation": "'Archaeolinguistic evidence for the farming/language dispersal of Koreanic', Evolutionary Human Sciences",
     "url": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/CE1DF81011ED49CED531AA6475959157/S2513843X20000493a.pdf/archaeolinguistic-evidence-for-the-farminglanguage-dispersal-of-koreanic.pdf"},
    {"id": S_KOREA_CA, "kind": "scholarly",
     "citation": "'The Transition from Foraging to Farming in Prehistoric Korea', Current Anthropology 52:S4",
     "url": "https://www.journals.uchicago.edu/doi/full/10.1086/658488"},
    {"id": S_STEVENS_FULLER, "kind": "scholarly",
     "citation": "Stevens & Fuller, 'The spread of agriculture in eastern Asia' (UCL Discovery)",
     "url": "https://discovery.ucl.ac.uk/id/eprint/10052010/1/Stevens_Fuller_Agricultural%20Bases%20in%20East%20Asia%20final%20ms.pdf"},
    {"id": S_KYUSHU_NEASIA, "kind": "scholarly",
     "citation": "'The Initial Spread of Early Agriculture into Northeast Asia', Asian Archaeology 3 (Kyushu University)",
     "url": "https://api.lib.kyushu-u.ac.jp/opac_download_md/1812318/Asian%20Archaeology%20Vol.3.pdf"},
    {"id": S_MUMUN_HANYANG, "kind": "scholarly",
     "citation": "'Direct isotopic evidence for human millet consumption in the Middle Mumun period' (Hanyang University)",
     "url": "https://scholarworks.bwise.kr/hanyang/bitstream/2021.sw.hanyang/173162/1/Direct%20isotopic%20evidence%20for%20human%20millet%20consumption%20in%20the%20Middle%20Mumun%20period%20Implication%20and%20importance%20of%20millets%20in%20early%20agriculture%20on%20the%20Korean%20Peninsula.pdf"},
    {"id": S_BALE_THESIS, "kind": "scholarly",
     "citation": "Bale, doctoral thesis on the Mumun Pottery Period (University of Toronto)",
     "url": "https://tspace.library.utoronto.ca/bitstream/1807/31685/1/Bale_Martin_T_201111_PhD_thesis.pdf"},
    {"id": S_SANNAI_HABU, "kind": "scholarly",
     "citation": "Habu, on Sannai Maruyama, Antiquity (2008)",
     "url": "https://junkohabu.com/wp-content/uploads/2017/04/habu2008-antiquity.pdf"},
    {"id": S_JOMON_PLOS, "kind": "scholarly",
     "citation": "'Regional population dynamics in Jomon Japan', PLOS ONE (2016)",
     "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0154809",
     "note": "Summed radiocarbon probability over 1,598 Late and 1,462 Final Jomon dates."},
    {"id": S_SHODA_2010, "kind": "scholarly",
     "citation": "Shoda, 'Radiocarbon and archaeology in Japan and Korea: what has changed because of the Yayoi dating controversy?', Radiocarbon 52 (2010)",
     "url": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/957FA42A4A7A4F3E8E3DA575246B8367/S0033822200045471a.pdf/radiocarbon-and-archaeology-in-japan-and-korea-what-has-changed-because-of-the-yayoi-dating-controversy.pdf"},
    {"id": S_SHODA_SEAA, "kind": "scholarly",
     "citation": "Shoda, 'A Comment on the Yayoi Period Dating Controversy', Bulletin of the Society for East Asian Archaeology 1",
     "url": "https://www.seaa-web.org/sites/default/files/publications/bseaa-1/BSEAA1-Shoda.pdf"},
]

CHECKED = "2026-08-08"
C14 = "radiocarbon-calibrated"
MAG = "magnetostratigraphy"


def extend(E, entities):
    _, P, ERA, EVENT, _, _ = make_builders(E)
    neo = "east-asia.china.neolithic"
    lp = "east-asia.china.late-pleistocene"
    leg = "east-asia.china.legendary"
    kor = "east-asia.korea"
    jom = "east-asia.japan.jomon"

    # ------------------------------------------------- Late Pleistocene

    # Terminal-Pleistocene pottery does not belong under an era called Neolithic.
    # These caves predate farming by thousands of years, and the whole reason
    # they matter is that foragers made pots.
    ERA("late-pleistocene", "Late Pleistocene China", "east-asia.china", -40000, -10551,
        "intermediate",
        summary="China before farming: the earliest modern human remains in the region, "
                "and foragers making pottery thousands of years before any crop.",
        start_dating_method=C14, end_dating_method=C14, standing="majority",
        date_precision="approx",
        date_note="A container era. The span runs from the earliest directly dated modern "
                  "human in the region to the start of the Neolithic sequence; each entry "
                  "below carries its own dating.",
        source_ids=[S_TIANYUAN])

    P("tianyuan", "Tianyuan Cave", lp, -38990, -36170, "specialist",
      summary="A femur near Beijing from one of the earliest directly dated modern humans "
              "in East Asia.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="34,430+/-510 BP uncalibrated on the femur, calibrating to 38,120-40,940 "
                "cal BP.",
      source_ids=[S_TIANYUAN])

    P("xianrendong", "Xianrendong Cave", lp, -18050, -13750, "intermediate",
      summary="A Jiangxi cave holding what may be the oldest pottery in the world, made by "
              "foragers during the Last Glacial Maximum — if the dates hold.",
      start_dating_method=C14, end_dating_method=C14, standing="minority",
      date_precision="disputed",
      date_note="Ten AMS dates put the lowest sherd-bearing levels at 20,000-19,000 cal BP, "
                "which would be 2,000-3,000 years older than any other pottery known. Two "
                "independent re-analyses dispute this. The range authored here is Kuzmin's "
                "more conservative re-derivation; the Science figure is carried below.",
      alternatives=[
          {"label": "Pottery at 20,000-19,000 cal BP", "standing": "minority",
           "start_year": -18050, "end_year": -17050, "dating_method": C14,
           "note": "The original Science claim, from the excavating team. Peer-reviewed, and "
                   "disputed by two later peer-reviewed re-analyses.",
           "source_ids": [S_XIANRENDONG]},
      ],
      caveats=[{"kind": "misconception",
                "text": "Reported almost everywhere as settled. It is not: specialists argue "
                        "the dates have obscure context, conflict with the TL dates on the "
                        "ceramics, and disagree with the palaeoclimate.",
                "source_ids": [S_YANSHINA, S_KUZMIN_POTTERY]}],
      as_of=CHECKED,
      source_ids=[S_XIANRENDONG, S_YANSHINA, S_KUZMIN_POTTERY])

    P("yuchanyan", "Yuchanyan Cave", lp, -16350, -13480, "intermediate",
      summary="A Hunan cave with early pottery and wild rice, dated by a study designed "
              "specifically to get the chronology right.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="The 2009 study dates the pottery to 18,300-15,430 cal BP, with the most "
                "secure earliest estimate at 18,300-17,500 cal BP. It was built around "
                "dating the association itself rather than the layer, which is why it is "
                "preferred here over the older lab results.",
      alternatives=[
          {"label": "Older lab results, c. 17,200-14,700 cal BP", "standing": "superseded",
           "start_year": -15250, "end_year": -12750, "dating_method": C14,
           "note": "Zhao and Wu's 2000 figures, calibrated. Younger than the dedicated 2009 "
                   "study and based on less controlled associations.",
           "source_ids": [S_KEALLY_C14]},
      ],
      source_ids=[S_YUCHANYAN, S_KEALLY_C14, S_FRONTIERS_C14])

    # ------------------------------------------------- Chinese Neolithic

    P("cishan", "Cishan Culture", neo, -6050, -5050, "intermediate",
      summary="A north China millet culture whose storage pits produced the claim that "
              "cereal farming here began at the Pleistocene boundary.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="The contested part is not the culture but its earliest millet. Three AMS "
                "dates were reported at 10,400-10,100 cal BP, which would put broomcorn "
                "millet cultivation near 10,000 BP.",
      alternatives=[
          {"label": "Millet cultivation from c. 10,400 cal BP", "standing": "minority",
           "note": "Zhao's critique argues the samples' archaeological context does not "
                   "support the claim. The earliest DIRECT date on millet grains anywhere in "
                   "the region is 5670-5610 BCE, at Xinglongwa.",
           "source_ids": [S_PNAS_CISHAN, S_ZHAO_OXFORD]},
      ],
      caveats=[{"kind": "misconception",
                "text": "The very early millet dates are widely repeated as the origin of "
                        "north Chinese agriculture. They are described in the literature as "
                        "highly controversial on sample-context grounds.",
                "source_ids": [S_ZHAO_OXFORD]}],
      as_of=CHECKED,
      source_ids=[S_PNAS_CISHAN, S_PNAS_MILLET, S_ZHAO_OXFORD])

    P("xinglongwa", "Xinglongwa Culture", neo, -6200, -5400, "intermediate",
      summary="A northeast China culture of planned villages, jade working, and the "
              "earliest millet grains anywhere to be dated directly rather than by context.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Flourishes after 8.2 ka cal BP in the regional sequence. Its significance "
                "for dating is the direct AMS date on millet grains, 5670-5610 BCE — the "
                "conservative anchor against which the disputed Cishan claims are measured.",
      source_ids=[S_ZHAO_OXFORD, S_ANTIQUITY_NE])

    P("dawenkou", "Dawenkou Culture", neo, -4300, -2600, "intermediate",
      summary="An eastern China culture of elaborate burials and incised pottery marks "
              "sometimes discussed, carefully, in relation to later Chinese writing.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="Conventionally 4300-2600 BCE in three phases. A Bayesian re-modelling puts "
                "the onset at 4500-3900 BCE and the end considerably later, at 2100-1800 "
                "BCE; the two schemes differ by centuries at both ends.",
      source_ids=[S_DAWENKOU_BAYES])

    P("hemudu", "Hemudu Culture", neo, -5000, -4000, "intermediate",
      summary="A waterlogged lower Yangtze site that preserved wooden mortise-and-tenon "
              "architecture and some of the earliest cultivated rice.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Radiocarbon places first occupation about 5000-4900 BCE and the main "
                "village ending about 4600 BCE. An independent paleomagnetic chronology "
                "gives a start near 7000 cal BP, which agrees once units are reconciled but "
                "rests on an entirely different method.",
      alternatives=[
          {"label": "Paleomagnetic chronology, from c. 7000 cal BP", "standing": "minority",
           "start_year": -5050, "end_year": -3050, "dating_method": MAG,
           "note": "Zheng et al. 2021, derived from sediment magnetism rather than "
                   "radiocarbon.",
           "source_ids": [S_HEMUDU_PALEO]},
      ],
      source_ids=[S_HEMUDU_UCL, S_HEMUDU_PALEO])

    P("daxi", "Daxi Culture", neo, -4450, -3350, "specialist",
      summary="A middle Yangtze culture with some of the earliest walled settlements in "
              "China, at Chengtoushan.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Full rice agriculture is established in the middle Yangtze in this period, "
                "about 6400-5300 BP. Fortification at Chengtoushan appears as early as "
                "6400-6100 cal BP.",
      source_ids=[S_DAXI_CA])

    P("shijiahe", "Shijiahe Culture", neo, -2900, -2050, "specialist",
      summary="A middle Yangtze late Neolithic culture of walled settlements and rice, "
              "contemporary with Longshan further north.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="AMS phases: early 4850-4400 cal BP, middle 4400-4200, late 4200-4000. Rice "
                "grains from Shijiahe contexts date to 2580-2340 and 2480-2280 cal BC.",
      source_ids=[S_SHIJIAHE])

    P("qijia", "Qijia Culture", neo, -2200, -1600, "specialist",
      summary="A northwest culture straddling the Neolithic and Bronze Age, central to "
              "arguments about how metallurgy reached China.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="disputed",
      date_note="Credible academic sources give ranges from about 2400/2250 BCE to as late "
                "as 1400 BCE for different sub-sites and phases. The Mogou site specifically "
                "dates to 1750-1400 BC. This is real heterogeneity within the culture rather "
                "than a dating error, and no single range represents the whole.",
      allow_outside_parent_dates=True,
      source_ids=[S_QIJIA_BA, S_MOGOU])

    P("liangzhu-dams", "The Liangzhu Hydraulic System", f"{neo}.liangzhu", -3250, -2650,
      "intermediate",
      summary="Eleven dams and levees around the Liangzhu city, the earliest large-scale "
              "water management known anywhere.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="AMS on grass from the sandbags used in construction, plus associated "
                "charcoal. High dams begin about 5200-4800 cal BP and low dams and levees "
                "about 5000-4800 cal BP — both before most of the walled city itself, which "
                "dates to 4900-4600 cal BP. The waterworks came first.",
      source_ids=[S_LIANGZHU_PNAS, S_LIANGZHU_ANTIQ, S_LIANGZHU_UNESCO])

    # -------------------------------------------------- Erlitou and Xia

    P("erlitou", "Erlitou", leg, -1750, -1520, "foundational",
      summary="A large early Bronze Age centre in Henan with palace foundations and bronze "
              "workshops, and the site the entire Xia argument is actually about.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="Wiggle-matched radiocarbon compresses the occupation to roughly 1750-1520 "
                "BCE, about two centuries. The date has moved repeatedly: broadly 2100-1300 "
                "BC on 20th-century radiocarbon, 1880-1520 BC from the Xia-Shang-Zhou "
                "Chronology Project, about 1900-1500 BC in the general literature, and later "
                "still after Wu Xiaohong's 2007 work on lower-layer samples. There is also "
                "a middle position: Liu Li and Chen Xingcan read phase II as state-level "
                "organisation but prefer the neutral label 'the Erlitou State', on the "
                "grounds that Chinese scholarship has spent too much effort on dynastic "
                "labelling and too little on craft production and settlement patterns.",
      alternatives=[
          {"label": "Erlitou is the Xia dynasty", "standing": "minority",
           "note": "Held by most Chinese scholars and some overseas. The Chronology Project "
                   "assigned all four Erlitou phases to Xia and dated Xia's start to c. 2070 "
                   "BCE.",
           "source_ids": [S_CHEN_CHUN, S_LILIU_2009]},
      ],
      caveats=[{"kind": "contested-existence",
                "text": "Most overseas scholars hold that Erlitou cannot be identified as Xia "
                        "without contemporaneous writing. Shang oracle bones show no sign of "
                        "a Xia concept; the name first appears in Zhou texts.",
                "source_ids": [S_CHEN_CHUN, S_LILIU_2009]}],
      # Erlitou outlasting the legendary era's end is the dispute, not an error:
      # the site is still occupied past the traditional Xia-Shang boundary.
      allow_outside_parent_dates=True,
      as_of=CHECKED,
      source_ids=[S_LILIU_2009, S_CHEN_CHUN, S_LAWLER_SCIENCE, S_ESCHOLAR_ERLITOU])

    # ------------------------------------------------------------ Korea

    ERA("chulmun", "Chulmun Period", kor, -6000, -1500, "foundational",
        summary="Korea's Neolithic: comb-patterned pottery, coastal foraging, and the "
                "slow arrival of millet from northeast China.",
        aliases=["Jeulmun pottery period"],
        start_dating_method=C14, end_dating_method=C14, standing="majority",
        date_precision="disputed",
        date_note="Schemes disagree on both ends. A four-phase calendar scheme runs "
                  "7500-1300 BC; a three-phase cal BP scheme runs 7500-3400 cal BP; another "
                  "source puts the Korean Neolithic's start near 10,000 BP. The range here "
                  "is a conservative middle of the published schemes, not an average of them.",
        source_ids=[S_KOREANIC, S_KOREA_CA])

    P("chulmun-millet", "Arrival of Millet in Korea", f"{kor}.chulmun", -3640, -2970,
      "specialist",
      summary="Foxtail and broomcorn millet reach the peninsula from northeast China, "
              "Korea's first cultivated cereals and some two millennia before rice.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="The earliest secure direct AMS date on a millet grain is 3640-3370 cal BC. "
                "Corroborating grains date to 3520, 3360 and 2970 cal BC. A 2025 Bayesian "
                "estimate gives a much wider 90% interval of 5772-3490 cal BCE, which is an "
                "uncertainty range and not a claim of an earlier arrival.",
      source_ids=[S_STEVENS_FULLER, S_KYUSHU_NEASIA])

    ERA("mumun", "Mumun Period", kor, -1500, -300, "foundational",
        summary="Korea's Bronze Age transition: undecorated pottery, megalithic burial, and "
                "the arrival of paddy rice from the Liaodong route.",
        aliases=["Mumun pottery period"],
        start_dating_method=C14, end_dating_method=C14, standing="majority",
        date_note="Commonly given as 1500-300 BC, with early Mumun 1500-800 BC and middle "
                  "Mumun 800-400 BC. Three directly AMS-dated middle Mumun individuals fall "
                  "at 770-410 cal BC.",
        source_ids=[S_MUMUN_HANYANG, S_BALE_THESIS, S_KOREANIC])

    P("mumun-rice", "Arrival of Rice in Korea", f"{kor}.mumun", -1500, -1000, "specialist",
      summary="Paddy rice reaches Korea by a Shandong-Liaodong route, the agricultural "
              "change that would shortly cross to Japan and begin the Yayoi.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="disputed",
      date_note="Associated with the start of Mumun around 1500 BCE, or about 1300 BCE on "
                "an archaeolinguistic reading. The earliest directly dated rice grains, from "
                "Oun-1 at Jinju, are calibrated two different ways from the SAME samples: "
                "2860-1320 cal BC by one treatment and 1950-1000 cal BC by another.",
      caveats=[{"kind": "misconception",
                "text": "Claims of Pleistocene rice in Korea, such as Sorori at 17,000-13,000 "
                        "BP, describe disputed 'quasi-rice' and are not evidence of "
                        "cultivation.",
                "source_ids": [S_KOREANIC]}],
      source_ids=[S_KOREANIC, S_STEVENS_FULLER])

    # ------------------------------------------------------------ Japan

    P("sannai-maruyama", "Sannai Maruyama", jom, -3950, -2350, "intermediate",
      summary="A large, long-lived Jomon settlement with monumental timber posts and "
              "long-distance exchange, built by people who were not farmers.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Occupied about 5900-4300 cal BP, corroborated across four independently "
                "published sources.",
      caveats=[{"kind": "misconception",
                "text": "Its scale is often read as implying agriculture. The economy was "
                        "foraging-based, which is precisely why the site matters for arguments "
                        "about sedentism without farming.",
                "source_ids": [S_SANNAI_HABU]}],
      source_ids=[S_SANNAI_HABU])

    P("jomon-decline", "The Late Jomon Population Decline", jom, -2470, -1250, "specialist",
      summary="A sustained demographic contraction across the Japanese archipelago, "
              "centuries before wet rice arrived.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_note="Summed radiocarbon probability over 1,598 Late Jomon dates (4420-3220 cal "
                "BP) and 1,462 Final Jomon dates (3220-2300 cal BP) shows decline and "
                "plateau, with regional troughs at 3900-3800 cal BP in Kanto and 3800-3500 "
                "cal BP in Aomori and Hokkaido.",
      caveats=[{"kind": "misconception",
                "text": "Koyama's often-quoted population figures are site-density "
                        "extrapolations, not counts derived from dated remains. The "
                        "radiocarbon curve is the citable evidence for the timing.",
                "source_ids": [S_JOMON_PLOS]}],
      source_ids=[S_JOMON_PLOS])

    EVENT("yayoi-redating", "The Yayoi Redating Controversy", "east-asia.japan.yayoi",
          -1000, -400, "intermediate",
          summary="In 2003 a national museum used AMS dating to move the start of the Yayoi "
                  "back five centuries, and the field has still not settled where it lands.",
          start_dating_method=C14, end_dating_method=C14, standing="majority",
          date_precision="disputed",
          date_note="The traditional start was the 5th-4th century BCE. In May 2003 the "
                    "National Museum of Japanese History dated charred residue on pottery and "
                    "argued for the 10th century BCE. Positions since: no earlier than the "
                    "9th century (Miyamoto); no earlier than the 8th (Takesue, Shoda); "
                    "outright rejection and retention of the 5th (Takakura, Hashiguchi). By "
                    "2010 most Japanese archaeologists had accepted the direction of the "
                    "shift without agreeing on its size.",
          alternatives=[
              {"label": "10th century BCE (NMJH, 2003)", "standing": "minority",
               "start_year": -1000, "end_year": -901, "dating_method": C14,
               "note": "The original proposal, from AMS dates on charred residue. Supported "
                       "in direction by paddy-field dating in northern Kyushu.",
               "source_ids": [S_SHODA_SEAA]},
              {"label": "9th-8th century BCE", "standing": "majority",
               "start_year": -900, "end_year": -701, "dating_method": C14,
               "note": "Miyamoto allows no earlier than the 9th century; Takesue and Shoda no "
                       "earlier than the 8th, on cross-dating rather than AMS.",
               "source_ids": [S_SHODA_2010]},
              {"label": "Traditional 5th century BCE", "standing": "superseded",
               "start_year": -500, "end_year": -401, "dating_method": "typological",
               "note": "The pre-2003 consensus, retained by Takakura and Hashiguchi, who "
                       "rejected the redating outright.",
               "source_ids": [S_SHODA_SEAA]},
          ],
          caveats=[{"kind": "misconception",
                    "text": "Not a dispute about whether AMS dating works. The criticisms are "
                            "that the redating altered the type-definitions it depended on, "
                            "and that the pottery itself was misidentified.",
                    "source_ids": [S_SHODA_2010, S_SHODA_SEAA]}],
          # Starting before its own parent period is the entire point.
          allow_outside_parent_dates=True,
          as_of=CHECKED,
          source_ids=[S_SHODA_2010, S_SHODA_SEAA])
