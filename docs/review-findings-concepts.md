# Correctness review: concepts.json (169 entities)

Kinds: threshold 48, event 42, language 28, tradition 18, people 13, taxon 12, network 8.
Reviewed from knowledge, no web verification. Citations deliberately not discussed.

---

## Patterns (stated once, not repeated per entry)

### P1. Thresholds carry zero uncertainty where they need the most
**Field:** `bounds`
**Currently:** 24 of the 26 `global.prehistory.firsts.*` thresholds have `bounds[1] = null` and
`bounds[0]` either equal to `start` or a token 1,000 years below it. So `cooking` is
`-778000` with `bounds [-779000, null]` — plus-or-minus five hundred years on an 800,000-year-old
event — and `butchery`, `cut-marks`, `cereal-farming`, `pottery`, `dog`, `irrigation`, `wheel`,
`writing`, `chicken`, `fermented-drink`, `spun-fibre`, `woven-cloth`, `horse-domestication`,
`artificial-mummification` and `figurative-art` have `bounds[0] == start` exactly, i.e. no
uncertainty at all.
**Should be:** every earliest-known-occurrence date needs a real two-sided interval, and for
Pleistocene thresholds the interval should be a visible fraction of the age (tens of thousands of
years at 300–800 ka, not hundreds).
**Confidence:** high
**Why:** This is the exact failure mode the brief warns about, inverted: the Berlin Wall got a
century it did not need, and these get a decade they cannot possibly have. A reader sees
`-778000 ± 500` and concludes the date of the first cooked meal is known to within a human lifetime.

### P2. `date_standing: consensus` used on thresholds that rest on one contested site
**Field:** `date_standing`
**Currently:** `consensus` on `cooking`, `figurative-art`, `pigment-use`, `spun-fibre`,
`stone-knapping`, `wood-structure`, `woven-cloth`, `pottery`.
**Should be:** `majority` or `minority` for most of these; see individual entries below.
**Confidence:** high
**Why:** Each of these is a single-site, single-team claim published in the last fifteen years and
argued about since. `consensus` is the strongest label the schema has and it is being spent on the
least settled dates in the file.

### P3. `dated_by: first-attestation` used where nothing is attested
**Field:** `dated_by`
**Currently:** all 13 `people` entries and all 18 `tradition` entries are `first-attestation`,
including `oceania.peoples-aboriginal-australians` (65,000 BCE), `africa.peoples-bantu-peoples`
(3000 BCE), `europe.peoples-sami` (1000 BCE), `global.traditions.hinduism` (1500 BCE) and
`global.traditions.zoroastrianism` (1200 BCE).
**Should be:** `luminescence`/`radiocarbon-calibrated` for the archaeological ones,
`glottochronology` for the linguistic ones, `received` for the traditional founding dates
(Buddha's death, Zarathustra, the Vedas). None of these dates comes from a first attestation:
Aboriginal Australians are dated by OSL at Madjedbebe, the Sami are first *attested* by Tacitus in
98 CE, and Zoroastrianism is first attested under the Achaemenids.
**Confidence:** high
**Why:** `first-attestation` tells a reader a text or inscription exists at that date. For a 65,000
BCE date that is a straightforwardly false statement about the evidence.

### P4. Networks and traditions carry manufactured symmetric bounds on documented dates
**Field:** `bounds`
**Currently:** `atlantic-slave-trade` 1501 with `[1496, 1506]`; `manila-galleon` 1565 with
`[1560, 1570]`; `hanseatic-league` 1150 with `[1120, 1180]`; `great-schism` 1054 with `[1049, 1059]`;
`sikhism` 1500 with `[1480, 1520]`; `islam` 610 with `[605, 615]`; `sunni-shia-split` 632 with
`[627, 637]`; `christianity` 30 with `[20, 40]`.
**Should be:** `[null, null]` where the year is a documented convention (1501, 1565, 1054, 632), and
a genuinely asymmetric range where the start is a scholarly choice rather than a measurement.
**Confidence:** medium-high
**Why:** This looks like the same spurious-plus-or-minus generator that produced the Berlin Wall
bug, scaled down from ±100 to ±5 or ±20. 1054 and 632 are known to the day; 1501 is the first year
in a documented voyage database. A range implies the year is estimated when it is not.

### P5. Taxon dates carry a −050 artefact and false precision
**Field:** `start` / `end`
**Currently:** `-193050`, `-855050`, `-1888050`, `-2398050`, `-398050`, `-333050`, `-144050`,
`-132050`, `-98050`, `-1898050`. Meanwhile `homo-erectus.end` is `-108000`, `homo-sapiens.start` is
`-310000` and `homo-heidelbergensis.start` is `-700000` — round.
**Should be:** consistent rounding. The `-050` is a BP→BCE conversion residue (1950 offset) and
presents Middle Pleistocene ages as accurate to the decade.
**Confidence:** high
**Why:** `-2398050` for the first appearance of *Homo habilis* claims ten-year precision on a
2.4-million-year-old date. A reader cannot tell it is an artefact.

---

## Thresholds

### global.prehistory.firsts.cut-marks
**Field:** `summary`
**Currently:** "roughly 800,000 years before the oldest known stone tools"
**Should be:** roughly 90,000 years before — or the sentence should name the Oldowan explicitly.
**Confidence:** high
**Why:** This file's own `stone-knapping` entry puts the oldest stone tools at 3,300,000 BCE and
Dikika at 3,390,000. The 800,000-year gap only works against the 2.6 Ma Oldowan, so the two entries
contradict each other in the same section.

### global.prehistory.firsts.stone-knapping
**Field:** `date_standing`
**Currently:** `consensus`, with the Lomekwian at 3.3 Ma treated as the point "where human
prehistory begins"
**Should be:** `minority`, or `majority` at most
**Confidence:** high
**Why:** Lomekwi 3 is actively disputed — the stratigraphic context and the anthropic origin of the
flakes have both been challenged, and the securely accepted earliest knapping remains Ledi-Geraru /
Gona at 2.6–2.9 Ma. Making the contested date both `consensus` and a structural anchor for the whole
app compounds the error.

### global.prehistory.firsts.cooking
**Field:** `date_standing` and `bounds`
**Currently:** `-778000`, `bounds [-779000, -778000]`, `consensus`
**Should be:** `minority` or `majority`, with bounds of at least ±20,000
**Confidence:** high
**Why:** The Gesher Benot Ya'aqov fish-tooth evidence is a 2022 single-site inference, and the
earliest-cooking question is one of the loudest open arguments in palaeoanthropology (Wrangham puts
it near 1.8 Ma, sceptics well after 400 ka). `consensus` with a 1,000-year window is the opposite of
the state of the field.

### global.prehistory.firsts.pigment-use
**Field:** `date_standing`
**Currently:** `-298000`, `consensus`
**Should be:** `majority`, with wider bounds
**Confidence:** medium-high
**Why:** ~300 ka (Olorgesailie) is the earliest *widely accepted* pigment use, but claims at
Wonderwerk and Kathu Pan reach 400–500 ka and are taken seriously. The bounds of ±1,000 years on a
300,000-year argon-argon date are also not credible.

### global.prehistory.firsts.figurative-art
**Field:** `date_standing`
**Currently:** `-49300`, `consensus`
**Should be:** `majority` at most
**Confidence:** medium-high
**Why:** The Sulawesi cave-art dates rest on uranium-series ages of overlying speleothem, which
gives a minimum age and has been methodologically criticised; the 2024 revision that pushed the
figure past 50 ka is a year or two old. The date has moved twice in a decade and will move again.

### global.prehistory.firsts.wood-structure
**Field:** `date_standing`
**Currently:** `-474000`, `consensus`
**Should be:** `majority` or `minority`
**Confidence:** medium
**Why:** Kalambo Falls rests on one 2023 paper with new luminescence ages; "oldest known wooden
structure" is defensible, "consensus" for the date is not yet.

### global.prehistory.firsts.deliberate-burial
**Field:** `date_standing`
**Currently:** `-428000`, `majority`
**Should be:** `minority`
**Confidence:** medium-high
**Why:** Sima de los Huesos at ~430 ka is read as deliberate deposition by its excavators and as
natural or fluvial accumulation by others; the mainstream earliest *burials* are Middle Palaeolithic
(Skhul, Qafzeh, Tabun) at 120–90 ka. Also the U-series age is 430 ± 60 ka, so bounds of 19,000 years
are too tight.

### global.prehistory.firsts.spun-fibre
**Field:** `start` / `date_standing`
**Currently:** `-30100` (Dzudzuana flax), `consensus`
**Should be:** older, or the summary should say "oldest dyed" — the three-ply cord from Abri du
Maras is ~41–52 ka
**Confidence:** medium
**Why:** Twisted plant fibre from a Neanderthal context now predates Dzudzuana by 10–20 millennia,
so this is an outdated first, presented as settled.

### global.prehistory.firsts.irrigation
**Field:** `start`
**Currently:** `-6200`, Choga Mami
**Should be:** c. −5500, or the site should change
**Confidence:** medium-high
**Why:** Choga Mami is a Samarran site; its occupation and its canal system are placed in the
mid-sixth millennium, not at 6200 BCE. The date predates the culture the site belongs to by several
centuries.

### global.prehistory.firsts.artificial-mummification
**Field:** `start`
**Currently:** `-6051`, bounds `[-6051, null]`
**Should be:** c. −5000
**Confidence:** medium-high
**Why:** Chinchorro *artificial* mummification begins around 7,000 BP (~5050 BCE); the earlier
Chinchorro dates are for natural mummies. The entry's own summary says "two thousand years before
anyone in Egypt", which is right for −5000 and wrong for −6051 (that would be three and a half
thousand).

### global.prehistory.firsts.dog
**Field:** `start`
**Currently:** `-13900`
**Should be:** c. −12,200 BCE, or state the figure as 14,200 BP
**Confidence:** medium
**Why:** The oldest undisputed domestic dog is the Bonn-Oberkassel burial at ~14,200 cal BP, which
is ~12,250 BCE. `-13900` looks like a BP figure used as a BCE figure, or a BP figure converted
inconsistently. Also "the only one domesticated by hunter-gatherers" is too absolute — reindeer are
a standing counterexample.

### global.milestones.iron-smelting
**Field:** `summary`
**Currently:** "Hittite-era bloomery iron" at −1900
**Should be:** pre-Hittite Anatolian, or the date should move to c. −1500
**Confidence:** high
**Why:** The Hittite Old Kingdom begins c. 1650 BCE. A 1900 BCE date sits in the Old Assyrian
colony period, two and a half centuries before any Hittite state — the entry's date and its
explanation cannot both be right.

### africa.prehistory.african-cattle
**Field:** `date_standing` / `dated_by` / `summary`
**Currently:** `-5750`, `dated_by: unknown`, `date_standing: minority`, summary calls it "the
oldest **uncontroversial** domestic cattle in Africa"
**Should be:** `radiocarbon-calibrated`, and either `majority`/`consensus` to match
"uncontroversial", or a summary that admits the date is a minority reading
**Confidence:** medium-high
**Why:** The entry describes itself as uncontroversial and is simultaneously labelled a minority
date with an unknown dating method. One of the three fields is wrong. (The genuinely contested claim
is independent Saharan domestication at 8000–7000 BCE, which this entry correctly declines to make.)

### africa.prehistory.african-cereals
**Field:** `start` / `date_standing`
**Currently:** `-4000`, `consensus`
**Should be:** c. −2500 for pearl millet; `majority` at best
**Confidence:** medium-high
**Why:** Domesticated pearl millet in the Sahel is securely dated to the mid-third millennium
(Ounjougou, Tichitt); sorghum domestication in eastern Sudan is later still and is itself argued
over. 4000 BCE is too early for either, and `consensus` for a date on African cereal domestication
overstates a genuinely thin record.

### global.prehistory.firsts.writing
**Field:** `start`
**Currently:** `-3400`, bounds `[-3400, null]`
**Should be:** c. −3350 to −3200, with two-sided bounds
**Confidence:** low-medium
**Why:** Uruk IV proto-cuneiform and the Abydos tags both sit in the second half of the
thirty-fourth to thirty-second centuries; −3400 is at or slightly before the earliest defensible
edge, and again has no upper bound.

---

## Events

### west-asia.iran.arab-conquest
**Field:** `bounds`
**Currently:** `start 633`, `end 651`, `bounds [608, 658]`
**Should be:** `[null, null]`
**Confidence:** high
**Why:** The lower bound is twenty-five years before the start, i.e. before Muhammad's mission
began — a ±25 leftover applied to a date fixed by narrative sources. It implies the conquest of Iran
might have started in the reign of Khosrow II. `dated_by: unknown` is also wrong for a
well-documented seventh-century campaign.

### west-asia.anatolia.hittites.sack-of-babylon
**Field:** `bounds` / `dated_by`
**Currently:** `-1595`, `bounds [null, null]`, `dated_by: calendar`, `date_standing: majority`
**Should be:** wide bounds (roughly −1660 to −1500), `dated_by: received` or `typological`
**Confidence:** high
**Why:** The entry's own summary says the date is "the hinge the whole Bronze Age chronology turns
on" — and then gives it no uncertainty at all. 1595 is the Middle Chronology figure; the High, Low
and Ultra-Low chronologies put it 64, 96 or 120 years apart. This is the one date in the file that
most needs bounds and has none.

### southeast-asia.prehistory.austronesian-expansion.isea-pottery
**Field:** `start` / `end`
**Currently:** `-3481` to `-2341`
**Should be:** roughly −2200 to −1500
**Confidence:** medium-high
**Why:** Neolithic pottery in the northern Philippines (Nagsabaran) and northern Borneo is dated to
around 4,000 BP; the Austronesian dispersal out of Taiwan itself only begins c. 3000 BCE. A 3481 BCE
date for pottery already in Borneo puts the arrival before the departure, and predates this file's
own `proto-austronesian` start of −3500 by almost nothing.

### europe.prehistory.steppe-influx
**Field:** `end`
**Currently:** `-3000` to `-2900`
**Should be:** end c. −2200, or later
**Confidence:** medium
**Why:** A hundred-year window cannot hold the process described. Corded Ware runs 2900–2350 BCE and
the Bell Beaker turnover in Britain is c. 2450 BCE, so the influx this entry names continues for
seven or eight centuries past its stated end.

### east-asia.japan.yayoi.yayoi-redating
**Field:** `start` / `end` / `dated_by`
**Currently:** an event named "The Yayoi Redating Controversy", dated −1000 to −400 by
radiocarbon
**Should be:** unclear — the dates describe the disputed span, not the controversy, which happened
in 2003
**Confidence:** medium
**Why:** As written, an event that took place in 2003 is dated to the first millennium BCE. If the
range is meant to bracket the competing proposals for the *start* of Yayoi, that needs to be in the
summary; as it stands −400 reads as the end of the Yayoi period, which is c. 250 CE.

### global.bronze-age.collapse
**Field:** `dated_by`
**Currently:** `unknown`
**Should be:** `radiocarbon-calibrated` or `typological`
**Confidence:** medium
**Why:** The collapse horizon is dated by destruction layers, ceramic phasing and radiocarbon at
Ugarit, Hattusa, Mycenae and elsewhere. `unknown` understates the evidence considerably.

### west-asia.arabia.pre-islamic.incense-trade
**Field:** `dated_by`
**Currently:** `calendar`, `bounds [null, null]`, for a span −700 to 200
**Should be:** `typological` or `first-attestation`, with bounds
**Confidence:** medium
**Why:** No calendar fixes the beginning or end of a caravan trade. This is the brief's item 4 —
`calendar` on something known from archaeology and classical geographers. (Also filed as `network` in
kind terms elsewhere in the file; this one is a `network` correctly, but its dating fields were
treated like an event's.)

### west-asia.anatolia.hittites.kadesh
**Field:** `bounds`
**Currently:** `-1274`, `bounds [null, null]`
**Should be:** roughly ±10–25 years
**Confidence:** low-medium
**Why:** 1274 is secure to about a decade within Egyptian chronology, not exact. Minor next to the
Sack of Babylon, but the same class of error.

---

## Languages

The good news first: no `language` entry uses `dated_by: calendar`, and every proto-language is
`glottochronology` + `historicity: reconstructed`. That risk did not materialise. The problems are
elsewhere.

### global.languages.avestan
**Field:** `dated_by`
**Currently:** `first-attestation`, start −1200
**Should be:** `received` or `typological`
**Confidence:** high
**Why:** The entry's own summary says Avestan was "preserved orally for centuries before it was
written" — the manuscripts are first millennium CE. A 1200 BCE first attestation is contradicted by
the same row.

### global.languages.sanskrit
**Field:** `dated_by`
**Currently:** `first-attestation`, start −1500
**Should be:** `received` or `typological`
**Confidence:** medium-high
**Why:** Same problem: 1500 BCE is the estimated composition date of the Rigveda, transmitted
orally; the earliest written Sanskrit is many centuries later. Nothing is attested at −1500.

### global.languages.quechua
**Field:** `dated_by`
**Currently:** `first-attestation`, start 1000
**Should be:** `glottochronology`
**Confidence:** medium-high
**Why:** Quechua is first written in the sixteenth century, under Spanish colonial authorship. A
1000 CE date can only be a linguistic reconstruction of Proto-Quechua's diversification.

### global.languages.nahuatl
**Field:** `dated_by`
**Currently:** `first-attestation`, start 600
**Should be:** `glottochronology`
**Confidence:** medium
**Why:** Nahuatl's arrival in central Mexico is inferred from linguistic and archaeological
argument; written Nahuatl begins in the sixteenth century, with at best glyphic name-signs in the
fifteenth.

### global.languages.classical-maya
**Field:** `summary`
**Currently:** "The only pre-Columbian American writing system fully deciphered"
**Should be:** "the only one substantially deciphered", or similar
**Confidence:** medium-high
**Why:** Maya script is not fully deciphered — a meaningful minority of signs and a good deal of
vocabulary remain unread, and the entry as written promises more than epigraphy delivers. The start
date of 250 CE is also late: the San Bartolo texts are third or second century BCE and the Long
Count reaches back to 36 BCE.

### global.languages.sumerian
**Field:** `summary`
**Currently:** "The first written language"
**Should be:** "among the first", or a formulation that acknowledges Egyptian
**Confidence:** medium
**Why:** This file's own `writing` threshold says proto-cuneiform and Egyptian hieroglyphs are "two
independent inventions whose dates overlap". Two rows in the same dataset cannot both be right.

### global.languages.proto-uralic
**Field:** `start`
**Currently:** `-4000`, bounds `[-5000, -3000]`
**Should be:** c. −2000, or bounds widened to include it
**Confidence:** medium
**Why:** Current Uralic scholarship has moved the Proto-Uralic node substantially later, to roughly
2000 BCE; 4000 BCE is an older glottochronological estimate and the stated bounds exclude the newer
position entirely.

### global.languages.latin
**Field:** `start` / `extant`
**Currently:** `-700`, `extant: true`
**Should be:** c. −600 for the first attestation; `extant` is arguable
**Confidence:** low
**Why:** The earliest Latin inscriptions (Praeneste fibula, Duenos inscription, Forum cippus) are
sixth century; −700 is at the outer edge. `extant: true` for a language with no native speakers is a
defensible convention but should be applied consistently with how Sanskrit and Aramaic are treated.

### global.languages.aramaic
**Field:** `start`
**Currently:** `-1100`
**Should be:** c. −900
**Confidence:** low-medium
**Why:** The earliest Aramaic inscriptions are tenth–ninth century (Tell Fekheriye and the Aramaean
royal inscriptions); 1100 BCE precedes any attested Aramaic text.

---

## Taxa

### global.prehistory.hominins.homo-luzonensis
**Field:** `start`
**Currently:** `-132050`, `end: null`
**Should be:** roughly −65,000 to −48,000
**Confidence:** high
**Why:** The Callao Cave *H. luzonensis* material is dated to 67,000 and 50,000 years ago by
uranium-series. A 134,000-year first appearance is roughly twice the published age, and the null end
implies the taxon never ended.

### global.prehistory.hominins.homo-heidelbergensis
**Field:** `bounds`
**Currently:** `start -700000`, `bounds [-1300000, -600000]`
**Should be:** something like `[-800000, -600000]`
**Confidence:** medium-high
**Why:** A lower bound of 1.3 Ma is 600,000 years below the start and reaches into *Homo erectus*
territory — no one places heidelbergensis in the Early Pleistocene. The asymmetry looks like a bad
default rather than a considered range.

### global.prehistory.hominins.homo-erectus
**Field:** `start` / `date_standing`
**Currently:** `-1888050`, `consensus`
**Should be:** `majority`, and consider the Drimolen DNH 134 date of c. 2.04 Ma
**Confidence:** medium
**Why:** The 2020 Drimolen calvaria pushed the earliest *H. erectus* to roughly 2.04 Ma, so 1.89 Ma
is either outdated or a deliberate rejection of that claim — and either way is not `consensus`. The
end date of −108,000 (Ngandong) is up to date and correct.

### global.prehistory.hominins.denisovans
**Field:** `date_standing` / `dated_by`
**Currently:** `-193050` to `-50000`, `dated_by: unknown`, `date_standing: consensus`
**Should be:** `majority`; `dated_by` should be `uranium-series`/`radiocarbon-calibrated` per the
Denisova Cave sequence
**Confidence:** medium
**Why:** Denisovans have no formal species name, their fossil range is a handful of specimens, and
admixture signals in Papuan genomes are read by some as survival well past 50 ka. `consensus` on the
first and last appearance of a population defined mainly by DNA is too strong, and `unknown` dating
sits oddly beside a `consensus` label.

### global.prehistory.hominins.homo-longi
**Field:** `end`
**Currently:** `null`
**Should be:** a last-appearance date, or an explicit note that the taxon is known from one specimen
**Confidence:** low-medium
**Why:** A null end on an extinct taxon reads as "still around". The summary correctly reports the
2025 palaeoproteomic result tying the Harbin cranium to Denisovans — which arguably makes the whole
row a synonym of the Denisovan entry, and worth stating in the summary as such.

### global.prehistory.hominins.homo-habilis
**Field:** `start`
**Currently:** `-2398050`
**Should be:** c. 2.1 Ma, or wider bounds
**Confidence:** low
**Why:** The 2.4 Ma end of the habilis range rests on fragmentary Uraha and Chemeron material of
disputed attribution; 2.1–1.5 Ma is the commoner published range.

---

## Traditions

### global.traditions.great-schism
**Field:** `kind` (and `extant`, `bounds`)
**Currently:** `kind: tradition`, `extant: true`, `end: null`, `bounds [1049, 1059]`
**Should be:** `kind: event`, `start 1054`, `end 1054`, `bounds [null, null]`, `extant: null`
**Confidence:** high
**Why:** The Great Schism is not a religion, philosophy or school — it is a dated event, filed under
the intended meaning of `tradition` by mistake. It is also marked as currently extant with no end,
and given a ±5-year window on 16 July 1054, a date known to the day.

### global.traditions.sunni-shia-split
**Field:** `kind` (and `bounds`)
**Currently:** `kind: tradition`, 632–680, `bounds [627, 637]`
**Should be:** `kind: event`; bounds `[null, null]`
**Confidence:** medium-high
**Why:** Same category error — a succession dispute is an event, not a school. 632 is the year of
Muhammad's death and is not uncertain by five years in either direction.

### global.traditions.zoroastrianism
**Field:** `dated_by`
**Currently:** `first-attestation`, start −1200
**Should be:** `received`
**Confidence:** medium-high
**Why:** Nothing Zoroastrian is attested at 1200 BCE; the earliest attestation is Achaemenid, six
centuries later. The bounds of [−1600, −800] do commendably signal that Zarathustra's date is
contested — the method label just contradicts them.

### global.traditions.mahayana
**Field:** `bounds`
**Currently:** `start 100`, `bounds [-1, 200]`
**Should be:** `[-100, 200]` or `[1, 200]`
**Confidence:** low-medium
**Why:** A lower bound of −1 is an off-by-one artefact of BCE/CE arithmetic, not a scholarly
position on the earliest Mahayana sutras.

### global.traditions.buddhism
**Field:** `dated_by`
**Currently:** `first-attestation`, start −450
**Should be:** `received`
**Confidence:** medium
**Why:** −450 approximates the Buddha's parinirvana in the corrected long chronology; the first
attestation of Buddhism is the Ashokan edicts, c. 250 BCE. (Applies equally to `hinduism`,
`jainism`, `confucianism`, `daoism` and `judaism` — see pattern P3.)

---

## Peoples

### oceania.peoples-aboriginal-australians
**Field:** `dated_by`
**Currently:** `first-attestation` for −65000
**Should be:** `luminescence`
**Confidence:** high
**Why:** The 65,000-year figure is the OSL date for the lowest artefact-bearing horizon at
Madjedbebe, itself contested. Calling it a first attestation asserts a written record 65,000 years
old.

### europe.peoples-celts
**Field:** `end`
**Currently:** `100` (CE)
**Should be:** much later, or `extant: true`
**Confidence:** medium-high
**Why:** Celtic-speaking peoples do not stop at 100 CE — Insular Celtic communities are continuous
to the present, and even on the continent Gaulish is attested into the third century. As filed, the
Celts end before Roman Britain begins.

### americas.peoples-thule
**Field:** `start` / `dated_by`
**Currently:** `1000`, `first-attestation`
**Should be:** c. 1200–1300 CE; `radiocarbon-calibrated`
**Confidence:** medium
**Why:** The re-dating of the Thule eastward migration moved it from c. 1000 to c. 1200–1300 CE on
recalibrated radiocarbon, and it is one of the better-known corrections in Arctic archaeology. There
is also no attestation of any kind at 1000 CE.

### central-asia.scythians
**Field:** `summary` (and `id`, `under`, `dated_by`)
**Currently:** `summary: null`; `dated_by: unknown`; id `central-asia.scythians`; placed under
"Eurasian Steppe < Central Asia & the Steppe"
**Should be:** a summary; and the same id pattern and parent as its siblings
**Confidence:** medium
**Why:** Every other steppe people uses `central-asia.peoples-*` and sits directly under "Central
Asia & the Steppe". This one is the odd row out on id, parent and dating method, and is the only
entity in the file with no summary at all — a reader arriving at the Scythians gets a blank. The
Sarmatians entry describes them as "successors to the Scythians", so the pair should be filed
alike.

### europe.peoples-sami
**Field:** `dated_by` (and `aliases`)
**Currently:** `first-attestation` for −1000; no aliases
**Should be:** `glottochronology`; add "Saami", "Sámi", "Lapps"
**Confidence:** medium
**Why:** Tacitus's *Fenni* (98 CE) is the first attestation; −1000 is a linguistic estimate. "Lapps"
is the exonym many readers will still arrive with.

### africa.peoples-amazigh
**Field:** `aliases`
**Currently:** `null`
**Should be:** `["Berbers", "Imazighen", "Amazigh peoples"]`
**Confidence:** high
**Why:** "Berber" is overwhelmingly the name an English-language reader searches for. With no alias,
this entity is effectively unreachable.

### europe.peoples-slavs
**Field:** `start`
**Currently:** `400`
**Should be:** c. 500–550
**Confidence:** low
**Why:** The Slavs are first named by Procopius, Jordanes and Pseudo-Maurice in the sixth century;
400 CE is a reconstruction, not an attestation.

---

## Networks

### global.networks.trans-saharan-trade
**Field:** `end`
**Currently:** `1600`
**Should be:** nineteenth or twentieth century, or `extant: true`
**Confidence:** medium-high
**Why:** Trans-Saharan caravan trade continued vigorously long after 1600 — Ghadames, Kano and
Tripoli routes were active into the late nineteenth century, and the trans-Saharan slave trade
outlasted the Atlantic one. Ending it at 1600 conflates the route with the fall of Songhai.

### global.networks.hanseatic-league
**Field:** `start`
**Currently:** `1150`, `bounds [1120, 1180]`
**Should be:** 1241 or 1356, or a summary that explains the early date
**Confidence:** low-medium
**Why:** 1150 predates Lübeck's refounding (1143 is the founding, but the merchant confederation is
thirteenth-century and the *Hansetag* structure is 1356). Filed as an organised network, the start
is a century or two early; the ±30 bounds are also invented.

---

## The twenty worst

1. **global.prehistory.firsts.*** — pattern P1: 24 thresholds with no upper bound and, in a dozen
   cases, zero uncertainty. A reader is told the first cooked meal is dated to ±500 years at 780 ka.
2. **west-asia.anatolia.hittites.sack-of-babylon** — the file's own summary calls it the hinge of
   Bronze Age chronology, then gives it no bounds. The single most consequential missing interval.
3. **global.prehistory.hominins.homo-luzonensis** — first appearance stated at 134 ka against a
   published 67–50 ka. Off by a factor of two, with a null end implying it never died out.
4. **global.prehistory.firsts.cut-marks** — "800,000 years before the oldest stone tools"
   contradicts this file's own stone-knapping entry by 700,000 years.
5. **west-asia.iran.arab-conquest** — bounds `[608, 658]` on a start of 633; the lower bound
   precedes Islam.
6. **global.prehistory.firsts.stone-knapping** — the contested Lomekwian at 3.3 Ma labelled
   `consensus` and used as the app's anchor for the start of prehistory.
7. **global.prehistory.firsts.cooking** — `consensus` and ±500 years on the most-argued threshold in
   palaeoanthropology.
8. **global.traditions.great-schism** — an event filed as a tradition, marked extant, with a ±5-year
   window on a date known to the day.
9. **Peoples and traditions, all 31 rows** — pattern P3: `first-attestation` on dates where nothing
   is attested, up to and including 65,000 BCE.
10. **oceania.peoples-aboriginal-australians** — the worst single instance of the above: a
    luminescence date presented as a written attestation.
11. **global.milestones.iron-smelting** — "Hittite-era" iron dated 250 years before the Hittites.
12. **europe.peoples-celts** — the Celts ended in 100 CE, which will surprise Ireland and Wales.
13. **southeast-asia.prehistory.austronesian-expansion.isea-pottery** — pottery arriving in Borneo a
    millennium before the expansion that carried it.
14. **global.prehistory.firsts.irrigation** — Choga Mami's canals dated seven centuries before its
    culture.
15. **Taxon `-050` suffix** — pattern P5: ten-year precision on Middle Pleistocene ages.
16. **africa.prehistory.african-cattle** — describes itself as uncontroversial while labelled a
    minority date with an unknown method.
17. **global.languages.classical-maya** — "fully deciphered" is a claim the epigraphy will not
    carry; start date also 400+ years late.
18. **global.prehistory.firsts.deliberate-burial** — Sima de los Huesos as `majority` for deliberate
    burial, when the reading itself is disputed.
19. **global.networks.trans-saharan-trade** — ends the trade in 1600, three centuries early.
20. **central-asia.scythians** — the only entity in the file with no summary, plus a nonstandard id
    and parent that split it from the Sarmatians it is defined against.

---

## Proposed tests

Each rule below was derived from an error class that occurs more than once in `concepts.json`.
Violation lists are exhaustive for this file, computed against the data rather than recalled.

### T1. A threshold must carry two-sided uncertainty bounds
**Rule:** if `kind == "threshold"` and `start` is set, then `bounds[0]` and `bounds[1]` must both be
non-null.
**Standing:** `safe` for archaeological thresholds; `advisory` overall.
**Why advisory overall:** a legitimate exception exists at the modern end. `global.milestones.transistor`
(1947) and `global.milestones.packet-switching` (1969) are documented to the day and correctly carry
`[null, null]`; forcing bounds on them would recreate the Berlin Wall bug in a new place.
**Recommended split:** make it `safe` when `dated_by` is in
`{radiocarbon-calibrated, uranium-series, argon-argon, luminescence, esr, magnetostratigraphy,
layer-counting, typological, unknown}`, and skip it when `dated_by == "calendar"`.
**Violations under the safe form (34):** `africa.prehistory.african-cattle`,
`africa.prehistory.african-cereals`, `global.milestones.alphabet`, `global.milestones.gunpowder`,
`global.milestones.iron-smelting`, `global.milestones.magnetic-compass`,
`global.milestones.movable-type`, `global.milestones.papermaking`,
`global.milestones.woodblock-printing`, `global.milestones.zero-as-number`,
`west-asia.anatolia.lydia.coinage`, and all 23 `global.prehistory.firsts.*` entries
(`artificial-mummification`, `butchery`, `cereal-farming`, `chicken`, `controlled-fire`, `cooking`,
`cut-marks`, `deliberate-burial`, `dog`, `fermented-drink`, `figurative-art`, `horse-domestication`,
`irrigation`, `pigment-use`, `pottery`, `seafaring`, `shell-beads`, `spun-fibre`, `stone-knapping`,
`symbolic-engraving`, `wheel`, `wood-structure`, `woven-cloth`, `writing`).

### T2. No entity may claim zero uncertainty by setting a bound equal to its own start
**Rule:** `bounds[0] != start` and `bounds[1] != start`, unless both bounds are null.
**Standing:** `safe`.
**Why:** a bound identical to the point estimate is not an uncertainty statement, it is a placeholder
that renders as certainty. There is no case where an estimated date is known to be exactly its own
lower limit.
**Violations (17):** `africa.prehistory.african-cattle`, `africa.prehistory.african-cereals`,
`global.prehistory.firsts.artificial-mummification`, `global.prehistory.firsts.butchery`,
`global.prehistory.firsts.cereal-farming`, `global.prehistory.firsts.chicken`,
`global.prehistory.firsts.cut-marks`, `global.prehistory.firsts.dog`,
`global.prehistory.firsts.fermented-drink`, `global.prehistory.firsts.figurative-art`,
`global.prehistory.firsts.horse-domestication`, `global.prehistory.firsts.irrigation`,
`global.prehistory.firsts.pottery`, `global.prehistory.firsts.spun-fibre`,
`global.prehistory.firsts.wheel`, `global.prehistory.firsts.woven-cloth`,
`global.prehistory.firsts.writing`.

### T3. Uncertainty must scale with age for pre-Holocene dates
**Rule:** if `start < -12000`, then `(bounds[1] - bounds[0]) >= 0.02 * abs(start)` — a minimum
uncertainty of 2% of the age.
**Standing:** `advisory`.
**Legitimate exception:** an ice-core or varve-counted date can be far more precise than 2% at great
age; `europe.prehistory.event-8point2ka` (`dated_by: layer-counting`) would fail a naive version of
this rule and is correct as it stands. Exempt `layer-counting` and `radiocarbon-calibrated` inside the
Holocene.
**Violations, all from missing rather than narrow bounds (18):** every pre-Holocene
`global.prehistory.firsts.*` threshold listed in T1, plus — for narrowness rather than absence —
`global.prehistory.hominins.homo-antecessor` (2.34% of 855 ka, marginal) and
`global.prehistory.firsts.cooking`, whose bounds if completed as `[-779000, -778000]` would be
0.13% of an 800,000-year age.
**Why this one matters most:** it is the direct inverse of the Berlin Wall bug. That bug was excess
uncertainty on a precise date; this is fictional precision on an imprecise one, and it is the
characteristic failure of the `threshold` kind.

### T4. `date_standing: consensus` requires a known dating method
**Rule:** if `date_standing == "consensus"` then `dated_by != "unknown"`.
**Standing:** `safe`.
**Why:** the field cannot simultaneously assert that scholars agree on a date and that nobody knows
how it was obtained.
**Violations (3):** `global.prehistory.hominins.denisovans`,
`global.prehistory.hominins.homo-heidelbergensis`, `global.prehistory.hominins.homo-neanderthalensis`.

### T5. `date_standing: consensus` is not available to single-site prehistoric firsts
**Rule:** if `kind == "threshold"` and `start < -10000`, `date_standing` may not be `consensus`.
**Standing:** `advisory`.
**Legitimate exception:** a few deep thresholds really are settled — the 2.6 Ma Oldowan first
appearance would defensibly be `consensus`. But the rule fires on exactly the entries where a reader
is most likely to be misled.
**Violations (7):** `global.prehistory.firsts.cooking`, `global.prehistory.firsts.figurative-art`,
`global.prehistory.firsts.pigment-use`, `global.prehistory.firsts.pottery`,
`global.prehistory.firsts.spun-fibre`, `global.prehistory.firsts.stone-knapping`,
`global.prehistory.firsts.wood-structure`. (`global.prehistory.firsts.symbolic-engraving` also fires.)

### T6. `dated_by: first-attestation` requires a date within the era of writing
**Rule:** if `dated_by == "first-attestation"` then `start > -3400`, the earliest date this dataset
itself assigns to writing.
**Standing:** `safe`.
**Why:** a first attestation presupposes an attestation. The rule is self-referential against the
file's own `global.prehistory.firsts.writing` entry, so it stays correct if that date moves.
**Violations (1):** `oceania.peoples-aboriginal-australians` (−65000).
**Recommended companion, `advisory`:** `first-attestation` also requires the date to fall within the
attested history of the relevant script tradition. That catches
`global.languages.quechua` (1000 CE, first written in the 1500s),
`global.languages.nahuatl` (600 CE, same),
`global.languages.avestan` (−1200, manuscripts a millennium later),
`global.languages.sanskrit` (−1500, oral transmission),
`africa.peoples-bantu-peoples` (−3000), `europe.peoples-sami` (−1000) and
`global.traditions.zoroastrianism` (−1200) — but it needs a per-region script table, so it cannot
fail a build.

### T7. `dated_by: calendar` requires a calendar
**Rule:** `dated_by == "calendar"` is permitted only if `start > 1400` CE, or the entity's
`date_standing` is `consensus` and its kind is `event`.
**Standing:** `advisory`.
**Legitimate exception:** `europe.mediterranean.rome.republic.late.caesar-assassination` (−44) and
`...actium` (−31) are genuinely calendar-dated from Roman sources, and correctly marked `consensus`
events — hence the second clause.
**Violations (1, and it is a real error):** `west-asia.arabia.pre-islamic.incense-trade`, a caravan
network spanning −700 to 200 with `dated_by: calendar` and no bounds. No calendar fixes the start of
a trade route.
**Also worth flagging under a stricter variant:** `west-asia.anatolia.hittites.sack-of-babylon`
(−1595) and `west-asia.anatolia.hittites.kadesh` (−1274) are `calendar` with `[null, null]`, and both
depend entirely on which Bronze Age chronology is chosen.

### T8. Bounds must not be perfectly symmetric across the whole dataset
**Rule:** the share of entities with two-sided bounds where `start - bounds[0] == bounds[1] - start`
must not exceed a threshold — say 70%.
**Standing:** `advisory`, and it is a dataset-level test rather than a per-entity one.
**Current state:** 89 of 91 two-sided bounds are exactly symmetric. The only two exceptions are
`global.prehistory.hominins.homo-heidelbergensis` and `global.traditions.mahayana`, and both of those
are themselves errors.
**Why:** real scholarly uncertainty is rarely symmetric — an earliest-occurrence date has a hard
floor and a soft ceiling, and a *terminus post quem* is one-sided by construction. Near-total
symmetry is a fingerprint of a generator applying ±N, which is precisely the mechanism that produced
the ±100 years on 1989. This test would have caught that bug as a class rather than as an instance.

### T9. Bounds must bracket the start
**Rule:** `bounds[0] <= start <= bounds[1]` whenever both are non-null; and if only `bounds[0]` is
set, `bounds[0] <= start`.
**Standing:** `safe`.
**Current violations of the strict two-sided form:** none.
**But:** `west-asia.iran.arab-conquest` has `start 633`, `end 651`, `bounds [608, 658]` — the bounds
bracket the start but the lower bound predates it by 25 years and the upper bound sits inside the
event's own span. A useful strengthening for spans: **if `end` is set, `bounds` must describe the
start alone, so `bounds[1] <= end`.** Under that form, `arab-conquest` fails
(`bounds[1] = 658 > end = 651`), which is the only place in the file where a start's uncertainty
overruns the end of the thing being dated. Mark the strengthened form `safe`.

### T10. Post-medieval documented dates may not carry uncertainty
**Rule:** if `start > 1500`, then `bounds == [null, null]`.
**Standing:** `advisory`.
**Legitimate exception:** a genuinely undated modern thing — an undocumented vernacular building, an
oral-history event in a region without records — could need bounds after 1500.
**Violations (2):** `global.networks.atlantic-slave-trade` (1501, `[1496, 1506]`) and
`global.networks.manila-galleon` (1565, `[1560, 1570]`). Both start dates come from documentary
records; the ±5 is invented.
**Note:** no `event` after 1500 currently violates the ±5 form of this rule, so the Berlin Wall class
of bug appears to be genuinely fixed for events. It survives in `network` and `tradition`.

### T11. Near-exact historical dates may not carry uncertainty
**Rule:** an entity whose `start` is a date fixed to the day in the historical record must have
`bounds == [null, null]`. Implementable as a curated allow-list of such years per entity, or by
requiring that any entity with `date_standing == "consensus"` and `start > 0` have null bounds.
**Standing:** `advisory` (the allow-list needs maintenance).
**Violations (5):** `global.traditions.great-schism` (1054, `[1049, 1059]` — 16 July 1054),
`global.traditions.sunni-shia-split` (632, `[627, 637]` — Muhammad's death),
`global.traditions.islam` (610, `[605, 615]`), `global.traditions.sikhism` (1500, `[1480, 1520]`),
`global.networks.atlantic-slave-trade` (1501).

### T12. Event-shaped names may not be filed under a non-event kind
**Rule:** if `name` matches `/schism|split|battle|\bwar\b|massacre|conference|assassination|sack|
invasion|revolt|rebellion|treaty|siege/i` then `kind == "event"`.
**Standing:** `advisory`.
**Legitimate exception:** a school named after a conflict, or a polity like "the Warring States", would
trip this and be correctly filed elsewhere. It should warn, not block.
**Violations (2), both real errors:** `global.traditions.great-schism` and
`global.traditions.sunni-shia-split` are dated events filed as religions. `great-schism` additionally
carries `extant: true` and `end: null`, i.e. an event of 1054 that is still going on.

### T13. An entity that is not a continuing thing may not be `extant`
**Rule:** `extant` may be true only if `end` is null AND `kind` is in
`{language, tradition, people, network, taxon}`. Additionally, if `kind == "event"` or the entity
fails T12, `extant` must be null.
**Standing:** `safe`.
**Violations (1):** `global.traditions.great-schism` (`extant: true` on a completed event).
**Note:** the general form is already clean — no entity in the file has both `extant: true` and a
non-null `end`.

### T14. An extinct taxon must have a last-appearance date
**Rule:** if `kind == "taxon"` and `extant` is not true, then `end` must be non-null.
**Standing:** `advisory`.
**Legitimate exception:** a taxon known from a single specimen has no meaningful range, and forcing an
`end` would fabricate one. The right fix there may be to set `end == start` and say so in the summary.
**Violations (2):** `global.prehistory.hominins.homo-longi` and
`global.prehistory.hominins.homo-luzonensis` — both extinct hominins with a null end, which renders
as no known extinction.
**Companion, `safe`:** a taxon's `end` must not postdate the present unless `extant` is true.
No current violations, but it is cheap insurance.

### T15. Deep-time dates must be rounded to their stated precision
**Rule:** if `abs(start) > 100000`, `start` must be a multiple of 1000. If `abs(start) > 1000000`,
a multiple of 10000.
**Standing:** `safe`.
**Why:** the `-050` suffix throughout the taxa is a residue of BP→BCE conversion (the 1950 offset)
and presents Middle Pleistocene ages as accurate to the decade. No palaeoanthropological date
supports that.
**Violations (10):** `global.prehistory.hominins.denisovans` (−193050),
`homo-antecessor` (−855050), `homo-erectus` (−1888050), `homo-floresiensis` (−98050),
`homo-habilis` (−2398050), `homo-longi` (−144050), `homo-luzonensis` (−132050),
`homo-naledi` (−333050), `homo-neanderthalensis` (−398050), `homo-rudolfensis` (−1898050).
**Related, `advisory`:** the same conversion residue at shallower depth produces
`global.prehistory.firsts.artificial-mummification` (−6051),
`global.prehistory.firsts.cereal-farming` (−8651),
`global.prehistory.firsts.cooking` (−778000 with a −779000 bound), and
`global.prehistory.firsts.figurative-art` (−49300). A rule requiring multiples of 50 below −5000
would catch these; `southeast-asia.prehistory.austronesian-expansion.isea-pottery` (−3481) and
`southeast-asia.prehistory.neolithic-migration-sea` (−2051) show the same signature above it.

### T16. Every entity must have a summary
**Rule:** `summary` must be non-null and at least, say, 20 characters.
**Standing:** `safe`.
**Violations (1):** `central-asia.scythians`.

### T17. Sibling entities of the same kind must share an id prefix and a parent
**Rule:** within a kind, entities under the same top-level region should follow the same id pattern.
Twelve of thirteen `people` use `<region>.peoples-<name>` and sit directly under the region.
**Standing:** `advisory` (a real sub-grouping may justify a deeper parent).
**Violations (1):** `central-asia.scythians` — id lacks the `peoples-` segment and it is filed under
"Eurasian Steppe < Central Asia & the Steppe" while the Sarmatians, defined in their own summary as
"successors to the Scythians", sit one level up. A reader comparing the two will find them in
different places.

### T18. A cross-reference in a summary must agree with the referenced entity's own dates
**Rule:** where a summary asserts a numeric interval relative to another concept ("N years before X",
"N centuries after Y"), the arithmetic must hold against that entity's `start`. Implementable by
extracting `\b(\d[\d,]*)\s*(years|centuries|millennia)\s+(before|after)\b` and requiring a named
target entity id in a new optional field.
**Standing:** `advisory` — it needs a new field to be checkable, so it cannot fail a build today.
**Violations found by hand (2):** `global.prehistory.firsts.cut-marks` says Dikika is "roughly
800,000 years before the oldest known stone tools" while this file's `stone-knapping` puts those at
−3,300,000, only 90,000 years earlier. `global.prehistory.firsts.artificial-mummification` says "two
thousand years before anyone in Egypt" while its own −6051 start makes the gap three and a half
thousand. Also in this class: `global.languages.sumerian` calls itself "the first written language"
while `global.prehistory.firsts.writing` calls Uruk and Abydos simultaneous independent inventions.
**Why it is worth building:** this is the only test here that checks a *claim* rather than a shape,
and all three violations are exactly the kind of thing a reader spots and a validator never does.
