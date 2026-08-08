# Changelog

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
