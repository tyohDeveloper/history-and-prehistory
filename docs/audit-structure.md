# Audit: structure and bias

Source: `/home/user/workspace/hp/docs/inventory.txt` (1,765 entities). No web search used;
all absences verified by grep against the inventory, all quotes taken from it verbatim.

## Numbers this audit rests on

From the inventory's own tallies and from parsing the tree:

- Kinds: `reign: 690` (39.1%), `period: 602`, `era: 350`, `event: 43`, `region: 42`,
  `threshold: 26`, `taxon: 12`. **43 events in 1,765 entities.**
- Reigns by top-level region: East Asia 182, South Asia 159, Europe 155, Africa 152,
  West Asia 19, Americas 8, Central Asia & the Steppe 7, Global & Multi-Regional 3,
  Southeast Asia 3, **Oceania 2**.
- Africa: 272 entities, of which the `Ancient Egypt` subtree alone is 189 (69%).
  Of Africa's 152 reigns, 143 are Egyptian. The whole rest of the continent has **six**
  named rulers: Hannibal, Shaka, Sundiata Keita, Mansa Musa, Sunni Ali, Askia Muhammad I
  (plus Ezana, Menelik II, Haile Selassie in the Nile Valley branch).
- `Africa > Central Africa`: 4 entities, 0 reigns. `Africa > East Africa`: 3 entities, 0 reigns.
- Japan: 312 entities, of which **256 are `period` nodes that are nengō era-names**
  (`Tenpyō-jingo [period] 765..767`, `Eiso [period] 989..990`, …). 42 reigns, all shoguns
  and shogunal regents. Zero emperors.
- Female reigns: **~26 of 690 (3.8%)**.
- 290 of 1,723 dated start years are multiples of 50; `3000BC` appears as a start 12 times,
  `1500BC` 10, `1200BC` 10, `3300BC` 10.
- `Global & Multi-Regional`: 114 entities.

---

# HALF ONE — Structural defects

### Egypt stops in 641 CE and never restarts
**Severity:** high
**What is missing:** the last child of `Ancient Egypt` is `Roman & Byzantine Egypt [era] 30BC..641 (inte)` — and it is **empty**. After it, Egypt does not exist. Missing: the Arab conquest of Egypt (639–641), Fustat, the Tulunids (868–905), the Ikhshidids, Fatimid Cairo (the `Fatimid Caliphate [era] 909..1171` exists but is filed under `Global & Multi-Regional > Multi-Regional Empires`, not under Egypt), Saladin and the Ayyubids (1171–1250), the **Mamluk Sultanate of Egypt (1250–1517)** with Baybars and Qutuz and Ain Jalut, Ottoman Egypt, Muhammad Ali Pasha (1805–1848), the Suez Canal, the British occupation from 1882, the Khedivate, and the Republic from 1952.
**Where it belongs:** `Africa > Nile Valley & Northeast Africa`, as siblings of `Ancient Egypt [era] 6000BC..641 (foun)`.
**Why it matters:** the dataset gives 143 named pharaohs and then treats the following fourteen centuries — during which Cairo was for long stretches the largest city in the world — as nothing. A reader concludes Egyptian history is a story about pyramids that ended when Rome fell.
**Rough dates:** 641–present.

### Mesopotamia and the Levant end in 539 BC
**Severity:** high
**What is missing:** `West Asia > Mesopotamia & Levant` terminates at `Neo-Babylonian Empire [era] 626BC..539BC` with `Nebuchadnezzar II [reign] 605BC..562BC`. Nothing after. Missing: Seleucid Babylonia, Hatra and Palmyra (and Zenobia — grep returns 0), Ctesiphon, the Rashidun conquest of Iraq, **Abbasid Baghdad as a place rather than a caliphate**, the Mongol sack of 1258, Ottoman Iraq and Syria, the Mandate period, and every modern state: Iraq, Syria, Lebanon, Jordan, Israel, Palestine.
**Where it belongs:** `West Asia > Mesopotamia & Levant [region] —..—`.
**Why it matters:** combined with the Egypt hole, the dataset's West Asia consists of 113 entities that almost all predate 500 BC. West Asia has 19 reigns; Ancient Rome alone has 100.
**Rough dates:** 539 BC – present.

### Anatolia ends in 546 BC, and the Ottomans are not reachable from West Asia
**Severity:** high
**What is missing:** `West Asia > Anatolia` runs `Troy`, `The Hittites`, `Mitanni`, `Neo-Hittite States`, `Phrygia`, `Urartu`, `Lydia [era] 680BC..546BC` — and stops. There is no Achaemenid Anatolia, no Hellenistic Anatolia, no Roman Asia Minor, no Armenian kingdoms, no **Seljuks of Rum**, no Byzantine Anatolia (Byzantium is filed under `Europe > Mediterranean`), no beyliks, no Ottoman Anatolia, no Republic of Türkiye, no Atatürk. The `Ottoman Empire [era] 1299..1922` sits in `Global & Multi-Regional > Multi-Regional Empires`.
**Where it belongs:** `West Asia > Anatolia [region] —..—`.
**Why it matters:** the tree makes a claim it cannot defend — that the Ottoman Empire was not an Anatolian or West Asian polity but a floating "multi-regional" one, while Rome, whose reach was comparably multi-regional, gets a full home under Europe. The asymmetry is the finding.
**Rough dates:** 546 BC – present.

### The Atlantic slave trade does not exist in the dataset
**Severity:** high
**What is missing:** `grep -i slave` returns exactly one hit: `Mamluk (Slave) Dynasty [period] 1206..1290`. There is no Atlantic slave trade, no Middle Passage, no plantation complex, no abolition. Yet every participant is present as an entity: `Kingdom of Dahomey [era] 1600..1904`, `Ashanti Empire [era] 1670..1902`, `Oyo Empire [era] 1400..1836`, `Benin Empire [era] 1180..1897`, `Kingdom of Kongo [era] 1390..1914`, `Portuguese Empire [era] 1415..1999`, `Dutch West India Company [era] 1621..1674`, `Spanish Empire`, `The British Empire`, `Viceroyalty of New Spain`. Also absent: the **Haitian Revolution** (grep "Haiti": 0), Palmares and the quilombos (0), the Jamaican Maroons (0), and **Brazil in any form whatsoever** (grep "Brazil": 0) — the single largest destination of enslaved Africans is not in the tree.
**Where it belongs:** `Global & Multi-Regional > Multi-Regional Empires` alongside `The Columbian Exchange [era] 1492..1700` and `Age of Exploration / Age of Sail [era] 1418..1815`; the Haitian Revolution under `Americas > Intermediate Area & Caribbean [region] —..—`, which currently holds one entity, `Taíno Chiefdoms [era] 1200..1500`.
**Why it matters:** the tree lists the ships (`Dutch West India Company`), the ports (`Ashanti`, `Dahomey`), and the destinations (`Viceroyalty of New Spain`) while omitting the cargo and the twelve million people. A reader assembles the Atlantic world with a hole where its organising economy was.
**Rough dates:** 1440s–1888.

### Empty containers where the ruler list is standard
**Severity:** high
The tree has 190+ leaf `era`/`period` nodes. Most are legitimately leaf-shaped. These are not — the dataset lists rulers densely elsewhere, and the king-lists here are textbook:

- `Global & Multi-Regional > Multi-Regional Empires > Ottoman Empire` has 2 reigns for 36 sultans across 623 years (12% span coverage). **Osman I is absent** (grep "Osman": 0), as are Orhan, Murad I, Bayezid I, Mehmed I, Selim I, Selim III, Mahmud II, Abdulhamid II, Mehmed VI.
- `Europe > Central Europe > Holy Roman Empire > Ottonian Dynasty [period] 919..1024` — empty. **Otto I is absent** (grep: 0).
- `... > Hohenstaufen Dynasty [period] 1138..1254` — empty. Frederick Barbarossa absent (grep: 0), Frederick II absent.
- The **Salian dynasty is missing entirely**, leaving an unexplained gap of 114 years inside the Holy Roman Empire between `Ottonian Dynasty …1024` and `Hohenstaufen Dynasty 1138…`: no Henry IV, no Investiture Controversy, no Canossa.
- `Europe > Western Europe > England > Plantagenet England [period] 1154..1485` — empty. No Henry II, Richard I, John, Magna Carta (grep: 0), Edward I, Edward III, Hundred Years' War, Wars of the Roses.
- `... > Stuart England / Britain [period] 1603..1714` — empty. No James I, Charles I, English Civil War, **Cromwell** (grep: 0), Glorious Revolution.
- `Europe > Western Europe > France > Capetian France [period] 987..1328` and `Valois France [period] 1328..1589` — both empty. No Philip Augustus, Louis IX, Philip IV, Joan of Arc, Francis I, Catherine de' Medici. `Bourbon France [period] 1589..1792` has one reign, `Louis XIV`; Louis XVI is absent although `French Revolution [period] 1789..1799` is present.
- `Europe > Central Europe`: `The Habsburg Monarchy`, `Rise of Prussia`, `German Empire`, `Weimar Republic`, `Nazi Germany`, `Post-War Germany` — **all six empty**. No Maria Theresa, no Frederick the Great, no Bismarck (grep: 1 hit, and it is `Berlin Conference`'s sibling text, not an entity), no Wilhelm II, **no Hitler** (grep: 0), no Adenauer.
- `Europe > Eastern Europe`: `Grand Duchy of Moscow 1263..1547` empty (no Ivan III); `Polish-Lithuanian Commonwealth 1569..1795` empty (no Jagiellonians, no Sobieski, no Partitions).
- `West Asia > Iran`: `Seleucid Empire` empty (no Seleucus I, no Antiochus III); `Median Empire` empty; `Qajar Dynasty 1794..1925` empty; `Pahlavi Dynasty 1925..1979` empty (no Reza Shah); `Islamic Republic of Iran 1979..—` empty (no Khomeini). `Safavid Empire 1501..1736` has one reign, `Abbas I the Great` — **the founder Ismail I is absent.**
- `Southeast Asia > Mainland Southeast Asia > Vietnam (dynastic)` has ten dynasty `period` children — `Lý Dynasty 1009..1225`, `Trần Dynasty 1225..1400`, `Later Lê Dynasty 1428..1789`, `Nguyễn Dynasty 1802..1945` — and **not one ruler**. All of Southeast Asia has 3 reigns. No Lê Lợi, no Gia Long, no Trần Hưng Đạo, no Trưng sisters.
- `Africa > Central Africa > Kingdom of Kongo 1390..1914` — empty, though its king-list is among the best-documented in Africa (Nzinga a Nkuwu/João I, Afonso I, Garcia II). `Luba Empire`, `Lunda Empire`, `Swahili Coast City-States`, `Sultanate of Zanzibar`, `Great Zimbabwe`, `Mutapa Empire`, `Ghana Empire`, `Kanem–Bornu Empire`, `Benin Empire`, `Oyo Empire`, `Kingdom of Dahomey`, `Ashanti Empire`, `Sokoto Caliphate`, `Almoravid Empire`, `Almohad Caliphate`, `Alaouite Morocco` — all empty. Absent by name: Idris Alooma, Ewuare, Osei Tutu, Usman dan Fodio, Yusuf ibn Tashfin, Nzinga of Ndongo-Matamba, Amina of Zazzau.
- `Americas`: `Toltec Empire`, `Purépecha Empire`, `Chimú (Chimor)`, `Wari Empire`, `Tiwanaku`, `Moche`, `Comanche Empire`, `Haudenosaunee Confederacy`, `Mapuche / Araucanía` — all empty. The Americas' entire reign budget is 8.
- `East Asia > China > Shang Dynasty 1600BC..1046BC` empty (no Wu Ding, no Di Xin), `Three Kingdoms`, `Jin Dynasty`, `Northern and Southern Dynasties`, `Five Dynasties and Ten Kingdoms`, `Liao Dynasty`, `Western Xia`, `Jin Dynasty (Jurchen)`, `Republic of China`, `People's Republic of China` — all empty. **China's 20th century contains zero people**: no Sun Yat-sen, no Chiang Kai-shek, no Mao, no Deng, and no events — no Long March, no Cultural Revolution, no Tiananmen. Also absent: Taiping Rebellion, Opium Wars, Boxer Uprising (grep: 0 each).

**Why it matters:** the pattern is not random. Reigns cluster where a canonical numbered king-list exists (Egypt's dynasties, Rome's emperors, China's pre-1912 emperors, India's dynasties). Where a polity's leadership must be researched rather than copied from a list, the container is left empty. The reader sees a world in which some societies had rulers and others had only names.

### Egyptian dynasties 7–10, 14, 16, 17, 23 and 24 are missing
**Severity:** high
**What is missing:** the tree runs `1st`, `2nd`, `3rd`, `4th`, `5th`, `6th`, then `First Intermediate Period [era] 2181BC..2055BC` **empty** (dynasties 7–10, the Herakleopolitans, Merikare, the Instruction texts), then `11th Dynasty (reunified)`, `12th`, `13th Dynasty [period] 1773BC..1650BC` **empty** (Sobekhotep, Neferhotep), then `Second Intermediate Period` containing only `15th Dynasty — Hyksos`. **There is no 17th Dynasty** (grep: 0): no Seqenenre Tao, no Kamose. Then `22nd Dynasty (Libyan/Bubastite) 945BC..720BC` jumps straight to `25th Dynasty — Kushite` — the 23rd and 24th are absent (grep "23rd": 0).
**Where it belongs:** `Ancient Egypt > Second Intermediate Period [era] 1650BC..1550BC` etc.
**Why it matters:** with no 17th Dynasty, the tree shows the Hyksos ruling unopposed for a century and then `Ahmose I [reign] 1550BC..1525BC` appearing from nowhere. The Theban war of liberation — the founding event of the New Kingdom — has no place to sit. Similarly, the First Intermediate Period as an empty box turns Egypt's first state collapse into a blank.
**Rough dates:** 2181–2055 BC; 1773–1550 BC; 837–720 BC.

### Artaxerxes I and III exist only as Egyptian pharaohs
**Severity:** high
**What is missing:** `Achaemenid Empire [era] 550BC..330BC` lists five kings: `Cyrus II the Great`, `Cambyses II`, `Darius I the Great`, `Xerxes I`, then a **129-year gap** to `Darius III [reign] 336BC..330BC`. Bardiya, Artaxerxes I, Xerxes II, Darius II, Artaxerxes II, Artaxerxes III and Artaxerxes IV are all absent from Iran. But `Artaxerxes I (as pharaoh) [reign] 465BC..424BC` and `Artaxerxes III (as pharaoh) [reign] 343BC..338BC` both exist — under `Ancient Egypt > Late Period > 27th Dynasty — First Persian` and `31st Dynasty (Second Persian)`.
**Where it belongs:** `West Asia > Iran > Achaemenid Empire`.
**Why it matters:** the tree asserts, structurally, that Artaxerxes I was a ruler of Egypt and not of Persia. It also loses the Achaemenid century that contains the Greco-Persian Wars from the Persian side, the satrapal revolts, and the Peace of Callias. This is the clearest case of a child under the wrong parent making a false claim.
**Rough dates:** 465–338 BC.

### Iran has a 319-year hole because Mongol and Timurid Iran are filed in Central Asia
**Severity:** high
**What is missing:** `West Asia > Iran` runs `The Iranian Intermezzo [era] 821..1055` and then jumps to `Qara Qoyunlu [era] 1374..1468`. Missing from Iran: the Great Seljuks, the Khwarazmians, the Mongol invasion of 1219–1221, the **Ilkhanate**, the Injuids and Muzaffarids, and **Timur**. Every one of these entities exists — `Seljuk Empire [era] 1037..1194`, `Khwarazmian Empire [era] 1077..1231`, `Ilkhanate [period] 1256..1335`, `Timurid Empire [era] 1370..1507` — all under `Central Asia & the Steppe`.
**Where it belongs:** `West Asia > Iran`, or cross-filed.
**Why it matters:** the reader scanning Iran's column sees three centuries of nothing between the Buyids and the Turkmen confederations, i.e. exactly the period of Iran's Persianate literary flowering, Nizami and Hafez, and the Mongol catastrophe.
**Rough dates:** 1055–1374.

### Byzantium: no reigns for its first 161 years, no dynasties, no Amorians, no Latin Empire
**Severity:** medium-high
**What is missing:** `Byzantine Empire [era] 330..1453` has 39 reigns but the first is `Anastasius I [reign] 491..518` — nothing between 330 and 491 (Constantius II through Zeno are either filed under Rome or absent: Leo I, Zeno, Basiliscus have no entry). Then a **65-year gap** `Irene of Athens …802 → Basil I 867…`: the entire Amorian dynasty and second iconoclasm — Nikephoros I, Michael I, Leo V, Michael II, Theophilos, Michael III — is absent. A **43-year gap** `Basil II …1025 → Romanos IV 1068…` removes Zoe and Theodora Porphyrogenita, Constantine IX and the schism of 1054. The **57-year gap** `Alexios IV …1204 → Michael VIII 1261…` has no Fourth Crusade, no Latin Empire, no Empire of Nicaea. And unlike Rome, Byzantium has **no dynasty-level `period` layer at all** — no Macedonian, Komnenian or Palaiologan grouping — so 39 emperors sit in one flat list.
**Where it belongs:** `Europe > Mediterranean > Byzantine Empire [era] 330..1453`.
**Why it matters:** Rome gets `Julio-Claudian Dynasty`, `Flavian Dynasty`, `Severan Dynasty`, `Nerva–Antonine Dynasty` and so on; Byzantium, its direct continuation in the same region of the same tree, gets none. The same class of thing is filed at two depths within one branch.

### Inconsistent filing depth: a king sits at depth 2 in India and depth 5 in Egypt
**Severity:** medium-high
Measured depths of `reign` nodes by region:

| Region | reign depths |
|---|---|
| South Asia | **111 at depth 2**, 45 at depth 3, 3 at depth 1 |
| West Asia | 18 at depth 3 |
| East Asia | 137 at depth 3, 45 at depth 4 |
| Europe | 81 at depth 5, 45 at depth 3, 27 at depth 4, 2 at depth 2 |
| Africa | **125 at depth 5**, 18 at depth 4, 9 at depth 3 |

The four cases the brief asks about:

- **Egypt:** `Africa > Nile Valley & Northeast Africa > Ancient Egypt > New Kingdom > 18th Dynasty > Hatshepsut` — region → region → era → era → period → reign. Depth 5.
- **China:** `East Asia > China > Tang Dynasty > Empress Wu Zetian` — depth 3; but `East Asia > China > Han Dynasty > Western Han > Emperor Wu` is depth 4. Inconsistent within one country.
- **England:** `Europe > Western Europe > England (Medieval to Modern) > Tudor England > Henry VIII` — depth 4, with only 4 reigns in the whole English subtree of 10 entities.
- **Persia:** `West Asia > Iran > Achaemenid Empire > Cyrus II the Great` — depth 3, and Iran has **no dynasty-period layer whatsoever**: `Safavid Empire`, `Qajar Dynasty`, `Pahlavi Dynasty` are all `[era]` hanging directly off the region, siblings of `Elam [era] 3200BC..539BC`.

**Why it matters:** depth reads as significance and as internal articulation. Egypt appears to have five levels of structure and India two, purely as an artefact of who authored which branch. Any tool that renders this tree by depth, or truncates it, will silently amputate different things in different regions.

### Suspicious uniformity: two date-conversion offsets and heavy round-number placeholders
**Severity:** medium
**What is wrong:** 145 start years end in `51` — `3298051BC`, `2598051BC`, `298051BC`, `18051BC` — which is a Before-Present-to-BC conversion using a 1951 epoch. But three entities use a **1950 epoch instead**: `Turkana Basin [period] 4098050BC..738051BC`, `Sterkfontein [period] 3668051BC..2068050BC`, `Olduvai Gorge [period] 2036050BC..798051BC` — note that `Sterkfontein` and `Olduvai Gorge` each mix both offsets *within a single entity*. Separately, 290 of 1,723 dated starts are multiples of 50, and specific values repeat far beyond coincidence: `3000BC` starts 12 entities, `1500BC` 10, `1200BC` 10, `3300BC` 10, `1650BC` 7.
**Why it matters:** `4098050BC` implies year-level precision on a four-million-year-old date, and the mixed offsets mean any arithmetic on these dates is off by one year in an inconsistent subset. The clustering on `1200BC` is worse than cosmetic: it is the Bronze-Age-collapse date being reused as a default (`Iron Age 1200BC`, `Late Bronze Age Collapse 1200BC`, `Neo-Hittite States 1180BC`, `Arwad 1200BC`, `Sidon 1200BC`, `Tyre 1200BC`, `Phoenician Independence 1200BC`, `Domestication of the Dromedary 1200BC`), so a reader sees a spurious global synchrony that is really one placeholder.

### 70+ entities whose dates contradict their parent's
**Severity:** medium
Verified programmatically. Not all are errors — Japanese nengō legitimately straddle reign boundaries, and `Kublai Khan [reign] 1260..1294` under `Yuan Dynasty [era] 1271..1370` reflects real history. But these are defects:

- `African Prehistory [era] 3298051BC..3000BC` has children starting **800,000 years before it** (`Turkana Basin 4098050BC`) and ending **3,000 years after it** (`Nok Culture 1500BC..1BC`, `Bantu Homeland Phase …2051BC`, `Gobero …2851BC`).
- `Phoenician City-States [era] 1500BC..332BC` contains `Byblos [era] 3000BC..332BC` — the child predates the parent by 1,500 years.
- `Elam [era] 3200BC..539BC` contains `Susa [period] 4200BC..539BC` (1,000 years early) and `Middle Elamite Period [era] 1450BC..1050BC` contains `Chogha Zanbil [period] 1250BC..640BC` (410 years late).
- `West Asian Prehistory [era] 13000BC..3800BC` contains `Epipalaeolithic (Levant) [era] 23000BC..10000BC` — 10,000 years early — and three Chalcolithic children ending up to 700 years after the parent.
- `Mongol Empire [era] 1206..1368` contains `Chagatai Khanate [period] 1226..1687` and `Golden Horde [period] 1242..1502`, i.e. children outliving the parent by 319 and 134 years.
- `Aboriginal Australia [era] 65000BC..—` contains `Sahul [period] 73051BC..10051BC`.
- `Post-Independence South Asia [era] 1947..—` contains `Mahatma Gandhi [reign] 1915..1948`, `Muhammad Ali Jinnah [reign] 1913..1948`, `Subhas Chandra Bose [reign] 1938..1945` — three men whose entire significance is pre-independence, filed under independence.
- `Nabta Playa [period] 8851BC..4251BC` contains `Nabta Terminal Neolithic [period] 4651BC..3451BC`.
- `Achaemenid Empire [era] 550BC..330BC` starts nine years after its own founder, `Cyrus II the Great [reign] 559BC..530BC`.
- `Rashtrakuta Dynasty [era] 753..982` starts 18 years after its founder `Dantidurga [reign] 735..756`.

### Date discontinuities inside parents
**Severity:** medium
- `Kingdom of Kush [era] 2500BC..350`: `Kerma Phase …1500BC` → `Napatan Phase 1070BC…`. A **430-year gap** that is precisely the Egyptian New Kingdom occupation of Nubia — the viceroys of Kush, Napata's founding, the temple at Jebel Barkal. Nothing marks it.
- `Joseon Dynasty [era] 1392..1897`: 8 reigns for 505 years (45% coverage), with gaps `1506→1567` (61 years: the Imjin War's antecedents, the four literati purges), `1608→1724` (**116 years**: no Gwanghaegun, no Injo, no Manchu invasions, no Sukjong), `1800→1864` (64 years).
- `Goryeo Dynasty [era] 918..1392`: `Seongjong …997` → `Chungnyeol 1274…`, a **277-year gap** containing the Khitan wars, the Mongol invasions, the Tripitaka Koreana and the entire Choe military dictatorship.
- `Sasanian Empire [era] 224..651`: `Shapur I …270` → `Khosrow I 531…`, a **261-year gap** — no Shapur II, no Yazdegerd, no Kavad, no Peroz, no Mazdakite revolt.
- `Satavahana Empire [era] 230BC..220`: `Satakarni I …170BC` → `Gautamiputra Satakarni 78…`, a **248-year gap**.
- `Russian Empire [era] 1721..1917`: two reigns, Peter and Catherine (19% coverage). No Elizabeth, Paul I, Alexander I and 1812, Nicholas I, Alexander II and emancipation, Nicholas II.
- `Roman Republic [period] 509BC..27BC`: 482 years, 11 reigns, 26% coverage; `Scipio Africanus …201BC` → `Tiberius Gracchus 133BC…`. `Early Republic [period] 509BC..287BC` is empty — no Twelve Tables, no Conflict of the Orders, no Samnite Wars.
- `Kingdom of Hawaii [era] 1795..1898`: `Kamehameha I …1819` → `Queen Liliʻuokalani 1891…`, a 72-year gap skipping Kamehameha II–V, Kaʻahumanu, Lunalilo, Kalākaua, and the 1893 overthrow.
- `South Asia` itself: `Guru Nanak [reign] 1469..1539` → `Rabindranath Tagore [reign] 1878..1941`, a 339-year gap between two region-level `reign` children who are not rulers at all.

### Successions with holes
**Severity:** medium
- `Aztec Empire [era] 1428..1521`: `Itzcoatl`, `Moctezuma I`, `Ahuitzotl`, `Moctezuma II`. Skips **Axayacatl and Tizoc** between 1469 and 1486, and omits the two tlatoque of the conquest, Cuitláhuac and **Cuauhtémoc** (grep: 0) — so the empire simply stops after Moctezuma II.
- `Inca Empire [era] 1438..1533`: `Pachacuti`, `Topa Inca Yupanqui`, `Huayna Capac`, `Atahualpa`. **Huáscar is absent** (grep: 0), so the civil war that made the Spanish conquest possible is invisible, as is the whole pre-Pachacuti dynasty.
- `Chola Empire [era] 848..1279`: `Kulottunga I …1120` → `Kulottunga III 1178…` skips Vikrama Chola and Kulottunga II; `Aditya I`, `Parantaka I`, then a jump to `Rajaraja I 985` omitting Sundara Chola and Uttama Chola.
- `Indo-Greek Kingdoms [era] 200BC..10`: four kings — `Demetrius I`, `Menander I`, `Apollodotus II`, `Strato II` — out of roughly thirty attested; Eucratides, Antialcidas and Heliocles absent.
- `Pallava Dynasty [era] 275..897`: three kings for 622 years (21%), all clustered 600–796; nothing for the first three centuries or the last century.
- `Kingdoms of Israel and Judah [era] 1050BC..586BC`: two reigns, `David` and `Solomon`, for 464 years. No division of the kingdom in 931 BC, no Jeroboam, Omri, Ahab, Jehu, **Athaliah**, Hezekiah, Josiah; no fall of Samaria in 722 BC, no Babylonian exile. Also: merging Israel and Judah into one entity is itself a contested claim the tree makes silently.
- `2nd Dynasty` (Egypt): `Nynetjer …2780BC` → `Peribsen 2740BC…` skips Weneg, Senedj and Sekhemib.

### False claims the tree makes by shape
**Severity:** medium
- `Africa > North Africa > Carthaginian Empire [era] 814BC..146BC` has exactly one child: `Hannibal Barca (general) [reign] 221BC..183BC`. Carthage was an oligarchic republic governed by elected shophets and a council; the tree renders it as a monarchy with a single king. Dido/Elissa, Hamilcar Barca, Hasdrubal and Hanno the Navigator are all absent.
- `Kingdom of Macedon [period] 700BC..146BC` is a **sibling** of `Ancient Greece [era] 3200BC..146BC`, not a child of it, while `Classical Greece` is inside Greece. The tree takes a position on whether Macedon was Greek — one of the most politically loaded questions in the field — without saying so.
- `Europe > Western Europe > The Netherlands [reign] 1581..—` — a republic (and later kingdom) filed with `kind = reign`, its children being `Dutch East India Company` and two West India Companies. The schema has no kind for "state", so a country becomes a reign.
- `Yuan Dynasty [era] 1271..1370` under China, `Mongol Empire [era] 1206..1368` under Central Asia, with `Kublai Khan` under the former: the tree splits one polity in two and gives no relation between them.
- `Global & Multi-Regional > Multi-Regional Empires [era] 550BC..1997` — an "era" running 2,547 years whose children are five caliphates/empires plus `Age of Exploration`, `Columbus reaches the Americas`, `Scramble for Africa` and `Decolonization`. The 550 BC start is the Achaemenid founding date, but no Achaemenid entity is inside it.
- `Prophet Muhammad [reign] 610..632`, `Martin Luther (theologian) [reign] 1517..1546`, `Guru Nanak [reign] 1469..1539`, `Kabir [reign] 1440..1518`, `Pericles (statesman) [reign] 461BC..429BC`, `Rabindranath Tagore [reign] 1878..1941`, `Mahatma Gandhi [reign] 1915..1948`, plus **fourteen** British governors-general and viceroys — all `kind = reign`. The dataset's only container for a person is a reign, so every prophet, poet and colonial administrator is rendered as a monarch.

### Ancient Greece and the Hellenistic world are near-empty
**Severity:** medium
**What is missing:** `Archaic Greece [period] 800BC..480BC` — empty (no Solon, Cleisthenes, Lycurgus, colonisation, Homer). `Classical Greece [period] 480BC..323BC` — one child, `Pericles (statesman)`. `Hellenistic Period [era] 323BC..31BC` — empty. Absent: Sparta and Athens as entities, the Persian Wars, Marathon, Salamis, the Delian League, the Peloponnesian War, Socrates/Plato/Aristotle, Thebes, the Diadochi, Antigonid Macedon, Pergamon, the Library of Alexandria, Archimedes.
**Where it belongs:** `Europe > Mediterranean > Ancient Greece [era] 3200BC..146BC`.
**Why it matters:** the branch of the tree carrying the most cultural weight in the dataset's own framing (`Classical Antiquity`, `Axial Age` both exist as global eras) has almost nothing in it, while `Ancient Rome` next door has 100 reigns. The dataset venerates the Classical and then does not describe it.

---

# HALF TWO — Bias and framing

### European periodisation installed as the global spine
**Severity:** high
`Global & Multi-Regional` holds the dataset's chronological skeleton, and it is Europe's:

```
Bronze Age [era] 3300BC..1200BC
  Early Bronze Age [period] 3300BC..2100BC
  Middle Bronze Age [period] 2100BC..1550BC
  Late Bronze Age [period] 1550BC..1200BC
  Late Bronze Age Collapse [event] 1200BC..1150BC
Iron Age [era] 1200BC..550BC
Classical Antiquity [era] 800BC..500
  Axial Age [era] 800BC..200BC
Late Antiquity [era] 250..750
Middle Ages [era] 500..1500
  Black Death [event] 1346..1353
Early Modern [era] 1500..1800
Long 19th Century [era] 1789..1914
Short 20th Century [era] 1914..1991
```

Specific distortions:

- **`Iron Age [era] 1200BC..550BC` is empty and its bounds are Near Eastern.** Sub-Saharan Africa had no Bronze Age at all — iron and copper arrive together — so `Nok Culture [period] 1500BC..1BC`, one of the earliest iron-working traditions anywhere, is filed under `African Prehistory` instead, with an end date of `1BC` inside a parent that ends `3000BC`. The Americas and Oceania never had an Iron Age; Japan's sequence runs `Jōmon Period → Yayoi Period [era] 300BC..300`, where bronze and iron arrive simultaneously; South Asian iron predates 1200 BC at Malhar and Raja Nala ka Tila. The `550BC` end date is the Achaemenid founding — a Persian political event closing a technological era for the whole planet.
- **`Middle Ages [era] 500..1500`**, whose only child is `Black Death`, sits above nothing and beside everything. There is no "middle" in the Chinese sequence — the Tang and Song fall inside it and are the high point, not a trough. The Islamic translation movement, Abbasid Baghdad and al-Andalus fall in it and are not "middle" anything. `Late Antiquity [era] 250..750` overlaps it by 250 years with no explanation of the relation.
- **`Long 19th Century [era] 1789..1914`** takes the French Revolution as the hinge of world history; **`Short 20th Century [era] 1914..1991`** takes Sarajevo and the Soviet collapse. Both are Hobsbawm's frames for Europe, presented as global containers.
- **`BCE (Before Common Era) [era] 3500BC..1BC` and `CE (Common Era) [era] 1..—` are filed as historical eras.** A calendar convention is not a period. And beginning "BCE" at 3500 BC — the dataset's own `Writing [threshold] 3400BC` — encodes the claim that history starts with literate Mesopotamia; everything before is `Human Prehistory`, including Australia's continuous 65,000 years.
- **Three-age vocabulary replicated regionally**: `Chalcolithic (South Asia) [era] 3000BC..700BC`, `Chalcolithic (Anatolia) 5500BC..3000BC`, `Chalcolithic (Southern Levant)`, `Chalcolithic (Southeast Europe)`, `Late Chalcolithic (Mesopotamia)`. And `Greek Dark Ages [period] 1100BC..800BC` retains a label the field has largely abandoned.

**Why it matters:** the reader who navigates by these eras is navigating Europe's clock. Every non-European sequence must be translated into it, and the translation costs are invisible in the tree.

### Great-man bias: 690 reigns and 43 events
**Severity:** high
39% of the dataset is individual rulers; 2.4% is events. The consequences are systematic, not incidental:

- **No trade networks.** grep returns 0 for "Silk Road", 0 for "Indian Ocean", 0 for "Trans-Saharan", 0 for "Hanseatic", 0 for "Venice", 0 for "Genoa", 0 for "Guild", 0 for "Merchant". The dataset has `The Incense Route [period] 700BC..200` and `Qhapaq Ñan [period] 1438..1533` and `Bismarck Obsidian Network [period] 18051BC..1051BC` — so it *can* hold networks; it simply holds almost none. The three largest exchange systems in premodern history are absent.
- **No institutions.** 0 hits for "Parliament", "Assembly", "Council", "Democracy", "Law", "Constitution" as entities. `Hammurabi [reign] 1792BC..1750BC` exists; his code does not. `Magna Carta` does not exist. The Athenian democracy does not exist.
- **No stateless or non-monarchical societies with internal history.** Only two entities contain "Confederacy": `Maratha Confederacy` (which has 5 reigns and a `Peshwa Era`) and `Haudenosaunee Confederacy [era] 1450..—`, which is **empty** — because the schema's only person-kind is `reign`, and the Great Law of Peace produced no kings. Nothing represents the Gayanashagowa, the clan mothers, the Grand Council at Onondaga, or the League's role in 17th-century geopolitics.
- **Pastoralists appear only when they conquered someone.** `Scythians [era] 900BC..200BC` — empty. `Saka [era] 600BC..100BC` — empty. `Xiongnu Empire [era] 209BC..93` — one reign, `Modu Chanyu`. `First Turkic Khaganate`, `Second Turkic Khaganate`, `Uyghur Khaganate` — all empty. The Eurasian Steppe region has 0 reigns beyond Modu. Absent entirely: the Tuareg, the Fulani beyond `Sokoto Caliphate`, the Bedouin, the Kazakh zhuz, the Nenets, the Mongol pastoral economy as distinct from the Mongol conquest.
- **Hunter-gatherers exist only as prehistory sites.** `Klasies River Mouth`, `Blombos Cave`, `Apollo 11 Cave` are `period` nodes dated to tens of thousands of years BC. The San and Khoikhoi as *historical* peoples with an internal past into the colonial period — absent. The **Ainu** — absent (grep: 0). The **Sámi** — absent (0). **Inuit and Thule** — absent (0). The Andamanese — absent.
- **Maritime networks under-represented.** `The Austronesian Expansion [era] 3551BC..1130BC` and `Polynesian Voyaging & Settlement [era] 1025..1290` are present and good. But the Bugis and Makassar maritime world — absent (0). The Batak, the Sama-Bajau — absent. The Swahili coast is one empty node, `Swahili Coast City-States [era] 900..1500`, with no Kilwa, Mombasa, Pate, Lamu or Sofala (grep: 0 each) despite the Kilwa Chronicle.

**Why it matters:** a reader learns that history is what kings did. Societies organised without kings are either absent or present as an empty box, which reads as "nothing happened here."

### Women: 26 of 690 reigns (3.8%)
**Severity:** high
The 26: Merneith, Nitocris, Sobekneferu, Hatshepsut, Neferneferuaten, Tausret, Cleopatra III, Berenice III, Cleopatra VII, Empress Dowager Lü, Wu Zetian, Cixi, Catherine the Great, Irene of Athens, Elizabeth I, Victoria, Liliʻuokalani, Rudrama Devi, Razia Sultana, Tarabai, Benazir Bhutto (×2), Indira Gandhi (×2), Sheikh Hasina (×2). Nine of the 26 are Egyptian; six are South Asian politicians of the last 80 years. **Africa outside Egypt has no female entity. The Americas have none. Southeast Asia has none. Central Asia and the Steppe have none. West Asia has none.**

Absent queens-regnant, regents and rulers whose absence is not defensible (all verified 0 hits):
- **Africa:** Amanirenas and the Kandakes of Meroë, Amina of Zazzau, **Nzinga of Ndongo and Matamba**, Queen Idia of Benin, Ranavalona I of Madagascar, Yaa Asantewaa, Empress Zewditu, Queen Nandi.
- **Europe:** **Theodora** (0 hits — Justinian I is present without her), Zoe and Theodora Porphyrogenita, **Margaret I of Denmark** — who founded the `Kalmar Union [era] 1397..1523` that sits empty in the tree — **Isabella I of Castile** (absent although `Reconquista & Iberian Unification [era] 711..1492` and `Spanish Empire [era] 1492..1898` are both present), **Maria Theresa** (absent although `The Habsburg Monarchy [era] 1526..1918` is present and empty), Eleanor of Aquitaine, Matilda, Mary I, Mary II, Anne, Christina of Sweden, Catherine de' Medici, Anne of Austria, Elizabeth of Russia, Olga of Kyiv, **Elizabeth II** (0 hits), Boudica, Zenobia.
- **Asia:** **Empress Suiko** (0 hits) and Japan's other seven reigning empresses — Kōgyoku, Jitō, Genmei, Genshō, Kōken/Shōtoku, Go-Sakuramachi — an absence guaranteed by the decision to populate Japan with 42 shoguns and zero monarchs; Queen Seondeok and Jindeok of Silla; the Trưng Sisters; Empress Dowager Cixi is present but Empress Dowager Longyu is not; Sorghaghtani Beki and Töregene Khatun; Mandukhai Khatun; Nur Jahan; Chand Bibi; Ahilyabai Holkar; Rani Lakshmibai; Sammu-ramat; Puduhepa; Kubaba of Kish; Pharaoh-era aside, Arsinoe II and Cleopatra I–II.
- **Oceania/Americas:** Kaʻahumanu, Queen Emma, Pōmare IV; the Aztec cihuacoatl office; Malintzin.

**Why it matters:** 3.8% is not what the historical record says; it is what a ruler-list-copying method returns. And the pattern of *which* women survive — Egyptian pharaohs, three Chinese empresses, four European monarchs, six modern South Asian prime ministers — tells you exactly which king-lists were transcribed.

### Literate and monumental bias, measured
**Severity:** high
`Ancient Egypt` = 189 entities and 143 reigns, because Manetho, the Turin Canon and the Palermo Stone hand you a numbered list. `Africa > Central Africa` = **4 entities, 0 reigns** for the Kongo, Luba and Lunda. `Africa > East Africa` = **3 entities, 0 reigns** for the entire Swahili coast, the Buganda and Bunyoro kingdoms (grep: 0), Ethiopia's Zagwe (0), the Funj Sultanate of Sennar (0), Adal (0), Darfur (0).

The bias is visible even *within* a category. `Poverty Point [period] 1751BC..1151BC` and `Watson Brake [period] 3500BC..3100BC` are present — monumental earthworks. **Adena and Hopewell are absent** (0 hits each) — same tradition, less spectacular mounds. `Great Zimbabwe [era] 1100..1450` is present, a stone site; `Mapungubwe`, its predecessor, is absent. `Nan Madol` is present as `Saudeleur Dynasty (Nan Madol) [era] 1100..1628` — basalt megaliths; the rest of Micronesia is one further node.

Absent for want of inscriptions and stone: the Sahel's oral-tradition polities beyond the three big empires (Kaabu, Jolof, Segou, Massina, Toucouleur — 0 each); the Igbo, Yoruba and Akan as societies rather than as `Benin Empire`/`Oyo Empire`/`Ashanti Empire` (0 hits for "Igbo", "Yoruba", "Akan"); the Ainu, Sámi, Inuit; the Chumash and Calusa; every Amazonian polity after `Marajoara Culture [era] 400..1400`.

**Why it matters:** the dataset's implicit claim is that the density of entities tracks the density of history. It tracks the density of surviving inscriptions. A reader concludes that Egypt had 4,000 years of eventful history and Central Africa had four things.

### Colonised and enslaved peoples appear only as objects
**Severity:** high
- `Global & Multi-Regional > Multi-Regional Empires > Scramble for Africa [era] 1881..1914` has one child: `Berlin Conference [event] 1884..1885`. The conquest of a continent is represented by the European meeting that authorised it. There is no Maji Maji, no Herero and Nama genocide (grep "Genocide": 0), no Anglo-Zulu War or Isandlwana — `Zulu Kingdom [era] 1816..1897` simply stops — no Battle of Adwa, although `Menelik II [reign] 1889..1913` is present, no Samori Ture, no Urabi revolt, no Mahdist state.
- `Decolonization [era] 1945..1997` is a **single empty leaf** for the political emancipation of two-thirds of humanity. No Ghana 1957, no Algerian War, no Bandung Conference, no Mau Mau, no Vietnamese independence beyond `French Indochina [era] 1887..1954`.
- `Africa > Nile Valley & Northeast Africa` places `Scramble for Africa` nowhere; both entities most specifically about Africa are filed **outside Africa**, under `Global & Multi-Regional`.
- **North America:** `Colonial North America [era] 1492..1783` → `United States [era] 1776..—` whose only child is `Civil War & Reconstruction [period] 1861..1877`. No Indian Removal Act, no Trail of Tears (0), no reservation system (0), no Wounded Knee, no Dawes Act, no boarding schools. `Comanche Empire [era] 1750..1875` ends in 1875 with nothing to explain it. `Haudenosaunee Confederacy [era] 1450..—` is open-ended and empty. No Powhatan, Cherokee, Lakota, Apache, Diné (0 each).
- **Australia:** `Aboriginal Australia [era] 65000BC..—` is open-ended but its children are `Sahul`, `Madjedbebe`, `Lake Mungo` — all Pleistocene. Then `Colonial Australia [era] 1788..1901` and `Commonwealth of Australia [era] 1901..—`, both empty. There is no frontier violence (0), no Stolen Generations, no Mabo, no 1967 referendum. The tree implies Aboriginal history is 65,000 years of archaeology followed by someone else's colony.
- **Korea:** `Japanese Colonial Rule [era] 1910..1945` — empty. No March 1st Movement, no Provisional Government, no forced labour.
- **India:** `East India Company Rule` and `British Raj` between them supply **15 governors-general and viceroys as `reign` entities** — Clive, Hastings, Cornwallis, Wellesley, Bentinck, Dalhousie, Canning, Lytton, Ripon, Curzon, Hardinge, Chelmsford, Irwin, Linlithgow, Mountbatten. The colonial administration receives full dynastic treatment; Indian resistance receives `Indian Rebellion of 1857`, `Jallianwala Bagh Massacre`, `Salt March`. Absent: the Bengal famines of 1770 and 1943, the Permanent Settlement, deindustrialisation, the INC's founding, Khilafat, Quit India, Ambedkar's Mahad Satyagraha.
- **South Africa:** apartheid does not exist (grep: 0).

**Why it matters:** the tree grants interiority — reigns, dynasties, sub-periods — to empires and grants only a start and end date to the people they ruled. That is the single most consequential framing choice in the dataset, and it is expressed purely through structure, so it is invisible to anyone reading entity text.

### "Global & Multi-Regional" is a dumping ground
**Severity:** medium-high
Its 114 entities are five unrelated things:

1. **Genuinely cross-regional:** `Human Prehistory`, `Paleolithic`, `Hominins`, `Neolithic Transition`, `Behavioural Firsts` (the 26 `threshold` nodes), `The Columbian Exchange`, `World War I`, `World War II`, `Cold War`, `COVID-19 Pandemic`. These belong here.
2. **European periodisation posing as global:** `Bronze Age`, `Iron Age`, `Classical Antiquity`, `Late Antiquity`, `Middle Ages`, `Early Modern`, `Industrial Revolution`, `Second Industrial Revolution`, `Long 19th Century`, `Short 20th Century`, `Contemporary`.
3. **Calendar conventions as entities:** `BCE (Before Common Era) [era] 3500BC..1BC`, `CE (Common Era) [era] 1..—`.
4. **West Asian polities evicted from West Asia:** `Rashidun Caliphate`, `Umayyad Caliphate` (Damascus), `Abbasid Caliphate` (Baghdad), `Fatimid Caliphate` (Cairo), `Ottoman Empire` (Bursa, Edirne, Istanbul). Their removal is why `West Asia` has 113 entities and 19 reigns, why Anatolia's sequence ends in 546 BC, and why Egypt's ends in 641.
5. **Africa's two biggest modern processes:** `Scramble for Africa`, `Decolonization`.

Categories 2–5 are not "multi-regional." They are, respectively, Europe's chronology, a dating convention, West Asia's history, and Africa's. The container's real rule is: *anything that does not fit the region-then-polity-then-ruler template goes here.* And note the double standard — `Ancient Rome`, `The British Empire`, `Spanish Empire`, `Portuguese Empire`, `Mongol Empire`, `Inca Empire` are all at least as multi-regional as the Umayyads, and all are filed in a region.

### Top-level groupings embed a viewpoint
**Severity:** medium
- The ten top-level regions are nine geographic containers plus one residual. Eight of the nine are compass-and-continent labels of European coinage: `West Asia`, `East Asia`, `South Asia`, `Southeast Asia`, `Central Asia & the Steppe`, `Oceania`. "West Asia" is at least better than "Middle East"; "the Steppe" is a view from a settled society.
- `Europe` gets four top-level intellectual eras of its own — `The Renaissance`, `The Reformation`, `Scientific Revolution`, `The Enlightenment` — as direct children of the region, a privilege no other region receives. There is no equivalent node for the Abbasid translation movement, the Song commercial revolution, the Kyoto court's literary culture, the Sanskrit cosmopolis, or the Timbuktu manuscript tradition. `Axial Age` exists but is buried under `Classical Antiquity`.
- `Americas > North America` contains `Colonial North America`, `United States` — and no Canada (0 hits) and no Mexico under North America (`Mexico (independent)` is filed under `Mesoamerica`). `Americas > Amazon & Southern Cone` has 3 entities and contains no Brazil, no Argentina, no Chile.
- `Africa > Nile Valley & Northeast Africa` groups Egypt with Kush, Aksum and Ethiopia, which is defensible; but Egypt within it is 189 of 200 entities, so the grouping functions as "Egypt, plus three neighbours."

### Japan: 256 calendar labels, 42 shoguns, zero emperors
**Severity:** medium
`East Asia > Japan` is 312 entities — 18% of the entire dataset — and 256 of them are nengō: `Ten'ō [period] 781..782`, `Eien [period] 987..989`, `Ten'yō [period] 1144..1145`. These drive the inventory's century histogram (`1300 CE: 96`, `1400 CE: 82`), so the dataset's apparent 14th-century peak in world history is an artefact of Japanese era-name granularity. Meanwhile the 42 `reign` entries are Minamoto and Kujō shoguns, four Kamakura princely figureheads, three unifiers and fifteen Tokugawa — and **not one tennō**. No Jinmu, no Suiko, no Tenmu, no Kanmu, no Go-Daigo (although `Kenmu Restoration [era] 1333..1336` is present), no Meiji as a person (only `Meiji [period] 1868..1912` as a nengō).
**Why it matters:** the tree accidentally makes a sophisticated argument — that real power lay with shoguns — and then undermines it, because with no emperors at all there is nothing for the shoguns to be regents *of*, and the Kenmu Restoration and Meiji Restoration become events without protagonists. Compare China, where 118 of 170 entities are emperors. Two neighbouring branches of the same tree use opposite conventions for the same class of thing.

### Where coverage is genuinely good
**Severity:** — (clean bill)
Worth recording so effort is not wasted here:
- **Palaeoanthropology and deep prehistory.** `Global & Multi-Regional > Human Prehistory` with `Hominins` (12 `taxon` nodes from *habilis* to *luzonensis*), `Paleolithic` with 15 named industries, and 26 `threshold` nodes from `Cut-Marked Bone` to `Domestic Chicken` is a coherent, well-shaped, genuinely global structure. `African Prehistory`'s 40 sites and `European Prehistory`'s 40 are strong.
- **Indus Valley.** `Indus Valley Civilization [era] 3300BC..1300BC` with `Early Harappan Ravi Phase`, `Kot Dijian Phase`, `Mature Harappan Phase`, `Harappan Deurbanisation`, `Late Harappan Phase`, plus `The Indus Script`, `The Rakhigarhi Genome` and `The Ghaggar-Hakra Question` — phase structure, sites and live controversies together. This is the model the rest of the dataset should follow.
- **Maritime Southeast Asia.** 16 polities from `Srivijaya` to `Republic of Indonesia`, including `Tondo`, `Kahuripan`, `Sultanate of Sulu`, `Demak`, `Aceh` — a genuinely non-canonical list. It needs rulers, but the polity coverage is better than Europe's.
- **The Andean sequence.** `Norte Chico / Caral` → `Chavín` → `Nazca`/`Moche` → `Tiwanaku`/`Wari` → `Chimú` → `Inca` → `Neo-Inca State at Vilcabamba` is correct and complete at the culture level.
- **Vietnamese dynastic sequence.** Ten dynasties plus `Trịnh Lords` and `Nguyễn Lords` as parallel children of `Later Lê Dynasty` — an unusually sophisticated bit of modelling.
- **Japanese nengō.** Whatever the weighting problem, the nengō list itself is complete and correctly dated, including the Nanboku-chō period's parallel northern and southern era names (`Engen`/`Ryakuō`, `Kōkoku`/`Kōei`).

---

## The five worst

1. **Colonised and enslaved peoples exist only as objects of empire, and the Atlantic slave trade does not exist at all.** `Scramble for Africa` has one child and it is `Berlin Conference`. `Decolonization [era] 1945..1997` is an empty leaf. `Japanese Colonial Rule [era] 1910..1945` is empty. `Colonial Australia` is empty. The `British Raj` supplies nine viceroys as `reign` entities while the Bengal famines are absent. And a `grep -i slave` across 1,765 entities returns one hit, `Mamluk (Slave) Dynasty` — no Middle Passage, no Haitian Revolution, no maroon polity, no abolition, and no Brazil in any form. The dataset lists the traders, the ports and the destinations and omits the trade. This is the finding that most changes what a reader believes.

2. **Egypt ends in 641, Mesopotamia and the Levant end in 539 BC, Anatolia ends in 546 BC, and the Ottomans and caliphates are filed outside West Asia.** Four of the deepest continuously documented regions on earth are terminated in antiquity, and the polities that would continue them — `Umayyad`, `Abbasid`, `Fatimid`, `Ottoman` — have been moved to `Global & Multi-Regional`. West Asia is left with 113 entities and 19 reigns against Ancient Rome's 100. A reader concludes the ancient Near East produced civilisation and then stopped.

3. **190+ empty containers, concentrated wherever no numbered king-list existed to copy.** `Ottoman Empire` (2 sultans of 36), `Ottonian Dynasty`, `Hohenstaufen Dynasty`, `Plantagenet England`, `Stuart England`, `Capetian France`, `Valois France`, all six German entities including `Nazi Germany`, `Qajar`/`Pahlavi`/`Islamic Republic of Iran`, `Seleucid Empire`, `Polish-Lithuanian Commonwealth`, ten Vietnamese dynasties, sixteen African kingdoms, `Republic of China` and `People's Republic of China`. Twentieth-century China and Germany contain zero people between them. The reader cannot distinguish "we have not written this yet" from "there was nothing here," and the boundary between the two tracks the availability of a list, not the availability of history.

4. **39% of the dataset is individual rulers, 3.8% of those rulers are women, and there is no representation available for a society without kings.** 690 reigns and 43 events. `Haudenosaunee Confederacy` is empty because the schema's only person-kind is `reign`. `The Netherlands` is filed as a `reign`. So are Muhammad, Luther, Guru Nanak, Pericles, Tagore, Gandhi and fourteen viceroys. Absent as a consequence: every trade network of consequence (no Silk Road, no Indian Ocean, no trans-Saharan, no Hanseatic), every legal and deliberative institution, the Ainu, Sámi, Inuit, Tuareg, Bedouin, San, and — after the 26 female reigns, nine of them Egyptian — Theodora, Suiko, Isabella I, Maria Theresa, Margaret I, Nzinga, Amanirenas, the Trưng sisters, Elizabeth II.

5. **European periodisation is installed as the dataset's global chronological spine, with a calendar convention filed as an era.** `Bronze Age`, `Iron Age` (empty, 1200–550 BC, imposed on regions that had no Bronze Age, no Iron Age, or both at once), `Classical Antiquity`, `Late Antiquity`, `Middle Ages`, `Early Modern`, `Long 19th Century`, `Short 20th Century` — plus `BCE (Before Common Era) [era] 3500BC..1BC`, which begins where writing begins and thereby defines everything earlier, including 62,000 years of Aboriginal Australia, as pre-history. Europe additionally gets `The Renaissance`, `The Reformation`, `Scientific Revolution` and `The Enlightenment` as region-level eras that no other region is granted. Every non-European sequence in the dataset has to be read through this clock, and the tree never says so.
