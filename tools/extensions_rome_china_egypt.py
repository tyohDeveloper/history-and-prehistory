"""Extension module: adds Roman emperors, Byzantine emperors, Chinese emperors,
and Egyptian pharaohs (comprehensive) to the entities list.

Invoked from build_data.py after the main definitions have been added.
The function extend(E, entities, egypt, rome, cn) is called with references
to the E() helper and the entities list, plus the ID prefixes.
"""

def extend(E, rome, cn, egypt):
    # =========================================================================
    # ROMAN EMPERORS
    # =========================================================================

    def R(slug, name, parent, s, e, tier="specialist", summary=None, aliases=None):
        kw = {}
        if summary: kw["summary"] = summary
        if aliases: kw["aliases"] = aliases
        E(f"{rome}.empire.{slug}", "reign", name, parent, start=s, end=e, tier=tier, **kw)

    # Julio-Claudian (already have augustus, nero)
    jc = f"{rome}.empire.julio-claudian"
    R("tiberius",         "Tiberius",           jc, 14,   37, "intermediate", "Augustus's stepson and successor.")
    R("caligula",         "Caligula",           jc, 37,   41, "foundational", "Notorious for cruelty; assassinated by the Praetorian Guard.", ["Gaius"])
    R("claudius",         "Claudius",           jc, 41,   54, "foundational", "Conquered Britain (43 CE).")

    # Year of the Four Emperors
    y4 = f"{rome}.empire.year-of-four"
    E(y4, "period", "Year of the Four Emperors", f"{rome}.empire", start=69, end=69, tier="intermediate")
    R("galba",     "Galba",     y4, 68, 69)
    R("otho",      "Otho",      y4, 69, 69)
    R("vitellius", "Vitellius", y4, 69, 69)

    # Flavian
    fl = f"{rome}.empire.flavian"
    R("vespasian", "Vespasian", fl, 69, 79, "foundational", "Founded the Flavian dynasty; began the Colosseum.")
    R("titus",     "Titus",     fl, 79, 81, "intermediate",  "Vesuvius erupted (79 CE) during his reign; destroyed Jerusalem (70 CE).")
    R("domitian",  "Domitian",  fl, 81, 96, "intermediate")

    # Nerva-Antonine (already have trajan, hadrian, marcus-aurelius)
    na = f"{rome}.empire.nerva-antonine"
    R("nerva",           "Nerva",           na, 96,  98, "intermediate")
    R("antoninus-pius",  "Antoninus Pius",  na, 138, 161, "intermediate")
    R("lucius-verus",    "Lucius Verus",    na, 161, 169, "specialist", "Co-emperor with Marcus Aurelius.")
    R("commodus",        "Commodus",        na, 180, 192, "foundational", "Son of Marcus Aurelius; his reign is often cited as the start of Rome's decline.")

    # Year of the Five Emperors
    y5 = f"{rome}.empire.year-of-five"
    E(y5, "period", "Year of the Five Emperors", f"{rome}.empire", start=193, end=193, tier="specialist")
    R("pertinax",         "Pertinax",         y5, 193, 193)
    R("didius-julianus",  "Didius Julianus",  y5, 193, 193)
    R("pescennius-niger", "Pescennius Niger", y5, 193, 194)
    R("clodius-albinus",  "Clodius Albinus",  y5, 193, 197)

    # Severan
    sv = f"{rome}.empire.severan"
    E(sv, "period", "Severan Dynasty", f"{rome}.empire", start=193, end=235, tier="intermediate")
    R("septimius-severus", "Septimius Severus", sv, 193, 211, "intermediate", "African-born emperor; expanded to Mesopotamia.")
    R("caracalla",         "Caracalla",         sv, 198, 217, "foundational", "Extended Roman citizenship to all free inhabitants (Constitutio Antoniniana, 212).")
    R("geta",              "Geta",              sv, 209, 211)
    R("macrinus",          "Macrinus",          sv, 217, 218)
    R("elagabalus",        "Elagabalus",        sv, 218, 222, "intermediate")
    R("severus-alexander", "Severus Alexander", sv, 222, 235, "intermediate")

    # Crisis of the Third Century
    c3 = f"{rome}.empire.crisis-of-third-century"
    E(c3, "period", "Crisis of the Third Century", f"{rome}.empire", start=235, end=284, tier="foundational",
      summary="Fifty years of civil war, plague, and near-collapse.")
    R("maximinus-thrax",     "Maximinus Thrax",       c3, 235, 238)
    R("gordian-i",           "Gordian I",             c3, 238, 238)
    R("gordian-ii",          "Gordian II",            c3, 238, 238)
    R("pupienus",            "Pupienus",              c3, 238, 238)
    R("balbinus",            "Balbinus",              c3, 238, 238)
    R("gordian-iii",         "Gordian III",           c3, 238, 244)
    R("philip-arab",         "Philip the Arab",       c3, 244, 249)
    R("decius",              "Decius",                c3, 249, 251, "intermediate", "First empire-wide persecution of Christians.")
    R("trebonianus-gallus",  "Trebonianus Gallus",    c3, 251, 253)
    R("aemilianus",          "Aemilianus",            c3, 253, 253)
    R("valerian",            "Valerian",              c3, 253, 260, "foundational", "Captured alive by the Sasanian king Shapur I.")
    R("gallienus",           "Gallienus",             c3, 253, 268, "intermediate")
    R("claudius-gothicus",   "Claudius II Gothicus",  c3, 268, 270)
    R("quintillus",          "Quintillus",            c3, 270, 270)
    R("aurelian",            "Aurelian",              c3, 270, 275, "foundational", "Restored the empire; reconquered Palmyra and the Gallic Empire.")
    R("tacitus",             "Tacitus",               c3, 275, 276)
    R("florianus",           "Florianus",             c3, 276, 276)
    R("probus",              "Probus",                c3, 276, 282)
    R("carus",               "Carus",                 c3, 282, 283)
    R("carinus",             "Carinus",               c3, 283, 285)
    R("numerian",            "Numerian",              c3, 283, 284)

    # Dominate / Tetrarchy
    dt = f"{rome}.empire.dominate-tetrarchy"
    E(dt, "period", "Dominate / Tetrarchy", f"{rome}.empire", start=284, end=324, tier="intermediate")
    R("diocletian",       "Diocletian",       dt, 284, 305, "foundational", "Founded the Tetrarchy; ended the third-century crisis. Last major persecution of Christians.")
    R("maximian",         "Maximian",         dt, 286, 305, "intermediate")
    R("galerius",         "Galerius",         dt, 305, 311)
    R("constantius-i",    "Constantius I",    dt, 305, 306)
    R("severus-ii",       "Severus II",       dt, 306, 307)
    R("maxentius",        "Maxentius",        dt, 306, 312, "intermediate", "Defeated by Constantine at the Milvian Bridge (312).")
    R("licinius",         "Licinius",         dt, 308, 324, "intermediate", "Co-issued the Edict of Milan (313) legalizing Christianity.")

    # Constantinian (already have constantine)
    cn_dyn = f"{rome}.empire.constantinian"
    E(cn_dyn, "period", "Constantinian Dynasty", f"{rome}.empire", start=306, end=363, tier="foundational")
    R("constantine-ii",   "Constantine II",   cn_dyn, 337, 340)
    R("constans-i",       "Constans I",       cn_dyn, 337, 350)
    R("constantius-ii",   "Constantius II",   cn_dyn, 337, 361)
    R("julian",           "Julian the Apostate", cn_dyn, 361, 363, "foundational", "Last non-Christian emperor; briefly attempted to restore traditional Roman religion.")
    R("jovian",           "Jovian",           cn_dyn, 363, 364)

    # Valentinianic-Theodosian
    vt = f"{rome}.empire.valentinianic-theodosian"
    E(vt, "period", "Valentinianic & Theodosian Dynasties", f"{rome}.empire", start=364, end=457, tier="intermediate")
    R("valentinian-i",   "Valentinian I",   vt, 364, 375)
    R("valens",          "Valens",          vt, 364, 378, "foundational", "Killed at the Battle of Adrianople (378).")
    R("gratian",         "Gratian",         vt, 375, 383)
    R("valentinian-ii",  "Valentinian II",  vt, 375, 392)
    R("theodosius-i",    "Theodosius I the Great", vt, 379, 395, "foundational", "Made Nicene Christianity the state religion; last emperor of a united empire.")
    R("arcadius",        "Arcadius (East)", vt, 395, 408, "intermediate", "First separate Eastern Roman emperor.")
    R("honorius",        "Honorius (West)", vt, 395, 423, "foundational", "On his watch, Rome was sacked by Alaric's Visigoths (410).")
    R("theodosius-ii",   "Theodosius II (East)", vt, 408, 450, "intermediate", "Built the Theodosian Walls of Constantinople.")
    R("marcian",         "Marcian (East)", vt, 450, 457)

    # Western collapse
    wc = f"{rome}.empire.western-collapse"
    E(wc, "period", "Western Collapse", f"{rome}.empire", start=455, end=480, tier="foundational",
      allow_outside_parent_dates=True,
      date_note="476 marks Romulus Augustulus's deposition in the West; Julius Nepos was still recognized in the East until 480.")
    R("valentinian-iii", "Valentinian III (West)", wc, 425, 455, "intermediate")
    R("petronius-maximus", "Petronius Maximus", wc, 455, 455)
    R("avitus",          "Avitus",          wc, 455, 456)
    R("majorian",        "Majorian",        wc, 457, 461)
    R("libius-severus",  "Libius Severus",  wc, 461, 465)
    R("anthemius",       "Anthemius",       wc, 467, 472)
    R("olybrius",        "Olybrius",        wc, 472, 472)
    R("glycerius",       "Glycerius",       wc, 473, 474)
    R("julius-nepos",    "Julius Nepos",    wc, 474, 480, "intermediate", "Recognized in the East until 480.")
    E(f"{rome}.empire.romulus-augustulus", "reign", "Romulus Augustulus", wc,
      start=475, end=476, tier="foundational",
      date_precision="traditional",
      summary="Traditionally counted as the last Western Roman emperor; deposed by Odoacer in 476 CE. Modern scholarship notes Julius Nepos was still recognized in the East until 480.")

    # =========================================================================
    # BYZANTINE EMPERORS (major ones)
    # =========================================================================

    byz = "europe.mediterranean.byzantine"
    def B(slug, name, s, e, tier="specialist", summary=None):
        kw = {}
        if summary: kw["summary"] = summary
        E(f"{byz}.{slug}", "reign", name, byz, start=s, end=e, tier=tier, **kw)

    B("anastasius-i",       "Anastasius I",        491, 518)
    B("justin-i",           "Justin I",            518, 527)
    B("justin-ii",          "Justin II",           565, 578)
    B("tiberius-ii",        "Tiberius II Constantine", 578, 582)
    B("maurice",            "Maurice",             582, 602, "intermediate")
    B("phocas",             "Phocas",              602, 610)
    B("heraclius",          "Heraclius",           610, 641, "foundational", "Defeated Sasanian Persia (622-628); Arab conquests began at end of reign.")
    B("constans-ii",        "Constans II",         641, 668)
    B("constantine-iv",     "Constantine IV",      668, 685, "intermediate", "Repelled the First Arab Siege of Constantinople (674-678).")
    B("justinian-ii",       "Justinian II",        685, 711)
    B("leo-iii",            "Leo III the Isaurian", 717, 741, "foundational", "Repelled the Second Arab Siege of Constantinople (717-718); began Iconoclasm.")
    B("constantine-v",      "Constantine V",       741, 775)
    B("irene",              "Irene of Athens",     797, 802, "intermediate", "First woman to rule Byzantium in her own name.")
    B("basil-i",            "Basil I",             867, 886, "intermediate", "Founded the Macedonian dynasty.")
    B("leo-vi",             "Leo VI the Wise",     886, 912)
    B("constantine-vii",    "Constantine VII Porphyrogenitus", 913, 959, "intermediate", "Scholar-emperor; wrote De Administrando Imperio.")
    B("nikephoros-ii",      "Nikephoros II Phokas", 963, 969)
    B("john-i-tzimiskes",   "John I Tzimiskes",    969, 976)
    B("basil-ii",           "Basil II the Bulgar-Slayer", 976, 1025, "foundational", "Presided over Byzantium at its medieval peak.")
    B("romanos-iv",         "Romanos IV Diogenes", 1068, 1071, "intermediate", "Captured at Manzikert (1071).")
    B("alexios-i",          "Alexios I Komnenos",  1081, 1118, "foundational", "Requested Western aid, sparking the First Crusade.")
    B("john-ii",            "John II Komnenos",    1118, 1143)
    B("manuel-i",           "Manuel I Komnenos",   1143, 1180, "intermediate")
    B("andronikos-i",       "Andronikos I Komnenos", 1183, 1185)
    B("isaac-ii",           "Isaac II Angelos",    1185, 1195)
    B("alexios-iii",        "Alexios III Angelos", 1195, 1203)
    B("alexios-iv",         "Alexios IV Angelos",  1203, 1204)
    B("michael-viii",       "Michael VIII Palaiologos", 1261, 1282, "foundational", "Reconquered Constantinople from the Latin Empire (1261).")
    B("andronikos-ii",      "Andronikos II Palaiologos", 1282, 1328)
    B("john-v",             "John V Palaiologos",  1341, 1391)
    B("john-vi",            "John VI Kantakouzenos", 1347, 1354)
    B("manuel-ii",          "Manuel II Palaiologos", 1391, 1425, "intermediate", "Toured Western Europe seeking help against the Ottomans.")
    B("john-viii",          "John VIII Palaiologos", 1425, 1448)

    # =========================================================================
    # CHINESE EMPERORS
    # =========================================================================

    def C(slug, name, parent, s, e, tier="specialist", summary=None):
        kw = {}
        if summary: kw["summary"] = summary
        E(f"{parent}.{slug}", "reign", name, parent, start=s, end=e, tier=tier, **kw)

    # Qin (already have shi-huang)
    C("er-shi",  "Qin Er Shi",  f"{cn}.qin", -210, -207, "intermediate", "Second and last Qin emperor.")
    C("ziying",  "Ziying",      f"{cn}.qin", -207, -206)

    # Western Han (already have gaozu, wu)
    wh = f"{cn}.han.western"
    C("hui",         "Emperor Hui",         wh, -195, -188)
    C("lu-empress",  "Empress Dowager Lü",  wh, -188, -180, "intermediate", "De facto ruler as regent.")
    C("wen-han",     "Emperor Wen",         wh, -180, -157, "intermediate")
    C("jing",        "Emperor Jing",        wh, -157, -141)
    C("zhao",        "Emperor Zhao",        wh, -87,  -74)
    C("xuan",        "Emperor Xuan",        wh, -74,  -49, "intermediate")
    C("yuan-han",    "Emperor Yuan",        wh, -49,  -33)
    C("cheng-han",   "Emperor Cheng",       wh, -33,  -7)
    C("ai-han",      "Emperor Ai",          wh, -7,   -1)
    C("ping-han",    "Emperor Ping",        wh, -1,   6)
    C("ruzi-ying",   "Ruzi Ying",           wh, 6,    9)

    # Xin
    C("wang-mang",   "Wang Mang",           f"{cn}.han.xin", 9, 23, "intermediate", "Confucian scholar-usurper.")

    # Eastern Han
    eh = f"{cn}.han.eastern"
    C("guangwu",   "Emperor Guangwu",   eh, 25,  57, "intermediate", "Restored the Han after Wang Mang.")
    C("ming-han",  "Emperor Ming",      eh, 57,  75, "intermediate", "Introduced Buddhism officially to China.")
    C("zhang-han", "Emperor Zhang",     eh, 75,  88)
    C("he-han",    "Emperor He",        eh, 88,  106)
    C("shang-han", "Emperor Shang",     eh, 106, 106)
    C("an-han",    "Emperor An",        eh, 106, 125)
    C("shun-han",  "Emperor Shun",      eh, 125, 144)
    C("chong-han", "Emperor Chong",     eh, 144, 145)
    C("zhi-han",   "Emperor Zhi",       eh, 145, 146)
    C("huan-han",  "Emperor Huan",      eh, 146, 168)
    C("ling-han",  "Emperor Ling",      eh, 168, 189)
    C("shao-han",  "Emperor Shao",      eh, 189, 189)
    C("xian-han",  "Emperor Xian",      eh, 189, 220, "intermediate", "Last Han emperor; puppet of Cao Cao.")

    # Sui
    C("wen-sui",  "Emperor Wen of Sui",  f"{cn}.sui", 581, 604, "foundational", "Reunified China after nearly four centuries of division.")
    C("yang-sui", "Emperor Yang of Sui", f"{cn}.sui", 604, 618, "intermediate", "Completed the Grand Canal; overreach doomed the dynasty.")
    C("gong-sui", "Emperor Gong of Sui", f"{cn}.sui", 617, 618)

    # Tang (already have taizong, wu-zetian, xuanzong)
    tg = f"{cn}.tang"
    C("gaozu-tang",     "Emperor Gaozu",     tg, 618, 626, "intermediate", "Founded the Tang.")
    C("gaozong-tang",   "Emperor Gaozong",   tg, 649, 683)
    C("zhongzong",      "Emperor Zhongzong", tg, 684, 710)
    C("ruizong",        "Emperor Ruizong",   tg, 684, 690)
    C("suzong-tang",    "Emperor Suzong",    tg, 756, 762, "intermediate", "Reigned during the An Lushan Rebellion.")
    C("daizong-tang",   "Emperor Daizong",   tg, 762, 779)
    C("dezong-tang",    "Emperor Dezong",    tg, 779, 805)
    C("shunzong-tang",  "Emperor Shunzong",  tg, 805, 805)
    C("xianzong-tang",  "Emperor Xianzong",  tg, 805, 820)
    C("muzong-tang",    "Emperor Muzong",    tg, 820, 824)
    C("jingzong-tang",  "Emperor Jingzong",  tg, 824, 826)
    C("wenzong-tang",   "Emperor Wenzong",   tg, 826, 840)
    C("wuzong-tang",    "Emperor Wuzong",    tg, 840, 846, "intermediate", "Great Anti-Buddhist Persecution (845).")
    C("xuanzong-later", "Emperor Xuānzong (later)", tg, 846, 859)
    C("yizong-tang",    "Emperor Yizong",    tg, 859, 873)
    C("xizong-tang",    "Emperor Xizong",    tg, 873, 888)
    C("zhaozong-tang",  "Emperor Zhaozong",  tg, 888, 904)
    C("ai-tang",        "Emperor Ai of Tang", tg, 904, 907, "intermediate", "Last Tang emperor.")

    # Song
    ns = f"{cn}.song.northern"
    C("taizu-song",    "Emperor Taizu",    ns, 960,  976, "foundational", "Founded the Song dynasty.")
    C("taizong-song",  "Emperor Taizong",  ns, 976,  997)
    C("zhenzong",      "Emperor Zhenzong", ns, 997,  1022)
    C("renzong-song",  "Emperor Renzong",  ns, 1022, 1063, "intermediate")
    C("yingzong-song", "Emperor Yingzong", ns, 1063, 1067)
    C("shenzong-song", "Emperor Shenzong", ns, 1067, 1085, "intermediate", "Backed Wang Anshi's controversial New Policies reforms.")
    C("zhezong",       "Emperor Zhezong",  ns, 1085, 1100)
    C("huizong-song",  "Emperor Huizong",  ns, 1100, 1126, "foundational", "Artist-emperor; his reign ended with the Jurchen sack of Kaifeng.")
    C("qinzong",       "Emperor Qinzong",  ns, 1126, 1127, "intermediate", "Captured by the Jurchens in the Jingkang Incident.")

    ss = f"{cn}.song.southern"
    C("gaozong-song",  "Emperor Gaozong",  ss, 1127, 1162, "intermediate", "Founded the Southern Song at Lin'an (Hangzhou).")
    C("xiaozong-song", "Emperor Xiaozong", ss, 1162, 1189)
    C("guangzong",     "Emperor Guangzong", ss, 1189, 1194)
    C("ningzong-song", "Emperor Ningzong", ss, 1194, 1224)
    C("lizong",        "Emperor Lizong",   ss, 1224, 1264)
    C("duzong",        "Emperor Duzong",   ss, 1264, 1274)
    C("gong-song",     "Emperor Gong of Song", ss, 1274, 1276)
    C("duanzong",      "Emperor Duanzong", ss, 1276, 1278)
    C("bing-song",     "Emperor Bing",     ss, 1278, 1279, "intermediate", "Last Song emperor; drowned at the Battle of Yamen.")

    # Yuan (already have kublai)
    y = f"{cn}.yuan"
    C("chengzong-yuan", "Temür Khan (Chengzong)", y, 1294, 1307)
    C("wuzong-yuan",    "Külüg Khan (Wuzong)",    y, 1307, 1311)
    C("renzong-yuan",   "Buyantu Khan (Renzong)", y, 1311, 1320)
    C("yingzong-yuan",  "Gegeen Khan (Yingzong)", y, 1320, 1323)
    C("taiding",        "Yesün Temür (Taiding)",  y, 1323, 1328)
    C("tianshun-yuan",  "Ragibagh Khan",          y, 1328, 1328)
    C("wenzong-yuan",   "Tugh Temür (Wenzong)",   y, 1328, 1332)
    C("mingzong-yuan",  "Kusala (Mingzong)",      y, 1329, 1329)
    C("ningzong-yuan",  "Rinchinbal (Ningzong)",  y, 1332, 1332)
    C("huizong-yuan",   "Toghon Temür (Huizong)", y, 1333, 1370, "intermediate", "Last Yuan emperor of China; expelled to Mongolia.")

    # Ming (already have hongwu, yongle)
    m = f"{cn}.ming"
    C("jianwen",       "Jianwen Emperor",   m, 1398, 1402, "intermediate", "Deposed by his uncle, the future Yongle Emperor.")
    C("hongxi",        "Hongxi Emperor",    m, 1424, 1425)
    C("xuande",        "Xuande Emperor",    m, 1425, 1435, "intermediate")
    C("zhengtong",     "Zhengtong Emperor", m, 1435, 1449, "intermediate", "Captured by the Mongols in the Tumu Crisis (1449); later restored.")
    C("jingtai",       "Jingtai Emperor",   m, 1449, 1457)
    C("tianshun-ming", "Tianshun Emperor",  m, 1457, 1464, "intermediate", "Same person as Zhengtong, restored after Jingtai.")
    C("chenghua",      "Chenghua Emperor",  m, 1464, 1487)
    C("hongzhi",       "Hongzhi Emperor",   m, 1487, 1505, "intermediate", "Model Confucian ruler.")
    C("zhengde",       "Zhengde Emperor",   m, 1505, 1521)
    C("jiajing",       "Jiajing Emperor",   m, 1521, 1567, "intermediate")
    C("longqing",      "Longqing Emperor",  m, 1567, 1572)
    C("wanli",         "Wanli Emperor",     m, 1572, 1620, "foundational", "Longest-reigning Ming emperor.")
    C("taichang",      "Taichang Emperor",  m, 1620, 1620)
    C("tianqi",        "Tianqi Emperor",    m, 1620, 1627)
    C("chongzhen",     "Chongzhen Emperor", m, 1627, 1644, "foundational", "Last Ming emperor; hanged himself as Beijing fell.")

    # Qing (already have kangxi, qianlong, cixi)
    q = f"{cn}.qing"
    C("shunzhi",   "Shunzhi Emperor",   q, 1644, 1661, "intermediate", "First Qing emperor to rule over China proper.")
    C("yongzheng", "Yongzheng Emperor", q, 1722, 1735, "intermediate")
    C("jiaqing",   "Jiaqing Emperor",   q, 1796, 1820)
    C("daoguang",  "Daoguang Emperor",  q, 1820, 1850, "intermediate", "Reigned during the First Opium War (1839-1842).")
    C("xianfeng",  "Xianfeng Emperor",  q, 1850, 1861, "intermediate", "Reigned during the Taiping Rebellion and Second Opium War.")
    C("tongzhi",   "Tongzhi Emperor",   q, 1861, 1875)
    C("guangxu",   "Guangxu Emperor",   q, 1875, 1908, "intermediate", "Attempted the Hundred Days' Reform (1898).")
    C("xuantong",  "Xuantong Emperor (Puyi)", q, 1908, 1912, "foundational", "Last emperor of China; later puppet ruler of Manchukuo.")

    # =========================================================================
    # EGYPTIAN PHARAOHS
    # =========================================================================

    def P(slug, name, parent, s, e, tier="specialist", summary=None, aliases=None):
        kw = {}
        if summary: kw["summary"] = summary
        if aliases: kw["aliases"] = aliases
        E(f"{parent}.{slug}", "reign", name, parent, start=s, end=e, tier=tier, **kw)

    # 1st Dynasty (already have narmer)
    d1 = f"{egypt}.early-dynastic.dyn1"
    P("hor-aha",   "Hor-Aha",   d1, -3080, -3050)
    P("djer",      "Djer",      d1, -3050, -3000)
    P("djet",      "Djet",      d1, -3000, -2990)
    P("merneith",  "Merneith (regent)", d1, -2990, -2980, "intermediate", "Possibly the earliest attested female Egyptian ruler.")
    P("den",       "Den",       d1, -2985, -2930)
    P("anedjib",   "Anedjib",   d1, -2930, -2925)
    P("semerkhet", "Semerkhet", d1, -2925, -2915)
    P("qa-a",      "Qa'a",      d1, -2915, -2890)

    # 2nd Dynasty
    d2 = f"{egypt}.early-dynastic.dyn2"
    P("hotepsekhemwy", "Hotepsekhemwy", d2, -2890, -2865)
    P("raneb",         "Raneb",         d2, -2865, -2825)
    P("nynetjer",      "Nynetjer",      d2, -2825, -2780)
    P("peribsen",      "Peribsen",      d2, -2740, -2730)
    P("khasekhemwy",   "Khasekhemwy",   d2, -2725, -2686, "intermediate", "Reunified Egypt after internal conflict.")

    # 3rd Dynasty (already have djoser)
    d3 = f"{egypt}.old-kingdom.dyn3"
    P("sanakht",    "Sanakht",    d3, -2686, -2667)
    P("sekhemkhet", "Sekhemkhet", d3, -2648, -2640)
    P("khaba",      "Khaba",      d3, -2640, -2637)
    P("huni",       "Huni",       d3, -2637, -2613)

    # 4th Dynasty (already have sneferu, khufu, khafre, menkaure)
    d4 = f"{egypt}.old-kingdom.dyn4"
    P("djedefre",   "Djedefre",   d4, -2566, -2558)
    P("shepseskaf", "Shepseskaf", d4, -2503, -2498)

    # 5th Dynasty
    d5 = f"{egypt}.old-kingdom.dyn5"
    P("userkaf",     "Userkaf",           d5, -2494, -2487)
    P("sahure",      "Sahure",            d5, -2487, -2475)
    P("neferirkare", "Neferirkare Kakai", d5, -2475, -2455)
    P("shepseskare", "Shepseskare",       d5, -2455, -2448)
    P("neferefre",   "Neferefre",         d5, -2448, -2445)
    P("nyuserre",    "Nyuserre Ini",      d5, -2445, -2421)
    P("menkauhor",   "Menkauhor",         d5, -2421, -2414)
    P("djedkare",    "Djedkare Isesi",    d5, -2414, -2375)
    P("unas",        "Unas",              d5, -2375, -2345, "intermediate", "His pyramid contains the earliest Pyramid Texts.")

    # 6th Dynasty (already have pepi2)
    d6 = f"{egypt}.old-kingdom.dyn6"
    P("teti",        "Teti",       d6, -2345, -2333)
    P("userkare",    "Userkare",   d6, -2333, -2332)
    P("pepi-i",      "Pepi I",     d6, -2332, -2283)
    P("merenre-i",   "Merenre I",  d6, -2283, -2278)
    P("merenre-ii",  "Merenre II", d6, -2184, -2184)
    E(f"{d6}.nitocris", "reign", "Nitocris (traditional)", d6,
      start=-2184, end=-2181, tier="intermediate",
      date_precision="traditional",
      summary="Traditionally the earliest named female pharaoh; historicity debated.")

    # 11th Dynasty (already have mentuhotep2)
    d11 = f"{egypt}.middle-kingdom.dyn11"
    P("intef-i",        "Intef I",        d11, -2125, -2112)
    P("intef-ii",       "Intef II",       d11, -2112, -2063)
    P("intef-iii",      "Intef III",      d11, -2063, -2055)
    P("mentuhotep-iii", "Mentuhotep III", d11, -2004, -1992)
    P("mentuhotep-iv",  "Mentuhotep IV",  d11, -1992, -1985)

    # 12th Dynasty
    d12 = f"{egypt}.middle-kingdom.dyn12"
    P("amenemhat-i",   "Amenemhat I",  d12, -1985, -1956, "intermediate", "Founder of the 12th Dynasty; moved capital to Itjtawy.")
    P("senusret-i",    "Senusret I",   d12, -1956, -1911, "intermediate")
    P("amenemhat-ii",  "Amenemhat II", d12, -1911, -1877)
    P("senusret-ii",   "Senusret II",  d12, -1877, -1870)
    P("senusret-iii",  "Senusret III", d12, -1870, -1831, "foundational", "Great warrior-king; conquered Nubia. Sometimes identified with the legendary 'Sesostris'.")
    P("amenemhat-iii", "Amenemhat III", d12, -1831, -1786, "intermediate", "Prosperous long reign; built the Labyrinth at Hawara.")
    P("amenemhat-iv",  "Amenemhat IV", d12, -1786, -1777)
    P("sobekneferu",   "Sobekneferu",  d12, -1777, -1773, "intermediate", "First fully confirmed female pharaoh.")

    # 15th Dynasty (Hyksos)
    d15 = f"{egypt}.sip.dyn15-hyksos"
    P("salitis", "Salitis (Hyksos)", d15, -1650, -1630)
    P("khyan",   "Khyan (Hyksos)",   d15, -1610, -1580)
    P("apepi",   "Apepi (Hyksos)",   d15, -1590, -1550, "intermediate")

    # 18th Dynasty (already have ahmose1, hatshepsut, thutmose3, amenhotep3, akhenaten, tutankhamun)
    d18 = f"{egypt}.new-kingdom.dyn18"
    P("amenhotep-i",    "Amenhotep I",    d18, -1525, -1504)
    P("thutmose-i",     "Thutmose I",     d18, -1504, -1492, "intermediate", "First pharaoh buried in the Valley of the Kings.")
    P("thutmose-ii",    "Thutmose II",    d18, -1492, -1479)
    P("amenhotep-ii",   "Amenhotep II",   d18, -1425, -1400)
    P("thutmose-iv",    "Thutmose IV",    d18, -1400, -1390)
    P("smenkhkare",     "Smenkhkare",     d18, -1335, -1334, "intermediate", "Amarna-era co-ruler with Akhenaten; identity debated.")
    P("neferneferuaten", "Neferneferuaten", d18, -1334, -1332, "intermediate", "Possibly Nefertiti or Meritaten ruling as pharaoh.")
    P("ay",             "Ay",             d18, -1323, -1319)
    P("horemheb",       "Horemheb",       d18, -1319, -1292, "intermediate", "General who erased the Amarna heresy from official records.")

    # 19th Dynasty (already have seti1, ramesses2)
    d19 = f"{egypt}.new-kingdom.dyn19"
    P("ramesses-i", "Ramesses I", d19, -1295, -1294)
    P("merneptah",  "Merneptah",  d19, -1213, -1203, "intermediate", "His stele contains the earliest extra-biblical mention of Israel.")
    P("amenmesse",  "Amenmesse",  d19, -1203, -1200)
    P("seti-ii",    "Seti II",    d19, -1200, -1194)
    P("siptah",     "Siptah",     d19, -1194, -1188)
    P("tausret",    "Tausret",    d19, -1188, -1186, "intermediate", "Last ruler of the 19th Dynasty; female pharaoh.")

    # 20th Dynasty (already have ramesses3)
    d20 = f"{egypt}.new-kingdom.dyn20"
    P("setnakht",      "Setnakht",      d20, -1186, -1184)
    P("ramesses-iv",   "Ramesses IV",   d20, -1155, -1149)
    P("ramesses-v",    "Ramesses V",    d20, -1149, -1145)
    P("ramesses-vi",   "Ramesses VI",   d20, -1145, -1137)
    P("ramesses-vii",  "Ramesses VII",  d20, -1136, -1129)
    P("ramesses-viii", "Ramesses VIII", d20, -1129, -1126)
    P("ramesses-ix",   "Ramesses IX",   d20, -1126, -1108)
    P("ramesses-x",    "Ramesses X",    d20, -1108, -1099)
    P("ramesses-xi",   "Ramesses XI",   d20, -1099, -1069, "intermediate", "Last pharaoh of the New Kingdom.")

    # 21st Dynasty (Tanis)
    d21 = f"{egypt}.tip.dyn21"
    E(d21, "period", "21st Dynasty (Tanis)", f"{egypt}.tip", start=-1069, end=-945)
    P("smendes",       "Smendes",       d21, -1069, -1043)
    P("psusennes-i",   "Psusennes I",   d21, -1039, -991, "intermediate", "Intact silver coffin found at Tanis.")
    P("amenemope",     "Amenemope",     d21, -993,  -984)
    P("osorkon-elder", "Osorkon the Elder", d21, -984, -978)
    P("siamun",        "Siamun",        d21, -978, -959)
    P("psusennes-ii",  "Psusennes II",  d21, -959, -945)

    # 22nd Dynasty (Libyan/Bubastite)
    d22 = f"{egypt}.tip.dyn22"
    E(d22, "period", "22nd Dynasty (Libyan/Bubastite)", f"{egypt}.tip", start=-945, end=-720)
    P("shoshenq-i",   "Shoshenq I",   d22, -945, -924, "intermediate", "Sacked Jerusalem (traditional biblical 'Shishak').")
    P("osorkon-i",    "Osorkon I",    d22, -924, -889)
    P("osorkon-ii",   "Osorkon II",   d22, -872, -837)
    P("shoshenq-iii", "Shoshenq III", d22, -837, -798)

    # 25th Dynasty (Kushite) — already have piye, taharqa
    d25 = f"{egypt}.tip.dyn25-kushite"
    P("shabaka",   "Shabaka",   d25, -721, -707, "intermediate")
    P("shebitku",  "Shebitku",  d25, -707, -690)
    P("tantamani", "Tantamani", d25, -664, -656, "intermediate", "Last Kushite pharaoh of Egypt; expelled by the Assyrians.")

    # 26th Dynasty (Saite)
    d26 = f"{egypt}.late-period.dyn26-saite"
    P("psamtik-i",   "Psamtik I",   d26, -664, -610, "intermediate", "Reunified Egypt under native rule.")
    P("necho-ii",    "Necho II",    d26, -610, -595, "intermediate", "Commissioned a Phoenician circumnavigation of Africa.")
    P("psamtik-ii",  "Psamtik II",  d26, -595, -589)
    P("apries",      "Apries",      d26, -589, -570)
    P("amasis-ii",   "Amasis II",   d26, -570, -526, "intermediate")
    P("psamtik-iii", "Psamtik III", d26, -526, -525, "intermediate", "Last Saite pharaoh; defeated by Cambyses.")

    # 27th Dynasty (First Persian) — Achaemenids as pharaohs
    d27 = f"{egypt}.late-period.dyn27-persian1"
    P("cambyses-egypt",     "Cambyses II (as pharaoh)",     d27, -525, -522, "intermediate")
    P("darius-i-egypt",     "Darius I (as pharaoh)",        d27, -522, -486, "intermediate")
    P("xerxes-i-egypt",     "Xerxes I (as pharaoh)",        d27, -486, -465)
    P("artaxerxes-i-egypt", "Artaxerxes I (as pharaoh)",    d27, -465, -424)

    # 28th–30th Dynasties (native restoration)
    d28 = f"{egypt}.late-period.dyn28"
    E(d28, "period", "28th Dynasty", f"{egypt}.late-period", start=-404, end=-398)
    P("amyrtaeus", "Amyrtaeus", d28, -404, -398, "intermediate", "Sole ruler of the 28th Dynasty.")

    d29 = f"{egypt}.late-period.dyn29"
    E(d29, "period", "29th Dynasty", f"{egypt}.late-period", start=-398, end=-380)
    P("nepherites-i", "Nepherites I", d29, -398, -393)
    P("psammuthes",   "Psammuthes",   d29, -392, -391)
    P("hakor",        "Hakor",        d29, -393, -380)

    d30 = f"{egypt}.late-period.dyn30"
    E(d30, "period", "30th Dynasty", f"{egypt}.late-period", start=-380, end=-343)
    P("nectanebo-i",  "Nectanebo I",  d30, -380, -362, "intermediate")
    P("teos",         "Teos",         d30, -362, -360)
    P("nectanebo-ii", "Nectanebo II", d30, -360, -343, "foundational", "Last native Egyptian pharaoh.")

    d31 = f"{egypt}.late-period.dyn31"
    E(d31, "period", "31st Dynasty (Second Persian)", f"{egypt}.late-period", start=-343, end=-332)
    P("artaxerxes-iii-egypt", "Artaxerxes III (as pharaoh)", d31, -343, -338)
    P("darius-iii-egypt",     "Darius III (as pharaoh)",     d31, -336, -332)

    # Ptolemaic — already have ptolemy1, cleopatra7
    pt = f"{egypt}.ptolemaic"
    P("ptolemy-ii",   "Ptolemy II Philadelphus",     pt, -283, -246, "intermediate", "Commissioned the Septuagint translation of the Hebrew Bible.")
    P("ptolemy-iii",  "Ptolemy III Euergetes",       pt, -246, -222, "intermediate")
    P("ptolemy-iv",   "Ptolemy IV Philopator",       pt, -221, -204)
    P("ptolemy-v",    "Ptolemy V Epiphanes",         pt, -204, -181, "intermediate", "His decree is preserved on the Rosetta Stone.")
    P("ptolemy-vi",   "Ptolemy VI Philometor",       pt, -180, -145)
    P("ptolemy-vii",  "Ptolemy VII",                 pt, -145, -144)
    P("ptolemy-viii", "Ptolemy VIII Physcon",        pt, -170, -116)
    P("cleopatra-iii", "Cleopatra III",              pt, -142, -101)
    P("ptolemy-ix",   "Ptolemy IX Lathyros",         pt, -116, -81)
    P("ptolemy-x",    "Ptolemy X Alexander I",       pt, -110, -88)
    P("berenice-iii", "Berenice III",                pt, -81, -80)
    P("ptolemy-xi",   "Ptolemy XI Alexander II",     pt, -80, -80)
    P("ptolemy-xii",  "Ptolemy XII Auletes",         pt, -80, -51, "intermediate", "Cleopatra VII's father.")
    P("ptolemy-xiii", "Ptolemy XIII",                pt, -51, -47, "intermediate", "Co-ruler with sister Cleopatra VII; killed by Caesar.")
    P("ptolemy-xiv",  "Ptolemy XIV",                 pt, -47, -44)
    P("caesarion",    "Ptolemy XV Caesarion",        pt, -44, -30, "intermediate", "Son of Cleopatra VII and Julius Caesar; last Ptolemy.")

    # =========================================================================
    # JAPANESE SHŌGUNS — Kamakura, Muromachi (Ashikaga), and Tokugawa bakufu
    # =========================================================================
    # Shōgun = the de facto military ruler of Japan while emperors reigned
    # symbolically. Dates are the years each held the title Sei-i Taishōgun.

    def S(slug, name, native, parent, s, e, tier="specialist", summary=None, aliases=None):
        kw = {"native_name": native}
        if summary: kw["summary"] = summary
        if aliases: kw["aliases"] = aliases
        E(f"{parent}.{slug}", "reign", name, parent, start=s, end=e, tier=tier, **kw)

    # --- Kamakura shōgunate (1192–1333) ---
    # 9 shōguns: 3 Minamoto, 2 Fujiwara-shogun (Sekke), 4 imperial-prince (Miyashogun)
    ks = "east-asia.japan.kamakura"
    S("shogun-yoritomo",  "Minamoto no Yoritomo",  "源頼朝",     ks, 1192, 1199, "foundational",
      "Founder of the Kamakura bakufu and Japan's first shōgun in the enduring sense.")
    S("shogun-yoriie",    "Minamoto no Yoriie",    "源頼家",     ks, 1202, 1203, "intermediate",
      "Deposed by the Hōjō regents.")
    S("shogun-sanetomo",  "Minamoto no Sanetomo",  "源實朝",     ks, 1203, 1219, "intermediate",
      "Last Minamoto shōgun; a noted waka poet, assassinated at Tsurugaoka Hachiman-gū.")
    S("shogun-yoritsune", "Kujō Yoritsune",        "九条頼経",   ks, 1226, 1244,
      summary="First Sekke shōgun; installed as a child by the Hōjō regents.")
    S("shogun-yoritsugu", "Kujō Yoritsugu",        "九条頼嘆",   ks, 1244, 1252)
    S("shogun-munetaka",  "Prince Munetaka",       "宗尊親王",   ks, 1252, 1266,
      summary="First imperial-prince (Miya) shōgun.")
    S("shogun-koreyasu",  "Prince Koreyasu",       "惟康親王",   ks, 1266, 1289)
    S("shogun-hisaaki",   "Prince Hisaaki",        "久明親王",   ks, 1289, 1308)
    S("shogun-morikuni",  "Prince Morikuni",       "守邦親王",   ks, 1308, 1333, "intermediate",
      "Last Kamakura shōgun; deposed when the bakufu fell to Emperor Go-Daigo's forces.")

    # --- Ashikaga (Muromachi) shōgunate (1338–1573) ---
    # 15 shōguns. Placed under the Muromachi era.
    ms = "east-asia.japan.muromachi"
    S("shogun-takauji",   "Ashikaga Takauji",      "足利尊氏",   ms, 1338, 1358, "foundational",
      "Founder of the Ashikaga bakufu; installed the Northern Court against Emperor Go-Daigo.")
    S("shogun-yoshiakira","Ashikaga Yoshiakira",   "足利義詮",   ms, 1358, 1367)
    S("shogun-yoshimitsu","Ashikaga Yoshimitsu",   "足利義満",   ms, 1368, 1394, "foundational",
      "Reunified the Northern and Southern Courts (1392); built Kinkaku-ji, the Golden Pavilion.")
    S("shogun-yoshimochi","Ashikaga Yoshimochi",   "足利義持",   ms, 1394, 1423)
    S("shogun-yoshikazu", "Ashikaga Yoshikazu",    "足利義量",   ms, 1423, 1425)
    S("shogun-yoshinori", "Ashikaga Yoshinori",    "足利義教",   ms, 1429, 1441, "intermediate",
      "Assassinated by Akamatsu Mitsusuke at the Kakitsu Incident.")
    S("shogun-yoshikatsu","Ashikaga Yoshikatsu",   "足利義勝",   ms, 1442, 1443)
    S("shogun-yoshimasa", "Ashikaga Yoshimasa",    "足利義政",   ms, 1449, 1473, "foundational",
      "Aesthete-shōgun; built Ginkaku-ji. His succession dispute triggered the Ōnin War (1467).")
    S("shogun-yoshihisa", "Ashikaga Yoshihisa",    "足利義尚",   ms, 1473, 1489)
    S("shogun-yoshitane", "Ashikaga Yoshitane",    "足利義材",   ms, 1490, 1493,
      summary="Deposed, later restored (1508–1521); dates given are of first tenure.")
    S("shogun-yoshizumi", "Ashikaga Yoshizumi",    "足利義澄",   ms, 1494, 1508)
    S("shogun-yoshitane-2","Ashikaga Yoshitane (restored)", "足利義材", ms, 1508, 1521,
      summary="Second tenure after being restored to the shōgunate.")
    S("shogun-yoshiharu", "Ashikaga Yoshiharu",    "足利義晴",   ms, 1521, 1546)
    S("shogun-yoshiteru", "Ashikaga Yoshiteru",    "足利義輝",   ms, 1546, 1565, "intermediate",
      "Renowned swordsman; killed defending himself against Matsunaga and Miyoshi forces.")
    S("shogun-yoshihide", "Ashikaga Yoshihide",    "足利義栗",   ms, 1568, 1568,
      summary="Reigned only a few months and never entered Kyoto.")
    S("shogun-yoshiaki",  "Ashikaga Yoshiaki",     "足利義昭",   ms, 1568, 1573, "intermediate",
      "Last Ashikaga shōgun; expelled from Kyoto by Oda Nobunaga.")

    # --- Tokugawa (Edo) shōgunate (1603–1867) ---
    # 15 shōguns. Placed under Edo period. Ieyasu is already present; add the rest.
    ts = "east-asia.japan.edo"
    # Ieyasu is already at east-asia.japan.edo.ieyasu — skip.
    S("shogun-hidetada",  "Tokugawa Hidetada",     "徳川秀忠",   ts, 1605, 1623, "intermediate",
      "Consolidated Tokugawa authority; enforced the persecution of Christians.")
    S("shogun-iemitsu",   "Tokugawa Iemitsu",      "徳川家光",   ts, 1623, 1651, "foundational",
      "Sealed Japan under sakoku isolation policies; suppressed the Shimabara Rebellion.")
    S("shogun-ietsuna",   "Tokugawa Ietsuna",      "徳川家綱",   ts, 1651, 1680)
    S("shogun-tsunayoshi","Tokugawa Tsunayoshi",   "徳川綱吉",   ts, 1680, 1709, "intermediate",
      "Known for the eccentric Shōrui Awaremi no Rei (compassion for living things) edicts.")
    S("shogun-ienobu",    "Tokugawa Ienobu",       "徳川家宣",   ts, 1709, 1712)
    S("shogun-ietsugu",   "Tokugawa Ietsugu",      "徳川家繼",   ts, 1713, 1716,
      summary="Died a child; ended the direct main line, opening the succession to the Kishū branch.")
    S("shogun-yoshimune", "Tokugawa Yoshimune",    "徳川吉宗",   ts, 1716, 1745, "foundational",
      "Enacted the Kyōhō Reforms; permitted the study of Dutch/Western texts.")
    S("shogun-ieshige",   "Tokugawa Ieshige",      "徳川家重",   ts, 1745, 1760)
    S("shogun-ieharu",    "Tokugawa Ieharu",       "徳川家治",   ts, 1760, 1786,
      summary="Reign dominated by chamberlain Tanuma Okitsugu's controversial commercial policies.")
    S("shogun-ienari",    "Tokugawa Ienari",       "徳川家斉",   ts, 1787, 1837, "intermediate",
      "Longest-reigning Tokugawa shōgun; Kansei Reforms under Matsudaira Sadanobu early in his reign.")
    S("shogun-ieyoshi",   "Tokugawa Ieyoshi",      "徳川家慶",   ts, 1837, 1853, "intermediate",
      "On his deathbed when Perry's Black Ships arrived (1853).")
    S("shogun-iesada",    "Tokugawa Iesada",       "徳川家定",   ts, 1853, 1858, "intermediate",
      "Signed the Harris Treaty opening Japan to foreign trade.")
    S("shogun-iemochi",   "Tokugawa Iemochi",      "徳川家茂",   ts, 1858, 1866, "intermediate",
      "Reigned during the bakumatsu crisis; died young in Osaka.")
    S("shogun-yoshinobu", "Tokugawa Yoshinobu",    "徳川慶喜",   ts, 1866, 1867, "foundational",
      "Last shōgun of Japan; resigned power to the Meiji Emperor in the Taisei Hōkan (1867).")
