# Correctness review — cities-1.json (719 entries)

Judgement pass, no web verification, per `docs/briefs/correctness-review.md`.
Coverage: all 719 rows read (Africa 159, Europe 222, Americas 180, East Asia 93, Central Asia 65).

Citations are deliberately not reported. Findings below are grouped: first four
**systematic patterns** (reported once, per the brief), then individual entries.

---

## Patterns

### PATTERN-1 — `kind: city` used for monuments, sanctuaries, cemeteries, forts and landscapes
**Field:** kind (and by implication the file this belongs in)
**Currently:** ~40 rows are `kind: city`. In 14 of them the summary itself ends with
"…; not a city", "…; a fort, not a city", "…; sanctuary rather than city", "…; ceremonial,
not a city".
**Should be:** these are not cities and should not be in a cities file at all — or `kind`
should be `site` / `sanctuary` / `necropolis` / `fortress` / `earthwork`.
**Confidence:** high
**Why:** A row whose own summary says it is not a city is self-refuting. Individual rows are
listed below (NOTCITY-*) because the class is not uniform in severity, but the systematic point
is one bug: the enumeration pulled in the whole archaeological gazetteer, not just cities.

### PATTERN-2 — `dated_by: typological` on foundation dates that are documented calendar dates
**Field:** dated_by
**Currently:** 610 of 719 rows are `typological`, including foundations known precisely from
written record: Cairo 969, Kairouan 670, Fez 789, Mahdia 916, Madinat al-Zahra 936, Ashir 936,
Tahert 761, Raqqada 876, Alexandria −331, Aquileia −181, Ariminum −268, Cremona −218,
Lugdunum −43, Cologne −38, Emerita Augusta −25, Londinium 47, Deva 74, Thamugadi 100,
Djemila 96, Kyoto 794, Nara 710, Fujiwara-kyo 694, Nagaoka-kyo 784, Otsu 667, Buyeo 538,
Kaesong 918, Ordu-Baliq 744, Ai-Khanoum, Sabi, Xianyang −350, Chengdu −311, Guangzhou −214.
**Should be:** `calendar` (or `received`) for any foundation attested by a dated text; reserve
`typological` for dates derived from material culture.
**Confidence:** high
**Why:** Brief item 4. The 109 `calendar` rows are almost all post-1000 CE with `bounds: [null, null]`,
which suggests `dated_by` was assigned by date range rather than by evidence type.

### PATTERN-3 — `historicity` is null on every row, including legendary foundations
**Field:** historicity
**Currently:** null (= accepted) for all 719, including Alba Longa ("Legendary mother city of
Rome"), Lavinium ("Legendary landing city of Aeneas"), Thinis ("site not securely located"),
Njimi ("its site remains unidentified"), Khyunglung ("Reputed capital of Zhangzhung"),
Yumbulagang ("Reputedly Tibet's oldest building"), and the legendary-annal foundation dates
Kyiv 482, Gimhae 42, Gyeongju −57, Jeonju −57, Pyongyang −1000 (Gojoseon).
**Should be:** `legendary` or `contested` on those rows.
**Confidence:** high
**Why:** Brief item 5. Presenting a traditional/legendary foundation with tight archaeological-looking
bounds is exactly the failure mode the brief names.

### PATTERN-4 — `aliases` polluted with regions, provinces, and non-names
**Field:** aliases
**Currently:** a large minority of rows carry a modern governorate/province/county as an "alias"
(Abydos → "Sohag", Antinoöpolis → "Minya", Adulis → "Northern Red Sea", Italica → "Seville
province", Conimbriga → "Coimbra district", Madinat al-Zahra → "Córdoba province", plus ~80 more),
and some carry outright non-names: Buhen → "flooded by Lake Nasser"; Faras, Mirgissa, Semna →
"flooded"; Mogador → "Cerne?"; Ghat → "Ghadamis nearby"; Kerma → "Doukki Gel nearby";
Raqqada → "Sabra al-Mansuriyya nearby"; Itil → "Khazar capital"; Khyunglung → "Zhangzhung capital";
Taihe → "Nanzhao capital"; Jeonju → "Hubaekje capital".
**Should be:** aliases should hold names a reader might arrive with. Location belongs in a location
field; "flooded" and "Cerne?" belong nowhere.
**Confidence:** high
**Why:** A reader searching aliases for "Sohag" will be handed Abydos and Akhmim; a reader searching
"flooded" gets four Nubian forts.

---

## Living cities given an end year, or ended at a conquest they survived

### americas.mesoamerica.aztec.tenochtitlan
**Field:** end / extant / aliases / under / id
**Currently:** `end: 1521`, `extant: null`, `aliases: null`, `under: "Aztec Empire < Mesoamerica < Americas"`.
**Should be:** `end: null`, `extant: true`, aliases including "México-Tenochtitlan" and "Mexico City";
`under` and id format matching the other 718 rows.
**Confidence:** high
**Why:** This is the file's Constantinople case. Tenochtitlan was not abandoned in 1521 — it was
renamed and rebuilt as Mexico City on the same island and has been inhabited without interruption
since. It is also the only row in the file with a nested `under`, a dotted non-`city-` id, and the
only row with `date_standing`, so it looks like it was authored by a different process.

### europe.city-aquileia
**Field:** end
**Currently:** `end: 452` — "destroyed by Attila".
**Should be:** no single end, or an end in the 6th–7th century for the city's collapse; Aquileia
remained the seat of a patriarchate through the Middle Ages and is an inhabited comune today.
**Confidence:** high
**Why:** Attila's sack is precisely the "conquest treated as ending" error. The patriarchate the
summary itself mentions post-dates 452 by centuries.

### africa.city-tahert
**Field:** end
**Currently:** `end: 909` — fall of the Rustamid imamate.
**Should be:** no end / extant true. Tahert is Tiaret, a living Algerian city of several hundred
thousand people.
**Confidence:** high
**Why:** The Fatimid conquest ended the imamate, not the settlement. The alias field already says
"Tiaret".

### east-asia.city-otsu
**Field:** name / end / extant
**Currently:** name "Otsu", `end: 672`.
**Should be:** either name it "Ōtsu-kyō" (the 667–672 palace capital) or set `end: null`,
`extant: true`. Ōtsu is the capital of Shiga Prefecture today.
**Confidence:** high
**Why:** As written it tells the reader a major modern Japanese city ceased to exist in 672.

### east-asia.city-zhengzhou-shang
**Field:** name / end
**Currently:** name "Zhengzhou", `start: -1600`, `end: -1046`.
**Should be:** name "Zhengzhou Shang City" (as in the aliases), and end around −1300, when the
Erligang capital was abandoned; −1046 is the fall of the Shang dynasty, not of this site.
**Confidence:** medium
**Why:** Two errors compound: a living city of 12 million is given a Bronze Age end date, and the
end date borrowed from dynastic chronology outlives the site's occupation by ~250 years.

### east-asia.city-anyang-yin
**Field:** name / extant
**Currently:** name "Anyang", `end: -1046`, `extant: null`.
**Should be:** name "Yinxu" (or "Yin"), with Anyang as an alias.
**Confidence:** medium
**Why:** Same conflation as Zhengzhou: the archaeological capital ended in 1046 BCE, the modern
prefecture city of the same name did not.

### europe.city-falerii
**Field:** end
**Currently:** `end: 1500`.
**Should be:** unclear — Falerii Veteres is Civita Castellana, continuously inhabited to today;
Falerii Novi is the abandoned grid town. The row merges two settlements with two different fates.
**Confidence:** medium
**Why:** Whichever is meant, 1500 fits neither: Falerii Novi was abandoned in the early Middle Ages
and Civita Castellana never was.

### east-asia.city-buyeo-sabi
**Field:** end / extant
**Currently:** name "Buyeo", `end: 660`.
**Should be:** name "Sabi" for the Baekje capital; Buyeo is an inhabited county seat today.
**Confidence:** medium
**Why:** 660 is the Tang–Silla conquest of Baekje, not the end of the town.

### Minor cases of the same shape (low confidence individually, a real pattern together)
**Field:** end / extant
**Currently:** end dates that close out sites whose settlements continued or continue as villages
or towns: `africa.city-thysdrus` (end 700 — El Djem is a living town), `africa.city-oxyrhynchus`
(end 900 — el-Bahnasa is inhabited), `africa.city-thugga` (end 1200 — Dougga village was occupied
into the 20th century), `europe.city-abdera` (end 1000 — Avdira), `europe.city-chaeronea` (end 400),
`europe.city-eretria` (end 600 — modern Eretria), `europe.city-isca-caerleon` (end 400 — Caerleon),
`europe.city-aventicum` (end 600 — Avenches), `europe.city-devin` (end 1500 — a Bratislava borough),
`africa.city-gedi` (end 1600 vs summary "abandoned in the 17th century").
**Should be:** in each case either extend the end, or make clear the row is the ancient city rather
than the modern place.
**Confidence:** low
**Why:** Defensible as "the ancient city ended", but a reader will read "no longer exists".

---

## `extant: true` on things that are not living cities

### europe.city-aquincum
**Field:** extant / start / aliases
**Currently:** `start: -50`, `extant: true`, aliases "Buda", "Budapest".
**Should be:** `start` c. AD 40–50 (the Eravisci settlement is earlier but the Roman city is 1st
century CE); `extant` should not be true for Aquincum, which is a ruin park inside Budapest.
**Confidence:** medium
**Why:** The summary itself pivots to "medieval Buda became the Hungarian royal capital" — that is a
different, later, non-continuous settlement. Also the negative start looks like a sign error.

### americas.city-canyon-de-chelly
**Field:** kind / name
**Currently:** `kind: city`, `extant: true`, "Continuously inhabited canyon…".
**Should be:** not a city — a canyon containing many cliff dwellings and farms.
**Confidence:** high
**Why:** A canyon is a landscape, not a settlement; "White House Ruin" as an alias confirms the row
is really about a group of sites.

### africa.city-bahariya
**Field:** kind / aliases
**Currently:** `kind: city`, "Bahariya", extant true, alias "Zawiyat el-Amwat".
**Should be:** Bahariya is an oasis depression containing several villages; if a city is wanted, it
is El-Bawiti, which is missing from the aliases.
**Confidence:** medium
**Why:** Region-as-city error, plus the most likely search term (Bawiti) is absent.

### africa.city-kilwa
**Field:** extant
**Currently:** `extant: true`, no end.
**Should be:** low-confidence — Kilwa Kisiwani is a small village amid ruins; the city ended in the
16th century. Either set an end for the city or say the modern village is not the city.
**Confidence:** low
**Why:** Reader will infer a functioning Swahili metropolis.

### africa.city-hippo-regius
**Field:** extant
**Currently:** `extant: true`, alias "Annaba".
**Should be:** the ancient city is a ruin field; Annaba grew up beside rather than on it.
**Confidence:** low
**Why:** Same conflation as Aquincum, but the continuity claim is more defensible here.

---

## Not cities (individual rows; see PATTERN-1)

### NOTCITY — self-declared in the summary
**Field:** kind
**Currently:** `kind: city` on rows whose own summaries deny it:
- `africa.city-deir-el-medina` — "village of the tomb-builders … not a city"
- `africa.city-giza-workers` — "a support settlement, not a city"
- `africa.city-kahun` — "not a city"
- `africa.city-saqqara` — "a cemetery complex, not a city"
- `africa.city-nuri` — "a necropolis, not a city"
- `africa.city-mirgissa` — "a fort, not a city"
- `africa.city-semna` — "a fort, not a city"
- `africa.city-musawwarat` — "ceremonial, not a city"
- `africa.city-igbo-ukwu` — "a ritual centre, not a city"
- `africa.city-koumbi-tegdaoust-note` — "ceremonial, not a city"
- `europe.city-delphi` — "sanctuary, not a city"
- `europe.city-dodona` — "sanctuary rather than city"
- `europe.city-isthmia` — "a cult centre, not a city"
- `europe.city-jelling` — "not a city"
**Should be:** removed from the cities file, or re-typed.
**Confidence:** high
**Why:** No judgement needed; the rows contradict themselves.

### NOTCITY — not self-declared but equally clear
**Field:** kind
**Currently:** `kind: city` on:
- `europe.city-avebury` — a stone circle and ceremonial landscape
- `europe.city-durrington-walls` — a Neolithic enclosure/settlement of Stonehenge builders
- `europe.city-emain-macha` — Navan Fort, a royal ceremonial earthwork
- `central-asia.city-samye` — a monastery
- `central-asia.city-yumbulagang` — a single castle building
- `americas.city-acre-geoglyphs` — "hundreds of geometric ditched enclosures"
- `americas.city-hopewell-earthworks` — earthwork complexes, plural
- `americas.city-newark-earthworks` — an earthwork complex
- `americas.city-fort-ancient` — a hilltop enclosure
- `americas.city-san-agustin` — "dispersed funerary and ceremonial landscape"
- `americas.city-tierradentro` — "ceremonial zone" of shaft tombs
- `americas.city-sacsayhuaman` — a ceremonial fortress above Cusco (and a district of a city
  already in the file, Cusco)
- `americas.city-sitio-conte` — a burial ground
- `americas.city-marajo` — "mound complexes" across an island
**Should be:** re-typed or removed.
**Confidence:** high
**Why:** Monuments, sanctuaries, cemeteries and multi-site landscapes, exactly the categories the
objective asks to flag.

### NOTCITY — borderline (villages, hillforts, single fortresses, site networks)
**Field:** kind
**Currently:** `kind: city` on `europe.city-danebury` (hillfort), `europe.city-dunadd` (inauguration
fort), `europe.city-durrnberg` (mine and cemetery), `europe.city-gnezdovo` ("trade and burial
complex"), `europe.city-epidaurus` (sanctuary with a small town), `europe.city-jarrow` (monastery),
`central-asia.city-ayazkala` (fortress complex), `central-asia.city-toprakkala` (royal citadel),
`central-asia.city-dashly` (palace-fortress), `central-asia.city-botai` (pit-house settlement),
`central-asia.city-sintashta` and `central-asia.city-arkaim` (small fortified settlements),
`east-asia.city-banpo` ("planned Neolithic village"), `east-asia.city-sannai-maruyama` (Jomon
settlement), `americas.city-llanos-de-mojos` / `americas.city-upano-sangay` / `americas.city-kuhikugu`
(low-density site networks), `americas.city-mesa-verde` (a plateau of many villages),
`americas.city-caguana` (ceremonial plaza complex), `americas.city-cahuachi` ("largely empty between
festivals").
**Should be:** at minimum, flag as pre-urban / non-urban rather than city.
**Confidence:** medium (low for the low-density-urbanism cases, where "city" is a live scholarly claim)
**Why:** Calling Banpo or Botai a city imports 6,000 years of anachronism; the Amazonian and Puuc
garden-city cases are genuinely arguable and I would not force them.

---

## Duplicate entities entered twice

### central-asia.city-gurganj / central-asia.city-konye-urgench
**Field:** id (whole rows)
**Currently:** two rows for the same city — Gurganj `start: 300, end: 1600`, Konye-Urgench
`start: 400, end: 1600`; each lists the other's name in its aliases.
**Should be:** one row. Konye-Urgench ("Old Urgench") *is* Gurganj.
**Confidence:** high
**Why:** Two rows with conflicting start dates for one place; a reader consulting either gets a
different founding century.

### central-asia.city-afrasiab / central-asia.city-samarkand
**Field:** id (whole rows)
**Currently:** Afrasiab `start: -700, end: 1220`; Samarkand `start: -700, extant: true` with
"Afrasiab" in its aliases.
**Should be:** one row, or an explicit statement that Afrasiab is the pre-1220 mound of the same
city, not a separate settlement.
**Confidence:** medium
**Why:** As it stands, Samarkand appears to have been founded twice and destroyed once.

### east-asia.city-fenghao / east-asia.city-haojing
**Field:** id (whole rows)
**Currently:** Fenghao `-1100 → -771`, described as "twin Zhou capital complex of Feng and Hao";
Haojing `-1046 → -771`, "Western Zhou royal capital", which is the Hao half of the same complex.
**Should be:** one row, or Haojing scoped explicitly as a component of Fenghao.
**Confidence:** medium
**Why:** Overlapping rows with different starts for the same royal centre; the −1100/−1046
discrepancy is the Zhou conquest date leaking into a settlement date.

### east-asia.city-taihe-dali / east-asia.city-dali
**Field:** id
**Currently:** Taihe (Nanzhao capital, 750–1250) and Dali (Dali kingdom capital, 937–).
**Should be:** low-confidence — these are adjacent successive capitals in the same basin and the
1250 end on Taihe overlaps the whole life of Dali.
**Confidence:** low
**Why:** Defensible as two sites, but the overlap needs a note.

---

## Identifier, placement and naming errors

### africa.city-koumbi-tegdaoust-note
**Field:** id / name / start / end / kind
**Currently:** id `africa.city-koumbi-tegdaoust-note`, name "Sine-Ngayene", summary about the
Senegambian megalithic circles, `start: -300, end: 1500`.
**Should be:** the id belongs to a different place entirely (Kumbi Saleh / Tegdaoust, both of which
already have their own rows), the word "note" should not be in an id, and the Senegambian stone
circles are conventionally dated to roughly the 7th–15th centuries CE, not from 300 BCE.
**Confidence:** high
**Why:** Three independent errors in one row, including an id that will send readers to the wrong
country (Mauritania vs Senegal) and a start ~1,000 years too early.

### europe.city-cologne-dorestad
**Field:** id
**Currently:** id prefixed `cologne-`, name "Dorestad".
**Should be:** `europe.city-dorestad`. Dorestad is at Wijk bij Duurstede in the Netherlands and has
nothing to do with Cologne.
**Confidence:** high
**Why:** Copy-paste in the id; misfiles a Frisian emporium under a German city.

### europe.city-chersonesus
**Field:** aliases
**Currently:** aliases "Kherson", "Korsun", "Sevastopol".
**Should be:** drop "Kherson". Chersonesus Taurica is inside modern Sevastopol; Kherson is a
different city 200 km away founded in 1778.
**Confidence:** medium
**Why:** The single most likely way for a reader to be actively misled by an alias in this file.

### americas.city-copan
**Field:** aliases
**Currently:** aliases `["Oxwitza'", "Copan"]`.
**Should be:** "Oxwitik". Oxwitza' is Caracol's ancient name — and `americas.city-caracol` in this
same file correctly carries "Oxwitza".
**Confidence:** medium
**Why:** The same Maya toponym is assigned to two different cities in one file; one of them is wrong.

### central-asia.city-hecatompylos, central-asia.city-shahr-i-sokhta
**Field:** under
**Currently:** filed under "Central Asia & the Steppe"; both are in Iran (Semnan; Sistan).
**Should be:** an Iran / Greater Iran / Near East branch if one exists.
**Confidence:** low
**Why:** Defensible on cultural grounds (Parthian, Helmand civilisation), but a reader looking for
Iranian sites will not look in the steppe file.

### europe.city-brattahlid, europe.city-gardar-greenland
**Field:** under
**Currently:** Greenland sites filed under Europe.
**Should be:** low-confidence flag only — culturally Norse, geographically North America.
**Confidence:** low
**Why:** Worth a deliberate decision rather than an accident; both carry "Greenland" in aliases,
which suggests the author noticed.

---

## Dates that are wrong

### europe.city-kyiv
**Field:** start / bounds / dated_by / historicity
**Currently:** `start: 482`, `bounds: [472, 492]`, `dated_by: typological`.
**Should be:** late 9th century for the urban settlement (with 6th–7th century occupation traces);
482 is the anniversary date adopted in 1982 from chronicle legend and should be marked
`received` / `legendary`, not given ±10 years of archaeological precision.
**Confidence:** high
**Why:** Textbook case of a legendary founding presented as archaeology, with false precision on top.

### europe.city-frankfurt
**Field:** start
**Currently:** `start: -80`, `bounds: [-105, -55]`.
**Should be:** 1st century CE for the Roman settlement on the Domhügel, or 794 for Franconofurd.
**Confidence:** medium
**Why:** There is no 1st-century-BCE Frankfurt; the value looks like a sign or century slip, and the
summary is entirely about the medieval imperial city.

### europe.city-lindum
**Field:** start
**Currently:** `start: -60`, `bounds: [-85, -35]`.
**Should be:** c. AD 48–60 — the legionary fortress at Lincoln is post-conquest.
**Confidence:** high
**Why:** Britain had no Roman legionary colonies in 60 BCE. Sign error.

### europe.city-carnuntum
**Field:** start
**Currently:** `start: -40`, `bounds: [-50, -30]`.
**Should be:** early 1st century CE (first mentioned AD 6; legionary base from c. AD 40).
**Confidence:** medium
**Why:** Another apparent sign flip on a well-known Roman date; the summary's content (Marcus
Aurelius, Pannonia Superior) is 2nd century.

### europe.city-corinium
**Field:** start
**Currently:** `start: -50`.
**Should be:** c. AD 70 for the town (the fort is c. AD 49).
**Confidence:** medium
**Why:** Pre-conquest Cirencester was not a town; same sign-flip family as Lindum and Carnuntum.

### europe.city-carteia
**Field:** start / bounds
**Currently:** `start: -940`, `bounds: [-1081, -799]`.
**Should be:** roughly 7th century BCE for the Phoenician settlement, 171 BCE for the Roman colony
the summary describes.
**Confidence:** medium
**Why:** −940 is two to three centuries earlier than any Phoenician presence in the far west and has
no evidential basis.

### africa.city-agadez
**Field:** start
**Currently:** `start: 1100`, `dated_by: calendar`, `bounds: [null, null]`.
**Should be:** 14th–15th century; the sultanate is 15th century.
**Confidence:** medium
**Why:** ~300 years too early for a Tuareg town whose whole significance is late-medieval, and
`calendar` with no bounds implies a precision nobody has.

### americas.city-cuicuilco
**Field:** end / summary
**Currently:** `end: -100`, "buried by the Xitle lava flow".
**Should be:** the two claims cannot both stand — the Xitle eruption is dated to roughly the 3rd–4th
century CE, several hundred years after 100 BCE.
**Confidence:** medium
**Why:** Either the end date or the stated cause of abandonment is wrong; as written the city is
destroyed centuries before the volcano erupts.

### east-asia.city-changan
**Field:** start
**Currently:** `start: -1000`, `bounds: [-1020, -980]`.
**Should be:** 202/200 BCE for Han Chang'an. The Zhou capitals of the same plain are already separate
rows (`fenghao`, `haojing`).
**Confidence:** medium
**Why:** As written, Chang'an is founded ~800 years before it existed and duplicates Fenghao/Haojing.

### europe.city-dimini
**Field:** end
**Currently:** `start: -4800, end: -1100` (3,700-year span for a "Neolithic walled village").
**Should be:** roughly −4800 to −4400 for the Neolithic village; the Mycenaean material in the area
belongs to the neighbouring Bronze Age site (Iolkos/Dimini tholoi), not the same settlement.
**Confidence:** medium
**Why:** Two archaeologically distinct settlements welded into one implausible span.

### east-asia.city-jeonju
**Field:** start
**Currently:** `start: -57`, `bounds: [-107, -7]`.
**Should be:** unclear — but −57 is the legendary foundation year of Silla, which also appears as the
start of `east-asia.city-gyeongju`. Jeonju's significance is as the Later Baekje capital, 900 CE.
**Confidence:** medium
**Why:** The same annalistic date used for two unrelated Korean cities is a tell that it was reached
for rather than derived.

### east-asia.city-gimhae, east-asia.city-gyeongju, east-asia.city-pyongyang
**Field:** start / dated_by / historicity
**Currently:** Gimhae 42 (±25), Gyeongju −57 (±10), Pyongyang −1000 as "Capital of Gojoseon".
**Should be:** all three are traditional/annalistic dates; Gojoseon's capital location is contested.
Mark `received` and `legendary`/`contested`.
**Confidence:** medium
**Why:** Tight archaeological-looking bounds on foundation myths.

### central-asia.city-khyunglung, central-asia.city-yumbulagang
**Field:** start / historicity
**Currently:** Khyunglung `-500`, "Reputed capital of Zhangzhung"; Yumbulagang `-100`,
"Reputedly Tibet's oldest building".
**Should be:** both should be `contested`/`legendary`; the Yarlung dynasty dates from Tibetan
tradition are not archaeological, and the standing structure at Yumbulagang is much later.
**Confidence:** medium
**Why:** "Reputed" in the summary and no historicity flag is the caveat-lost failure the brief warns of.

### africa.city-thinis, africa.city-njimi
**Field:** dated_by / bounds
**Currently:** Thinis `-3500` with `bounds [-4025, -2975]`, `typological`, summary "site not securely
located"; Njimi `900–1400`, `typological`, summary "its site remains unidentified".
**Should be:** `received` (both are known only from texts); an unlocated site cannot be dated
typologically because there is no assemblage to type.
**Confidence:** high
**Why:** Brief item 4, in its clearest form.

### Wide-bounds / precision mismatches (low, grouped)
**Field:** bounds
**Currently:** ±450 to ±825 year bounds on Egyptian and Greek town foundations (Akhmim, Coptos,
Crocodilopolis, Elkab, Mendes, Thinis, Larissa all at ±450–525; Durankulak ±825; Knossos ±420),
against ±10 or tighter on far shakier numbers (Kyiv 482 ±10, Aksum −100 ±10, Caral −3000 ±180,
Gimhae 42 ±25). Kellis has `start: 50` with `bounds: [-1, 100]`, straddling the era boundary
asymmetrically for no reason.
**Should be:** bounds proportional to evidence, not to round-number distance from zero.
**Confidence:** low individually, medium as a pattern
**Why:** Uncertainty appears to be generated as a percentage of the date rather than from the
evidence, which is why Kyiv is more precise than Knossos.

### Other individually weak start dates (low confidence, listed for the sourcing sweep)
**Field:** start
**Currently:** `africa.city-ghat` 500 (no basis I know of for a 6th-century Ghat);
`africa.city-qasr-ibrim` −1000 (occupation generally from c. 8th century BCE);
`africa.city-ceuta` −300 (Phoenician presence is earlier, Roman Septem later);
`africa.city-bejaia` −300 (Saldae is Punic; the city that matters is Hammadid, 1067);
`europe.city-limerick` 812 (the Viking settlement is c. 922); `europe.city-esztergom` −50;
`europe.city-adrianople` −100 (Hadrianopolis is c. AD 125; the Thracian predecessor is undated);
`europe.city-aachen` −1 (the Roman baths are 1st century CE, the city Carolingian);
`central-asia.city-balkh` −1500; `central-asia.city-kabul` −1500;
`americas.city-aspero` −3700.
**Should be:** each re-examined; I would not defend the current values but I am not certain enough
to name replacements.
**Confidence:** low
**Why:** All are round numbers reached at the plausible extreme of their region's chronology.

---

## Summaries that overstate or contradict each other

### africa.city-jenne-jeno vs africa.city-dia
**Field:** summary
**Currently:** Jenne-jeno: "Africa's oldest known city south of the Sahara". Dia: "Early Middle Niger
urban cluster contemporary with and older than Jenne-jeno".
**Should be:** one of these has to yield. Also "contemporary with and older than" is internally
contradictory as a phrase.
**Confidence:** high
**Why:** Two rows in one file make incompatible priority claims; a reader hitting both learns nothing.

### africa.city-syene
**Field:** summary
**Currently:** "Granite quarry city where Eratosthenes measured the earth."
**Should be:** Eratosthenes worked in Alexandria and used a reported observation at Syene.
**Confidence:** medium
**Why:** Places a famous measurement in the wrong city.

### africa.city-askar-qatai
**Field:** name / start
**Currently:** one row for "Al-Askar and Al-Qata'i", `start: 750`.
**Should be:** two foundations — al-Askar c. 750, al-Qata'i c. 870. A single start hides the later one.
**Confidence:** medium
**Why:** Two palace-cities merged; the row cannot carry a correct date for both.

### europe.city-gipeswic
**Field:** summary
**Currently:** "Earliest English town of the Anglo-Saxon period".
**Should be:** one of the earliest — Lundenwic, Hamwic and Canterbury are all in the running and two
of them are rows in this same file.
**Confidence:** low
**Why:** Superlative the evidence will not carry.

### americas.city-santarem-tapajos
**Field:** extant / name
**Currently:** the Tapajó town, `extant: true`, name "Santarém".
**Should be:** distinguish the pre-Columbian Tapajó centre (which ended) from the Portuguese city
founded in 1661 on the site.
**Confidence:** low
**Why:** Continuity is asserted across a colonial rupture.

---

## Missing alternate names worth adding
**Field:** aliases
**Currently:** `americas.mesoamerica.aztec.tenochtitlan` — null (needs "México-Tenochtitlan",
"Mexico City"); `africa.city-katsina` — null; `africa.city-lamu` — null; `europe.city-burgos`,
`europe.city-cremona`, `europe.city-gniezno`, `europe.city-lund`, `europe.city-amalfi` — null;
`africa.city-bahariya` — missing "El-Bawiti"; `africa.city-buhen`, `africa.city-faras`,
`africa.city-semna`, `africa.city-mirgissa` — carry "flooded" instead of a real second name.
**Should be:** the modern name for each ancient city and vice versa.
**Confidence:** medium (high for Tenochtitlan)
**Why:** Tenochtitlan with no aliases at all, in a file that gives Abydos three, is the reader's
worst case: the single most-searched pre-Columbian city with no route from "Mexico City".

---

## The twenty worst

Ordered by how badly each misleads a reader.

1. **americas.mesoamerica.aztec.tenochtitlan** — the file's Constantinople: a city that became
   Mexico City is recorded as ending in 1521, with no aliases, no `extant`, and a one-off
   `under`/id format.
2. **PATTERN-1 / the fourteen self-declared non-cities** — rows whose own summaries say "not a city"
   (Saqqara, Delphi, Dodona, Isthmia, Jelling, Nuri, Semna, Mirgissa, Deir el-Medina, Kahun,
   Heit el-Ghurab, Musawwarat, Igbo-Ukwu, Sine-Ngayene).
3. **africa.city-koumbi-tegdaoust-note** — id points at Kumbi Saleh/Tegdaoust, name is Sine-Ngayene,
   the start is ~1,000 years too early, and it is not a city.
4. **europe.city-aquileia** — ended at Attila's sack in 452, ignoring the patriarchate the row itself
   names and the living comune today.
5. **central-asia.city-gurganj / konye-urgench** — the same city twice, with different founding
   centuries.
6. **europe.city-kyiv** — a legendary 482 founding given ±10 years and `typological` dating.
7. **africa.city-tahert** — a living Algerian city (Tiaret) ended at the 909 conquest of a dynasty.
8. **east-asia.city-otsu** — a modern prefectural capital ended in 672.
9. **PATTERN-2 / dated_by** — 610 `typological` rows including dozens of foundations known from dated
   texts; the field currently encodes date range, not evidence type.
10. **PATTERN-3 / historicity** — null on all 719, including six rows whose summaries say
    "legendary", "reputed" or "not securely located".
11. **europe.city-lindum** — a Roman colony in Britain dated to 60 BCE by sign error.
12. **east-asia.city-zhengzhou-shang** — a living city of millions given a −1046 end, and that end
    borrowed from dynastic chronology rather than the site.
13. **europe.city-cologne-dorestad** — Frisian emporium filed under a Cologne id.
14. **americas.city-canyon-de-chelly** — a canyon entered as an extant city.
15. **europe.city-chersonesus** — "Kherson" as an alias, pointing readers to a different city on a
    different river founded 2,200 years later.
16. **americas.city-cuicuilco** — abandonment date and stated volcanic cause separated by ~400 years.
17. **europe.city-frankfurt** — founded 80 BCE for a row entirely about the medieval imperial city.
18. **africa.city-jenne-jeno vs africa.city-dia** — mutually exclusive "oldest city south of the
    Sahara" claims, one phrased "contemporary with and older than".
19. **east-asia.city-changan** — Han Chang'an dated to 1000 BCE, duplicating the Zhou capitals that
    already have their own rows.
20. **PATTERN-4 / aliases** — governorates, provinces, "flooded", "Cerne?" and "Ghadamis nearby"
    entered as alternate names, while Tenochtitlan, Lamu and Katsina have none.

### Honest summary of confidence
The strong findings are structural and self-evident: non-cities, duplicates, id/name mismatches,
living cities with end dates, and the four field-level patterns. The date findings are strongest
where a sign or a century has obviously flipped (Lindum, Carnuntum, Frankfurt, Changan, Kyiv) and
weakest in the block of round-number early starts (Balkh −1500, Kabul −1500, Ghat 500, Ceuta −300),
which I have marked low rather than guess. Roughly consistent with the note that a third of the file
was graded low confidence: the Egyptian, Greek and Chinese cores read as sound, while the Saharan,
Tibetan, Korean-annal and Roman-Britain foundation dates are where the errors cluster.

---

## Proposed tests

Each rule below is stated so it can be implemented against the JSON as it stands, with the
violating ids from cities-1.json listed. `safe` = no legitimate exception found in 719 rows, may
fail the build. `advisory` = real exceptions exist, warn only; a named exception is given for each.

### T1 — A row whose summary denies it is a city must not have `kind: city` — `safe`
**Rule:** if `summary` matches `/not a city|rather than city|not a settlement|support settlement/i`
then `kind != "city"`.
**Violations (14):** `africa.city-deir-el-medina`, `africa.city-giza-workers`,
`africa.city-igbo-ukwu`, `africa.city-kahun`, `africa.city-koumbi-tegdaoust-note`,
`africa.city-mirgissa`, `africa.city-musawwarat`, `africa.city-nuri`, `africa.city-saqqara`,
`africa.city-semna`, `europe.city-delphi`, `europe.city-dodona`, `europe.city-isthmia`,
`europe.city-jelling`.
**Why safe:** a row cannot legitimately assert its own type is wrong. This is the cheapest rule in
the list and it catches 14 real errors today.

### T2 — Category nouns in the summary require a non-`city` kind or an explicit justification — `advisory`
**Rule:** if `summary` matches `/\b(sanctuary|necropolis|cemetery|monastery|hillfort|earthwork|
geoglyph|stone circle|canyon|oasis|palace-fortress|pit-house|plaza complex|mound complex|
ceremonial landscape)\b/i` and `kind == "city"`, warn.
**Violations worth acting on:** `europe.city-avebury`, `europe.city-durrington-walls`,
`europe.city-emain-macha`, `europe.city-danebury`, `europe.city-durrnberg`, `europe.city-gnezdovo`,
`central-asia.city-samye`, `central-asia.city-yumbulagang`, `central-asia.city-botai`,
`central-asia.city-dashly`, `central-asia.city-toprakkala`, `americas.city-acre-geoglyphs`,
`americas.city-hopewell-earthworks`, `americas.city-newark-earthworks`, `americas.city-fort-ancient`,
`americas.city-san-agustin`, `americas.city-tierradentro`, `americas.city-sacsayhuaman`,
`americas.city-sitio-conte`, `americas.city-marajo`, `americas.city-canyon-de-chelly`,
`africa.city-bahariya`.
**Legitimate exception:** `europe.city-eleusis`, `europe.city-aquae-sulis`, `europe.city-iona`,
`europe.city-cerveteri`, `americas.city-moundville` — real cities whose summaries happen to mention
a sanctuary, a cemetery or a monastery inside them. That is why this is advisory and T1 is not.

### T3 — Legendary, traditional or unlocated entities must carry a `historicity` value — `safe`
**Rule:** if `summary` matches `/legendar|reputed|traditional (capital|home)|not securely located|
remains unidentified|probable capital|candidate for/i` then `historicity != null`.
**Violations (13):** `europe.city-alba-longa`, `europe.city-lavinium`, `africa.city-thinis`,
`africa.city-njimi`, `africa.city-niani`, `africa.city-kumbi-saleh`,
`central-asia.city-khyunglung`, `central-asia.city-yumbulagang`, `east-asia.city-taosi`,
`east-asia.city-yoshinogari`, `europe.city-heuneburg`, `east-asia.city-kaifeng`,
`central-asia.city-merv`.
**Why safe:** the rule does not decide *which* value; it only requires that a row hedging in prose
must hedge in the field a machine reads. `historicity: null` currently means "accepted" for all 719
rows, including Alba Longa. (The Kaifeng and Merv hits are on the word "possibly" in a superlative
rather than on existence — the fix there is to loosen the summary or set the field, either way a
human decision, which is the point.)

### T4 — `dated_by` must not be a pure function of `bounds` nullity — `safe`
**Rule:** across the file, `dated_by == "calendar"` must not be perfectly correlated with
`bounds == [null, null]`. Implement as: at least one `calendar` row with numeric bounds, and at
least one `typological` row without, must exist — or, better, per-row: a foundation whose summary
names a documented founder, dynasty or dated event should be `calendar`.
**Violations:** currently 109/109 `calendar` rows have null bounds and 610/610 `typological` rows
have numeric bounds — 0 exceptions in either direction. `dated_by` is therefore carrying no
information beyond "is this date fuzzy", which is what `bounds` already says.
**Worst individual consequences:** `africa.city-cairo` (969, Fatimid foundation),
`africa.city-kairouan` (670), `africa.city-fez` (789), `africa.city-alexandria` (−331),
`europe.city-lugdunum` (−43), `europe.city-londinium` (47), `east-asia.city-kyoto` (794),
`east-asia.city-nara` (710), `central-asia.city-ordu-baliq` (744) — all documented calendar dates
marked `typological`.

### T5 — `bounds` width must not be a fixed percentage of the date's distance from zero — `safe`
**Rule:** compute `ratio = (bounds[1] - bounds[0]) / max(1, abs(start))` for every bounded row.
Fail if more than 20% of rows share any single ratio rounded to two decimals.
**Violations:** 187 rows at exactly 0.12, 149 at 0.30, 87 at 0.04, 31 at 0.50, 22 at 0.33, 21 at
1.00. Uncertainty was generated arithmetically from the year, not from evidence.
**Consequences already visible:** `europe.city-kyiv` 482 gets ±10 while `europe.city-knossos` −7000
gets ±420; `africa.city-akhmim` −3000 gets ±450; `africa.city-thinis` — a site nobody can locate —
gets ±525 as if that were a measurement.

### T6 — A city ending in a known conquest or dynastic-fall year must say it was abandoned — `advisory`
**Rule:** maintain a list of conquest/annexation years; if `end` is within ±1 of one of them, require
`summary` to match `/abandon|destroy|razed|erased|annihilat|sacked|burned|burnt|never rebuilt|
depopulat|lost to/i`, else warn.
**Violations (10 real):** `americas.mesoamerica.aztec.tenochtitlan` (1521 — became Mexico City),
`africa.city-tahert` (909 — is Tiaret), `east-asia.city-otsu` (672), `east-asia.city-buyeo-sabi`
(660), `east-asia.city-anyang-yin` and `east-asia.city-zhengzhou-shang` (−1046, the fall of the
Shang used as a settlement end), `east-asia.city-goryeong` (562, "absorbed by Silla"),
`east-asia.city-liao-shangjing` (1220), `americas.city-tenayuca` (1521), `americas.city-yagul`
(1521), plus `europe.city-capua` (841) and `africa.city-carthage` (698) to review.
**Legitimate exception:** `americas.city-iximche` (1524), `americas.city-zaculeu` (1525),
`americas.city-qumarkaj` (1524) — genuinely abandoned at or just after conquest, correctly ended.
Hence advisory.

### T7 — A city whose summary says it was abandoned must have a non-null `end` — `safe`
**Rule:** if `summary` matches the abandonment pattern in T6 then `end != null` and
`extant != true`.
**Violations (1):** `americas.city-azcapotzalco` — "…until the Aztec Triple Alliance destroyed it in
1428", with `end: null` and `extant: true`.
**Why safe:** even Azcapotzalco is arguably a true positive rather than an exception — the polity was
destroyed, the town became a Mexico City borough, and the summary should say which. One violation
today, but it is the mirror of T6 and cheap to keep.

### T8 — `extant: true` iff `end: null` — `safe`
**Rule:** `extant == true` requires `end == null`; `end == null` requires `extant == true`.
**Violations:** none — 0 rows break it in either direction (all 285 `extant: true` rows have null
end, all 434 null-extant rows have an end).
**Why propose it anyway:** it is the invariant the objective asks for, it currently holds, and
locking it in prevents the Tenochtitlan repair from being done half-way (someone setting
`extant: true` while leaving `end: 1521`).

### T9 — An id's slug must match its name or one of its aliases — `advisory`
**Rule:** the portion of `id` after `city-`, with hyphens removed and diacritics folded, must be a
substring of the folded `name` or of a folded alias.
**Violations (7):** `africa.city-koumbi-tegdaoust-note` ~ "Sine-Ngayene" (the real bug — id points at
two other cities that have their own rows, and contains the word "note"),
`europe.city-cologne-dorestad` ~ "Dorestad" (caught by a variant of this rule: id contains a second
city's name), `americas.city-east-st-louis-mound-group` ~ "…Mound Center",
`americas.city-hopewell-earthworks` ~ "Hopewell Ceremonial Earthworks",
`east-asia.city-jin-shangjing` ~ "Shangjing Huining", `east-asia.city-liao-shangjing` ~ "Shangjing
Linhuang", `europe.city-citania-briteiros` ~ "Citânia de Briteiros",
`americas.city-betatakin-keet-seel` ~ "Betatakin and Keet Seel".
**Legitimate exception:** the two Shangjing rows, where the dynasty prefix in the id usefully
disambiguates two capitals with the same name. Advisory for that reason.

### T10 — If row A lists row B's exact name as an alias, one of them is a duplicate — `advisory`
**Rule:** flag any pair where `aliases[i]` of A equals `name` of B (case-folded), especially when the
pair also shares a `start` or an `end`.
**Violations that are real duplicates (3):** `central-asia.city-afrasiab` ↔
`central-asia.city-samarkand` (each names the other, identical `start: -700`),
`central-asia.city-konye-urgench` ↔ `central-asia.city-gurganj` (each names the other, identical
`end: 1600`), `east-asia.city-taihe-dali` ↔ `east-asia.city-dali`.
**Legitimate exception:** 34 further hits are correct — `americas.city-pisac` and six other Inca
sites carry "Cusco" as a location alias, `africa.city-fustat` carries "Cairo", `europe.city-londinium`
carries "Lundenwic". Adding the shared-`start`-or-`end` condition removes almost all of them, which
is why the threshold matters.
**Note:** this test only works while T11 is unfixed; once location strings leave `aliases`, the rule
becomes nearly `safe`.

### T11 — `aliases` may contain only names, not places or annotations — `advisory`
**Rule:** reject an alias that matches `/nearby|flooded|\?$|\barea\b|province|district|
(County|Region|Oblast|Governorate|Valley|Bay|Delta|Islands|coast|capital)$/`.
**Violations (59 alias values across ~55 rows).** The unambiguous ones: `africa.city-buhen`
("flooded by Lake Nasser"), `africa.city-faras`, `africa.city-semna`, `africa.city-mirgissa`
("flooded"), `africa.city-mogador` ("Cerne?"), `africa.city-ghat` ("Ghadamis nearby"),
`africa.city-kerma` ("Doukki Gel nearby"), `africa.city-raqqada` ("Sabra al-Mansuriyya nearby"),
`africa.city-thinis` ("Girga area"), `europe.city-alba-longa` ("Castel Gandolfo area"),
`europe.city-augusta-raurica` ("Basel area"), plus ~45 province/region strings
(`central-asia.city-*` "…Region"/"Oblast", `americas.city-*` "…Valley", `europe.city-italica`
"Seville province", `europe.city-conimbriga` "Coimbra district").
**Legitimate exception:** `central-asia.city-itil` "Khazar capital" and `east-asia.city-taihe-dali`
"Nanzhao capital" are how those sites are actually referred to in the literature, so a blanket fail
would lose real search terms. Advisory, with the location strings split into a proper field.

### T12 — Every city should have at least one alias — `advisory`
**Rule:** `len(aliases or []) >= 1`.
**Violations (8):** `americas.mesoamerica.aztec.tenochtitlan`, `africa.city-katsina`,
`africa.city-lamu`, `europe.city-amalfi`, `europe.city-burgos`, `europe.city-cremona`,
`europe.city-gniezno`, `europe.city-lund`.
**Legitimate exception:** Amalfi, Cremona and Lund genuinely have no widely used second name, so
this can only ever warn. It is worth having solely because it catches Tenochtitlan, the single
worst alias gap in the file.

### T13 — A Roman or post-Roman foundation must not have a negative start — `advisory`
**Rule:** if `summary` matches `/Roman colony|legionary|legionary fortress|colonia|veteran colony|
Roman (town|foundation|fort)/i` and `start < 0`, warn. Tighten to `start < -60` for provinces
conquered after 60 BCE (Britain, Pannonia, Dacia, Mauretania): a city in Britain with a Roman-founded
summary and `start < 0` is always wrong.
**Violations:** `europe.city-lindum` (−60, Lincoln), `europe.city-corinium` (−50, Cirencester),
`europe.city-carnuntum` (−40), `europe.city-aquincum` (−50), `europe.city-durovernum` (−50),
`europe.city-calleva` (−50), `europe.city-isca-dumnoniorum` (55 — correct, shows the rule's shape),
`europe.city-frankfurt` (−80).
**Legitimate exception:** `europe.city-durovernum` and `europe.city-calleva` had real pre-conquest
Iron Age settlements, so a negative start is defensible for them even though the summary is Roman.
Britain-specific tightening turns the clear cases (Lindum) into hard failures.

### T14 — A founding date must not precede plausible sedentism for its region — `advisory`
**Rule:** per-region floor on `start`, e.g. Sahel/West Africa −2000, Ethiopian highlands −1500,
Bantu southern Africa 200 CE, North America (Southwest) −1000, Amazonia −1000,
Andes −4000, Mongolian steppe 500 CE, Tibet −500, Japan −4000 (Jomon sedentism), Northern Europe
−5000, Aegean/Anatolia −7500. Fail if `start` precedes the floor for the row's region.
**Violations under those floors:** none in this file survive the floors as drawn — the closest calls
are `europe.city-knossos` (−7000, correct), `europe.city-karanovo` (−6200, correct) and
`central-asia.city-namazgadepe` (−4500, correct), all of which are genuinely that old.
**Why still worth adding:** it is the rule the objective asks for, and it would have caught
`africa.city-koumbi-tegdaoust-note` if the Senegambian floor is set at 1 CE — the row currently
claims a 300 BCE start for a megalithic tradition whose earliest phase is roughly a millennium later.
Advisory because regional floors are themselves contested and will produce false positives on
exactly the frontier sites that matter most.

### T15 — A row's end must not be earlier than a later event named in its own summary — `advisory`
**Rule:** extract four-digit years from `summary`; fail if any exceeds `end` (or if any exists and
`end == null` alongside abandonment language, per T7).
**Violations:** `africa.city-gedi` (`end: 1600`, summary "abandoned in the 17th century"),
`europe.city-aquileia` (`end: 452`, summary "patriarchate", an institution of the 6th–15th
centuries), `americas.city-cuicuilco` (`end: -100`, summary "buried by the Xitle lava flow", a
3rd–4th century CE event — this one needs an event-date table, not a regex).
**Legitimate exception:** summaries that mention a later excavation, rediscovery or naming
(`africa.city-rosetta` "later namesake of the trilingual stone", `east-asia.city-kharakhoto`
"recovered from the sands in 1908") — so the rule must ignore years in discovery clauses, which is
why it can only warn.

### Which of these would have caught what
T1, T3, T6, T7, T9 and T10 between them catch every high-confidence finding in this review except
the pure date errors. T4 and T5 do not catch a single individual claim but explain why the date
metadata cannot be trusted anywhere in the file, which is worth more than any one correction. T14 is
the rule the objective asked for and is also the weakest one here — I would ship it advisory-only and
expect to argue about its thresholds.
