# Correctness review: polities, eras and cultures (424 entries)

Judgement pass, no sources consulted. Findings ordered by theme; the twenty worst are ranked at the end.

Counts as shipped: 268 `polity`, 144 `era`, 12 `culture`.

---

## Patterns (stated once, not repeated per entry)

### PATTERN-1 — 59 entries carry ±25-year bounds and `dated_by: unknown` on dates fixed to the year by written record
**Field:** `dated_by`, `bounds`
**Currently:** e.g. Tang Dynasty 618 `[593, 643]` `unknown`; Abbasid Caliphate 750 `[725, 775]`; Rashidun 632 `[607, 657]`; Umayyad 661 `[636, 686]`; Kievan Rus' 862 `[837, 887]`; Carolingian Empire 751 `[726, 776]`; Song 960 `[935, 985]`; Sui 581 `[556, 606]`; Goryeo 918 `[893, 943]`; Unified Silla 668; Khmer Empire 802; Đinh Dynasty 968; Early Lê 980; Ngô 939; Heian 794; Nara 710; Rise of Islam 610; HRE 800; France 987; England 927; Buyid 934; Saffarid 861; Tahirid 821; Fatimid 909; Chola 848; Harsha 606; Rashtrakuta 753; Western Chalukya 973; Uyghur Khaganate 744; Five Dynasties 907; Liao 907.
**Should be:** `dated_by: calendar` with `bounds: [null, null]` for all of these. The Abbasid revolution, the Tang founding, Charlemagne's coronation and the Hijra-era caliphates are dated to the year (often the month) in contemporary or near-contemporary annals.
**Confidence:** high
**Why:** This is the mirror image of the Berlin Wall bug in the brief — false uncertainty on precisely known dates. A reader is told the Tang could have begun in 593, which no historian has ever proposed. It appears to be a blanket ±25 applied wherever `dated_by` was left as `unknown`.

### PATTERN-2 — The Anatolia and Arabia blocks file kingdoms as `era`
**Field:** `kind`
**Currently:** Lydia, Mitanni, Urartu, Phrygia, Neo-Hittite States, The Hittites, Dilmun, The Nabataeans, Saba are all `era`. So are Aq Qoyunlu and Qara Qoyunlu in Iran.
**Should be:** `polity` for all of them (Neo-Hittite States is a set of polities, so `era` is at least arguable; the rest are not).
**Confidence:** high
**Why:** Every one of these had a king, a capital and a chancery. Urartu fought Assyria as a state; Lydia's Mermnad dynasty is a king-list; Saba's mukarribs built the Marib dam. These are the clearest kind errors in the file and they cluster, which suggests one authoring pass mislabelled the whole region.

### PATTERN-3 — Regional `Prehistory` containers start at wildly inconsistent points, and several start after their own children
**Field:** `start`
**Currently:** African Prehistory −3,298,050; European Prehistory −453,050; Central Asian −298,050; Oceanian −73,050; Southeast Asian −44,050; Americas −34,050; West Asian −13,000; South Asian −8,950; East Asian −14,000.
**Should be:** a stated rule, applied consistently — either "earliest hominin presence in the region" or "earliest anatomically modern human presence". Under any rule West Asia (−13,000), South Asia (−8,950) and East Asia (−14,000) are wrong by hundreds of thousands of years: West Asia has Ubeidiya at c. 1.5 Ma, South Asia has Attirampakkam, East Asia has Zhoukoudian.
**Confidence:** high
**Why:** Two of them are self-contradicting: `west-asia.prehistory` starts −13,000 but contains Epipalaeolithic (Levant) at −23,000; `east-asia.prehistory` ends −300 but Late Pleistocene China, in the same tree, starts −40,000. European Prehistory at −453,050 also postdates Atapuerca and Happisburgh by several hundred thousand years.

### PATTERN-4 — `dated_by: calendar` on African and Pacific polities whose foundation dates are tradition or archaeology, not records
**Field:** `dated_by`
**Currently:** Kingdom of Kongo 1390, Luba 1585, Lunda 1665, Great Zimbabwe 1100, Benin Empire 1180, Oyo 1400, Kingdom of Dahomey 1600, Saudeleur 1100, Yapese Empire 1400, Māori Aotearoa 1250, Mapuche 1000 — all `calendar`, no bounds.
**Should be:** `typological`/`radiocarbon-calibrated`/`received` as appropriate, with real bounds. Great Zimbabwe's occupation dates are radiocarbon and stratigraphy; Kongo's 1390 is a genealogy back-calculated from oral tradition.
**Confidence:** medium-high
**Why:** `calendar` with no bounds tells the reader these are documentary dates of the same standing as 1492. They are not, and the round numbers (1100, 1250, 1400, 1000) give it away.

---

## Kind errors: things that are not polities filed as `polity`

### europe.reformation
**Field:** `kind`
**Currently:** `polity`, "The Reformation", 1517–1648.
**Should be:** `era`.
**Confidence:** high
**Why:** A religious movement has no government. This is the single worst kind error in the file — nothing about the Reformation resembles a state, and its own summary describes an upheaval, not a polity.

### west-asia.arabia.rise-islam
**Field:** `kind`
**Currently:** `polity`, "Rise of Islam", 610–632.
**Should be:** `era` (the span of Muhammad's prophetic career). If a polity is wanted here it is the Medinan community/state from 622, which is a different entity with different dates.
**Confidence:** high
**Why:** The summary itself says "Muhammad's prophetic career and the birth of Islam" — a period, not a state.

### west-asia.anatolia.hittites.hittite-collapse
**Field:** `kind`
**Currently:** `polity`, "Collapse of the Hittite Empire", −1200 to −1180.
**Should be:** an event, or failing that `era`.
**Confidence:** high
**Why:** A collapse is not a thing with a government. Note also that a polity kind here makes the Hittite tree read as "empire contains two states, one of which is its own destruction".

### europe.mediterranean.greece and europe.mediterranean.greece.classical
**Field:** `kind`
**Currently:** both `polity` — "Ancient Greece" −3200 to −146, "Classical Greece" −480 to −323.
**Should be:** `era` for both, exactly as Ancient Rome and Ancient Egypt are handled.
**Confidence:** high
**Why:** Ancient Greece never had a government; that is the defining fact about it. Filing it as a polity while Ancient Rome is an era is also internally inconsistent. The states belong beneath it (Athens, Sparta, Macedon — Macedon is currently a sibling, not a child).

### europe.western.britain.victorian
**Field:** `kind`, `under`
**Currently:** `polity`, "Victorian Britain", 1837–1901, under England (Medieval to Modern).
**Should be:** `era`, and placed as a sibling of The Georgian Era.
**Confidence:** high
**Why:** The Georgian Era, the same kind of thing, is correctly an `era` in this file — and sits under Western Europe rather than under England, so the two are inconsistent in both fields. The polity through 1837–1901 is the United Kingdom.

### south-asia.independence.india-prime-ministers, south-asia.independence.pakistan-leaders
**Field:** `kind`
**Currently:** `polity` — "Prime Ministers of India", "Leaders of Pakistan".
**Should be:** not polities at all; these are office/person lists. Their children (reigns) should hang off the Republic of India and Pakistan as states.
**Confidence:** high
**Why:** An office-holder list has no span of its own and no government; it is a container. A reader looking for "India" will not find a polity for it.

### south-asia.independence
**Field:** `kind`
**Currently:** `polity`, "Post-Independence South Asia", 1947–present.
**Should be:** `era`, or a region node. Also carries Gandhi (1915–1948), Jinnah (1913–1948), Ambedkar (1927–1956) and Subhas Bose (1938–1945) as children, all of whom largely predate 1947.
**Confidence:** high
**Why:** "Post-Independence South Asia" is a period label covering several sovereign states; it is not one state. The four independence-era figures filed under a 1947-start node are misplaced by their own dates.

### global.multi-regional
**Field:** `kind`, `start`/`end`
**Currently:** `polity`, "Multi-Regional Empires", −550 to 1997.
**Should be:** a grouping/category node, not a polity. Its own summary says "Polities that held territory in more than one world region, gathered so they can be compared".
**Confidence:** high
**Why:** A polity spanning 2,547 years and containing the Abbasids, the Ottomans and Decolonization is a shelf, not a state.

### europe.central.prussia
**Field:** `kind`, `name`, `end`
**Currently:** `polity`, "Rise of Prussia", 1701–1871.
**Should be:** either the Kingdom of Prussia as a polity, 1701–1918 (dissolved as Free State in 1947), or an era named "Rise of Prussia".
**Confidence:** medium-high
**Why:** Prussia did not cease to exist in 1871; it became the dominant state within the German Empire and kept its own crown, army and administration. As written it is a polity named after a process and killed off half a century early.

### oceania.polynesia.aotearoa
**Field:** `kind`
**Currently:** `polity`, "Māori Aotearoa", 1250–1840.
**Should be:** `culture` or `era`. Pre-1840 Aotearoa was iwi and hapū, with no overarching government — that is precisely the "political organisation is the open question" case.
**Confidence:** medium-high
**Why:** The summary says "Māori settlement and society", which is not a polity's description.

### americas.amazon-southern.mapuche
**Field:** `kind`, `start`
**Currently:** `polity`, "Mapuche / Araucanía", 1000–1883.
**Should be:** `culture` or `era`. The Mapuche fought Inca and Spanish as autonomous lof and rehue with wartime toqui, not as a single state; and the 1000 start is an arbitrary round number.
**Confidence:** medium
**Why:** Filing a decentralised people as a polity implies a central government whose absence is the historically important fact.

### europe.mediterranean.rome.empire.year-of-four, .year-of-five, .western-collapse
**Field:** `kind`
**Currently:** all `polity` — "Year of the Four Emperors" (69), "Year of the Five Emperors" (193), "Western Collapse" (455–480).
**Should be:** `era` (or events). Each names a stretch of time or a process, not a state.
**Confidence:** medium-high
**Why:** A civil war year is not a polity; there was one polity, in crisis. Western Collapse also runs to 480, four years past the end of the Roman Empire it is filed under (476) — a child outliving its parent, the exact failure mode the brief calls out.

### americas.mesoamerica.teotihuacan
**Field:** `kind`
**Currently:** `polity`, −100 to 550.
**Should be:** defensible, but Teotihuacan is the textbook case of a major centre whose form of government is unknown (no ruler portraits, no king-list, collective-rule hypotheses live). Consider `culture`, or a summary that says so.
**Confidence:** low
**Why:** Flagged only because the brief's `culture` definition fits it better than most entries currently marked `culture`.

---

## Kind errors: states filed as `era`

### central-asia.qara-khitai
**Field:** `kind`
**Currently:** `era`, "Qara Khitai", 1124–1218.
**Should be:** `polity`. The Western Liao was a dynastic state with gurkhans, a capital at Balasagun and Chinese-style administration.
**Confidence:** high

### east-asia.china.western-xia
**Field:** `kind`
**Currently:** `era`, "Western Xia", 1038–1227.
**Should be:** `polity`. A Tangut empire with emperors, its own script and a bureaucracy; it is an era here apparently only because it lacks an official dynastic history.
**Confidence:** high

### europe.northern.kalmar
**Field:** `kind`
**Currently:** `era`, "Kalmar Union", 1397–1523.
**Should be:** `polity` — a personal union of three kingdoms under one monarch, which is a government.
**Confidence:** high

### southeast-asia.mainland.lan-xang
**Field:** `kind`
**Currently:** `era`, "Lan Xang", 1353–1707.
**Should be:** `polity`. Its own summary calls it a "Lao kingdom" with successor kingdoms.
**Confidence:** high

### southeast-asia.maritime.tondo
**Field:** `kind`
**Currently:** `era`, "Tondo", 900–1589.
**Should be:** `polity`. The summary literally opens "Polity on Manila Bay".
**Confidence:** high

### southeast-asia.maritime.kahuripan
**Field:** `kind`
**Currently:** `era`, "Kahuripan", 1019–1045.
**Should be:** `polity` — Airlangga's kingdom, partitioned between his heirs.
**Confidence:** high

### central-asia.hephthalites
**Field:** `kind`, `historicity`
**Currently:** `era`, `historicity: contested`, 440–560.
**Should be:** `polity`, historicity absent (accepted).
**Confidence:** high
**Why:** The Hephthalites are attested in Sasanian, Chinese, Indian and Byzantine sources, they minted coins, and they killed a Sasanian shah (Peroz I) in battle. What is contested is their ethno-linguistic origin and internal structure, not their existence. Marking them contested tells the reader they may not have happened.

### west-asia.iran.aq-qoyunlu, west-asia.iran.qara-qoyunlu
**Field:** `kind`
**Currently:** `era`.
**Should be:** `polity`. Both are Turkoman dynastic confederations with rulers, coinage and capitals (Tabriz, Diyarbakır) — the same category as the Safavids who replaced them and who are correctly a polity.
**Confidence:** high

### southeast-asia.mainland.british-burma, southeast-asia.mainland.french-indochina
**Field:** `kind`
**Currently:** `era`, 1885–1948 and 1887–1954.
**Should be:** `polity`. Both were governed territories with a constitution, a governor-general and a treasury; British Raj and Dutch East Indies are correctly polities in this same file.
**Confidence:** medium-high
**Why:** Inconsistent treatment of colonial states — the reader gets Raj-as-state and Indochina-as-period for the same kind of thing.

### europe.western.netherlands.voc, .wic-first, .wic-second
**Field:** `kind`
**Currently:** `era`.
**Should be:** `polity`. The VOC's own summary says it had "the power to wage war, coin money and hold territory" — that is a definition of a government.
**Confidence:** medium-high

### europe.western.france.colonial-empire-first, .colonial-empire-second
**Field:** `kind`
**Currently:** `era`, 1534–1814 and 1830–1962.
**Should be:** `polity`, alongside the British, Spanish and Portuguese empires, which are all polities here.
**Confidence:** medium
**Why:** Same-category entries split across two kinds; the reader cannot compare empires if half of them are periods.

### oceania.polynesia.new-zealand
**Field:** `kind`
**Currently:** `era`, "New Zealand (post-Waitangi)", 1840–present.
**Should be:** `polity`. New Zealand is a state, and Commonwealth of Australia in the same block is correctly a polity.
**Confidence:** high

### central-asia.sogdia
**Field:** `kind`, `historicity`
**Currently:** `era`, `historicity: contested`, −500 to 750.
**Should be:** `culture` or a region node; historicity absent.
**Confidence:** high
**Why:** Sogdiana is documented in Achaemenid inscriptions, Greek historians, Chinese annals and thousands of Sogdian-language documents; nothing about it is contested in the historicity sense. The summary's real point — "never politically unified" — is the `culture` case, not the `contested` case.

### central-asia.saka
**Field:** `kind`
**Currently:** `era`, −600 to −100.
**Should be:** `culture` (or a people). The Saka are known chiefly from kurgan burials and outsiders' names for them.
**Confidence:** medium

### africa.east.swahili
**Field:** `kind`
**Currently:** `era`, "Swahili Coast City-States", 900–1500.
**Should be:** `culture`, or a container for the individual sultanates (Kilwa, Mombasa, Pate) as polities. The end date is also questionable: Kilwa and the coast continued past 1500 under Portuguese and then Omani pressure well into the 19th century.
**Confidence:** medium

### oceania.melanesia.fijian-chiefdoms
**Field:** `kind`, `start`
**Currently:** `era`, 500–1874, `dated_by: unknown` with bounds `[475, 525]`.
**Should be:** `culture` for the pre-contact sequence, with Bau/Rewa/Verata as polities; and the 500 start with ±25 bounds is spurious precision — Fiji was settled c. 1000 BCE and chiefdom formation is a gradual archaeological inference.
**Confidence:** medium

### americas.intermediate.taino
**Field:** `kind`, `start`
**Currently:** `era`, "Taíno Chiefdoms", 1200–1500, `dated_by: calendar`.
**Should be:** `culture`. The chiefdoms are the polities; "Taíno" is the archaeological/ethnic horizon, and its dates come from ceramic series (Ostionoid/Chican), not a calendar. The 1200 start also cuts off several centuries of continuous development.
**Confidence:** medium

### west-asia.mesopotamia.phoenicia
**Field:** `kind`
**Currently:** `era`, "Phoenician City-States", −1500 to −332.
**Should be:** `culture`, with Tyre, Sidon and Byblos as polities beneath. Compare Carthage, which is correctly a polity.
**Confidence:** medium

### west-asia.anatolia.hittites
**Field:** `kind`
**Currently:** `era`, −1650 to −1180, summary "An Anatolian empire that fought Egypt to a draw at Kadesh".
**Should be:** either `polity` (the Hittite Empire, with Old/Middle/New Kingdom phases as eras beneath, matching the Egypt pattern), or keep `era` and rewrite the summary, which currently describes a state. As shipped, the kind and the summary contradict each other.
**Confidence:** medium-high
**Why:** Also structurally incomplete: the era contains an Old Kingdom and a Collapse but no New Kingdom / Empire period, which is the part the summary is actually about.

### southeast-asia.mainland.dvaravati
**Field:** `kind`, `historicity`
**Currently:** `era`, `historicity: contested`, 600–1100.
**Should be:** `culture`, historicity absent.
**Confidence:** high
**Why:** This is the textbook `culture` case as the brief defines it — a material horizon (Mon Buddhist art, stupas, coins reading *śrīdvāravatī*) whose political unity is the open question. Its existence as a culture is not contested; `contested` here misreads the debate.

### southeast-asia.mainland.funan
**Field:** `historicity`
**Currently:** `polity`, `historicity: contested`, 68–550.
**Should be:** historicity absent; the debate is over Funan's extent, centralisation and whether "Funan" is a Chinese exonym for something less unified — not over whether Óc Eo and its polity existed.
**Confidence:** medium

### east-asia.china.jin-jurchen.jingkang
**Field:** `kind`
**Currently:** `era`, "Jingkang Incident", 1126–1127.
**Should be:** an event. A two-year sack-and-capture is not a period label.
**Confidence:** medium

### central-asia.russian-turkestan
**Field:** `kind`
**Currently:** `era`, "Russian Conquest of Central Asia", 1865–1895.
**Should be:** an event/process, or a polity named Russian Turkestan (the Governorate-General, 1867–1917) — the id says one thing and the name another.
**Confidence:** medium

### west-asia.culture-sea-peoples
**Field:** `kind`
**Currently:** `culture`, `historicity: contested`, −1200 to −1150.
**Should be:** not a culture. The `contested` flag is right, but the Sea Peoples are a textual label in Egyptian inscriptions, deliberately *not* an archaeological horizon — no single material assemblage corresponds to them. That is the whole scholarly problem.
**Confidence:** medium

### south-asia.vedic.corpus
**Field:** `kind`
**Currently:** `era`, "The Vedic Corpus", −1500 to −500, identical span to its parent Vedic Period.
**Should be:** a text/work, not an era. As shipped it is a period that duplicates its parent exactly.
**Confidence:** medium

### global.bce, global.ce
**Field:** `kind`, `start`/`end`, `historicity`
**Currently:** `era`; BCE = −3500 to −1 with bounds `[-3700, -3300]`; CE = 1 to present with bounds `[-24, 26]`; both `historicity: interpretive`.
**Should be:** not eras at all — they are calendar conventions. If retained, BCE cannot start at 3500 BCE (it covers every year before 1), and CE cannot have ±25 bounds on year 1, which is a definitional boundary, not a measurement.
**Confidence:** high
**Why:** ±200 years of uncertainty on the start of "BCE" and ±25 on the start of "CE" are meaningless, and `historicity: interpretive` on a numbering scheme misuses the field.

---

## Dates and spans

### east-asia.china.yuan
**Field:** `end`
**Currently:** 1271–1370.
**Should be:** 1368 (Ming capture of Dadu / Toghon Temür's flight). 1370 is his death in Mongolia, by which point the regime is the Northern Yuan.
**Confidence:** high
**Why:** The Ming entry starts 1368, so the file simultaneously has the Yuan and the Ming ruling China for two years, with no note explaining it.

### africa.nile.egypt.middle-kingdom.dyn11
**Field:** `start`
**Currently:** "11th Dynasty (reunified)", −2125 to −1985, filed under Middle Kingdom (−2055 to −1650).
**Should be:** −2055 for the reunified phase. −2125 is the start of the whole Theban 11th Dynasty, most of which falls in the First Intermediate Period.
**Confidence:** high
**Why:** The name says "reunified" but the dates are the unreunified dynasty's, so the child begins 70 years before the era containing it.

### west-asia.prehistory
**Field:** `start`
**Currently:** −13,000, containing Epipalaeolithic (Levant) at −23,000.
**Should be:** far earlier (Lower Palaeolithic; Ubeidiya c. 1.5 Ma) if it means the region's prehistory, or renamed to what it actually covers ("West Asian Neolithisation").
**Confidence:** high
**Why:** A container that begins 10,000 years after its own first child.

### east-asia.prehistory
**Field:** `start`, `end`, `summary`
**Currently:** −14,000 to −300, summary "Jomon Japan and the Chinese Neolithic, gathered here for browsing".
**Should be:** at minimum start before Late Pleistocene China (−40,000), which sits in the same tree; the end at −300 is the end of Jōmon and has nothing to do with China, whose prehistory ends c. −1600.
**Confidence:** high
**Why:** The span is Japan's, applied to all of East Asia.

### central-asia.mongol-empire
**Field:** `end`
**Currently:** 1206–1368, containing Chagatai Khanate (to 1687) and Golden Horde (to 1502).
**Should be:** the unified empire ended in 1259/1260 (Toluid civil war) or 1294 at the latest; 1368 is the end of the *Yuan*, not the empire. Either way children running 130–320 years past the parent need explaining.
**Confidence:** medium-high
**Why:** As written the successor khanates outlive the empire they are filed inside, which is the brief's "polity outliving its own empire".

### central-asia.mongol-empire.chagatai
**Field:** `end`
**Currently:** 1226–1687.
**Should be:** 1347 for the Chagatai Khanate proper (it splits into Moghulistan and Transoxiana); 1687 belongs to the Eastern Chagatayid/Yarkent line and should be flagged as such.
**Confidence:** medium

### americas.prehistory
**Field:** `start`, `end`, `date_standing`
**Currently:** −34,050 to 500, `radiocarbon-calibrated`, `date_standing: majority`.
**Should be:** a start of c. −34,000 rests on the contested Chiquihuite Cave / pre-LGM claims, which are a minority position, not a majority one; consensus figures are c. 16,000–13,000 BCE, with White Sands at c. 21,000 BCE debated. And 500 CE is not the end of prehistory anywhere in the Americas — most of the hemisphere is pre-documentary until 1492.
**Confidence:** medium-high
**Why:** `date_standing: majority` on the earliest and least accepted peopling date presents a minority reading as settled.

### oceania.prehistory
**Field:** `start`
**Currently:** −73,050, while Aboriginal Australia in the same file starts −65,000.
**Should be:** consistent with the Sahul settlement figure used elsewhere (c. 65,000 BP, i.e. c. −63,000). −73,050 is older than any accepted date for human presence in Sahul.
**Confidence:** medium

### southeast-asia.prehistory
**Field:** `start`
**Currently:** −44,050.
**Should be:** earlier — modern humans are in island Southeast Asia by c. 65,000–73,000 BP (Lida Ajer, Callao, Madjedbebe as the neighbouring constraint), and *Homo erectus* far earlier still.
**Confidence:** medium

### south-asia.prehistory
**Field:** `start`
**Currently:** −8,950.
**Should be:** either much earlier, or renamed. Its summary ("early farming, rice cultivation, pre-urban settlement") describes the Neolithic only, but the entry is the region's whole prehistory container.
**Confidence:** medium

### europe.prehistory
**Field:** `start`
**Currently:** −453,050, `uranium-series`, `date_standing: consensus`.
**Should be:** far earlier. Atapuerca Sima del Elefante (c. 1.2 Ma) and Happisburgh (c. 800–950 ka) are not fringe claims. −453,050 looks like the date of one particular site (Sima de los Huesos) promoted to the start of European prehistory.
**Confidence:** medium-high

### global.prehistory.hominins
**Field:** `start`, `name`
**Currently:** "Hominins", −2,800,000 to present.
**Should be:** if it means hominins, c. 7 Ma (Sahelanthropus) or at least 4.4 Ma (Ardipithecus); −2.8 Ma is the earliest *Homo* (Ledi-Geraru). Either the start or the name is wrong.
**Confidence:** medium-high
**Why:** The summary's "a dozen or so named species, most of which overlapped" describes the whole hominin clade, which the date excludes by four million years.

### americas.north.haudenosaunee
**Field:** `bounds`
**Currently:** 1450–present, bounds `[1450, 1450]`, `dated_by: typological`, `date_standing: majority`.
**Should be:** wide bounds. The founding date of the Confederacy is one of the most genuinely disputed dates in North American history — proposals run from 1142 (Mann/Fields, from the eclipse tradition) through c. 1450 to c. 1600, and Haudenosaunee oral tradition places it much earlier than the archaeological reading.
**Confidence:** high
**Why:** Zero-width bounds assert certainty on precisely the date nobody can fix, and `majority` standing overstates it.

### oceania.polynesia.settlement
**Field:** `bounds`
**Currently:** 1025–1290, bounds `[1025, 1025]`, `date_standing: consensus`.
**Should be:** real bounds. The short-chronology start for East Polynesian expansion is c. 1025–1120 in the Wilmshurst/Hunt-Lipo synthesis, itself the product of a chronology revolution that overturned the previous consensus — precisely the situation where bounds matter.
**Confidence:** medium-high

### europe.western.migration
**Field:** `end`
**Currently:** Migration Period, 376–800.
**Should be:** 568 (Lombard entry into Italy) on the standard convention; 476 or c. 550 also defensible. An end at 800 swallows the whole Merovingian era and collides with the Carolingian Empire (751–888) and the HRE (800–) in the same file.
**Confidence:** medium

### east-asia.korea.three-kingdoms
**Field:** `start`, `dated_by`, `historicity`
**Currently:** `era` −57 to 668, `dated_by: unknown`, bounds `[-82, -32]`, no historicity flag; contains Munmu of Silla (661–681), whose reign runs 13 years past the era's end.
**Should be:** −57 is the *Samguk Sagi*'s traditional founding date for Silla, which almost no historian accepts as the start of a Silla state (archaeology puts state formation in the 4th century). It should be `dated_by: received` with a traditional/contested standing, exactly as Gojoseon is handled two entries away.
**Confidence:** medium-high
**Why:** The file marks Gojoseon's 2333 BCE as received and contested but treats Silla's 57 BCE as an ordinary date with ±25 bounds. Same source, same problem.

### east-asia.korea.chulmun
**Field:** `start`
**Currently:** −6000.
**Should be:** c. −8000 on the usual Jeulmun periodisation (Incipient/Initial Jeulmun from c. 8000 BCE); −6000 corresponds to Early Jeulmun.
**Confidence:** medium

### east-asia.japan.yayoi
**Field:** `start`, `bounds`
**Currently:** −300, bounds `[-325, -275]`.
**Should be:** contested and much wider. The AMS redating campaign (Kokuritsu Rekishi Minzoku Hakubutsukan, from 2003) pushed the Yayoi start to c. 900–1000 BCE, and that revision is now widely, though not universally, accepted. ±25 years on this date is the opposite of the actual state of the question.
**Confidence:** medium-high
**Why:** Also inconsistent with Jōmon ending at −300, which inherits the old chronology.

### west-asia.mesopotamia.israel-judah
**Field:** `start`, `summary`
**Currently:** "Kingdoms of Israel and Judah", −1050 to −586, no historicity flag, summary "Iron Age Hebrew kingdoms".
**Should be:** a start at 1050 BCE is the biblical united monarchy, whose existence and scale are among the most actively contested questions in Levantine archaeology (the "low chronology" debate). A start of c. 930 BCE for the two separate kingdoms, or an explicit contested marking, would be honest. Note also that Israel ends in 722, not 586.
**Confidence:** medium-high
**Why:** One span presented flatly conflates a contested united monarchy with two well-attested kingdoms that ended 136 years apart.

### west-asia.iran.median
**Field:** `historicity`, `summary`
**Currently:** "Median Empire", −678 to −549, no historicity flag, no summary.
**Should be:** flagged as contested. Since Sancisi-Weerdenburg, the existence of a Median *empire* (as opposed to a tribal confederation) has been seriously doubted; the dates and king-list come almost entirely from Herodotus, and Ecbatana has yielded little to confirm them.
**Confidence:** medium-high
**Why:** The file marks the Xia and Gojoseon contested on much the same kind of evidence, and leaves the Medes as accepted.

### west-asia.arabia.pre-islamic and .dilmun
**Field:** `start`
**Currently:** parent −3000 to 610; child Dilmun −3300 to −510.
**Should be:** the parent must start at or before its earliest child. Dilmun's own −3300 is also early for the polity — Dilmun appears in Mesopotamian texts from the later 4th/3rd millennium and its Barbar-period peak is c. 2200–1700 BCE.
**Confidence:** medium

### africa.nile.kush
**Field:** `start`, `name`
**Currently:** "Kingdom of Kush", −2500 to 350.
**Should be:** 2500–1500 BCE is Kerma, which is normally distinguished from Kush proper (Napatan/Meroitic, c. 1070 BCE onward). Either start c. −1070 or make clear the entry is the whole Nubian sequence, which the summary implies but the name does not.
**Confidence:** medium

### central-asia.turkic-khaganate
**Field:** `end`
**Currently:** First Turkic Khaganate, 552–603.
**Should be:** 603 is the definitive east–west split; the Eastern Khaganate survives to 630 (Tang conquest) and is usually counted within the First Khaganate. Given the Second Khaganate is dated 682–744 in this file, the 630 date is the one that makes the sequence legible.
**Confidence:** medium

### africa.nile.egypt.new-kingdom.dyn18 / .dyn19
**Field:** `end` / `start`
**Currently:** 18th Dynasty −1550 to −1292; 19th Dynasty −1295 to −1186.
**Should be:** one boundary, −1292 (Shoshenq/Ramesses I accession on the low chronology). As shipped the two dynasties overlap for three years.
**Confidence:** medium

### europe.central.hre.ottonian
**Field:** `start`
**Currently:** Ottonian Dynasty 919–1024, filed under Holy Roman Empire (800–1806).
**Should be:** 919 is Henry the Fowler's election as king of East Francia, 43 years before Otto I's imperial coronation in 962 — so as an *imperial* dynasty it begins in 962. Either start at 962 or note that the dynasty predates the empire it is filed under.
**Confidence:** low-medium

### europe.central.germany-modern
**Field:** `start` vs `summary`
**Currently:** start 1945, summary "Federal Republic of Germany from 1949 (reunified 1990)".
**Should be:** pick one — 1945 (occupation) or 1949 (the two German states). The record and its own description disagree by four years.
**Confidence:** medium

### south-asia.rashtrakuta
**Field:** `start`
**Currently:** 753, with Dantidurga (735–756) filed beneath.
**Should be:** 735 if Dantidurga's reign is included; 753 is the conventional imperial start (defeat of the Badami Chalukyas), which is also the end date given for Chalukyas of Badami.
**Confidence:** medium
**Why:** As shipped the dynasty's first ruler begins 18 years before the dynasty.

### americas.andes.tiwanaku
**Field:** `start`, `dated_by`
**Currently:** 500–1000, `dated_by: unknown`, bounds `[475, 525]`.
**Should be:** radiocarbon, with wider bounds. Tiwanaku's occupation begins in the last centuries BCE and its expansive state phase is usually placed c. 500–600 CE — a round 500 with ±25 is unwarranted precision on a radiocarbon-dated sequence.
**Confidence:** medium

### south-asia.indus
**Field:** `dated_by`
**Currently:** `culture`, −3300 to −1300, `dated_by: unknown`, bounds `[-3500, -3100]`.
**Should be:** `radiocarbon-calibrated`. The Harappan phase boundaries (Early 3300, Mature 2600, Late 1900) are radiocarbon-based, and every other comparable culture entry in this file uses that value.
**Confidence:** medium

### global.bronze-age
**Field:** `dated_by`
**Currently:** −3300 to −1200, `dated_by: calendar`, `date_standing: consensus`.
**Should be:** `radiocarbon-calibrated` or `typological`. Nothing about the start of the Bronze Age is calendrical, and the boundary is regionally variable by more than a millennium.
**Confidence:** medium-high

### global.iron-age
**Field:** `end`
**Currently:** −1200 to −550.
**Should be:** unclear as a single global span — the conventional end is 550 BCE only for the Near East (539, Cyrus); in Britain it runs to 43 CE, in Scandinavia to c. 800 CE, and South Asian and African sequences differ again. Either regionalise it or say in the summary that the end is a Near Eastern convention.
**Confidence:** medium
**Why:** This is the European/Near-Eastern periodisation imposed globally that the objective asks about.

### global.middle-ages
**Field:** `summary`
**Currently:** "Between the fall of Rome and the Renaissance; medieval Christendom, the Islamic Golden Age, Tang-Song China, and Kamakura Japan."
**Should be:** say explicitly that "Middle Ages" is a European periodisation and that Tang–Song China and Kamakura Japan are being slotted into a frame their own historiographies do not use.
**Confidence:** medium
**Why:** As written it presents Latin Christendom's tripartite scheme as a world period. Compare `global.mesolithic`, which handles exactly this problem well ("A European period name that much of the world does not use").

### global.neolithic / .agricultural-revolution
**Field:** `end`
**Currently:** Neolithic −10,000 to −3300; Neolithic Transition −10,000 to −1800, inside it.
**Should be:** the child cannot end 1,500 years after the parent. The Transition's −1800 (reflecting late/independent centres) is defensible on its own terms, but then it is not a subdivision of the Neolithic as dated here.
**Confidence:** medium

### global.multi-regional.age-of-sail
**Field:** `summary`
**Currently:** 1418–1815, summary "roughly Columbus to Napoleon".
**Should be:** the start is Portuguese (Madeira/Henry the Navigator, 1418–1419), 74 years before Columbus. Summary and dates describe different periods.
**Confidence:** medium

### africa.nile.egypt.late-period
**Field:** `summary`
**Currently:** "Egypt was twice a Persian province and twice independent again."
**Should be:** Egypt was twice a Persian province (525–404, 343–332) but independent again only once between them (404–343), and after 332 it was Macedonian, not independent. The symmetry is rhetorical rather than accurate.
**Confidence:** medium

### east-asia.china.jin-jurchen
**Field:** `summary`
**Currently:** "ruling from Kaifeng until the Mongol conquest".
**Should be:** the Jin ruled from Shangjing and then Zhongdu (modern Beijing); Kaifeng became the capital only in 1214, after the Mongol siege forced the move — the last 20 years of a 119-year dynasty.
**Confidence:** medium-high

### europe.mediterranean.rome.empire.valentinianic-theodosian
**Field:** `summary`
**Currently:** "The last dynasties to rule a single empire".
**Should be:** the claim is hard to sustain — the definitive administrative split is normally dated to 395, inside this very span, and the summary itself says the "final administrative division of east and west set in". Also 457 (Marcian's death) is an odd Theodosian terminus; Marcian was a Theodosian only by marriage.
**Confidence:** medium

### americas.mesoamerica.olmec
**Field:** `summary`
**Currently:** "Mother culture of Mesoamerica."
**Should be:** flag as contested. The *madre* vs *hermana* debate (Olmec as mother culture versus one sister culture among coeval developments) has been live since the 1990s and is not settled; stating it flatly is exactly the overstatement the brief targets.
**Confidence:** medium-high

### africa.west.songhai
**Field:** `summary`
**Currently:** "Largest state in West African history".
**Should be:** contested — Songhai and Mali are both claimed as the largest, and no reliable areal figures exist for either. Say "one of the largest" or attribute the claim.
**Confidence:** medium

### americas.andes.norte-chico
**Field:** `summary`
**Currently:** "Oldest known civilization in the Americas."
**Should be:** defensible but should be qualified — "oldest known" depends on defining civilisation by monumental architecture rather than writing or pottery (Caral had neither), and the claim is contested by those who read the sites as non-urban.
**Confidence:** low-medium

### south-asia.gupta
**Field:** `aliases`
**Currently:** aliases include "Golden Age of India".
**Should be:** the "Golden Age" label is a contested historiographical characterisation (and an alias, not a name); the summary correctly hedges with "often called", but the alias field asserts it.
**Confidence:** low-medium

### southeast-asia.mainland.vietnam
**Field:** `aliases`
**Currently:** `["Đại Việt", "Đại Cồ Việt", "Đại Ngu", "Đại Việt, 939-1804"]`
**Should be:** drop the fourth entry — an alias with a date range embedded in it is malformed and duplicates the first.
**Confidence:** high (that it is wrong as data), low importance

### south-asia.british-raj
**Field:** child placement
**Currently:** 1858–1947, with Mountbatten (1947–1948) filed beneath.
**Should be:** Mountbatten's 1947–1948 tenure was as Governor-General of *independent* India, after the Raj ended. He belongs under the post-independence state, or his span should be 1947 only (as Viceroy, to 15 August).
**Confidence:** medium

### europe.mediterranean.rome.empire
**Field:** `end` vs children
**Currently:** −27 to 476, with Julius Nepos (474–480) and Western Collapse (455–480) beneath.
**Should be:** if Nepos to 480 is counted, the empire's end date must accommodate it; if 476 is the chosen convention, Nepos's span needs a note. As shipped a polity has two children extending past its own death.
**Confidence:** medium

---

## Deliberate choices I would keep, and one I would not

- **Egypt's Old / Middle / New Kingdoms as eras, with dynasties as polities beneath.** Correct, and the best-modelled part of the file. The Intermediate Periods as eras with parallel dynasties is exactly right.
- **Ancient Egypt as an era.** Correct. There is no continuous polity from Naqada to the Arab conquest, and the dynasties beneath carry the government.
- **Ancient Rome as an era with Kingdom / Republic / Empire beneath.** Correct, and `dated_by: received` with `date_standing: traditional` on −753 is exactly the right handling of a legendary foundation date.
- **Elam as a polity with Old / Middle / Neo-Elamite eras beneath.** Consistent with the Egypt pattern; keep.
- **The one I would change:** **Ancient Greece as a polity** (above). If Rome and Egypt are eras with states beneath, Greece — the one of the three that genuinely never had a single government — cannot be the polity. Fixing this also gives Macedon, Classical Greece and the Hellenistic Period a coherent home; at present Hellenistic Period is a sibling of Ancient Greece rather than a phase within it.

---

## The twenty worst

Ranked by how badly each misleads a reader.

1. **PATTERN-1** — 59 precisely dated polities carrying ±25-year uncertainty and `dated_by: unknown`. The Tang, the Abbasids, Charlemagne's coronation and the Rashidun caliphs are all presented as datable only to within half a century. Highest volume, and it corrupts the field the whole dataset is built on.
2. **europe.reformation** — a religious movement filed as a polity.
3. **west-asia.arabia.rise-islam** — a prophetic career filed as a polity.
4. **europe.mediterranean.greece** (+ `.classical`) — Ancient Greece as a polity, while Rome and Egypt are correctly eras. Asserts a Greek state that never existed.
5. **PATTERN-2** — Lydia, Mitanni, Urartu, Phrygia, Saba, the Nabataeans, Dilmun, Aq Qoyunlu, Qara Qoyunlu: nine or ten kingdoms filed as spans of time.
6. **central-asia.hephthalites** — a well-attested empire that killed a Sasanian shah, marked `contested`, and filed as an era. Wrong on both fields.
7. **PATTERN-3 / west-asia.prehistory / east-asia.prehistory** — regional prehistory containers that begin after their own children and vary by three orders of magnitude between regions.
8. **americas.north.haudenosaunee** — zero-width bounds on the most disputed founding date in North American history, with `date_standing: majority`.
9. **east-asia.china.yuan** — ends 1370 while the Ming begins 1368, so two dynasties rule China simultaneously with no explanation.
10. **central-asia.mongol-empire** — successor khanates run 130 and 320 years past the parent empire's end date, which is itself the Yuan's date, not the empire's.
11. **americas.prehistory** — a contested pre-LGM peopling date marked `majority`, and prehistory ending in 500 CE.
12. **south-asia.independence.\*** — "Prime Ministers of India" and "Leaders of Pakistan" as polities, with the independence generation filed under a 1947-start node they predate.
13. **west-asia.mesopotamia.israel-judah** — the contested united monarchy given a flat 1050 BCE start with no historicity flag, and two kingdoms that ended 136 years apart collapsed into one end date.
14. **west-asia.iran.median** — a Median *empire* presented as accepted when its existence as an empire is a live scholarly dispute.
15. **southeast-asia.mainland.dvaravati** and **central-asia.sogdia** — the two clearest `culture` cases in the file, both filed as eras *and* marked `contested`, misdescribing the debate as one about existence.
16. **africa.nile.egypt.middle-kingdom.dyn11** — "11th Dynasty (reunified)" begins 70 years before the reunification, and before the era containing it.
17. **americas.mesoamerica.olmec** — "Mother culture of Mesoamerica" stated as fact; thirty years of *madre/hermana* argument erased in five words.
18. **east-asia.korea.three-kingdoms** — the legendary 57 BCE Silla foundation treated as an ordinary date with ±25 bounds, while Gojoseon's equivalent is correctly marked received and contested.
19. **east-asia.japan.yayoi** — −300 with ±25 bounds, ignoring the AMS redating that moved the Yayoi start to c. 900 BCE.
20. **west-asia.anatolia.hittites.hittite-collapse** and the Roman **year-of-four / year-of-five / western-collapse** — five events and crisis-years filed as polities, one of which (Western Collapse) outlives its own parent empire.

---

## Proposed tests

Each rule below is stated so it can be implemented against the current schema, with the threshold spelled out and the entities that violate it today named. `safe` = no legitimate exceptions found in this dataset, can fail the build. `advisory` = real exceptions exist, warn only.

Note on scope: five of these use `reigns.json` as well as `polities.json`, because the most diagnostic errors show up at the join.

---

### T1 — `advisory` · A polity's span must contain the span of every reign filed beneath it
**Rule:** for every entity of kind `reign`, `reign.start >= ancestor.start` and `reign.end <= ancestor.end` (treat null end as open). Report the delta in years.
**Violations today:** `americas.mesoamerica.aztec` (Itzcoatl 1427, parent 1428) · `east-asia.china.yuan` (Kublai 1260, parent 1271) · `east-asia.japan.azuchi-momoyama` (Nobunaga 1568, parent 1573) · `east-asia.korea.three-kingdoms` (Munmu 661–681, parent ends 668) · `europe.eastern.russian-empire` (Peter I 1682, parent 1721) · `europe.eastern.soviet` (Lenin 1917, parent 1922) · `europe.mediterranean.rome.empire` (Julius Nepos 474–480, parent ends 476) · `south-asia.british-raj` (Mountbatten 1947–1948, parent ends 1947) · `south-asia.independence` (Gandhi 1915, Jinnah 1913, Ambedkar 1927, Bose 1938; parent starts 1947) · `south-asia.rashtrakuta` (Dantidurga 735, parent 753) · `west-asia.iran.achaemenid` (Cyrus II −559, parent −550).
**Legitimate exception:** a ruler who reigned before the polity was founded and then founded it — Peter I ruled the Tsardom from 1682 and declared the empire in 1721, which is a fact, not an error. Same for Cyrus (king of Anshan from 559, empire dated from the conquest of Media in 550). These need a "reign predates polity" annotation rather than a fix, which is why this is advisory.
**Would have caught:** the Yuan/Kublai and Rashtrakuta/Dantidurga findings above, and the Mountbatten misplacement.

### T2 — `safe` · A child entity's span must lie inside its parent's span
**Rule:** for every entity with a parent in the same file, `child.start >= parent.start` and `child.end <= parent.end` (null end = open, but a null-ended child of a closed-ended parent is itself a violation).
**Violations today:** `africa.nile.egypt.middle-kingdom.dyn11` (−2125 vs −2055) · `africa.nile.egypt.predynastic.dynasty-0` (−3200 to −3085 vs parent ending −3100) · `central-asia.mongol-empire.chagatai` (to 1687 vs 1368) · `central-asia.mongol-empire.golden-horde` (to 1502 vs 1368) · `europe.mediterranean.rome.empire.western-collapse` (to 480 vs 476) · `global.neolithic.agricultural-revolution` (to −1800 vs −3300) · `global.prehistory.firsts` (−3,390,000 vs −3,300,000, and null end vs parent ending −3000) · `global.prehistory.hominins` (null end vs parent ending −3000) · `oceania.prehistory.australian-intensification` (to −51 vs −734) · `west-asia.arabia.pre-islamic.dilmun` (−3300 vs −3000) · `west-asia.prehistory.chalcolithic`, `.chalcolithic-anatolia`, `.epipalaeolithic`, `.late-chalcolithic-mesopotamia` (all outside −13,000 to −3800) · `central-asia.prehistory.mountain-corridor` (to −1250 vs −1400).
**Why safe:** 15 violations and not one of them is defensible — in every case either the parent's span or the child's is simply wrong. Where a successor state genuinely outlives its parent empire (Golden Horde), the fix is to reparent or to extend the parent, not to permit the contradiction.
**Would have caught:** the 11th Dynasty error, the West Asian prehistory container, and the Mongol successor khanates.

### T3 — `safe` · `bounds` must not be zero-width
**Rule:** if `bounds[0]` is not null then `bounds[1] - bounds[0] >= 1`. Zero-width bounds must be written as `[null, null]`.
**Violations today:** `americas.north.haudenosaunee` `[1450, 1450]` · `oceania.polynesia.settlement` `[1025, 1025]`.
**Why safe:** a bound of ±0 either means "no uncertainty", which is what `[null, null]` is for, or it is a data-entry accident. Both current violations are on dates with large real uncertainty, so the value is actively false.

### T4 — `advisory` · Bounds must be commensurate with `dated_by`
**Rule:** two thresholds.
(a) `dated_by` in {`calendar`, `received`, `first-attestation`} ⇒ `bounds` must be `[null, null]` or narrower than ±5 years.
(b) `dated_by == unknown` AND `start > 500 CE` AND bounds present ⇒ flag: a post-500 CE date that is genuinely unknown to ±25 is rare, and a post-500 CE date carrying exactly ±25 is almost always a default that was never revisited.
**Violations today (b):** 59 entities, listed under PATTERN-1 above — including `east-asia.china.tang`, `global.multi-regional.abbasid`, `global.multi-regional.rashidun`, `global.multi-regional.umayyad`, `europe.eastern.kievan-rus`, `europe.western.carolingian`, `east-asia.china.song`, `east-asia.china.sui`, `east-asia.korea.goryeo`, `southeast-asia.mainland.khmer`, `west-asia.arabia.rise-islam`, `europe.central.hre`, `europe.western.france`, `europe.western.england`.
**Legitimate exception:** `africa.west.kanem-bornu` (700) and `oceania.polynesia.tui-tonga` (950) really are traditional dates with genuine century-scale slack — for those the correct fix is *wider* bounds plus `dated_by: received`, not removal. So the test cannot auto-fail.
**Sharper safe variant:** flag any entity where `bounds[1] - bounds[0] == 50` exactly AND `dated_by == unknown` — that combination appears 59 times and is a machine default, never a judgement. As a build failure that would be defensible.
**Would have caught:** PATTERN-1, the largest single class of error in the file.

### T5 — `safe` · An entity of kind `polity` must not be named like a period, an event or a process
**Rule:** fail if `kind == polity` and `name` matches `\b(Age|Period|Antiquity|Era|Revolution|Reformation|Renaissance|Collapse|Rise|Conquest|Incident|Restoration|Prehistory|Intermezzo|Expansion|Exchange)\b` or `^Year of `.
**Violations today:** `europe.reformation` ("The Reformation") · `west-asia.arabia.rise-islam` ("Rise of Islam") · `west-asia.anatolia.hittites.hittite-collapse` ("Collapse of the Hittite Empire") · `europe.mediterranean.rome.empire.western-collapse` ("Western Collapse") · `europe.mediterranean.rome.empire.year-of-four` · `europe.mediterranean.rome.empire.year-of-five` · `europe.central.prussia` ("Rise of Prussia").
**Near-miss to whitelist:** `africa.nile.egypt.late-period.dyn26-saite` ("26th Dynasty — Saite Renaissance") is a genuine dynasty with a period nickname appended; match on the leading token or exclude names containing "Dynasty".
**Why safe:** with that one exclusion, all seven remaining matches are real kind errors, including the two worst in the file.

### T6 — `advisory` · An entity of kind `era` must not be named like a state
**Rule:** flag if `kind == era` and `name` matches `\b(Kingdom|Empire|Sultanate|Khanate|Khaganate|Dynasty|Caliphate|Union|Republic|Confederacy|Emirate|Viceroyalty|Company)\b`.
**Violations today:** `europe.northern.kalmar` ("Kalmar Union") · `europe.western.france.colonial-empire-first` · `.colonial-empire-second` · `europe.western.netherlands.voc` · `.wic-first` · `.wic-second`.
**Legitimate exception:** Egypt's `old-kingdom`, `middle-kingdom` and `new-kingdom` are deliberately eras, as are `west-asia.iran.elam.*-elamite` "Periods" — phases of one polity. Whitelist by id prefix, or exclude entities whose parent is a polity of the same civilisation.
**Extension worth having:** the reverse-signal version, matching the *summary* rather than the name, catches more: flag `kind == era` whose summary matches `^(An?|The) [A-Za-z ]*(kingdom|empire|state|sultanate|confederation|polity)\b`. That catches `west-asia.anatolia.hittites` ("An Anatolian empire…"), `west-asia.anatolia.lydia` ("A western Anatolian kingdom…"), `west-asia.anatolia.urartu` ("An Iron Age kingdom…"), `west-asia.anatolia.phrygia` ("An Anatolian kingdom…"), `west-asia.anatolia.mitanni` ("A Hurrian kingdom…"), `west-asia.iran.aq-qoyunlu` / `.qara-qoyunlu` ("Turkoman confederation…"), `southeast-asia.mainland.lan-xang` ("Lao kingdom…"), `southeast-asia.maritime.tondo` ("Polity on Manila Bay…"), `africa.east.swahili`, `oceania.polynesia.new-zealand`. That is PATTERN-2 caught by a regex over the field that already contradicts the kind.
**Would have caught:** PATTERN-2, ten-plus kind errors.

### T7 — `safe` · An entity of kind `polity` must not be an office list or a category shelf
**Rule:** fail if `kind == polity` and (`name` matches `^(Prime Ministers|Leaders|Presidents|Kings|Rulers|Heads) of ` OR `summary` contains any of "gathered here", "so they can be compared", "for browsing").
**Violations today:** `south-asia.independence.india-prime-ministers` · `south-asia.independence.pakistan-leaders` · `global.multi-regional` (summary: "gathered so they can be compared with each other").
**Why safe:** a container that admits in its own summary that it is a container cannot be a state. The two other entities with that summary language (`east-asia.prehistory`, `oceania.prehistory`) are correctly `era`, so the rule fires only on the real errors.

### T8 — `advisory` · `dated_by: calendar` requires a documentary calendar for that place and time
**Rule (a):** flag `dated_by == calendar` where `start < -600`.
**Violations (a):** `global.bronze-age` (−3300) · `west-asia.arabia.pre-islamic.dilmun` (−3300) · `west-asia.iran.elam.old-elamite` (−2400) · `west-asia.anatolia.hittites` and `.hittite-old-kingdom` (−1650) · `west-asia.anatolia.mitanni` (−1600) · `.hittite-collapse` (−1200) · `.neo-hittite` (−1180) · `west-asia.iran.elam.middle-elamite` (−1450) · `.neo-elamite` (−1050) · `west-asia.anatolia.urartu` (−840) · `west-asia.arabia.pre-islamic.saba` (−800) · `europe.mediterranean.macedon` (−700) · `west-asia.anatolia.lydia` (−680).
**Legitimate exception:** Bronze-Age Near Eastern dates come from king-lists and eclipse-anchored chronologies, which is a defensible reading of "calendar" even though the absolute anchor is disputed by ±64 years (the high/middle/low chronology problem). `global.bronze-age` at −3300 is not defensible under any reading.
**Rule (b):** flag `dated_by == calendar` with `start < 1600` in Africa south of the Sahara, the pre-Columbian Americas, and Oceania, where the date cannot rest on a local written record.
**Violations (b):** `africa.central.kongo` (1390) · `africa.southern.great-zimbabwe` (1100) · `africa.west.benin` (1180) · `africa.west.oyo` (1400) · `africa.southern.mutapa` (1430) · `americas.amazon-southern.mapuche` (1000) · `americas.intermediate.taino` (1200) · `americas.mesoamerica.purepecha` (1300) · `oceania.micronesia.saudeleur` (1100) · `oceania.micronesia.yap` (1400) · `oceania.polynesia.aotearoa` (1250).
**Legitimate exception in (b):** `africa.west.mali` (1235) and `africa.west.songhai` (1464) are dated from Arabic chronicles, and `americas.mesoamerica.aztec` (1428) and `americas.andes.inca` (1438) from post-conquest annals with year-count systems — documentary, if not European-calendrical.
**Would have caught:** PATTERN-4.

### T9 — `advisory` · Sibling polities described as sequential must not overlap
**Rule:** for sibling entities of kind `polity` under the same parent, flag any pair whose spans intersect by ≥1 year.
**Violations today:** `africa.nile.egypt.new-kingdom.dyn18` (ends −1292) vs `.dyn19` (starts −1295) · `south-asia.vijayanagara.saluva` (1485–1505) vs `.tuluva` (1491–1570) · `.tuluva` vs `.aravidu` (1542–1646) · `europe.mediterranean.rome.empire.valentinianic-theodosian` (364–457) vs `.western-collapse` (455–480) · `.dominate-tetrarchy` (284–324) vs `.constantinian` (306–363) · `central-asia.mongol-empire.chagatai` vs `.golden-horde`.
**Legitimate exception:** genuinely parallel regimes. Egypt's `tip.dyn22` and `tip.dyn25-kushite` overlap because Libyan and Kushite dynasties really did rule simultaneously — the Third Intermediate Period is defined by that. The Roman `year-of-four` inside `flavian`, and Abbasid/Fatimid under Multi-Regional Empires, are also legitimate. So: warn, and require an explicit `parallel: true` or a summary that says so.
**Would have caught:** the 18th/19th Dynasty three-year overlap and the Western Collapse / Roman Empire contradiction.

### T10 — `safe` · A regional prehistory era must begin no later than the earliest entity in its region
**Rule:** for each entity whose name matches `Prehistory$`, compute `min(start)` over all entities sharing its top-level region prefix; fail if the era's start is later.
**Violations today:** `east-asia.prehistory` (−14,000, while `east-asia.china.late-pleistocene` starts −40,000) · `west-asia.prehistory` (−13,000, while `west-asia.prehistory.epipalaeolithic` starts −23,000) · `global.prehistory` (−3,300,000, while `global.prehistory.firsts` starts −3,390,000).
**Why safe:** a container of a region's prehistory that starts after that region's oldest entity is self-contradicting on its face. This catches the East Asia case that T2 misses, because Late Pleistocene China is filed under China rather than under the prehistory node.
**Companion advisory:** also flag when a region's prehistory era *ends* after that region's first polity begins — `east-asia.prehistory` ends −300 while `east-asia.china.shang` begins −1600.

### T11 — `advisory` · `historicity: contested` must be justified, and must not be used for "politically fragmented"
**Rule:** flag `historicity` in {`contested`, `legendary`} where `dated_by` is `unknown` (i.e. contested existence asserted without saying what the evidence even is), and separately flag any entity whose summary contains "never politically unified", "of disputed political unity", or "whose political organisation" while `historicity == contested` — that is a `kind: culture` case, not an existence claim.
**Violations today (first clause):** `central-asia.hephthalites` · `central-asia.sogdia` · `east-asia.china.xia` · `southeast-asia.mainland.dvaravati` · `southeast-asia.mainland.funan`.
**Violations today (second clause):** `central-asia.sogdia` ("Never politically unified") · `southeast-asia.mainland.dvaravati` ("of disputed political unity").
**Legitimate exception:** `east-asia.china.xia` is correctly contested — the dispute really is over whether a Xia state existed — even though `dated_by` is `unknown`. So the first clause must warn, not fail. The second clause has no exception in this dataset and could be made safe.
**Would have caught:** the Hephthalites, Sogdia, Dvaravati and Funan historicity errors — four of the file's eight `contested` flags are wrong.

### T12 — `safe` · A `culture` must not have a `reign` child
**Rule:** fail if any entity of kind `culture` has a descendant of kind `reign`.
**Violations today:** none. All 12 cultures are clean.
**Keep it anyway:** it is the guard that stops the next author from giving the Olmec a king-list, and it costs nothing to run. Note that the related check *does* fire: nine entities of kind `era` have reign children (`east-asia.japan.edo`, `.kamakura`, `.muromachi`, `.azuchi-momoyama`, `east-asia.korea.three-kingdoms`, `east-asia.china.legendary`, `africa.nile.egypt.tip`, `europe.northern.viking-age`, `south-asia.east-india-company`) — which is legitimate for Japanese periods (the shogunate is the polity and the period is its name) but is a smell for `europe.northern.viking-age`, where Cnut is filed under a period rather than under any of the kingdoms he actually ruled.

### T13 — `advisory` · Every `reign` must have a polity ancestor
**Rule:** flag reigns whose ancestor chain contains no entity of kind `polity`.
**Violations today:** 16 — `europe.persons-socrates`, `-aristotle`, `-archimedes`, `-gutenberg`, `east-asia.persons-confucius`, `-laozi`, `central-asia.persons-zoroaster`, `-al-khwarizmi`, `-ibn-sina`, `south-asia.persons-mahavira`, `-siddhartha-gautama`, `-aryabhata`, `south-asia.kabir`, `south-asia.nanak`, `south-asia.tagore`, and `europe.western.netherlands`.
**Legitimate exception:** the `persons-*` entries are philosophers and scientists, not rulers; they hang off regions on purpose. The right fix is a separate kind for them rather than a reparent, so this stays advisory.
**But one violation is a real error, found by this rule:** `europe.western.netherlands` is kind `reign`, named "The Netherlands", spanning 1581 to the present, with the VOC and both West India Companies filed beneath it. A country is not a reign. It should be kind `polity` (the Dutch Republic and successors). This is the only entity in the dataset where a state is filed as a person's tenure.

### T14 — `advisory` · A globally scoped era must say that its boundaries are a regional convention
**Rule:** for entities under `global.*` of kind `era` whose span is drawn from one region's periodisation, require the summary to name the convention. Implementable as: `global.*` era whose summary mentions no region and whose name matches `(Age|Antiquity|Middle Ages|Iron|Bronze|Neolithic|Mesolithic|Paleolithic)` must contain one of "convention", "European", "Near Eastern", "regionally", "does not use".
**Violations today:** `global.bronze-age` (−3300 to −1200 is a Near Eastern/Aegean span presented globally) · `global.iron-age` (ends −550, which is the Near Eastern date; Britain runs to 43 CE, Scandinavia to c. 800 CE) · `global.middle-ages` (names Tang–Song China and Kamakura Japan inside a Latin-Christendom frame without saying so) · `global.classical-antiquity` (−800 to 500, Greek and Roman, correctly described but scoped `global`).
**Model to copy:** `global.mesolithic` already passes — "A European period name that much of the world does not use, and a live argument about whether it describes a real stage at all." That is exactly the sentence the other four need.
**Legitimate exception:** `global.paleolithic` and `global.neolithic.agricultural-revolution` are genuinely global in the sense intended, and the latter already says "at least seven regions".
**Would have caught:** the European-periodisation-imposed class the objective asks about.

### T15 — `safe` · The `extant` field must agree with `end`
**Rule:** if `end is null` then `extant` must be `true`; if `end` is non-null then `extant` must be `false` or null.
**Violations today:** all 25 entities with a null `end` — `extant` is `null` on every one of the 424 records, so the field is entirely unpopulated. Includes `americas.north.usa`, `east-asia.china.prc`, `europe.eastern.russia-modern`, `oceania.australia.commonwealth`, `africa.north.morocco-alaouite`, `europe.western.england`, `europe.western.france`, `global.ce`, `global.contemporary`.
**Why safe:** the field either means something or should be dropped. As shipped a consumer cannot distinguish "still exists" from "end date unknown", and both are encoded as null.

### T16 — `advisory` · An alias must not contain a date range or a duplicate of another alias
**Rule:** fail if any alias matches `\d{3,4}\s*[-–]\s*\d{3,4}`, or if two aliases on the same entity differ only by a suffix.
**Violations today:** `southeast-asia.mainland.vietnam`, alias `"Đại Việt, 939-1804"`, which both embeds a date range and duplicates the alias `"Đại Việt"` already present.
**Legitimate exception:** none found, but with one violation the rule is not yet earning build-failure status.

---

### Two things a test cannot catch, noted so they are not assumed covered

- **Overstated summaries.** "Mother culture of Mesoamerica", "Largest state in West African history", "Oldest known civilization in the Americas", "First empire in world history" are all superlatives asserting a contested reading. A lint for superlatives (`Largest|Oldest|First|Only|Greatest`) plus a requirement that the summary hedge or cite would fire on perhaps a dozen entries, most of them fairly. It is worth trying as advisory; it will not distinguish the fair superlatives from the unfair ones.
- **A date that is simply the wrong century.** Nothing structural distinguishes the Yuan ending in 1370 from the Yuan ending in 1368. That one was only catchable because the Ming's start contradicts it — which suggests the one genuinely high-value semantic test left: **for successive polities in the same region, flag where one's end and the next's start disagree by 1–5 years**, since conquests are usually single events. That would have caught the Yuan/Ming gap and the 18th/19th Dynasty overlap.
