# Changelog

## 0.42.0.0 — Smaller Language Families / Other Families, authored into the live dataset (2026-08-22)

The same pseudo-hierarchy from the research artifact (previously landed in
`docs/research/languages/tree.json` only) is now authored into `src/data/entities.json`, the file
the app actually ships. Reported from use: the Languages tab was still showing all 129 root family
nodes plus the existing "Families With One Language Here" container -- correctly grouping the
single-roster-entry families, but leaving every 2-9-entry family (Uralic, Hmong-Mien, Chibchan,
Algic, and 17 more) sitting at the top alongside Indo-European.

Replaced `author_languages.py`'s own `_group_singletons` (grouped 1-language families only, counted
from the authored entity list after family nodes with no dated descendant had already lost their
`is_family_node` distinction) with grouping done upstream in `build_tree.py`, on tree.json's own rows
while they still carry that field. One grouping pass, one count, no risk of the two disagreeing on
where the line falls:

- Top level (16): every family with >=10 roster entries, plus Mayan, Uto-Aztecan and Tupian named
  explicitly. Roster-entry count under-represents the Americas -- it measures how many named
  languages the Tier 1/Tier 2 research happened to carry for a family, not how historically
  significant it is, and a pure count threshold would have erased Maya, the Aztec empire and
  Guarani/Tupi from the top of the tree entirely.
- Smaller Language Families (`languages.smaller-families`): 3-9 entries, 18 families.
- Other Families (`languages.other-families`): 1-2 entries, 203 families. Not the same as
  Isolates -- Glottolog does show these with relatives, the roster just barely touches them.

`entities.json`: 7813 -> 7814 (two new container nodes; no leaf language moved or lost). Both
new containers carry summaries and pick up hull dates from their descendants like any other family
node, so region-node and dated-entity counts each move by the corresponding amount.

`author_languages._group_singletons` is left in the file, unused, as a record of the count-based
approach it replaced -- it is no longer called.

## 0.39.0.0 — Afro-Asiatic and 52 other families were sitting beside their own parent (2026-08-22)

`build_tree.py`'s topological sort used `len(paths.get(g, "").split("/"))` as an ancestor-depth key.
Splitting an empty string returns `['']` -- length 1, the same length as a genuine one-element path
like Semitic's `afro1255`. That tie let a depth-1 child sort before its own depth-0 parent whenever
Python's set-iteration order happened to put it first, so `emitted.get(chain[-1])` came back `None`
and the child fell back to the tree root as a sibling of its own parent instead of a child of it.

Confirmed empirically, not just by reading the sort key: rebuilding with a corrected key (0 for no
Glottolog path, real segment count otherwise) resolved all 60 fallback cases; the buggy key stranded
60. 53 of those were still visible as separate root nodes in the shipped tree, including Semitic,
Chadic, Cushitic, and Egyptian sitting beside Afro-Asiatic rather than under it, and Korean sitting
beside Koreanic.

Also folded Glottolog's own catch-all bookkeeping codes -- `Unclassifiable`, `Pidgin`, and
`Bookkeeping` (`uncl1493`, `pidg1258`, `book1242`) -- into the existing Unclassified container
instead of letting them surface as if they were independent, accepted language families.

Root-level family nodes: 292 -> 237. Isolates (184), Disputed Groupings (5) unaffected. Unclassified
grew from 0 to 8 (the languages previously mis-typed as belonging to a bookkeeping "family"). One
known placement quirk remains and is untouched here: Songhay sits at root outside any family node.

This fix lands in `docs/research/languages/tree.json` and its companions only.
`author_languages.py`'s `extend()` raises on any id already present in `src/data/entities.json`, and
reparenting under this fix changes ids for the 53 affected nodes while leaving the other ~237
identical -- a same-tree rerun cannot be reconciled against an already-authored dataset without a
deliberate re-authoring pass (drop the existing `languages.*` subtree, rerun `extend()`, repair any
cross-links pointing at the ~53 changed ids, rerun `dataset-integrity.test.ts`). The deployed app
still serves the pre-fix branch until that pass runs.

## 0.31.0.0 — Phoenicia and the Vedic period (2026-08-10)

The two widest childless blocks `coverage.py` was reporting. Both were hiding a
wrong date.

### Phoenicia ended in the wrong century

The entity ran 1500-539 BCE. **539 BCE is the Persian conquest — a change of
imperial overlord, not an end.** Under Achaemenid rule Tyre, Sidon and Byblos kept
their own kings and fleets; Sidon revolted in the 350s; Tyre held out against
Alexander for seven months. Homeland Phoenician independence ends in **332 BCE**
with the fall of Tyre. Corrected, with 539 kept as a sourced `minority`
alternative.

Now carries five periods (Late Bronze Age Canaanite, Independence, Assyrian,
Babylonian, Persian) and four cities (Byblos, Sidon, Tyre, Arwad), with Carthage
cross-linked.

### The name problem goes deeper here than Byzantine did

With Byzantium an exonym displaced a self-designation that is known. Here **there
may be no self-designation to recover.** The evidence — tombstones, coinage, the
near-total loss of Phoenician literature — shows people identifying as Tyrian,
Sidonian or Byblian, by city and family. Josephine Quinn argues "the Phoenicians"
as a self-conscious people is substantially a modern scholarly construction; the
Met treats Canaanite as the plausible collective self-term. Both recorded, neither
adopted.

Also recorded: Phoenicia was **never a state, empire or confederation** —
Britannica, the Met, Lipiński and Quinn agree — and **Punic versus Phoenician is a
modern split**, not one the ancient sources draw consistently.

### The Vedic period's end date describes a language, not a polity

Split into Early Vedic (Rigvedic) and Later Vedic, plus the corpus. **500 BCE is a
convention tied to Panini and the closing of the Vedic texts.** The political and
economic transition — the mahajanapadas, the second urbanisation, the Buddha and
Mahavira — is more consistently dated around 600 BCE, which is where this
dataset's Mahajanapadas entity already begins. Both recorded, and the overlap is
now deliberate rather than an accidental gap.

**Painted Grey Ware belongs to the Later Vedic phase only**, roughly 1200-600 BCE
— a distinction the single undivided block silently erased.

### Three claims kept apart

The Indo-Aryan migration question is represented, not settled. Public argument
merges three separable claims and the caveats keep them apart: a **linguistic**
claim about language origin, an **archaeological** claim about material
continuity, and a **genetic** claim about steppe ancestry. Named proponents on
both sides — Witzel, Parpola and Anthony for migration; Talageri, Elst and Danino
against — with Bryant's survey cited for both.

The genetic evidence already existed in this dataset, sourced, at
`south-asia.steppe-ancestry`. The Vedic node **links** to it with relation type
`other` rather than something stronger, because calling it "predecessor of" or
"part of" would assert the very connection under dispute.

### The dating method was wrong, and the screenshot said so

First attempt marked these `typological`, which puts a date on the scientific side
of the frame rule — so the readout rendered the Vedic period as **"3,449 - 2,449
BP"**. Nobody dates the Rigveda in years before present. Same failure as Chaco
Canyon rendering as "1,100 - 700 BP".

`received` is both the fix and the more accurate description: the schema defines it
as a date "arrived at by transmission rather than by measurement or attestation"
and cites typology-derived brackets as an example. A date inferred from the
internal stratigraphy of a language and handed down through scholarship is exactly
that.

### One gap closed, a smaller one opened

Phoenicia and the Vedic period both leave the childless-era report. **Byblos
immediately joins it**, as a single 2,668-year block. The tool is right — same
shape of problem, one level down — but the research covers the city's phases only
lightly and inventing subdivisions to satisfy a report would be worse than a
visible gap.

### Counts

1,705 → 1,717 entities. 670 → 689 sources. Entities carrying a source 479 → 495.
Unsourced foundational dates 271 → 269.

## 0.30.0.0 — A cross-region placement now needs a source (2026-08-09)

Twice in three releases a pass added `cross_parent_ids` asserting that a polity
held territory in another world region, with no citation, while an open issue said
unsourced region claims were the least honest field in the dataset. Nothing
checked, so nothing stopped it. **Rule 7** now does.

### What the rule covers, and what it deliberately does not

It fires when a cross-link crosses a **top-level geography** — "the Kushans held
South Asia" is a claim about the past and needs a source.

It is silent for links into `global`. Placing the Mongol Empire under
Multi-Regional Empires is *this dataset's taxonomy*, not a statement about the
world, and demanding an external citation for a classification decision would be
a category error. A rule that required footnotes for taxonomy would be
worked around rather than obeyed, and would end up grandfathered into
uselessness.

### No grandfather list

The nine geographic links that had no source are now sourced rather than
exempted, so the rule ships with **no exception list at all**. Every remaining
unsourced cross-link is taxonomy-only, which the rule correctly ignores.

Newly cited: the Kushite 25th dynasty to Britannica's Cushite-dynasty and Nubia
entries; the 27th dynasty to Britannica and UCL's Digital Egypt; Ptolemaic and
Roman Egypt, the Seleucids and Alexander to Britannica's Hellenistic-age and
Ptolemaic-dynasty entries; the Yuan to Britannica's Mongol-empire treatment; the
Kushans to Britannica and an Oxford University Press chapter; the Indo-Greeks to
Britannica.

Several of these look near-tautological — Ptolemaic Egypt *is* a Hellenistic
kingdom — and that is precisely why they were never sourced. But "obvious" is how
the unsourced Sarasvati assertion and the wrong Greece and Macedon dates got in.

### Verified by planting violations

The rule was tested three ways rather than assumed: an unsourced cross-region
link errors, a sourced one passes, and an unsourced link into `global` passes.

Worth recording that the **first attempt silently did nothing.** The insertion
anchor did not match, `str.replace` returned the file unchanged, and the tests
"passed" against a rule that was never in the file. The edit now asserts its
anchor exists before writing, and the rule's presence was confirmed by grep
before any behaviour was tested.

### Counts

Sources 660 → 670. Entities carrying a source 470 → 479. Cross-linked entities
sourced 29 → 38 of 46. Unsourced foundational dates 279 → 271.

## 0.29.1.0 — Source the region claims added in 0.29.0.0 (2026-08-09)

A self-inflicted regression, fixed one release later.

Issue #5 says the authored region lists are the only field in the dataset that is
neither sourced nor visibly marked as unsourced, and calls them its least honest
field. The previous release then added **nine more cross-links with no citation
at all** — seven of them on entities carrying no source whatsoever. The mistake
was made again, immediately, by the same reasoning that had identified it.

"This dynasty ruled Iran" is a claim, and the research that produced those links
already carried the warrant for each one. It simply was not attached. Now it is:

* **Seljuk** — every Great Seljuk capital (Nishapur, Ray, Isfahan, Hamadan) was
  in Iran.
* **Samanid** — held Khorasan, Ray, Tabaristan, Gorgan, Isfahan despite a Central
  Asian capital.
* **Ilkhanate** — Maragheh, Tabriz and Soltaniyeh were all Iranian capitals.
* **Khwarazmian** — Tabriz was the capital from 1225.
* **Ghaznavid** — cited to Dandanaqan, the 1040 defeat that ended its Iranian
  phase, which is what the qualification on the link refers to.
* **Timurid** — cited to Britannica's own hedged treatment, so the hedge points at
  something a reader can check.
* **Rashidun, Umayyad, Abbasid** — cited to Britannica's account of the conquest
  and its aftermath.

Cross-linked entities carrying a source: 22 → 29 of 46. The remaining 17 predate
this pass and are still open under #5.

## 0.29.0.0 — Central Asia and Islamic Iran, found by tooling (2026-08-09)

The first release where the *target* was chosen by a tool rather than by
judgement. `tools/report_gaps.py` was written to look for entities the data
implies but does not contain, and on its first run it named the two largest
remaining holes: a Central Asian branch with nothing between 1400 BCE and 1206
CE, and an Iran branch jumping from the Sasanians in 651 to the Safavids in 1501.

### Iran's 850-year hole was mostly a filing problem

The Seljuks, Ilkhanate, Timurids, Khwarazmians and Samanids were all already in
the dataset — filed under Central Asia. An Iranian reader could not see them,
though the Seljuk capitals were Nishapur, Ray, Isfahan and Hamadan and every
Ilkhanid capital was in Iran. Nine dynasties are now cross-linked to Iran, which
is what the multi-regional machinery was built for.

**The cross-links are graded, because the research was.** Seljuk, Ilkhanate,
Khwarazmian and Samanid are straightforward. The **Ghaznavids** held Khorasan
until Dandanaqan in 1040 and were an Afghan and north Indian power afterwards, so
the time limit is stated. **Timurid** control was loose and effectively confined
to Shah Rokh's reign, per Britannica's own hedged framing, and the hedge is
recorded rather than dropped.

Two errors were possible and only one was visible: claiming a Central Asian
dynasty ruled Iran would be a false statement, while hiding dynasties that
plainly governed Iran is a silent omission. The dataset was doing the second.

Newly authored: the Arab conquest, the **Iranian Intermezzo** (Britannica's own
section title, not a coinage here) with the Tahirids, Saffarids and Buyids, the
Qara Qoyunlu and Aq Qoyunlu, and the **Afsharids and Zand** — who fill the 53
years between Safavid and Qajar and *overlap each other*, the Afsharids holding
Khorasan while the Zand held everything else.

### The report caught its own follow-on

Closing the large hole exposed a smaller one: 651-821 still read as empty,
because the Rashidun, Umayyad and Abbasid caliphates governed Iran but were
reachable only from Arabia, Mesopotamia and Central Asia. Now linked. The
argument for re-running the report after every change rather than once.

### Central Asia: a correction first

The dataset carried a single **"First Turkic Khaganate, 552-744"**. That span
runs three distinct polities together — the first khaganate to its division
around 581-603, the eastern and western khaganates, and the *second* khaganate of
682-744 after a period of Tang control. Corrected to 552-603, with the second
authored separately.

Added: Hephthalites, Uyghur Khaganate, Ghaznavid, Kara-Khanid, Khwarazmian, the
Bukhara, Khiva and Kokand khanates, the Russian conquest, and **Qara Khitai** —
which closes a gap deliberately left open two releases ago because it needed the
two-date treatment. Chinese, Persian and Arab sources end the dynasty at the 1211
Naiman usurpation; modern scholarship dates the state's fall to 1218. Both kept.

### Two entities that are deliberately not states

**Saka** is a Persian exonym for eastern Iranian steppe peoples, as Scythian is a
Greek one; the two overlap without being identical, and neither is a
self-designation. Entered as a people with a naming caveat, not an empire.

**Sogdia was never unified.** Sources say so directly: a set of city-states around
Samarkand and Bukhara whose merchants ran the Silk Road, under a succession of
outside overlords. Authoring it as a kingdom would invent a polity to fill a
space — the exact failure this pass exists to correct.

### Counts

1,683 → 1,705 entities. 623 → 654 sources. Entities carrying a source 440 → 463.
Central Asia 43 → 56.

## 0.28.0.0 — Southeast Asia (2026-08-09)

Southeast Asia was the thinnest region in the dataset by a wide margin: **35
entities against East Asia's 491**. The imbalance was not evenly spread. Its
*prehistory* was well covered and fully sourced. Its *history* was eighteen
entities, of which **one** carried a source.

Now 65 entities, 25 foundational, and 39 of the 49 historical ones sourced.

### Three specific failures

**Burma stopped in 1297.** Pagan ended and nothing followed — 588 years blank
through the Toungoo and Konbaung dynasties, the Anglo-Burmese wars and the
colonial period. Now: Dvaravati, post-Pagan fragmentation, Toungoo, Konbaung,
British Burma.

**Majapahit had no predecessor.** A reader met the largest empire in Javanese
history arriving from nowhere in 1293, with the four centuries that produced
Borobudur and Prambanan absent. Now: Medang, Kahuripan, Kediri, Singhasari before
it, and Demak and the Mataram Sultanate after.

That is the *same failure* the Song had before the Jin was added — a consequence
with its cause deleted — found independently in a different region. Worth
checking for deliberately rather than stumbling on.

**Đại Việt was one node covering 939-1804**, in a dataset that gives China
individual emperors. Eleven dynasties now sit under it.

### The name was also wrong, which matters more

Đại Việt was in use **1054-1400 and 1428-1804**. Before that the state was Đại Cồ
Việt; under the Hồ it was Đại Ngu; during the Ming occupation it was the province
of Jiaozhi. Applying one name across 865 years asserted a continuity of
self-designation that never existed — the same error the Byzantine and Golden
Horde passes addressed.

The container is renamed Vietnam (dynastic), the three real names are recorded
with their actual spans, and **the dataset's own former span is entered as a
`rejected` form** so the correction is visible rather than silent.

### Dates that look precise and are not

Recorded as `alternatives` rather than smoothed into ranges, because a wide range
implies the middle is likeliest when the claim is that sources disagree:

* **Majapahit's 1527** is conventional, tied to Demak's conquest of Kediri; a
  chronogram gives 1478 and recent work dates the collapse to 1513-1528.
* **Sukhothai's 1238** and its "first Thai kingdom" framing both rest on the Ram
  Khamhaeng inscription, whose authenticity has been disputed since the 1980s.
  Entered as `traditional`.
* **Aceh** has four competing founding dates; **Sulu** two; **Lan Xang's** split
  is dated 1694 or 1707; the **Ngô** dynasty ends 965 or 968.
* **Indonesia** was proclaimed in 1945 and recognised in 1949. Both kept — which
  counts is a political question, not a factual one.

### Two entities needing opposite kinds of care

**Srivijaya was not identified until 1918**, when Cœdès assembled it from Chinese
accounts and inscriptions. Its nature is still argued and its capital unsettled,
so it carries a `contested-existence` caveat saying it is a modern reconstruction
rather than a state that named itself in its own surviving documents.

**The pre-Spanish Philippines runs the opposite risk.** Only **Tondo** is
authored, on the Laguna Copperplate Inscription. Cebu, Butuan and Maynila are far
thinner, and this literature contains the **Code of Kalantiaw**, a 1913
fabrication treated as authentic for decades. The honest answer to "what
pre-colonial states were there" is "one we can evidence here, and others we
cannot" — not a tidy list.

**Brunei** ends at 1888 rather than running to the present, because it was a
British protectorate until 1984 and an unbroken span would assert sovereignty
that lapsed for ninety-six years.

### Exonyms recorded, not suppressed

Funan is a Chinese exonym with no attested indigenous name. Siam is what
outsiders called Ayutthaya. Burma is the colonial-era form. Champa's own
attested self-designation was Campā, against Chinese Lin-yi and Vietnamese Chiêm
Thành. Champa is also marked as a confederation of five polities rather than one
continuous kingdom.

### Not done

The Trịnh-Nguyễn division is left unauthored. Modelling it as two co-existing
lord-domains under nominal Lê rule is right, but it needs the care the caliphate
overlap needs, and is filed as an open question.

### Counts

1,653 → 1,683 entities. 578 → 623 sources. Entities carrying a source 402 → 440.
Unsourced foundational dates 298 → 279.

## 0.27.0.0 — Old spellings, and the states the Song shared China with (2026-08-09)

### Wade-Giles, because half the library uses it

Anyone holding a book printed before about 1980 meets Ch'ing, Chou, Sung and
T'ang, and the dataset returned **nothing** for any of them. Nine dynasties now
carry their Wade-Giles form, sourced to the Library of Congress ALA-LC table.

**Only the forms that actually differ are recorded.** Shang, Han, Sui, Ming and
the Three Kingdoms states Wei, Shu and Wu are spelled identically in both
systems, so an alias would claim a name change where none happened.

Two cases are more interesting than the rest. **Yüan** differs from Pinyin only
by an umlaut that older printing frequently dropped, so one book may contain both
spellings. And **Wade-Giles renders both Jin dynasties as "Chin"** -- 晉 for
266-420 and 金 for the Jurchen state -- so the older system is strictly *less*
able to distinguish them than the modern one. That is the mirror image of the
Japanese era problem fixed in the previous release, where romanisation collapsed
two distinct kanji.

Searching "Chin" now correctly returns both the Qin and the Jurchen Jin, because
an unapostrophed "Chin" in an old book genuinely is ambiguous between Ch'in and
Chin.

**Postal romanisation was deliberately not done.** Peking, Nanking, Canton and
Amoy apply to *place* names, and the dataset contains no Chinese cities -- there
is nothing to attach them to. Recorded as an open issue rather than half-applied.

### The Song did not rule China alone

The dataset split the Song into Northern (960-1127) and Southern (1127-1279) but
contained **none of the states that caused the split**. The Southern Song exists
because the Jurchen Jin took Kaifeng in 1127 and carried off two emperors; the
consequence was in the data with the cause deleted.

Added: **Liao** (Khitan), **Jin** (Jurchen), **Western Xia** (Tangut), and the
**Jingkang Incident** itself, placed under the Jin that carried it out and
cross-linked to the Northern Song it ended, so it is reachable from either side.

Traditional historiography supports treating these as dynasties rather than
intrusions: the Yuan commissioned official histories of Liao, Jin and Song as
three parallel legitimate states. Western Xia notably received no official
history, which is recorded as a fact about the historiography rather than about
the state.

### Liao keeps both of its founding dates

907 is traditional and the year Yelü Abaoji became khagan; 916 is when he
proclaimed himself emperor in the Chinese manner, which most scholarship prefers.
The dataset leads with 907 because it is the date a reader arrives with, and
records 916 as a `majority` alternative against 907 as `traditional` -- using the
standing field added for exactly this. A Shandong University study argues the
*Liaoshi*'s own use of 907 was deliberate rather than an error.

### The Xia is entered as a dispute, not a dynasty

Britannica calls it legendary; the Cambridge History of Ancient China begins with
the Shang; the state-sponsored Xia-Shang-Zhou Chronology Project assigns it
2070-1600 BCE and identifies every Erlitou phase with it, on a method that drew
sustained criticism in Western sinology. It carries two `contested-existence`
caveats holding both positions, in the shape established for the ROC, and the
date note says plainly that its span is that project's position rather than an
established chronology.

This also makes "Hsia" findable, which was the original complaint.

### What adding things exposed

Two problems surfaced only because new entities sat next to old ones.

**The Sui was `intermediate`** -- invisible at the default tier -- while the
conquest dynasties were about to become visible. A reader at Standard tier would
have met the Liao before the dynasty that reunified China after four centuries of
division. Promoted, and the promotion immediately failed validation for having no
summary: the entity had been hidden, so nothing ever demanded one.

**The Five Dynasties sits at `specialist`**, so the interregnum between Tang and
Song is invisible by default and the two appear adjacent. Left alone
deliberately, because how much division a default view should show is an
editorial judgement rather than an error, and it is filed as an open question.

### Counts

1,648 → 1,653 entities. 561 → 578 sources, 402 cited. 86 entities carry
`name_forms`, up from 70.

## 0.26.0.0 — Multi-regional, not cross-regional (2026-08-09)

### The word was wrong, and so was the placement

"Cross-regional" implies crossing *from* one region *to* another. These polities
were in several at once, which is a different claim. The category is renamed
**Multi-Regional Empires** and stops being a top-level peer of real geographies,
because it never was a place.

It now sits at `global.multi-regional`, one level under Global & Multi-Regional
-- not directly under `global`, which already holds fifteen chronological
frames. The Abbasid Caliphate between the Bronze Age and the Middle Ages would
mix polities with periodisation.

The thirteen `cross-regional.*` identifiers are renamed to
`global.multi-regional.*`. The identifier is visible in the readout, and leaving
it pointing at a word the app no longer uses is the same drift that was flagged
on `dutch-eic`.

### Nothing was lost, and reach is inherited

Each empire is cross-linked to the regions it actually held. Because the tree
places an entity under every cross-link, **its children come with it**:
cross-linking the Ottoman Empire to Anatolia, the Nile Valley and Eastern Europe
makes Suleiman reachable by all three paths without touching his entity at all.
Nine cross-link lists cover several hundred descendants.

Verified by walking each path in the browser:

* West Asia → Anatolia → Ottoman Empire → Suleiman ✓
* Africa → Nile Valley & Northeast Africa → Ottoman Empire → Suleiman ✓
* Global & Multi-Regional → Multi-Regional Empires → Ottoman Empire → Suleiman ✓

The Ottoman Empire now appears in the Nile Valley column beside Kush, Aksum and
the Fatimids, which reads as it should.

### These are authored claims, unlike `regions`

The previous release drew a line: a *derived* list can say where an entity is
placed, but where a polity *ruled* has to be asserted. These cross-link lists
are that assertion, and they are deliberately coarse -- the regions a polity
substantially held, not every province it raided.

Two judgement calls recorded in the module: the **Rashidun** caliphate is given
West Asia and Africa but not Central Asia, since it reached Khorasan only at the
very end and the eastward push belongs to the Umayyads; and **Columbus** gets
the Americas and Europe rather than everywhere the consequences reached, which
would be the whole dataset.

### What the screenshot caught

The breadcrumb shows the canonical path. Navigating Africa → Nile Valley →
Ottoman → Suleiman and then being told "Global & Multi-Regional › ..." looks
like a bug. The readout now adds **"Also under Africa, Europe, West Asia"**,
which turns a surprise into information and uses the derived `regions` field to
do it.

### Counts

1,648 entities unchanged; this pass moved and relabelled. Region nodes 43 → 42.
85 entities now span more than one region, up from 60, because folding the
category made the empires' reach explicit.

## 0.25.0.0 — Cross-Regional means empires, and the deferred gaps are filled (2026-08-09)

### The category was inverted, and the fix was already waiting

Parked five releases ago with "continue as is and revisit". Cross-Regional
Empires held nine genuinely imperial entities and **twelve that were not empires
at all**: two world wars, the Cold War and its six events, plus the Bronze Age
Collapse, the Axial Age and the Black Death. Meanwhile every actual multi-region
empire sat filed under a single region.

The twelve have moved, and three of them landed somewhere standing empty:

* the world wars and the entire Cold War subtree into **global.short-20c**,
  Hobsbawm's short twentieth century, 1914-1991, which is exactly their span and
  had no children at all;
* the **Axial Age** into Classical Antiquity, an exact fit at -800 to -200;
* the **Black Death** into the Middle Ages.

That the misfits fitted the empty eras this neatly suggests the taxonomy was
sound and only the filing was wrong.

The test is now written into the category itself: a single polity whose
territory crossed more than one region, or a process of imperial expansion or
contraction. A worldwide event that belongs to nobody is Global.

Eight empires are **cross-linked** rather than moved -- Mongol, Timurid,
Achaemenid, Spanish, Portuguese, British, Russian, Rome. Moving them would gut
the regions and destroy the breadcrumb that says where a polity came from.

Which leaves a real finding: **the caliphates are the only entities whose
primary home is this category**, because they are the only ones with no single
regional origin. Rashidun through Abbasid governed from Arabia, Syria and Iraq
in turn while ruling from Iberia to Central Asia.

### Global becomes Global & Multi-Regional

Its old summary read "cross-regional and worldwide frames" -- running together
the two things this pass spent its time separating. The new name says what the
region is for: everything that is not one region, whether because it is
everywhere or because it is several places at once.

### `regions`, derived rather than authored

A new field lists the top-level geographies an entity is reachable from,
computed from the tree in both directions. 60 entities span more than one.

**It means placement, not territory**, and the difference matters. The
Hellenistic world comes out spanning four regions, which is right. The Mongol
empire comes out at two, which understates it: the Ilkhanate and Golden Horde
are ordinary children, so their cross-links to West Asia and Europe do not
propagate upward -- and propagating through every descendant would make Europe
"span" Africa because Ptolemaic Egypt cross-links into the Hellenistic world.
That gap is not a traversal bug. It is the difference between a placement graph
and a territorial claim, and only the first is something a tree can know.

### The deferred gaps, filled

Four things earlier passes declined, each for a stated reason now addressed:

* **A Netherlands node**, so the **VOC** and both **West India Companies** have
  somewhere to live. Two passes refused to wedge a company that operated from
  the Cape to Nagasaki under "Maritime Southeast Asia".
* Both companies turn out to illustrate a pattern this dataset keeps meeting: a
  date that looks disputed but is a process seen from different points. The VOC
  ends in 1798, 1799 or 1800 -- debts assumed, charter lapsed, state control --
  three steps, three correct dates. The WIC is **two companies**, bankrupt in
  1674 and rechartered in 1675; the old "1621-1794" figure ran them together.
* **The French colonial empire**, first and second, with the same
  periodisation argument as the British, and 5 July 1962 flagged as a
  commemorative convention chosen to fall 132 years after the landing at Algiers.
* **Britain's 123-year hole** between the Stuarts and the Victorians, filled as
  the Georgian era, whose own end is disputed between 1830 and 1837.
* **The Columbian Exchange**, deferred from the Americas pass because the
  estimates run from 8 million to over 100 million. Authored now precisely *as*
  a dispute -- Kroeber low, Dobyns at 90-112 million assuming 95 per cent
  mortality, Denevan at about 55 million -- because leaving it out left every
  post-1492 end date in the dataset unexplained.

### Counts

1,640 → 1,648 entities. 549 → 561 sources. 390 → 397 cited. Schema 3.3.0 →
3.4.0.

## 0.24.0.0 — Endonyms from cuneiform, and a name that claims the past (2026-08-09)

Fourth tranche, 54 to 70 entities. All eight kinds remain in use.

### The case that started this was not using the mechanism

The **Golden Horde** prompted the whole naming project three releases ago -- a
16th-century Russian coinage sitting where a polity's own name belonged -- and it
had been carrying flat `aliases` plus a caveat ever since, because it predated
`name_forms`. Now typed like everything else, with **Ulug Ulus** as the endonym.

### Cuneiform means some endonyms are recoverable exactly

Uruk is the Akkadian name. The city's own Sumerian name was **Unug**, written
𒀕𒆠. It reached English through the Bible as Erech and through Greek as Orchoe,
and the site is Warka in Arabic today -- possibly the root of "Iraq". Five names,
four languages, one place, and we know which one the inhabitants used.

**Chogha Zanbil** is the same shape: a modern Persian name for a mound whose
Elamite name, **Dur-Untash**, is stamped on its own bricks. Susa is the Greek
form of Shushan. And **Newgrange** is an English farm name -- from the grange
land of Mellifont Abbey -- for a monument the Irish call Sí an Bhrú.

### A name that is a claim about who owns the past

Calling the Indus civilization **Sindhu-Sarasvati** ties it to the Rigvedic
river, and through that to Vedic culture. Both halves of this are now recorded,
because a reader who meets only one has been handled:

* The identification of the Sarasvati with the Ghaggar-Hakra is *not* fringe. It
  dates to 1855 and generations of indologists, geologists and archaeologists
  have endorsed it.
* As a renaming it does work. Kumar sets out how identifying the two lets the
  Harappans be Aryanised, the Aryans be indigenous, and the Hindu community be
  the exclusive proprietor of the Indian past. Other historians call the label
  hyper-nationalist.

**The screenshot caught the dataset doing the thing it was documenting.** The
Indus summary read "along the Indus and Sarasvati rivers" -- asserting the
contested name as a bare fact, directly above the caveat calling it contested.
Same failure as the ROC's 1949: the prose making a claim the apparatus was busy
qualifying. Now reads Ghaggar-Hakra.

### A rival scheme, not a set of synonyms

Shaffer's **Integration Era** and **Localization Era** are not other words for
Mature and Late Harappan. They come from a different model, organised by
interaction intensity rather than urban phase, with its own boundaries --
Shaffer's Regionalization starts around 4000 BCE where Coningham and Young put it
at 5000. Filed with that stated, rather than implying interchangeability.

### One more silent editorial choice, stated

This dataset says Neolithic **Transition**, not Neolithic **Revolution**. Same
kind of choice as Age of Sail over Age of Discovery, and equally unexplained
until now. Childe's "revolution" is the famous label and implies a speed the
dataset's own entities contradict: roughly four thousand years in Southwest Asia.

### Smaller things

The Edo period is the Tokugawa period named for a capital instead of a house --
two conventions used interchangeably. "Protestant Reformation" names a movement
by its outcome and from one side. **Menander I** is remembered in two traditions
under two names, Greek on his coins and Milinda in the Pali Milindapanha where he
debates a monk and converts. **Tutankhamun** was Tutankhaten at accession,
honouring the god his father raised and he abolished -- and "King Tut" is a 1920s
press abbreviation, which is why the least consequential pharaoh is the most
famous.

### Counts

1,640 entities unchanged. 544 → 549 sources. 389 → 390 cited. 54 → 70 entities
with `name_forms`.

## 0.23.0.0 — Names that carry an ideology (2026-08-09)

A third tranche, 43 to 54 entities. The first covered states, the second people;
this one covers names whose problem is not that they are foreign but that they
encode a viewpoint -- and one case where a name is wrong on purpose.

### The dataset had already taken a side without saying so

Its first region is called **West Asia**, not the Middle East. That is the
decolonised alternative, and until now it was an unexplained editorial choice
sitting in the region list.

"Near East" and "Middle East" both measure distance from London. Mahan coined
"Middle East" in the *National Review* in September 1902, arguing the British
should hold the Persian Gulf against Russia and Germany; a Middle Eastern
Studies article finds General Gordon using it two years earlier. Either way it
is a naval strategist's term for a buffer zone, adopted by the people it was not
about, and scholars from the region have criticised it as colonialist.

Both names are now on the entity as exonyms, with a caveat saying the dataset
files the region as West Asia for that reason -- and that this is itself a
choice rather than a neutral default.

### A mine, a colony, and Cecil Rhodes

The **Kabwe cranium** was found in 1921 at the Broken Hill mine in Northern
Rhodesia, and Woodward named the species *Homo rhodesiensis*. Roksandic and
colleagues proposed dissolving the taxon in 2021 partly because the name honours
a man who disenfranchised southern Africa's black population. Britannica records
that the "Rhodesian man" framing was used to argue African *Homo* lagged behind
Eurasian in acquiring modern anatomy.

Named three times for other people. The place is Kabwe, Zambia; the entity keeps
that and files the rest as `historical` and `rejected`.

Also: **Taforalt** carries its French colonial name Grotte des Pigeons as
historical, and **Tell es-Sultan** is restored as the endonym alongside the
biblical Jericho.

### A spelling frozen by rule

**Neanderthal is misspelled on purpose.** The Neander valley was *Neanderthal*
until Germany's 1901 orthographic reform turned *Thal* into *Tal*. The valley
changed; the species could not, because zoological nomenclature fixes the
spelling used at the time of naming. So *Homo neanderthalensis* preserves an
orthography Germany abolished 125 years ago, while the German common name went
to *Neandertaler*.

That is a fourth kind of name difference: neither exonym, nor rename, nor a
classification that lost, but a spelling held in place by a rule while the world
moved past it.

### Two labels that are arguments

The **Vietnam War** is *Kháng chiến chống Mỹ*, the resistance war against
America, if you are Vietnamese -- each side names it for the other. The **Age of
Discovery** is a discovery from one end only; the dataset already preferred Age
of Sail, and now says why, because the places discovered were without exception
already inhabited.

### Deliberately not changed

The Gupta **"Golden Age of India"**. The label is loaded and stays as a flat
alias. Adjudicating whether the period earns it needs the scholarship on that
specific debate, and recording an unsourced editorial verdict would be worse
than leaving it untyped.

### Counts

1,640 entities unchanged. 537 → 544 sources. 43 → 54 entities with
`name_forms`. All eight kinds remain in use; `rejected` grows from one to three.

## 0.22.0.0 — More formal and historical names (2026-08-09)

A second tranche, from 24 entities carrying `name_forms` to 43. The first
covered states; this one covers people, peoples, and one event whose name is the
entire historiographical dispute in miniature.

### A name that is an argument

**The Indian Rebellion of 1857** is now the sharpest naming case in the dataset,
because every available label is a verdict.

The British called it the **Sepoy Mutiny** -- which says it was a breach of
military discipline. Savarkar called it the **First War of Independence** in
1909 -- which says it was national liberation. S. N. Sen, writing the official
centenary history, concluded it began as a fight for religion and ended as a war
of independence. Punjabi historians object that the First Anglo-Sikh War has the
better claim to "first"; South Indian historians point to the Vellore Mutiny;
and the broad modern position is that it was not nationalist in the modern sense
at all.

Naming it is taking a side. The entity now says so, with the labels typed by who
used them and two competing readings recorded as such.

### Rulers who changed their own names

* **Octavian became Augustus** when the Senate conferred the title on 16 January
  27 BCE -- 17 January in the 1911 Britannica. He had considered "Romulus" and
  rejected it as too close to king. The dataset had "Octavian" as a flat alias,
  which flattened a deliberate political act into a spelling variant.
* **Amenhotep IV became Akhenaten** in his fifth regnal year, trading a name
  meaning "Amun is satisfied" for one meaning "effective for the Aten" -- while
  abolishing Amun. Britannica, ARCE and the Met put it in year five; UCL's
  Digital Egypt puts it in year six, and both are recorded.
* **Caligula never was Caligula.** He was Gaius. "Little boot" was a soldiers'
  nickname from his childhood in camp which the sources say he disliked. It
  stays as the display name, because that is how history knows him, and now
  carries a note saying what it is.

### Greek is why several Egyptians have two names

Cheops, Chephren and Ozymandias are Herodotus and Diodorus rendering Khufu,
Khafre and User-maat-re into Greek, and Europe inherited the Greek rather than
the Egyptian. Those are `exonym`, not spelling variants. Egypt itself gets
**Kemet**, "the black land", and the note that every European name for the
country descends from the Greek Aigyptos.

Also: the Ghana Empire called itself **Wagadu** -- "Ghana" was its ruler's
title; **Saba** entered European tradition as biblical Sheba, attached to a
queen its own sources do not name; and Troy is filed with **Hisarlik**, the
modern name excavation reports use precisely because it does not assume the
identification.

### A third kind of name change

**Java Man** and **Peking Man** are neither exonyms nor renames but
classifications that lost -- *Pithecanthropus erectus* and *Sinanthropus
pekinensis*, both folded into *Homo erectus*. `historical` with a note carries
them.

Honorifics -- Mahatma, Netaji, Quaid-e-Azam, Bangabandhu -- are filed as
`common` with a gloss rather than given a kind of their own. They are titles
rather than names and a reader searching any of them should land on the person,
but adding an `honorific` kind for four entities would be inventing vocabulary
ahead of need.

### What the screenshot caught

The alternatives panel is headed "Competing dates". For 1857 the alternatives
are readings of what the event *was*, so the heading contradicted the entity's
own date note two lines above it. It now reads "Competing views" when no
alternative carries a year.

### Counts

1,640 entities unchanged; this pass typed names rather than adding. 528 → 537
sources. 385 → 388 cited. 24 → 43 entities with `name_forms`.

## 0.21.0.0 — Formal and historical names (2026-08-09)

`name_forms` shipped last release with eight entities and two of its eight kinds
unexercised. `formal` and `historical` are now in use across 24 entities, and
all eight kinds appear in the data.

### Two more slash hacks, and a third

`Iran / Persia`, `Habsburg / Austria-Hungary` and `North Africa (Maghreb)` were
doing what `Haudenosaunee (Iroquois)` did: cramming a second name into the
display field because there was nowhere else to put it. All three are now single
names with the alternatives typed.

Not every parenthetical is that, which is worth stating because a first attempt
at a general test said otherwise. `Chalcolithic (Anatolia)` is the only thing
separating five sibling entities, and `BCE (Before Common Era)` is a gloss.
`Paleolithic (Old Stone Age)` genuinely is two names. Telling them apart needs
judgement, so the test guards named regressions instead of pretending to a rule
it cannot apply.

### The `historical` kind earns its date fields

* **Persia to Iran** is the crispest case in the dataset. Iran was always the
  endonym; Persia is the Greek exonym Europe used. In December 1934 the Iranian
  foreign ministry gave foreign governments three months' notice, and from 21
  March 1935 -- Nowruz -- asked them to use Iran. Unlike "Byzantine", this is
  not a scholarly reinterpretation: it is a government changing what other
  governments must call it.
* **The Holy Roman Empire** accreted its title in layers and the sources
  disagree on when. `sacrum imperium` under Barbarossa's chancery in 1157;
  `sacrum Romanum imperium` in 1184 by one account, 1254 by others; "of the
  German Nation" first in a document in 1474 and fixed at the Diet of Cologne in
  1512, though some references still call the longer form unofficial. The
  competing dates are recorded, not picked.
* **The Ottoman state** was Devlet-i Aliyye, "the Exalted State", from its
  founding, with "Osmaniyye" added during the Tanzimat. Western Europe called it
  the Turkish Empire, which it never called itself.
* **Germany** gets the treatment its example invited: `Deutschland` as the
  translation, `Bundesrepublik Deutschland` as the formal name, `Germany` as the
  common one, and `West Germany` as historical -- with the precision that
  reunification was legally an *accession*, so the Federal Republic continued as
  the same subject of international law while the GDR ceased to exist.

### What `formal` reveals about the two Chinas

For the PRC and the ROC the display name already *is* the formal name. What was
missing is the common one -- "China" and "Taiwan" -- and those short forms are
precisely what the sovereignty dispute is about. They are tagged `common` with a
note pointing at the `contested-existence` caveat rather than resolved. The
mechanism does not settle that dispute and should not look as though it has.

### Deliberately undated

**Austria-Hungary from 1867.** The Ausgleich date is not in doubt, but it was
not in this module's sourcing pass, and a `from` year is a date claim like any
other. Recorded as a `historical` form with a note and no year. A new test
enforces this generally: a dated name form must be able to cite the change.

### Counts

1,640 entities unchanged; this pass renamed and typed rather than added. 526 →
528 sources. 382 → 385 cited. 8 → 24 entities with `name_forms`.

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

