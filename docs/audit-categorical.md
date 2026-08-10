# Audit: categorical gaps

**Lens:** whole *kinds* of history that are absent, not missing dynasties. Every claim below
was checked against `inventory.txt` by name and by plausible alias before being reported.

## The shape of the problem

The kind counts tell the story: `reign: 690`, `period: 602`, `era: 350`, then a cliff —
`event: 43`, `threshold: 26`, `taxon: 12`. The dataset is a very good genealogy of political
authority and a very thin record of everything that happened *to* people rather than *by*
rulers.

Two structural facts make it worse than the raw numbers suggest:

1. **The 43 events are not distributed as history.** By era: 8 are prehistoric/archaeogenetic
   (`The Speed of Egyptian State Formation`, `The Narmer Palette`, `North American Megafaunal
   Extinction`, `The 8.2 Kiloyear Event`, `Storegga Slide Tsunami`, `The Steppe Ancestry
   Influx`, `The Rakhigarhi Genome`, `Arrival of the Dingo`), 2 are historiographic disputes
   (`The Yayoi Redating Controversy`, `The Ghaggar-Hakra Question` is a period not an event),
   and of the remainder **14 are battles, wars, or massacres**. The entire span 500 CE–1300 CE
   contains exactly two events in the whole dataset (`Arab Conquest of Iran` 633–651,
   `Black Death` 1346–53 — the latter is 14th c.). Eight hundred years of world history with
   one event.

2. **The 26 thresholds stop at 1650 BC.** The last threshold in the dataset by start date is
   `Domestic Chicken [threshold] 1650BC`. Every technology after the chicken — iron smelting,
   the alphabet, paper, printing, gunpowder, the compass, the stirrup, the mouldboard plough,
   the astrolabe, positional zero, the telescope, the steam engine, vaccination, germ theory,
   electrification, the transistor — has no representation of any kind. `The Invention of
   Coinage [event] 650BC` is the sole exception and it is misfiled as an `event` under
   Anatolia rather than a `threshold`. The threshold vocabulary was built for palaeoanthropology
   and then abandoned at the Bronze Age.

**On `Global & Multi-Regional` (113 entities):** it is the right home for most of what follows,
but it is not currently doing that job. Of its 113 entities, 57 are prehistoric (Behavioural
Firsts + Paleolithic + Hominins + Neolithic Transition), and the historical remainder is a
periodisation scaffold (`BCE`, `CE`, `Bronze Age`, `Iron Age`, `Classical Antiquity`,
`Late Antiquity`, `Middle Ages`, `Early Modern`, `Long 19th Century`, `Short 20th Century`,
`Contemporary`) plus `Multi-Regional Empires` (which is really a caliphate/Ottoman list) plus
the 20th-century war-and-crisis chain. There is no branch under it for disease, climate,
religion, trade, or ideas. Those branches need to be created; the periodisation eras are the
natural parents for them, and several clusters below need a new intermediate node.

---

### Epidemic and pandemic disease

**Severity:** high
**What is missing:** the dataset contains exactly two disease entities in all of history —
`Black Death [event] 1346..1353` under `Middle Ages`, and `COVID-19 Pandemic [event]
2020..2023` under `Contemporary`. A search for "plague", "epidemic", "pox", "influenza",
"cholera" returns nothing else. Absent and authorable:
- Plague of Athens (430–426 BC)
- Antonine Plague (165–180)
- Plague of Cyprian (249–262)
- Plague of Justinian and the First Plague Pandemic (541–549; recurrences to c. 750)
- Japanese smallpox epidemic of 735–737
- Columbian Exchange virgin-soil die-off (1492–1650) — the single largest mortality event in
  the dataset's coverage and entirely unrepresented
- Cocoliztli epidemics of New Spain (1545–1548, 1576–1580)
- Third Plague Pandemic (1855–1960)
- Cholera pandemics, first through seventh (1817–present)
- 1918–1920 influenza pandemic
- HIV/AIDS pandemic (1981–present)

**Where it belongs:** a new `Disease & Demography` node under `Global & Multi-Regional
[region]`, with individual epidemics also datable into the regional branches they struck —
Plague of Athens under `Classical Greece [period] 480BC..323BC`, Antonine Plague under
`Nerva–Antonine Dynasty [period] 96..192`, Plague of Justinian under `Justinian I [reign]
527..565`, cocoliztli under `Mesoamerica [region]`, virgin-soil die-off under `The Columbian
Exchange [era] 1492..1700`.
**Why it matters:** without these a reader sees Athens lose the Peloponnesian War for
strategic reasons, the Roman third-century crisis as purely political, Justinian's
reconquest as failing through overreach, and the Americas as conquered by 600 Spaniards
rather than by smallpox. `The Columbian Exchange [era]` exists as a node with **zero
children** — the die-off is the thing it was created to hold.
**Rough dates:** 430 BC – present.

### Climate and volcanic forcing

**Severity:** high
**What is missing:** the dataset has three palaeoclimate entities — `The 8.2 Kiloyear Event
[event] 6300BC..6140BC`, `Storegga Slide Tsunami [event] 6191BC..6191BC`, `Green Sahara
[period] 12551BC..3051BC` — and then nothing for the whole historical period. No entity in
the dataset contains "Dryas", "volcan", "eruption", "drought", "famine", or "warm period".
Absent:
- Younger Dryas (10,900–9,700 BC) — a glaring hole given `Mesolithic (Eurasia) [era]
  10000BC..5000BC` and 120 pre-10,000 BC entities sit on either side of it
- 4.2 kiloyear event (c. 2200–1900 BC) — the dataset already has `Harappan Deurbanisation
  [period] 2200BC..1900BC` and the collapse of the Akkadian Empire and Old Kingdom Egypt at
  the same dates, with no shared cause named
- 3.2 kiloyear event / Late Bronze Age drought (c. 1250–1100 BC)
- Roman Warm Period (c. 250 BC – 400 CE)
- Late Antique Little Ice Age and the 536 CE dust veil (536–660)
- Medieval Climate Anomaly (c. 950–1250)
- Little Ice Age (c. 1300–1850), with the Maunder Minimum (1645–1715)
- Laki eruption (1783–84), Tambora and the Year Without a Summer (1815–16)
- Anthropogenic warming (c. 1850–present) — the dataset ends its causal story in 1991 with
  the USSR and has no environmental entity at all in `Contemporary [era] 1991..—`

**Where it belongs:** a new `Climate & Environment` node under `Global & Multi-Regional
[region]`; the Younger Dryas belongs beside the existing 8.2 ka event, which currently sits
oddly under `European Prehistory [era]` rather than in the global branch. `Late Bronze Age
Collapse [event] 1200BC..1150BC` already exists under `Bronze Age [era]` but has no
climatic, epidemic, or migratory children — it is a label without a mechanism.
**Why it matters:** the three biggest synchronised collapses in the dataset (2200 BC,
1200 BC, 536 CE) are each represented only by their political symptoms. A reader cannot see
why unrelated states failed in the same decades.
**Rough dates:** 10,900 BC – present.

### Religion as a category

**Severity:** high
**What is missing:** this is the largest single hole. The dataset contains **no religion as
an entity**. Verified absent by name: Buddhism, Christianity, Hinduism, Zoroastrianism,
Judaism (only `Kingdoms of Israel and Judah [era]`, a polity), Confucianism, Daoism, Jainism,
Shinto, Sikhism (only `Sikh Empire [era] 1799..1849`). No entity contains "temple",
"church", "monast", "council", "ritual", "sacrifice", or "monotheis". What exists is four
items: `Axial Age [era] 800BC..200BC` (no children), `Rise of Islam [era] 610..632`,
`The Reformation [era] 1517..1648` (children: Luther and the Thirty Years' War), and
`The Vedic Corpus [era] 1500BC..500BC`. Absent and authorable:
- Zoroaster and Zoroastrianism (c. 1000 BC – present)
- Upanishadic period and the śramaṇa movements (c. 800–400 BC)
- Siddhartha Gautama (c. 480–400 BC) and Mahavira (c. 599–527 BC) — note the schema already
  uses `[reign]` for non-rulers (`Pericles (statesman)`, `Cicero`, `Martin Luther
  (theologian)`, `Guru Nanak`), so founders are authorable without a new kind
- Confucius (551–479 BC), Laozi and the Daodejing, Mozi
- Second Temple Judaism (516 BC – 70 CE), the Babylonian Exile, destruction of the Temple (70),
  rabbinic Judaism and the Talmud (c. 200–600)
- Rise of Christianity (c. 30–380), Edict of Milan (313), First Council of Nicaea (325),
  Council of Chalcedon (451) and the Oriental Orthodox split, Christianisation of the Roman
  Empire (380)
- Ashokan Buddhist patronage and missions (c. 250 BC), Buddhism's transmission along the
  Silk Road to China (1st–5th c.), Mahayana emergence (1st c. BC – 1st c. CE), Chan/Zen,
  Vajrayana and the Tibetan transmissions (7th–11th c.), decline of Buddhism in India
- Islam after 632: the First Fitna and the Sunni–Shia split (656–661), Karbala (680),
  the schools of fiqh and sharia (8th–9th c.), Sufism and the tariqas (9th c. onward),
  Ismaili and Twelver Shiism
- East–West Schism (1054), monasticism (Benedictine c. 529, Cluny, the friars), the Crusades
  (1095–1291) — the dataset has no crusade entity of any kind
- Bhakti movement (7th–17th c.), Sikhism as a religion (1499 onward), Sant tradition
- Catholic Reformation / Council of Trent (1545–63), Calvinism, Anabaptism, Anglicanism,
  Puritanism, later Protestant revivals

**Where it belongs:** a new `Religions & Religious Movements` node under `Global &
Multi-Regional [region]`, with regional children placed in situ: Second Temple Judaism under
`Mesopotamia & Levant [region]`, Nicaea and the councils under `Roman Empire [era]
27BC..476` and `Byzantine Empire [era] 330..1453`, the Fitna under `Rashidun Caliphate [era]
632..661`, the Buddha and śramaṇas under `Mahajanapadas (Second Urbanization) [era]
600BC..345BC`, bhakti under `Chola Empire [era] 848..1279` and the Delhi Sultanate period,
Confucius under `Eastern Zhou`/`Spring and Autumn`, the councils of Trent under
`The Reformation [era] 1517..1648`. `Axial Age [era] 800BC..200BC` is an empty container
crying out for exactly these children.
**Why it matters:** roughly half of all recorded human motivation is missing. A reader can
see the Umayyad and Abbasid caliphates but not what Sunni or Shia means; can see `Ashoka the
Great [reign] 268BC..232BC` but not why he matters; can see the `Byzantine Empire` and the
`Holy Roman Empire` without the schism that separates them.
**Rough dates:** c. 1500 BC – present.

### Technology and science after 1650 BC

**Severity:** high
**What is missing:** as noted, thresholds terminate at `Domestic Chicken [threshold]
1650BC`. `The Wheel [threshold] 3500BC` and `Writing [threshold] 3400BC` exist; individual
writing systems and every post-Bronze-Age technology do not. Absent:
- Bronze and tin alloying (c. 3300 BC) — `Bronze Age [era]` exists as a period label but the
  metallurgy itself is not a threshold
- Iron and steel smelting (c. 1200 BC; crucible/wootz steel c. 300 BC) — same problem with
  `Iron Age [era] 1200BC..550BC`
- Cuneiform, Egyptian hieroglyphs, Chinese oracle-bone script (c. 1200 BC), Linear B,
  the Phoenician consonantal alphabet (c. 1050 BC) and the Greek vowel alphabet (c. 800 BC)
- Coinage — exists but as `The Invention of Coinage [event] 650BC` under Anatolia; should be
  a global threshold
- Iron ploughshare and mouldboard plough, horse collar (5th c. China, 9th c. Europe), stirrup
  (4th c. China, 8th c. Europe), horseshoe
- Papermaking (c. 100 CE), woodblock printing (7th c.), movable type (Bi Sheng c. 1040;
  Korean metal type 13th c.; Gutenberg c. 1450)
- Gunpowder (9th c.), the gun and cannon (13th–14th c.), the trace italienne and the
  gunpowder-fortification revolution
- Magnetic compass (11th c. China), sternpost rudder, lateen rig, the carvel-built full-rigged
  ship and caravel (15th c.), the marine chronometer (1761)
- Zero and positional notation (Brahmi/Indian, c. 3rd–7th c.), algebra (al-Khwarizmi c. 820),
  Hindu–Arabic numerals in Europe (Fibonacci 1202), logarithms (1614), calculus (1665–75)
- Astrolabe, the water-driven mill, the mechanical clock (c. 1300), spectacles
- Telescope and microscope (1608–10), the barometer, the vacuum pump
- Newcomen and Watt steam engines (1712, 1769), coke smelting, the power loom, the
  Bessemer converter (1856)
- Variolation and Jennerian vaccination (1796), anaesthesia (1846), germ theory (1861–76),
  antisepsis, antibiotics (1928/1942), the Haber–Bosch process (1909), the Green Revolution
- Electric generation and distribution (1831/1882), telegraph (1844), telephone, radio
- Fission and the bomb (1938/1945), the transistor (1947), the integrated circuit (1958),
  the internet (1969/1983), DNA structure (1953) and genome sequencing (2003)

**Where it belongs:** the existing `Behavioural Firsts [era] 3390000BC..—` under `Global &
Multi-Regional` is scoped to palaeoanthropology and should not be stretched to 1947. Author a
sibling — `Technological Thresholds` — under `Global & Multi-Regional [region]`, subdivided
by the existing periodisation eras (`Bronze Age`, `Iron Age`, `Middle Ages`, `Early Modern`,
`Industrial Revolution`, `Second Industrial Revolution`, `Short 20th Century`).
**Why it matters:** the dataset currently implies that after someone domesticated a chicken,
nothing was invented. `Industrial Revolution [era] 1760..1840` and `Second Industrial
Revolution [era] 1870..1914` both have **no children at all** — they are named without a
single machine, process, or discovery inside them.
**Rough dates:** 3300 BC – 2003 CE.

### Trade networks and economic systems

**Severity:** high
**What is missing:** no entity in the dataset contains "trade", "Silk", "bank", "guild",
"serf", "caste", or "market". The only economic entities are four chartered companies
(`Dutch East India Company [era] 1602..1799`, `Dutch West India Company`, `Second Dutch West
India Company`, `East India Company Rule [era] 1757..1858`) and `Mamluk (Slave) Dynasty
[period] 1206..1290`, which is a polity not an institution. Absent:
- Silk Road / trans-Eurasian exchange (c. 130 BC – 1450, with the Pax Mongolica peak
  1250–1350)
- Indian Ocean monsoon trade (c. 500 BC – 1500), the Periplus network, the Swahili–Gujarat–
  Malabar circuits, Srivijaya's and Malacca's straits tolls
- Trans-Saharan gold-and-salt trade (c. 700–1600) — the dataset has `Ghana Empire`,
  `Mali Empire`, `Songhai Empire` with no explanation of what they traded
- Hanseatic League (c. 1160–1669), the Champagne fairs, Venetian and Genoese Mediterranean
  systems, the Levant trade
- Atlantic slave trade (1526–1867) and the triangular trade — **entirely absent**, including
  the Middle Passage and the abolition movement (1787–1888)
- Indian Ocean and trans-Saharan slave trades (c. 800–1900)
- Serfdom in western Europe (c. 900–1400) and its later Russian and Polish forms (to 1861),
  manorialism, the encomienda and hacienda, the plantation complex, chattel slavery as an
  institution, indentured labour and the post-1834 coolie system
- Varna and jati (caste) as a social structure, c. 1000 BC – present
- Craft guilds (12th–18th c.), bills of exchange, double-entry bookkeeping (Pacioli 1494),
  the Medici and Fugger banks, central banking (Amsterdam 1609, Bank of England 1694), the
  joint-stock corporation, the South Sea and Mississippi bubbles (1720)
- The gold standard (1870s–1930s), Bretton Woods (1944–71), the demographic transition
  (c. 1750–present), the Great Divergence

**Where it belongs:** a new `Trade, Labour & Economic Systems` node under `Global &
Multi-Regional [region]`. Several belong regionally too: trans-Saharan trade under `West
Africa & Sahel [region]`, Indian Ocean trade spanning `East Africa`, `South Asia` and
`Maritime Southeast Asia`, the Hanse under `Northern Europe [region]`, the Atlantic slave
trade under `Age of Exploration / Age of Sail [era] 1418..1815` and `The Columbian Exchange
[era] 1492..1700`.
**Why it matters:** the dataset explains where power sat but never how it was paid for. The
absence of the Atlantic slave trade in a dataset that includes the Dutch West India Company
and the Berlin Conference is the most conspicuous single omission in the file.
**Rough dates:** c. 1000 BC – present.

### Migrations and language spreads

**Severity:** medium
**What is missing:** partial coverage exists and is good where present — `The Austronesian
Expansion [era] 3551BC..1130BC`, `The Steppe Ancestry Influx [event] 3000BC..2900BC`,
`Arrival of Steppe Ancestry in South Asia [period] 1900BC..1500BC`, `Migration Period [era]
376..800`, `The Anatolian Farmer Turnover [era] 6500BC..4000BC`, `The Two Routes of Neolithic
Spread [era] 6500BC..4000BC`, `Neolithic Migration into Southeast Asia [event] 2051BC`. Still
absent:
- Bantu expansion (c. 1000 BC – 500 CE) — the dataset has only `Bantu Homeland Phase [period]
  5051BC..2051BC`, i.e. the homeland but not the expansion, which is the reason most of
  sub-Saharan Africa speaks what it speaks
- Indo-European dispersal as a named process (c. 4000–1000 BC) — the genetic proxies exist,
  the language-family spread does not
- Sea Peoples (c. 1200–1150 BC)
- Turkic westward migrations (6th–11th c.), Oghuz/Seljuk entry into Iran and Anatolia
- Arab tribal settlement after the conquests (7th–8th c.)
- Slavic expansion (5th–8th c.), Magyar arrival (895), Viking diaspora and settlement
  (793–1066) — no "Viking" or "Norse" entity exists
- Han settlement of the south and the Ming/Qing frontier movements
- Atlantic European emigration (1815–1930, c. 55 million people), Indian and Chinese
  indentured diasporas (1834–1920), Great Migration within the US (1916–70), post-1945
  labour migrations, post-1947 partition displacement (the event exists; the migration does
  not)
- Sinicisation of writing across East Asia; spread of Arabic, Latin, Spanish, English

**Where it belongs:** a new `Migrations & Language Spreads` node under `Global &
Multi-Regional [region]`; Bantu expansion under `Africa [region]` alongside `Bantu Homeland
Phase`, Sea Peoples under `Late Bronze Age Collapse [event] 1200BC..1150BC`, Turkic
migrations under `Eurasian Steppe [region]` and `Anatolia [region]`.
**Why it matters:** language maps are the most durable trace most societies leave, and the
dataset explains the deep-prehistoric ones well and the historical ones not at all.
**Rough dates:** c. 4000 BC – 1970.

### Law, governance concepts, and political ideas

**Severity:** high
**What is missing:** no entity in the dataset contains "law", "code", "constitution",
"suffrage", "examination", "republic" (except as a polity name), or "rights". Absent:
- Code of Hammurabi (c. 1754 BC) — `Hammurabi [reign] 1792BC..1750BC` exists; the code does
  not
- Ur-Nammu's laws, Hittite laws, the Torah as law, Draco and Solon's reforms (621/594 BC)
- Twelve Tables (451 BC), the praetorian edict, Roman jurisprudence, the Antonine
  Constitution (212), Corpus Juris Civilis (529–534) — `Justinian I [reign] 527..565` exists
  without the legal codification that is the reason his name survives
- Legalism and the Qin administrative model, the Han synthesis, the Tang Code (653),
  Confucian bureaucracy and the imperial examination system (keju, 605–1905) — a
  thousand-year institution with no entity, in a branch (`East Asia`, 518 entities) that is
  the dataset's largest
- Sharia and the schools of fiqh (8th–9th c.), the qadi system
- Magna Carta (1215), the origins of parliament (1265/1295), English common law, the
  Ottoman kanun, Justinian's reception and the medieval revival of Roman law (Bologna,
  c. 1088)
- Westphalian sovereignty (1648), habeas corpus, the Bill of Rights (1689), the separation
  of powers, the US Constitution (1787), the Declaration of the Rights of Man (1789), the
  Napoleonic Code (1804)
- Abolition of slavery (1807/1833/1865/1888), serf emancipation (1861), universal male
  suffrage, women's suffrage (1893–1971), the Universal Declaration of Human Rights (1948),
  the Geneva Conventions
- `Decolonization [era] 1945..1997` exists with **no children** — no Indian independence as
  a global process, no Bandung (1955), no Year of Africa (1960), no Algerian War, no
  Vietnamese or Indonesian independence, no UN Resolution 1514

**Where it belongs:** a new `Law & Governance` node under `Global & Multi-Regional [region]`,
plus in-place children: Hammurabi's code under `Hammurabi [reign] 1792BC..1750BC`, the Twelve
Tables under `Early Republic [period] 509BC..287BC`, the Corpus under `Justinian I [reign]`,
the examination system under `China [region]` spanning `Tang Dynasty [era] 618..907` to
`Qing`, Magna Carta under `Western Europe [region]`, the suffrage and rights entities under
`Long 19th Century [era] 1789..1914` and `Short 20th Century [era] 1914..1991`.
**Why it matters:** these are the entities a reader actually looks up. The dataset can name
every Chinese emperor and cannot say how China was governed.
**Rough dates:** c. 2100 BC – 1971.

### Intellectual and artistic movements outside Europe

**Severity:** medium
**What is missing:** European coverage here is genuinely decent — `The Renaissance [era]
1300..1600` with Italian and Northern children, `Scientific Revolution [era] 1543..1700`,
`The Enlightenment [era] 1680..1815`. The problem is that these four are the *only*
intellectual entities in the dataset, and they sit under `Europe [region]`, which frames
"having ideas" as a European activity. Absent:
- Presocratics, the Academy and Lyceum, Hellenistic philosophy — Stoicism, Epicureanism,
  Scepticism, Neoplatonism (c. 600 BC – 500 CE)
- Library and Museum of Alexandria, Hellenistic astronomy and mathematics (Euclid,
  Archimedes, Ptolemy)
- Nyaya, Samkhya, Vedanta and the six darshanas; Panini's grammar (c. 500 BC); Nagarjuna;
  Nalanda (5th–12th c.); Aryabhata, Brahmagupta, Bhaskara, the Kerala school
- Hundred Schools of Thought (c. 500–221 BC), Neo-Confucianism (Zhu Xi, 12th c.),
  Han and Song historiography, Chinese astronomy and the Song technological peak
- Graeco-Arabic translation movement and the House of Wisdom (8th–10th c.); the Islamic
  Golden Age as an intellectual entity (c. 800–1250) — the caliphates are all present, the
  scholarship is not; al-Khwarizmi, Ibn Sina, al-Biruni, Ibn al-Haytham, Ibn Rushd,
  Ibn Khaldun (1332–1406), the Maragha and Samarkand observatories
- Latin scholasticism and the medieval university (Bologna 1088, Paris c. 1150, Oxford),
  Aquinas, the twelve-century translations from Arabic
- Romanticism (c. 1790–1850), Positivism, Marxism, Darwinism (1859), Modernism
  (c. 1890–1940), psychoanalysis, relativity and quantum mechanics as intellectual events
- The Renaissance is present with no `Humanism` and no printing revolution attached

**Where it belongs:** the four existing movements should arguably be re-parented, or mirrored,
into a `Intellectual & Artistic Movements` node under `Global & Multi-Regional [region]`, with
regional children: Hellenistic philosophy under `Classical Greece [period] 480BC..323BC`, the
translation movement under `Abbasid Caliphate [era] 750..1258`, Hundred Schools under
`Eastern Zhou`, the darshanas under `Vedic Period`/`Mahajanapadas`, Neo-Confucianism under
`Song Dynasty [era] 960..1279`.
**Why it matters:** with only European movements represented, the tree makes an implicit
claim about where thought happens that the rest of the dataset's careful regional balance
otherwise avoids.
**Rough dates:** c. 600 BC – 1940.

### Art, architecture, and material culture after prehistory

**Severity:** medium
**What is missing:** the dataset treats art seriously in prehistory — `Chauvet Cave Art`,
`Altamira Cave Art`, `Lascaux Cave Art`, `Blombos Cave`, `Figurative Art [threshold]`,
`Abstract Engraving [threshold]`, `Use of Pigment [threshold]` — and then stops. There is no
entity for any historical artistic tradition, monument, or building programme. No "pyramid",
"temple", "cathedral", "mosque" entity exists anywhere; `Stonehenge Construction [period]`
and `Newgrange [period]` are the last monuments in the file, both prehistoric. Absent:
- Giza pyramid complex (c. 2560 BC) — `Khufu [reign] 2589BC..2566BC` exists without it
- Parthenon (447–432 BC), Hellenistic and Roman monumental architecture, Roman concrete
- Terracotta Army and the Qin mausoleum (c. 210 BC), the Great Wall as a construction
  programme
- Ajanta and Ellora, Borobudur (c. 800), Angkor Wat (c. 1150), Great Zimbabwe (c. 1100–1450)
- Hagia Sophia (537), Dome of the Rock (691), the Alhambra, Timurid architecture, the Taj
  Mahal (1632–53)
- Gothic cathedrals (1140 onward), Song landscape painting, Persian miniature, ukiyo-e
- Bronze casting traditions: Shang, Benin, Chola

**Where it belongs:** `Global & Multi-Regional [region]` is the wrong home for most of these;
they should attach to the polity that built them — Giza under `4th Dynasty [period]
2613BC..2494BC`, Hagia Sophia under `Justinian I [reign] 527..565`, Angkor Wat under the
Khmer entries in `Mainland Southeast Asia [region]`, Great Zimbabwe under `Southern Africa
[region]`.
**Why it matters:** the dataset knows what a cave painting is and not what a cathedral is.
Monuments are also the primary way non-specialist readers enter a period.
**Rough dates:** c. 2560 BC – 1900.

### Famine, natural disaster, and demographic shock (non-epidemic)

**Severity:** medium
**What is missing:** no entity contains "famine", "earthquake", "flood", or "drought".
Absent:
- Antioch earthquake (526), Shaanxi earthquake (1556, c. 830,000 dead), Lisbon earthquake
  and tsunami (1755), Tangshan (1976)
- Yellow River course changes and floods (1048, 1194, 1855, 1887, 1931) — a recurring
  determinant of Chinese dynastic fate in a branch of 518 entities
- Great Famine of 1315–17, Great Bengal Famine of 1770, Irish Famine (1845–52), Indian
  famines of 1876–78 and 1896–1902, Chinese famine of 1876–79, Soviet famines (1921–22,
  1932–33), Bengal 1943, Great Chinese Famine (1959–61)
- The Holocaust and the 20th-century genocides — `Nazi Germany [era] 1933..1945` and
  `World War II [event] 1939..1945` exist; the Holocaust, the Armenian genocide (1915),
  Rwanda (1994) and Cambodia (1975–79) do not appear anywhere

**Where it belongs:** the famines and disasters mostly regionally (`China [region]`, `South
Asia [region]`, `Western Europe [region]`); the genocides under `Short 20th Century [era]
1914..1991` in `Global & Multi-Regional`. The absence of the Holocaust is severe enough on
its own to warrant treating this as high rather than medium if the maintainers agree.
**Rough dates:** 526 – 1994.

### Warfare as a system, not a list of battles

**Severity:** low
**What is missing:** the dataset has 14 battle/war events, heavily weighted to Rome, Napoleon
and the 20th century (`Battle of Kadesh`, `Battle of Actium`, `Battle of Austerlitz`,
`Battle of Trafalgar`, `Battle of Waterloo`, the world wars, Korea, Vietnam). What is absent
is the change in how war worked:
- Chariot warfare (c. 1700–1200 BC), the composite bow, massed infantry and the hoplite
  phalanx, the Roman legion as an institution
- Steppe cavalry archery and its dominance (c. 700 BC – 1500 CE)
- The stirrup and heavy cavalry, the castle, the crossbow
- The gunpowder revolution and the decline of cavalry (14th–17th c.), the military revolution
  and standing armies (1550–1700), levée en masse (1793), industrialised war (1861–1918),
  nuclear deterrence (1945–)
- The Crusades (1095–1291), the Mongol conquests as a campaign system (the empire exists as
  `Mongol Empire [era] 1206..1368`; the conquests and their demographic effect do not),
  the Hundred Years' War, the Napoleonic Wars as a system (only three battles), the Punic
  Wars (only `Middle Republic (Punic Wars) [period]`)

**Where it belongs:** the technological items in the proposed `Technological Thresholds`
node; the campaigns under the relevant polities.
**Why it matters:** low severity only because the political spine partly covers it — but the
existing battle selection is regionally lopsided in a way the rest of the dataset is not.
**Rough dates:** c. 1700 BC – 1945.

---

## Genuinely fine

Two clean bills of health, since absence of a hole is information:

- **Deep prehistory and palaeoanthropology.** The `Behavioural Firsts` thresholds, the twelve
  hominin taxa, the lithic industries, and the site-level coverage of Africa (271 entities)
  are the strongest part of the dataset by a wide margin. Nothing significant is missing here.
- **Archaeogenetics and migration in prehistory.** `The Steppe Ancestry Influx`,
  `The Rakhigarhi Genome`, `The Anatolian Farmer Turnover`, `The Two Routes of Neolithic
  Spread`, `Arrival of Steppe Ancestry in South Asia`, `The Austronesian Expansion` — this is
  current, well-chosen, and unusually good. The failure is that this modern, process-oriented
  approach was applied only before 3000 BC.

---

## The five worst

1. **Religion as a category.** Zero religions in 1,765 entities. Buddhism, Christianity,
   Hinduism, Zoroastrianism, Judaism-as-religion, Confucianism, Daoism, and the Sunni–Shia
   split are all absent, and the `Axial Age [era] 800BC..200BC` node sits empty waiting for
   them. This distorts more of the dataset than anything else, because it silently removes
   the stated motive of most premodern political action.
2. **Trade networks and the Atlantic slave trade.** No Silk Road, no Indian Ocean trade, no
   trans-Saharan trade, no Hanse, and above all no Atlantic slave trade — in a dataset that
   nonetheless includes two Dutch West India Companies and the Berlin Conference. The
   economic engine of every empire listed is invisible.
3. **Technology after 1650 BC.** Thresholds stop at the domestic chicken. No iron, alphabet,
   paper, printing, gunpowder, compass, zero, steam engine, vaccination, electricity, or
   transistor; `Industrial Revolution` and `Second Industrial Revolution` are childless
   labels. The dataset cannot answer "when did X get invented" for any historical X.
4. **Epidemic disease.** Two disease entities in all of history. No Plague of Justinian, no
   Antonine Plague, no 1918 influenza, and no Columbian die-off — despite an empty
   `The Columbian Exchange [era] 1492..1700` node that exists for precisely that purpose.
   Readers get a purely political explanation for the three largest population collapses on
   record.
5. **Law and governance concepts, including the imperial examination system.** Hammurabi
   without his code, Justinian without the Corpus, England without Magna Carta or common law,
   China without keju, and a childless `Decolonization [era] 1945..1997`. The dataset lists
   690 rulers and never explains how any of them ruled.

**Cross-cutting recommendation:** all five need new thematic branches under `Global &
Multi-Regional [region]`, which is currently 50% palaeoanthropology and 50% periodisation
scaffold. It is the right home structurally — the periodisation eras (`Bronze Age` through
`Contemporary`) are natural parents — but it needs five new intermediate nodes
(`Disease & Demography`, `Climate & Environment`, `Religions & Religious Movements`,
`Technological Thresholds`, `Trade, Labour & Economic Systems`, plus `Law & Governance`,
`Migrations & Language Spreads`, `Intellectual & Artistic Movements`) before any of this is
authorable. Two of the existing `kind` values also need widening: `threshold` currently means
"palaeoanthropological first" and needs to mean "technological or institutional first" through
to the present, and `event` needs to stop meaning "battle".
