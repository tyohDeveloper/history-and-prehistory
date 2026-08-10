"""Sources, summaries and honest dating for the entities promoted to Essentials.

Promoting 57 entities to the top tier moved 47 unsourced date ranges into the most
prominent view in the app, which made issue #2 measurably worse before it made it
better. This is the other half of that change.

Twenty-nine dated entities were researched. **Twenty-one matched their stored dates and
eight did not**, and the eight are the valuable part -- a citation that quietly disagrees
with the date it is attached to is worse than no citation, because it looks like
verification.

Two dates are corrected outright:

* **Qajar 1789 -> 1794.** Britannica dates the dynasty 1794-1925. 1789 is when Agha
  Mohammad Khan began his unification campaign, 1794 when he eliminated his last rival,
  1796 when he was crowned. All three are defensible; the campaign start was the weakest
  and the least sourced, so the other two are recorded as alternatives.
* **Rashtrakuta 735 -> 753.** Dantidurga defeated the last Badami Chalukya king in 753.
  This also removes an 18-year overlap with the Chalukyas of Badami, who end in 753 --
  the two now hand off cleanly, which is itself evidence the old date was wrong.

Six keep their dates and gain an explicit record of the disagreement, because the
dataset's own convention is to keep rival claims apart rather than average them. The
Mutapa Empire is the worst case found: three reputable sources give three incompatible
ranges, and ours is corroborated only at Wikipedia tier.

Gojoseon needed more than a citation. Its start year of 2333 BCE is the **Dangun
foundation myth**, not an archaeological date. The dating machinery already handled this
correctly -- `start_dating_method: received`, `date_precision: traditional`, and the
dagger marker reading "Received convention, not a finding" -- so what was missing was
only the reason. A sourced caveat now names the Dangun myth and states that historians
of Korea treat the date as legend. The end year, 108 BCE, is the Han conquest and is
solid.
"""

PROMOTED_SOURCES = [
    {"id": "src-africa-nile-egypt-fip", "kind": "institutional",
     "citation": "\"Timeline of ancient Egypt\", The British Museum",
     "url": "https://www.britishmuseum.org/learn/schools/ages-7-11/ancient-egypt/timeline-ancient-egypt",
     "note": "British Museum gives First Intermediate Period as 'about 2181-2055 BC', matching exactly; Britannica's main Egypt article gives a slightly later c.2118-c.1980 BCE."},
    {"id": "src-africa-nile-egypt-sip", "kind": "institutional",
     "citation": "\"Chronology: The Second Intermediate Period\", UCL Digital Egypt for Universities",
     "url": "https://www.ucl.ac.uk/museums-static/digitalegypt/2inter/index.html",
     "note": "UCL states outright 'there is no general agreement in Egyptology either about the length or how to define the Second Intermediate Period'; other sources range c.1782-c.1539 BCE."},
    {"id": "src-africa-nile-egypt-tip", "kind": "institutional",
     "citation": "\"Chronology: The Third Intermediate Period\", UCL Digital Egypt for Universities",
     "url": "https://www.ucl.ac.uk/museums-static/digitalegypt/3inter/index.html",
     "note": "UCL and the British Museum both give 1069-664 BC, matching our range (-1069..-656) within a few years at the end."},
    {"id": "src-africa-nile-egypt-late-period", "kind": "reference",
     "citation": "\"Late period\", Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Late-period",
     "note": "Britannica dates the Late Period 664-332 BCE, matching our range exactly."},
    {"id": "src-africa-nile-aksum", "kind": "reference",
     "citation": "\"Aksum\", Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Aksum-ancient-kingdom-Africa",
     "note": "Britannica's infobox spans to c.1100; most other sources (Wikipedia, HeritageDaily) put Aksum's collapse c.940-960, closer to our end year of 940."},
    {"id": "src-east-asia-china-jin", "kind": "reference",
     "citation": "\"Jin dynasty\", Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Jin-dynasty-China-AD-265-316-317-317-420",
     "note": "Britannica dates the Jin dynasty 265-420 CE; the 1-year difference from our 266 start is within normal rounding of the founding date."},
    {"id": "src-east-asia-china-north-south", "kind": "reference",
     "citation": "\"Southern Dynasties\", Encyclopaedia Britannica",
     "url": "https://www.britannica.com/event/Southern-Dynasties",
     "note": "Britannica gives 420-589 CE for this period, matching our range exactly."},
    {"id": "src-east-asia-korea-gojoseon", "kind": "reference",
     "citation": "\"Dan'gun and Gojoseon founding myth vs. archaeology\", GlobalSecurity.org / \"Gojoseon\", World History Encyclopedia",
     "url": "https://www.globalsecurity.org/military/world/rok/history-gojoseon.htm",
     "note": "GlobalSecurity states serious historians treat 2333 BCE/Dangun as pure myth with no archaeological support; the -108 end year matches the Han conquest recorded by World History Encyclopedia."},
    {"id": "src-east-asia-korea-three-kingdoms", "kind": "reference",
     "citation": "\"Three Kingdoms period\", Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Three-Kingdoms-period",
     "note": "Britannica dates the period c.57 BCE-668 CE, matching our range exactly."},
    {"id": "src-east-asia-korea-unified-silla", "kind": "reference",
     "citation": "\"Unified Silla dynasty\", Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Unified-Silla-dynasty",
     "note": "Britannica gives 668-935, matching our range exactly."},
    {"id": "src-west-asia-mesopotamia-ur3", "kind": "reference",
     "citation": "\"3rd Dynasty of Ur\", Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/3rd-Dynasty-of-Ur",
     "note": "Britannica gives c.2112-c.2004 BCE (middle chronology, the mainstream figure used in scientific publications), matching our range exactly."},
    {"id": "src-west-asia-mesopotamia-kassite", "kind": "institutional",
     "citation": "\"The Middle Babylonian / Kassite Period (ca. 1595-1155 B.C.) in Mesopotamia\", The Metropolitan Museum of Art",
     "url": "https://www.metmuseum.org/essays/the-middle-babylonian-kassite-period-ca-1595-1155-b-c-in-mesopotamia",
     "note": "Met Museum gives 1595-1155 BC using the middle chronology (sack of Babylon in 1595 BC as dividing line); short/long chronologies would shift these dates."},
    {"id": "src-west-asia-iran-qajar", "kind": "reference",
     "citation": "\"Qajar dynasty\", Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Qajar-dynasty",
     "note": "Britannica dates Qajar rule from 1794 (when Agha Mohammad Khan eliminated his rivals), not 1789; end year 1925 matches."},
    {"id": "src-europe-mediterranean-greece-dark-age", "kind": "reference",
     "citation": "\"A Timeline of Ancient Greece\", TheCollector.com (cf. \"Greek Dark Age\", World History Encyclopedia)",
     "url": "https://www.thecollector.com/timeline-ancient-greece/",
     "note": "Source gives 'Dark Age / Early Iron Age (c.1100-c.800 BCE)' and explicitly notes the 'Dark Age' label is disputed, with 'Early Iron Age' preferred by many scholars."},
    {"id": "src-europe-western-england-plantagenet", "kind": "reference",
     "citation": "\"House of Plantagenet\", Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/house-of-Plantagenet",
     "note": "Britannica states the Plantagenets reigned 1154-1485, matching our range exactly."},
    {"id": "src-europe-western-england-stuart", "kind": "reference",
     "citation": "\"House of Stuart\", Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/House-of-Stuart",
     "note": "Britannica confirms English rule 1603-1714, but rule was interrupted 1649-1660 by the Commonwealth, so 1603-1714 is a conventional simplification, not continuous rule."},
    {"id": "src-europe-western-iberia-reconquista", "kind": "reference",
     "citation": "\"Reconquista\", Encyclopaedia Britannica",
     "url": "https://www.britannica.com/event/Reconquista",
     "note": "Britannica ties 711 to the Muslim conquest's start and 1492 to the fall of Granada, matching our range, though it separately notes Christian resistance is often dated from 718 (Covadonga)."},
    {"id": "src-europe-central-habsburg-monarchy", "kind": "reference",
     "citation": "\"House of Habsburg\" (summary), Encyclopaedia Britannica",
     "url": "https://www.britannica.com/summary/House-of-Habsburg",
     "note": "Britannica states Habsburg control of Hungary and Bohemia ran 1526-1918, matching our range exactly; Habsburg rule of Austria itself dates earlier, to 1282."},
    {"id": "src-europe-central-prussia", "kind": "reference",
     "citation": "\"Prussia\", Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Prussia",
     "note": "Britannica and Wikipedia confirm the Kingdom of Prussia existed 1701-1918; our 1701-1871 end reflects a 'Rise of Prussia' framing ending at German unification, not the state's full lifespan."},
    {"id": "src-europe-eastern-moscow", "kind": "reference",
     "citation": "\"Grand Principality of Moscow\", Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Grand_Principality_of_Moscow",
     "note": "Wikipedia's infobox gives 1263-1478/1547, close to ours, but Britannica's own 'Grand Principality of Moscow' page instead gives c.1251-1505, a genuine cross-source disagreement. [Wikipedia-tier source; no better available]"},
    {"id": "src-south-asia-satavahana", "kind": "reference",
     "citation": "\"Satavahana Empire\", historicindia.org (Encyclopedia of History), corroborated by multiple academic-adjacent sources",
     "url": "https://historicindia.org/article/satavahana-dynasty",
     "note": "Most sources converge on c.230 BCE-220 CE; a Maharashtra government gazetteer instead argues for c.222 BCE-226 CE, and Britannica itself declines to give firm year bounds."},
    {"id": "src-africa-southern-mutapa", "kind": "reference",
     "citation": "\"Mutapa Empire\", New World Encyclopedia",
     "url": "https://www.newworldencyclopedia.org/entry/Mutapa_Empire",
     "note": "Three incompatible ranges exist: New World Encyclopedia's 1450-1629 (+ distinct second polity 1803-1902), Britannica's 1301-1700, and the Wikipedia-consensus 1430-1760 that matches ours."},
    {"id": "src-americas-mesoamerica-purepecha", "kind": "reference",
     "citation": "\"Purépecha Empire\", Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Pur%C3%A9pecha_Empire",
     "note": "Wikipedia states the empire was founded in the early 14th century and fell to Spain in 1530, consistent with our 1300-1530 range. [Wikipedia-tier source; no better available]"},
    {"id": "src-europe-mediterranean-rome-empire-severan", "kind": "institutional",
     "citation": "\"The Severan Dynasty (193-235 A.D.)\", The Metropolitan Museum of Art",
     "url": "https://www.metmuseum.org/essays/the-severan-dynasty-193-235",
     "note": "Met Museum essay title itself states 193-235 A.D., matching our range exactly; Britannica agrees."},
    {"id": "src-europe-mediterranean-rome-empire-valentinianic-theodosian", "kind": "reference",
     "citation": "\"History of the Roman Empire\", Wikipedia",
     "url": "https://en.wikipedia.org/wiki/History_of_the_Roman_Empire",
     "note": "Combining the Valentinianic dynasty's start (364) with the Theodosian dynasty's end (Marcian's death, 457) matches our range exactly as a joint era. [Wikipedia-tier source; no better available]"},
    {"id": "src-south-asia-pallava", "kind": "reference",
     "citation": "\"Pallava dynasty\", Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Pallava_dynasty",
     "note": "Wikipedia and several history-reference sites give 275-897 CE, matching ours; Britannica instead uses a looser 'early 4th to late 9th century' framing. [Wikipedia-tier source; no better available]"},
    {"id": "src-south-asia-pala", "kind": "reference",
     "citation": "\"Pala dynasty\", Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Pala-dynasty",
     "note": "Britannica describes Pala rule as spanning the 8th to 12th century, consistent with our 750-1161 range; precise year figures corroborated by other sources (e.g. Thai Wikipedia: 750-1161)."},
    {"id": "src-south-asia-rashtrakuta", "kind": "reference",
     "citation": "\"Timeline: Rashtrakuta Dynasty\", World History Encyclopedia",
     "url": "https://www.worldhistory.org/timeline/Rashtrakuta_Dynasty/",
     "note": "Most sources place the dynasty's founding in 753 (Dantidurga's defeat of the last Chalukya king), not 735; the 982 end year (Indra IV's death) matches ours exactly."},
    {"id": "src-south-asia-chalukya-badami", "kind": "reference",
     "citation": "\"Chalukya dynasty\", Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Chalukya-dynasty",
     "note": "Britannica gives 543-757 CE for the Western/Badami Chalukyas, matching our range within a few years (753 vs 757 end)."},
]

# entity id -> source id
ATTACH = {
    "africa.nile.egypt.fip": "src-africa-nile-egypt-fip",
    "africa.nile.egypt.sip": "src-africa-nile-egypt-sip",
    "africa.nile.egypt.tip": "src-africa-nile-egypt-tip",
    "africa.nile.egypt.late-period": "src-africa-nile-egypt-late-period",
    "africa.nile.aksum": "src-africa-nile-aksum",
    "east-asia.china.jin": "src-east-asia-china-jin",
    "east-asia.china.north-south": "src-east-asia-china-north-south",
    "east-asia.korea.gojoseon": "src-east-asia-korea-gojoseon",
    "east-asia.korea.three-kingdoms": "src-east-asia-korea-three-kingdoms",
    "east-asia.korea.unified-silla": "src-east-asia-korea-unified-silla",
    "west-asia.mesopotamia.ur3": "src-west-asia-mesopotamia-ur3",
    "west-asia.mesopotamia.kassite": "src-west-asia-mesopotamia-kassite",
    "west-asia.iran.qajar": "src-west-asia-iran-qajar",
    "europe.mediterranean.greece.dark-age": "src-europe-mediterranean-greece-dark-age",
    "europe.western.england.plantagenet": "src-europe-western-england-plantagenet",
    "europe.western.england.stuart": "src-europe-western-england-stuart",
    "europe.western.iberia.reconquista": "src-europe-western-iberia-reconquista",
    "europe.central.habsburg-monarchy": "src-europe-central-habsburg-monarchy",
    "europe.central.prussia": "src-europe-central-prussia",
    "europe.eastern.moscow": "src-europe-eastern-moscow",
    "south-asia.satavahana": "src-south-asia-satavahana",
    "africa.southern.mutapa": "src-africa-southern-mutapa",
    "americas.mesoamerica.purepecha": "src-americas-mesoamerica-purepecha",
    "europe.mediterranean.rome.empire.severan": "src-europe-mediterranean-rome-empire-severan",
    "europe.mediterranean.rome.empire.valentinianic-theodosian": "src-europe-mediterranean-rome-empire-valentinianic-theodosian",
    "south-asia.pallava": "src-south-asia-pallava",
    "south-asia.pala": "src-south-asia-pala",
    "south-asia.rashtrakuta": "src-south-asia-rashtrakuta",
    "south-asia.chalukya-badami": "src-south-asia-chalukya-badami",
}


# ── date corrections ─────────────────────────────────────────────────────────
# (id, field, old, new). Asserting the old value means a future upstream edit that
# changes the date cannot silently invalidate the correction.
CORRECTIONS = [
    ("west-asia.iran.qajar", "start_year", 1789, 1794),
    ("south-asia.rashtrakuta", "start_year", 735, 753),
]

# ── contested dating, kept explicit rather than smoothed ─────────────────────
# id -> list of alternatives to record beside our figure.
ALTERNATIVES = {
    "west-asia.iran.qajar": [
        {"label": "From the start of Agha Mohammad Khan's unification campaign",
         "standing": "minority", "start_year": 1789, "end_year": 1925,
         "note": "The date this dataset used before it was sourced."},
        {"label": "From Agha Mohammad Khan's coronation as shah",
         "standing": "minority", "start_year": 1796, "end_year": 1925},
    ],
    "africa.nile.aksum": [
        {"label": "Britannica, counting the Aksumite successor states",
         "standing": "majority", "start_year": 100, "end_year": 1100,
         "note": "Aksum's collapse is itself disputed; c.940-960 is the narrower reading."},
    ],
    "africa.nile.egypt.sip": [
        {"label": "UCL Digital Egypt", "standing": "majority",
         "start_year": -1700, "end_year": -1550},
        {"label": "World History Encyclopedia", "standing": "minority",
         "start_year": -1782, "end_year": -1539},
    ],
    "europe.eastern.moscow": [
        {"label": "Britannica", "standing": "majority",
         "start_year": 1251, "end_year": 1505,
         "note": "Britannica's own dating differs from the more commonly cited convention."},
    ],
    "south-asia.rashtrakuta": [
        {"label": "From the start of Dantidurga's reign", "standing": "minority",
         "start_year": 735, "end_year": 982,
         "note": "The date this dataset used before it was sourced. It counts the "
                 "founder's career rather than the dynasty's paramountcy."},
        {"label": "Britannica", "standing": "majority",
         "start_year": 755, "end_year": 975},
    ],
    "africa.southern.mutapa": [
        {"label": "Britannica, under 'Matapa'", "standing": "majority",
         "start_year": 1301, "end_year": 1700},
        {"label": "New World Encyclopedia, first Mutapa state only",
         "standing": "minority", "start_year": 1450, "end_year": 1629,
         "note": "Treats 1803-1902 as a separate second Mutapa state."},
    ],
}

# id -> text appended to date_note. These say what the bounds do and do not mean.
DATE_NOTES = {
    "africa.nile.egypt.sip":
        "Egyptology has no agreement on the length of this period or on how to define it; "
        "UCL says so directly. The figures here sit inside the plausible range without "
        "being uniquely confirmed by any one authority.",
    "africa.nile.aksum":
        "Britannica runs Aksum to c.1100 by counting the successor states; the narrower "
        "reading ends the kingdom itself around 940-960.",
    "west-asia.iran.qajar":
        "Britannica dates the dynasty from 1794, when Agha Mohammad Khan eliminated his "
        "last rival. 1789 (campaign) and 1796 (coronation) are also used.",
    "europe.eastern.moscow":
        "1263 is the start of Daniel's line and 1547 Ivan IV's coronation as tsar, which "
        "ends the grand-principality label. Britannica's own dating differs, c.1251-1505.",
    "east-asia.korea.gojoseon":
        "The 2333 BCE start is the traditional Dangun foundation date, not an "
        "archaeological one; there is no material evidence for it. The 108 BCE end is the "
        "Han conquest and is secure.",
    "west-asia.mesopotamia.kassite":
        "These are middle-chronology figures, the convention most used in scientific "
        "publication. Short or long chronology shifts both ends by decades. 1595 BCE is "
        "the Hittite sack of Babylon.",
    "europe.central.habsburg-monarchy":
        "1526 is Ferdinand I's acquisition of the Hungarian and Bohemian crowns, forming "
        "the composite realm. Habsburg rule in Austria alone goes back to 1282.",
    "europe.western.england.stuart":
        "Stuart rule was not continuous: the monarchy was abolished from 1649 to 1660 "
        "under the Commonwealth and Protectorate, then restored. 1603-1714 is a "
        "conventional simplification that elides the interregnum.",
    "europe.central.prussia":
        "1871 is the proclamation of the German Empire, where the story of Prussia's rise "
        "ends. Prussia itself continued as a state until 1918 and as a legal entity later "
        "still.",
    "south-asia.satavahana":
        "One of the most chronologically contested dynasties in ancient India. Britannica "
        "declines firm bounds; a Maharashtra gazetteer argues c.222 BCE-226 CE.",
    "africa.southern.mutapa":
        "The most contested dating in this dataset: three reputable sources give three "
        "incompatible ranges, and this one is corroborated only at Wikipedia tier.",
    "south-asia.rashtrakuta":
        "753 is Dantidurga's defeat of the last Badami Chalukya king, which is when the "
        "dynasty became paramount. Dantidurga's own reign began in 735, so the founder "
        "predates the dynasty as dated here.",
    "east-asia.china.jin":
        "Britannica gives 265 for the start; the one-year difference is a matter of "
        "whether the abdication or the enthronement is counted.",
}

# Caveats where the dating or the label is the problem, not the entity.
CAVEATS = {
    "east-asia.korea.gojoseon": (
        "contested-existence",
        "The 2333 BCE founding comes from the Dangun myth. Historians of Korea treat it "
        "as legend: there is no archaeological and very little textual evidence."),
    "europe.mediterranean.greece.dark-age": (
        "naming-confusion",
        "\u201cDark Age\u201d is disputed and increasingly avoided. Protogeometric, "
        "Geometric and Early Iron Age are used instead; the period was not uniformly one "
        "of decline."),
}

# A better label the field actually prefers.
NAME_FORMS = {
    "europe.mediterranean.greece.dark-age": [
        {"name": "Early Iron Age", "kind": "scholarly"},
    ],
}


# ── summaries ────────────────────────────────────────────────────────────────
# The promoted entities reached the top tier with no summary. A reader who opens
# "Gojoseon" at Essentials should not get a bare date range.
SUMMARIES = {
    "africa.nile.egypt.tip": "Egypt fragmented after the New Kingdom: Libyan and Nubian "
        "dynasties ruled in parallel from different cities, and the Kushite 25th Dynasty "
        "took the whole country.",
    "africa.nile.egypt.late-period": "The last era of native and Persian rule, ending "
        "with Alexander's conquest. Egypt was twice a Persian province and twice "
        "independent again.",
    "africa.nile.aksum": "An Ethiopian trading power on the Red Sea that minted its own "
        "coinage, controlled the incense routes, and adopted Christianity in the fourth "
        "century, making it one of the earliest Christian states.",
    "east-asia.china.jin": "Briefly reunified China after the Three Kingdoms, then lost "
        "the north to steppe powers and fled south \u2014 the beginning of nearly three "
        "centuries of division.",
    "east-asia.china.north-south": "Rival northern and southern courts, the north under "
        "non-Han dynasties that progressively adopted Chinese administration. Buddhism "
        "spread widely in both.",
    "east-asia.korea.gojoseon": "The first Korean state in the traditional account, in the "
        "peninsula's northwest and southern Manchuria, ended by Han conquest in 108 BCE.",
    "east-asia.korea.unified-silla": "Silla, allied with Tang China, defeated Baekje and "
        "Goguryeo and then turned on its ally, unifying most of the peninsula for the "
        "first time and presiding over a Buddhist cultural peak.",
    "west-asia.mesopotamia.ur3": "The last Sumerian-speaking dynasty, which left the "
        "earliest surviving law code and an administrative archive of tens of thousands of "
        "tablets.",
    "west-asia.mesopotamia.kassite": "Four centuries of stable Babylonian rule under a "
        "dynasty of foreign origin, during which Babylon became a recognised great power in "
        "the diplomacy of the Late Bronze Age.",
    "west-asia.iran.qajar": "The dynasty that lost the Caucasus to Russia, granted the "
        "concessions that made Iran a field of Anglo-Russian competition, and was forced "
        "into a constitution in 1906.",
    "europe.mediterranean.greece.dark-age": "The centuries between the collapse of "
        "Mycenaean palace society and the emergence of the city-states: writing was lost "
        "and populations fell, but iron came into use and the epics took shape.",
    "europe.western.england.plantagenet": "Three centuries covering Magna Carta, the first "
        "English parliaments, the Black Death, the Hundred Years' War and the Wars of the "
        "Roses.",
    "europe.western.england.stuart": "Union of the English and Scottish crowns, civil war, "
        "regicide, republic, restoration and the constitutional settlement of 1688.",
    "europe.western.iberia.reconquista": "The long, discontinuous Christian expansion "
        "against Muslim al-Andalus, ending in 1492 with Granada \u2014 the same year as the "
        "expulsion of the Jews and Columbus's first voyage.",
    "europe.central.habsburg-monarchy": "A composite realm assembled by marriage rather "
        "than conquest, holding together Austrians, Hungarians, Czechs, Poles, Croats, "
        "Romanians and Italians until nationalism pulled it apart in 1918.",
    "europe.central.prussia": "A minor Baltic state that turned military and "
        "administrative reform into great-power status, then unified Germany around itself.",
    "europe.eastern.moscow": "A minor principality under Mongol overlordship that "
        "outmanoeuvred its rivals, absorbed them, stopped paying tribute, and became the "
        "core of the Russian state.",
    "central-asia.samanid": "A Persian revival in Bukhara and Samarkand: the dynasty under "
        "which New Persian became a literary language again, patronising Rudaki, Ferdowsi's "
        "sources and Avicenna's education.",
    "central-asia.timurid": "Timur's conquests were devastating and short-lived, but the "
        "dynasty he founded made Samarkand and Herat centres of astronomy, miniature "
        "painting and architecture, and produced the founder of Mughal India.",
    "south-asia.mahajanapadas": "India's second urbanisation: sixteen or so states across "
        "the Ganges plain, some kingdoms and some republics, the setting in which Buddhism "
        "and Jainism emerged.",
    "south-asia.indo-greek": "Greek-speaking kings ruling in Bactria and northwest India "
        "after Alexander, issuing bilingual coinage and, in Menander's case, appearing in "
        "Buddhist literature as a convert.",
    "south-asia.satavahana": "The dominant power of the Deccan between the Maurya and Gupta "
        "empires, controlling the trade that carried Roman coinage into central India.",
    "south-asia.pallava": "A Tamil dynasty at Kanchipuram whose rock-cut temples at "
        "Mahabalipuram set the pattern for South Indian architecture, and whose script was "
        "carried across Southeast Asia.",
    "south-asia.chalukya-badami": "Rulers of the western Deccan from Badami, remembered for "
        "cave temples and for a long contest with the Pallavas to the south.",
    "south-asia.rashtrakuta": "A Deccan empire that raided north and south alike and built "
        "the Kailasa temple at Ellora, cut whole from the rock as a single excavation.",
    "south-asia.maratha": "The power that broke Mughal dominance in the Deccan and "
        "governed much of the subcontinent through a confederacy of chiefs, until the "
        "British defeated it in three wars.",
    "south-asia.sikh-empire": "Ranjit Singh's state in Punjab, which absorbed Kashmir and "
        "Peshawar, kept the British at the Sutlej for a generation, and fell within a "
        "decade of his death.",
    "south-asia.pala": "The last major Buddhist dynasty in India, patrons of Nalanda and "
        "Vikramashila, from which Buddhism was carried into Tibet.",
    "africa.southern.mutapa": "A gold-trading state that succeeded Great Zimbabwe, dealt "
        "with Swahili and later Portuguese merchants, and was progressively undermined by "
        "them.",
    "americas.mesoamerica.zapotec": "Builders of Monte Alb\u00e1n, a city levelled from a "
        "mountaintop, and users of one of the earliest writing systems in the Americas.",
    "americas.mesoamerica.toltec": "A central Mexican power at Tula that later "
        "Mesoamericans, the Aztecs above all, treated as the model of civilisation and "
        "claimed descent from.",
    "americas.mesoamerica.purepecha": "The Aztecs' most effective rival, never conquered by "
        "them, and the only Mesoamerican state working metal for tools and weapons at scale.",
    "europe.mediterranean.rome.empire.severan": "A dynasty of provincial origin that "
        "widened citizenship, leaned openly on the army for legitimacy, and ended in the "
        "assassination that opened the third-century crisis.",
    "europe.mediterranean.rome.empire.valentinianic-theodosian": "The last dynasties to "
        "rule a single empire: Christianity became the state religion, the Goths won at "
        "Adrianople, and the final administrative division of east and west set in.",
}


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}

    missing = [i for i in ATTACH if i not in by_id]
    if missing:
        raise KeyError(f"promoted_sourcing: unknown ids {missing}")

    # Corrections first, asserting the old value so an upstream change cannot slip past.
    for eid, field, old, new in CORRECTIONS:
        e = by_id[eid]
        if e[field] != old and e[field] != new:
            raise AssertionError(
                f"promoted_sourcing: {eid}.{field} is {e[field]}, expected {old} before "
                f"correcting to {new}; the upstream date changed")
        e[field] = new

    for eid, source_id in ATTACH.items():
        e = by_id[eid]
        e["source_ids"] = sorted(set(e.get("source_ids", [])) | {source_id})

    for eid, alts in ALTERNATIVES.items():
        e = by_id[eid]
        existing = list(e.get("alternatives", []))
        labels = {a["label"] for a in existing}
        for a in alts:
            if a["label"] not in labels:
                existing.append({**a, "source_ids": [ATTACH[eid]]})
        e["alternatives"] = existing

    for eid, note in DATE_NOTES.items():
        e = by_id[eid]
        prior = (e.get("date_note") or "").strip()
        if note not in prior:
            e["date_note"] = f"{prior} {note}".strip()

    for eid, (kind, text) in CAVEATS.items():
        e = by_id[eid]
        assert len(text) <= 200, f"{eid}: caveat is {len(text)} chars, max 200"
        cav = list(e.get("caveats", []))
        if not any(c["text"] == text for c in cav):
            cav.append({"kind": kind, "text": text, "source_ids": [ATTACH[eid]]})
        e["caveats"] = cav

    for eid, forms in NAME_FORMS.items():
        e = by_id[eid]
        nf = list(e.get("name_forms", []))
        have = {f["name"] for f in nf}
        for f in forms:
            if f["name"] not in have:
                nf.append(f)
        e["name_forms"] = nf

    # Dantidurga reigned 735-756 and founded the dynasty, which is dated from his 753
    # victory. The founder predating his own dynasty is a real pattern, not a data error,
    # and the schema has a flag for exactly this.
    founder = by_id.get("south-asia.rashtrakuta.dantidurga")
    if founder is not None:
        founder["allow_outside_parent_dates"] = True
        prior = (founder.get("date_note") or "").strip()
        extra = ("His reign began in 735, before the 753 victory over the Chalukyas from "
                 "which the dynasty is dated.")
        if extra not in prior:
            founder["date_note"] = f"{prior} {extra}".strip()

    wrote = 0
    for eid, text in SUMMARIES.items():
        e = by_id.get(eid)
        if e is None:
            raise KeyError(f"promoted_sourcing: unknown summary id {eid}")
        if not (e.get("summary") or "").strip():
            e["summary"] = text
            wrote += 1

    print(f"Promoted sourcing: {len(ATTACH)} sourced, {len(CORRECTIONS)} dates corrected, "
          f"{sum(len(v) for v in ALTERNATIVES.values())} alternatives, {wrote} summaries")
