# Audit: regional gaps — missing polities, dynasties and peoples

Lens: which polities, dynasties and peoples a knowledgeable reader would expect and cannot
find. Every absence below was checked against `inventory.txt` by name and by the obvious
alternate names/spellings before being reported. Cities are excluded per the brief.

## What the region counts actually mean

The headline distribution (East Asia 518, Europe 285, Africa 271, South Asia 233, West Asia
113, Global 113, Americas 74, Southeast Asia 66, Central Asia 55, Oceania 27) overstates two
regions and understates the rest, for a structural reason worth stating before the findings:

- **East Asia's 518 is padded by Japanese era names.** Roughly 230 of those 518 entries are
  Japanese `nengō` — `Kōhō [period] 964..968`, `Ten'en [period] 974..976`, `Eiso [period]
  989..990` and so on, one per two-to-five-year regnal era. They are legitimate entities, but
  they are calendar labels, not polities. Strip them and East Asia is closer to 290.
- **Africa's 271 is dominated by African Prehistory (~40 site entries) plus the complete
  Egyptian pharaoh list (~150 reigns).** Everything from the Sahel to the Cape after 1500 is
  fewer than 20 entities.
- **West Asia's 113 covers Mesopotamia, Anatolia, Iran, Arabia and the Levant with almost no
  ruler lists at all** — see below. It is not merely thin; it is structurally different from
  Egypt and China, which get reign-by-reign treatment. The Caliphates and the Ottomans were
  also moved out to `Global & Multi-Regional`, so the nominal 113 overstates even that.

So the real imbalance is worse than the counts suggest, and it is concentrated in exactly the
places the brief suspected.

---

## West Asia

### Assyrian ruler list is effectively empty
**Severity:** high
**What is missing:** the entire Neo-Assyrian king list except one man. `Ashurbanipal
[reign] 669BC..631BC` is the *only* Assyrian ruler in the dataset. Absent: Ashur-uballit I,
Adad-nirari I, Shalmaneser I, Tukulti-Ninurta I, Tiglath-Pileser I, Ashurnasirpal II,
Shalmaneser III, Shamshi-Adad V, Adad-nirari III, Tiglath-Pileser III, Shalmaneser V,
Sargon II, Sennacherib, Esarhaddon, Ashur-etil-ilani, Sin-shar-ishkun. Also absent: an
**Old Assyrian Period** node (the era node starts at 2025BC but its only children are
`Middle Assyrian Empire` and `Neo-Assyrian Empire`, leaving 660 years unlabelled),
Shamshi-Adad I, the Assyrian trading colony system at Kanesh, the deportation policy, the
**Fall of Nineveh (612 BC)**.
**Where it belongs:** `Assyrian Empires [era] 2025BC..609BC (foun)` and its child
`Neo-Assyrian Empire [period] 911BC..609BC (foun)`.
**Why it matters:** the first genuine territorial empire in world history is represented by
one king. A reader cannot see how Assyria was built, and Sennacherib and Sargon II — the two
Assyrians most likely to appear in any other narrative a reader has met — are simply not
there. Egypt gets 150 reigns; Assyria gets one.
**Rough dates:** 2025–609 BC; Neo-Assyrian peak 745–627 BC.

### Babylonian ruler lists: one king each for Old and Neo-Babylonian
**Severity:** high
**What is missing:** under Old Babylonian, only `Hammurabi`. Absent: Sumu-abum, Sin-Muballit,
Samsu-iluna, Ammi-Ditana, Samsu-Ditana, and the **Code of Hammurabi as an entity in its own
right**. Under Neo-Babylonian, only `Nebuchadnezzar II`. Absent: Nabopolassar (who founded
it), Amel-Marduk, Neriglissar, Labashi-Marduk, Nabonidus, Belshazzar, and the **Fall of
Babylon to Cyrus (539 BC)**. `Kassite Babylon [era] 1595BC..1155BC` has no rulers and no
children at all — no Kurigalzu, no Burna-Buriash II, no Amarna correspondence, no Elamite
sack of Babylon. The **Second Dynasty of Isin** and **Nebuchadnezzar I** are absent, as is
the Sealand dynasty.
**Where it belongs:** `Old Babylonian Empire [era] 2000BC..1600BC (foun)`,
`Kassite Babylon [era] 1595BC..1155BC (foun)`, `Neo-Babylonian Empire [era] 626BC..539BC (foun)`.
**Why it matters:** Babylon is the reference civilisation for law, astronomy and the
scribal tradition, and the dataset gives it two named individuals across 1,500 years. The
539 BC fall — the hinge that hands Mesopotamia to Persia permanently — is not an entity.
**Rough dates:** 2000–539 BC.

### Sumerian city-state period has no polities
**Severity:** high
**What is missing:** `Sumerian Early Dynastic [era] 2900BC..2334BC` contains exactly one
child, `Gilgamesh (legendary)`. Absent: **Lagash** (Ur-Nanshe, Eannatum and the Stele of the
Vultures, Entemena, **Gudea**), **Kish**, **Umma**, **Nippur**, **Isin**, **Larsa**, the
Lagash–Umma border war, **Lugalzagesi of Uruk**. Under Akkad, only `Sargon of Akkad` —
absent: Rimush, Manishtushu, **Naram-Sin**, Shar-kali-sharri, **Enheduanna** (the first named
author in world literature), and the **Gutian interlude**. `Ur III (Neo-Sumerian) [era]
2112BC..2004BC` has no children at all — no **Ur-Nammu**, no **Shulgi**, no Code of Ur-Nammu,
no Amorite incursions, no fall of Ur.
**Where it belongs:** `Sumerian Early Dynastic [era] 2900BC..2334BC (foun)`,
`Akkadian Empire [era] 2334BC..2154BC (foun)`, `Ur III (Neo-Sumerian) [era] 2112BC..2004BC (foun)`.
**Why it matters:** the dataset asserts that Mesopotamia invented cities and writing and then
declines to name a single Sumerian city-state or a single king of Ur. Ur III in particular is
the best-documented bureaucratic state of the third millennium and it is a bare label.
**Rough dates:** 2900–2004 BC.

### Hittite kings — the empire has no rulers
**Severity:** high
**What is missing:** `The Hittites` has five children, all periods or events
(`Hattusa`, `Hittite Old Kingdom`, `Mursili I Sacks Babylon`, `Battle of Kadesh`,
`Collapse of the Hittite Empire`) and **zero reigns**. Absent: Hattusili I, Mursili I as a
reign, Telipinu and the Edict of Telipinu, Tudhaliya I, **Suppiluliuma I**, Mursili II,
Muwatalli II, **Hattusili III** and the Egyptian–Hittite treaty (the oldest surviving
parity treaty), Tudhaliya IV, Suppiluliuma II. Also absent: a **Hittite New Kingdom /
Empire period** node between the Old Kingdom and the collapse; the Hittite Laws; **Kizzuwatna**,
**Arzawa**, the **Luwians**, **Ahhiyawa**. `Mitanni [era] 1600BC..1260BC` likewise has no
children — no Shaushtatar, no **Tushratta**, no Hurrians as a people.
**Where it belongs:** `The Hittites [era] 1650BC..1180BC (foun)` and
`Mitanni [era] 1600BC..1260BC (inte)`.
**Why it matters:** the Bronze Age Near East was a three-way great-power system (Egypt,
Hatti, Assyria/Mitanni). Egypt's side is fully populated with reigns; the Hittite and Hurrian
sides are empty, so the system reads as Egypt plus scenery.
**Rough dates:** 1650–1180 BC.

### Sasanian shahs, Parthian kings, and the whole Seleucid dynasty
**Severity:** high
**What is missing:** `Sasanian Empire` carries four shahs (`Ardashir I`, `Shapur I`,
`Khosrow I Anushirvan`, `Khosrow II Parviz`) out of roughly thirty. Absent: Bahram I–II,
Narseh, **Shapur II** (the 70-year reign that fought Julian), Ardashir II, Shapur III,
Yazdegerd I, **Bahram V Gur**, Yazdegerd II, Peroz I, Balash, **Kavad I**, Hormizd IV,
Bahram Chobin, Kavad II, **Purandokht** and **Azarmidokht** (the two Sasanian queens),
**Yazdegerd III** (the last shah). Also absent: the Roman–Sasanian wars as entities, the
Mazdakite movement, Ctesiphon's sack.
`Parthian (Arsacid) Empire` has exactly one reign, `Mithridates I`. Absent: **Arsaces I**,
Mithridates II the Great, Orodes II and the **Battle of Carrhae (53 BC)**, Phraates IV,
Vologases I, Artabanus IV.
`Seleucid Empire [era] 312BC..63BC (foun)` has **no children whatsoever**: no **Seleucus I
Nicator**, no Antiochus I, no **Antiochus III the Great**, no **Antiochus IV Epiphanes**, no
Battle of Magnesia, no Maccabean revolt against him.
`Median Empire [era] 678BC..549BC` also has no children — no Deioces, Cyaxares or Astyages.
**Where it belongs:** `Sasanian Empire [era] 224..651 (foun)`,
`Parthian (Arsacid) Empire [era] 247BC..224 (foun)`, `Seleucid Empire [era] 312BC..63BC (foun)`,
`Median Empire [era] 678BC..549BC (inte)`.
**Why it matters:** Rome's emperors are enumerated down to `Florianus [reign] 276..276`, a
two-month usurper. Rome's actual peer rival for seven centuries gets four shahs and one
Parthian. The dataset therefore cannot represent Rome's eastern frontier as a two-sided story.
**Rough dates:** 312 BC – 651 CE.

### Achaemenid mid-dynasty is missing
**Severity:** medium
**What is missing:** the Achaemenid list jumps from `Xerxes I [reign] 486BC..465BC` straight
to `Darius III [reign] 336BC..330BC`, skipping 130 years. Absent: Bardiya/Smerdis,
**Artaxerxes I**, Xerxes II, Sogdianus, **Darius II**, **Artaxerxes II** (Cunaxa, the
Anabasis), **Artaxerxes III** (as Great King — he appears only as `Artaxerxes III (as
pharaoh)` under Egypt's 31st Dynasty), Arses/Artaxerxes IV. Also absent: the satrapy system,
the Royal Road, the Behistun inscription, the Greco-Persian Wars as Persian-side entities.
**Where it belongs:** `Achaemenid Empire [era] 550BC..330BC (foun)`.
**Why it matters:** the gap covers the period the Greek sources are actually about, so the
Achaemenids appear only as founders and as Alexander's victim.
**Rough dates:** 465–330 BC.

### Armenia, Pontus, Pergamon and post-Hellenistic Anatolia
**Severity:** high
**What is missing:** **Armenia does not exist in the dataset in any form.** No Kingdom of
Armenia, no Orontid, **Artaxiad** (Tigranes the Great), Arsacid Armenian or **Bagratid**
dynasty; no Tiridates III and the 301 CE adoption of Christianity as a state religion (the
first anywhere); no Cilician Armenia. Also absent from Anatolia: **Kingdom of Pontus**
(Mithridates VI and the Mithridatic Wars), **Pergamon and the Attalids**, **Bithynia**,
**Cappadocia**, **Commagene**, **Caria** and **Lycia**, the **Galatians**, the **Ionian
League**. `Phrygia`, `Urartu` and `Lydia` exist as bare eras with no rulers — no **Midas**,
no Sarduri I/II, Argishti I or Rusa I, no **Gyges, Alyattes or Croesus** (though
`The Invention of Coinage` is attributed to Lydia).
**Where it belongs:** `Anatolia [region] —..— (foun)` and its children `Phrygia [era]
900BC..540BC (inte)`, `Urartu [era] 840BC..590BC (inte)`, `Lydia [era] 680BC..546BC (inte)`.
**Why it matters:** Anatolia between the Hittites and the Ottomans is a blank in this
dataset apart from four unpopulated labels. And a world-history dataset with no Armenia at
all has no first Christian state and no Armenian plateau as an actor in Roman–Persian,
Byzantine–Arab or Ottoman–Safavid history.
**Rough dates:** 850 BC – 1375 CE.

### The Crusades, the Ayyubids and the Egyptian Mamluk Sultanate
**Severity:** high
**What is missing:** the word "crusade" appears nowhere. Absent: the **First Crusade**
(1096–99) and the later numbered crusades, the **Kingdom of Jerusalem**, County of Edessa,
Principality of Antioch, County of Tripoli, the **Fourth Crusade and the sack of
Constantinople (1204)** with its successor states (**Latin Empire**, **Empire of Nicaea**,
**Empire of Trebizond**, Despotate of Epirus), the **Knights Templar**, **Hospitaller** and
**Teutonic Order**. Also absent: the **Zengids** and Nur ad-Din, the **Ayyubid Sultanate**
and **Saladin**, the Battle of Hattin (1187), the **Mamluk Sultanate of Egypt and Syria**
(1250–1517 — the only "Mamluk" entry in the dataset is `Mamluk (Slave) Dynasty [period]
1206..1290` under the Delhi Sultanate), Baybars, **Ain Jalut (1260)**, Qutuz, Qalawun,
Qaitbay. The **Sultanate of Rum** is absent, so is the **Battle of Manzikert (1071)** —
though `Romanos IV Diogenes [reign] 1068..1071` is present, which is a reign defined
entirely by a battle the dataset does not contain.
**Where it belongs:** `Middle Ages [era] 500..1500 (foun)` /
`Multi-Regional Empires [era] 550BC..1997 (foun)`; the Levantine states under
`Mesopotamia & Levant [region] —..— (foun)`; the Egyptian sultanates under
`Nile Valley & Northeast Africa [region] —..— (foun)`, whose Egypt coverage stops at
`Roman & Byzantine Egypt [era] 30BC..641`.
**Why it matters:** this is the single largest connected hole in the dataset. Two centuries
of Latin–Muslim–Byzantine interaction, the polity that stopped the Mongols, and the state
that ruled Egypt for 267 years are all absent. Egypt's timeline has a **1,200-year void
between 641 and the modern era** — no Tulunids, Ikhshidids, Ayyubids, Mamluks or Ottoman
Egypt; the Fatimids appear only as a global entry.
**Rough dates:** 969–1517.

### Second Temple Judaea: Hasmoneans, Herodians, the revolts
**Severity:** medium
**What is missing:** `Kingdoms of Israel and Judah [era] 1050BC..586BC` has only `David` and
`Solomon`. Absent: the division of the kingdom, Jeroboam, Omri, **Ahab**, Jehu, Hezekiah,
Josiah, the Assyrian destruction of Samaria (722 BC), the fall of Jerusalem (586 BC), the
**Babylonian Exile** and the Return. And there is no Judaean entity after 586 BC at all: no
Yehud province, no **Maccabean Revolt**, no **Hasmonean dynasty** (Judas Maccabeus, John
Hyrcanus, Alexander Jannaeus, Salome Alexandra), no **Herod the Great** or Herodian dynasty,
no Roman province of Judaea, no **First Jewish–Roman War (66–73)** or destruction of the
Second Temple, no **Bar Kokhba revolt (132–136)**.
**Where it belongs:** `Kingdoms of Israel and Judah [era] 1050BC..586BC (foun)`.
**Why it matters:** the dataset carries Christianity's later institutional history nowhere
and its origin context not at all; the political matrix of Second Temple Judaism is missing
entirely, which also removes the setting for the Gospels and for rabbinic Judaism.
**Rough dates:** 930 BC – 136 CE.

### Ottoman sultans: two out of thirty-six
**Severity:** high
**What is missing:** `Ottoman Empire` carries `Mehmed II the Conqueror` and
`Suleiman I the Magnificent` and nothing else. Absent: **Osman I**, Orhan, **Murad I**
(Kosovo), **Bayezid I** and Ankara (1402), the Interregnum, Mehmed I, **Murad II**,
Bayezid II, **Selim I** (Chaldiran, the caliphal title), Selim II, Murad III, Ahmed I,
**Murad IV**, Mehmed IV, Ahmed III, **Mahmud II**, Abdulmejid I, **Abdulhamid II**,
Mehmed VI. Absent as events: the **Fall of Constantinople (1453)** — nowhere in the dataset,
though `Constantine XI Palaiologos [reign] 1449..1453` is present — **Chaldiran (1514)**,
Mohács (1526), the **Sieges of Vienna (1529 and 1683)**, **Lepanto (1571)**, Karlowitz (1699),
the **Tanzimat**, the Young Turk Revolution, the Armenian Genocide, the abolition of the
Sultanate and Caliphate (1922–24). Structurally, the Ottomans sit under
`Global & Multi-Regional`, which means West Asia's own count excludes its longest-lived state.
**Where it belongs:** `Ottoman Empire [era] 1299..1922 (foun)`.
**Why it matters:** 1453 not existing as an event is the clearest single symptom in the
dataset. Two sultans cannot carry six centuries, and the Ottoman–Safavid and
Ottoman–Habsburg rivalries have no Ottoman-side entities to hang on.
**Rough dates:** 1299–1922.

### Caliphs: one named caliph in three caliphates
**Severity:** high
**What is missing:** `Rashidun Caliphate`, `Umayyad Caliphate` and `Fatimid Caliphate` have
no children at all; `Abbasid Caliphate` has exactly one, `Harun al-Rashid`. Absent: **Abu
Bakr, Umar, Uthman, Ali**; the **First and Second Fitnas**; **Muawiya I**, Abd al-Malik,
al-Walid I, Umar II, the Battle of Karbala (680) and the **Sunni–Shia division** as an entity;
**Abu al-Abbas**, **al-Mansur**, al-Ma'mun and the **House of Wisdom**, al-Mutawakkil, the
Samarra anarchy, the Buyid takeover, the **Mongol sack of Baghdad (1258)**. Also absent:
the **Emirate and Caliphate of Córdoba** (see Europe), the **Umayyad conquests** as events,
**Yarmouk (636)** and **Qadisiyyah (636)** — though `Arab Conquest of Iran [event] 633..651`
covers the Persian side, and the Islamic conquest of Egypt is implied only by
`Roman & Byzantine Egypt [era] 30BC..641`.
**Where it belongs:** `Rashidun Caliphate [era] 632..661 (foun)`,
`Umayyad Caliphate [era] 661..750 (foun)`, `Abbasid Caliphate [era] 750..1258 (foun)`,
`Fatimid Caliphate [era] 909..1171 (inte)`.
**Why it matters:** Islam has a founder (`Prophet Muhammad`) and one Abbasid caliph.
The succession dispute that produced the Sunni–Shia split — arguably the most consequential
political event of the seventh century — is not representable.
**Rough dates:** 632–1258.

### Arabia and the Gulf after Saba
**Severity:** medium
**What is missing:** `Pre-Islamic Arabia` has `Dilmun`, `Umm an-Nar`, `Wadi Suq`, `Saba`,
`The Incense Route` and `The Nabataeans`. Absent: **Maʿin**, **Qataban**, **Hadhramaut**,
**Himyar** (which absorbed Saba and converted to Judaism), the Aksumite conquest of Yemen,
**Kinda**, the **Ghassanids** and **Lakhmids** (the Byzantine and Sasanian Arab client
kingdoms), Palmyra and **Zenobia**, Hatra, Characene, Osroene. Later: no **Ibadi Imamate of
Oman**, no **Qarmatians**, no Rashidi/**Saudi states** or Wahhabi movement, no Sharifate of
Mecca.
**Where it belongs:** `Pre-Islamic Arabia [era] 3000BC..610 (inte)` and
`Arabia [region] —..— (foun)`.
**Why it matters:** without Himyar and the Ghassanid/Lakhmid clients, the political Arabia
that Islam emerged into is absent, and Arabia looks like caravan routes plus a prophet.
**Rough dates:** 800 BC – 1932 CE.

---

## Central Asia and the steppe

### The Huns, and the western steppe generally
**Severity:** high
**What is missing:** **the Huns and Attila do not appear anywhere in the dataset** (the only
"Hun" matches are Egypt's `Huni` and India's `Shunga`). Also entirely absent: the **Avar
Khaganate** (no match in the tree — the seven "avar" hits are Indian names like
`Devavarman`), the **Pannonian Avars**, the **Sarmatians**, the **Alans**, the **Pechenegs**,
the **Cumans/Kipchaks**, the **Khazar Khaganate**, **Volga Bulgaria**, the **Rouran
Khaganate**, the **Wusun**, the **Yuezhi**, **Kangju**, the **Tuoba/Xianbei** as a named
people.
**Where it belongs:** `Eurasian Steppe [region] —..— (foun)`, which currently holds only
`Scythians`, `Saka`, `Xiongnu Empire`, `First Turkic Khaganate`, `Second Turkic Khaganate`
and `Uyghur Khaganate`.
**Why it matters:** the dataset has `Migration Period [era] 376..800` and the full Roman
collapse sequence down to `Romulus Augustulus`, but not the people whose arrival caused it.
The Khazars' absence also removes the power that blocked the Arab advance north of the
Caucasus and shaped early Rus.
**Rough dates:** 370–1240.

### Post-Timurid Central Asia: Kazakhs, Uzbeks, Dzungars, the Tatar khanates
**Severity:** high
**What is missing:** the **Kazakh Khanate** (1465–1847; Janybek and Kerei, Kasym Khan,
Ablai Khan, the Zhuz division), the **Dzungar Khanate** (1634–1758, Galdan Boshugtu, the
Qing extermination campaign), the **Shaybanid** dynasty by name and **Abu'l-Khayr Khan** /
Muhammad Shaybani (`Khanate of Bukhara [era] 1501..1920` exists but has no children and no
dynastic subdivision into Shaybanid/Janid/Manghit), the **Nogai Horde**, the **Crimean
Khanate** (1441–1783 — absent, despite three centuries of raiding into Poland-Lithuania and
Muscovy), the **Khanate of Kazan**, **Astrakhan**, **Sibir**, the **Kalmyk Khanate**,
**Moghulistan** and the **Yarkent Khanate**, the **Northern Yuan** and the **Oirats**. Also
absent for Afghanistan: the **Hotak dynasty** and the **Durrani Empire** (1747–1823, Ahmad
Shah Durrani) — Afghanistan has no polity in the dataset at any date. Timurid successors
**Shah Rukh** and **Ulugh Beg** are also absent.
**Where it belongs:** `Central Asia [region] —..— (foun)` and
`Timurid Empire [era] 1370..1507 (foun)`.
**Why it matters:** Central Asia 1500–1900 exists in the dataset only as three static khanate
labels plus `Russian Conquest of Central Asia`. The Kazakh–Dzungar wars, the Qing destruction
of the Dzungars, and the Tatar khanates that Muscovy conquered on its way to becoming Russia
are all unrepresentable — and the Durrani gap means Afghanistan appears nowhere as a state.
**Rough dates:** 1441–1876.

### Mongol Empire and Golden Horde have almost no rulers
**Severity:** medium
**What is missing:** `Mongol Empire` lists `Genghis Khan`, `Ögedei Khan` and `Möngke Khan`.
Absent: **Tolui**, **Güyük Khan**, the regency of Töregene, **Batu Khan**, **Hulagu**,
Ariq Böke and the Toluid Civil War. `Golden Horde [period] 1242..1502` and
`Ilkhanate [period] 1256..1335` and `Chagatai Khanate [period] 1226..1687` have **no children
at all** — no Berke, Öz Beg, Mamai or **Tokhtamysh**; no Abaqa, Ghazan or Öljaitü. Absent as
events: the Mongol invasion of Rus' (1237–40), the sack of Baghdad (1258), Ain Jalut (1260),
the two failed invasions of Japan (1274, 1281), Kulikovo (1380).
**Where it belongs:** `Mongol Empire [era] 1206..1368 (foun)` and its children
`Golden Horde [period] 1242..1502 (inte)`, `Ilkhanate [period] 1256..1335 (inte)`.
**Why it matters:** the largest contiguous land empire in history is three khans and four
undivided labels. The Golden Horde in particular is the central fact of Russian and Ukrainian
history for 240 years and has no internal structure here at all.
**Rough dates:** 1206–1502.

### Sogdiana and Bactria as polities
**Severity:** medium
**What is missing:** `Sogdia [era] 500BC..750` exists as one undivided 1,250-year label with
no children — no Achaemenid satrapy of Sogdiana, no Spitamenes, no Sogdian merchant network,
no Sogdian letters, no Devashtich and the Arab conquest. The **Greco-Bactrian Kingdom** is
absent as a polity (Bactria appears only as `Bactria-Margiana Archaeological Complex` and as
`Demetrius I of Bactria` filed under South Asia's Indo-Greek Kingdoms), as are Diodotus I and
Euthydemus I. `Kushan Empire` has one reign, `Kanishka the Great` — absent: Kujula
Kadphises, Vima Kadphises, Huvishka, Vasudeva I. `Hephthalites [era] 440..560` has no
children — no Toramana or Mihirakula (who are also missing from the South Asian side).
**Where it belongs:** `Central Asia [region] —..— (foun)`, specifically
`Sogdia [era] 500BC..750 (foun)`, `Kushan Empire [era] 30..375 (foun)`,
`Hephthalites [era] 440..560 (foun)`.
**Why it matters:** these are the states that carried Buddhism to China and ran the Silk
Road; the dataset has them as labels with no internal history, so the transmission mechanism
is invisible.
**Rough dates:** 250 BC – 750 CE.

---

## Oceania

### Rapa Nui is absent entirely
**Severity:** high
**What is missing:** **no Rapa Nui, no Easter Island, no moai** anywhere in the dataset
(verified: the only "eastern" matches are Eastern Zhou/Han/Europe/North America). Absent:
the settlement of Rapa Nui (c. 1200), the ahu and **moai** construction sequence, the
**Rano Raraku** quarry, the deforestation/collapse debate, the **huri moai** period, the
**birdman (tangata manu) cult**, the 1862–63 Peruvian slave raids, the 1888 Chilean
annexation.
**Where it belongs:** `Polynesia [region] —..— (foun)`.
**Why it matters:** Rapa Nui is the single most-discussed case study in the literature on
island societies, ecological limits and monument-building — the standing example in every
collapse debate — and it does not exist here.
**Rough dates:** 1200–1888.

### Samoa, Tahiti and the rest of Polynesia
**Severity:** high
**What is missing:** **Samoa in any form** — no **Tui Manuʻa**, no Tui Aʻana or Tui
Atua, no **Malietoa**, no Samoan civil wars, no German/American partition of 1899. Also
absent: **Tahiti and the Society Islands** (the **Pōmare dynasty**, Pōmare I–V, the ariʻi
system, the 1880 French annexation), the **Marquesas**, the **Cook Islands**, **Tuvalu**,
**Niue**, and — despite the brief's expectation — **Māori iwi** as entities (`Māori Aotearoa
[era] 1250..1840` has no children: no Ngāpuhi, Waikato-Tainui, Ngāti Toa, Ngāi Tahu, no
Te Rauparaha, no **Kīngitanga / Māori King movement** and Pōtatau Te Wherowhero, no **New
Zealand Wars**, and no **Treaty of Waitangi** as an event — it survives only inside the name
`New Zealand (post-Waitangi)`). The **Moriori** of Rēkohu/Chatham Islands are absent.
`Tuʻi Tonga Empire [era] 950..1865` has no children — no Tuʻi Tonga kings, no
**Tuʻi Haʻatakalaua** or **Tuʻi Kanokupolu** lines, no Taufaʻāhau/George Tupou I.
`Kingdom of Hawaii` has `Kamehameha I` and `Queen Liliʻuokalani` only — absent: Kamehameha
II–V, Lunalilo, **Kalākaua**, the **abolition of the kapu system (1819)**, the 1893
overthrow and 1898 annexation as events.
**Where it belongs:** `Polynesia [region] —..— (foun)`, `Tuʻi Tonga Empire [era]
950..1865 (inte)`, `Māori Aotearoa [era] 1250..1840 (foun)`,
`Kingdom of Hawaii [era] 1795..1898 (foun)`.
**Why it matters:** Oceania's 27 entities include four for Australian prehistory and three
for modern Australia/NZ statehood, leaving roughly a dozen for the whole Pacific. Polynesia's
three great archipelagic polities (Tonga, Hawaiʻi, Tahiti) are one label, two labels and
nothing.
**Rough dates:** 950–1899.

### Melanesia and Micronesia are two entries each
**Severity:** medium
**What is missing:** `Melanesia` holds `Lapita Culture` and `Fijian Chiefdoms [era]
500..1874` — with no **Bau**, no **Cakobau**, no Fijian cession to Britain as an event.
Absent: **Vanuatu** (Roi Mata's domain, the Kuwae eruption c. 1452), **New Caledonia** and the
Kanak, the **Solomon Islands**, **Bougainville**, **New Guinea** as a polity or peoples (the
Kuk agricultural sequence appears only as `New Guinea Highlands [period] 8271BC..2031BC` under
global Neolithic Transition), **German New Guinea** and Papua. `Micronesia` holds only
`Saudeleur Dynasty (Nan Madol)` and `Yapese Empire (Sawei)`; absent: the **Chamorro** and
the **Latte period** of the Marianas, **Palau**, **Kiribati**, **Nauru**, the **Marshall
Islands** and their stick charts, the Spanish/German/Japanese administrations.
**Where it belongs:** `Melanesia [region] —..— (foun)` and `Micronesia [region] —..— (inte)`.
**Why it matters:** the two most populous and linguistically diverse parts of Oceania have
four entities between them, one of which is an archaeological culture.
**Rough dates:** 1500 BC – 1975 CE.

---

## Southeast Asia

### Burma before Pagan and beside Pagan; Arakan; the Mon
**Severity:** medium
**What is missing:** the **Pyu city-states** (c. 200 BC – 1050 CE, Sri Ksetra, Halin,
Beikthano — the first Buddhist states in Burma), the **Mon kingdoms** and **Hanthawaddy
Pegu** (1287–1552, Razadarit, Queen Shin Sawbu, Dhammazedi), **Arakan / Mrauk U** (1429–1785),
**Lanna** (Chiang Mai, 1292–1775, Mangrai). `Pagan Kingdom [era] 849..1297` has no rulers —
no Anawrahta, Kyansittha or Narathihapate; `Toungoo Dynasty` has none — no Tabinshwehti or
**Bayinnaung**; `Konbaung Dynasty` has none — no **Alaungpaya**, Hsinbyushin or Bodawpaya,
and no Anglo-Burmese Wars.
**Where it belongs:** `Mainland Southeast Asia [region] —..— (foun)`,
`Pagan Kingdom [era] 849..1297 (inte)`, `Toungoo Dynasty [era] 1510..1752 (foun)`,
`Konbaung Dynasty [era] 1752..1885 (foun)`.
**Why it matters:** the Burmese polity list is complete at era level and empty at ruler
level, and the Mon and Arakanese — the states Burma repeatedly conquered — are missing, so
Burmese history reads as a single unopposed lineage.
**Rough dates:** 200 BC – 1885 CE.

### Thai and Khmer rulers; Angkor's founder
**Severity:** medium
**What is missing:** `Khmer Empire (Angkor)` has two kings, `Suryavarman II` and
`Jayavarman VII`. Absent: **Jayavarman II**, who founded the empire in the very year the era
node starts (802), plus Indravarman I, **Yasovarman I**, Rajendravarman II, Jayavarman IV,
and the 1431 Ayutthayan sack. `Sukhothai Kingdom` has no rulers — no **Ramkhamhaeng** and no
Thai script. `Ayutthaya Kingdom` has none — no Ramathibodi I, Trailokanat, **Naresuan**,
Narai, and no 1767 Burmese destruction as an event. `Rattanakosin (Chakri Dynasty)` has none
— no Rama I, **Rama IV Mongkut**, **Rama V Chulalongkorn** (whose reforms are why Siam was
never colonised), Rama IX. `Champa` and `Srivijaya` likewise have no rulers.
**Where it belongs:** `Khmer Empire (Angkor) [era] 802..1431 (foun)`,
`Sukhothai Kingdom [era] 1238..1438 (foun)`, `Ayutthaya Kingdom [era] 1351..1767 (inte)`,
`Rattanakosin (Chakri Dynasty) [era] 1782..— (inte)`.
**Why it matters:** Vietnam's dynastic sequence is fully articulated (`Ngô`, `Đinh`,
`Early Lê`, `Lý`, `Trần`, `Hồ`, Ming occupation, `Later Lê` with `Trịnh`/`Nguyễn` lords,
`Mạc`, `Tây Sơn`, `Nguyễn`), which makes the empty Thai and Khmer ruler lists look like an
uneven authoring effort rather than a judgement.
**Rough dates:** 802–1910.

### The spice sultanates and modern Southeast Asia
**Severity:** medium
**What is missing:** **Ternate** and **Tidore** (the Maluku clove sultanates the entire
European spice trade was built to reach), **Gowa-Tallo / Makassar**, **Johor**, **Banten**,
**Pattani**, **Maguindanao**, the **Sulu**-adjacent Rajahnate polities, **Sunda /
Pajajaran**, **Bali** and the Gelgel/Klungkung line, the **Sailendra** dynasty by name
(`Medang Kingdom [era] 732..1006` covers the period but the dynasty and Borobudur's builders
are unnamed), **Gajah Mada** (`Majapahit Empire` has only `Hayam Wuruk`). Modern: after
`Spanish Philippines [era] 1565..1898` **there is no Philippine entity at all** — no
Philippine Revolution, Rizal, Aguinaldo, First Philippine Republic, Philippine–American War,
US colonial period or Republic of the Philippines. Also absent: **British Malaya**, the
Federated Malay States, the **Federation of Malaysia**, **Singapore**, **Timor-Leste**,
independent **Myanmar** after `British Burma [era] 1885..1948`, independent **Laos** and
**Cambodia**, the **Khmer Rouge**. Prehistory: **Đông Sơn** and **Sa Huỳnh** cultures are
absent despite `Ban Chiang`, `Man Bac` and `Da But` being present.
**Where it belongs:** `Maritime Southeast Asia [region] —..— (foun)`,
`Majapahit Empire [era] 1293..1527 (foun)`, `Southeast Asian Prehistory [era] 44051BC..500BC (foun)`.
**Why it matters:** Indonesia has a successor entity (`Republic of Indonesia`) and the
Philippines, Malaysia, Singapore, Myanmar, Laos, Cambodia and Timor-Leste have none — the
region ends at decolonisation for six of eight countries. And the Moluccan sultanates'
absence removes the actual destination of the Age of Exploration the dataset covers at
length.
**Rough dates:** 500 BC – present.

---

## The Americas

The brief's Andean and Mesoamerican checklist is in better shape than expected. Present and
correctly placed: `Norte Chico / Caral`, `Chavín`, `Nazca`, `Moche`, `Tiwanaku`,
`Wari Empire`, `Chimú (Chimor)`, `Mapuche / Araucanía`, `Mississippian Culture`,
`Ancestral Puebloan`, `Haudenosaunee Confederacy`, `Comanche Empire`, `Purépecha Empire`,
`Zapotec (Monte Albán)`, `Toltec Empire`. Of that list, three are genuinely absent —
**Muisca**, **Hohokam** and **Mixtec** — and the deeper problems are elsewhere.

### Muisca, Hohokam, Mixtec, and the intermediate cultures
**Severity:** medium
**What is missing:** the **Muisca Confederation** (zipa of Bacatá, zaque of Hunza, the
Eldorado myth, 1537 conquest) — `Intermediate Area & Caribbean [region]` contains only
`Taíno Chiefdoms`, so Colombia, Panama and Costa Rica have no polity at all, and the Chibchan
world, **Quimbaya**, **Tairona**, **Cocle** and **Diquís** (stone spheres) are absent.
**Hohokam** (canal irrigation in the Sonoran desert, 300–1500) is absent, as are **Mogollon**,
**Mimbres**, **Fremont** and **Casas Grandes/Paquimé**. **Mixtec** (the Ñuu Dzaui city-states,
the codices, Eight Deer Jaguar Claw) is absent, as are **Huastec** and Epi-Olmec/Izapa. In
the Andes: **Paracas**, **Recuay**, **Lambayeque/Sicán**, **Cañari**, **Chachapoya**,
**Diaguita/Calchaquí**. In lowland South America: **Tupí** and **Guaraní**, **Charrúa**,
the Llanos de Mojos earthworks, the Casarabe culture.
**Where it belongs:** `Intermediate Area & Caribbean [region] —..— (inte)`,
`North America [region] —..— (foun)`, `Mesoamerica [region] —..— (foun)`,
`Amazon & Southern Cone [region] —..— (inte)`.
**Why it matters:** the Muisca were one of the four largest polities Spain encountered in
the Americas, alongside the Aztecs, Inca and Tarascans, and the other three are present.
**Rough dates:** 300 BC – 1600 CE.

### Adena, Hopewell, and the Arctic
**Severity:** medium
**What is missing:** **Adena** (800 BC – 100 CE) and **Hopewell** (100 BC – 500 CE) — the
mound-building traditions between `Poverty Point [period] 1751BC..1151BC` and
`Mississippian Culture [era] 800..1600`, both absent, leaving a 1,000-year hole in eastern
North America. Also absent: the entire **Arctic** — no **Paleo-Eskimo/Arctic Small Tool
tradition**, no **Dorset culture**, no **Thule culture** (the Inuit ancestors, c. 1000–1600),
no Inuit, Yupik or Aleut, no **Norse Greenland or Vinland/L'Anse aux Meadows** (the first
European contact with the Americas, absent while `Columbus reaches the Americas [event]
1492..1492` is present).
**Where it belongs:** `North America [region] —..— (foun)` and
`Americas Prehistory [era] 34051BC..500 (foun)`.
**Why it matters:** the dataset argues for deep prehistory deliberately (White Sands,
Pre-Clovis, Monte Verde) and then skips the two Woodland traditions that explain how Cahokia
became possible, plus the whole Arctic, which is the one region where the archaeological
sequence runs unbroken into a living people.
**Rough dates:** 2500 BC – 1600 CE.

### North American nations after contact
**Severity:** medium
**What is missing:** `North America` has `Haudenosaunee Confederacy` and
`Comanche Empire` and no other Indigenous polity after 1492. Absent: the **Powhatan
Confederacy**, the **Wendat/Huron Confederacy**, the **Cherokee Nation**, the **Muscogee
(Creek) Confederacy**, the **Lakota/Očhéthi Šakówiŋ**, the **Blackfoot Confederacy**, the
**Navajo (Diné)** and **Apache**, the **Pueblo Revolt of 1680**, **Tecumseh's confederacy**,
the **Indian Removal Act and Trail of Tears**, the **Métis** and the Red River Resistance.
**Where it belongs:** `North America [region] —..— (foun)`, alongside
`Colonial North America [era] 1492..1783 (foun)`.
**Why it matters:** two Indigenous polities across three centuries of contact means
colonisation appears as an uncontested process; `Comanche Empire` is tagged `spec` and
`Haudenosaunee` `inte`, so even the two present entries are low-tier.
**Rough dates:** 1500–1890.

### The conquest itself, and Latin America after independence
**Severity:** high
**What is missing:** **Cortés and Pizarro appear nowhere in the dataset**, and neither does
the **fall of Tenochtitlan (1521)** or the **capture of Atahualpa at Cajamarca (1532)** as
events — `Aztec Empire [era] 1428..1521` and `Atahualpa [reign] 1532..1533` simply stop.
Also absent: the **Viceroyalty of New Granada**, the **Viceroyalty of Río de la Plata**,
**Portuguese/colonial Brazil** in any form (no Brazil entity at all — no captaincies, no
Bahia sugar economy, no Minas Gerais gold, no **Empire of Brazil**, no Pedro I or Pedro II,
no 1888 abolition), the **Haitian Revolution** and Toussaint Louverture and Dessalines, the
**Spanish American wars of independence** with Bolívar, San Martín, Hidalgo and Sucre, the
**Mexican Revolution**, and **Canada** in any form (no New France as a distinct entity, no
Hudson's Bay Company, no 1867 Confederation, no Dominion of Canada). The United States has
exactly one child, `Civil War & Reconstruction` — no American Revolution or Revolutionary
War, no Constitution, no Louisiana Purchase, no Westward Expansion, no presidents.
**Where it belongs:** `Americas [region]` — specifically
`Viceroyalty of New Spain [era] 1521..1821 (foun)`,
`Viceroyalty of Peru [era] 1542..1824 (inte)`,
`Colonial North America [era] 1492..1783 (foun)`, `United States [era] 1776..— (foun)`.
**Why it matters:** the Americas' 74 entities are heavily pre-Columbian; the post-1500
hemisphere is four colonial containers and two modern states. Brazil — the largest country
in the region — and Canada are absent entirely, and the two conquests that ended the two
largest indigenous empires are not events.
**Rough dates:** 1519–1917.

---

## Africa

Africa's 271 is real but very unevenly spent: African Prehistory (~40 entries) plus Ancient
Egypt's near-complete pharaoh list (~150 reigns) plus Kush/Aksum account for the great
majority. From the brief's checklist, present: `Kanem–Bornu Empire`, `Oyo Empire`,
`Kingdom of Dahomey`, `Ashanti Empire`, `Kingdom of Kongo`, `Lunda Empire`, `Luba Empire`,
`Swahili Coast City-States`, `Ethiopian Empire`. Absent: **Wadai, Darfur, Sennar, Ife,
Ndongo, Buganda, Bunyoro, Rwanda, the Zagwe, Merina** — nine of nineteen.

### The Great Lakes kingdoms
**Severity:** high
**What is missing:** **Buganda** (with its kabaka line — Kintu, Mutesa I, Mwanga II),
**Bunyoro-Kitara** (and the Chwezi/Bito traditions, Kabalega), **Rwanda / the Nyiginya
kingdom** (Ruganzu Ndori, Rwabugiri, the mwami institution), **Burundi**, **Ankole**,
**Toro**, **Karagwe**, **Buhaya**. `East Africa [region]` currently contains exactly two
entities: `Swahili Coast City-States [era] 900..1500` and `Sultanate of Zanzibar [era]
1856..1964`.
**Where it belongs:** `East Africa [region] —..— (foun)`.
**Why it matters:** the interlacustrine kingdoms were among the most densely populated and
most centralised states in precolonial Africa, and they are the direct cause of the political
structures of modern Uganda, Rwanda and Burundi. Two entities cannot cover East Africa.
**Rough dates:** 1300–1900.

### Madagascar
**Severity:** high
**What is missing:** **Madagascar does not appear in the dataset at all** — no Austronesian
settlement of Madagascar (the longest prehistoric ocean migration on record, and directly
relevant to `The Austronesian Expansion [era] 3551BC..1130BC` under Southeast Asia), no
**Kingdom of Imerina / Merina**, no **Andrianampoinimerina**, **Radama I** or **Ranavalona I**,
no Sakalava or Betsimisaraka kingdoms, no French conquest of 1895.
**Where it belongs:** `Africa [region] —..— (foun)` — it has no sub-region that would hold it
(`Central Africa`, `East Africa`, `Nile Valley & Northeast Africa`, `North Africa`,
`Southern Africa`, `West Africa & Sahel`).
**Why it matters:** the Merina unified an island the size of France in the early nineteenth
century, and the Austronesian settlement of Madagascar is the single strongest piece of
evidence for the scale of the Austronesian expansion the dataset already covers.
**Rough dates:** 500–1897.

### Christian and Islamic Nubia and the Horn
**Severity:** medium
**What is missing:** the Nubian Christian kingdoms — **Nobatia**, **Makuria** (and the baqt
treaty with Egypt that held for six centuries) and **Alodia** — are absent, leaving a
1,200-year gap between `Kingdom of Kush [era] 2500BC..350` / `Meroitic Phase` and the modern
Sudan. Also absent: the **Funj Sultanate of Sennar**, **Darfur (the Keira sultanate)**,
**Wadai**, **Bagirmi**, the **Shilluk**. In the Horn: the **Zagwe dynasty** and the
**Lalibela** rock churches; the **Solomonic restoration of 1270** as a named dynasty
(`Ethiopian Empire [era] 1270..1974` starts precisely there but has only three reigns —
`Ezana` is filed under Aksum, then nothing until `Menelik II` in 1889); Amda Seyon I,
Zara Yaqob, Tewodros II, Yohannes IV; the **Adal Sultanate** and Ahmad ibn Ibrahim
al-Ghazi (Gragn) and the Ethiopian–Adal war; **Ifat**; the **Ajuran Sultanate** and the
Somali polities.
**Where it belongs:** `Nile Valley & Northeast Africa [region] —..— (foun)`,
`Ethiopian Empire [era] 1270..1974 (foun)`.
**Why it matters:** Ethiopia has three named rulers across 700 years and Nubia has none after
350 CE, so the two oldest continuous Christian polities outside Europe are near-invisible,
and the Ethiopian–Adal war — the conflict that drew in both Ottoman and Portuguese forces —
cannot be told.
**Rough dates:** 350–1889.

### The Maghreb between Carthage and the Alaouites
**Severity:** medium
**What is missing:** `North Africa [region]` holds only `Carthaginian Empire`,
`Almoravid Empire`, `Almohad Caliphate` and `Alaouite Morocco`. Absent: **Numidia** and
**Masinissa**, **Mauretania**, the **Garamantes**, Roman Africa and the Vandal kingdom, the
**Aghlabids**, **Rustamids**, **Idrisids**, **Zirids**, **Hammadids**, the **Marinids**,
**Hafsids**, **Zayyanids**, the **Wattasids** and **Saadi dynasty**, the Barbary regencies
of Algiers, Tunis and Tripoli, and the **French conquest of Algeria** with Abd al-Qadir.
**Where it belongs:** `North Africa [region] —..— (foun)`.
**Why it matters:** four entities cover 2,700 years of the Maghreb, with a 900-year gap
between Carthage and the Almoravids and another between the Almohads and 1631.
**Rough dates:** 200 BC – 1912 CE.

### West African states beyond the four big empires
**Severity:** medium
**What is missing:** **Ife** (the ancestor-polity of Benin and Oyo, and the source of the
bronze heads — Benin and Oyo are both present, Ife is not), the **Hausa city-states** (Kano,
Katsina, Zazzau and the Kano Chronicle), the **Mossi kingdoms** (Ouagadougou, Yatenga), the
**Jolof/Wolof Empire** and Cayor, Baol and Waalo, **Kaabu**, the **Kingdom of Nri** and Igbo
polities, **Nupe**, **Dagbon**, the **Fante Confederacy**, **Bamana Ségou**, the **Massina
Empire**, the **Toucouleur Empire** of al-Hajj Umar Tall, the **Wassoulou Empire** of Samori
Ture, the **Bornu–Kanem sub-dynasties** (Sayfawa) and Idris Alooma.
**Where it belongs:** `West Africa & Sahel [region] —..— (foun)`.
**Why it matters:** the Sahel appears as a clean succession of four imperial hegemons
(Ghana, Mali, Songhai, Sokoto), which is exactly the simplified story a specialist would flag
— the forest-belt and Hausa polities that were the actual centres of population and trade are
missing.
**Rough dates:** 1000–1898.

### Southern Africa after Great Zimbabwe, and colonial/modern Africa
**Severity:** high
**What is missing:** `Southern Africa [region]` holds `Great Zimbabwe`, `Mutapa Empire`
and `Zulu Kingdom` only. Absent: **Mapungubwe** (the predecessor of Great Zimbabwe), the
**Rozvi Empire**, **Torwa/Butua**, the **Maravi** confederacy, **Barotseland/Lozi**, the
**Mfecane** as an era, the **Ndebele** of Mzilikazi, the **Basotho** and **Moshoeshoe I**,
the **Swazi**, the **Xhosa** and the Cape Frontier Wars, the **Griqua**. Colonial and modern:
no **Dutch Cape Colony** or British Cape Colony, no **Great Trek** or Boer republics, no
**Anglo-Zulu War (1879)**, no **South African War (1899–1902)**, no Union of South Africa, no
**apartheid** and no **Mandela**. More broadly, Africa's only twentieth-century entities are
`Scramble for Africa`, `Berlin Conference`, `Decolonization` (all filed under Global),
`Sultanate of Zanzibar`, `Haile Selassie` and `Alaouite Morocco` — there is no **Muhammad Ali
Pasha**, no Khedivate of Egypt, no **Suez Canal**, no Mahdist Sudan, no Nasser, no
independent African state after 1960 anywhere in the dataset.
**Where it belongs:** `Southern Africa [region] —..— (foun)`,
`Nile Valley & Northeast Africa [region] —..— (foun)`, `Scramble for Africa [era] 1881..1914 (foun)`.
**Why it matters:** Africa in the twentieth century — a fifth of humanity, fifty-odd states —
is three global-level abstractions and one emperor. The Mfecane's absence also leaves the
Zulu Kingdom as an isolated event rather than the product of a regional upheaval.
**Rough dates:** 1220–present.

---

## Europe

Europe's 285 is concentrated on Rome (about 100 reigns, down to two-month usurpers), Byzantium
(about 35), plus England, France and the Holy Roman Empire. The Western-centrism the brief
suspected is real but specific: it is **Latin-Western** centrism, and it excludes most of
Catholic and Orthodox Europe east of the Elbe as well as the Mediterranean city-republics.

### Poland, Hungary, Bohemia — three of medieval Europe's largest kingdoms, absent
**Severity:** high
**What is missing:** **Poland does not exist as a polity in the dataset** (the only match is
`Polish-Lithuanian Commonwealth [era] 1569..1795`). Absent: the **Piast dynasty** (Mieszko I,
Bolesław I Chrobry, Casimir III the Great), the **Jagiellonian dynasty**, the Union of Krewo
and Union of Lublin, Jan III Sobieski, the **Partitions of Poland**, the Duchy of Warsaw, the
Second Polish Republic. **Hungary** is absent entirely: no **Árpád dynasty** (Árpád,
**Stephen I**, Béla III, Béla IV and the Mongol invasion of 1241), no Angevin Hungary, no
**Matthias Corvinus**, no **Battle of Mohács (1526)** — even though `The Habsburg Monarchy
[era] 1526..1918` begins in that year, so its start date has no cause in the dataset. **Bohemia**
is absent: no **Přemyslid dynasty**, no Wenceslas, no Ottokar II, no **Charles IV**, no
**Jan Hus** or **Hussite Wars**, no Defenestration of Prague (which likewise makes
`Thirty Years' War [event] 1618..1648` start out of nowhere). Also absent: the
**Grand Duchy of Lithuania** as a polity (Mindaugas, Gediminas, Algirdas, **Vytautas**,
Jogaila, the Battle of Grunwald 1410) — pre-1569 Lithuania, then Europe's largest state by
area, is not in the tree.
**Where it belongs:** `Central Europe [region] —..— (foun)` and
`Eastern Europe [region] —..— (foun)`.
**Why it matters:** three of the four largest Latin-Christian kingdoms of the later Middle
Ages are missing while Rome's 60-day emperors are enumerated. Two existing entities
(`The Habsburg Monarchy`, `Thirty Years' War`) have start dates that the dataset cannot
explain because the Bohemian and Hungarian causes are absent.
**Rough dates:** 966–1918.

### The Balkans: Bulgaria, Serbia, and the Danubian principalities
**Severity:** high
**What is missing:** the **First Bulgarian Empire** (Asparuh, **Krum**, **Boris I** and the
Christianisation, **Simeon I**, Samuel) and the **Second Bulgarian Empire** (Ivan Asen II) —
absent, even though `Basil II the Bulgar-Slayer [reign] 976..1025` is present and named for a
polity the dataset does not contain. **Serbia** absent: no **Nemanjić dynasty**, no Stefan
Nemanja, no **Stefan Dušan** and the Serbian Empire, no **Battle of Kosovo (1389)**. Also
absent: **Croatia** (Tomislav), **Bosnia**, the **Zeta/Montenegro** line, **Wallachia**
(Mircea the Elder, **Vlad III the Impaler**) and **Moldavia** (**Stephen the Great**),
**Great Moravia** (Rastislav, **Cyril and Methodius** and the Glagolitic alphabet — the origin
of Cyrillic, which the dataset's Slavic states would all use), **Greek independence** and the
modern Balkan states.
**Where it belongs:** `Eastern Europe [region] —..— (foun)` and
`Mediterranean [region] —..— (foun)`.
**Why it matters:** the Byzantine reign list is detailed, but every polity Byzantium actually
fought in the Balkans is missing, so Byzantine history reads as an empire with no neighbours.
Cyril and Methodius' absence removes the origin of Slavic literacy.
**Rough dates:** 681–1878.

### Rus' succession and Novgorod
**Severity:** medium
**What is missing:** `Kievan Rus' [era] 862..1240` has exactly one child,
`Vladimir the Great`. Absent: **Rurik**, Oleg, Igor, **Olga of Kiev**, Sviatoslav I,
**Yaroslav the Wise** and the Russkaya Pravda, Vladimir Monomakh, the fragmentation into
appanages, the **Novgorod Republic** (and its veche, and **Alexander Nevsky** — no Neva 1240
or Lake Peipus 1242), **Galicia-Volhynia**, **Vladimir-Suzdal**, the **Mongol sack of Kiev
(1240)** and the Tatar Yoke, the **Battle of Kulikovo (1380)**, Ivan III's "gathering of the
Russian lands", the **Zaporozhian Cossacks** and the Hetmanate. `Grand Duchy of Moscow [era]
1263..1547` has no children at all.
**Where it belongs:** `Kievan Rus' [era] 862..1240 (foun)` and
`Grand Duchy of Moscow [era] 1263..1547 (foun)`.
**Why it matters:** Russia's founding narrative and Novgorod's alternative republican model
are both a single name; the transition from Rus' to Muscovy — the most contested question in
East European historiography — has no entities to argue with.
**Rough dates:** 862–1547.

### Al-Andalus and the Iberian kingdoms
**Severity:** high
**What is missing:** `Reconquista & Iberian Unification [era] 711..1492` is a single
781-year label with **no children**, and it is the only Iberian entity in Europe. Absent on
the Muslim side: the **Emirate of Córdoba** and **Abd al-Rahman I**, the **Caliphate of
Córdoba** and **Abd al-Rahman III**, al-Hakam II and al-Mansur ibn Abi Aamir, the **Taifa
period**, the **Nasrid Emirate of Granada** and the Alhambra, the **Mozarabs** and
**Mudéjars**, the 1492 expulsion and the Morisco revolts. Absent on the Christian side:
the **Kingdom of Asturias** and Pelagius, **León**, **Castile** (El Cid, Alfonso VI,
Alfonso X, Isabella I), the **Crown of Aragon** (Ramon Berenguer IV, James I the Conqueror,
Peter III, Ferdinand II) and its Mediterranean empire, **Navarre** (Sancho III), **Portugal
as a kingdom** (Afonso Henriques, the Aviz dynasty, John I, Henry the Navigator — only
`Portuguese Empire [era] 1415..1999` exists), the **Battle of Las Navas de Tolosa (1212)**,
the **Catholic Monarchs**, the **Spanish Inquisition**.
**Where it belongs:** `Reconquista & Iberian Unification [era] 711..1492 (foun)` under
`Western Europe [region] —..— (foun)`.
**Why it matters:** the Almoravids and Almohads are present but filed under `North Africa`,
so from Europe's side Iberia 711–1492 is one word. Córdoba was the largest city in Western
Europe and the main channel for Greek and Arabic learning into Latin Christendom, and it is
absent.
**Rough dates:** 711–1492.

### The Italian city-republics, the Papacy, and Norman Sicily
**Severity:** high
**What is missing:** **the Papacy appears nowhere** — not one pope, no Papal States, no
**Investiture Controversy** or Gregory VII and Canossa, no **Innocent III**, no Avignon
Papacy, no Western Schism, no Council of Trent (`The Reformation [era] 1517..1648` has only
`Martin Luther` and `Thirty Years' War`). Also absent: the **Republic of Venice** (the doge,
the Fourth Crusade, the Stato da Mar, Lepanto), **Genoa**, **Florence** and the **Medici**,
**Milan** and the Visconti/Sforza, Pisa, the **Lombard League**, the **Kingdom of Sicily**
and **Norman Sicily** (Robert Guiscard, **Roger II**, the Hauteville dynasty, the preceding
**Emirate of Sicily**), the **Kingdom of Naples**, the Italian Wars, the **Risorgimento** and
**Kingdom of Italy**, Garibaldi, Cavour, **Fascist Italy** and Mussolini. `Italian
Renaissance [period] 1300..1600` exists with no political container beneath it.
**Where it belongs:** `Mediterranean [region] —..— (foun)`,
`The Renaissance [era] 1300..1600 (foun)`, `The Reformation [era] 1517..1648 (foun)`.
**Why it matters:** the Renaissance is present as a cultural era with none of the states that
produced it, and the institution that shaped a thousand years of European politics — the
Papacy — is absent while individual Roman usurpers are itemised. Italy also has no modern
state entity at all, so a WWII Axis power is missing.
**Rough dates:** 756–1945.

### Post-Roman successor kingdoms and the pre-Roman peoples
**Severity:** high
**What is missing:** `Migration Period [era] 376..800` has **no children**. Absent: the
**Visigothic Kingdom** (Alaric I and the sack of Rome 410, Euric, Reccared, Toledo, the 711
collapse), the **Ostrogothic Kingdom** and **Theodoric the Great**, the **Vandal Kingdom** of
Africa and Genseric, the **Lombard Kingdom** and Alboin, the **Merovingian Franks** and
**Clovis I** (the only "Clovis" entries in the dataset are the Palaeoindian
`Clovis Culture` and `Pre-Clovis Horizon`), the **Burgundians**, Suebi, Alemanni,
**Anglo-Saxon kingdoms** (the Heptarchy, **Wessex**, **Mercia** and Offa, **Alfred the
Great**, the **Danelaw**, Æthelstan — `England (Medieval to Modern) [era] 927..—` starts at
Æthelstan's unification without him), the **Battle of Tours (732)**, the **Battle of the
Catalaunian Plains (451)**. On the pre-Roman side: the **Etruscans**, the **Celts** and
**Gauls**, **Vercingetorix** and the Gallic Wars, the **Hallstatt** and **La Tène** cultures,
**Dacia** and **Decebalus**, the **Thracians**, the **Illyrians**, the **Iberians**, the
**Picts**, the **Sea Peoples**.
**Where it belongs:** `Migration Period [era] 376..800 (inte)`,
`England (Medieval to Modern) [era] 927..— (foun)`,
`Ancient Rome [era] 753BC..476 (foun)`, `Iron Age [era] 1200BC..550BC (foun)`.
**Why it matters:** the dataset enumerates the Western Roman collapse emperor by emperor
(`Avitus`, `Glycerius`, `Libius Severus`) and then has no entity for a single one of the
kingdoms that replaced them, and no Etruscans or Gauls for Rome to have grown out of and
conquered. The Franks — whose Carolingian phase is present from 751 — have no Merovingian
prehistory, so Charlemagne's dynasty appears from nowhere.
**Rough dates:** 900 BC – 800 CE.

### Northern Europe and the Hanse
**Severity:** medium
**What is missing:** `Northern Europe [region]` holds three entities: `Viking Age` (one
child, `Cnut the Great`), `Kalmar Union`, `Swedish Empire`. Absent: the **Kingdom of
Denmark** (Harald Bluetooth, Gorm, Valdemar the Great), the **Kingdom of Norway** (Harald
Fairhair, Olaf Tryggvason, **Harald Hardrada**, Olaf II), the **Kingdom of Sweden** before
1611, **Gustav I Vasa**, **Gustavus Adolphus** and **Charles XII**, the **Icelandic
Commonwealth** and the Althing (930 — arguably the oldest continuous parliament), the
**Norse settlement of Greenland**, the **Sámi**, Finland, the **Hanseatic League** (Lübeck,
the Kontore, the Bergen and Novgorod trade), the **Teutonic Order** and Livonian Order, the
Great Northern War.
**Where it belongs:** `Northern Europe [region] —..— (foun)` and
`Viking Age [era] 793..1066 (foun)`.
**Why it matters:** the Viking Age has one named person and he is a king of England. The
Hanse is the most important non-dynastic political-economic institution of the medieval
north and it is not in the dataset at all.
**Rough dates:** 793–1721.

---

## Where coverage is genuinely fine

Worth saying, so the effort is not misdirected:

- **Ancient Egypt.** Near-complete dynastic and regnal coverage from `Narmer / Menes` to
  `Ptolemy XV Caesarion`, with predynastic phases and intermediate periods properly modelled.
  The only visible dynastic gaps are the 14th, 16th, 17th, 23rd and 24th dynasties, and the
  Theban High Priests of Amun.
- **Rome and Byzantium.** Roman coverage is exhaustive to the point of listing usurpers who
  reigned for weeks. The Byzantine emperor list is thin in the eighth-to-ninth centuries
  (no Nikephoros I, Michael II, Theophilos, Theodora) and skips the Latin period, but is
  otherwise solid.
- **The Chinese dynastic sequence.** Every dynasty from Xia to the PRC is present, with full
  reign lists for Han, Tang, Song, Yuan, Ming and Qing, and a well-modelled Neolithic
  sequence. Missing at the margins: **Balhae**, **Nanzhao** and **Dali**, the **Ryukyu
  Kingdom**, the **Ainu**, **Tuyuhun**, and Taiwan as a polity — plus per-ruler coverage of
  Three Kingdoms, Jin, Northern and Southern Dynasties, Liao, Western Xia and Jurchen Jin.
- **Vietnam.** The most completely modelled dynastic sequence outside China, Egypt and Japan,
  including the Trịnh/Nguyễn lordship split.
- **South India.** Chola, Pallava, Rashtrakuta, Chalukya, Kakatiya and Vijayanagara all
  present with substantial ruler lists — better than most general-purpose datasets manage.
- **Deep prehistory and lithic industries.** Coherent and genuinely global: African, European,
  Central Asian, South Asian, Southeast Asian and American sequences all populated, with the
  `Behavioural Firsts` threshold series tying them together.

---

## The five worst

1. **The Crusades, Ayyubids and Mamluk Sultanate — and with them Egypt 641–1798.** A single
   connected void covering the Kingdom of Jerusalem, the military orders, Saladin, Hattin,
   Baybars, Ain Jalut and the Fourth Crusade's shattering of Byzantium. Egypt, the
   best-covered polity in the dataset before 641, then has no state at all for twelve
   centuries. This removes both the main axis of medieval Christian–Muslim interaction and
   the power that stopped the Mongols.
2. **West Asian ruler lists are empty across the board.** One Assyrian king, one Old
   Babylonian, one Neo-Babylonian, zero Hittites, zero Sumerian city-states, zero Ur III
   kings, zero Seleucids, one Parthian, four Sasanians, two Ottomans, one Abbasid caliph, no
   Rashidun caliphs. Against 150 pharaohs and ~100 Roman emperors, the dataset structurally
   asserts that the region which invented cities, writing and law had almost no history —
   and it lacks the **Fall of Constantinople (1453)** entirely.
3. **Poland, Hungary, Bohemia, Lithuania, Bulgaria, Serbia and Al-Andalus are all absent as
   polities.** Half of Europe by area and a majority of its medieval kingdoms. Two existing
   entities (`The Habsburg Monarchy` 1526, `Thirty Years' War` 1618) have start dates the
   dataset cannot explain because their Hungarian and Bohemian causes are missing, and
   `Basil II the Bulgar-Slayer` is named for a state that does not exist here.
4. **No Papacy, no Italian city-republics, no post-Roman successor kingdoms, no Etruscans or
   Gauls.** The Renaissance and Reformation are present as cultural eras with none of the
   institutions or states that produced or opposed them, and the Roman collapse is itemised
   emperor by emperor with no Visigoths, Ostrogoths, Vandals, Lombards, Merovingians or
   Anglo-Saxons to replace them. Modern Italy is absent too.
5. **Africa and Oceania have no modern or post-1500 political history worth the name.**
   Missing: Madagascar in any form, all the Great Lakes kingdoms, Christian Nubia, the Zagwe,
   the Maghreb between 146 BC and 1631, the Mfecane and everything after it, colonial and
   independent Africa (no apartheid, no Mandela, no Muhammad Ali Pasha, no Suez, no
   post-1960 state). In Oceania, Rapa Nui, Samoa and Tahiti are entirely absent and Tonga,
   Hawaiʻi and Māori Aotearoa are single labels with almost no internal structure.

*Honourable mentions that just miss the top five:* the Huns, Avars, Khazars and Pechenegs
(the western steppe is absent while the Migration Period it caused is present); the Kazakh,
Dzungar, Crimean and Tatar khanates plus the Durrani Empire (so Afghanistan appears nowhere);
Brazil, Canada, Haiti and the Latin American independence wars, plus Cortés, Pizarro and the
fall of Tenochtitlan as events; Armenia in any form; the Philippines, Malaysia, Singapore and
Myanmar after decolonisation; and Adena, Hopewell, Thule and the Arctic.
