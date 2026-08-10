# Correctness review: `reigns.json` (702 rulers and named individuals)

Judgement pass, no web verification. Regnal chronologies were checked for internal consistency
(consecutive reigns, dynasty spans in `polities.json`), for plausibility of reign length, and for
`dated_by` / `historicity` / `date_standing` fitting how the date is actually known.

Overall: the modern half of the dataset (post-1000 CE Europe, China, Korea, Japan, South Asia) is in
good shape — I found almost nothing wrong in the Ming, Qing, Song, Joseon, Goryeo, Tokugawa,
Ashikaga, Mughal, Delhi Sultanate, Byzantine Komnenian/Palaiologan, Roman imperial, or modern
political sequences. The problems concentrate in (a) Egyptian chronology, where accession years are
mixed between competing schemes and produce overlaps and gaps, (b) the metadata fields `dated_by`
and `bounds`, which are applied by a rule that does not match how these dates are known, and
(c) a handful of interrupted reigns collapsed into one continuous span.

Patterns are stated once at the end rather than repeated per row.

---

## Egypt — chronology internal to dynasties

### africa.nile.egypt.new-kingdom.dyn20.ramesses-iii
**Field:** start
**Currently:** -1186 (reign -1186..-1155), identical to the accession of his father Setnakht
(-1186..-1184) and to the 20th Dynasty's own start
**Should be:** -1184 (Ramesses III c. 1184–1153)
**Confidence:** high
**Why:** As it stands Ramesses III's reign begins two years before Setnakht's ends, and the two
overlap for the whole of Setnakht's reign; the conventional chronology this dataset otherwise
follows puts Ramesses III's accession at Setnakht's death.

### africa.nile.egypt.new-kingdom.dyn19.seti-i
**Field:** start
**Currently:** -1290, leaving a four-year vacancy after Ramesses I ends in -1294
**Should be:** -1294
**Confidence:** high
**Why:** Seti I succeeded his father directly; the 19th Dynasty span (-1295..-1186) and Ramesses I's
own dates (-1295..-1294) both come from the chronology in which Seti I is 1294–1279, so -1290 is a
value imported from a different scheme and leaves four years with no king.

### africa.nile.egypt.old-kingdom.dyn3.sanakht
**Field:** start/end (or Djoser's)
**Currently:** Sanakht -2686..-2667 while Djoser is -2670..-2650 — a three-year overlap
**Should be:** unclear — either Sanakht ends -2667 and Djoser runs -2667..-2648, or Djoser is placed
first in the dynasty; the two rows cannot both stand
**Confidence:** medium
**Why:** Two consecutive 3rd Dynasty kings overlap, and Djoser's end (-2650) then leaves a further
two-year gap before Sekhemkhet (-2648), so the dynasty's internal arithmetic does not close.

### africa.nile.egypt.tip.dyn25.piye
**Field:** end (or Shabaka's start)
**Currently:** Piye -744..-714 overlapping Shabaka -721..-707 by seven years
**Should be:** unclear — the mainstream scheme is Piye 747–716, Shabaka 716–702, Shebitku 702–690
**Confidence:** medium
**Why:** Two Kushite kings of the same line cannot overlap for seven years; the row set mixes an
older Piye dating with a Shabaka dating from a different reconstruction. Related: the Shabaka /
Shebitku order here follows the pre-Tang-i Var arrangement, which most Egyptologists now reverse.

### africa.nile.egypt.early-dynastic.dyn1.merneith
**Field:** end (or Den's start)
**Currently:** Merneith (regent) -2990..-2980 overlapping Den -2985..-2930
**Should be:** Merneith's regency should end where Den's reign begins
**Confidence:** medium
**Why:** She is presented as regent *for* Den, so a five-year overlap of regency and reign is
internally contradictory.

### africa.nile.egypt.sip.dyn15-hyksos.khyan
**Field:** end (or Apepi's start)
**Currently:** Khyan -1610..-1580, Apepi -1590..-1550 — a ten-year overlap between successive Hyksos
kings
**Should be:** Khyan ending c. -1590
**Confidence:** medium
**Why:** No co-regency is claimed, and the 15th Dynasty is not presented here as a divided kingship.

### africa.nile.egypt.new-kingdom.dyn18.amenhotep-iii
**Field:** start
**Currently:** -1388, two years after Thutmose IV ends (-1390)
**Should be:** -1390 (if the Thutmose IV dates are kept)
**Confidence:** low
**Why:** -1388 belongs to von Beckerath's scheme while Thutmose IV's -1400..-1390 belongs to Shaw's;
mixing them opens a two-year interregnum that no source posits.

### africa.nile.egypt.tip.dyn21.psusennes-i
**Field:** end
**Currently:** -991, overlapping Amenemope (-993..-984)
**Should be:** -993, or the overlap should be labelled a co-regency
**Confidence:** low
**Why:** Defensible as a documented co-regency, but as presented two Tanite kings simply overlap.

### africa.nile.egypt.middle-kingdom.dyn11.intef-i / intef-ii / intef-iii
**Field:** under (placement)
**Currently:** filed under `11th Dynasty (reunified) < Middle Kingdom`, with reigns -2125..-2055
**Should be:** the pre-reunification Intefs belong to the First Intermediate Period
(-2181..-2055), not the Middle Kingdom
**Confidence:** medium
**Why:** The Middle Kingdom begins at -2055 in this dataset's own `polities.json`, and
Mentuhotep II's summary here says he founded it — so three reigns that end before he acceded are
filed inside a period that had not started, and the parent dynasty row itself starts 70 years before
its parent period.

### africa.nile.egypt.sip.dyn15-hyksos.salitis
**Field:** historicity (and dated_by)
**Currently:** absent (i.e. accepted); `dated_by: unknown`
**Should be:** `legendary` or `contested`; `dated_by: received`
**Confidence:** medium
**Why:** Salitis is known only from Manetho as transmitted by Josephus, with no contemporary
attestation and no monuments; presenting him as an accepted king with a twenty-year reign
(-1650..-1630) overstates the evidence, especially beside Khyan and Apepi, who are attested.

### africa.nile.egypt.early-dynastic.dyn1.narmer
**Field:** historicity
**Currently:** `contested`
**Should be:** absent (accepted), with the Menes identification and the dates flagged instead — the
`date_standing: traditional` and the summary already do this
**Confidence:** medium
**Why:** Narmer's existence is not contested: he is attested on the Narmer Palette, on serekhs from
Egypt and the southern Levant, and in the Abydos king lists. What is contested is his equation with
Manetho's Menes and the extent of the unification, both of which the summary covers.

### africa.nile.egypt.old-kingdom.dyn6.nitocris
**Field:** start/end
**Currently:** -2184..-2181, a three-year reign given to the year for a figure marked `legendary`
**Should be:** no year-level dates, or an explicit floruit window
**Confidence:** low
**Why:** A row that says in one field that the person may not have existed and in another that she
reigned exactly three specific years reads as far firmer than the evidence.

### africa.nile.egypt.ptolemaic.ptolemy-ix
**Field:** start/end
**Currently:** -116..-81 as one continuous reign, overlapping Ptolemy X (-110..-88)
**Should be:** two tenures, c. 116–107 and 88–81
**Confidence:** medium
**Why:** Ptolemy IX was driven out by Ptolemy X and returned nineteen years later; presented as a
single 35-year reign it contradicts the neighbouring row rather than complementing it. Ptolemy VIII
(-170..-116) has the same problem in milder form (170–164, then 145–116).

---

## China, Korea, Japan

### east-asia.china.tang.zhongzong
**Field:** start/end
**Currently:** 684..710, a 26-year reign that entirely contains Ruizong's first reign (684–690) and
Wu Zetian's Zhou (690–705)
**Should be:** two tenures — 684 (a few weeks) and 705–710
**Confidence:** high
**Why:** Zhongzong was deposed by his mother within months in 684 and only restored in 705; as
written the row asserts he was emperor throughout Wu Zetian's reign, which the dataset also records.

### east-asia.china.legendary.shennong
**Field:** start/end
**Currently:** -2852..-2697, byte-identical to Fuxi's -2852..-2697
**Should be:** the traditional sequence puts Shennong after Fuxi (commonly c. 2737–2698)
**Confidence:** medium
**Why:** Two successive Three Sovereigns cannot hold the identical 155-year span; one row has clearly
been copied from the other.

### east-asia.korea.three-kingdoms.jangsu
**Field:** summary
**Currently:** "presided over a 79-year reign, the longest in East Asian history"
**Should be:** "the longest reign in Korean history" (or drop the superlative)
**Confidence:** low
**Why:** The claim is defensible only if legendary Japanese reigns are excluded and the comparison
set is narrow; the safe and usual formulation is the Korean one.

### east-asia.japan.azuchi-momoyama.nobunaga
**Field:** start (or placement)
**Currently:** 1568..1582, filed under Azuchi–Momoyama Period, which `polities.json` starts at 1573
**Should be:** either the period start or Nobunaga's start needs to move; his 1568 entry into Kyoto
predates the period he is filed in by five years
**Confidence:** low
**Why:** Not a factual error about Nobunaga, but the row sits five years outside its own parent.

### east-asia.china.han.western.gaozu
**Field:** start
**Currently:** -202, while the Western Han parent begins -206
**Should be:** defensible as written (emperor from 202; king of Han from 206) — flagged only because
it leaves the dynasty's first four years with no ruler row
**Confidence:** low
**Why:** A reader comparing the dynasty span to its first reign will see a four-year hole.

---

## Rome and Byzantium

### europe.mediterranean.byzantine.justinian-ii
**Field:** start/end
**Currently:** 685..711 as one continuous reign
**Should be:** 685–695 and 705–711
**Confidence:** high
**Why:** He was deposed, mutilated and exiled for ten years; a single 26-year span erases the
Leontios/Tiberios III interval and makes the reign look twice as long as it was.

### europe.mediterranean.rome.empire.constantine
**Field:** under (placement)
**Currently:** `Roman Empire < Ancient Rome < Mediterranean < Europe` — the only reign filed directly
at that level
**Should be:** `Constantinian Dynasty` (306–363 in `polities.json`), which his 306–337 fits exactly
and which already holds his sons
**Confidence:** high
**Why:** Constantine's four sons and Julian are in the Constantinian Dynasty and Constantine is not,
so a reader browsing that dynasty finds it without its founder.

### europe.mediterranean.rome.republic.* (Gracchi, Marius, Sulla, Crassus, Pompey, Cicero, Cato, Mark Antony, Octavian)
**Field:** under (placement)
**Currently:** filed directly under `Roman Republic`, while `Late Republic` (-133..-27) exists as a
child and holds only Julius Caesar
**Should be:** all of these fall inside -133..-27 and belong in `Late Republic` alongside Caesar
**Confidence:** medium
**Why:** Identical figures from the same two decades are split across two levels for no stated
reason; Tiberius Gracchus (-133) literally defines the sub-period's start yet sits above it.

### europe.mediterranean.rome.empire.clodius-albinus / pescennius-niger
**Field:** under (placement)
**Currently:** filed under `Year of the Five Emperors`, whose span is 193..193, with reigns running
to 197 and 194
**Should be:** placement or span needs to give; as written two children outlive their parent by up to
four years
**Confidence:** low
**Why:** Both were proclaimed in 193 and held out for years afterwards, so the reign dates are right
and the container is too narrow.

### europe.western.carolingian.charlemagne
**Field:** summary
**Currently:** "First Emperor of the Romans since antiquity"
**Should be:** "first emperor in the West since 476" — the Eastern emperors held the title
continuously and unbrokenly in 800
**Confidence:** medium
**Why:** As phrased it contradicts the dataset's own Byzantine sequence, in which Irene of Athens is
reigning as emperor in the year Charlemagne was crowned.

### europe.western.france.napoleon.napoleon-i
**Field:** start/end vs summary
**Currently:** 1804..1814, summary ends "before defeat at Waterloo (1815)"
**Should be:** either note the Hundred Days as a second tenure or drop the 1815 reference
**Confidence:** low
**Why:** The row's own summary describes an event outside the reign it records, with no second row to
hold it — the dataset does this correctly elsewhere (Humayun restored, Yoshitane restored).

---

## West and Central Asia, South Asia

### west-asia.mesopotamia.old-babylonian.hammurabi
**Field:** dated_by (and bounds)
**Currently:** `calendar`, `bounds: [null, null]`, `date_standing: majority`
**Should be:** not `calendar`; these are middle-chronology dates resting on the Venus tablet of
Ammisaduqa and eponym/king lists, and they need bounds
**Confidence:** high
**Why:** Nothing about -1792..-1750 comes from a calendar. Competing chronologies move Hammurabi by
roughly 56–64 years in either direction (high 1848–1806, low 1728–1686), so this is precisely the
case where absent bounds mislead: the row shows zero uncertainty on the most chronology-dependent
date in the dataset.

### west-asia.arabia.rise-islam.muhammad
**Field:** start
**Currently:** 610..632, filed as a reign
**Should be:** 622–632 if the row records rule; 610 is the traditional date of the first revelation,
not of any authority
**Confidence:** medium
**Why:** As a `reign` row it asserts twelve years of rule that did not exist — Muhammad held no
political authority in Mecca before the hijra.

### west-asia.mesopotamia.sumerian.gilgamesh
**Field:** start/end
**Currently:** -2700..-2600, i.e. a 100-year reign, `historicity: legendary`
**Should be:** a floruit window, not a reign span
**Confidence:** medium
**Why:** A century-long reign is implausible on its face, and the two numbers are plainly the ends of
an uncertainty range being displayed as accession and death.

### south-asia.satavahana.gautamiputra / vasishthiputra
**Field:** start/end
**Currently:** Gautamiputra Satakarni 78..102 overlapping Vasishthiputra Pulumavi 96..130
**Should be:** unclear — Satavahana chronology is genuinely disputed, but father and son should not
overlap by six years, and the following gap to Yajna Satakarni (152) is unexplained
**Confidence:** medium
**Why:** Successive rulers of one line overlap, and the dates appear drawn from two different
reconstructions (the Saka-era-based and the Puranic-list-based).

### south-asia.persons-mahavira
**Field:** date_standing
**Currently:** absent, with -599..-527 given to the year and `dated_by: first-attestation`
**Should be:** `traditional`
**Confidence:** medium
**Why:** 599–527 BCE is the traditional Jain reckoning; a substantial body of scholarship places him
c. 540–468, and nothing about these dates rests on first attestation.

### south-asia.persons-siddhartha-gautama
**Field:** date_standing / dated_by
**Currently:** -480..-400, `dated_by: first-attestation`, no date_standing
**Should be:** flag as contested/majority — this is the short chronology, against the traditional
563–483
**Confidence:** low
**Why:** Defensible as a choice, but presented as if uncontroversial in a dataset that marks far less
disputed dates as `traditional`.

### central-asia.persons-zoroaster / east-asia.persons-laozi
**Field:** start/end
**Currently:** Zoroaster -1200..-1000; Laozi -600..-500
**Should be:** floruit ranges, not lifespans — as written they read as a 200-year and a 100-year life
**Confidence:** medium
**Why:** Neighbouring person rows (Confucius -551..-479, Aristotle -384..-322) use start/end as birth
and death, so the same fields carry two incompatible meanings and these two look absurd by
comparison.

---

## Kind and structure

### europe.western.netherlands
**Field:** kind (and the row's existence in this file)
**Currently:** `kind: reign`, `name: The Netherlands`, `under: Western Europe < Europe`, 1581..null,
summary describing "the Dutch Republic and its successors, and the two chartered companies"
**Should be:** a polity, not a reign — `polities.json` already files the VOC and WIC beneath
`europe.western.netherlands` as its children
**Confidence:** high
**Why:** A country is not a reign and has no ruler; this row is a polity parent that has landed in
the reigns file, which is why it is the only "reign" in the dataset with no person and no end.

---

## Patterns (stated once)

### P1. `bounds` are computed from the start date only, so they exclude the end of any reign longer than the bound width
**Confidence:** high that the values are as described; medium that this is wrong rather than intended

Some 75 rows have an `end` outside their own `bounds` — e.g. Ezana 320..360 with bounds [295, 345],
Augustus -27..14 with [-52, -2], Basil II 976..1025 with [951, 1001], Ramesses II's dynasty-mates,
Kumaragupta I, Nandivarman II, Pepi II. In every case bounds = start ± 25 (or ± 50 / ± 100 for
older rows). If bounds are meant as uncertainty on the accession, they are technically defensible
but will render as an interval that does not contain the reign; if they are meant as the row's date
envelope, they are wrong on a tenth of the file. Either way one convention should be stated and
applied.

### P2. The bound *widths* are wrong in both directions
**Confidence:** high

- **Too wide:** Roman emperors carry ±25 years (Caligula 37..41 with bounds [12, 62]; the Year of the
  Four Emperors rows, dated to the month, carry [43, 93] and [44, 94]). Ptolemies, Achaemenids
  (Cyrus [-609, -509]), Han and Tang emperors, and Muhammad ([585, 635]) are the same. Achaemenid,
  Ptolemaic, Han and Roman regnal dates are fixed by documentary and astronomical records to the
  year or better; ±25 or ±50 years on them is a century-scale error of the kind this brief exists to
  catch.
- **Too narrow / absent:** Hammurabi has no bounds at all despite a ~60-year chronology dispute, and
  every legendary row (Romulus, Dangun, the Three Sovereigns, Gilgamesh, Nitocris) has
  `bounds: [null, null]` while carrying year-precise start and end.

### P3. `dated_by: unknown` on dates that are documentary
**Confidence:** high

All 79 Roman imperial rows, all 18 Ptolemaic rows, the Achaemenids, the Han, Sui and Tang emperors,
the Sasanians and the early Byzantines are `dated_by: unknown`. These are the best-documented regnal
dates in antiquity — consular fasti, papyri, coinage, Babylonian astronomical diaries, the *Shiji*
and the standard histories. `unknown` tells the reader nobody knows where the date came from, which
is the opposite of the case, and it is the single most widespread metadata error in the file.

### P4. `dated_by` flips from `unknown` to `calendar` at an arbitrary threshold, mid-dynasty
**Confidence:** high

The Northern Song splits at Renzong (Taizu, Taizong, Zhenzong `unknown` with ±25 bounds; Renzong
onwards `calendar` with none). The Cholas split at Rajendra I, the Byzantines at Romanos IV, the
Korean Three Kingdoms between Jangsu and Seong of Baekje. Nothing changed about how these dates are
known across those boundaries; the cut appears to be roughly "before/after 1050 CE". Consecutive
reigns in one dynasty should not disagree about how they are dated.

### P5. Egyptian dates before ~2000 BCE claim year precision they cannot have
**Confidence:** high

Every Early Dynastic, Old Kingdom and early 11th Dynasty reign carries single-year accession and
death dates — Anedjib -2930..-2925, Khaba -2640..-2637, Userkare -2333..-2332, Merenre II
-2184..-2184. Egyptian chronology before the Middle Kingdom is not resolvable to the year and is
conventionally cited in round decades with an explicit ± of 50–150 years; the ±100 bounds here are
the right order of magnitude, but the headline figures read as exact. The knock-on effect is
visible in the overlaps and gaps reported above: false precision makes each dynasty's arithmetic
look broken when in reality no one knows the numbers that closely.

Related: Egyptian reigns are all `dated_by: unknown`. They rest on king lists (Turin Canon, Abydos,
Manetho), dead reckoning from dated regnal-year documents, and astronomical/Assyrian synchronisms.
If the vocabulary has no `king-list` or `synchronism` value, `received` fits far better than
`unknown`.

### P6. Pre-colonial American, West African and Southern African reigns are `dated_by: calendar` with no bounds
**Confidence:** medium

Itzcoatl, Moctezuma I, Ahuitzotl, Pachacuti, Topa Inca, Huayna Capac, Sundiata Keita, Sunni Ali,
Askia Muhammad and Shaka all carry `calendar` and `bounds: [null, null]`, i.e. zero uncertainty.
Inca dates before Atahualpa are reconstructions from Spanish colonial chroniclers and are disputed
by decades; Aztec dates come from codices requiring calendar correlation; Sundiata's 1235 and 1255
come from oral epic plus Ibn Khaldun. These deserve bounds and a `received` or `traditional`
marking, exactly as the Roman kings and Dangun get. The one internal symptom: the Aztec Empire spans
1428..1521 while Itzcoatl's reign starts 1427.

### P7. Interrupted reigns collapsed into single spans
**Confidence:** high where flagged individually

The dataset handles this correctly in several places (Humayun / Humayun restored, Ashikaga Yoshitane
/ Yoshitane restored, Zhengtong / Tianshun, Indira Gandhi, Benazir Bhutto, Sheikh Hasina) and
incorrectly in others (Zhongzong, Justinian II, Ptolemy IX, Ptolemy VIII). Emperor Ruizong is the
mirror image: his first reign (684–690) is present, his second (710–712) is missing, which is why
there is a two-year hole before Xuanzong.

### P8. Cosmetic but load-bearing: split id prefixes inside the 25th Dynasty
**Confidence:** high

`africa.nile.egypt.tip.dyn25.piye` and `...dyn25.taharqa` sit beside
`...dyn25-kushite.shabaka`, `...dyn25-kushite.shebitku`, `...dyn25-kushite.tantamani`, while
`polities.json` has only `dyn25-kushite`. Two of the five kings are keyed to a parent that does not
exist.

---

## The twenty worst

1. **east-asia.china.tang.zhongzong** — a 26-year reign that swallows Wu Zetian's entire reign; two
   short tenures presented as one long one.
2. **europe.mediterranean.byzantine.justinian-ii** — 685..711 as one span erases a ten-year
   deposition and exile and doubles the apparent reign.
3. **P3 — `dated_by: unknown` on ~120 Roman, Ptolemaic, Achaemenid, Han/Tang and Sasanian rows**, the
   best-documented regnal dates in antiquity.
4. **P2 — ±25-year bounds on reigns dated to the day**, including the Year of the Four Emperors and
   Caligula; a reader is told Rome's imperial chronology is uncertain by a generation.
5. **africa.nile.egypt.new-kingdom.dyn20.ramesses-iii** — accession set two years before his
   predecessor's death, overlapping Setnakht's whole reign.
6. **europe.western.netherlands** — a country filed as a reign, with no person, no end, and children
   in another file.
7. **west-asia.mesopotamia.old-babylonian.hammurabi** — `dated_by: calendar` with no bounds on the
   single most chronology-dependent date in the dataset.
8. **africa.nile.egypt.new-kingdom.dyn19.seti-i** — four kingless years between Ramesses I and Seti I,
   caused by mixing two chronologies.
9. **P5 — year-precise Egyptian dates before 2000 BCE**, which manufacture the overlaps and gaps
   reported throughout the Old Kingdom.
10. **west-asia.arabia.rise-islam.muhammad** — a reign starting in 610, twelve years before he held
    any authority.
11. **europe.mediterranean.rome.empire.constantine** — the Constantinian Dynasty filed without
    Constantine.
12. **africa.nile.egypt.tip.dyn25.piye** — seven-year overlap with Shabaka, plus a superseded
    Shabaka/Shebitku order.
13. **africa.nile.egypt.ptolemaic.ptolemy-ix** — an interrupted reign shown as continuous and
    overlapping Ptolemy X.
14. **east-asia.china.legendary.shennong** — dates copied verbatim from Fuxi.
15. **africa.nile.egypt.sip.dyn15-hyksos.salitis** — a Manetho-only king presented as accepted
    history with exact dates.
16. **P6 — Inca, Aztec, Mali, Songhai and Zulu reigns marked `calendar` with zero uncertainty**, when
    they rest on colonial chronicles, codices and oral tradition.
17. **africa.nile.egypt.middle-kingdom.dyn11.intef-i/ii/iii** — three reigns filed inside a Middle
    Kingdom that had not begun.
18. **africa.nile.egypt.old-kingdom.dyn3.sanakht** — overlaps Djoser, and the 3rd Dynasty's
    arithmetic does not close.
19. **africa.nile.egypt.early-dynastic.dyn1.narmer** — `historicity: contested` for a king attested
    on his own palette; it is the Menes identification that is contested.
20. **P4 — `dated_by` flipping mid-dynasty** in the Northern Song, the Cholas, the Byzantines and the
    Korean Three Kingdoms, at what appears to be an arbitrary date threshold.

## Proposed tests

Each test below is stated so it can be implemented directly against `reigns.json` plus its parent
files, with the threshold fixed. Violation lists are the current contents of the data, computed
mechanically, not by judgement. `safe` means I could find no legitimate exception and it can fail a
build; `advisory` means real history violates it and it should warn only — each advisory test names
the exception that makes it advisory.

### T1 — No reign starting before 747 BCE may be `dated_by: calendar`

**Rule:** if `start < -747` then `dated_by` must not be `calendar`. 747 BCE is the Nabonassar era,
the earliest point from which a continuous, astronomically anchored civil calendar is recoverable;
nothing earlier is dated by calendar in the sense this field means.

**Violations:** `west-asia.mesopotamia.old-babylonian.hammurabi` (-1792, `dated_by: calendar`,
`date_standing: majority`, bounds null).

**Status:** `safe`. Every other pre-747 row in the file already uses `received`, `unknown` or
`first-attestation`, so the rule costs nothing and catches the one row that asserts a precision no
Bronze Age date has. This is finding *hammurabi* above.

### T2 — Reigns before 2000 BCE must declare their dating standing and carry non-zero bounds

**Rule:** if `start < -2000` then `date_standing` must be non-null and `bounds` must be non-null with
half-width ≥ 25 years. Third-millennium regnal years come from king lists reconciled against a
handful of astronomical and radiocarbon anchors; the competing conventional chronologies differ by
50–150 years, so a bare year is a false claim regardless of which chronology it came from.

**Violations:** 44 rows, all Egyptian — the whole of `dyn1`, `dyn2`, `dyn3`, `dyn4`, `dyn5`, `dyn6`
and the early `dyn11` group, e.g. `africa.nile.egypt.early-dynastic.dyn1.hor-aha`,
`...dyn1.djer`, `...dyn1.den`, `...dyn2.peribsen`, `...dyn2.khasekhemwy`,
`africa.nile.egypt.old-kingdom.dyn3.sanakht`, `...dyn3.djoser`, `...dyn4.khufu`,
`...dyn6.pepi-ii`. `west-asia.mesopotamia.sumerian.gilgamesh` passes on `date_standing` but fails on
bounds.

**Status:** `safe` as stated, but it fails 44 rows on first run, so it should land with the
migration that adds `date_standing: conventional` to the Egyptian block. This is pattern **P5**, and
it is the upstream cause of the dyn1, dyn2, dyn3 and dyn6 overlaps reported individually above.

### T3 — `bounds` must contain both `start` and `end`

**Rule:** if `bounds` is non-null then `bounds[0] <= start` and `end <= bounds[1]`.

**Violations:** 74 rows. Every one is a reign whose `bounds` were generated as `start ± N` with no
regard for `end`, so any reign longer than N years fails: `africa.nile.aksum.ezana`,
`europe.mediterranean.rome.empire.augustus`, `europe.mediterranean.byzantine.basil-ii`,
`south-asia.gupta.kumaragupta-i`, `south-asia.pallava.nandivarman-ii`,
`east-asia.china.han.eastern.guangwu`, `east-asia.china.tang.gaozong-tang`,
`east-asia.china.tang.xuanzong`, `east-asia.china.tang.zhongzong`,
`east-asia.china.tang.dezong-tang`, `west-asia.iran.sasanian.shapur-i`,
`west-asia.iran.sasanian.khosrow-i`, `west-asia.iran.sasanian.khosrow-ii`,
`europe.persons-gutenberg`, `central-asia.persons-ibn-sina`, and 59 others.

**Status:** `safe`. There is no reading of `bounds` under which a reign's own end date falls outside
its uncertainty envelope. This is pattern **P1**, and it is the cheapest test here: it is pure
arithmetic on one row and it finds a systematic generation bug.

### T4 — Within a dynasty that otherwise chains exactly, no adjacent pair may be off by 1–5 years

**Rule:** group reigns by `under`. For groups with ≥4 dated reigns, sort by `start` and compute
`delta = next.start - this.end` for each adjacent pair. If ≥50% of the group's pairs have
`delta == 0` — i.e. the group was compiled as a continuous succession — then flag any pair with
`1 <= |delta| <= 5`. Rationale: in a source that chains reigns end-to-start, a small non-zero delta
is not a historical fact about an interregnum, it is two reigns taken from two different
chronologies.

**Violations (the diagnostic ones):** `dyn19.ramesses-i → dyn19.seti-i` (+4);
`dyn20.setnakht → dyn20.ramesses-iii` (-2); `dyn3.sanakht → dyn3.djoser` (-3);
`dyn3.djoser → dyn3.sekhemkhet` (+2); `dyn1.merneith → dyn1.den` (-5);
`dyn2.peribsen → dyn2.khasekhemwy` (+5); `dyn18.thutmose-iv → dyn18.amenhotep-iii` (+2);
`dyn21.smendes → dyn21.psusennes-i` (+4); `dyn21.psusennes-i → dyn21.amenemope` (-2);
`east-asia.china.tang.gaozong-tang → east-asia.china.tang.ruizong` (+1);
`south-asia.chola.kulottunga-iii → south-asia.chola.rajaraja-iii` (-2);
`south-asia.maurya.bindusara → south-asia.maurya.ashoka` (+5);
`americas.andes.inca.huayna-capac → americas.andes.inca.atahualpa` (+5);
`europe.mediterranean.byzantine.constantine-vii → ...nikephoros-ii` (+4);
`europe.mediterranean.byzantine.manuel-i → ...andronikos-i` (+3);
`east-asia.japan.kamakura.shogun-yoritomo → ...shogun-yoriie` (+3);
`east-asia.japan.muromachi.shogun-yoshikazu → ...shogun-yoshinori` (+4);
`east-asia.japan.muromachi.shogun-yoshiteru → ...shogun-yoshihide` (+3);
`east-asia.china.yuan.wenzong-yuan → ...mingzong-yuan` (-3), and 25 more.

**Status:** `advisory`. Legitimate exceptions are real and named: the Maurya +5 is the genuine
succession dispute between Bindusara's death and Ashoka's consecration in 268 BCE, the Ashokan
inscriptions themselves date from the consecration; the Muromachi +3 is the genuine 1565–1568
shogunal vacancy after Yoshiteru's assassination; the Byzantine +4 is Romanos II simply being absent
from the file rather than a bad date. But this test is what surfaced *seti-i*, *ramesses-iii*,
*sanakht*, *merneith* and *psusennes-i* — five real errors — and it does so without needing any
knowledge of who these people were.

### T5 — A reign that wholly contains another reign under the same parent must say why

**Rule:** for two reigns A, B under the same `under`, if `A.start <= B.start` and `A.end >= B.end`
and A is strictly longer than B, then A's `summary` must contain an explicit co-rule marker
(`co-regen`/`co-rul`/`co-emperor`/`regent`/`regency`/`rival`/`restored`/`usurp`/`deposed`), or a
dedicated `co_rule: true` field must be set. Full containment is either a co-regency, a regency, a
rival claim, or an error, and only the last of those goes unremarked.

**Violations (the errors, not the co-regencies):** `east-asia.china.tang.zhongzong`, whose
684..710 swallows both `east-asia.china.tang.ruizong` and `east-asia.china.tang.wu-zetian`;
`africa.nile.egypt.ptolemaic.ptolemy-ix` containing `...ptolemy-x`;
`africa.nile.egypt.new-kingdom.dyn20.ramesses-iii` containing `...setnakht`;
`africa.nile.egypt.old-kingdom.dyn6.nitocris` containing `...merenre-ii`;
`south-asia.independence.jinnah` containing `south-asia.independence.gandhi`;
`south-asia.independence.ambedkar` and `...gandhi` each containing `...subhas-bose`.

**Status:** `advisory`. The exception list is long and entirely genuine: `dyn18.thutmose-iii`
contains `dyn18.hatshepsut` because that co-regency is the historical fact; every Roman co-emperor
pair (`marcus-aurelius`/`lucius-verus`, `diocletian`/`maximian`, `caracalla`/`geta`,
`honorius`/`arcadius`) is a real joint rule; `east-asia.china.qing.cixi` contains `tongzhi` and
`guangxu` because she was regent over both; the same-year Crisis and Year-of-Five rows nest because
those claimants overlapped in months. The test's value is that it forces the distinction to be
recorded in the data rather than left to the reader, which is exactly what failed for Zhongzong.

### T6 — Two reigns under the same parent may not share an identical `start` and `end`

**Rule:** no two rows with the same `under` may have identical non-null `(start, end)`.

**Violations:** `east-asia.china.legendary.fuxi` and `east-asia.china.legendary.shennong`, both
-2852..-2697; `europe.mediterranean.rome.empire.balbinus`, `...gordian-i`, `...gordian-ii`,
`...pupienus`, all 238..238; `...didius-julianus` and `...pertinax`, both 193..193; `...otho` and
`...vitellius`, both 69..69.

**Status:** `advisory`. The legitimate exception is the sub-annual claimant: four emperors really did
begin and end in 238, and a year-granularity schema cannot distinguish them. But a 155-year
identical span is not that, and the Fuxi/Shennong duplication — a copy-paste of one traditional
regnal span onto the next sovereign — is a real error this test finds for free. Narrow it to
`safe` by exempting pairs where `end - start <= 1`.

### T7 — A reign longer than 63 years must carry `date_standing` or an explicit note

**Rule:** if `end - start > 63` then `date_standing` must be non-null, or `summary` must
acknowledge the length. 63 is chosen because Louis XIV's 72 years is the longest verified European
reign and Victoria's 64 the longest British; above that threshold the population is dominated by
traditional or symbolic figures.

**Violations:** `east-asia.china.legendary.fuxi` (155), `...shennong` (155),
`east-asia.china.legendary.emperor-yao` (100), `...huangdi` (100), `...zhuanxu` (78), `...emperor-ku`
(70) — all of which pass, they carry `date_standing: traditional` — versus the actual failures:
`africa.nile.egypt.old-kingdom.dyn6.pepi-ii` (94), `west-asia.mesopotamia.sumerian.gilgamesh` (100,
passes on `date_standing`), `central-asia.persons-zoroaster` (200),
`east-asia.persons-laozi` (100), `south-asia.persons-siddhartha-gautama` (80),
`east-asia.korea.three-kingdoms.jangsu` (78), `south-asia.kabir` (78),
`europe.persons-archimedes` (75), `south-asia.persons-aryabhata` (74),
`europe.western.france.bourbon.louis-xiv` (72), `east-asia.persons-confucius` (72),
`south-asia.persons-mahavira` (72), `europe.persons-socrates` (71),
`central-asia.persons-al-khwarizmi` (70), `south-asia.nanak` (70),
`europe.persons-gutenberg` (68), `south-asia.pallava.nandivarman-ii` (65),
`africa.nile.egypt.new-kingdom.dyn19.ramesses-ii` (66),
`europe.western.britain.victorian.victoria` (64), `south-asia.rashtrakuta.amoghavarsha` (64).

**Status:** `advisory`. Louis XIV's 72 years, Victoria's 64 and Ramesses II's 66 are all correct, so
this can never fail a build. It is still worth running: it is what makes `persons-zoroaster` (200
years) and `persons-laozi` (100 years) visible as lifespan-shaped rows filed as reigns, and it flags
`jangsu` and `nandivarman-ii`, whose lengths I doubt on other grounds.

### T8 — Legendary and mythological rows must declare `date_standing`

**Rule:** if `historicity` is `legendary` or `mythological` then `date_standing` must be non-null.
If the figure's existence is not accepted, the dates attached to them are by definition traditional
or received rather than established, and the field that says so must be filled.

**Violations:** `central-asia.persons-zoroaster` (`legendary`, -1200..-1000,
`date_standing: null`), `east-asia.persons-laozi` (`legendary`, -600..-500, `date_standing: null`).

**Status:** `safe`. The other 17 legendary and mythological rows already set `date_standing`, so the
two failures are omissions rather than a difference of policy.

### T9 — A reign's id prefix must resolve to an existing entity

**Rule:** strip the last dot-segment from `id`; the remainder must be either an existing entity `id`
somewhere in the corpus, or an ancestor of the row's own resolved parent. Exempt rows whose leaf
segment begins `persons-`, which are deliberately filed at region root.

**Violations:** `africa.nile.egypt.tip.dyn25.piye` and `africa.nile.egypt.tip.dyn25.taharqa`, whose
prefix `africa.nile.egypt.tip.dyn25` does not exist — the dynasty's id is
`africa.nile.egypt.tip.dyn25-kushite`, and the other four kings of that dynasty are keyed to it
correctly. Note the Roman emperors all pass: `europe.mediterranean.rome.empire.hadrian` is filed
under `nerva-antonine` but `europe.mediterranean.rome.empire` is a genuine ancestor of that parent.

**Status:** `safe`. This is pattern **P8**, and it is the class of error most likely to make a
downstream join silently drop rows.

### T10 — A row in `reigns.json` must be a person: no children, and an `end` unless living

**Rule:** no entity in any other file may name a `reigns.json` row as its parent; and every reign
must have a non-null `end` unless `extant` is true or the row is a currently serving officeholder.

**Violations:** `europe.western.netherlands` — kind `reign`, 1581..null, and the parent of
`europe.western.netherlands.voc`, `...wic-first` and `...wic-second` in `polities.json`. It is a
country. (`south-asia.independence.india-prime-ministers.modi` also has a null `end` and is the
legitimate case: still in office.)

**Status:** `safe` on the no-children half — a person cannot be the parent of a chartered company —
and `advisory` on the null-`end` half, where Modi is the named legitimate exception.

### T11 — `dated_by` must not change between consecutive reigns of the same parent

**Rule:** for each `under` group with ≥4 reigns, all rows must share one `dated_by` value, unless
the differing row also differs in `date_standing` or `bounds` in a way that explains it.

**Violations:** `europe.mediterranean.byzantine` (`unknown` for `anastasius-i` through `basil-ii`,
then `calendar` from `romanos-iv` on); `south-asia.chola` (`unknown` through `rajaraja-i`, `calendar`
from `rajendra-i`); `east-asia.china.song.northern` (`unknown` through `zhenzong`, `calendar` from
`renzong-song`); `east-asia.korea.three-kingdoms` (`unknown` for the Goguryeo kings, `calendar` for
the Baekje and Silla kings); `europe.mediterranean.rome.republic` (`unknown` for
`scipio-africanus`, `calendar` for the ten later figures);
`europe.mediterranean.rome.empire.western-collapse` (`unknown` throughout, `received` for
`romulus-augustulus`); `africa.nile.egypt.early-dynastic.dyn1` and
`africa.nile.egypt.old-kingdom.dyn6` (`unknown` throughout, `received` for `narmer` and `nitocris`).

**Status:** `advisory`. The Egyptian cases are the legitimate exception and show why: Narmer and
Nitocris really are on a different evidential footing from their dynastic neighbours — Nitocris is
Manetho-only — so a per-row difference there is correct. The Byzantine, Chola, Song and Korean cases
are pattern **P4**: an evidential claim flipping at a date threshold rather than at a change in the
evidence, which no historian would produce and which a machine can spot immediately.

### T12 — `dated_by: calendar` requires a dated calendar era attested in the polity's own records

**Rule:** maintain an explicit allowlist of ancestor polities whose records include a dated era
(Roman consular and AUC dating, Egyptian regnal years, Chinese reign eras, Islamic Hijri, Indic
Śaka and Vikrama, Christian AD, Japanese nengō). A reign whose ancestors are all off the list must
use `received` or `unknown`.

**Violations:** `americas.andes.inca.pachacuti`, `...topa`, `...huayna-capac`, `...atahualpa`;
`americas.mesoamerica.aztec.itzcoatl`, `...moctezuma-i`, `...ahuitzotl`, `...moctezuma-ii`;
`africa.west.mali.sundiata`, `...mansa-musa`; `africa.west.songhai.sunni-ali`,
`...askia-muhammad`; `africa.southern.zulu.shaka`; `oceania.polynesia.hawaii.kamehameha-i`,
`...liliuokalani`; `west-asia.mesopotamia.old-babylonian.hammurabi`.

**Status:** `advisory`, because the allowlist is a judgement and edge cases are arguable — the Aztec
dates do rest partly on codices with a genuine 52-year calendar round, and Liliʻuokalani's reign is
documented in an 1890s constitutional monarchy with Gregorian dates, so she is a legitimate
exception. But the Inca, Mali, Songhai and Zulu rows are pattern **P6**: dates from oral tradition
and colonial-era chronicles presented with zero stated uncertainty.

### T13 — A reign must fall inside its parent's span

**Rule:** `parent.start <= reign.start` and `reign.end <= parent.end`, resolving the parent through
`under`.

**Violations:** 19 rows. `east-asia.japan.azuchi-momoyama.nobunaga` (1568 vs parent 1573);
`americas.mesoamerica.aztec.itzcoatl` (1427 vs 1428); `south-asia.rashtrakuta.dantidurga` (735 vs
753); `west-asia.iran.achaemenid.cyrus-ii` (-559 vs -550);
`europe.mediterranean.rome.empire.galba` (68 vs 69); `...carinus` (end 285 vs 284); `...jovian` (end
364 vs 363); `...clodius-albinus` (end 197 vs 193); `...pescennius-niger` (end 194 vs 193);
`...valentinian-iii` (425 vs 455); `east-asia.china.yuan.kublai` (1260 vs 1271);
`europe.eastern.russian-empire.peter-i` (1682 vs 1721); `europe.eastern.soviet.lenin` (1917 vs
1922); `east-asia.korea.three-kingdoms.munmu-of-silla` (end 681 vs 668);
`south-asia.british-raj.mountbatten` (end 1948 vs 1947); `south-asia.independence.gandhi` (1915),
`...jinnah` (1913), `...ambedkar` (1927), `...subhas-bose` (1938), all against a parent starting
1947.

**Status:** `advisory`. The legitimate exceptions are numerous and structural: Kublai ruled from
1260 but proclaimed the Yuan in 1271, Peter I from 1682 but declared the Empire in 1721, Lenin from
1917 but the USSR was constituted in 1922, and Munmu's reign spans the boundary between the Three
Kingdoms and Unified Silla by definition. The independence-movement rows are the finding *Late
Republic / independence figures filed one level too high* — they are not misdated, they are misfiled
under a polity that postdates their activity, which is the same defect in a different guise. Nobunaga
and Cyrus II are worth a human look; the Roman one-year overshoots are period-boundary conventions.
