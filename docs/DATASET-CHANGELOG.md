# Changelog

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
