# Changelog

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
