# Correctness review: periods (522 entries)

Judgement pass, no web search. Emphasis on Japanese nengō, Chinese/Korean/Vietnamese period and
reign-era dates, and boundary consistency against parents.

## Headline

**The nengō year values are, with two or three exceptions, correct.** I checked all 248 Japanese
era/period rows against the standard nengō sequence year by year. Asuka (5), Nara (13), Kamakura
(49), Edo (35), Azuchi–Momoyama (3), modern (5) and the Muromachi Northern and Southern chains
(49) all abut correctly and match the received dates. That is a good result and worth saying plainly
before the complaints.

**The nengō metadata is systematically wrong for exactly 51 of them.** Every Asuka, Nara, and
pre-1028 Heian nengō carries `dated_by: unknown` and a fabricated ±25-year uncertainty window. The
identical error, at ±25 or ±50, appears on Wang Mang's Xin interregnum, Capetian France, and four of
the five Phoenician sub-periods. These are documentary calendar dates known to the day. This is the
single largest and most mechanical defect in the file.

---

## Patterns (stated once, not repeated per entry)

### P1. Fabricated ±25-year uncertainty on nengō whose dates are documentary

**Field:** `bounds` and `dated_by`
**Currently:** 51 nengō rows have `dated_by: unknown` and `bounds` of exactly start−25 / start+25.
**Should be:** `bounds: [null, null]`, `dated_by: calendar` — as the other 197 Japanese rows
already correctly have.
**Confidence:** high
**Why:** Era changes are recorded to the day in the *Shoku Nihongi*, *Nihon Kiryaku* and the
kugyō registers. Saying Wadō began somewhere in 683–733 is not caution, it is misinformation: the
proclamation is dated Wadō 1/1/11. The split is also arbitrary — Chōgen (1028) onward is already
`calendar` with null bounds, so the file contradicts itself about the same class of fact.

Violating ids: `east-asia.japan.asuka.hakuchi`, `.keiun`, `.shucho`, `.taiho`, `.taika`;
`east-asia.japan.nara.enryaku`, `.hoki`, `.jingo-keiun`, `.jinki`, `.reiki`, `.ten-o`, `.tenpyo`,
`.tenpyo-hoji`, `.tenpyo-jingo`, `.tenpyo-kanpo`, `.tenpyo-shoho`, `.wado`, `.yoro`;
`east-asia.japan.heian.anna`, `.choho-heian`, `.chotoku`, `.daido`, `.eien`, `.eikan`, `.eiso`,
`.encho`, `.engi`, `.gangyo`, `.jogan`, `.jogen-heian1`, `.johei`, `.jowa-heian`, `.kanna`,
`.kanpyo-heian`, `.kasho-heian`, `.koho`, `.konin`, `.ninju`, `.ninna`, `.owa`, `.saiko`,
`.shoryaku`, `.shotai`, `.ten-an`, `.ten-en`, `.tencho`, `.tengen`, `.tengyo`, `.tenroku`,
`.tenryaku`, `.tentoku`.

Two sub-cases are especially bad: `east-asia.japan.nara.tenpyo-kanpo` is a **three-month** era
(749/4–749/7), given a fifty-year window; and `east-asia.japan.asuka.shucho` is a **single-year**
era (686) given 661–711.

### P2. The same fabricated window on non-Japanese dates that are equally exact

**Confidence:** high
**Why:** `east-asia.china.han.xin` (9–23 CE, Wang Mang) carries `bounds: [-16, 34]` — a window
that crosses the BC/AD boundary for a usurpation dated to the day in the *Han shu*. The Phoenician
sub-periods are pinned to events with absolute dates: 883 BC (Ashurnasirpal II's accession),
612 BC (fall of Nineveh), 539 BC (Cyrus takes Babylon), 332 BC (Alexander at Tyre); all four carry
±25 or ±50 and `dated_by: unknown`. `europe.western.france.capetian` starts 987, the election of
Hugh Capet, and carries 962–1012.

Violating ids: `east-asia.china.han.xin`, `west-asia.mesopotamia.phoenicia.assyrian-period`,
`.babylonian-period`, `.persian-period`, `europe.western.france.capetian`.

### P3. `radiocarbon-uncalibrated` on values that are plainly calibrated

**Confidence:** medium
**Why:** Fourteen rows claim uncalibrated radiocarbon but carry calendar-scale figures. Neolithic
Jericho at −8300 to −7300 is the *calibrated* PPNA range; the uncalibrated figures are roughly
7000–6000 bc. Same mismatch at `west-asia.prehistory.ain-ghazal` (−8400/−6600),
`europe.prehistory.lascaux` (−19550, i.e. ~17,000 bp calibrated), `east-asia.china.neolithic.hongshan`
(−4551/−2851 — every other Chinese Neolithic row in the file is `radiocarbon-calibrated`), and the
three `africa.prehistory.nabta-playa.*` sub-phases. Either the label or the numbers are wrong;
the numbers look right, so the label is the error.
Also: `africa.prehistory.enkapune-ya-muto`, `africa.prehistory.ishango`,
`africa.prehistory.wadi-kubbaniya`, `americas.prehistory.cactus-hill`,
`americas.prehistory.las-vegas-culture`, `southeast-asia.prehistory.hoabinhian`,
`southeast-asia.prehistory.yangtze-rice`.

### P4. Bare nengō with nothing attached

**Confidence:** high that this is a real defect, medium that it belongs in this review
**Why:** 218 of the 248 Japanese era rows have a null summary, no aliases, no ruler, and no
`historicity`. A reader arriving at `east-asia.japan.heian.kaho` learns that Kahō ran 1094–1097 and
nothing else — not which emperor, not why the era was changed, not that the name is a Chinese-classic
allusion. The brief's exception applies: an era-name row whose only content is two years only makes
sense alongside the reign it dates. This matches the prior audit's 256-of-312 finding. Not a
hundred separate findings, one structural one.

### P5. Consequence of P4: no disambiguation on the two Kamakura rival eras

`east-asia.japan.kamakura.gentoku` (1329–1332) and `east-asia.japan.kamakura.genko-kamakura2`
(1331–1334) overlap, correctly, because Go-Daigo proclaimed Genkō in 1331 while the Jimyōin line
kept Gentoku to 1332. Every equivalent Muromachi row is labelled "Northern Court nengō" /
"Southern Court nengō"; these two are not, so the overlap reads as an error rather than the fact it
is. **Confidence:** medium.

---

## Findings

### east-asia.japan.kenmu.kenmu-era
**Field:** `end`
**Currently:** Kenmu 1334 → 1336
**Should be:** 1338, or the row should be split into a Southern usage (1334–1336) and a Northern
usage (1334–1338)
**Confidence:** high
**Why:** The Southern court abandoned Kenmu for Engen in 1336, but the Northern court kept counting
Kenmu until Ryakuō in 1338. As it stands the Northern chain has a two-year hole: Kenmu ends 1336 and
`east-asia.japan.muromachi.ryakuo` starts 1338, with nothing in between. This is the one genuine gap
in the whole Japanese sequence.

### east-asia.japan.heian.juei
**Field:** `end` (or missing summary)
**Currently:** Juei 1182 → 1185, overlapping `east-asia.japan.heian.genryaku` (1184–1185)
**Should be:** either `end: 1184`, or a summary saying the Taira continued to date by Juei in the
west after the Kyoto court adopted Genryaku in 1184
**Confidence:** medium
**Why:** The overlap is historically real but unexplained, and it is the only overlap in the file
outside the labelled Nanboku-chō rows. A reader cannot tell whether this is the Genpei War
complication or a typo.

### east-asia.japan.muromachi.shokei
**Field:** `under`
**Currently:** Shōkei 1332–1333, filed under Muromachi Period
**Should be:** under Kamakura, alongside `east-asia.japan.kamakura.genko-kamakura2`
**Confidence:** high
**Why:** Shōkei is the Jimyōin-line era proclaimed against Go-Daigo's Genkō and ended when Kamakura
fell in 1333. It sits entirely three years before the Muromachi period begins in 1336. A period
cannot precede its own parent.

### east-asia.japan.kamakura.genko-kamakura2
**Field:** `end` vs `under`
**Currently:** Genkō 1331–1334 under Kamakura Period
**Should be:** unclear — the era genuinely runs to 1334 but the Kamakura bakufu fell in 1333
**Confidence:** medium
**Why:** The year values are right; the placement makes the child outlive the parent polity. This is
the standard awkwardness of the Kenmu Restoration and should be flagged in a summary rather than
silently left as a boundary violation.

### east-asia.japan.azuchi-momoyama.keicho
**Field:** `under`
**Currently:** Keichō 1596–1615 under Azuchi–Momoyama Period
**Should be:** flagged as spanning Azuchi–Momoyama and Edo, or split at 1603
**Confidence:** medium
**Why:** Azuchi–Momoyama ends in 1600 or 1603 on any reckoning. Keichō covers Sekigahara, the
founding of the Tokugawa bakufu, and the Siege of Osaka; twelve of its nineteen years are Edo
period. A reader looking for the era of the Osaka campaigns will not look under Azuchi–Momoyama.

### east-asia.japan.nara.enryaku
**Field:** `under`
**Currently:** Enryaku 782–806 under Nara Period
**Should be:** flagged as spanning Nara and Heian
**Confidence:** medium
**Why:** Enryaku is the era in which the capital moved to Heian-kyō (794). Twelve of its
twenty-four years are the early Heian period; it is the era name Heian historians use most.

### east-asia.japan.heian.tenroku / east-asia.japan.heian.ten-en
**Field:** `end` / `start`
**Currently:** Tenroku 970–974, Ten'en 974–976
**Should be:** 973 for both, on the usual convention
**Confidence:** low
**Why:** Ten'en was proclaimed in the twelfth month of Tenroku 4, i.e. December 973 in the Japanese
calendar, which converts to January 974 Julian. Standard nengō tables give 973. The file appears to
be using Julian conversion consistently (see the next entry), so this may be a deliberate convention
rather than an error — but it should be documented, because it disagrees with every printed table.

### east-asia.japan.muromachi.kokoku / east-asia.japan.muromachi.shohei
**Field:** `end` / `start`
**Currently:** Kōkoku 1340–1347, Shōhei 1347–1370
**Should be:** 1346 for both, on the usual convention
**Confidence:** low
**Why:** Same mechanism — Shōhei was proclaimed in the twelfth month of Kōkoku 7 (December 1346),
which is January 1347 Julian. Consistency with the Tenroku/Ten'en case suggests convention, not
error, but the two together are the only places the file disagrees with the standard tables.

### east-asia.china.zhou.eastern.warring-states
**Field:** `under` (or `end`)
**Currently:** Warring States 475–221 BC, filed beneath Eastern Zhou (770–256 BC)
**Should be:** unclear — the child outlives the parent by 35 years
**Confidence:** medium
**Why:** The last Zhou king was deposed in 256 BC; the Warring States period conventionally runs to
the Qin unification in 221. The two are not in a containment relation, so filing one inside the
other guarantees a contradiction. Either scope Warring States to 475–256 under Eastern Zhou, or lift
it to a sibling of the Zhou.

### east-asia.china.neolithic.cishan
**Field:** `summary`
**Currently:** "…whose storage pits produced the claim that cereal farming here began at the
Pleistocene boundary."
**Should be:** early Holocene, or "ten thousand years ago"
**Confidence:** high
**Why:** The Pleistocene ends at 11,700 BP, c. 9700 BC. The Cishan millet claim is c. 10,000 BP
(8000 BC) and the row itself dates the culture to 6050–5050 BC. The summary overstates by roughly
two millennia at best, and mislabels the epoch.

### east-asia.china.neolithic.longshan
**Field:** `dated_by`
**Currently:** `typological`
**Should be:** `radiocarbon-calibrated`
**Confidence:** medium
**Why:** Longshan's 2600–1900 BC span is a radiocarbon chronology; it is one of the better-dated
Chinese Neolithic sequences. Every sibling row in `east-asia.china.neolithic.*` is
`radiocarbon-calibrated`. Black-pottery typology is how sites are *assigned* to Longshan, not how
the period is dated.

### east-asia.china.neolithic.shijiahe
**Field:** `start`
**Currently:** −2900
**Should be:** c. −2500
**Confidence:** medium
**Why:** Shijiahe culture proper is c. 2500–2000 BC; 2900–2500 BC in the middle Yangtze is
Youziling. The summary says "contemporary with Longshan further north", and the row itself puts
Longshan at 2600–1900 — the start dates disagree with the summary's own claim.

### east-asia.china.neolithic.hongshan
**Field:** `dated_by`
**Currently:** `radiocarbon-uncalibrated`
**Should be:** `radiocarbon-calibrated`
**Confidence:** medium
**Why:** See P3. −4551/−2851 is the calibrated range; the odd trailing 51 also suggests a BP→BC
conversion, which only makes sense for calibrated dates.

### global.neolithic.agricultural-revolution.mesoamerica
**Field:** `summary`
**Currently:** "the squash predates maize by over four thousand years"
**Should be:** roughly a thousand years
**Confidence:** high
**Why:** Domesticated *Cucurbita pepo* at Guilá Naquitz is c. 10,000 BP; the Balsas maize evidence is
c. 9,000 BP. The gap is on the order of one millennium, not four. The row's own span (−8051 to
−4301) does not accommodate a four-thousand-year internal gap either.

### global.paleolithic.later-stone-age
**Field:** `end` (or `summary`)
**Currently:** end −10050, summary "continues into the historical period"
**Should be:** an end in the last two thousand years, or `null`
**Confidence:** high
**Why:** The row contradicts itself in adjacent fields. LSA industries continue to the ethnographic
present in parts of southern and eastern Africa; ending at 10,050 BC cuts off nine tenths of the
tradition the summary describes.

### west-asia.arabia.pre-islamic.saba.marib-dam
**Field:** `end`
**Currently:** 300
**Should be:** c. 570, or `null`
**Confidence:** medium-high
**Why:** The summary says "whose failure became a parable" — the parable (the Sayl al-ʿArim of
Qur'an 34) refers to the final sixth-century CE collapse, and the Abraha inscription records a
breach and repair in 548. An end date of 300 CE excludes the very event the summary is about.

### africa.prehistory.nok
**Field:** `end`
**Currently:** −1
**Should be:** c. 200 CE (or 300 CE)
**Confidence:** medium
**Why:** Nok terracotta and iron production continue into the early centuries CE. An end of exactly
1 BC looks like a placeholder produced by an era-boundary rule rather than a date anyone asserts.

### americas.mesoamerica.maya.classic.tikal
**Field:** `start`
**Currently:** 600
**Should be:** c. −600 for the site, or c. 250 if the row means Tikal's Classic apogee
**Confidence:** medium-high
**Why:** Tikal is named as a place, not a phase, and the summary calls it "the largest excavated
Classic Maya city". Its dynastic sequence begins in the first century CE (Yax Ehb' Xook), Stela 29
is dated 292 CE, and occupation begins in the Middle Preclassic. Starting at 600 erases the entire
Early Classic including the Teotihuacan entrada of 378.

### americas.andes.inca.machu-picchu
**Field:** `bounds`
**Currently:** `[1450, 1450]`
**Should be:** `[null, null]`, or a real interval such as 1420–1450
**Confidence:** high
**Why:** A zero-width uncertainty interval is not an uncertainty statement. The AMS programme on the
site gives an occupation from c. 1420, i.e. the start is *less* certain than the point value, not
infinitely certain.

### africa.prehistory.taforalt
**Field:** `bounds`
**Currently:** `[-19300, null]`
**Should be:** a closed interval or `[null, null]`
**Confidence:** medium
**Why:** A one-sided bound on a start date reads as "no later than nothing", which is not a claim.
Taforalt is described in its own summary as the most extensively radiocarbon-dated LSA site in North
Africa, so a symmetric interval is available.

### central-asia.prehistory.bmac.gonur-depe
**Field:** `start`/`end` vs `under`
**Currently:** Gonur Depe −2300 to −1500, inside BMAC −2200 to −1700
**Should be:** widen BMAC to c. 2300–1500, or narrow Gonur
**Confidence:** medium
**Why:** The type site of the Oxus civilisation cannot begin a century before, and end two centuries
after, the complex it defines. Gonur's own span is the better one; the parent is too narrow.

### africa.prehistory.nabta-playa.terminal-neolithic
**Field:** `end` vs parent
**Currently:** Terminal Neolithic ends −3451; parent Nabta Playa ends −4251
**Should be:** extend the parent to c. −3450
**Confidence:** high
**Why:** A sub-phase running eight centuries past the end of the site it belongs to. One of the two
is wrong and the sub-phase sequence (middle → late → terminal, 6151→3451) is internally consistent,
so the parent's end is the error.

### west-asia.prehistory.late-chalcolithic-mesopotamia.jemdet-nasr
**Field:** `start`
**Currently:** −3200
**Should be:** c. −3100
**Confidence:** medium
**Why:** Jemdet Nasr is defined as the period *between* Uruk and Early Dynastic — its own summary
says so — but 3200 overlaps the Uruk period, which the sibling rows end at 3100. Consecutive
Mesopotamian periods should not overlap by a century.

### west-asia.prehistory.late-chalcolithic-mesopotamia.uruk-period.proto-cuneiform
**Field:** `end` vs `under`
**Currently:** Proto-Cuneiform −3350 to −3000, filed under Uruk Period
**Should be:** unclear — the Uruk IV/III script tradition genuinely runs past the end of the Uruk
period as the file draws it
**Confidence:** low-medium
**Why:** Child ends a century after its parent. Defensible in substance, but as filed it is a
boundary contradiction.

### south-asia.indus.deurbanisation
**Field:** `start`
**Currently:** −2200
**Should be:** c. −1900
**Confidence:** medium
**Why:** The row's siblings put the Mature Harappan, Mohenjo-daro and Lothal all at their full
extent until 1900. A deurbanisation beginning in 2200 means the cities were being abandoned for
three centuries while the file simultaneously says they were at maximum extent. The standard span
for the process is 1900–1700/1600.

### south-asia.indus.late
**Field:** `start`
**Currently:** −1800
**Should be:** −1900
**Confidence:** medium
**Why:** Mature Harappan ends 1900 and Late Harappan starts 1800, leaving a century in which the
Indus civilisation is in neither phase. The Localization Era conventionally begins at 1900.

### south-asia.prehistory.mehrgarh
**Field:** `end`
**Currently:** −4650
**Should be:** c. −2600
**Confidence:** medium
**Why:** The row is titled for the site, not for Period I. Mehrgarh is occupied through Periods
II–VII to c. 2600 BC, when it is abandoned in favour of Nausharo. Ending at 4650 removes the
ceramic Neolithic and Chalcolithic sequence that makes the site important.

### americas.prehistory.old-copper-complex
**Field:** `start`
**Currently:** −7551
**Should be:** c. −6500 at the earliest
**Confidence:** medium
**Why:** Even the recent revision pushing Great Lakes native-copper working back only reaches c.
8,500 years ago (6500 BC); 7551 BC is 9,500 BP, older than any published claim. The traditional
range is 4000–1000 BC.

### americas.prehistory.paleoindian
**Field:** `start` and `end`
**Currently:** −11250 to −9501
**Should be:** c. −13000 to −8000
**Confidence:** medium
**Why:** As drawn, Paleoindian starts after `americas.prehistory.pre-clovis` (−14050) and after
`americas.prehistory.clovis` begins (−11100 is inside it, but only just), excludes Monte Verde and
Cooper's Ferry entirely, and ends a thousand years before
`americas.prehistory.archaic` starts (−8500), leaving a gap with no period in it.

### americas.prehistory.archaic
**Field:** `end`
**Currently:** 500
**Should be:** c. −1000
**Confidence:** medium
**Why:** The Archaic ends with the Woodland in the east and the Formative elsewhere; 500 CE puts it
concurrent with Hopewell and, in this file, with the start of Classic Maya. The row also overlaps
`americas.prehistory.poverty-point` and `watson-brake`, which is fine, but the late end is not.

### africa.prehistory.pinnacle-point
**Field:** `start`
**Currently:** −90050
**Should be:** c. −162000
**Confidence:** medium
**Why:** The summary's headline claims — earliest evidence for marine resource use and for heat
treatment of silcrete — rest on PP13B and PP5-6 levels dated to c. 164 ka and c. 72 ka
respectively. A start at 90 ka excludes the 164 ka evidence the summary is built on.

### southeast-asia.prehistory.yangtze-rice
**Field:** `under`
**Currently:** Southeast Asian Prehistory
**Should be:** East Asia (China), or merged with
`global.neolithic.agricultural-revolution.yangtze`
**Confidence:** high
**Why:** The lower Yangtze is in China. The file already has the same process filed correctly under
the global Neolithic node with a different span (−8051 to −2351 there, −10550 to −5051 here), so
this is both a misplacement and a duplicate with inconsistent dates.

### west-asia.anatolia.hittites.hattusa
**Field:** `dated_by`
**Currently:** `typological`
**Should be:** `calendar`
**Confidence:** medium
**Why:** Hattusa's chronology comes from the royal archives found in it — the best textual
chronology in Bronze Age Anatolia. Typology is not what dates the Hittite capital.

### west-asia.iran.elam.linear-elamite
**Field:** `summary`
**Currently:** "A later Iranian script, claimed in 2022 to have been deciphered as the oldest purely
phonographic writing known."
**Should be:** drop "later", or say "later than Proto-Elamite"
**Confidence:** low
**Why:** "Later" and "oldest known" in one sentence read as a contradiction. The intended sense is
presumably later than Proto-Elamite, which the sibling row dates to 3300–2900.

### europe.mediterranean.greece.archaic
**Field:** `dated_by`
**Currently:** `calendar`
**Should be:** `received`
**Confidence:** low-medium
**Why:** 800 BC is a modern periodisation convention, not a documentary date; 480 (Salamis) is.
Compare `europe.mediterranean.greece.dark-age`, which is `unknown`, and the Vedic rows, which
correctly use `received` for exactly this kind of scholarly convention.

### africa.nile.kush.napatan
**Field:** `start`
**Currently:** −1070
**Should be:** c. −750, with 1070–750 left as the post-New-Kingdom interval
**Confidence:** low-medium
**Why:** 1070 BC is the end of Egyptian New Kingdom control, not the beginning of the Napatan state.
The Napatan phase is conventionally dated from the el-Kurru royal cemetery and Kashta/Piye, c.
800–750 BC. As drawn the row silently absorbs three dark centuries.

### europe.prehistory.cardial
**Field:** `start`
**Currently:** −5800
**Should be:** c. −5600
**Confidence:** low
**Why:** Impressed Ware appears in the Adriatic c. 6000 BC but Cardial proper in the western
Mediterranean is 5600–5000 BC. Minor, and the row bundles two traditions, so the early start is
partly defensible.

### europe.prehistory.lascaux
**Field:** `dated_by`
**Currently:** `radiocarbon-uncalibrated`
**Should be:** `radiocarbon-calibrated`
**Confidence:** medium
**Why:** −19550/−19050 is the calibrated equivalent of the ~17,000 bp charcoal dates. If the label
were true the values would be about 2,500 years younger.

### west-asia.prehistory.jericho-neolithic
**Field:** `dated_by`
**Currently:** `radiocarbon-uncalibrated`
**Should be:** `radiocarbon-calibrated`
**Confidence:** medium
**Why:** −8300/−7300 is the calibrated PPNA/early-PPNB range for Tell es-Sultan; Kenyon's
uncalibrated figures are roughly 7000–6000 bc.

### west-asia.prehistory.ppna / west-asia.prehistory.ppnb
**Field:** boundary
**Currently:** PPNA −9800 to −8800, PPNB −8600 to −6900
**Should be:** abutting at c. −8700
**Confidence:** low
**Why:** A 200-year gap between two phases defined as consecutive. Real transitional variability
exists (the "PPNA/B" or EPPNB problem), so this is a quibble unless the file elsewhere requires
consecutive phases to abut.

### global.paleolithic.acheulean
**Field:** `dated_by`
**Currently:** `magnetostratigraphy`
**Should be:** `argon-argon` (with magnetostratigraphic support)
**Confidence:** low
**Why:** The 1.76 Ma Kokiselei start is an Ar-Ar tuff date; palaeomagnetism constrains it but does
not produce it. Compare `global.paleolithic.oldowan` and `lomekwian`, both `argon-argon`.

---

## The twenty worst

Ordered by how badly each misleads a reader.

1. **P1** — 51 nengō carrying a fabricated ±25-year uncertainty and `dated_by: unknown` on dates
   recorded to the day. This is the Berlin Wall failure mode, fifty-one times over, in the region the
   dataset covers most densely.
2. **P2** — the same fabricated window on Wang Mang's Xin (`bounds: [-16, 34]`, crossing the BC/AD
   line for a reign dated to the day), the four Phoenician sub-periods, and Capetian France.
3. **east-asia.japan.kenmu.kenmu-era** — end 1336 leaves a two-year hole in the Northern Court
   sequence before Ryakuō 1338. The only true gap in the Japanese chain.
4. **global.paleolithic.later-stone-age** — end date and summary contradict each other in adjacent
   fields; nine tenths of the tradition is cut off.
5. **global.neolithic.agricultural-revolution.mesoamerica** — "squash predates maize by over four
   thousand years" is wrong by a factor of four and is the row's only substantive claim.
6. **americas.mesoamerica.maya.classic.tikal** — start 600 CE erases Tikal's entire Early Classic,
   its founding dynasty, and the Teotihuacan entrada.
7. **east-asia.china.neolithic.cishan** — "cereal farming began at the Pleistocene boundary" is off
   by two millennia and mislabels the epoch.
8. **west-asia.arabia.pre-islamic.saba.marib-dam** — end 300 CE excludes the sixth-century collapse
   the summary's "parable" refers to.
9. **east-asia.japan.muromachi.shokei** — a period filed 1332–1333 beneath a parent that begins in
   1336.
10. **americas.andes.inca.machu-picchu** — `bounds: [1450, 1450]`, a zero-width uncertainty.
11. **africa.prehistory.nabta-playa.terminal-neolithic** — sub-phase ends 800 years after its parent.
12. **east-asia.china.zhou.eastern.warring-states** — child outlives parent by 35 years because the
    two are not in a containment relation at all.
13. **southeast-asia.prehistory.yangtze-rice** — the Yangtze filed under Southeast Asia, duplicating
    an existing row with a different span.
14. **central-asia.prehistory.bmac.gonur-depe** — the type site brackets the complex it defines on
    both ends.
15. **east-asia.japan.azuchi-momoyama.keicho** — Sekigahara, the founding of the bakufu, and the
    Siege of Osaka all filed under Azuchi–Momoyama.
16. **africa.prehistory.pinnacle-point** — start 90 ka excludes the 164 ka evidence the summary
    depends on.
17. **south-asia.indus.deurbanisation** + **south-asia.indus.late** — the cities are simultaneously
    at maximum extent and being abandoned 2200–1900, and then nothing happens 1900–1800.
18. **americas.prehistory.paleoindian** + **americas.prehistory.archaic** — a 1,000-year hole
    between them and an Archaic running to 500 CE.
19. **P3** — fourteen rows labelled `radiocarbon-uncalibrated` while carrying calibrated values,
    including Jericho, 'Ain Ghazal, Lascaux and Hongshan.
20. **P4** — 218 of 248 Japanese era rows are two years and a name, with no ruler, no summary and no
    alias.

---

## Proposed tests

Each test below is stated as an implementable rule with an explicit threshold, marked `safe` (no
legitimate exceptions; may fail the build) or `advisory` (real exceptions exist; warn only), and
followed by the entities in this dataset that currently violate it. Every test corresponds to an
error class I actually found more than once.

### T1 — Nengō and reign eras carry no uncertainty bounds `safe`

**Rule:** if an entity's `under` chain contains a Japanese period node (Asuka, Nara, Heian,
Kamakura, Kenmu, Muromachi, Azuchi–Momoyama, Edo, or modern Japan) and its span is under 100 years,
then `bounds` must be `[null, null]`. Generalised form: for any entity with `start >= 600` whose
region is Japan, China, Korea or Vietnam and whose kind is an era or reign period, `bounds` must be
`[null, null]`.
**Why safe:** nengō dates come from dated proclamations in the court chronicles. There is no nengō
whose start year is uncertain. A ±25-year window on a three-month era is never defensible.
**Violations (51):** all ids listed under P1.

### T2 — Nengō and reign eras are dated by calendar, never `unknown` or `typological` `safe`

**Rule:** for the same entity set as T1, `dated_by` must equal `calendar`. Reject `unknown`,
`typological`, `received`, and any radiometric value.
**Why safe:** a documentary era name is a calendar date by construction. `typological` would mean
the era name was inferred from pottery, which is incoherent.
**Violations (51):** the same 51 ids as T1 (they overlap exactly — every row with bogus bounds also
has `dated_by: unknown`), i.e. all of `east-asia.japan.asuka.*`, all of `east-asia.japan.nara.*`,
and the 33 pre-1028 `east-asia.japan.heian.*` rows.

### T3 — Post-600 CE dated political periods in East Asia must be `calendar` `advisory`

**Rule:** any entity with `start >= 600` under Japan, China, Korea or Vietnam must have
`dated_by: calendar`.
**Why advisory rather than safe:** archaeological periods can legitimately postdate 600 CE and be
radiocarbon-dated — for example a Japanese kiln phase, or `americas` analogues like
`americas.north.ancestral-puebloan.chaco` (850–1250, `dendrochronology`), which is the right method
for its evidence. The exception must be allowed for `kind: period` rows that are archaeological
cultures rather than named eras.
**Violations:** the 51 rows in T2. No legitimate exception exists among them, but the rule as
written would also catch future archaeological rows, hence advisory.

### T4 — Consecutive eras under the same parent must abut exactly `advisory`

**Rule:** sort all era rows sharing a parent by `start`. For each consecutive pair, require
`next.start == prev.end`. Report both gaps (`next.start > prev.end`) and overlaps
(`next.start < prev.end`).
**Handling the Nanboku-chō schism:** from 1331 to 1392 two courts proclaimed rival eras
simultaneously, so overlap is expected and correct. Partition the comparison by court before
sorting: an era row must declare its court (Northern or Southern) and abutment is checked *within
each court's chain only*. Rows carrying "Northern Court nengō" in their summary form one chain,
"Southern Court nengō" the other, and Kenmu belongs to both. Under that partition the Southern chain
(Kenmu → Engen → Kōkoku → Shōhei → Kentoku → Bunchū → Tenju → Kōwa → Genchū → Ōei) abuts perfectly
and the Northern chain abuts perfectly except for one gap.
**Why advisory rather than safe:** besides the schism, there are genuine periods with no era name at
all — 654–686 and 686–701 in the Asuka period — so gaps are sometimes the truth. Those two should be
allowlisted explicitly rather than silently tolerated.
**Violations after partitioning and allowlisting the Asuka interregna:**
- `east-asia.japan.kenmu.kenmu-era` (ends 1336) → `east-asia.japan.muromachi.ryakuo` (starts 1338):
  a 2-year gap in the Northern chain.
- `east-asia.japan.heian.juei` (ends 1185) vs `east-asia.japan.heian.genryaku` (1184–1185): a
  1-year overlap outside the schism window, requiring either a correction to 1184 or an explicit
  Taira-usage note.
- `east-asia.japan.kamakura.gentoku` (1329–1332) vs `east-asia.japan.kamakura.genko-kamakura2`
  (1331–1334): a legitimate rival-court overlap that the partition rule cannot see, because neither
  row declares a court. This is itself the finding — the test forces the two rows to be labelled.
- `south-asia.indus.mature` (ends −1900) → `south-asia.indus.late` (starts −1800): 100-year gap.
- `west-asia.prehistory.ppna` (ends −8800) → `west-asia.prehistory.ppnb` (starts −8600): 200-year
  gap.
- `americas.prehistory.paleoindian` (ends −9501) → `americas.prehistory.archaic` (starts −8500):
  ~1,000-year gap.
- `global.paleolithic.still-bay` (ends −65850) → `global.paleolithic.howiesons-poort` (starts
  −62850): a 3,000-year gap that is real and should be allowlisted, which is why this test is
  advisory.

### T5 — A period's span must fall within its parent's span `safe`

**Rule:** where the parent entity exists in the dataset, require
`parent.start <= child.start` and `child.end <= parent.end`, treating a null end as open. Report
both directions separately.
**Why safe:** containment is what `under` asserts. A sub-phase outside its parent means one of the
two dates is wrong, always.
**Violations (4):**
- `africa.prehistory.nabta-playa.terminal-neolithic` ends −3451 > parent
  `africa.prehistory.nabta-playa` ends −4251.
- `central-asia.prehistory.bmac.gonur-depe` starts −2300 < parent `central-asia.prehistory.bmac`
  starts −2200, **and** ends −1500 > parent ends −1700.
- `east-asia.china.zhou.eastern.warring-states` ends −221 > parent
  `east-asia.china.zhou.eastern` ends −256.

### T6 — A period's span must fall within the polity or era named in its `under` string `advisory`

**Rule:** the same containment check as T5, but resolved against the *named* ancestor even when that
ancestor is not a row in this file — Japanese period boundaries are fixed constants (Asuka 538–710,
Nara 710–794, Heian 794–1185, Kamakura 1185–1333, Kenmu 1333–1336, Muromachi 1336–1573,
Azuchi–Momoyama 1568–1600, Edo 1603–1868, modern 1868–). Require the child's span to intersect the
parent's and to be contained in it; report containment failures with the number of years outside.
**Why advisory rather than safe:** era names legitimately straddle period boundaries — that is how
periodisation works, since the political transition rarely coincides with an era proclamation.
Enryaku spanning the move to Heian-kyō is a legitimate exception, as is Genna spanning nothing but
sitting right after the Edo boundary. The test should warn and require an explicit
"spans-parent-boundary" acknowledgement rather than block.
**Violations:**
- `east-asia.japan.muromachi.shokei` (1332–1333) is *entirely outside* Muromachi (from 1336) — this
  one is a hard error, not a straddle, and should fail even under an advisory rule. A separate strict
  clause is worth having: **if a child's span does not intersect its named parent's span at all,
  fail.** `shokei` is the only violation of that strict clause.
- `east-asia.japan.nara.enryaku` (782–806): 12 years past the end of Nara.
- `east-asia.japan.azuchi-momoyama.keicho` (1596–1615): 15 years past the end of Azuchi–Momoyama.
- `east-asia.japan.kamakura.genko-kamakura2` (1331–1334): 1 year past the fall of Kamakura.

### T7 — `bounds` must be a proper interval containing the point estimate `safe`

**Rule:** if `bounds` is not `[null, null]`, then both elements must be non-null,
`bounds[0] < bounds[1]`, and `bounds[0] <= start <= bounds[1]`. Reject zero-width and one-sided
intervals.
**Why safe:** a zero-width interval asserts infinite precision, which no method delivers, and a
one-sided interval is not a statement about anything. Neither can be intended.
**Violations (2):**
- `americas.andes.inca.machu-picchu`, `bounds: [1450, 1450]`.
- `africa.prehistory.taforalt`, `bounds: [-19300, null]`.

### T8 — `radiocarbon-uncalibrated` values must be consistent with uncalibrated magnitudes `advisory`

**Rule:** for any entity with `dated_by: radiocarbon-uncalibrated` and a start older than 6000 BC,
compare its start against calibrated siblings covering the same phenomenon; flag when the value is
within 2% of the known calibrated range rather than the uncalibrated one. A cheaper implementable
proxy: flag any `radiocarbon-uncalibrated` row whose start is more than 5% older than the
uncalibrated equivalent of its own stated cultural phase, or simply flag every
`radiocarbon-uncalibrated` row for manual confirmation, since the label is rare (14 of 522) and
almost always a mistake in a dataset that otherwise reports calibrated dates.
**Why advisory:** legacy literature genuinely reports uncalibrated dates and some rows may
faithfully reproduce them; the label is not wrong in principle.
**Violations (all 14 warrant review; these are the ones I judge actually mislabelled):**
`west-asia.prehistory.jericho-neolithic` (−8300 is calibrated PPNA),
`west-asia.prehistory.ain-ghazal` (−8400), `europe.prehistory.lascaux` (−19550),
`east-asia.china.neolithic.hongshan` (−4551, and every sibling is calibrated),
`africa.prehistory.nabta-playa.late-neolithic`, `.middle-neolithic`, `.terminal-neolithic`.
Remaining flagged for review: `africa.prehistory.enkapune-ya-muto`, `africa.prehistory.ishango`,
`africa.prehistory.wadi-kubbaniya`, `americas.prehistory.cactus-hill`,
`americas.prehistory.las-vegas-culture`, `southeast-asia.prehistory.hoabinhian`,
`southeast-asia.prehistory.yangtze-rice`.

### T9 — Named era rows must have a ruler, or a summary, or an alias `advisory`

**Rule:** any entity whose `under` chain reaches a Japanese, Chinese, Korean or Vietnamese period
node and whose span is under 100 years must have at least one of: a linked ruler, a non-null
`summary`, or a non-null `aliases`.
**Why advisory:** coverage gaps are tracked separately by policy, and a bare row is not false, only
useless. But a row consisting of a name and two years is the case the brief's exception describes —
its existence only makes sense alongside the reign it dates.
**Violations:** 218 of 248 Japanese era rows. The 30 that pass are the five modern eras, the
Nanboku-chō rows carrying court labels, and the Muromachi rows with schism summaries. Report as a
single aggregate count, not 218 findings.

### T10 — A summary's internal arithmetic must agree with the row's own dates `advisory`

**Rule:** where a summary states a duration, a gap, or a relative claim in years ("for four thousand
years", "nineteen centuries before X", "predates Y by N years", "continues into the historical
period"), extract the figure and compare it against `end - start` for the row, or against the
referenced sibling's dates, with a tolerance of 20%. Flag disagreements beyond tolerance.
**Why advisory:** natural-language extraction is imprecise and rhetorical rounding is normal.
**Violations found by hand:**
- `global.neolithic.agricultural-revolution.mesoamerica`: "over four thousand years" against an
  actual squash-to-maize gap of about one thousand.
- `global.paleolithic.later-stone-age`: "continues into the historical period" against
  `end: -10050`.
- `east-asia.china.neolithic.cishan`: "the Pleistocene boundary" against a row spanning
  −6050 to −5050, a 3,650-year discrepancy with the epoch named.
- `west-asia.arabia.pre-islamic.saba.marib-dam`: a summary whose "parable" refers to an event in
  570 CE against `end: 300`.
- `africa.prehistory.pinnacle-point`: a summary resting on 164 ka evidence against
  `start: -90050`.
- `east-asia.china.neolithic.shijiahe`: "contemporary with Longshan further north" against a start
  300 years before the file's own Longshan row.
