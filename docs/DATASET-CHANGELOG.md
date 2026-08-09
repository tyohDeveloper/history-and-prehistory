# Changelog

## 0.20.0.0 — A mechanism for names, and the region that needed it most (2026-08-09)

### The mechanism

Three releases of naming work kept hitting the same wall: `aliases` is a flat
list of strings, and a flat list cannot say **why** a name differs, **who** uses
it, **when** it applied, or **whether anyone repudiates it**. That is why the
easy cases got filled in -- Cheops, King Tut, Ozymandias -- while the loaded
ones went bare. There was nowhere to put the reason.

`name_forms` replaces the guesswork with structure. Each form carries a `kind`:

| kind | meaning |
| --- | --- |
| `endonym` | what it called itself |
| `exonym` | an outsiders' name |
| `formal` | official long form |
| `common` | everyday short form |
| `translation` | same referent, another language |
| `scholarly` | a modern academic coinage with no ancient referent |
| `historical` | used only during a stated period |
| `rejected` | actively repudiated by descendant communities |

plus optional `lang`, `from`/`to`, `note`, and `source_ids`.

**`aliases` is now derived from `name_forms` at build time.** Authors write one
thing; search indexes every form regardless of kind. The two cannot drift, which
matters more than it sounds -- drift here means a reader searching "Anasazi"
silently gets nothing.

The readout groups the forms under plain headings -- "Called itself", "Named by
outsiders", "Rejected name" -- because the difference between a name a people
chose and a name imposed on them is content, not metadata about content. A
rejected form renders struck through and still matches search.

### The region that needed it

The Americas was being handled four different ways at once. `Ancestral Puebloan`
had the corrected name and no alias, so **"Anasazi" found nothing**.
`Haudenosaunee (Iroquois)` crammed both names into the display name. `Aztec
Empire` used an alias. `Inca Empire` used `native_name`. One problem, four
strategies, none of them stated.

It also had a sourcing split as clean as any in the dataset:
`americas.prehistory` was **23 of 23 entities cited**, and everything else was
**0 of 45**. Every archaeological site rigorous, every civilization bare.

The naming cases here are unusually sharp:

* **Olmec** is the best-documented misnomer in the dataset. Nahuatl for "rubber
  people", used by the Mexica for their own Gulf Coast contemporaries, borrowed
  by Hermann Beyer in 1929 for a civilization that had ended two thousand years
  earlier. No endonym survives.
* **Anasazi** is Navajo, glossed "enemy ancestors", rejected by Pueblo peoples
  since the early 1990s. The National Park Service states plainly that no one
  knows what these people called themselves; the Hopi term for their own
  ancestors is Hisatsinom.
* **Inca** was the ruler's title, held by perhaps 40,000 people. It now names an
  empire of millions. The polity was Tawantinsuyu.
* **Aztec** is a 19th-century label popularised by Humboldt for what was the
  Excan Tlatoloyan, an alliance of three city-states. Its people were Mexica.
* **Toltec** keeps its dates and gains a `contested-existence` caveat, because
  whether Tula supported a real state or "Toltec" is substantially a Mexica
  retrospective ideal is unresolved.
* **Haudenosaunee** loses its parenthetical, and its founding becomes the
  dispute it is: the archaeological mainstream in the 1450s against Mann and
  Fields' 1142, argued from oral tradition and a solar eclipse -- with the
  published rebuttal recorded rather than omitted.

Seven capitals and sites were added to childless parents: Cahokia, Chaco Canyon,
Tenochtitlan, Monte Alban, Tikal, Machu Picchu and the Qhapaq Nan.

### Tree rings

Rendering Ancestral Puebloan revealed a hole. The dataset had no
`dendrochronology`, so the American Southwest -- where Douglass **invented**
tree-ring dating, and where great houses are dated to the year and sometimes to
the felling season -- was filed under radiocarbon and displayed as "1,100 - 700
BP".

The fix exposed a conceptual error in the frame logic, which chose BP versus
calendar by asking whether a method was "scientific". That is the wrong axis.
Dendrochronology is as scientific as radiocarbon and belongs with the calendar
methods anyway, because its result *is* an absolute calendar year. Chaco now
reads 850-1250 CE.

### Corrections

The Zapotec ended at 800, which is the close of Monte Alban's Classic
florescence rather than of the Zapotec, who persisted to the conquest; extended
to 1521. Moche ended a century early. Tenochtitlan is recorded as predating the
Triple Alliance by a century -- the capital is older than the empire it came to
head.

### Deliberately NOT authored

The **Columbian Exchange and contact-era depopulation**. Estimates run from
roughly 8 million to over 100 million, and the disagreement is methodological
rather than evidentiary. It needs a pass of its own with the competing
estimation methods named, not a number wedged into a summary line.

### Counts

1,633 → 1,640 entities. 494 → 519 sources. 358 → 382 cited. Eight entities now
carry structured `name_forms`. Americas outside prehistory: 0 → 24 sourced.

## 0.19.0.0 — One naming rule, applied twice (2026-08-09)

### Correcting yesterday

0.18.0.0 renamed the Golden Horde to "Ulus of Jochi", on the sound and
well-sourced grounds that the common name is a 16th-century Russian coinage.
The reasoning held. The application did not.

The Byzantine Empire has **precisely the same problem** -- nobody inside it ever
called it Byzantine -- and it was left named "Byzantine Empire" with the endonym
demoted to an alias. Two identical problems given opposite treatments in the
same dataset.

The rename also traded away something worth more than it gained. This is a
reference tool. Hiding the term a reader arrives with defeats the purpose, and
while search still found it, anyone *browsing* Central Asia met a name they had
no reason to recognise.

### The rule, stated once and applied to both

* `name` is the name a reader arrives with. Being findable is the function, not
  a compromise of it.
* `native_name` is what the polity called itself. It renders directly under the
  title, so it cannot be missed.
* `aliases` carry the remaining variants so search catches all of them.
* A sourced `naming-confusion` caveat explains what the common name gets wrong
  and who coined it.

Neutrality does not come from suppressing the exonym. It comes from never
letting the exonym stand alone and unexplained.

So the Golden Horde is the Golden Horde again, now showing **Ulug Ulus** -- its
own name for itself, "Great State", attested in Turkic sources and given by both
the Hermitage and the Kazakh government -- under the title. Byzantium gets the
same treatment for the first time, with Basileia ton Rhomaion.

### A live dispute is not a dead mislabel

`east-asia.china.roc` was published as 1912-1949 with no qualification. Whether
the Republic of China ended in 1949 is one of the most actively contested
questions in international law, and publishing that bare date silently adopts
one side of it.

Three positions are now recorded: the PRC's formal statement that its
proclamation "brought the historical status of the Republic of China to an end";
Taiwan's government portal stating it relocated and has exercised jurisdiction
since; and the academic position that it was a government of the state of China
rather than a state in its own right. Brookings notes Beijing has a vested
interest in its own claim.

This needed a different instrument from the Golden Horde. Byzantium is a
retrospective mislabel of a dead polity where nobody's interests are at stake.
The ROC is a live dispute in which each name is official to someone, so
`naming-confusion` would be wrong -- it implies a mistake to correct.
`contested-existence` and competing dates instead.

The entity's summary had said "continues on Taiwan" all along. The prose knew;
the date did not.

Korea gets the related note: the two states share no word for the nation they
both claim -- Joseon in the North, Hanguk in the South -- and English flattens
both to "Korea", which conceals the disagreement rather than resolving it.

### A Danish scheme applied to the world

Bronze Age and Iron Age carried no sources at all, and the Iron Age no caveats,
while the dataset applies both worldwide. Thomsen devised the scheme in 1837 for
northern European material. Connah's verdict on exporting it is quoted directly:
applying it to African archaeology "produced little more than confusion, whereas
in the Americas or Australasia it has been irrelevant".

### What visual review caught

A duplicate. The Golden Horde displayed two near-identical naming caveats,
because this module *reworded* one a previous pass had written and the dedup
matched on exact text. Repeated caveat kinds are legitimate -- Ban Chiang
carries two genuinely distinct misconceptions -- so the new test compares
opening text rather than banning the kind, and superseding is now opt-in.

### Counts

1,633 entities unchanged; this pass corrected rather than added. 481 → 494
sources. 353 → 358 cited. 325 → 329 native names. Twelve `naming-confusion`
caveats → sixteen.

## 0.18.0.0 — A naming rule, and the empire that was missing (2026-08-09)

### The naming rule, stated for the first time

The dataset already had two mechanisms for names and had been applying them to
the wrong half of the problem. `aliases` renders as "Also known as" and makes an
entity findable. A `naming-confusion` caveat renders under "Worth knowing",
carries sources, and explains why a name misleads.

Between them they cover the ground. But they had been used for the *harmless*
cases — Cheops, King Tut, Ozymandias, Near East — and skipped on the loaded
ones. The Golden Horde had neither, despite "Golden Horde" being a documented
16th-century Russian coinage that the polity never used for itself.

The rule from here: **file under the name the polity used where one is
recoverable, keep the common name as an alias so search still works, and when
the common name embeds somebody's later claim, say so in a caveat with a
source.** Findability and truth are different jobs and there is already a field
for each.

Applied to the Ulus of Jochi, which is now its name. Searching "Golden Horde"
still finds it. Its founding, previously the bare fact 1240, is now `disputed`
with four sourced positions — the grant of the ulus in 1224/25, the western
campaign of 1236-40, the conventional 1240s, and c. 1260, which is where the
Cambridge History of the Mongol Empire starts it.

Not yet applied to the caliphates, the PRC and ROC, or Korea. Those need it.

### The British Empire did not exist here

England ran to the Stuarts and then jumped to the Victorian era. No Act of
Union, no empire, and nothing at all after 1901.

It is added with both ends held open, because neither is a fact. The start is a
**definitional fork rather than a dispute**: nobody disagrees about what
happened in 1497, 1583 or 1607, only about which one counts. That is a different
species of uncertainty from a contested radiocarbon date and the entity says so
in as many words. The end has four live positions — 1947, 1956, 1960, 1997 —
with named proponents and no winner.

The First/Second Empire split is recorded as **contested**, not as settled
periodisation: standard in Britannica and the tertiary literature, rejected by
Marshall and by Cambridge specialists who argue the two overlapped and the break
is artificial. Pre-1707 activity is flagged as English rather than British.

### An identifier that contradicted its own dates

`southeast-asia.maritime.dutch-eic` covers 1800-1949. The Dutch East India
Company's charter lapsed on 31 December 1799, so that period is by definition
*not* company rule — it is the state colony. The entity now says so, and carries
1945 as an alternative end, since Indonesia dates independence from the
proclamation and 1949 is only when the Netherlands agreed.

### Iberia, sourced

Spain's 1898 is now scoped to the empire it actually ends — the American and
Pacific one — with the 1975-76 withdrawal from the Western Sahara as the later
terminus. Portugal's 1415-1999 is confirmed rather than changed: 584 years, and
unusually for an empire of that size, both ends are largely uncontested.

The Cross-Regional Empires category now carries a scholarly warrant rather than
a filing rationale. Burbank and Cooper treat the caliphates, the Mongol empire
and the European maritime empires as comparable, and the Oxford World History of
Empire frames that comparison as a corrective to older single-region history.

### What the tests caught

Three failures, two of them substantive. The duplicate-alternative test rejected
the new competing dates because they described years in prose without setting
the year fields — so the app could not have rendered them comparably. The
split-dating-method catalogue caught the Ulus of Jochi and prompted a rethink:
`typological` was wrong, because the disagreement is about which event counts as
a beginning, not about how any candidate date was derived. Both ends are
calendar dates from written sources; the fork lives in `date_precision`.

### Deliberately NOT authored

The **VOC**, the **Dutch West India Company** and the **French colonial
empire**. The first two have no sensible parent: there is no Netherlands node in
the dataset at all, and filing a company that operated from the Cape to Nagasaki
under "Maritime Southeast Asia" would be worse than omitting it. That is a gap
to fix with a Netherlands node, not a place to wedge an entity. The WIC also
needs splitting into two charters, 1621-1674 and c. 1675-1791/92, with sources
differing on the final year.

### Counts

1,631 → 1,633 entities. 461 → 481 sources. 346 → 353 cited. Nine
`naming-confusion` caveats → twelve.

## 0.17.0.0 — Citations for Greece and Rome, and what the Mesolithic actually is (2026-08-08)

Two jobs. Neither added much, and both fixed things that were wrong.

### The rigour was inverted

616 entities displayed a date with no source behind them, and the worst were
the most famous. Namazga — a Turkmen pottery sequence almost nobody will look
up — had three sources, a dagger in the picker, and a caveat about Soviet
typology. The Roman Republic had nothing. Everything authored under the
sourcing rule was scrupulous; everything older was bare, and that is precisely
the material a visitor opens first.

This is the first tranche: the seventeen foundational Mediterranean entities.

**Two dates were simply wrong.**

Greece started at **3000 BCE**. The British Museum, Cambridge and Smarthistory
all put the start of the Greek Bronze Age at about **3200**. The dataset was
carrying a rounding as a fact, two centuries out.

Macedon started at **808 BCE** — a king-list back-calculation to Karanos, a
founder Herodotus does not even name. Britannica, the Oxford Companion and the
Lexicon of Argead Macedonia all date the attested kingdom to about **700 BCE**
under Perdiccas I. Corrected, with the legend retained as a `traditional`
alternative on a `received` dating method. It is the same error as Rome's 753
and it had been sitting one row away from it for the entire life of the project.

**Four conventions are now labelled as conventions.** Rome's 753 is Varro's
back-calculation, which the Oxford Classical Dictionary calls "artificial
manipulation" that "does not accord with any archaeological starting point";
ancient authors proposed at least six years, from 841 to 728 BCE. The Republic's
509 is Varronian too. 476 CE is Gibbon's marker — a UCL thesis says flatly "476
is not the year in which the empire ended, and never was", Gibbon's own footnote
conceded it was "not positively ascertained", and Britannica declines to give a
year. Byzantium's 330 is one of at least six live conventions, and the Oxford
Dictionary of Byzantium avoids the word entirely before the 7th century.

One label rather than a date is flagged: "Crisis of the Third Century" asserts a
coherent systemic collapse that Lewitt, Witschel and others reject.

The effect is that all the epistemic machinery built since 3.6.0.0 — the dagger,
the received-convention banner, the split start/end dating methods, the
competing-dates block — now fires on the entity people are most likely to open.

### The Mesolithic was empty for the right reason

`global.mesolithic` had been the widest childless era for six passes and I
deferred it every time. The content was never missing: Maglemose, Kongemose,
Ertebolle, Star Carr, the Azilian and the Sauveterrian all already existed under
European prehistory, which is where the term has content.

What is actually disputed is the **global category**. Africa uses Later Stone
Age, the Americas use Archaic, Southwest Asia uses Epipalaeolithic. Czarnik
called the Mesolithic a negative category, defined by being neither Palaeolithic
nor Neolithic. Elliott and Warren, writing in 2023 against Graeber and Wengrow's
worldwide "Mesolithic", argue that exporting the label pegs the rest of the
world to a northern European developmental stage.

So the node is not filled with children. It is reframed as the argument, with
`standing: minority`, a `contested-existence` caveat, and the regional
alternatives named in its date note. A test now requires it to name them.

A satisfying consequence: `coverage.py` already skips eras that have caveats and
no children, on the grounds that they are concepts rather than empty containers.
Giving this node its caveats made it drop off the gap report by itself, under a
rule written three passes earlier.

Also added: Muge, the Obanian, and the 8.2 kiloyear event, plus better dates for
the three Scandinavian cultures from Allentoft et al.'s 2024 Bayesian model over
81 radiocarbon dates. The 8.2 ka entity records that the ice core dates the
event far more precisely than any archaeological response being matched to it,
and that western Scotland collapsed while Atlantic Iberia grew.

### Deliberately NOT authored, for the second time

The **Tardenoisian**. A previous pass declined it because sources disagreed by
3,000 years and mixed calibrated with uncalibrated figures. This pass confirms
Thevenin and Rozoy still disagree with no calibration status stated on either
side. Two passes have now reached the same answer, recorded here so a third does
not have to repeat the work.

### Counts

1,628 → 1,631 entities, which understates the pass: 20 existing entities were
corrected or sourced rather than added. 424 → 461 sources. 325 → 346 cited.
Foundational entities still without a source: 179 → 162.

## 0.16.0.0 — Pre-Islamic Arabia and Predynastic Egypt (2026-08-08)

Twenty entities across the two remaining large gaps flagged by the childless
report, and one rendering bug that only twenty entities could have exposed.

### Egypt: how fast a state can appear

`africa.nile.egypt.predynastic` held 6000–3100 BCE with no children, so the
dataset had Narmer but nothing he came out of. It now has the Badarian, Naqada
I, II and III, Hierakonpolis, tomb U-j, Dynasty 0, and the Lower Egyptian
sequence of Merimde, el-Omari and Maadi-Buto.

The organising entity is **the speed of state formation**. Dee et al.'s 2013
Bayesian model over 186 radiocarbon dates compressed the whole run from
pre-state to unified state into roughly **600–700 years**, against about
**4,000–5,000** for the same journey in Southwest Asia. The dataset can now
show both ends of that comparison, because the Uruk period was authored one
release earlier. At its finest resolution the model puts the assimilation of
Upper and Lower Egyptian funerary practice at five or six generations.

That model also moved dates: the Badarian ended two to three centuries later
than typological estimates had it. Where a museum round number disagrees with a
modelled radiocarbon range here, the range wins and the round number is
recorded as a conversion of Petrie's relative seriation, which is what it is.

**The Narmer Palette is authored as iconography, not as a record of conquest.**
Scholarship is genuinely split, Tell el-Farkha shows no invasion layer, and the
Lower Egyptian material culture had already been absorbed gradually, centuries
earlier. The palette proves a kingship ideology existed by about 3100 BC. It
does not date a unification or show that unification was an event.

Already in the dataset and therefore not re-authored: the Green Sahara, Nabta
Playa with its three sub-phases, and the Fayum Neolithic. Checked first this
time, which the East Asia pass had to learn the hard way.

### Arabia: Dilmun, Saba, the Nabataeans, and the camel

`west-asia.arabia.pre-islamic` held three and a half millennia with no
children. It now has Dilmun, Umm an-Nar, Wadi Suq, Saba, the Marib Dam, the
Nabataeans, camel domestication and the incense route.

Two of those are worth more than their subject.

**The Marib Dam is physical evidence contradicting a story everyone knows.**
Its collapse is remembered as the Sayl al-'Arim, conventionally 570 CE. AMS
dating of charcoal in the basin silts puts the dam's final activity between
roughly 1 CE and the end of the third century — three hundred years earlier.
Both ship; neither is resolved. It is also the dataset's first entity whose
START is textual and whose END is scientific, which is the reverse of the usual
direction and is now pinned by a test.

**Camel domestication carries a documented correction.** Timna Site 30's bones
were long cited for domestication by the 13th century BCE. They belong to the
site's last occupation phase, not its Late Bronze Age layers; OxA-2165 at
2650 +/- 90 BP calibrates to 969–600 BCE. Not a bad measurement — a good
measurement attached to the wrong layer.

South Arabian dates ship under the **Long Chronology** and say so, because
after the Hammurabi fix in 0.15.0.0 an unlabelled scheme-dependent date is not
acceptable anywhere in this dataset.

### Deliberately NOT authored

**Magan**, the copper source that supplied Mesopotamia, because every date
found for it traces to Wikipedia. **Himyar**, because the research marked its
dates search-located and never confirmed by fetching; the convergence on 110
BCE is probably right, and probably right is not the standard. And no single
Merimde range, because published radiocarbon for that site varies by five
hundred years across research groups — it ships wide and says why.

### Counts

1,608 → 1,628 entities. 396 → 424 sources. 305 → 325 cited. 318 → 338 with a
start dating method, 252 → 271 with an end one.

## 0.15.0.0 — Uruk, Elam, Anatolia, and Hammurabi's missing frame (2026-08-08)

Twenty-five entities, and one long-standing bug fixed.

### The bug: a chronology quoted as a fact

Hammurabi has shipped since the beginning as 1792–1750 BCE with no note, no
standing, and no source. Those are **Middle Chronology** dates. Three rival
schemes are in active use and they move the same reign across a spread of about
120 years, taking the entire 2nd-millennium Mesopotamian sequence with them.
There is no independent dating underneath: it rests on king-lists anchored to
the Venus Tablet of Ammi-saduqa, whose observations are astronomically periodic
and therefore fit several real years equally well.

This is the Monte Verde failure class exactly — a number quoted without the
frame that produced it — and it was sitting on one of the most recognisable
dates in the dataset. Hammurabi and the Old Babylonian era now carry the frame,
and a test forbids any chronology-dependent date from omitting it. The same
treatment is applied to the sack of Babylon, whose six proposed dates span 237
years.

### Anatolia was an empty region

`west-asia.anatolia` existed as a node containing nothing. No Hittites, no
Troy, no Lydia, no Urartu. It now has the Hittites (Old Kingdom, Hattusa,
Kadesh, the collapse, and the Neo-Hittite successor states with their
Assyrian-recorded annexation dates), Mitanni, Urartu, Phrygia, Lydia, the
invention of coinage, and Troy.

Two things worth pulling out. The **Hattusa "sack" never happened** as usually
told — German Archaeological Institute evidence does not support violent
destruction, and the buildings were deliberately emptied first. And the
**collapse drought is dated far more precisely than the collapse**: tree rings
and carbon isotopes give 1198–1196 BCE, three named years, against a political
record that manages "first quarter of the 12th century".

### The Uruk period, which was entirely absent

The dataset went from Ubaid straight to the Early Dynastic at 2900 BCE,
skipping the first cities and the invention of writing. The container era was
already there, describing itself as "the sequence that ends with the first
cities and the first writing", and holding nothing.

Now: the Uruk period, the city, the Uruk expansion, proto-cuneiform, and Jemdet
Nasr.

Chronology is authored from ARCANE's calibrated radiocarbon rather than the
round numbers, with the four competing frameworks named and not averaged.
ARCANE also notes that the widely quoted early figures for Uruk IVa rest on
uncalibrated readings — the same error this dataset made with Monte Verde,
found here in the published literature.

Uruk's size is left at CDLI's 100 hectares. Figures from 250 to 600 ha
circulate; only CDLI's traces to an institution. No population figure is
authored at all, because none of the widely repeated ones trace to anything.

The **token hypothesis is not authored as the origin of writing**. It is the
popular account and it is under specific statistical attack: Zimansky showed
that only 18% of claimed token subtypes have more than four members and that
the "sheep" token has fifteen attestations in total. It ships as a contested
alternative, with a second caveat noting tokens were never replaced by writing
at all — they continue alongside it into the 1st millennium BC.

### Elam subdivided

Proto-Elamite, Linear Elamite, Old, Middle and Neo-Elamite, Chogha Zanbil, and
Susa. Proto-Elamite's date note records a limit worth knowing: precision beyond
"3300–2900" is not achievable because the relevant dates sit on a plateau in
the calibration curve. That is a physical constraint, not a shortage of samples.

The 2022 Linear Elamite decipherment ships as a claim with qualified
acceptance, alongside Dahl's counter-model that the script was deliberately
archaised rather than inherited.

### Deliberately NOT authored

Eridu (founding date untraceable to the excavation report); the Hittite Middle
Kingdom (the literature calls it an ill-defined dark age and declines to bound
it, so this does too); Urartu's collapse date; and **all of pre-Islamic
Arabia** — Dilmun, Saba, the Nabataeans, the Marib Dam — whose research is
archived in `docs/anatolia-arabia-research.md` and is the obvious next pass.

### Counts

1,583 → 1,608 entities. 366 → 396 sources. 278 → 305 cited. 292 → 318 with a
start dating method, 229 → 252 with an end one.

## 0.14.0.0 — Erlitou, Korean prehistory, and the Chinese Neolithic filled in (2026-08-08)

Twenty entities. This pass started from a false positive and is more useful for
having done so.

### The gap report was wrong, and the tool is fixed

`east-asia.prehistory` was named the dataset's biggest hole: 13,700 years, no
children. It is a navigation era. Its own summary says Jomon and the Chinese
Neolithic "also sit in their own national sequences, where they belong" — and
they did, Jomon in six subdivided phases under Japan and six cultures under
China. A research pass went out to fill a gap that was not there.

What the CORRECTED report showed was three real gaps of quite different shape:

- **Korea had no prehistory at all.** Eight children under `east-asia.korea`,
  every one of them a state, the earliest Gojoseon at 2333 BCE. No Chulmun, no
  Mumun, no arrival of millet or rice. An entire peninsula began in the Bronze
  Age.
- **`east-asia.china.legendary` was childless across 3,400 years** — the node
  that carries the Xia — while Erlitou, the site the Xia argument is actually
  about, was not in the dataset at all.
- The Chinese Neolithic had six cultures and was missing most of the rest.

### Added — Erlitou and the Xia question

Parented under `legendary`, deliberately, so the evidence sits next to the
tradition rather than in a separate wing of the tree.

The identification is not adjudicated. Most Chinese scholars read Erlitou as
Xia; most overseas scholars hold it cannot be confirmed without contemporaneous
writing; a middle position prefers "the Erlitou State". All three ship, with
their standings, and the dataset picks no winner.

Worth noting that the empirical driver here is not ideology but re-dating.
Erlitou's span has moved later and narrower across at least three episodes —
from 2100–1300 BC on early radiocarbon, to 1880–1520 from the Chronology
Project, to roughly 1750–1520 on wiggle-matching — travelling from a
comfortable fit with textual Xia dates toward a range that begins near the
traditional END of Xia. Erlitou is authored with
`allow_outside_parent_dates` because it outlasts the legendary era, which is
the dispute rather than an error.

### Added — Korea

Chulmun and Mumun as eras, plus the arrival of millet (earliest secure direct
AMS date on a grain, 3640–3370 cal BC) and of rice. The rice entry carries a
clean demonstration of why calibration must be stated: the SAME Oun-1 grain
samples are published as 2860–1320 cal BC by one treatment and 1950–1000 cal BC
by another.

### Added — China and Japan

Cishan, Xinglongwa, Dawenkou, Hemudu, Daxi, Shijiahe and Qijia. The Liangzhu
hydraulic system as a child of the existing Liangzhu entity — the dams were
built BEFORE most of the walled city. A new `late-pleistocene` era, because
terminal-Pleistocene pottery does not belong under an era called Neolithic:
Tianyuan Cave, Xianrendong and Yuchanyan.

Xianrendong's famous 20,000 cal BP pottery ships as `minority` with a
misconception caveat. The Science paper is peer-reviewed and so are both
re-analyses disputing it. Yuchanyan, which an earlier pass declined to author
because sources conflicted, is authored now on the dedicated 2009 PNAS study,
with the older lab results carried as `superseded`.

For Japan: Sannai Maruyama, the Late Jomon population decline, and the 2003
Yayoi redating controversy as an event carrying four competing start dates from
the 10th to the 5th century BCE. It starts before its own parent period, which
is the entire point.

### A test caught a misuse of `alternatives`

Erlitou was first authored with two interpretive alternatives — "is Xia" and
"the Erlitou State" — and the duplicate-alternative test added in 0.10.0.0
rejected it. The test keys on `standing|start_year|end_year`, and two undated
minority alternatives are indistinguishable under that key. It was right to:
`alternatives` is a DATE structure, and to a reader two undated entries at the
same standing read as the same claim asserted twice. The middle position moved
into `date_note`.

### Counts

1,563 → 1,583 entities. 331 → 366 sources. 258 → 278 cited. 272 → 292 with a
start dating method, 209 → 229 with an end one.

## 0.13.0.0 — The Indus subdivided, and the Southern Neolithic (2026-08-08)

`south-asia.indus` held 3300–1300 BCE as a single entity with no children. Seventeen
entities now fill it in, and a second South Asian Neolithic joins the dataset.

### Added — the Indus Civilisation

Three phases (Kot Dijian, Mature, Late) on the Harappa test-trench sequence,
which rests on more than seventy radiocarbon dates at the type site and is where
the familiar 2600–1900 BCE bracket actually comes from. Five sites: Harappa,
Mohenjo-daro, Dholavira, Lothal, Rakhigarhi. Then the Indus script, the
deurbanisation, and the Ghaggar-Hakra question.

**The Rakhigarhi genome** is authored as an event in its own right. One woman,
I6113, the only one of 61 skeletal samples to yield usable DNA, with no steppe
and no Anatolian farmer ancestry — and a misconception caveat, because the
result was widely reported as disproving Indo-Aryan migration and does not. Its
companion, **the arrival of steppe ancestry** at roughly 1900–1500 BCE, is
authored separately. Both findings are correct and mutually consistent; the
tension is entirely between the papers and the coverage of them.

Note what the genome entity's date note says: five attempts to directly date the
individual failed on carbon-to-nitrogen ratio. She is dated by seven charcoal
samples from the habitation area. There is no calibrated date for the woman
herself, and the dataset says so rather than quietly borrowing the context date.

### Added — the Southern Neolithic

A genuinely separate centre in the South Deccan that the dataset had nothing on:
the era, the ashmounds (mounds of burnt cattle dung, formed in under two
centuries between 1950 and 1750 BC), and the indigenous domestication of
browntop and foxtail millet with mung bean and horsegram. Plus Burzahom in
Kashmir.

### A 1964 paper is not a live dispute

The research returned Agrawal's 550-year Harappan span, 2300–1750 BC, as a
competing modern chronology. It is *Science* 143(3609), 28 February 1964 —
uncalibrated radiocarbon published three years before Suess released the first
calibration curve, which is exactly why it runs short. It ships as
`superseded`, not as an alternative of equal footing, and a test enforces that.
It is kept rather than dropped because the figure still circulates and a reader
who meets it is owed the explanation.

This is the Monte Verde failure class again: a date in a frame that misleads
when lifted out of it.

### Deliberately NOT authored

**Kalibangan** has real published dates, but this pass could only reach them
through an exam-cramming site and a course handout. **Ganweriwala** is barely
excavated and its one circulating date traces to Wikipedia. **Ochre Coloured
Pottery** and **Painted Grey Ware** have genuinely scattered chronologies —
PGW proposals span 2600 to 1200 BCE and the disagreement is partly
methodological, Libby versus Cambridge half-lives, which is not something a
midpoint can fix.

The **2026 Mohenjo-daro re-dating** IS included, but as an `alternative` with
`minority` standing, because it currently rests on press reporting of a
technical briefing rather than a published paper.

### A schema gap, recorded not papered over

Four caveats wanted kinds the schema does not have — `method` (this figure is
uncalibrated), `sourcing` (this rests on a press report), `dispute` (still
open), `scope` (one sample cannot carry this claim). The enum offers only
`misconception`, `naming-confusion` and `contested-existence`. Rather than
mislabel them, their text moved into `date_note`, which is uncapped and
rendered. The gap is real and is written down here, which is how `received`
started in 0.12.0.0.

### Counts

1,546 → 1,563 entities. 308 → 331 sources. 241 → 258 cited entities. 255 → 272
with a start dating method, 192 → 209 with an end one.

## 0.12.0.0 — The `received` dating method (schema 3.1.0) (2026-08-08)

0.11.0.0 recorded a schema gap rather than papering over it: `dating_method` had
no value for a date arrived at by transmission. Rome's 753 BCE comes from the
annalists, Narmer's 3100 from king-lists, the Namazga brackets from Masson's
ceramic typology. Calling any of them `typological` would have described someone
actively dating material by its style, and `unknown` would have claimed the
provenance was lost — when in fact it is perfectly well known. It just is not
evidence.

### Added — `received`

Schema 3.1.0 adds `received` to the dating-method enum, on all three fields that
carry one. Nine entities now use it: Rome's Kingdom, Gojoseon, Gilgamesh, David,
Solomon, Narmer, Nitocris, the Namazga Sequence and Altyn-Depe.

It is deliberately distinct from its two neighbours. `typological` is an active
method — someone is dating material by its style now. `unknown` means the
provenance is lost. `received` means the provenance is known and is a chain of
transmission rather than a measurement.

`received` also joins `CALENDAR_METHODS`, so the app does not report a handed-
down date as scientifically dated.

### Why the enum grew rather than the guard relaxing

The 0.11.0.0 test for `standing: "traditional"` could only check the precision
field, with a comment explaining that requiring a method was impossible. That
clause is now enforced: a traditional standing requires `date_precision:
"traditional"` AND `start_dating_method: "received"`. The loophole closes.

### Counts

1,546 entities unchanged. 248 → 255 with a start dating method, 185 → 192 with
an end one. Schema 3.0.0 → 3.1.0.

## 0.11.0.0 — Received conventions (2026-08-08)

0.10.0.0 left the Namazga sequence out because its phase brackets trace to
Soviet-era ceramic typology rather than to any published radiocarbon table.
That was right on the sourcing rule and wrong on the outcome: Namazga organises
every account of Central Asian prehistory, and a reader who looks it up and
finds nothing learns less than one who finds it clearly labelled.

This release adds it under `standing: "traditional"` — and that is only
defensible because the app now leads with the label rather than burying it. A
dagger marks the range in the picker gutter and a banner sits above the summary
in the readout. Without that, adding unsourced brackets would just have been a
quiet dilution of the rule.

### Added

- **Namazga Sequence**, 4800-1500 BCE, `traditional`. The date note carries all
  six phase brackets, the competing sets, and the reason not to trust any of
  them: modern reassessments compress Namazga V into 2400-1950 or 2250-1700
  BCE, and one report gives C14 dates for a single final Namazga VI layer
  scattering from 1884 to 818 BC.
- **Altyn-Depe**, 2100-1650 BCE, `traditional`. Dated by its Namazga V pottery,
  so it inherits that sequence's problem entirely.
- **Kelteminar**, 6000-3000 BCE — deliberately NOT traditional. A peer-reviewed
  source does give it a millennium-scale range, so it is a thinly sourced
  minority claim rather than a convention. The distinction is the point.

### Changed

Seven entities that were already received conventions but declared it only
through `date_precision` now carry `standing: "traditional"` as well: Rome's
Kingdom, Gojoseon, Gilgamesh, David, Solomon, Narmer and Nitocris. Romulus
Augustulus is deliberately excluded — his deposition in 476 is attested, and the
`traditional` precision there marks the "fall of Rome" convention rather than a
legendary date for the man.

### A schema gap, recorded not papered over

`dating_method` has no value for "arrived at by ancient tradition". Rome's 753
BCE comes from the annalists and Narmer's 3100 from king-lists; calling either
`typological` would misdescribe it, so those entities have no dating method and
the guard test explicitly does not require one.

### Counts

1,543 → 1,546 entities. 238 → 241 cited. 307 → 308 sources. Schema unchanged at
3.0.0.

## 0.10.0.0 — Central Asia, the Austronesian expansion, Oceania (2026-08-08)

The three thinnest regions. `tools/coverage.py` found Central Asia with nothing
at all between 10,000 and 3,700 BCE, Southeast Asia almost nothing before 1,600
BCE, and Oceania nothing whatever between 10,000 and 1,500 BCE — the largest
maritime migration in human prehistory was simply missing. Research in
`docs/centralasia-research.md` and `docs/seasia-oceania-research.md`.

### Added — Central Asia (9 entities)

Jeitun, Anau, Sarazm, the Inner Asian Mountain Corridor with Begash and Tasbas
beneath it, Gonur Depe, Seima-Turbino, and the Tarim Basin mummies.

The organising finding is that crops crossed Asia in the hands of herders, not
farmers: wheat and barley east, broomcorn millet west, carried by transhumant
pastoralists who at Begash were feeding the millet to their sheep. It happened
before any steppe-ancestry population reached the region, which rules out the
obvious alternative.

Two genuine reversals are recorded. **Seima-Turbino** moved 500-700 years older
under AMS dating, from Late to Middle Bronze Age; three chronologies are carried
side by side rather than reconciled. **The Tarim mummies** carry no Afanasievo,
Oxus or corridor ancestry at all — a local population that borrowed its
neighbours' wheat and dairying rather than importing them, which is the reverse
of every previous hypothesis.

### Added — Southeast Asia and Oceania (15 entities)

The Austronesian Expansion as a spine, with Dabenkeng, the arrival of pottery in
Island Southeast Asia, and the settlement of the Marianas beneath it. Da But,
Man Bac, Khok Phanom Di, Ban Non Wat, Non Nok Tha, the Neolithic migration into
Southeast Asia, and the Toalean culture. For Oceania: the Bismarck obsidian
network, Torres Strait settlement, the arrival of the dingo, and Australian
mid-Holocene intensification.

The expansion is authored for what it contradicts. It stalled — centuries
between the Philippines and the Marianas, more before Lapita. The domesticates
did not travel as a set: pigs reach northern Luzon two thousand years before
dogs. Pottery appears in Borneo and the northern Philippines at the same time
rather than in sequence. And the Bismarck obsidian network shows Near Oceania
had been trading across open water for seventeen thousand years before Lapita
voyagers arrived.

### Changed

**Ban Chiang** gains the controversy it is famous for and did not carry: a 1976
claim of the world's earliest bronze at 3600 BC, abandoned in 1982, and a
long-versus-short chronology dispute a 2022 review still calls only "close to
resolution". **Lapita** gains the unresolved 3550-3200 cal BP range for its own
beginning.

### Not added

Three Central Asian entities were researched and deliberately left out, for
different reasons. **Kelteminar** has no fetched primary radiocarbon dataset at
all. **Altyn-Depe** has no independent modern dating and inherits the Namazga
uncertainty. **The Namazga I-VI sequence** is the awkward one: it is the standard
framework for the whole region and its phase brackets are quoted everywhere, but
essentially all of them trace to Soviet-era typology rather than to a published
radiocarbon table — Hiebert found C14 dates for a single Namazga VI layer
spanning 1884 to 818 BC. Authoring it would mean importing a chronology the
sources cannot support.

Rock art in Island Southeast Asia is likewise absent: dating claims were
plentiful in search results and thin in fetched primary sources.

### Counts

1,519 → 1,543 entities. 214 → 238 cited. 261 → 307 sources. Schema unchanged at
3.0.0.

## 0.9.0.0 — European Mesolithic and Holocene Americas (2026-08-08)

Two coverage passes aimed by `tools/coverage.py`, which found Europe holding
five non-reign entities for the whole of 10,000-3,000 BCE — and nothing at all
between 10,000 and 5,500 — and the Americas holding one 9,000-year "Archaic
Period" for everything between the Paleoindians and Norte Chico. Research in
`docs/europe-research.md` and `docs/americas-research.md`.

### Fixed — a cal BP figure stored as a BCE year

`global.paleolithic.monte-verde` held `-14500..-14000`, and its Surovell
alternative `-8200..-4200`. Both were cal BP figures written straight into the
calendar-year field, putting the site **1,950 years too early** and the rival
claim 2,250 years too early. 14,500 cal BP is 12,551 BCE.

Found by accident: the Americas pass authored a second Monte Verde using the
`bp()` helper, and the two disagreed by two millennia. A dataset-wide audit for
the same pattern turned up no other instances. Both a units regression test and
a "there is exactly one Monte Verde" test now guard it.

### Added — Europe, 10,000-2,500 BCE (24 entities)

Mesolithic: Azilian, Maglemosian, Sauveterrian, Kongemose, Ertebolle, Star Carr,
Lepenski Vir, the drowning of Doggerland, the Storegga tsunami.

Farming's arrival: Franchthi Cave, Sesklo, Starcevo-Koros-Cris, Cardial and
Impressed Ware, Vinca, Michelsberg, Varna, Cucuteni-Trypillia with its
mega-sites, Funnelbeaker, Newgrange, Skara Brae, Ness of Brodgar.

Two synthesis entities carry findings that do not belong buried in a note on
someone's pottery: **The Two Routes of Neolithic Spread** (inland 50 km per
generation, coastal 70, same interbreeding rate, different outcomes at the far
ends) and **The Anatolian Farmer Turnover** (70-100% replacement of local
forager ancestry between 6500 and 4000 BCE), plus **The Steppe Ancestry Influx**
at 3000-2900 BCE.

Nearly everything here has been re-dated recently and usually later. Varna moved
~200 years younger under AMS; Thessaly's Neolithic start moved from 7000 to
6700-6500 cal BC; Lepenski Vir gained a 700-year occupation hiatus its original
stratigraphy lacked; Skara Brae turned out not to be continuously occupied. Each
older figure is carried as a `superseded` alternative rather than dropped.

### Added — Holocene Americas (15 entities)

Cooper's Ferry, the Western Stemmed Tradition, the megafaunal extinction, Watson
Brake, Poverty Point, the Chinchorro, Las Vegas culture, Valdivia, Huaca Prieta,
Caballo Muerto, Cerro Sechin, the Old Copper Complex, Taperinha, and an
**Artificial Mummification** threshold.

Chosen for what they overturn: Great Lakes copper working starts c. 9,500 years
ago, older than most Old World metallurgy; Chilean mummification predates
Egypt's by two millennia; the hemisphere's oldest pottery is Amazonian, not
Andean; Watson Brake's mounds were raised by hunter-gatherers with no
agriculture.

**Cerro Sechin is authored as a warning rather than a date.** Its widely
repeated 7600 BCE occupation could not be confirmed against the Peruvian
Ministry of Culture's own excavation report, whose oldest AMS date is 1887-1689
cal BC and which has no dates at all for Sechin Bajo. The entity records what
the primary source contains and says the popular figure is unverified — not that
it is wrong.

### Changed

White Sands gains the two rounds it was missing: the 2025 mud dates (a third
independent material, second lab) and the 2024 critique arguing for a
significantly younger chronology. They cut in opposite directions and both are
recorded.

### Not added

`n.a.` in research and deliberately absent: the Tardenoisian (sources disagree
by up to 3,000 years and mix calibrated with uncalibrated figures), a
pan-European Sauveterrian range, a sharp Azilian end date, Beringian Standstill
durations, and Caverna da Pedra Pintada.

One citation error from the research pass was caught during authoring: the
Storegga tsunami paper had been given the DOI of the Fort & Perez-Losada
interbreeding paper. Corrected in both the dataset and the archived research.

### Counts

1,480 → 1,519 entities. 175 → 214 cited. 203 → 261 sources. Schema unchanged at
3.0.0.

## 0.8.0.0 — The Neolithic transition (2026-08-08)

Aimed by `tools/coverage.py`, which found "Agricultural Revolution" holding
5,500 years with zero children — the most consequential transition in scope
stored as one undifferentiated block. Research in `docs/neolithic-research.md`
(62 sources).

### Changed — "Agricultural Revolution" was wrong twice over

The node was an `event` named after a model the field has abandoned. Both are
now corrected; the id `global.neolithic.agricultural-revolution` is unchanged,
so nothing addressing it breaks.

- `kind` event → era. A 4,000-year process is not "a discrete moment".
- Named **Neolithic Transition**. The dominant model is protracted, multi-focus
  and largely unconscious rather than invented, and the field has largely
  replaced Childe's "revolution" for that reason. The old names stay as
  aliases, because that is what readers arrive holding.
- `end_year` -4500 → -1800. The end is diachronous and outlasts the Neolithic
  label itself, because Eastern North America domesticates thousands of years
  after the Fertile Crescent.
- Carries the dissent rather than erasing it: Abbo and Gopher's rapid,
  conscious, core-area model is recorded as a live minority position, with the
  published exchange cited.
- Caveat that "how many independent centres exist" is unsettled — Harlan
  counted 6, Vavilov 12, Purugganan and Fuller 24.

### Added — eight independent centres

Fertile Crescent, Yangtze Valley, Yellow River Basin, Mesoamerica, Andes, New
Guinea Highlands, Eastern North America, Southwest Amazonia.

- Yangtze carries the 2024 *Science* trajectory (exploitation 24,000 BP,
  domestication 11,000 BP) as a minority alternative to the Shangshan
  consensus, rather than replacing it.
- Yellow River is marked `disputed`: phytolith dates at Cishan reach 10,300 cal
  BP while macrobotanical remains from the same sites are as late as 5,900 cal
  BC. Both are recorded; neither is silently picked.
- Mesoamerican maize keeps its two figures apart — starch and phytoliths at
  8,700 cal BP versus direct AMS cobs at 6,250 cal BP — because they rest on
  different evidence and averaging them would be false precision.

### Added — eleven behavioural firsts

The firsts layer previously stopped at African cereals. The additions were
chosen for what they contradict as much as for what they record.

- **Pottery** (Xianrendong, 20,000 cal BP) predates farming in the same region
  by over ten millennia. Ceramics are not a marker of agriculture or sedentism.
- **Domestic dog** (15,800 years ago) and **fermented drink** (Raqefet, 13,700
  cal BP) are both Palaeolithic and both pre-agricultural.
- **Horse domestication** is dated to the Volga-Don DOM2 lineage at 2200 BCE.
  Botai, c. 3500 BC, is recorded as `superseded`: it remains the earliest known
  husbandry but is a genetic dead end, and conflating the two is the usual
  error in older secondary sources.
- **Domestic chicken** (Ban Non Wat, Thailand, 1650 BCE), following the 2022
  reassessment that displaced an Indian origin.
- **The wheel** and **writing** are both recorded as unresolved priority
  disputes with two equal-standing claims, not as single inventions that spread.
- Also: spun fibre, woven cloth, cereal domestication, irrigation.

### Not added

Flagged `n.a.` in research and deliberately left out rather than guessed:
Yuchanyan pottery, plough dates, the Bactrian camel, Chinese *qu* fermentation,
and broad potato claims earlier than the Jiskairumoko direct evidence.

### Counts

1,461 → 1,480 entities. 155 → 175 cited. 175 → 203 sources. Schema unchanged at
3.0.0.

## 0.7.0.0 — Ages spine and regional navigation (2026-08-08)

### Added — Chalcolithic, regionally and never globally

Research (`docs/ages-spine-research.md`) found the term is irreducibly
regional: "there is no general agreement about what the Copper Age actually
is." A global node would need to span c. 6500 BC to c. 700 BC, swallowing the
Neolithic, the whole Bronze Age and part of the Iron Age, describing no real
shared period. So this does NOT follow the "Mesolithic (Eurasia)" pattern,
which works only because one qualifier covers one contiguous span.

- Chalcolithic (Southeast Europe) 5000-3700 BC — earliest known copper smelting.
- Chalcolithic (Southern Levant) 4700-3600 BC.
- Chalcolithic (Anatolia) 5500-3000 BC, flagged for three incompatible
  sub-periodizations in active use.
- Late Chalcolithic (Mesopotamia) 4500-3100 BC — ends 200 years AFTER the global
  Bronze Age node starts, which is the point.
- Chalcolithic (South Asia) 3000-700 BC — contemporary with Harappan Bronze Age
  urbanism, not prior to it.

Each records where there is no Chalcolithic at all: most of sub-Saharan Africa
goes stone straight to iron, China folds early copper into the Late Neolithic,
the Americas never reached a continent-wide Bronze Age, and Australian
archaeology dropped three-age terminology. A caveat on `global.bronze-age` notes
that its clean 3300 BC seam hides this wedge.

### Added — Epipalaeolithic, Levant only

Deliberately not a global or Eurasian node: it would double-count "Mesolithic
(Eurasia)", since the two are largely the same idea under different regional
naming traditions. One entity is defensible because its early part is invisible
under the current spine.

- Epipalaeolithic (Levant) 23,000-10,000 BC, IntCal20. Ends exactly where the
  Mesolithic node begins.
- Kebaran 23,000-16,000 BC and Geometric Kebaran 16,000-13,000 BC.
- The existing Natufian is the Late Epipalaeolithic and is cross-linked into it,
  not moved: its id and its breadcrumb are unchanged.

### Added — East Asian and Oceanian prehistory navigation

Seven regions had a `.prehistory` era and two did not, so Jomon, the Chinese
Neolithic, Sahul, Madjedbebe and Lake Mungo were unreachable by that route.
Fixed with `cross_parent_ids` rather than re-parenting, so ids, primary parents,
breadcrumbs and containment validation are all untouched.

Two placements were left alone on purpose. Jomon stays under Japan because it is
Japan's founding era, not a detachable prehistoric episode. Aboriginal Australia
is NOT gathered under Oceanian Prehistory: it has no end date because the
traditions are living, and filing an ongoing culture under "prehistory" would
say something false. Only its dated Pleistocene sites appear.

A null end is now read as UNDATED rather than ongoing when deriving these spans.
Propagating Madjedbebe's null rendered Oceanian prehistory as "75.0 ka -
present", which says the Pleistocene never ended.

### Changed — Nabta Playa and Green Sahara

Both already existed and were left in place in 0.6.0.0. Enriched here rather
than duplicated:

- **Nabta Playa** gains its three published phases (Middle, Late and Terminal
  Neolithic) and a calibration warning. The site span is stated in CALIBRATED
  years ending 6,200 cal BP, while the excavation literature publishes the
  ceremonial phases as bare radiocarbon BP ending 5,400 BP. Same event, two
  conventions. The phases carry the uncalibrated figures as published, flagged,
  rather than being silently converted. Also gains the caveat that its early
  Holocene cattle are argued to be hunted aurochs rather than domesticates.
- **Green Sahara** gains two corroborating syntheses and the detail that parts
  of the Sahel, Arabia and East Africa stayed wet until the 4.2 ka event.

### Stats

- **1,461 entities** (up from 1,448). **175 sources** (up from 160); 155
  entities cite at least one.
- All nine regions now have a prehistory branch.
- **Validation:** OK, no errors, 0 warnings.

## 0.6.0.0 — African prehistory depth and per-boundary dating (2026-08-08)

**Schema 3.0.0. Africa goes from 8 prehistory nodes to 37.**

### Note on the gap in this file

This changelog stopped at 2.1.0 and never recorded the renumbering to the
four-part scheme, nor the prehistory and regional-prehistory passes that took
the corpus from 1,305 to 1,417 entities. Those entries are not reconstructed
here; this file resumes from 0.6.0.0 and the intervening work is visible in the
git history and in `docs/regional-prehistory-authoring-notes.md`.

### Schema 3.0.0 — per-boundary dating (Q-30)

- `dating_method` is replaced by `start_dating_method` and `end_dating_method`.
  MAJOR because a consumer reading the entity-level field now finds nothing.
  Inside `alternatives`, `dating_method` is retained and correct: an alternative
  is a claim about one boundary.
- The end is **not** inherited from the start. 104 ends carry a method, derived
  only where physically possible — radiocarbon carries only within radiocarbon's
  reach, geochronological methods only where the end is also beyond it — and
  left unset otherwise. See `tools/end_dating.py`.
- Four entities have genuinely different science at each end: Neanderthal
  Europe, the Middle Stone Age, Rising Star and Sterkfontein. Under the single
  field every one of them was mislabelled at one end.
- `cosmogenic` added to the dating-method vocabulary. Sterkfontein and
  Swartkrans rest on 26Al/10Be isochron burial dating, which previously had no
  way to be recorded.
- The validator now checks BOTH boundaries against the radiocarbon ceiling. The
  end check is new reach, not a port: an impossible end date was untestable
  before, because the end had no method to test.

### Added — African prehistory (31 entities, 46 sources)

Africa held 8 prehistory nodes against Europe's 11, for the continent holding
roughly 3.0 of the app's 3.3 million years. The dataset already carried a
caveat warning readers that figurative art did not begin in Europe while the
node counts implied the opposite.

- **East African Rift:** Turkana Basin, Laetoli, Hadar, Gona, Melka Kunture,
  Olorgesailie, Herto, Bodo, Enkapune Ya Muto.
- **Southern Africa:** Sterkfontein, Swartkrans, Rising Star, Sibudu, Pinnacle
  Point, Diepkloof, Apollo 11 Cave, Kabwe.
- **North Africa and the Sahara:** Jebel Irhoud, Taforalt, Wadi Kubbaniya,
  Gobero, Capsian, Khartoum Mesolithic, Fayum Neolithic; Ishango in Central
  Africa.
- **Domestication and metallurgy:** cattle herding, cereal domestication, the
  Bantu homeland phase, Nok culture.
- **Behavioural firsts:** Cut-Marked Bone (Dikika) and Structural Use of Wood
  (Kalambo Falls). The Dikika sources had been in the registry since the
  prehistory pass and the Behavioural Firsts era was already dated to 3.39 Ma to
  hold it, but the node itself was never written.
- Two reference anchors added, Laetoli footprints and Lucy, because the new
  content ran older than the oldest anchor and had nothing to orient against.

### Disputes carried rather than resolved

Five entities are authored `date_precision: disputed` with rival chronologies as
`alternatives` and an `as_of` stamp, instead of one figure being quietly chosen:

- **Sterkfontein** — cosmogenic burial dating (~3.4-3.7 Ma) against U-Pb, ESR
  and palaeomagnetism (~2.0-2.6 Ma). Over a million years apart, for the same
  deposits, unresolved as of 2024.
- **Melka Kunture** — whether Garba IVD holds the earliest Acheulean at 1.95 Ma.
- **Ishango** — three incompatible figures; the radiocarbon is compromised by
  volcanic disruption of the local carbon reservoir.
- **Nok / Taruga iron smelting** — spread across nearly a millennium, partly
  because of a radiocarbon calibration plateau that more dating cannot fix.
- **Bantu homeland** — two syntheses 1,000-2,000 years apart on proto-Bantu.

### Corrections carried as caveats

Kabwe is not ~500,000 years old (299±25 ka by direct dating). Wadi Kubbaniya is
not an early-agriculture site; its cereals were modern contaminants. Nabta
Playa's early Holocene cattle are argued to be hunted aurochs, not domesticates.
Herto is not the oldest *Homo sapiens*. Gona is no longer uniquely the earliest
Oldowan.

### Deliberately not done

- **Laetoli is a site, not a behavioural first.** A bipedalism threshold would
  have moved the app's floor from 3.3 Ma to 3.66 Ma on an anatomical trait
  rather than a manufacturing behaviour, which is the arbitrary-floor problem
  the scope gate exists to prevent.
- **Nabta Playa and Green Sahara were already authored** with their own sources
  and are left untouched.
- **Regional placement is unchanged.** Jomon still sits under `east-asia.japan`
  and Sahul under `oceania.australia.aboriginal` rather than under
  `.prehistory` branches. Consistency there is a re-parenting job, not depth.
- **No global Chalcolithic or Epipalaeolithic framework.** African
  Epipalaeolithic content is authored (Capsian, Qarunian, Khartoum Mesolithic),
  but a worldwide framework needs its own sourced pass and would otherwise be
  invented rather than cited.

### Stats

- **1,448 entities** (up from 1,417). Prehistory 128, or 8.8% of the corpus, up
  from 97 and 6.8%.
- **Africa 37 prehistory nodes** (up from 8), now the largest regional branch.
- **160 sources** (up from 114); 144 entities cite at least one (up from 113).
- 49 entities carry alternatives, 52 carry caveats.
- **Validation:** OK, no errors, 0 warnings.

## 2.1.0 — South Asia expansion (2026-07-20)

**Closes the coverage gap flagged by the council review.** South Asia grew from 26 entities to 206, with dedicated attention to rulers, movements, and modern political history.

### New South Asian entities (180)

**Ancient / classical:**
- Maurya: added remaining rulers — Bindusara, Dasharatha, Samprati, Shalishuka, Devavarman, Shatadhanvan, Brihadratha
- Shunga: Pushyamitra, Agnimitra, Vasumitra, Bhagabhadra, Devabhuti
- Satavahana: Simuka, Satakarni I, Gautamiputra, Vasishthiputra, Yajna Satakarni
- Indo-Greek: Demetrius I, Menander I 'Milinda', Apollodotus II, Strato II
- Gupta: Chandragupta I, Samudragupta ('Napoleon of India'), Ramagupta, Kumaragupta I, Skandagupta, Purugupta, Narasimhagupta, Vishnugupta
- **New era: Harsha's Empire** (606–647) with Harshavardhana
- **New era: Pallava Dynasty** (275–897) with Mahendravarman I, Narasimhavarman I, Nandivarman II
- **New era: Pala Empire** (750–1161) with Gopala, Dharmapala, Devapala
- **New era: Rashtrakuta Dynasty** (735–982) with Dantidurga, Krishna I, Govinda III, Amoghavarsha
- **New era: Chalukyas of Badami** (543–753) with Pulakeshin II; **Western Chalukya Empire** (973–1189)
- Chola: Vijayalaya, Aditya I, Parantaka I, Rajadhiraja I, Rajendra II, Virarajendra, Kulottunga I, Kulottunga III, Rajaraja III, Rajendra III

**Medieval Islamic:**
- Delhi Sultanate: full dynasty sub-periods (Mamluk, Khalji, Tughlaq, Sayyid, Lodi) with 12 sultans including Qutb ud-Din Aibak, Iltutmish, **Razia Sultana**, Balban, Alauddin Khalji, Muhammad bin Tughlaq, Firoz Shah Tughlaq, Ibrahim Lodi
- Vijayanagara: Sangama, Saluva, Tuluva, and Aravidu sub-dynasties with 10 rulers including **Krishnadevaraya** and Aliya Rama Raya
- Bahmani Sultanate era + rulers; Deccan Sultanates era; Bengal Sultanate era
- Hoysala Empire era; Kakatiya Dynasty era with Ganapati Deva and **Rani Rudrama Devi**

**Mughal:**
- Humayun (both tenures), Jahangir, and all 10 late Mughals: Bahadur Shah I, Jahandar Shah, Farrukhsiyar, Muhammad Shah 'Rangila', Ahmad Shah Bahadur, Alamgir II, Shah Alam II, Akbar Shah II, and **Bahadur Shah II 'Zafar'** (last Mughal)
- **New Suri interregnum period** (1540–1555) with Sher Shah Suri and Islam Shah Suri

**Early modern:**
- Maratha: Shivaji, Sambhaji, Rajaram, Tarabai, Shahu I; **Peshwa Era sub-period** with 5 peshwas including Baji Rao I and Baji Rao II
- Sikh Empire: Maharaja Ranjit Singh, Kharak Singh, Nau Nihal Singh, Sher Singh, Duleep Singh
- **Kingdom of Mysore era** with Haidar Ali and Tipu Sultan

**Colonial:**
- **New era: East India Company Rule** (1757–1858) with 6 governors-general (Clive, Hastings, Cornwallis, Wellesley, Bentinck, Dalhousie) and the **Indian Rebellion of 1857** as an event
- British Raj viceroys: Canning, Lytton, Ripon, Curzon, Hardinge, Chelmsford, Irwin, Linlithgow, Mountbatten
- New events: Jallianwala Bagh Massacre (1919), Salt March (1930), Partition of India (1947)

**Independence and modern:**
- Founding figures: Gandhi, Jinnah, Ambedkar, Subhas Chandra Bose
- **India Prime Ministers sub-period** with Nehru, Shastri, Indira Gandhi (both terms), Rajiv Gandhi, Narasimha Rao, Vajpayee, Manmohan Singh, Modi
- **Pakistan Leaders sub-period** with Liaquat Ali Khan, Ayub Khan, Zulfikar Ali Bhutto, Zia-ul-Haq, **Benazir Bhutto**, Musharraf
- Bangladesh Liberation War event; Sheikh Mujibur Rahman, Sheikh Hasina
- Sri Lankan Civil War event

**Cultural / religious figures** attached to South Asia:
- Guru Nanak (founder of Sikhism)
- Kabir (bhakti-sufi poet)
- Rabindranath Tagore (first non-European Nobel laureate in Literature)

### Stats
- **1,303 total entities** (up from 1,123 in 2.0.0)
- **South Asia coverage: 26 → 206 entities** (7.9× growth)
- **Kind breakdown:** 43 regions, 248 eras, 343 periods, **641 reigns** (up from 493), 28 events (up from 22)
- **Tier breakdown:** 336 foundational, 415 intermediate, 552 specialist
- **Validation:** `✓ OK — no errors. 0 warnings.`

### Data model corrections
- Corrected Shunga era end to -73 (Devabhuti's death) with `date_note` documenting the -75/-73 disagreement
- Extended Satavahana era to -230 (Simuka's founding), with `date_note` noting the imperial phase begins c. -100
- Extended Rashtrakuta era to 735 (Dantidurga's founding)
- Flagged 5 legitimate role/date overlaps with `allow_outside_parent_dates` (Gandhi, Jinnah, Ambedkar, Subhas Bose, Mountbatten)

### Council-round fixes (applied mid-review)
- Renamed duplicate slug `south-asia.harsha.harsha` → `south-asia.harsha.harshavardhana` to avoid breadcrumb collision
- Split **Sheikh Hasina** into two tenures: 1st term (1996–2001) + 2nd term (2009–2024, forced from office in the 2024 uprising). Previous single record misrepresented her as longest-serving PM with only her first term modeled.
- Split **Benazir Bhutto** into two tenures: 1st term (1988–1990) + 2nd term (1993–1996). Previous single record claimed "twice PM" while modeling only the first term.
- Removed hagiographic phrasing from Samudragupta summary ("Napoleon of India" → Allahabad Prashasti-centered description) and Baji Rao I summary ("undefeated in 41 battles" → neutral phrasing).
- **Final v2.1.0 count: 1,305 entities** (643 reigns, 337 foundational). Validation: `✓ OK — no errors. 0 warnings.`

---

## 2.0.0 — Phase 0 & Phase 1 (2026-07-20)

**Data corrections and schema hardening based on the model-council review.**

### New required fields on every entity
- `parent_id` (nullable) — must always be present, `null` only for top-level regions
- `start_year` and `end_year` (nullable) — always present, `null` for unknown/ongoing
- `tier` — always present (defaults to `intermediate`)

### New optional fields
- `redirect_ids: []` — for future id migrations without breaking permalinks
- `start_year_min` / `start_year_max` / `end_year_min` / `end_year_max` — for scholarly disagreement (used on Ashoka, Bronze Age, Bronze Age Collapse)
- `start_precision` / `end_precision` — per-endpoint precision, in addition to the existing `date_precision`
- `date_note` — free text for disputed or transitional dating
- `allow_outside_parent_dates: bool` — silences the containment warning for legitimate role overlaps
- `links: []` — typed relations (successor_state_of, conquered_by, co_ruler_with, etc.). Populated on Yuan Dynasty as a working example.
- `capitals: []` — for polities whose capital changed over time
- More `date_precision` enum values: `year`, `decade`, `century`, `millennium`, `approx`, `traditional`, `disputed`, `unknown`, `exact`

### New wrapper schemas (dataset-level)
Every data file now requires:
- `schema_version` — semver of the model
- `dataset_version` — semver of the content
- `generated_at` — ISO-8601 UTC timestamp
- Its typed array (`entities` / `calendars` / `themes` / `frames`)

New schema files:
- `entities-file.schema.json`
- `calendars-file.schema.json`
- `themes-file.schema.json`
- `reference-frames-file.schema.json`

### Schema strictness
- ID pattern tightened: `^[a-z0-9]+(?:[.-][a-z0-9]+)*$` (rejects double separators, trailing separators, underscores)
- `additionalProperties: false` on nested source objects
- `uniqueItems: true` on all list-of-strings fields (aliases, cross_parent_ids, calendar_ids, etc.)
- `reference-frame` now requires `anchor_set` and `summary`
- `calendar.named_years` items now support optional `id` and `entity_ids` (many-to-many)

### Data corrections
- **Egypt** span extended from -3100..-30 to -6000..641 to contain both Predynastic and Roman/Byzantine children
- **11th Dynasty** span extended to include the early Theban Intefs before Mentuhotep II's reunification
- **18th Dynasty** end date corrected from -1295 to -1292 to contain Horemheb
- **Third Intermediate Period** end corrected from -664 to -656 to contain the full Kushite Dynasty 25
- **Yuan Dynasty** end extended from 1368 to 1370 (Toghon Temür ruled from Mongolia after Beijing fell)
- **Western Collapse** end extended from 476 to 480 (Julius Nepos recognized in East)
- **Kublai Khan, Cyrus II, Peter I, Lenin, Nobunaga, Itzcoatl, Valentinian III, Galba, and other overlap-legitimate rulers** marked with `allow_outside_parent_dates: true` and a `date_note`
- **Nengō spanning Japanese-era boundaries** (Wadō, Enryaku, Keichō, Shōkei, Genkō) marked with `allow_outside_parent_dates`
- **Narmer, Nitocris, Romulus Augustulus** now flagged `date_precision: "traditional"`
- **Two Kamakura-era Genkō nengō** disambiguated in display names: `Genkō (元亨)` and `Genkō (元弘)`
- **Missing summaries** backfilled on 119 foundational-tier entities

### New entities (33 total)
- **Renaissance** (Italian + Northern), **Reformation** (+ Luther, Thirty Years' War), **Scientific Revolution**, **Enlightenment**
- **Industrial Revolution** (First + Second), **Scramble for Africa** (+ Berlin Conference), **Decolonization**
- **Napoleonic Wars** (+ Austerlitz, Trafalgar, Waterloo)
- **Caesar's Assassination**, **Battle of Actium**
- **Korean War**, **Vietnam War**, **Cuban Missile Crisis**, **Apollo 11 Moon Landing**, **Fall of the Berlin Wall**, **Dissolution of the Soviet Union**
- **September 11 Attacks**, **War on Terror**, **Global Financial Crisis**, **COVID-19 Pandemic**
- **Neolithic (Agricultural) Revolution**, **Early / Middle / Late Bronze Age** subdivisions

### New themes (7)
- Greater Islamic World
- Industrialization
- Birth of Major Religions
- Cold War Proxy Conflicts
- Decolonization
- Mesoamerican Civilizations
- Early Modern European Transformations

### New reference-frame anchors (9)
- Waterloo (1815), Fall of Granada (1492), Siege of Vienna (1529), Founding of the Mughal Empire (1526)
- First Opium War (1839–42), Atomic bombing of Hiroshima (1945), Apollo 11 (1969), Fall of the Berlin Wall (1989), September 11 (2001)
- All previously-missing summaries on existing anchors backfilled

### Validator (`validate.py`) — now checks:
- Schema violations at file wrapper level AND item level
- Duplicate entity ids
- Missing parent / cross_parent / link / calendar_id / redirect_id references
- Year zero (invalid in BCE/CE without astronomical numbering)
- Inverted date ranges (both start/end and min/max)
- Named-year sequences (inverted, missing links)
- **NEW warning-level checks:** child-outside-parent dates (respecting `allow_outside_parent_dates`), foundational tier missing summary, reference frames missing summary, duplicate sibling display names under same parent

### Stats
- **1,123 entities** (up from 1,090)
- **300 foundational · 326 intermediate · 497 specialist**
- **43 regions · 235 eras · 330 periods · 493 reigns · 22 events**
- **21 calendars · 16 themes · 37 reference frames**

### Validation result
`✓ OK — no errors. 0 warnings.`
