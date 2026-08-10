import json

cities = []

def add(**kwargs):
    cities.append(kwargs)

# 1. Rome
add(
    slug="rome",
    name="Rome",
    start_year=-900,
    end_year=None,
    summary="Capital of a republic and empire that shaped Western law, language, and urban form for two millennia.",
    aliases=["Roma"],
    date_precision="approx",
    contested="Legendary founding by Romulus is traditionally dated 753 BCE; archaeology shows Palatine huts a century or more earlier.",
    region_hint="europe",
    modern_name=None,
    still_inhabited=True,
    peak="1st century BCE - 2nd century CE, height of the Roman Empire",
    source={"citation": "'Ancient Rome - Rome's foundation myth', Britannica", "url": "https://www.britannica.com/place/ancient-Rome/Romes-foundation-myth", "kind": "reference"},
    date_agreement="differs: legendary founding is 753 BCE (traditional), but Britannica's archaeology of the Palatine shows a village there in the 10th/9th century BCE, earlier than the legendary date.",
)

# 2. Athens
add(
    slug="athens",
    name="Athens",
    start_year=-3000,
    end_year=None,
    summary="Birthplace of direct democracy and classical philosophy, drama, and architecture.",
    aliases=["Athina"],
    date_precision="approx",
    region_hint="europe",
    modern_name=None,
    still_inhabited=True,
    peak="5th century BCE, Golden Age under Pericles",
    source={"citation": "'Athens - History', Britannica", "url": "https://www.britannica.com/place/Athens/History", "kind": "reference"},
    date_agreement="matches: Britannica and Wikipedia's History of Athens both place Neolithic settlement before/around 3000 BCE.",
)

# 3. Sparta
add(
    slug="sparta",
    name="Sparta",
    start_year=-950,
    end_year=None,
    summary="Militarized city-state whose disciplined hoplite army dominated the Peloponnese for centuries.",
    aliases=["Lacedaemon", "Sparti"],
    date_precision="approx",
    contested="Legendary/traditional founding is sometimes given as the 9th century BCE (Britannica); the city was later sacked and greatly depopulated before the modern town was rebuilt in 1834 on the same site.",
    region_hint="europe",
    modern_name="Sparti, Greece",
    still_inhabited=True,
    peak="6th-4th century BCE, dominance of the Peloponnesian League",
    source={"citation": "'Sparta', Britannica", "url": "https://www.britannica.com/place/Sparta", "kind": "reference"},
    date_agreement="differs: Perseus Princeton Encyclopedia of Classical Sites and TheCollector place Dorian occupation at c. 950 BCE, while Britannica gives a traditional 9th-century-BCE founding.",
)

# 4. Alexandria
add(
    slug="alexandria",
    name="Alexandria",
    start_year=-331,
    end_year=None,
    summary="Hellenistic Egypt's capital and home to antiquity's greatest library and lighthouse.",
    aliases=["Al-Iskandariyya"],
    date_precision="exact",
    contested="A modest fishing settlement called Rhakotis existed on the site as early as c. 1500 BCE, but it was not a substantial city before Alexander's foundation.",
    region_hint="africa",
    modern_name="Alexandria, Egypt",
    still_inhabited=True,
    peak="3rd-1st century BCE, Ptolemaic capital and center of Hellenistic scholarship",
    source={"citation": "'Alexandria', Wikipedia", "url": "https://en.wikipedia.org/wiki/Alexandria", "kind": "reference, used after checking Britannica"},
    date_agreement="differs: Wikipedia and World History Encyclopedia give 331 BCE; Britannica gives 332 BCE for Alexander's founding.",
)

# 5. Constantinople
add(
    slug="constantinople",
    name="Constantinople",
    start_year=-657,
    end_year=None,
    summary="Roman/Byzantine imperial capital for over a thousand years, guarding the strait between Europe and Asia.",
    aliases=["Byzantium", "Constantinopolis"],
    date_precision="approx",
    region_hint="europe",
    modern_name="Istanbul, Turkey",
    still_inhabited=True,
    peak="4th-15th century CE, capital of the Roman/Byzantine Empire",
    source={"citation": "'Istanbul', Wikipedia", "url": "https://en.wikipedia.org/wiki/Istanbul", "kind": "reference"},
    date_agreement="approx: Wikipedia gives Byzantium's founding by Megarian colonists as c. 657 BCE; some secondary sources cite 660-667 BCE. The city was not ended by the 1453 Ottoman conquest and was only officially renamed Istanbul in 1930.",
)

# 6. Carthage
add(
    slug="carthage",
    name="Carthage",
    start_year=-725,
    end_year=None,
    summary="Phoenician trading power whose wars with Rome, including Hannibal's campaign, reshaped the Mediterranean.",
    aliases=["Qart-hadasht", "Carthago"],
    date_precision="approx",
    contested="Traditional founding by Dido is dated 814 BCE, but Britannica states archaeology has found nothing earlier than the last quarter of the 8th century BCE, a century later than the legend.",
    region_hint="africa",
    modern_name="Carthage (suburb of Tunis), Tunisia",
    still_inhabited=True,
    peak="4th-3rd century BCE, height of Punic maritime power",
    source={"citation": "'Carthage', Britannica", "url": "https://www.britannica.com/place/Carthage-ancient-city-Tunisia", "kind": "reference"},
    date_agreement="differs: traditional founding date is 814 BCE, but archaeological evidence supports the late 8th century BCE. The Punic city was destroyed by Rome in 146 BCE, refounded by Julius Caesar/Augustus, flourished as Roman Carthage, and declined after the Arab conquest c. 698 CE; the site has been continuously inhabited into the present as part of greater Tunis.",
)

# 7. Jerusalem
add(
    slug="jerusalem",
    name="Jerusalem",
    start_year=-3000,
    end_year=None,
    summary="Sacred center of Judaism, Christianity, and Islam, continuously settled near the Gihon Spring for five millennia.",
    aliases=["Yerushalayim", "Al-Quds"],
    date_precision="approx",
    region_hint="west-asia",
    modern_name=None,
    still_inhabited=True,
    peak="10th century BCE, First Temple period under David and Solomon",
    source={"citation": "'Jerusalem - History', Britannica", "url": "https://www.britannica.com/place/Jerusalem/History", "kind": "reference"},
    date_agreement="matches: Britannica and Wikipedia's History of Jerusalem both place the earliest settlement near the Gihon Spring at c. 3000 BCE; a 2016 find in the broader Shuafat area suggested activity as early as 5000 BCE but is not for the core City of David site.",
)

# 8. Babylon
add(
    slug="babylon",
    name="Babylon",
    start_year=-2300,
    end_year=1000,
    summary="Mesopotamian capital under Hammurabi and Nebuchadnezzar II, seat of the Hanging Gardens legend.",
    aliases=["Babel", "Babilim"],
    date_precision="approx",
    region_hint="west-asia",
    modern_name="near Hillah, Iraq",
    still_inhabited=False,
    peak="6th century BCE, Neo-Babylonian Empire under Nebuchadnezzar II",
    source={"citation": "'Babylon', Wikipedia", "url": "https://en.wikipedia.org/wiki/Babylon", "kind": "reference"},
    date_agreement="approx: Britannica says the city was probably first settled in the 3rd millennium BCE, with the earliest textual mention under Shar-Kali-Sharri (2217-2193 BCE); Wikipedia's infobox and World History Encyclopedia agree the city was abandoned c. 1000 CE following decline after the 7th-century Arab conquest.",
)

# 9. Ur
add(
    slug="ur",
    name="Ur",
    start_year=-3800,
    end_year=-450,
    summary="Sumerian city-state and Third Dynasty capital famed for its ziggurat and royal tombs.",
    aliases=["Tell el-Muqayyar"],
    date_precision="approx",
    region_hint="west-asia",
    modern_name="near Nasiriyah, Iraq",
    still_inhabited=False,
    peak="21st century BCE, Third Dynasty of Ur",
    source={"citation": "'Ur', World History Encyclopedia", "url": "https://www.worldhistory.org/ur/", "kind": "reference"},
    date_agreement="differs: World History Encyclopedia says Ur was founded by 3800 BCE and fell into ruin around 450 BCE; Britannica dates founding more broadly to the 4th millennium BCE; an academic study in American Journal of Archaeology suggests occupation may have continued to c. 300 BCE.",
)

# 10. Uruk
add(
    slug="uruk",
    name="Uruk",
    start_year=-5000,
    end_year=700,
    summary="One of the world's first true cities, credited with early writing and monumental temple architecture.",
    aliases=["Warka", "Erech"],
    date_precision="approx",
    contested="The legendary founder-king Enmerkar of the Sumerian King List is not a securely historical figure.",
    region_hint="west-asia",
    modern_name="near Warka, Iraq",
    still_inhabited=False,
    peak="4th millennium BCE, Uruk period urban expansion",
    source={"citation": "'Uruk', Wikipedia", "url": "https://en.wikipedia.org/wiki/Uruk", "kind": "reference"},
    date_agreement="matches: Wikipedia's infobox and World History Encyclopedia agree on a c. 5000 BCE founding and abandonment around 700 CE, with the city largely deserted by or shortly after the Islamic conquest of the 630s.",
)

# 11. Nineveh
add(
    slug="nineveh",
    name="Nineveh",
    start_year=-6000,
    end_year=-612,
    summary="Assyrian imperial capital under Sennacherib, destroyed by a Babylonian-Median coalition in 612 BCE.",
    aliases=["Ninawa"],
    date_precision="approx",
    region_hint="west-asia",
    modern_name="within Mosul, Iraq",
    still_inhabited=False,
    peak="8th-7th century BCE, capital of the Neo-Assyrian Empire",
    source={"citation": "'Nineveh', Britannica", "url": "https://www.britannica.com/place/Nineveh-ancient-city-Iraq", "kind": "reference"},
    date_agreement="differs: Britannica and World History Encyclopedia describe a Neolithic hamlet founded by the 7th millennium BCE (c. 6000 BCE), while Wikipedia's infobox lists 'Built c. 3000 BC' for the more substantial city; all sources agree the city was destroyed and abandoned in 612 BCE.",
)

# 12. Persepolis
add(
    slug="persepolis",
    name="Persepolis",
    start_year=-518,
    end_year=-330,
    summary="Ceremonial capital of the Achaemenid Persian Empire, built by Darius I and burned by Alexander the Great.",
    aliases=["Takht-e Jamshid", "Parsa"],
    date_precision="approx",
    region_hint="west-asia",
    modern_name="near Shiraz, Iran",
    still_inhabited=False,
    peak="522-486 BCE, reign of Darius I",
    source={"citation": "'Persepolis', Wikipedia", "url": "https://en.wikipedia.org/wiki/Persepolis", "kind": "reference"},
    date_agreement="matches: Wikipedia's infobox and the scholarly source Achaemenica.org both date construction to c. 518-515 BCE under Darius I, and agree the city was abandoned after being burned in 330 BCE by Alexander's army.",
)

# 13. Baghdad
add(
    slug="baghdad",
    name="Baghdad",
    start_year=762,
    end_year=None,
    summary="Abbasid caliphate capital and medieval center of science, philosophy, and trade under the House of Wisdom.",
    aliases=["Madinat al-Salam"],
    date_precision="exact",
    region_hint="west-asia",
    modern_name=None,
    still_inhabited=True,
    peak="8th-9th century CE, Abbasid Golden Age",
    source={"citation": "'Baghdad - History', Britannica", "url": "https://www.britannica.com/place/Baghdad/History", "kind": "reference"},
    date_agreement="matches: Britannica and Wikipedia's History of Baghdad both give the true founding by Caliph al-Mansur as 762 CE, though a smaller pre-existing Persian village occupied the site earlier.",
)

# 14. Damascus
add(
    slug="damascus",
    name="Damascus",
    start_year=-3000,
    end_year=None,
    summary="Often called the world's oldest continuously inhabited capital, a hub of trade and Islamic learning.",
    aliases=["Dimashq", "Sham"],
    date_precision="approx",
    region_hint="west-asia",
    modern_name=None,
    still_inhabited=True,
    peak="7th-8th century CE, capital of the Umayyad Caliphate",
    source={"citation": "'Ancient City of Damascus', UNESCO World Heritage Centre", "url": "https://whc.unesco.org/en/list/20/", "kind": "institutional"},
    date_agreement="matches: UNESCO and Wikipedia both cite settlement of the urban core c. 3000 BCE; a separate, much older Neolithic site at Tell Ramad nearby (c. 6300-8000 BCE) is sometimes conflated with Damascus's antiquity but is a distinct site.",
)

# 15. Memphis (Egypt)
add(
    slug="memphis-egypt",
    name="Memphis",
    start_year=-3100,
    end_year=641,
    summary="Old Kingdom capital of unified Egypt, seat of the cult of Ptah and gateway to the Saqqara necropolis.",
    aliases=["Ineb-hedj", "Men-nefer"],
    date_precision="approx",
    contested="Legendary founder-king Menes is traditionally credited with founding Memphis c. 2925-2900 BCE, but Wikipedia notes the site was already occupied earlier, during the reign of Iry-Hor.",
    region_hint="africa",
    modern_name="near Mit Rahina, south of Cairo, Egypt",
    still_inhabited=False,
    peak="c. 2600-2100 BCE, Old Kingdom capital",
    source={"citation": "'Memphis, Egypt', Wikipedia", "url": "https://en.wikipedia.org/wiki/Memphis,_Egypt", "kind": "reference"},
    date_agreement="differs: World History Encyclopedia's timeline places the Arab invasion and quarrying of Memphis's ruins around 640 CE, while Britannica describes final abandonment only after Cairo's founding in the 10th century CE.",
)

# 16. Thebes (Egypt) / Luxor
add(
    slug="thebes-egypt",
    name="Thebes",
    start_year=-3200,
    end_year=None,
    summary="New Kingdom Egyptian capital and religious center of Amun, home to Karnak and the Valley of the Kings.",
    aliases=["Waset", "Luxor"],
    date_precision="approx",
    contested="Thebes was sacked by Assyrians in 666 BCE and further destroyed by Rome in the 1st century BCE, but the site continued to be inhabited and today forms the modern city of Luxor.",
    region_hint="africa",
    modern_name="Luxor, Egypt",
    still_inhabited=True,
    peak="c. 1550-1069 BCE, New Kingdom capital",
    source={"citation": "'Thebes, Egypt', Wikipedia", "url": "https://en.wikipedia.org/wiki/Thebes,_Egypt", "kind": "reference"},
    date_agreement="approx: Wikipedia states Thebes was inhabited from around 3200 BCE; World History Encyclopedia describes the city's political decline and eventual destruction by Rome in the 1st century CE, after which the site continued as a much smaller settlement that persists today as Luxor.",
)

# 17. Meroe
add(
    slug="meroe",
    name="Meroë",
    start_year=-890,
    end_year=350,
    summary="Later capital of the Kingdom of Kush, famed for its own pyramid fields and ironworking industry.",
    aliases=["Bedewi"],
    date_precision="approx",
    region_hint="africa",
    modern_name="near Kabushiya, Sudan",
    still_inhabited=False,
    peak="c. 300 BCE-100 CE, height of Meroitic Kingdom of Kush",
    source={"citation": "'Meroe', World History Encyclopedia", "url": "https://www.worldhistory.org/Meroe/", "kind": "reference"},
    date_agreement="differs: World History Encyclopedia dates the earliest known tomb to c. 890 BCE and the city becoming capital c. 590 BCE, while an Oxford academic source puts the earliest remains in the 10th century BCE; sources agree the city was destroyed by an Aksumite invasion between 320 and 350 CE and abandoned soon after.",
)

# 18. Timbuktu
add(
    slug="timbuktu",
    name="Timbuktu",
    start_year=1100,
    end_year=None,
    summary="Trans-Saharan trade hub and center of Islamic scholarship famed for its manuscript libraries.",
    aliases=["Tombouctou", "Tin Bukt"],
    date_precision="approx",
    contested="A separate Iron Age settlement (Tombouze) existed nearby from the 5th century BCE to c. 1000 CE but was abandoned before Timbuktu itself was founded; it is not the same site.",
    region_hint="africa",
    modern_name=None,
    still_inhabited=True,
    peak="14th-16th century CE, height of trans-Saharan trade and Islamic scholarship",
    source={"citation": "'Timbuktu', Britannica", "url": "https://www.britannica.com/place/Timbuktu-Mali", "kind": "reference"},
    date_agreement="matches: Britannica, World History Encyclopedia, and Wikipedia converge on Timbuktu being founded around 1100 CE by Tuareg nomads as a seasonal camp that became permanent.",
)

# 19. Great Zimbabwe
add(
    slug="great-zimbabwe",
    name="Great Zimbabwe",
    start_year=1100,
    end_year=1550,
    summary="Largest stone-built city of pre-colonial sub-Saharan Africa, capital of a gold-trading Shona kingdom.",
    aliases=[],
    date_precision="approx",
    note="This settlement may already exist in the dataset as a related empire or archaeological-site entry; reconcile with that record if present.",
    region_hint="africa",
    modern_name=None,
    still_inhabited=False,
    peak="14th-15th century CE, height of the Kingdom of Zimbabwe",
    source={"citation": "'Great Zimbabwe National Monument', UNESCO World Heritage Centre", "url": "https://whc.unesco.org/en/list/364/", "kind": "institutional"},
    date_agreement="approx: UNESCO and Britannica date the first stonework to c. 900-1100 CE, with the city abandoned around 1450 CE due to overpopulation and resource depletion; Wikipedia notes some continued visitation into the 17th century for spiritual purposes even after political abandonment.",
)

# 20. Cordoba
add(
    slug="cordoba-spain",
    name="Córdoba",
    start_year=-169,
    end_year=None,
    summary="Capital of the Umayyad Caliphate of Córdoba, a medieval center of learning, tolerance, and architecture.",
    aliases=["Corduba", "Qurtuba"],
    date_precision="approx",
    contested="An earlier Carthaginian/Iberian settlement existed on or near the site before the Roman city was founded.",
    region_hint="europe",
    modern_name=None,
    still_inhabited=True,
    peak="10th century CE, capital of the Caliphate of Córdoba",
    source={"citation": "'Cordoba', Britannica", "url": "https://www.britannica.com/place/Cordoba-Spain", "kind": "reference"},
    date_agreement="approx: sources place the Roman foundation by consul Marcus Claudius Marcellus between 169 and 152 BCE; Britannica notes Córdoba 'was probably Carthaginian in origin' before Roman occupation in 152 BCE.",
)

# 21. Samarkand
add(
    slug="samarkand",
    name="Samarkand",
    start_year=-700,
    end_year=None,
    summary="Silk Road crossroads and later Timurid capital renowned for Registan Square and monumental architecture.",
    aliases=["Maracanda", "Afrasiyab"],
    date_precision="approx",
    region_hint="central-asia",
    modern_name=None,
    still_inhabited=True,
    peak="14th-15th century CE, capital of the Timurid Empire",
    source={"citation": "'Samarkand', Wikipedia", "url": "https://en.wikipedia.org/wiki/Samarkand", "kind": "reference"},
    date_agreement="differs: there is no direct evidence of Samarkand's founding date; Wikipedia and the Institute of Archaeology of Samarkand estimate c. 700 BCE, UNESCO cites the 7th century BCE, and a 2025 Uzbek-French archaeological reassessment argues for urbanization as early as the late 2nd/early 1st millennium BCE.",
)

# 22. Chang'an / Xi'an
add(
    slug="changan-xian",
    name="Chang'an",
    start_year=-1100,
    end_year=None,
    summary="Capital of more Chinese dynasties than any other city, including the Han and Tang golden ages.",
    aliases=["Xi'an", "Hao"],
    date_precision="approx",
    region_hint="east-asia",
    modern_name="Xi'an, China",
    still_inhabited=True,
    peak="7th-8th century CE, capital of the Tang dynasty",
    source={"citation": "'Xi'an', Britannica", "url": "https://www.britannica.com/place/Xian-China", "kind": "reference"},
    date_agreement="approx: Britannica states cities have existed in the area since the 11th century BCE; the name Chang'an itself is traditionally dated to the Han dynasty's founding of its capital in 202 BCE per Wikipedia, and the site's name later changed to Xi'an under the Ming dynasty.",
)

# 23. Beijing
add(
    slug="beijing",
    name="Beijing",
    start_year=-1045,
    end_year=None,
    summary="Imperial capital of the Yuan, Ming, and Qing dynasties, and capital of modern China.",
    aliases=["Ji", "Peking", "Dadu"],
    date_precision="approx",
    region_hint="east-asia",
    modern_name=None,
    still_inhabited=True,
    peak="15th-19th century CE, Ming and Qing imperial capital",
    source={"citation": "'Beijing - History', Britannica", "url": "https://www.britannica.com/place/Beijing/History", "kind": "reference"},
    date_agreement="matches: Britannica and Wikipedia's History of Beijing agree the earliest walled city, Ji, was established by around 1045 BCE at the founding of the Zhou dynasty; the modern Beijing Municipal Government uses this date as the city's official founding year.",
)

# 24. Kyoto
add(
    slug="kyoto",
    name="Kyoto",
    start_year=794,
    end_year=None,
    summary="Imperial capital of Japan for over a thousand years and cradle of Heian court culture.",
    aliases=["Heian-kyo", "Miyako"],
    date_precision="exact",
    region_hint="east-asia",
    modern_name=None,
    still_inhabited=True,
    peak="9th-12th century CE, Heian period",
    source={"citation": "'Kyoto', Britannica", "url": "https://www.britannica.com/place/Kyoto-Japan", "kind": "reference"},
    date_agreement="matches: Britannica, Wikipedia, and Japan's Agency for Cultural Affairs all agree Kyoto was founded as Heian-kyo in 794 CE by Emperor Kammu.",
)

# 25. Nara
add(
    slug="nara",
    name="Nara",
    start_year=710,
    end_year=None,
    summary="Japan's first permanent imperial capital, home to the Great Buddha of Todai-ji.",
    aliases=["Heijo-kyo"],
    date_precision="exact",
    region_hint="east-asia",
    modern_name=None,
    still_inhabited=True,
    peak="710-784 CE, Nara period capital",
    source={"citation": "'Nara', Britannica", "url": "https://www.britannica.com/place/Nara-Japan", "kind": "reference"},
    date_agreement="matches: Britannica, Wikipedia, and World History Encyclopedia agree Empress Genmei established the capital at Heijo-kyo (Nara) in 710 CE; the capital moved away in 784 CE but the settlement itself continued and is inhabited today.",
)

# 26. Gyeongju
add(
    slug="gyeongju",
    name="Gyeongju",
    start_year=-57,
    end_year=None,
    summary="Capital of the Silla kingdom for nearly a millennium, dense with royal tombs and Buddhist temples.",
    aliases=["Seorabeol", "Geumseong", "Kyongju"],
    date_precision="traditional",
    contested="The traditional founding by Hyeokgeose in 57 BCE comes from the 12th-century Samguk sagi; World History Encyclopedia notes modern historians consider this date unlikely to be accurate and prefer a later date for Silla as a unified political entity.",
    region_hint="east-asia",
    modern_name=None,
    still_inhabited=True,
    peak="7th-9th century CE, capital of Unified Silla",
    source={"citation": "'Gyeongju', World History Encyclopedia", "url": "https://www.worldhistory.org/Gyeongju/", "kind": "reference"},
    date_agreement="traditional: not an archaeological date; 57 BCE is the legendary founding date of the Silla kingdom's capital at Saro, per the Samguk sagi.",
)

# 27. Angkor
add(
    slug="angkor",
    name="Angkor",
    start_year=802,
    end_year=1431,
    summary="Capital of the Khmer Empire, encompassing the vast temple complex of Angkor Wat.",
    aliases=["Yasodharapura"],
    date_precision="approx",
    note="This settlement may already exist in the dataset as a related empire or archaeological-site entry; reconcile with that record if present.",
    region_hint="southeast-asia",
    modern_name="near Siem Reap, Cambodia",
    still_inhabited=False,
    peak="12th-13th century CE, reigns of Suryavarman II and Jayavarman VII",
    source={"citation": "'Angkor', Britannica", "url": "https://www.britannica.com/place/Angkor", "kind": "reference"},
    date_agreement="approx: 802 CE is the traditional founding of the Khmer Empire under Jayavarman II, though the capital only moved to the Angkor site itself under Yasovarman I around 890-900 CE; Britannica and Wikipedia agree the city was sacked and largely abandoned in 1431, though Angkor Wat itself was never fully abandoned and remained a Buddhist shrine.",
)

# 28. Pataliputra / Patna
add(
    slug="pataliputra-patna",
    name="Pataliputra",
    start_year=-490,
    end_year=None,
    summary="Capital of the Maurya and Gupta empires, once among the largest cities in the ancient world.",
    aliases=["Patna"],
    date_precision="approx",
    contested="Britannica describes the ancient city as deserted by the 7th century CE and refounded as Patna in 1541 CE; treated here as one continuous city per the brief's rule that decline/refounding on the same site is not an end.",
    region_hint="south-asia",
    modern_name="Patna, India",
    still_inhabited=True,
    peak="3rd century BCE, capital of the Maurya Empire under Ashoka",
    source={"citation": "'Patna', Britannica", "url": "https://www.britannica.com/place/Patna", "kind": "reference"},
    date_agreement="approx: Britannica dates the founding of Pataliputra by Ajatashatru to the 5th century BCE and states it declined and was deserted by the 7th century CE, before being refounded as Patna in 1541 CE; the site is continuously inhabited today as modern Patna, so this entry treats the city as continuing rather than ending.",
)

# 29. Varanasi
add(
    slug="varanasi",
    name="Varanasi",
    start_year=-1200,
    end_year=None,
    summary="One of the world's oldest continuously inhabited cities and Hinduism's most sacred pilgrimage site.",
    aliases=["Kashi", "Benares", "Banaras"],
    date_precision="approx",
    region_hint="south-asia",
    modern_name=None,
    still_inhabited=True,
    peak="6th century BCE onward, center of Vedic and Buddhist learning",
    source={"citation": "'Varanasi', Britannica", "url": "https://www.britannica.com/place/Varanasi", "kind": "reference"},
    date_agreement="differs: excavations at the Rajghat site date continuous settlement to roughly the 8th-11th century BCE; Wikipedia's List of oldest continuously inhabited cities cites c. 1200 BCE, while some researchers (IIT-Kharagpur boring studies) suggest occupation as early as 2000 BCE. No single date is universally agreed; 1200 BCE reflects the most commonly cited figure.",
)

# 30. Tenochtitlan
add(
    slug="tenochtitlan",
    name="Tenochtitlan",
    start_year=1325,
    end_year=1521,
    summary="Island capital of the Aztec Empire, one of the largest cities in the world before Spanish conquest.",
    aliases=["Mexico-Tenochtitlan"],
    date_precision="traditional",
    contested="The exact founding date is unclear; 13 March 1325 was chosen retrospectively in 1925 to mark the city's 600th anniversary, per Wikipedia.",
    note="This settlement may already exist in the dataset as a related empire or archaeological-site entry; reconcile with that record if present.",
    region_hint="americas",
    modern_name="Mexico City, Mexico",
    still_inhabited=False,
    peak="late 15th century-1519 CE, height of the Aztec Empire",
    source={"citation": "'Tenochtitlan', Britannica", "url": "https://www.britannica.com/place/Tenochtitlan", "kind": "reference"},
    date_agreement="traditional: Britannica gives founding 'c. 1325'; the precise day is a modern commemorative convention, not an archaeological date. The city was destroyed by Spanish conquistadors in 1521, and modern Mexico City was built on and around its ruins, so this is treated as a genuine end rather than a renaming.",
)

# 31. Cusco
add(
    slug="cusco",
    name="Cusco",
    start_year=1100,
    end_year=None,
    summary="Capital of the Inca Empire, its stonework foundations still underlying much of the modern city.",
    aliases=["Cuzco", "Qosqo"],
    date_precision="traditional",
    contested="Traditionally founded by Manco Capac in the 11th or 12th century CE per Inca legend; the exact founding date and process are unknown, though the valley itself was inhabited for roughly 3,000 years before the Inca city was established.",
    region_hint="americas",
    modern_name=None,
    still_inhabited=True,
    peak="15th-16th century CE, capital of the Inca Empire (Tawantinsuyu)",
    source={"citation": "'Cuzco', Britannica", "url": "https://www.britannica.com/place/Cuzco", "kind": "reference"},
    date_agreement="traditional: Britannica dates Cusco's founding as an Inca settlement to the 11th or 12th century CE; Wikipedia's History of Cusco notes the site was already inhabited about 3,000 years before that as evidenced by archaeological remains, but the Inca city itself has no securely dated founding event.",
)

# 32. Cahokia
add(
    slug="cahokia",
    name="Cahokia",
    start_year=700,
    end_year=1400,
    summary="Largest pre-Columbian city north of Mexico, its earthen mounds still dominate the Mississippi floodplain.",
    aliases=["Cahokia Mounds"],
    date_precision="approx",
    region_hint="americas",
    modern_name=None,
    still_inhabited=False,
    peak="c. 1050-1200 CE, peak Mississippian population",
    source={"citation": "'Cahokia Mounds', Britannica", "url": "https://www.britannica.com/place/Cahokia-Mounds", "kind": "reference"},
    date_agreement="matches: Britannica states Cahokia was first occupied in 700 CE and flourished c. 950-1350 CE; other sources describe a slow decline and abandonment spread across the 1200s-1300s, with full abandonment by around 1400 CE.",
)

# 33. Teotihuacan
add(
    slug="teotihuacan",
    name="Teotihuacan",
    start_year=-100,
    end_year=750,
    summary="Pre-Aztec metropolis of the Americas, home to the Pyramids of the Sun and Moon, whose builders remain unidentified.",
    aliases=[],
    date_precision="approx",
    note="This settlement may already exist in the dataset as a related empire or archaeological-site entry; reconcile with that record if present.",
    region_hint="americas",
    modern_name=None,
    still_inhabited=False,
    peak="c. 500 CE, one of the largest cities in the world with 125,000-200,000 residents",
    source={"citation": "'Teotihuacan', Wikipedia", "url": "https://en.wikipedia.org/wiki/Teotihuacan", "kind": "reference"},
    date_agreement="differs: Wikipedia's infobox gives founding c. 100 BCE and abandonment c. 750 CE; Britannica says the area was settled by 400 BCE but did not see large-scale urban growth until roughly three centuries later; UNESCO and most sources agree the city was burned and abandoned during the 7th century CE.",
)

# 34. Nan Madol
add(
    slug="nan-madol",
    name="Nan Madol",
    start_year=1180,
    end_year=1628,
    summary="Megalithic city of artificial islets that served as the Saudeleur dynasty's capital in Micronesia.",
    aliases=[],
    date_precision="approx",
    contested="Human activity at the site dates back to the 1st or 2nd century CE, but the monumental megalithic construction associated with the Saudeleur dynasty's capital began around 1180-1200 CE per uranium-thorium dating.",
    region_hint="oceania",
    modern_name=None,
    still_inhabited=False,
    peak="13th-16th century CE, seat of the Saudeleur dynasty",
    source={"citation": "'Nan Madol', Britannica", "url": "https://www.britannica.com/place/Nan-Madol", "kind": "reference"},
    date_agreement="differs: Britannica says construction began about the 8th century with monuments dated 1180-1200; Wikipedia and the Pohnpei Historic Preservation Office state Nan Madol was the Saudeleur capital until about 1628; other sources (Atlas Obscura, NPS) give a broader abandonment window extending into the 18th-19th century as the site's importance faded.",
)


with open("/home/user/workspace/hp/docs/research/cities.json", "w") as f:
    json.dump(cities, f, indent=2, ensure_ascii=False)

print(f"Wrote {len(cities)} cities")
