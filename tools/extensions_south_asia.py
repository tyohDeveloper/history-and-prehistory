"""Extension module: comprehensive South Asian rulers.

Closes the coverage gap identified by the model-council review. Adds:
- Maurya (remaining), Gupta (all major), Chola (extended), Delhi Sultanate rulers
- Vijayanagara, Bahmani/Deccan sultanates, Bengal Sultanate
- Maratha peshwas and chhatrapatis, Sikh Empire rulers
- Mughal (remaining after already-added Babur/Akbar/Shah-Jahan/Aurangzeb)
- Late-Mughal fig-emperors
- East India Company governors-general + British Raj viceroys (key ones)
- Independence-era founders (Gandhi, Jinnah, Nehru, Ambedkar) and modern PMs

Called from build_data.py after the main extensions.
"""


from builders import make_builders


def extend(E, sa):
    R, P, ERA, EVENT, *_ = make_builders(E)

    # =========================================================================
    # MAURYA EMPIRE — remaining rulers (already have Chandragupta, Ashoka)
    # =========================================================================
    m = f"{sa}.maurya"
    R("bindusara",       "Bindusara",              m, -297, -273, "intermediate",
      "Son of Chandragupta; extended the empire to the Deccan. Father of Ashoka.")
    R("dasharatha",      "Dasharatha",             m, -232, -224)
    R("samprati",        "Samprati",               m, -224, -215,
      summary="Grandson of Ashoka; patronized Jainism.")
    R("shalishuka",      "Shalishuka",             m, -215, -202)
    R("devavarman",      "Devavarman",             m, -202, -195)
    R("shatadhanvan",    "Shatadhanvan",           m, -195, -187)
    R("brihadratha",     "Brihadratha",            m, -187, -185, "intermediate",
      "Last Maurya emperor; assassinated by his general Pushyamitra Shunga.")

    # =========================================================================
    # SHUNGA EMPIRE — rulers
    # =========================================================================
    sh = f"{sa}.shunga"
    R("pushyamitra",     "Pushyamitra Shunga",     sh, -185, -149, "intermediate",
      "Founder of the Shunga dynasty; former Maurya general.")
    R("agnimitra",       "Agnimitra",              sh, -149, -141)
    R("vasumitra",       "Vasumitra",              sh, -141, -131)
    R("bhagabhadra",     "Bhagabhadra",            sh, -110, -83)
    R("devabhuti",       "Devabhuti",              sh, -83, -73,
      summary="Last Shunga ruler; assassinated by his minister Vasudeva Kanva.")

    # =========================================================================
    # SATAVAHANA EMPIRE — major rulers
    # =========================================================================
    st = f"{sa}.satavahana"
    R("simuka",          "Simuka",                 st, -230, -207,
      summary="Traditional founder of the Satavahana dynasty in the Deccan.")
    R("satakarni-i",     "Satakarni I",            st, -180, -170, "intermediate",
      "Consolidated the Satavahana state; performed Vedic ashvamedha sacrifice.")
    R("gautamiputra",    "Gautamiputra Satakarni", st, 78, 102, "intermediate",
      "Greatest Satavahana ruler; defeated the Western Kshatrapas.")
    R("vasishthiputra",  "Vasishthiputra Pulumavi", st, 96, 130)
    R("yajna-satakarni", "Yajna Satakarni",        st, 152, 181,
      summary="Last great Satavahana emperor.")

    # =========================================================================
    # INDO-GREEK KINGDOMS — key kings
    # =========================================================================
    ig = f"{sa}.indo-greek"
    R("demetrius-i",     "Demetrius I of Bactria", ig, -200, -180, "intermediate",
      "Founder of the Indo-Greek kingdom; pushed into the Punjab.")
    R("menander-i",      "Menander I 'Soter'",     ig, -165, -130, "foundational",
      "Greatest Indo-Greek king; the Buddhist king Milinda of the Milindapañha dialogues.",
      aliases=["Milinda"])
    R("apollodotus-ii",  "Apollodotus II",         ig, -80, -65)
    R("strato-ii",       "Strato II",              ig, -25, 10,
      summary="Last known Indo-Greek king; ended by Indo-Scythian conquest.")

    # =========================================================================
    # GUPTA EMPIRE — full ruler list (already have Chandragupta II)
    # =========================================================================
    g = f"{sa}.gupta"
    R("chandragupta-i",  "Chandragupta I",         g, 319, 335, "intermediate",
      "Founder of the imperial Gupta dynasty.")
    R("samudragupta",    "Samudragupta",           g, 335, 375, "foundational",
      "Warrior-emperor who conquered much of the subcontinent; commemorated in the Allahabad Prashasti inscription.")
    R("ramagupta",       "Ramagupta",              g, 375, 380)
    R("kumaragupta-i",   "Kumaragupta I",          g, 415, 455, "intermediate",
      "Founded the Nalanda monastic university.")
    R("skandagupta",     "Skandagupta",            g, 455, 467, "intermediate",
      "Repelled the Hephthalite (White Hun) invasions; last of the great Guptas.")
    R("purugupta",       "Purugupta",              g, 467, 473)
    R("narasimhagupta",  "Narasimhagupta Baladitya", g, 495, 530,
      summary="Defeated the Hun ruler Mihirakula.")
    R("vishnugupta",     "Vishnugupta",            g, 540, 550,
      summary="Last recorded Gupta emperor.")

    # =========================================================================
    # HARSHA'S EMPIRE (7th century) — parent under Post-Gupta
    # =========================================================================
    E(f"{sa}.harsha", "era", "Harsha's Empire", sa, start=606, end=647, tier="intermediate",
      summary="Last great pre-Islamic north Indian empire; centered on Kannauj.")
    R("harshavardhana",  "Harshavardhana",         f"{sa}.harsha", 606, 647, "foundational",
      "Buddhist emperor of Kannauj; his court was described by the Chinese pilgrim Xuanzang.",
      native="हर्षवर्धन")

    # =========================================================================
    # CHOLA EMPIRE — extended (already have Rajaraja I, Rajendra I)
    # =========================================================================
    c = f"{sa}.chola"
    R("vijayalaya",      "Vijayalaya Chola",       c, 848, 871, "intermediate",
      "Founder of the imperial Chola line.")
    R("aditya-i",        "Aditya I",               c, 871, 907)
    R("parantaka-i",     "Parantaka I",            c, 907, 955, "intermediate")
    R("rajadhiraja",     "Rajadhiraja I",          c, 1044, 1054)
    R("rajendra-ii",     "Rajendra II",            c, 1054, 1063)
    R("virarajendra",    "Virarajendra",           c, 1063, 1070)
    R("kulottunga-i",    "Kulottunga I",           c, 1070, 1120, "intermediate",
      "Long reign that stabilized the empire; sent embassies to Song China.")
    R("kulottunga-iii",  "Kulottunga III",         c, 1178, 1218)
    R("rajaraja-iii",    "Rajaraja III",           c, 1216, 1256)
    R("rajendra-iii",    "Rajendra III",           c, 1246, 1279,
      summary="Last Chola emperor; his death ended the dynasty.")

    # =========================================================================
    # PALLAVA DYNASTY
    # =========================================================================
    E(f"{sa}.pallava", "era", "Pallava Dynasty", sa, start=275, end=897, tier="intermediate",
      summary="South Indian dynasty ruling from Kanchipuram; commissioned the great rock-cut temples at Mahabalipuram.")
    R("mahendravarman-i", "Mahendravarman I",      f"{sa}.pallava", 600, 630, "intermediate",
      "Warrior-poet-playwright; started the rock-cut temple tradition.")
    R("narasimhavarman-i", "Narasimhavarman I",    f"{sa}.pallava", 630, 668, "intermediate",
      "Founded Mamallapuram (Mahabalipuram); defeated the Chalukyas.")
    R("nandivarman-ii",  "Nandivarman II",         f"{sa}.pallava", 731, 796)

    # =========================================================================
    # PALA EMPIRE (Bengal)
    # =========================================================================
    E(f"{sa}.pala", "era", "Pala Empire", sa, start=750, end=1161, tier="intermediate",
      summary="Buddhist dynasty of Bengal and Bihar; patronized Nalanda and founded Vikramashila.")
    R("gopala",          "Gopala",                 f"{sa}.pala", 750, 770, "intermediate",
      "Founder of the Pala dynasty; elected by a council of chiefs.")
    R("dharmapala",      "Dharmapala",             f"{sa}.pala", 770, 810, "intermediate",
      "Extended Pala power across northern India; founded Vikramashila monastery.")
    R("devapala",        "Devapala",               f"{sa}.pala", 810, 850, "intermediate",
      "Peak of Pala power.")

    # =========================================================================
    # RASHTRAKUTA DYNASTY
    # =========================================================================
    E(f"{sa}.rashtrakuta", "era", "Rashtrakuta Dynasty", sa, start=735, end=982, tier="intermediate",
      summary="Deccan-based empire that patronized both Hinduism and Jainism; commissioned Kailasa Temple at Ellora.",
      date_note="Founded under Dantidurga c. 735; imperial power consolidated by 753.")
    R("dantidurga",      "Dantidurga",             f"{sa}.rashtrakuta", 735, 756,
      summary="Founder of the Rashtrakuta dynasty.")
    R("krishna-i",       "Krishna I",              f"{sa}.rashtrakuta", 756, 774, "intermediate",
      "Commissioned the Kailasa Temple at Ellora, carved from a single monolith.")
    R("govinda-iii",     "Govinda III",            f"{sa}.rashtrakuta", 793, 814, "intermediate")
    R("amoghavarsha",    "Amoghavarsha I",         f"{sa}.rashtrakuta", 814, 878, "intermediate",
      "Longest-reigning Rashtrakuta ruler; patron of Kannada and Sanskrit literature.")

    # =========================================================================
    # CHALUKYA DYNASTIES
    # =========================================================================
    E(f"{sa}.chalukya-badami", "era", "Chalukyas of Badami", sa, start=543, end=753, tier="intermediate",
      aliases=["Early Western Chalukyas"],
      summary="Deccan dynasty that dominated south-central India during the 6th–8th centuries.")
    R("pulakeshin-ii",   "Pulakeshin II",          f"{sa}.chalukya-badami", 610, 642, "intermediate",
      "Defeated Harshavardhana on the Narmada; received an embassy from Khosrow II of Persia.")
    E(f"{sa}.chalukya-western", "era", "Western Chalukya Empire", sa, start=973, end=1189, tier="specialist",
      summary="Kalyani-based revival of Chalukya power.")

    # =========================================================================
    # DELHI SULTANATE — dynasty sub-periods and key sultans
    # =========================================================================
    ds = f"{sa}.delhi-sultanate"
    P("mamluk",          "Mamluk (Slave) Dynasty",     ds, 1206, 1290, "intermediate",
      "First Delhi Sultanate dynasty; Turkic ex-slave rulers.")
    R("qutbuddin-aibak", "Qutb ud-Din Aibak",      f"{ds}.mamluk", 1206, 1210, "intermediate",
      "Founder of the Delhi Sultanate; began construction of the Qutb Minar.")
    R("iltutmish",       "Iltutmish",              f"{ds}.mamluk", 1211, 1236, "intermediate",
      "Consolidated Delhi Sultanate authority; issued the silver tanka.")
    R("razia-sultana",   "Razia Sultana",          f"{ds}.mamluk", 1236, 1240, "foundational",
      "First female Muslim ruler of the subcontinent; daughter of Iltutmish.",
      native="رضیہ سلطانہ")
    R("balban",          "Ghiyas ud-Din Balban",   f"{ds}.mamluk", 1266, 1287, "intermediate",
      "Restored central authority after nobles' insubordination.")
    P("khalji",          "Khalji Dynasty",         ds, 1290, 1320, "intermediate",
      "Second Delhi Sultanate dynasty; Turco-Afghan.")
    R("jalaluddin-khalji", "Jalal ud-Din Firuz Khalji", f"{ds}.khalji", 1290, 1296)
    R("alauddin-khalji", "Alauddin Khalji",        f"{ds}.khalji", 1296, 1316, "foundational",
      "Repelled multiple Mongol invasions; extended sultanate power into the Deccan; imposed strict price controls.")
    P("tughlaq",         "Tughlaq Dynasty",        ds, 1320, 1414, "intermediate")
    R("ghiyasuddin-tughlaq", "Ghiyas ud-Din Tughlaq", f"{ds}.tughlaq", 1320, 1325)
    R("muhammad-tughlaq", "Muhammad bin Tughlaq",  f"{ds}.tughlaq", 1325, 1351, "foundational",
      "Brilliant and eccentric; moved the capital to Daulatabad and back, and introduced token copper currency.")
    R("firoz-tughlaq",   "Firoz Shah Tughlaq",     f"{ds}.tughlaq", 1351, 1388, "intermediate",
      "Public-works reformer; built canals and cities.")
    P("sayyid",          "Sayyid Dynasty",         ds, 1414, 1451)
    R("khizr-khan",      "Khizr Khan",             f"{ds}.sayyid", 1414, 1421)
    P("lodi",            "Lodi Dynasty",           ds, 1451, 1526, "intermediate",
      "Final Delhi Sultanate dynasty; Afghan Pashtuns.")
    R("bahlul-lodi",     "Bahlul Lodi",            f"{ds}.lodi", 1451, 1489)
    R("sikandar-lodi",   "Sikandar Lodi",          f"{ds}.lodi", 1489, 1517, "intermediate")
    R("ibrahim-lodi",    "Ibrahim Lodi",           f"{ds}.lodi", 1517, 1526, "intermediate",
      "Last Delhi Sultan; defeated and killed by Babur at the First Battle of Panipat.")

    # =========================================================================
    # VIJAYANAGARA EMPIRE — dynasties and rulers
    # =========================================================================
    v = f"{sa}.vijayanagara"
    P("sangama",         "Sangama Dynasty",        v, 1336, 1485, "intermediate")
    R("harihara-i",      "Harihara I",             f"{v}.sangama", 1336, 1356, "intermediate",
      "Co-founder of the Vijayanagara Empire with his brother Bukka I.")
    R("bukka-i",         "Bukka I",                f"{v}.sangama", 1356, 1377, "intermediate",
      "Co-founder; secured southern India against the Bahmani Sultanate.")
    R("harihara-ii",     "Harihara II",            f"{v}.sangama", 1377, 1404)
    R("devaraya-i",      "Deva Raya I",            f"{v}.sangama", 1406, 1422)
    R("devaraya-ii",     "Deva Raya II",           f"{v}.sangama", 1424, 1446, "intermediate",
      "Peak of Sangama dynasty; patron of Kannada, Telugu, Sanskrit, and Tamil literature.")
    P("saluva",          "Saluva Dynasty",         v, 1485, 1505)
    P("tuluva",          "Tuluva Dynasty",         v, 1491, 1570, "intermediate")
    R("krishnadevaraya", "Krishnadevaraya",        f"{v}.tuluva", 1509, 1529, "foundational",
      "Greatest Vijayanagara emperor; poet, patron, and warrior. Peak of the empire.")
    R("achyuta-deva",    "Achyuta Deva Raya",      f"{v}.tuluva", 1529, 1542)
    R("sadashiva",       "Sadashiva Raya",         f"{v}.tuluva", 1542, 1570)
    P("aravidu",         "Aravidu Dynasty",        v, 1542, 1646,
      tier="specialist",
      summary="Rump dynasty after the catastrophic defeat at the Battle of Talikota (1565).")
    R("rama-raya",       "Aliya Rama Raya",        f"{v}.aravidu", 1542, 1565, "intermediate",
      "De facto ruler killed at Talikota; his death broke Vijayanagara power.")

    # =========================================================================
    # BAHMANI AND DECCAN SULTANATES
    # =========================================================================
    E(f"{sa}.bahmani", "era", "Bahmani Sultanate", sa, start=1347, end=1527, tier="intermediate",
      summary="First independent Muslim kingdom of the Deccan; the great rival of Vijayanagara.")
    R("bahman-shah",     "Alauddin Bahman Shah",   f"{sa}.bahmani", 1347, 1358, "intermediate",
      "Founder of the Bahmani Sultanate.")
    R("firuz-bahmani",   "Firuz Shah Bahmani",     f"{sa}.bahmani", 1397, 1422)
    R("ahmad-shah-bahmani", "Ahmad Shah Wali Bahmani", f"{sa}.bahmani", 1422, 1436)
    E(f"{sa}.deccan-sultanates", "era", "Deccan Sultanates", sa, start=1490, end=1687, tier="intermediate",
      aliases=["Five Sultanates of the Deccan"],
      summary="Five successor states to the Bahmani Sultanate: Ahmadnagar, Berar, Bidar, Bijapur, Golconda. Together they defeated Vijayanagara at Talikota (1565).")

    # =========================================================================
    # BENGAL SULTANATE
    # =========================================================================
    E(f"{sa}.bengal-sultanate", "era", "Bengal Sultanate", sa, start=1352, end=1576, tier="intermediate",
      summary="Independent Muslim sultanate of Bengal; a major trading power in the Indian Ocean.")

    # =========================================================================
    # HOYSALA and KAKATIYA (major South Indian medieval)
    # =========================================================================
    E(f"{sa}.hoysala", "era", "Hoysala Empire", sa, start=1026, end=1343, tier="intermediate",
      summary="Karnataka dynasty famed for its ornate temple architecture (Belur, Halebidu).")
    E(f"{sa}.kakatiya", "era", "Kakatiya Dynasty", sa, start=1163, end=1323, tier="intermediate",
      summary="Telugu dynasty of Warangal; extensive irrigation and temple-building.")
    R("ganapati-deva",   "Ganapati Deva",          f"{sa}.kakatiya", 1199, 1262, "intermediate")
    R("rudrama-devi",    "Rani Rudrama Devi",      f"{sa}.kakatiya", 1263, 1289, "foundational",
      "Female monarch who ruled as king in her own right; consolidated Kakatiya power.",
      native="రుద్రమదేవి")

    # =========================================================================
    # MUGHAL EMPIRE — the rest of the emperors (already have Babur/Akbar/Shah-Jahan/Aurangzeb)
    # =========================================================================
    mg = f"{sa}.mughal"
    R("humayun",         "Humayun",                mg, 1530, 1540, "intermediate",
      "Son of Babur; lost the empire to Sher Shah Suri before reconquering it.")
    R("humayun-restored", "Humayun (restored)",    mg, 1555, 1556, "specialist",
      "Second tenure after 15 years in Safavid exile.")
    R("jahangir",        "Jahangir",               mg, 1605, 1627, "foundational",
      "Son of Akbar; connoisseur and diarist. His court welcomed the first English ambassador (Sir Thomas Roe).")
    R("bahadur-shah-i",  "Bahadur Shah I",         mg, 1707, 1712, "intermediate",
      "First of the 'later Mughals'; empire began its rapid decline.")
    R("jahandar-shah",   "Jahandar Shah",          mg, 1712, 1713)
    R("farrukhsiyar",    "Farrukhsiyar",           mg, 1713, 1719,
      summary="Granted the East India Company the firman that laid the foundation for its later dominance.")
    R("muhammad-shah",   "Muhammad Shah 'Rangila'", mg, 1719, 1748, "intermediate",
      "Reign saw Nader Shah's sack of Delhi (1739), which broke Mughal power for good.")
    R("ahmad-shah-mughal", "Ahmad Shah Bahadur",   mg, 1748, 1754)
    R("alamgir-ii",      "Alamgir II",             mg, 1754, 1759)
    R("shah-alam-ii",    "Shah Alam II",           mg, 1759, 1806, "intermediate",
      "Restored to Delhi by the Marathas; became a British pensioner after the Company took Delhi in 1803.")
    R("akbar-shah-ii",   "Akbar Shah II",          mg, 1806, 1837)
    R("bahadur-shah-ii", "Bahadur Shah II 'Zafar'", mg, 1837, 1857, "foundational",
      "Last Mughal emperor; symbolic leader of the 1857 Indian Rebellion. Exiled to Rangoon by the British.")

    # --- Suri interregnum inside the Mughal era ---
    P("suri",            "Sur Empire (interregnum)", mg, 1540, 1555, "intermediate",
      "Afghan dynasty that ousted the Mughals for 15 years.")
    R("sher-shah-suri",  "Sher Shah Suri",         f"{mg}.suri", 1540, 1545, "foundational",
      "Reformer par excellence; built the Grand Trunk Road, introduced the rupee, and reformed the postal system.")
    R("islam-shah-suri", "Islam Shah Suri",        f"{mg}.suri", 1545, 1554)

    # =========================================================================
    # MARATHA CONFEDERACY — chhatrapatis and peshwas
    # =========================================================================
    mar = f"{sa}.maratha"
    R("shivaji",         "Chhatrapati Shivaji",    mar, 1674, 1680, "foundational",
      "Founder of the Maratha Empire; revolutionary military organizer who challenged the Mughals.",
      native="छत्रपती शिवाजी महाराज")
    R("sambhaji",        "Sambhaji",               mar, 1680, 1689, "intermediate",
      "Son of Shivaji; captured and executed by Aurangzeb after long resistance.")
    R("rajaram",         "Rajaram",                mar, 1689, 1700)
    R("tarabai",         "Tarabai",                mar, 1700, 1708, "intermediate",
      "Female regent who led the Maratha resistance against Aurangzeb.")
    R("shahu",           "Shahu I",                mar, 1708, 1749, "intermediate",
      "Reign saw the rise of the peshwas as the effective rulers of the confederacy.")
    P("peshwa-era",      "Peshwa Era",             mar, 1713, 1818, "foundational",
      "Peshwas (chief ministers) became the effective rulers; the Maratha confederacy dominated most of India.")
    R("balaji-vishwanath", "Balaji Vishwanath",    f"{mar}.peshwa-era", 1713, 1720, "intermediate",
      "First peshwa of the Bhat family; consolidated Maratha authority.")
    R("baji-rao-i",      "Baji Rao I",             f"{mar}.peshwa-era", 1720, 1740, "foundational",
      "Highly successful general who expanded Maratha power northward to Delhi and the Deccan.")
    R("balaji-baji-rao", "Balaji Baji Rao (Nana Saheb)", f"{mar}.peshwa-era", 1740, 1761, "intermediate",
      "Reign ended with the catastrophic defeat at the Third Battle of Panipat (1761).")
    R("madhavrao-i",     "Madhavrao I",            f"{mar}.peshwa-era", 1761, 1772, "intermediate",
      "Restored Maratha power after Panipat.")
    R("baji-rao-ii",     "Baji Rao II",            f"{mar}.peshwa-era", 1795, 1818, "intermediate",
      "Last peshwa; deposed by the British after the Third Anglo-Maratha War.")

    # =========================================================================
    # SIKH EMPIRE — rulers
    # =========================================================================
    sk = f"{sa}.sikh-empire"
    R("ranjit-singh",    "Maharaja Ranjit Singh",  sk, 1801, 1839, "foundational",
      "Founder of the Sikh Empire; the 'Lion of Punjab'.",
      native="ਮਹਾਰਾਜਾ ਰਣਜੀਤ ਸਿੰਘ")
    R("kharak-singh",    "Kharak Singh",           sk, 1839, 1839)
    R("nau-nihal-singh", "Nau Nihal Singh",        sk, 1839, 1840)
    R("sher-singh",      "Sher Singh",             sk, 1841, 1843)
    R("duleep-singh",    "Duleep Singh",           sk, 1843, 1849, "intermediate",
      "Child ruler at the end of the empire; deposed and taken to Britain after the Second Anglo-Sikh War.")

    # =========================================================================
    # MYSORE (18th century)
    # =========================================================================
    E(f"{sa}.mysore", "era", "Kingdom of Mysore", sa, start=1399, end=1947, tier="intermediate",
      summary="South Indian kingdom that under Haidar Ali and Tipu Sultan resisted British expansion.")
    R("haidar-ali",      "Haidar Ali",             f"{sa}.mysore", 1761, 1782, "intermediate",
      "Warrior-general who seized effective control of Mysore; fought the First and Second Anglo-Mysore Wars.")
    R("tipu-sultan",     "Tipu Sultan",            f"{sa}.mysore", 1782, 1799, "foundational",
      "The 'Tiger of Mysore'; killed defending Seringapatam against the British.",
      native="ٹیپو سلطان")

    # =========================================================================
    # EAST INDIA COMPANY RULE — governors-general (key ones)
    # =========================================================================
    E(f"{sa}.east-india-company", "era", "East India Company Rule",
      sa, start=1757, end=1858, tier="foundational",
      summary="British East India Company ruled increasingly large parts of India from Plassey (1757) to the Government of India Act (1858).")
    R("clive",           "Robert Clive (Governor of Bengal)", f"{sa}.east-india-company", 1757, 1760, "intermediate",
      "Victor of Plassey (1757); established Company rule in Bengal.")
    R("hastings",        "Warren Hastings (Governor-General)", f"{sa}.east-india-company", 1774, 1785, "intermediate",
      "First Governor-General of Bengal; consolidated Company authority.")
    R("cornwallis",      "Lord Cornwallis (Governor-General)", f"{sa}.east-india-company", 1786, 1793, "intermediate",
      "Enacted the Permanent Settlement of Bengal, restructuring landholding.")
    R("wellesley",       "Lord Wellesley (Governor-General)", f"{sa}.east-india-company", 1798, 1805, "intermediate",
      "Aggressive expansionist; defeated Tipu Sultan and the Marathas.")
    R("bentinck",        "Lord William Bentinck (Governor-General)", f"{sa}.east-india-company", 1828, 1835, "intermediate",
      "Abolished sati; began English-language education under Macaulay's Minute.")
    R("dalhousie",       "Lord Dalhousie (Governor-General)", f"{sa}.east-india-company", 1848, 1856, "intermediate",
      "'Doctrine of Lapse' annexations; his policies helped precipitate the 1857 Rebellion.")
    E(f"{sa}.east-india-company.rebellion-1857", "event",
      "Indian Rebellion of 1857", f"{sa}.east-india-company", start=1857, end=1858, tier="foundational",
      aliases=["First War of Independence", "Sepoy Mutiny", "Great Rebellion"],
      summary="Massive uprising against Company rule; suppressed with great violence. Led directly to the establishment of the British Raj.")

    # =========================================================================
    # BRITISH RAJ — key viceroys and events
    # =========================================================================
    br = f"{sa}.british-raj"
    R("canning",         "Lord Canning (1st Viceroy)", br, 1858, 1862, "intermediate",
      "First Viceroy of India; oversaw the transfer from Company to Crown.")
    R("lytton",          "Lord Lytton (Viceroy)",  br, 1876, 1880, "intermediate",
      "Presided over the Great Famine and proclaimed Victoria Empress of India (1877).")
    R("ripon",           "Lord Ripon (Viceroy)",   br, 1880, 1884)
    R("curzon",          "Lord Curzon (Viceroy)",  br, 1899, 1905, "foundational",
      "Partition of Bengal (1905) galvanized Indian nationalism.")
    R("hardinge",        "Lord Hardinge (Viceroy)", br, 1910, 1916, "intermediate",
      "Moved the capital from Calcutta to New Delhi.")
    R("chelmsford",      "Lord Chelmsford (Viceroy)", br, 1916, 1921, "intermediate",
      "Reign included the Jallianwala Bagh massacre (1919).")
    R("irwin",           "Lord Irwin (Viceroy)",   br, 1926, 1931, "intermediate",
      "Negotiated with Gandhi during the Salt Satyagraha.")
    R("linlithgow",      "Lord Linlithgow (Viceroy)", br, 1936, 1943, "intermediate",
      "Longest-serving viceroy; declared India at war in 1939 without consultation.")
    R("mountbatten",     "Lord Mountbatten (Last Viceroy)", br, 1947, 1948, "foundational",
      "Presided over the Partition of India; last Viceroy and first Governor-General of independent India.")
    E(f"{br}.jallianwala", "event", "Jallianwala Bagh Massacre", br,
      start=1919, end=1919, tier="foundational",
      summary="British troops opened fire on unarmed civilians in Amritsar; a decisive turning point in Indian nationalism.")
    E(f"{br}.salt-march", "event", "Salt March / Salt Satyagraha", br,
      start=1930, end=1930, tier="foundational",
      summary="Gandhi's 240-mile march to defy the British salt monopoly; galvanized mass civil disobedience.")
    E(f"{br}.partition", "event", "Partition of India", br,
      start=1947, end=1947, tier="foundational",
      summary="Division of British India into India and Pakistan; one of history's largest forced migrations, with mass violence.")

    # =========================================================================
    # INDEPENDENCE-ERA LEADERS AND MODERN LEADERS
    # =========================================================================
    ind = f"{sa}.independence"
    # Founding fathers (dates = period of major political leadership)
    R("gandhi",          "Mahatma Gandhi",         ind, 1915, 1948, "foundational",
      "Leader of the Indian independence movement; pioneer of nonviolent civil disobedience.",
      aliases=["Mohandas K. Gandhi", "Mahatma"],
      native="महात्मा गांधी")
    R("jinnah",          "Muhammad Ali Jinnah",    ind, 1913, 1948, "foundational",
      "Founder of Pakistan; first Governor-General of Pakistan.",
      aliases=["Quaid-e-Azam"],
      native="محمد علی جناح")
    R("ambedkar",        "B. R. Ambedkar",         ind, 1927, 1956, "foundational",
      "Chief architect of the Indian Constitution; leader of the Dalit civil rights movement.",
      native="भीमराव रामजी आंबेडकर")
    R("subhas-bose",     "Subhas Chandra Bose",    ind, 1938, 1945, "intermediate",
      "Nationalist leader who allied with the Axis and led the Indian National Army against the British.",
      aliases=["Netaji"])

    # India — prime ministers (major ones)
    P("india-prime-ministers", "Prime Ministers of India", ind, 1947, None, "foundational",
      "Heads of government of the Republic of India from Independence to the present.")
    R("nehru",           "Jawaharlal Nehru",       f"{ind}.india-prime-ministers", 1947, 1964, "foundational",
      "First Prime Minister of India; led non-aligned foreign policy and state-led industrialization.",
      native="जवाहरलाल नेहरू")
    R("shastri",         "Lal Bahadur Shastri",    f"{ind}.india-prime-ministers", 1964, 1966,
      summary="Led India through the 1965 war with Pakistan; died at Tashkent.")
    R("indira-gandhi",   "Indira Gandhi",          f"{ind}.india-prime-ministers", 1966, 1977, "foundational",
      "First female Prime Minister; declared the Emergency (1975-77). Assassinated in 1984 during a second term.")
    R("indira-gandhi-2", "Indira Gandhi (second term)", f"{ind}.india-prime-ministers", 1980, 1984, "intermediate")
    R("rajiv-gandhi",    "Rajiv Gandhi",           f"{ind}.india-prime-ministers", 1984, 1989, "intermediate",
      "Modernizer PM; assassinated in 1991.")
    R("narasimha-rao",   "P. V. Narasimha Rao",    f"{ind}.india-prime-ministers", 1991, 1996, "intermediate",
      "Launched the 1991 economic liberalization reforms with Manmohan Singh as Finance Minister.")
    R("vajpayee",        "Atal Bihari Vajpayee",   f"{ind}.india-prime-ministers", 1998, 2004, "intermediate",
      "BJP leader; conducted 1998 nuclear tests and pursued Pakistan-India dialogue.")
    R("manmohan-singh",  "Manmohan Singh",         f"{ind}.india-prime-ministers", 2004, 2014, "foundational",
      "Economist PM; architect of 1991 liberalization now heading government during India's high-growth 2000s.")
    R("modi",            "Narendra Modi",          f"{ind}.india-prime-ministers", 2014, None, "foundational",
      "Long-serving BJP prime minister.")

    # Pakistan — key leaders
    P("pakistan-leaders", "Leaders of Pakistan", ind, 1947, None, "intermediate",
      "Heads of state and government of Pakistan.")
    R("liaquat-ali-khan", "Liaquat Ali Khan",      f"{ind}.pakistan-leaders", 1947, 1951,
      summary="First Prime Minister of Pakistan; assassinated 1951.")
    R("ayub-khan",       "Ayub Khan",              f"{ind}.pakistan-leaders", 1958, 1969, "intermediate",
      "Military ruler; led Pakistan through the 1965 war.")
    R("bhutto",          "Zulfikar Ali Bhutto",    f"{ind}.pakistan-leaders", 1971, 1977, "intermediate",
      "Founder of the PPP; oversaw the 1973 constitution. Executed by Zia-ul-Haq in 1979.")
    R("zia-ul-haq",      "Muhammad Zia-ul-Haq",    f"{ind}.pakistan-leaders", 1978, 1988, "intermediate",
      "Military ruler who Islamized Pakistan's legal and social systems; died in a plane crash.")
    R("benazir",         "Benazir Bhutto (1st term)", f"{ind}.pakistan-leaders", 1988, 1990, "foundational",
      "First female head of government in a Muslim-majority nation. Dismissed by presidential decree in 1990.",
      aliases=["Benazir Bhutto"])
    R("benazir-2",       "Benazir Bhutto (2nd term)", f"{ind}.pakistan-leaders", 1993, 1996, "intermediate",
      "Second term as PM; dismissed on corruption charges. Assassinated 2007.",
      aliases=["Benazir Bhutto"])
    R("musharraf",       "Pervez Musharraf",       f"{ind}.pakistan-leaders", 1999, 2008, "intermediate",
      "Military ruler; key US ally in the War on Terror.")

    # Bangladesh — founding
    E(f"{ind}.bangladesh-liberation", "event", "Bangladesh Liberation War",
      ind, start=1971, end=1971, tier="foundational",
      summary="East Pakistan's independence war; India intervened decisively. Birth of Bangladesh.")
    R("mujib",           "Sheikh Mujibur Rahman",  ind, 1971, 1975, "foundational",
      "Founder of Bangladesh; assassinated in a 1975 coup.",
      aliases=["Bangabandhu"])
    R("hasina",          "Sheikh Hasina (1st term)", ind, 1996, 2001, "intermediate",
      "First tenure as PM of Bangladesh; daughter of Sheikh Mujibur Rahman.",
      aliases=["Sheikh Hasina"])
    R("hasina-2",        "Sheikh Hasina (2nd term)", ind, 2009, 2024, "foundational",
      "Longest-serving PM of Bangladesh; forced from office in a 2024 popular uprising.",
      aliases=["Sheikh Hasina"])

    # Sri Lanka — key events
    E(f"{ind}.sri-lanka-civil-war", "event", "Sri Lankan Civil War",
      ind, start=1983, end=2009, tier="intermediate",
      summary="Long conflict between the Sri Lankan government and the LTTE (Tamil Tigers); ended with the military defeat of the LTTE.")

    # =========================================================================
    # KEY CULTURAL / RELIGIOUS FIGURES (kind=reign as figureheads)
    # =========================================================================
    R("nanak",           "Guru Nanak",             sa, 1469, 1539, "foundational",
      "Founder of Sikhism.",
      native="ਗੁਰੂ ਨਾਨਕ")
    R("kabir",           "Kabir",                  sa, 1440, 1518, "intermediate",
      "Bhakti-Sufi mystic poet whose verses are foundational for both Hindu and Sikh traditions.")
    R("tagore",          "Rabindranath Tagore",    sa, 1878, 1941, "foundational",
      "Bengali polymath; first non-European Nobel laureate in Literature (1913). Composed the national anthems of India and Bangladesh.",
      native="রবীন্দ্রনাথ ঠাকুর")
