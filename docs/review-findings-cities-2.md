# Correctness review — `cities-2.json` (719 entities)

Judgement pass, no web verification. Reviewer's own knowledge only.

Regional split: West Asia 261, Europe 219, South Asia 122, Southeast Asia 82, Oceania 31,
Phoenician City-States 4.

---

## Patterns (stated once, not repeated per entry)

### PATTERN A — ~55 entities are not cities, and about forty of them say so in their own summary

`kind` is `city` for every row in the file, including monuments, sanctuaries, Neolithic villages,
fortresses, ceremonial landscapes, an island, and two polities. The tell is that the summary itself
frequently ends "…; not a city", "…, not a settlement", "…, not a town", "ceremonial, not a city",
"a village, not a city", "garrison, not a town", "proto-urban tribal centre, not a city". An entity
whose own description denies it is a city should not be filed as one. Full list:

**Monuments / sanctuaries / ceremonial sites:** `europe.city-stonehenge`, `europe.city-tarxien`,
`europe.city-tara`, `europe.city-thingvellir`, `europe.city-olympia`, `europe.city-nemea`,
`west-asia.city-yazilikaya`, `west-asia.city-didyma`, `west-asia.city-karahan-tepe`,
`west-asia.city-takht-e-soleyman`, `south-asia.city-konark`, `south-asia.city-sanchi`,
`south-asia.city-sarnath`, `south-asia.city-ajanta`, `south-asia.city-ellora`,
`south-asia.city-lumbini`, `southeast-asia.city-borobudur`, `southeast-asia.city-dieng`,
`southeast-asia.city-myson`, `oceania.city-taputapuatea`, `oceania.city-me-ae-iipona`,
`oceania.city-haamonga-a-maui`, `oceania.city-pulemelei`, `oceania.city-badrulchau`,
`oceania.city-orongo`.

**Neolithic/Chalcolithic villages and type-sites:** `west-asia.city-asikli-hoyuk`,
`west-asia.city-beidha`, `west-asia.city-can-hasan`, `west-asia.city-cayonu`,
`west-asia.city-choga-mami`, `west-asia.city-hacilar`, `west-asia.city-jarmo`,
`west-asia.city-nevali-cori`, `west-asia.city-samarra-prehistoric`,
`west-asia.city-tell-es-sawwan`, `west-asia.city-tell-al-ubaid`, `europe.city-starcevo`,
`europe.city-vinca`, `europe.city-nea-nikomedeia`.

**Fortresses, camps, compounds, industrial sites:** `west-asia.city-masada`,
`west-asia.city-qumran`, `west-asia.city-timna-copper`, `europe.city-trelleborg`,
`europe.city-maiden-castle`, `europe.city-vix-mont-lassois`, `europe.city-su-nuraxi`.

**Landscapes, road networks, islands, regions, polities:** `oceania.city-brewarrina-fish-traps`,
`oceania.city-budj-bim`, `oceania.city-kuk-swamp`, `oceania.city-ara-metua`,
`oceania.city-rapa-nui`, `oceania.city-roi-mata-domain`, `oceania.city-house-of-taga`,
`europe.city-tartessos`, `southeast-asia.city-mataram-medang`, `southeast-asia.city-kauthara`,
`southeast-asia.city-kedah-bujang`.

The worst of these are broken out individually below.

### PATTERN B — `bounds` are computed as a fixed percentage of the date, not from evidence

Across 612 rows with numeric bounds, the half-width is almost always exactly 2%, 6%, 15%, 25% or
50% of `|start|` (221 rows at 6%, 142 at 15%, 81 at 2%). This means uncertainty is wrong in *both*
directions and is never about the evidence:

- Foundation years known to the year from inscriptions or annals still carry large bounds:
  `west-asia.city-erebuni` (summary literally says "founded in 782 BCE", bounds ±46),
  `west-asia.city-argishtihinili` (776 BCE Argishti I, bounds ±116),
  `west-asia.city-dur-sharrukin` (±14), `west-asia.city-persepolis` (±10),
  `west-asia.city-artaxata` (±25), `west-asia.city-baghdad` (762 CE, ±15),
  `europe.city-rhodes-city` (408 BCE, ±10), `europe.city-messene` (369 BCE, ±25).
- Conversely, deep-prehistoric sites that nobody can place within centuries get spuriously tight
  bounds: `west-asia.city-megiddo` (−5000 ±100), `west-asia.city-hazor` (−2700 ±54),
  `west-asia.city-ugarit` (−6000 ±120), `west-asia.city-assur` (−2600 ±52),
  `europe.city-mycenae` (−1900 ±38), `europe.city-stonehenge` (−3000 ±60).

Fix the generator, not the rows.

### PATTERN C — `dated_by: typological` on cities with documented foundation dates

`typological` is used for essentially everything pre-medieval, including Hellenistic, Roman and
early Islamic foundations whose founding year is a documentary fact, not a pottery estimate:
`west-asia.city-baghdad` (762), `west-asia.city-basra` (636), `west-asia.city-kufa` (638),
`west-asia.city-samarra` (836), `west-asia.city-seleucia` (−305), `west-asia.city-dura-europos`
(−303), `west-asia.city-edessa` (−303), `west-asia.city-nicaea` (−316),
`west-asia.city-erebuni`, `west-asia.city-argishtihinili`, `west-asia.city-dur-sharrukin`,
`west-asia.city-persepolis`, `west-asia.city-artaxata`, `europe.city-thessalonica` (−315),
`europe.city-narbo` (−118), `europe.city-piacenza`/`europe.city-tarraco` (−218),
`europe.city-portus` (42), `europe.city-ulpia-traiana`/`europe.city-nicopolis-ad-istrum` (106),
`europe.city-split` (295), `europe.city-ribe`, `europe.city-sigtuna`, `europe.city-nidaros`.
These should be `calendar`/documentary. (The four Phoenician rows use `unknown`, inconsistently
with everything else in the file.)

### PATTERN D — `aliases` are polluted with modern administrative regions

Very many rows list a province, district, oblast or island group as an "alias": `Dorset`, `Crete`,
`Sicily`, `Argolis`, `Bavaria`, `Boeotia`, `Laconia`, `Tuscany`, `Lazio`, `Campania`,
`Emilia-Romagna`, `Dhi Qar`, `Babil`, `Hasakah`, `Nineveh`, `Fars`, `Khuzestan`, `Makkah`,
`Hadramawt`, `Southern District`, `West Bank`, `Bagalkot`, `Rakhine State`, `Tongatapu`, and so on.
These are not names the city was ever called. A few are outright wrong as aliases:
`west-asia.city-kashan` → "Isfahan", `west-asia.city-khaybar` → "Madinah",
`west-asia.city-jeddah` → "Makkah", `west-asia.city-zabid` → "Hodeidah",
`west-asia.city-kufa` → "Najaf", `west-asia.city-taif` → "Makkah". Meanwhile some rows that badly
need a modern alias have none (see the Phoenician entries below).

---

## Findings

### west-asia.mesopotamia.phoenicia.tyre
**Field:** end (and aliases)
**Currently:** `end: -332`, no aliases; summary "fell to Alexander after a seven-month siege"
**Should be:** `end: null`, `extant: true`; aliases should include Sur / Ṣūr / Ṣur, Ṣurru
**Confidence:** high
**Why:** Alexander's siege is a conquest, not an ending — Tyre was refounded within a generation,
was a major Roman and Crusader city, and is the fourth-largest city in Lebanon today.

### west-asia.mesopotamia.phoenicia.sidon
**Field:** end (and aliases)
**Currently:** `end: -332`, no aliases
**Should be:** `end: null`, `extant: true`; aliases Saida / Ṣaydā, Ṣidunu
**Confidence:** high
**Why:** Sidon passed to Alexander and continued unbroken as a Hellenistic, Roman, Islamic and
Ottoman port; it is a living Lebanese city.

### west-asia.mesopotamia.phoenicia.byblos
**Field:** end, start (and aliases)
**Currently:** `start: -3000`, `end: -332`, no aliases
**Should be:** `end: null`, `extant: true`; start plausibly −5000 or earlier; aliases Jbeil / Jubayl,
Gubla, Gebal
**Confidence:** high
**Why:** Byblos is routinely cited as one of the oldest *continuously inhabited* cities on earth
(Neolithic occupation from the 6th–5th millennium), so both a −3000 founding and a 332 BCE ending
are wrong; modern Jbeil sits on the site.

### west-asia.mesopotamia.phoenicia.arwad
**Field:** end (and aliases, summary)
**Currently:** `start: -1200`, `end: -332`, no aliases; summary "The northernmost city, on an island"
**Should be:** `end: null`, `extant: true`; aliases Ruad, Arados, Antaradus-offshore
**Confidence:** high
**Why:** Arwad is the only inhabited island in Syria today and was continuously occupied through
Hellenistic, Roman, Crusader and Ottoman times. The summary also only parses inside its parent
list ("the northernmost city" of what?).

### south-asia.city-anuradhapura
**Field:** end
**Currently:** `end: 1017` (the Chola conquest), `extant: null`
**Should be:** `extant: true`, `end: null` — or an explicit note that the *capital* function ended
**Confidence:** high
**Why:** Anuradhapura ceased to be the royal capital after the Chola invasion but the place was
never abandoned and is a substantial living Sri Lankan city and pilgrimage centre.

### europe.city-mystras
**Field:** end
**Currently:** `end: 1500`
**Should be:** c. 1830s
**Confidence:** high
**Why:** Mystras was inhabited long past 1500 — Ottoman and Venetian silk town, still populated
until the founding of modern Sparti in the 1830s drew the inhabitants down to the plain.

### europe.city-skalholt
**Field:** end
**Currently:** `end: 1500`
**Should be:** 1785 (or `null`, since a farm and church remain)
**Confidence:** high
**Why:** Skálholt was Iceland's principal see until the 1780s, when earthquake damage and the
Laki disaster caused the see to move to Reykjavík. 1500 is arbitrary.

### southeast-asia.city-lamphun
**Field:** start
**Currently:** `-600`
**Should be:** c. 750 CE
**Confidence:** high
**Why:** Hariphunchai was a Mon polity founded in the mid-8th century CE; a 600 BCE founding is off
by roughly 1,350 years and predates any urbanism in northern Thailand.

### southeast-asia.city-mataram-medang
**Field:** kind / whole entity
**Currently:** filed as a city; summary "Central Javanese **kingdom** whose shifting royal centre…"
**Should be:** a polity, not a city — and it duplicates `southeast-asia.city-prambanan-mataram`,
which lists "Medang" as an alias
**Confidence:** high
**Why:** By the summary's own admission there is no fixed settlement here; Medang is the state whose
capital moved. This is exactly the "polity sharing its capital's name" case.

### europe.city-tartessos
**Field:** kind / whole entity
**Currently:** filed as a city; summary "Legendary silver-rich **kingdom and trading polity**";
aliases include "lower Guadalquivir"
**Should be:** a polity/region; `historicity` should also flag that the city of Tartessos is
unlocated and semi-legendary
**Confidence:** high
**Why:** No Tartessian city site is identified; the name denotes a region and a culture. Presenting
it as a city with archaeological-style bounds (−900 ±135) overstates the evidence badly.

### oceania.city-rapa-nui
**Field:** kind / whole entity
**Currently:** a city named "Rapa Nui", summary "Island society of **dispersed hamlets**";
aliases include "Rano Raraku", "Ahu Tongariki" (a quarry and a platform)
**Should be:** an island/society, not a city — and by its own summary explicitly not nucleated
**Confidence:** high
**Why:** Easter Island is an island, not a settlement, and the entry admits the settlement pattern
was dispersed.

### europe.city-stonehenge
**Field:** kind / whole entity
**Currently:** city; summary "Iconic ceremonial monument and gathering place; **not a settlement**"
**Should be:** a monument
**Confidence:** high
**Why:** Self-contradicting row; the most reader-misleading of the not-a-city cases.

### west-asia.city-masada
**Field:** kind / whole entity
**Currently:** city; summary "…a **fortress, not a city**"
**Should be:** a fortress/palace complex
**Confidence:** high

### west-asia.city-qumran
**Field:** kind / whole entity
**Currently:** city; summary "a **community compound, not a city**"
**Should be:** a settlement/compound
**Confidence:** high

### west-asia.city-yazilikaya
**Field:** kind / whole entity
**Currently:** city; summary "Rock sanctuary… **ceremonial, not a city**"
**Should be:** a sanctuary, and it is an annex of Hattusa rather than an independent place
**Confidence:** high

### west-asia.city-didyma
**Field:** kind / whole entity
**Currently:** city; summary "Oracle sanctuary of Apollo attached to Miletus; **ceremonial, not a
city**"
**Should be:** a sanctuary, filed under Miletus
**Confidence:** high

### southeast-asia.city-borobudur
**Field:** kind / whole entity
**Currently:** city; summary "Largest Buddhist **monument** on earth, a stone mandala"
**Should be:** a monument
**Confidence:** high

### south-asia.city-konark
**Field:** kind / whole entity
**Currently:** city; summary "…a **monument** and port shrine, **not a city**"
**Should be:** a temple/monument
**Confidence:** high

### south-asia.city-ajanta / south-asia.city-ellora
**Field:** kind / whole entity
**Currently:** cities
**Should be:** rock-cut cave complexes (a monastery and a temple group)
**Confidence:** high
**Why:** Caves, explicitly named as such in both summaries; neither was ever a town.

### europe.city-olympia / europe.city-nemea
**Field:** kind / whole entity
**Currently:** cities; both summaries say "sanctuary… rather than a true city" / "sanctuary, not a
city"
**Should be:** Panhellenic sanctuaries
**Confidence:** high

### europe.city-tara / europe.city-thingvellir
**Field:** kind / whole entity
**Currently:** cities; summaries "ceremonial inauguration site… **not an urban centre**" and
"assembly plain… **not a town**"
**Should be:** ceremonial/assembly sites
**Confidence:** high

### europe.city-tarxien
**Field:** kind / name / whole entity
**Currently:** one "city" named "Tarxien and Ġgantija temples", aliases "Ggantija", "Hagar Qim"
**Should be:** three separate temple complexes on two islands, none of them a city
**Confidence:** high
**Why:** Not a city, and it merges three distinct sites (Tarxien and Ħaġar Qim on Malta, Ġgantija
on Gozo) into a single entity with a single date range.

### oceania.city-brewarrina-fish-traps / oceania.city-kuk-swamp / oceania.city-budj-bim / oceania.city-ara-metua
**Field:** kind / whole entity, and `extant: true`
**Currently:** cities with `extant: true` and no end
**Should be:** a fish-trap complex, an agricultural site, an aquaculture landscape, and a road/marae
network respectively; none is an inhabited city today
**Confidence:** high
**Why:** These are landscapes and installations. `extant: true` on Kuk Swamp in particular implies a
living city where there is an archaeological wetland.

### west-asia.city-ashdod
**Field:** extant
**Currently:** `start: -1600`, `extant: true`, `end: null`
**Should be:** the ancient city ended (Tel Ashdod / Ashdod-Yam abandoned by the medieval period);
modern Ashdod is a 1956 foundation on a different site
**Confidence:** medium
**Why:** As written, a reader will think the Philistine city has been inhabited continuously to the
present. Same issue, more mildly, at `west-asia.city-beersheba` (Tel Sheva is a ruin; the modern
city is Ottoman-era and adjacent).

### europe.city-ryazan
**Field:** whole entity — two places conflated
**Currently:** name "Ryazan", `start: 1095`, `extant: true`, aliases "Old Ryazan", "Staraya Ryazan",
summary "destroyed by the Mongols in 1237 and relocated"
**Should be:** split — Old Ryazan (destroyed 1237, abandoned, `extant: null`) versus modern Ryazan
(the former Pereyaslavl-Ryazansky, extant)
**Confidence:** high
**Why:** One row cannot be both the site destroyed in 1237 and the living city, and the aliases
point at the abandoned one while `extant` points at the living one.

### southeast-asia.city-cebu and southeast-asia.city-cebu-sugbu
**Field:** duplicate entities
**Currently:** two rows for the same place — "Cebu" (start 1000, alias Sugbu) and "Sugbu"
(start 1200, alias Cebu), with near-identical summaries
**Should be:** one entity
**Confidence:** high
**Why:** Straight duplication with contradictory start dates.

### west-asia.city-dezful-jundishapur
**Field:** id / name — three cities conflated
**Currently:** id `dezful-jundishapur`, name "Shushtar", summary about the Shushtar hydraulic system
**Should be:** Shushtar only; Dezful and Gundeshapur are separate places, and Gundeshapur already
has its own row (`west-asia.city-gundeshapur`)
**Confidence:** high
**Why:** The identifier names two cities that the entry is not about; a reader searching for
Jundishapur lands on Shushtar.

### south-asia.city-sirsukh-sialkot
**Field:** id
**Currently:** id `sirsukh-sialkot`, name "Sialkot"
**Should be:** Sialkot (Sagala); Sirsukh is one of the three mounds of Taxila, 250 km away, and is
already listed as an alias of `south-asia.city-taxila`
**Confidence:** high

### europe.city-naples-cuma
**Field:** id
**Currently:** id `naples-cuma`, name "Puteoli", summary about Pozzuoli's harbour
**Should be:** id should reference Puteoli/Pozzuoli; Cumae is a different Greek city
**Confidence:** high

### west-asia.city-melitene
**Field:** whole entity / aliases — overlaps another row
**Currently:** Melitene, `start: -1200`, aliases "Malatya", "Melid"; but
`west-asia.city-arslantepe` is also aliased "Melid, Malatya"
**Should be:** Melid = Arslantepe (the Neo-Hittite mound); Melitene = the Roman legionary city
(Battalgazi/old Malatya), founded as a garrison in the 1st century CE
**Confidence:** medium
**Why:** Two rows claim the same ancient name, and Melitene's −1200 start belongs to Arslantepe/Melid,
not to the Roman city.

### west-asia.city-nicomedia
**Field:** start
**Currently:** `-712`
**Should be:** −264 (Nicomedes I), with Astacus as the predecessor settlement if −712 is wanted
**Confidence:** medium
**Why:** 712 BCE is the traditional founding of Megarian Astacus. Nicomedia itself is a Hellenistic
foundation; as written the entry implies a 448-year-older city than existed under that name.

### europe.city-venice
**Field:** start / dated_by / historicity
**Currently:** `start: 421`, `bounds: [411, 431]`, `dated_by: typological`
**Should be:** legendary; real lagoon settlement is 6th–7th century CE, with the ducal centre at
Rivoalto from c. 810
**Confidence:** medium-high
**Why:** 25 March 421 is the traditional/legendary founding date. Presenting it with archaeological
bounds and no `historicity` marker is precisely the "legendary founding presented as
archaeological" failure.

### south-asia.city-dwarka
**Field:** start / historicity
**Currently:** `start: -1500`, `historicity: null`, summary "**Legendary** Krishna capital and a real
medieval pilgrimage… port"
**Should be:** the archaeological/urban site is medieval; if −1500 is retained it must be marked
legendary
**Confidence:** medium-high
**Why:** The summary concedes the early city is legendary while the date field presents 1500 BCE as
a fact with ±225 bounds.

### europe.city-padua
**Field:** start
**Currently:** `-1200`
**Should be:** c. −1000 / 10th–9th century BCE
**Confidence:** medium
**Why:** −1200 tracks the Antenor foundation legend rather than the Venetic archaeology, which
begins in the early first millennium. Same concern, weaker, at `europe.city-tibur` (−1200).

### southeast-asia.city-lopburi
**Field:** start
**Currently:** `-500`
**Should be:** c. 6th century CE (Dvaravati Lavo)
**Confidence:** medium
**Why:** Lavo is a Dvaravati-era city; a 500 BCE founding precedes urbanism in the Chao Phraya basin
by a millennium. Prehistoric occupation in the region is not the city.

### southeast-asia.city-nakhon-pathom
**Field:** start
**Currently:** `-100`
**Should be:** c. 6th century CE
**Confidence:** medium
**Why:** Nakhon Pathom is the flagship Dvaravati city; Dvaravati is a mid-first-millennium CE
culture.

### southeast-asia.city-nakhonsithammarat
**Field:** start
**Currently:** `-200`
**Should be:** c. 2nd–7th century CE at the earliest
**Confidence:** medium
**Why:** Tambralinga is attested from the early centuries CE, not the 3rd century BCE.

### southeast-asia.city-hanoi
**Field:** start
**Currently:** `-200`
**Should be:** 7th century CE (Dai La) or 1010 (Thang Long); Co Loa, the −300 site, already has its
own row
**Confidence:** medium
**Why:** Hanoi as a city dates from the Chinese-period citadel at Dai La; the −200 date belongs to
the neighbouring Au Lac capital, which is `southeast-asia.city-coloa`.

### south-asia.city-gaur
**Field:** start
**Currently:** `-400`
**Should be:** unclear — the excavated city is early-medieval to Sultanate; −400 rests on the
literary Gauda region name, not on a city
**Confidence:** medium

### south-asia.city-lahore
**Field:** start
**Currently:** `-100`
**Should be:** unclear — first firm attestation is 7th century CE, with archaeology reaching perhaps
the early first millennium CE
**Confidence:** medium
**Why:** A 100 BCE founding for Lahore is a recall artefact; nothing dates the city that early.

### europe.city-viminacium
**Field:** start
**Currently:** `-100`
**Should be:** early 1st century CE
**Confidence:** medium
**Why:** Viminacium is a Roman legionary foundation of the Julio-Claudian period; there is no
pre-Roman city of that name.

### europe.city-sopianae
**Field:** start
**Currently:** `-50`
**Should be:** c. 100 CE
**Confidence:** medium
**Why:** Sopianae is a 2nd-century CE Roman town; the entry's own summary calls it "late Roman".

### europe.city-vindobona
**Field:** start
**Currently:** `-15`
**Should be:** late 1st century CE (c. 97 CE legionary camp)
**Confidence:** medium

### europe.city-thasos
**Field:** end / extant
**Currently:** `end: 600`, `extant: null`
**Should be:** `extant: true`, `end: null`
**Should be:** Limenas (the ancient city site) is the island's inhabited capital today; occupation was
never broken for a millennium and a half.
**Confidence:** medium

### west-asia.city-palmyra
**Field:** end
**Currently:** `end: 1400`
**Should be:** `null` / 2015 — Tadmur remained an inhabited village and then town, and modern Tadmur
adjoins the ruins
**Confidence:** medium
**Why:** Palmyra shrank drastically but was never abandoned; the village occupied the Bel temple
precinct until the 1930s.

### west-asia.city-side
**Field:** end
**Currently:** `end: 1100`
**Should be:** `extant: true` — the ancient site is the modern town of Side/Selimiye
**Confidence:** medium

### west-asia.city-harran
**Field:** end
**Currently:** `end: 1260`
**Should be:** `extant: true` — Harran is an inhabited town today, though much reduced after the
Mongol destruction
**Confidence:** medium

### west-asia.city-marib
**Field:** end / extant
**Currently:** `end: 700`, `extant: null`
**Should be:** at minimum note that Ma'rib is a living Yemeni city and provincial capital on the
same oasis
**Confidence:** medium

### southeast-asia.city-angkor
**Field:** end
**Currently:** `end: 1431`
**Should be:** the *capital* ended in 1431; the site was never wholly abandoned (Angkor Wat remained
an active monastery and the region stayed populated)
**Confidence:** medium
**Why:** 1431 is a conquest/abandonment-of-capital date being used as an end of occupation.

### southeast-asia.city-ayutthaya
**Field:** end
**Currently:** `end: 1767`
**Should be:** `extant: true` — Phra Nakhon Si Ayutthaya is a living provincial city on the island
**Confidence:** medium
**Why:** The 1767 Burmese sack ended the kingdom and the royal city, not the settlement.

### south-asia.city-polonnaruwa
**Field:** end
**Currently:** `end: 1300`
**Should be:** `extant: true` — modern Polonnaruwa is an inhabited town beside the ancient city
**Confidence:** low-medium

### europe.city-torcello
**Field:** end
**Currently:** `end: 1500`
**Should be:** never fully abandoned; a handful of residents and the basilica remain
**Confidence:** low

### south-asia.city-madurai
**Field:** aliases
**Currently:** includes "Toundis"
**Should be:** remove; Ptolemy's name for Madurai is Modoura. Tyndis/Toundis is a Kerala coast port
**Confidence:** medium-high

### europe.city-poliochni
**Field:** aliases
**Currently:** includes "Palamari"
**Should be:** remove — Palamari is a Bronze Age site on Skyros, unrelated to Poliochni on Lemnos
**Confidence:** medium-high

### south-asia.city-sarnath
**Field:** aliases
**Currently:** includes "Varanasi"
**Should be:** remove; Sarnath is a distinct site near Varanasi, not another name for it
**Confidence:** medium

### europe.city-sybaris
**Field:** aliases
**Currently:** includes "Thurii", "Copia"
**Should be:** remove — Thurii was a *successor* refoundation and already has its own row
(`europe.city-thurii`), which repeats the same two aliases
**Confidence:** medium

### europe.city-sipontum
**Field:** aliases
**Currently:** includes "Manfredonia"
**Should be:** remove; Manfredonia is the replacement town founded 1256, per the entry's own summary
**Confidence:** low-medium

### europe.city-nikaia
**Field:** aliases
**Currently:** "Nice", "Nicaea"
**Should be:** drop "Nicaea" or qualify it — it collides with `west-asia.city-nicaea` (İznik), the
Nicaea any reader will actually be looking for
**Confidence:** low-medium

### europe.city-midea
**Field:** aliases
**Currently:** "Dendra"
**Should be:** Dendra is the adjacent cemetery, not an alternative name for the citadel; it is where
the armour cited in the summary was found
**Confidence:** low

### europe.city-samos-city
**Field:** aliases
**Currently:** "Pythagoreion", "Heraion", "Samos"
**Should be:** drop "Heraion" — the sanctuary is a separate site from the city
**Confidence:** low

### europe.city-novgorod
**Field:** dated_by
**Currently:** `typological`, `start: 859`
**Should be:** `received`/chronicle — 859 is the Novgorod chronicle's date; the dendrochronology of
the site begins in the 930s
**Confidence:** medium
**Why:** A chronicle date presented as a typological one, and arguably 70 years too early for the
settlement.

### europe.city-preslav
**Field:** start
**Currently:** `821`
**Should be:** c. 893 as capital (fortress possibly late 9th century)
**Confidence:** low-medium

### europe.city-veii
**Field:** end vs summary
**Currently:** `end: -100`, summary "destroyed in 396 BCE"
**Should be:** consistent — either the site ended in 396 or it continued (as it did, as a Roman
municipium) and the summary should not read as an ending
**Confidence:** low
**Why:** Internal tension between the date field and the prose.

### west-asia.city-kussara
**Field:** whole entity
**Currently:** a dated city (−2000 to −1600) whose summary says "site not yet identified", alias
"central Anatolia"
**Should be:** flag as unlocated; the bounds imply a site-based date range for a place nobody has
found
**Confidence:** low-medium
**Why:** Same problem as Akkad, Larak, Gerrha and Ubar in this file — unlocated places carrying
archaeological-looking date ranges. Akkad at least says so in its summary.

### south-asia.city-ganweriwala
**Field:** summary
**Currently:** "a fifth of the civilisation's capitals"
**Should be:** "one of the five largest Indus sites" — as written it is unintelligible
**Confidence:** low
**Why:** Wording that a reader cannot parse into a claim.

### southeast-asia.city-mahendraparvata
**Field:** summary
**Currently:** "found by lidar in 2012"
**Should be:** located by airborne lidar surveys published from 2013 (and greatly extended in 2019)
**Confidence:** low

### southeast-asia.city-kota-batu-brunei
**Field:** aliases
**Currently:** includes "Brunei Darussalam"
**Should be:** remove — that is the modern country
**Confidence:** medium

### southeast-asia.city-kauthara / southeast-asia.city-panduranga
**Field:** kind
**Currently:** cities; summaries call them a "port **region**" and a "**principality**"
**Should be:** Cham principalities, with Nha Trang / Phan Rang as the cities
**Confidence:** medium

### southeast-asia.city-kedah-bujang
**Field:** kind / name
**Currently:** city named "Bujang Valley"
**Should be:** an archaeological valley complex containing many sites (Sungai Batu, Pengkalan Bujang)
**Confidence:** medium

### oceania.city-butuan
**Field:** kind
**Currently:** city; summary "Balangay-building trading **polity**"
**Should be:** polity/settlement cluster
**Confidence:** low

### europe.city-sparta
**Field:** extant
**Currently:** `extant: true`, `end: null`
**Should be:** ancient Sparta declined to a village and was superseded by Mystras; modern Sparti is
an 1834 foundation on the site
**Confidence:** low
**Why:** Defensible as continuity of place, but the row hides a real break that the Mystras entry
depends on.

### europe.city-malia
**Field:** end
**Currently:** `-1250`
**Should be:** the palace was destroyed c. −1450; post-palatial occupation continued more thinly
**Confidence:** low

### west-asia.city-jericho
**Field:** summary
**Currently:** "a stone tower a thousand years before farming villages spread"
**Should be:** unclear as phrased — PPNA Jericho *is* one of the founding farming-village
settlements; the tower's distinction is monumentality, not precedence over villages
**Confidence:** low

---

## The twenty worst

Ordered by how badly each misleads a reader.

1. **PATTERN A** — ~55 entities filed as cities that are monuments, sanctuaries, caves, villages,
   fortresses, landscapes, an island and two kingdoms, about forty of which say "not a city" in
   their own summary text.
2. **`west-asia.mesopotamia.phoenicia.tyre`** — ended at Alexander's conquest; Tyre is a living city.
3. **`west-asia.mesopotamia.phoenicia.sidon`** — same conquest-as-ending error; Saida is a living city.
4. **`west-asia.mesopotamia.phoenicia.byblos`** — ended in 332 BCE and founded 2,000 years too late,
   for a city usually named as the oldest continuously inhabited in the world.
5. **`west-asia.mesopotamia.phoenicia.arwad`** — ended in 332 BCE; still inhabited, and the summary
   only parses inside its parent list.
6. **`south-asia.city-anuradhapura`** — ended at the 1017 Chola conquest; a living city.
7. **`southeast-asia.city-lamphun`** — founded 600 BCE for an 8th-century-CE Mon foundation, off by
   ~1,350 years.
8. **`europe.city-tartessos`** — a semi-legendary kingdom and region presented as a dated city.
9. **`southeast-asia.city-mataram-medang`** — a kingdom filed as a city, and duplicating the
   Prambanan row.
10. **`oceania.city-rapa-nui`** — an island whose own summary says the settlement was dispersed.
11. **`europe.city-ryazan`** — the Mongol-destroyed site and the living city merged into one row with
    contradictory fields.
12. **PATTERN B** — uncertainty computed as a flat percentage of the date, giving ±46 years on a
    foundation the summary dates to the exact year and ±100 on a −5000 mound.
13. **`europe.city-venice`** — the legendary 421 CE founding presented as archaeologically bounded.
14. **`south-asia.city-dwarka`** — a −1500 date whose own summary calls the city legendary.
15. **`west-asia.city-dezful-jundishapur`** — one row identified by the names of three different
    cities, one of which has its own separate row.
16. **`europe.city-mystras`** — ended in 1500; actually inhabited until the 1830s.
17. **`southeast-asia.city-cebu` / `southeast-asia.city-cebu-sugbu`** — the same city entered twice
    with different founding dates.
18. **`west-asia.city-ashdod`** — the Philistine tell marked as continuously inhabited to the present.
19. **`southeast-asia.city-nakhon-pathom`, `southeast-asia.city-lopburi`,
    `southeast-asia.city-nakhonsithammarat`, `southeast-asia.city-hanoi`** — a cluster of mainland
    Southeast Asian cities pushed several centuries to a millennium too early, all by the same kind
    of error.
20. **PATTERN C** — `dated_by: typological` on Hellenistic, Roman, Urartian and early Islamic
    foundations whose founding years are documentary facts (Baghdad 762, Basra 636, Erebuni 782 BCE,
    Persepolis, Dur-Sharrukin, Thessalonica, Narbo).

---

## Proposed tests

Each test below corresponds to an error class that occurred more than once in `cities-2.json`.
Violator lists are the entities in this file that fail the rule as written today.

### T1 — A row whose own summary denies it is a city must not be `kind: city` — `safe`
**Rule:** if `kind == "city"` and the summary matches
`/not a(n)? (city|settlement|town|true city|city proper|urban centre)|not an urban/i`, fail.
**Violations (25):** `europe.city-maiden-castle`, `europe.city-olympia`, `europe.city-stonehenge`,
`europe.city-tara`, `europe.city-thingvellir`, `europe.city-trelleborg`, `europe.city-vinca`,
`south-asia.city-konark`, `southeast-asia.city-myson`, `west-asia.city-asikli-hoyuk`,
`west-asia.city-beidha`, `west-asia.city-can-hasan`, `west-asia.city-cayonu`,
`west-asia.city-choga-mami`, `west-asia.city-didyma`, `west-asia.city-hacilar`,
`west-asia.city-jarmo`, `west-asia.city-karahan-tepe`, `west-asia.city-masada`,
`west-asia.city-nevali-cori`, `west-asia.city-qumran`, `west-asia.city-samarra-prehistoric`,
`west-asia.city-tell-es-sawwan`, `west-asia.city-timna-copper`, `west-asia.city-yazilikaya`.
**Why safe:** there is no legitimate reason for a row to assert its own kind is wrong. This single
rule catches half of PATTERN A mechanically and would have caught Stonehenge, Masada and Yazılıkaya.

### T2 — Vocabulary blocklist in `name`/`summary` for non-settlement kinds — `advisory`
**Rule:** warn when a `kind: city` row's **name** contains any of `temple`, `temples`, `cave`,
`caves`, `stupa`, `monument`, `sanctuary`, `fort`, `fortress`, `fish traps`, `swamp`, `platform`,
`traps`, `mound`, `field system`, `domain`, `settlements`, `House of`, `Ara `, `Meʻae`/`Meae`,
`Marae`; or when the **summary's first clause** heads with one of `Rock sanctuary`, `Ceremonial`,
`Largest … monument`, `Type site`, `Type-site`, `Neolithic village`, `village`.
**Violations beyond T1 (partial):** `europe.city-tarxien` ("Tarxien and Ġgantija temples"),
`europe.city-su-nuraxi`, `europe.city-vix-mont-lassois`, `europe.city-nea-nikomedeia`,
`europe.city-starcevo`, `west-asia.city-tell-al-ubaid`, `west-asia.city-takht-e-soleyman`,
`south-asia.city-ajanta`, `south-asia.city-ellora`, `south-asia.city-sanchi`,
`south-asia.city-sarnath`, `south-asia.city-lumbini`, `southeast-asia.city-borobudur`,
`southeast-asia.city-dieng`, `southeast-asia.city-kedah-bujang`,
`oceania.city-brewarrina-fish-traps`, `oceania.city-kuk-swamp`, `oceania.city-budj-bim`,
`oceania.city-ara-metua`, `oceania.city-house-of-taga`, `oceania.city-pulemelei`,
`oceania.city-me-ae-iipona`, `oceania.city-haamonga-a-maui`, `oceania.city-badrulchau`,
`oceania.city-orongo`, `oceania.city-taputapuatea`, `oceania.city-roi-mata-domain`.
**Advisory, because:** legitimate cities carry such words — `europe.city-monemvasia` and
`south-asia.city-chittorgarh` are genuine fortress-cities, `south-asia.city-srirangam` and
`south-asia.city-puri` are genuine temple cities, and `west-asia.city-baalbek` is a sanctuary city
that is also an inhabited town.

### T3 — `extant: true` ⇔ `end: null` — `safe`
**Rule:** `extant == true` requires `end == null`; `end != null` requires `extant != true`.
**Violations:** none in this file (0 of 719) — the file already satisfies it. Worth locking in
anyway, because several of the substantive findings (Anuradhapura, Tyre, Thasos, Side, Harran) are
cases where the *correct* fix flips both fields together and a partial fix would break the invariant.
**Why safe:** the two fields are definitionally linked.

### T4 — `extant` must not be null when `end` is null — `safe`
**Rule:** a row may not leave both `extant` and `end` unset; occupation status must be asserted.
**Violations:** none currently (0 of 719).
**Why safe:** structural completeness; prevents the "unknown whether this place still exists" state
that makes T3 and T5 unenforceable.

### T5 — A row ending in a known conquest/sack year must state abandonment in its summary — `advisory`
**Rule:** maintain a list of well-known conquest, sack and dynastic-fall years
(−332, −330, −146, −133, 476, 1017, 1204, 1236, 1258, 1260, 1265, 1270, 1431, 1453, 1521, 1565,
1767, 1857 …). If `end` equals one of them, require the summary to contain
`/abandon|deserted|razed to|never reoccupied|depopulated|site was left/i`. Otherwise warn: conquest
and renaming are not endings.
**Violations (9):** `west-asia.mesopotamia.phoenicia.tyre`, `…sidon`, `…byblos`, `…arwad` (all −332),
`south-asia.city-anuradhapura` (1017), `southeast-asia.city-angkor` (1431),
`southeast-asia.city-ayutthaya` (1767), `west-asia.city-harran` (1260), `west-asia.city-dvin` (1236).
**Advisory, because:** some conquests really did end a city — `europe.city-motya` (−397, destroyed by
Dionysius I and never rebuilt as a city), `europe.city-naxos-sicily` (−403),
`west-asia.city-caesarea` (1265) and `south-asia.city-vijayanagara` (1565) all pass the smell test
and their summaries say so.

### T6 — A summary asserting abandonment or destruction requires a non-null `end` — `advisory`
**Rule:** if the summary matches `/abandon|deserted|submerged|razed|destroyed|ruined|silted|lost to/i`
and `end == null` and `extant == true`, warn.
**Violations (7):** `europe.city-narbo`, `europe.city-ryazan`, `europe.city-scupi`,
`south-asia.city-chittorgarh`, `south-asia.city-somnath`, `west-asia.city-nishapur`,
`west-asia.city-ray`.
**Advisory, because:** most of these are legitimate — a city can be destroyed and rebuilt on the same
spot (`west-asia.city-nishapur` was sacked by the Mongols and is a living city; `europe.city-narbo`'s
*harbour* silted while Narbonne survived). But this rule is exactly what surfaces
`europe.city-ryazan`, where "destroyed by the Mongols in 1237 and relocated" sits beside
`extant: true`, which is a genuine two-places-in-one-row error.

### T7 — `bounds` must not be a fixed proportion of `start` — `safe`
**Rule:** compute `h = (bounds[1] - bounds[0]) / 2` and `r = h / |start|`. Fail if `r` rounds exactly
to one of {0.02, 0.03, 0.05, 0.06, 0.07, 0.08, 0.12, 0.15, 0.17, 0.20, 0.25, 0.50} across more than
5% of the corpus, or fail per-row if `r` is exactly one of those values and `|start| > 100`.
**Violations:** 391 of 719 rows match a percentage bucket exactly; 221 sit at exactly 6% and 142 at
exactly 15%. Named examples: `west-asia.city-erebuni` (summary says "founded in 782 BCE", bounds
±46 = 6%), `west-asia.city-argishtihinili` (±116 = 15%), `west-asia.city-baghdad` (762, ±15 = 2%),
`europe.city-megiddo`-class deep-prehistoric rows at ±2%.
**Why safe:** uncertainty derived from the magnitude of the date rather than from the evidence is
never correct, in either direction. This is the generator bug behind the "66 – 65 BP" Berlin Wall
incident in a different costume.

### T8 — A documented foundation year must not be `dated_by: typological` — `advisory`
**Rule:** if `dated_by == "typological"` and either (a) `start > 600` CE, or (b) the summary contains
a founder or a year (`/founded (in|by)|colony of|refounded|purpose-built|victory city/i`), warn and
require `calendar` or `received`.
**Violations (88 rows have `typological` with `start > 500`), named examples:** `west-asia.city-baghdad`,
`west-asia.city-basra`, `west-asia.city-kufa`, `west-asia.city-samarra`, `west-asia.city-erebuni`,
`west-asia.city-argishtihinili`, `west-asia.city-dur-sharrukin`, `west-asia.city-persepolis`,
`west-asia.city-artaxata`, `europe.city-thessalonica`, `europe.city-narbo`, `europe.city-piacenza`,
`europe.city-tarraco`, `europe.city-split`, `europe.city-novgorod`, `europe.city-ribe`,
`europe.city-sigtuna`, `europe.city-nidaros`, `europe.city-ulpia-traiana`,
`europe.city-nicopolis-ad-istrum`.
**Advisory, because:** a genuinely typological date can coexist with a late start —
`europe.city-paviken` (600 CE) and `west-asia.city-mecca` (300 CE) really are dated by material
culture, not by a document.

### T9 — An alias must not be the `name` of a different entity in the corpus — `advisory`
**Rule:** for each alias, if it exactly matches another entity's `name`, warn; two rows may not claim
each other's identity.
**Violations (37 pairs), the ones that are real errors:** `southeast-asia.city-cebu` ↔
`southeast-asia.city-cebu-sugbu` (the same city entered twice), `southeast-asia.city-prambanan-mataram`
→ "Medang" (duplicating `southeast-asia.city-mataram-medang`), `europe.city-sybaris` → "Thurii"
(a successor city with its own row), `south-asia.city-sarnath` → "Varanasi",
`europe.city-nikaia` ↔ `west-asia.city-nicaea`, `west-asia.city-kashan` → "Isfahan",
`europe.city-mdina` → "Medina", `south-asia.city-sisupalgarh` → "Bhubaneswar",
`southeast-asia.city-wiangkumkam` → "Chiang Mai", `southeast-asia.city-sriksetra` → "Pyay",
`europe.city-nicopolis-ad-istrum` → "Veliko Tarnovo".
**Advisory, because:** genuine successor-name pairs exist and are useful —
`west-asia.city-nineveh` → "Mosul" and `west-asia.city-mosul` → "Nineveh" reflect a real
relationship, as does `west-asia.city-ctesiphon` → "Baghdad".

### T10 — Aliases must not be administrative regions — `advisory`
**Rule:** reject aliases matching a gazetteer of modern first- and second-level administrative units
plus the suffix patterns `/ (Oblast|Province|District|Region|State|county|prefecture|Krai)$/i` and
`/^(near|around) /i`.
**Violations:** widespread — `Dorset`, `Crete`, `Sicily`, `Argolis`, `Boeotia`, `Laconia`, `Bavaria`,
`Tuscany`, `Lazio`, `Campania`, `Emilia-Romagna`, `Vojvodina`, `Dhi Qar`, `Babil`, `Hasakah`,
`Nineveh`, `Fars`, `Khuzestan`, `Kerman`, `Makkah`, `Hadramawt`, `Southern District`, `West Bank`,
`Bagalkot`, `Rakhine State`, `Sagaing Region`, `Kirovohrad Oblast`, `Leningrad Oblast`,
`near Belgrade`, `Dedan nearby`, `Bisotun nearby`, `Brunei Darussalam`.
**Advisory, because:** a handful of places genuinely share their region's name —
`europe.city-ohrid`, `southeast-asia.city-ternate`, `southeast-asia.city-tidore` and
`west-asia.city-tarim` are all cities whose name is also the administrative unit's name.

### T11 — Every ancient-named city that is `extant: true` must carry its modern name as an alias, and vice versa — `advisory`
**Rule:** if `extant == true` and `start < 500` and `aliases` is empty, fail; more generally, if the
`name` is an ancient form and no alias contains a modern toponym, warn.
**Violations (empty aliases):** `west-asia.mesopotamia.phoenicia.tyre`, `…sidon`, `…byblos`,
`…arwad` (no Sur / Saida / Jbeil / Ruad), `europe.city-ravenna`, `europe.city-segovia`,
`europe.city-verona`, `europe.city-zamora`, `west-asia.city-mtskheta`, `west-asia.city-wasit`,
`west-asia.city-yazd`, `west-asia.city-ardabil`, plus `europe.city-nitra`, `europe.city-ribe`,
`europe.city-roskilde`, `europe.city-sigtuna`, `europe.city-smolensk`, `europe.city-tver`,
`europe.city-valladolid`, `europe.city-yaroslavl`.
**Advisory, because:** cities whose ancient and modern names are identical legitimately need no alias
— Ravenna, Verona and Segovia are the same word in both registers. The four Phoenician rows are the
real failures: readers arrive with "Sur", "Saida", "Jbeil".

### T12 — Founding date must not precede the regional urbanism threshold — `advisory`
**Rule:** per-region floors on `start` for `kind: city`, keyed on `under` and (where needed)
a sub-region tag: mainland/island Southeast Asia −300; Polynesia and Micronesia +800; Melanesia
−1300 (Lapita); Australia and highland New Guinea — no urbanism, so any `kind: city` row is a
failure; Scandinavia, Rus and Poland +500; Sub-Saharan and Atlantic Europe −800. Fail if
`start < floor` unless the row is explicitly typed as a village/proto-urban site.
**Violations:** `southeast-asia.city-lamphun` (−600), `southeast-asia.city-lopburi` (−500),
`southeast-asia.city-angkor-borei` (−400), `southeast-asia.city-nakhon-pathom` (−100, fails the
tighter Dvaravati floor of +500 if one is adopted), `southeast-asia.city-nakhonsithammarat` (−200),
`southeast-asia.city-hanoi` (−200), and every Oceanian row with a negative start:
`oceania.city-kuk-swamp` (−7000), `oceania.city-budj-bim` (−4500),
`oceania.city-brewarrina-fish-traps` (−4000), `oceania.city-lapita-talepakemalai` (−1350),
`oceania.city-bourewa` (−1100), `oceania.city-teouma` (−1000), `oceania.city-nukuleka` (−900),
`oceania.city-mulifanua` (−800), `oceania.city-mangaasi` (−700), `oceania.city-badrulchau` (−100).
**Advisory, because:** the floors are judgement calls and a real early outlier would trip them —
`europe.city-provadia-solnitsata` (−5500) and `west-asia.city-jericho` (−9600) are defensible as
the earliest towns in their regions and should be allowed through with a note.

### T13 — Legendary foundation dates must be marked — `advisory`
**Rule:** if the summary contains `/legendary|traditional(ly)? (founded|founding)|claimed in
chronicles|said to|mythical/i` and `historicity` is null and `dated_by` is `typological`, fail: a
legendary date may not be presented as an archaeological one.
**Violations:** `south-asia.city-dwarka` ("Legendary Krishna capital", `historicity: null`,
`start: -1500`), `europe.city-tartessos` ("Legendary silver-rich kingdom"),
`west-asia.city-ubar` ("identified with legendary Iram"), `southeast-asia.city-tagaung`
("claimed in chronicles"), `europe.city-wolin` ("identified with legendary Jomsborg"),
`west-asia.city-acemhoyuk` ("possibly the Purushanda of legend"). Add
`europe.city-venice` (421) and `europe.city-padua` (−1200), which carry legendary dates without the
word "legendary" and so escape the text rule — evidence that T13 needs a companion list of known
legendary foundation years (Rome −753, Venice 421, Padua −1184/−1200, Kathmandu 723, Lalitpur 299).
**Advisory, because:** `europe.city-rome` at −800 is a defensible archaeological date sitting next to
a famous legendary one, and should not fail.

### T14 — `id` stem must be recoverable from `name` or `aliases` — `safe` (after diacritic folding)
**Rule:** normalise the id stem and the `name` + `aliases` blob (strip diacritics, lowercase, drop
hyphens). Every alphabetic token of the stem longer than three characters must appear in the blob.
**Violations after folding out the false positives** (`mikulcice`, `nimes`, `poznan`, `starcevo`,
`szekesfehervar`, `tonsberg`, `vinca`, `wroclaw`, `stare-mesto-uherske` all fail only on diacritics
and are fine): `west-asia.city-dezful-jundishapur` (name "Shushtar" — two unrelated cities in the
id, one of which has its own row), `south-asia.city-sirsukh-sialkot` ("Sirsukh" is a mound at
Taxila), `europe.city-naples-cuma` (name "Puteoli"; Cumae is a different city).
**Why safe:** once diacritics are folded, an id naming a place the row is not about is always an
error, and all three violations here are genuine conflations.

### T15 — No two rows may describe the same place — `advisory`
**Rule:** flag pairs where names or aliases overlap *and* summaries share three or more distinctive
content words, or where one row's alias set is a subset of another's.
**Violations:** `southeast-asia.city-cebu` / `southeast-asia.city-cebu-sugbu` (both "Visayan port
polity", contradictory starts of 1000 and 1200), `southeast-asia.city-mataram-medang` /
`southeast-asia.city-prambanan-mataram`, `west-asia.city-melitene` / `west-asia.city-arslantepe`
(both aliased "Melid, Malatya"), `west-asia.city-dezful-jundishapur` /
`west-asia.city-gundeshapur`, `europe.city-sybaris` / `europe.city-thurii` (successor cities sharing
both aliases).
**Advisory, because:** genuine successor and twin pairs must be allowed —
`west-asia.city-seleucia` / `west-asia.city-veh-ardashir` / `west-asia.city-ctesiphon` are three real
cities in one conurbation, and `west-asia.city-nineveh` / `west-asia.city-mosul` is a real
succession.
