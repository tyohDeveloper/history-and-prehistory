# History & Prehistory — Dataset Gap Analysis (v2.1.0)

**Dataset:** `History-Picker--Data-v2.1.0-South-Asia-Expansion--Council-Review.zip`
**Built:** 2026-07-20 (session `6b4f4d2d`)
**Analyzed:** 2026-08-07
**Schema version:** 1.0.0 · **Dataset version:** 2.1.0
**Validation status at time of analysis:** `✓ OK — no errors. 0 warnings.` (re-run of bundled `validate.py`)

**Counts as measured, not as documented:**

| Metric | Value |
|---|---|
| Entities | 1,305 |
| `region` | 43 (11 top-level roots) |
| `era` | 248 |
| `period` | 343 |
| `reign` | 643 |
| `event` | 28 |
| Calendars | 21 |
| Themes | 16 |
| Reference frames | 37 |

Tier split: 337 foundational · 416 intermediate · 552 specialist.

> Note: the bundled `README.md` still describes the v2.0.0 state (1,123 entities, 28 reference frames, dataset 2.0.0). It is stale relative to `CHANGELOG.md` and the data. Fix before first commit — see §5.9.

---

## 1. Regional coverage: depth vs. sparsity

### 1.1 Top-level distribution

Entity counts by top-level root (all descendants, including the root):

| Root region | Entities | era | period | reign | event | Verdict |
|---|---:|---:|---:|---:|---:|---|
| East Asia | 452 | 37 | 257 | 154 | 0 | Over-weighted (see §1.2) |
| Africa | 220 | 36 | 25 | 152 | 0 | Deep but narrow (see §1.3) |
| Europe | 219 | 34 | 37 | 136 | 6 | Reasonable |
| South Asia | 208 | 29 | 13 | 159 | 6 | Reasonable (v2.1.0 target) |
| West Asia | 47 | 21 | 2 | 19 | 0 | **Severely thin** |
| Americas | 45 | 28 | 3 | 8 | 0 | **Severely thin** |
| Cross-Regional Empires | 26 | 10 | 0 | 3 | 12 | Structural bucket |
| Global | 25 | 17 | 3 | 0 | 4 | Structural bucket |
| Central Asia & the Steppe | 24 | 10 | 3 | 7 | 0 | **Thin** |
| Oceania | 20 | 13 | 0 | 2 | 0 | **Thin** |
| Southeast Asia | 19 | 13 | 0 | 3 | 0 | **Thin** |

Four regions (East Asia, Africa, Europe, South Asia) hold **1,099 of 1,305 entities — 84%**. The remaining seven roots share 206.

The council's v2.1.0 synthesis already names Americas and West Asia as the next two content gaps. This analysis confirms it and adds a sharper framing: **Southeast Asia, Oceania, and Central Asia are worse than they look**, because their entity counts are inflated by `era` nodes with no children at all (§3.1). Southeast Asia has 13 eras and 3 reigns; Oceania has 13 eras and 2 reigns. These are label-only regions — a user drilling into them hits a dead end on the second column.

### 1.2 East Asia is not deep, it is nengō-inflated

East Asia's 452 entities include **302 under Japan alone**, and of Japan's 257 `period` nodes the overwhelming majority are individual nengō era-names (Taika, Hakuchi, Shuchō, Taihō, … Reiwa). These are real and valuable — they are the payload for the Japanese-nengō calendar cross-reference — but they inflate the apparent depth of East Asia relative to every other region.

**Corrected view of East Asia:**

- Japan: 302 entities, dominated by ~250 nengō periods
- China: 137 entities
- Korea: 9 entities — **thinner than Oceania**

Korea at 9 entities is a genuine anomaly. The dataset models Gojoseon, Three Kingdoms, Unified Silla, Korean Empire, Japanese Colonial Rule, and Divided Korea as eras with essentially no rulers. Goryeo and Joseon — two of the longest continuous dynasties in the dataset's scope, with well-documented complete king lists — are underpopulated. Given that a `korean-regnal` calendar is already modeled in `calendars.json`, this is a cheap high-value fill.

**Vietnam** is similar: `vietnamese-nien-hieu` is a modeled calendar, but Southeast Asia has 3 reigns total across the whole root. The calendar has nothing to point at.

### 1.3 Africa is Egypt

Africa's 220 entities include **186 under Nile Valley & Northeast Africa**. The rest of the continent:

| Sub-region | Entities |
|---|---:|
| West Africa & Sahel | 13 |
| North Africa (Maghreb) | 5 |
| Southern Africa | 4 |
| Central Africa | 3 |
| East Africa | 2 |

East Africa at 2 entities is the single sparsest named sub-region in the dataset. Swahili coast city-states, Aksum (currently only reachable via the Nile Valley branch), and the Ethiopian Empire's 700-year span (2 rulers — see §3.2) all belong here.

### 1.4 Empty and near-empty region nodes

- **Anatolia** — 0 descendants. A region node that leads nowhere. Either populate (Hittites, Lydia, Byzantine Anatolia, Seljuk Rum, Ottoman core) or remove; a zero-child column is a UI dead end.
- **Intermediate Area & Caribbean** — 1 descendant.
- **Amazon & Southern Cone**, **Melanesia**, **Micronesia**, **Australia** — 2–3 descendants each.
- **North America** — 7 descendants, with no post-independence political history (no US presidents, no Canadian confederation).

### 1.5 Prioritized regional fill

| Priority | Target | Rationale |
|---|---|---|
| P0 | Americas post-independence | Largest absolute gap; 8 reigns for two continents; council-flagged |
| P0 | West Asia post-Sasanian | 21 eras / 19 reigns; Umayyad, Abbasid, Seljuk, Ottoman rulers all missing or stubbed |
| P1 | Korea (Goryeo, Joseon) | 9 entities; `korean-regnal` calendar has no targets |
| P1 | East + West Africa | 2 and 13 entities; Swahili coast, Aksum, Ethiopian lineage |
| P1 | Southeast Asia rulers | 13 eras / 3 reigns; `vietnamese-nien-hieu` calendar has no targets |
| P2 | Anatolia | Currently a zero-child node |
| P2 | Oceania, Central Asia | Structurally thin but lower user demand |

---

## 2. Time-period gaps

Century-by-century entity coverage (an entity counts toward every century it spans) shows three distinct problem zones.

### 2.1 The pre-3000 BCE cliff

Only **19 entities** in the whole dataset start before 3000 BCE, and 5 of them are the abstract Global eras (Paleolithic, Mesolithic, Neolithic, Bronze Age, BCE). Everything before ~3100 BCE is represented by five global label-nodes plus Aboriginal Australia, Jōmon, Predynastic Egypt, and Legendary China.

This is exactly the region the prehistory scope extension has to fill. See §4.

### 2.2 The 500–900 CE West Asian hole

West Asia's per-century count runs 4–5 through the Sasanian period and then goes to **literally zero for the 700s, 800s, and 900s CE**. The Umayyad and Abbasid Caliphates exist in the dataset but are filed under **Cross-Regional Empires**, not West Asia, and carry no rulers. A user selecting "West Asia" and scrubbing to 800 CE sees an empty region during the Islamic Golden Age.

This is a taxonomy problem as much as a content problem — see §5.6.

### 2.3 Thin centuries by region

| Region | Centuries with ≤2 entities | Note |
|---|---|---|
| West Asia | 700s, 800s, 900s CE (zero); 1000s–1300s CE (zero) | Post-Sasanian to Ottoman is a 900-year void |
| Southeast Asia | Everything before 1 CE (zero) | Region starts at Funan, 68 CE |
| Central Asia | 1 CE – 500 CE (0–2); post-1700 (0–1) | Sogdians, Kushans, Timurids, Khanates all missing or stubbed |
| Oceania | Everything before 1500 BCE (zero) | Lapita is the earliest node; Aboriginal Australia sits under a separate branch |
| Americas | Post-1900 (3 entities) | No 20th-century American political history at all |
| Europe | 500s CE (8) | Post-Roman / pre-Carolingian trough |
| Africa | 1 CE – 500 CE (4–7) | Post-Ptolemaic, pre-Islamic North and East Africa |

### 2.4 The contemporary drop-off

The 2000s CE column has 35 entities total, and 10 of those are South Asian (because South Asia got a full PM list in v2.1.0). Every other region's living political history is one or two era nodes deep. Post-2000 coverage is a documented council P2, and the imbalance is now visible: South Asia's modern coverage is roughly 3× any peer region's.

### 2.5 Event coverage is lopsided

28 events total. **12 are filed under Cross-Regional Empires, 6 under South Asia, 6 under Europe, 4 under Global — and 0 under East Asia, Africa, West Asia, Americas, Central Asia, Southeast Asia, or Oceania.**

There is no Meiji Restoration event, no Taiping Rebellion, no fall of Tenochtitlan, no Battle of Adwa, no Haitian Revolution, no Suez Crisis. The event layer is essentially a Euro-Atlantic and South Asian layer. For a picker whose selling point is "what else was happening?", this asymmetry is more user-visible than the entity counts.

---

## 3. Incomplete ruler lineages

### 3.1 Structural: 145 of 248 eras have no children

**58% of era nodes are leaves.** A user who drills Region → Era hits a dead end more often than not. Many are legitimately leaf-shaped (Axial Age, Migration Period, Late Antiquity — conceptual eras with no ruler list). But a large number are polities with well-known, easily-sourced ruler sequences:

Pre-1000 CE: Shang Dynasty, Ur III, Elam, Median Empire, Seleucid Empire, Three Kingdoms of Korea, Unified Silla, Rashidun Caliphate, Umayyad Caliphate, Gojoseon, Kassite Babylon, Funan, Srivijaya, Champa, Ghana Empire, First Turkic Khaganate, Teotihuacan, Moche, Wari, Tiwanaku.

Post-1000 CE: Kanem–Bornu, Qajar Dynasty, Pahlavi Dynasty, Sokoto Caliphate, German Empire, Weimar Republic, Nazi Germany, Korean Empire, Republic of China, People's Republic of China, Russian Federation, Islamic Republic of Iran, Mexico (independent), Commonwealth of Australia, New Zealand, Kingdom of Tonga, Sultanate of Zanzibar, Dutch East Indies, Post-War Germany, Divided Korea, Republic of Indonesia.

Separately, **282 of 343 `period` nodes have no reign children** — though the great majority of those are Japanese nengō, which legitimately have no ruler layer beneath them.

### 3.2 Measured lineage gaps

Parents holding ≥2 reign children were checked for chronological holes >25 years, at the head (parent start → first ruler), between consecutive rulers, and at the tail (last ruler → parent end). 34 parents show gaps. The worst:

| Parent | Root | Rulers | Parent span (yr) | Gap (yr) | Where |
|---|---|---:|---:|---:|---|
| Kingdom of Macedon | Europe | 2 | 662 | 626 | Head −808→−359; tail −323→−146 |
| Ethiopian Empire | Africa | 2 | 704 | 619 | Head 1270→1889 |
| Khmer Empire (Angkor) | SE Asia | 2 | 629 | 555 | 802→1113, 1150→1181, 1218→1431 |
| Ottoman Empire | Cross-Regional | 2 | 623 | 547 | 1299→1451, 1481→1520, 1566→1922 |
| Kingdom of Mysore | South Asia | 2 | 548 | 510 | 1399→1761; 1799→1947 |
| Pallava Dynasty | South Asia | 3 | 622 | 489 | 275→600, 668→731, 796→897 |
| Mali Empire | Africa | 2 | 435 | 390 | 1255→1312; 1337→1670 |
| Israel and Judah | West Asia | 2 | 464 | 385 | Head; tail to 586 BCE |
| Byzantine Empire | Europe | 35 | 1123 | 363 | 330→491, 802→867, 1025→1068, 1204→1261 |
| Satavahana Empire | South Asia | 5 | 450 | 314 | −170→78 is the big one |
| Pala Empire | South Asia | 3 | 411 | 311 | Tail 850→1161 |
| Sasanian Empire | West Asia | 4 | 427 | 261 | 270→531 |
| Russian Empire | Europe | 2 | 196 | 158 | 1725→1762; 1796→1917 |

**The Ottoman Empire is the standout defect.** Three rulers (implied Osman-era, Mehmed II, Suleiman) across 623 years, with 1566→1922 — the entire late Ottoman period including Tanzimat, Abdul Hamid II, and the collapse — unrepresented. It is also mis-parented under Cross-Regional Empires rather than West Asia (§5.6).

**Byzantine Empire** is the best-populated lineage in the dataset (35 rulers) and still has four visible holes, including the Nikaian exile 1204–1261. It is the useful benchmark: 35 rulers over 1,123 years is roughly the density a "complete" lineage looks like in this schema.

### 3.3 Density benchmark

Using Byzantine (35 rulers / 1,123 yr ≈ 1 per 32 yr) and Ptolemaic Egypt (18 / 302 ≈ 1 per 17 yr) as the achieved standard, most flagged lineages above are at 1 ruler per 200–350 years. A pragmatic completion target is **one ruler node per ~30 years of polity span** for any polity marked `foundational` or `intermediate`, with `specialist` polities allowed to stay sparse.

### 3.4 Loose reigns and kind overloading

Carried forward from the council review and confirmed here: `reign` is doing duty for monarchs, prime ministers, viceroys, governors-general, revolutionaries, poets, and religious founders. Guru Nanak, Kabir, and Tagore hang directly off the `south-asia` region node as `reign` entities with no intervening era or period — a type-grammar violation that will render as a category jolt in a Miller column. The optional `subkind` field the council recommended is the right fix and should land before the next region is authored.

---

## 4. Where prehistory / anthropology attaches

The scope extension calls for pre-writing periods on radiocarbon-BP ranges with validity flags. The current tree gives it almost nothing to attach to: the entire Paleolithic is one `Global` node spanning −3,300,000 to −10,000, and it is childless.

### 4.1 The reference-frame problem comes first

`start_year`/`end_year` are typed `integer` in proleptic Gregorian. Paleolithic already stores `-3300000`. That works arithmetically but conflates three incompatible dating regimes on one axis:

1. **Calendar years** (post-writing, absolute, ±0–1 yr)
2. **Calibrated radiocarbon** (cal BP, ~50,000 BP ceiling, asymmetric confidence intervals)
3. **Uncalibrated / non-radiometric** (K-Ar, OSL, ESR, biostratigraphy — the Oldowan/Acheulean range, where "±" is measured in tens of thousands of years)

`date_precision: approx` — currently applied to 1,246 of 1,305 entities, i.e. nearly everything — carries no information at all at this scale. Before prehistory data is authored, the schema needs a way to say which regime a date came from. See §5.1.

### 4.2 Proposed attach points by region

| Root region | Attach under | Candidate prehistory nodes |
|---|---|---|
| **Global** | `Paleolithic` (currently childless) | Oldowan (2.6 Ma), Acheulean (1.76 Ma), Middle Paleolithic / Mousterian, Upper Paleolithic, Aurignacian, Gravettian, Solutrean, Magdalenian; then Mesolithic and Neolithic already exist as siblings |
| **Africa** | New sibling era before `Ancient Egypt` | East African Rift hominin sequence, Olduvai, Omo, Middle Stone Age, Howiesons Poort, Later Stone Age, Sahara pastoral / Green Sahara, Nabta Playa → hands off to Predynastic Egypt |
| **West Asia** | New era before `Elam` | Natufian, Pre-Pottery Neolithic A/B, Göbekli Tepe, Çatalhöyük, Halaf, Ubaid → hands off to Sumer |
| **East Asia** | Beside `Jōmon Period` (exists, childless) | Jōmon Incipient→Final sub-phases; Chinese Neolithic: Peiligang, Yangshao, Hongshan, Longshan, Liangzhu → hands off to `Legendary & Neolithic China` |
| **South Asia** | New era before `Indus Valley Civilization` | Mehrgarh, Bhirrana, Early Harappan / Ravi phase → hands off to IVC |
| **Europe** | New era; Europe currently starts at 1300 CE at root level | Neanderthal Europe, Aurignacian/Gravettian cave art (Chauvet, Lascaux, Altamira), LBK, Corded Ware, Bell Beaker, Megalithic (Stonehenge, Newgrange) |
| **Americas** | New era before `Norte Chico` | Beringia crossing, Pre-Clovis (Monte Verde), Clovis, Folsom, Archaic, Paleoindian → hands off to Norte Chico / Olmec |
| **Oceania** | Extend `Aboriginal Australia` (childless, −65,000 to 1788) | Sahul colonization, Madjedbebe, Lake Mungo; and pre-Lapita Near Oceania (Papuan settlement ~50 ka) which is currently missing entirely |
| **Southeast Asia** | New era; region currently starts at 68 CE | Hoabinhian, Homo floresiensis, Ban Chiang, early rice domestication |
| **Central Asia** | New era; region currently starts at 1206 CE | Denisova Cave, Botai horse domestication, Andronovo, Afanasievo, BMAC |

**Two structural notes:**

- **Aboriginal Australia's placement is wrong for this extension.** It is currently an Oceania-level era spanning −65,000 to 1788 with no children, sitting alongside Lapita and Polynesian Voyaging. Once prehistory is real content, Sahul settlement needs to be a first-class prehistory node, not a leaf.
- **The Holocene handoff to Deep Time.** The family plan gives `earth-cosmos.tyoh.app` a one-directional inbound link to History at the Holocene boundary (~11,700 BP). The dataset currently has no node marking that boundary. `Mesolithic` (−10,000) is close but not the boundary, and it is a cultural label, not a geological one. **Recommend an explicit Holocene-start node** (or a documented boundary marker in the reference-frames file) so the cross-app link has a stable target that does not shift when Mesolithic dates are refined per-region.
- **"Mesolithic" is Eurocentric as a global node.** It has no meaning in the Americas, sub-Saharan Africa, or Australia. If prehistory becomes real content, `Global → Mesolithic` should either be scoped to Eurasia or reframed as "Epipaleolithic / Mesolithic (Eurasia)".

### 4.3 What the picker needs on top of the data

- **BP ↔ CE toggle** on the readout (already scoped in the wiki).
- **Validity flag** for pre-calibration dates, distinct from the existing `date_precision` enum.
- **Log-ish or piecewise timeline scale.** A linear timeline that includes the Oldowan makes all of recorded history a sub-pixel sliver. The Deep Time app solves this with a log-seconds axis; History needs at minimum a piecewise-compressed scrubber, or the prehistory branch will be unusable in the same widget as the historical branch. **This is a UI decision that should be settled before prehistory data is authored**, because it may change how prehistory nodes want to be bucketed.

---

## 5. Schema issues and inconsistencies

### 5.1 The schema is ahead of the data (council's central finding, quantified)

Field population across all 1,305 entities:

| Field | Populated | Note |
|---|---:|---|
| `id`, `kind`, `name`, `parent_id`, `start_year`, `end_year`, `tier` | 1,305 | Required; fine |
| `date_precision` | 1,297 | But 1,246 are `approx` — near-zero information |
| `summary` | 573 (44%) | See §5.3 |
| `native_name` | 322 | 248 of them are nengō periods |
| `calendar_ids` | 267 | 256 are East Asian — see §5.4 |
| `aliases` | 47 | |
| `date_note` | 33 | |
| `allow_outside_parent_dates` | 27 | Correctly used where present |
| `cross_parent_ids` | 11 | |
| `end_precision` / `start_precision` | 8 / 7 | |
| `start_year_min/max`, `end_year_min/max` | 3 / 3 / 2 / 2 | Essentially unused |
| `misconceptions` | 3 | |
| `capital` | 1 | |
| `links` | **1** | |
| `sources` | **0** | |
| `themes`, `region_tags`, `successor_ids`, `predecessor_ids`, `redirect_ids`, `capitals`, `notable_figures` | **0** | Defined, never used |

Seven schema fields have zero instances dataset-wide. The council correctly diagnosed the mechanical cause: the `R()` and `P()` builder helpers in the extension modules don't accept these fields, so authors physically cannot populate them without editing the helpers. **Fix the helpers before authoring prehistory**, or prehistory will accrue the same debt — and prehistory is the branch that most needs `date_note`, `*_year_min/max`, and `sources`.

### 5.2 `sources: []` is empty across the entire dataset — and it blocks a stated product requirement

The standalone-HTML5 standard says: "Every non-obvious value in the app should trace back to a source listed here [the sources page]." With `sources` unpopulated on all 1,305 entities, that page cannot be generated from the data. It would have to be hand-maintained and would drift immediately.

This matters more for prehistory than for history: a Ramesses II date can be waved at as common knowledge; an Oldowan start date cannot. **Recommend making `sources` required (min 1) for any entity with a prehistory subkind**, even if it stays optional elsewhere.

### 5.3 Summary coverage is inverted relative to tier

| Kind | With summary |
|---|---|
| `event` | 28 / 28 (100%) |
| `era` | 157 / 248 (63%) |
| `reign` | 314 / 643 (49%) |
| `period` | 68 / 343 (20%) |
| `region` | **6 / 43 (14%)** |

Regions are the **first thing a user sees** in the leftmost Miller column and the least documented kind in the dataset. 37 of 43 region nodes have no summary at all. That is the cheapest single UX win available — 37 short paragraphs.

Cross-checking against tier: a meaningful number of `foundational` entities lack summaries. **Recommend a validator rule: `tier: foundational` implies `summary` required.** That is enforceable, small, and matches the novice-first framing in the family wiki.

### 5.4 `calendar_ids` is an East Asia–only feature in practice

| Root | Entities with `calendar_ids` |
|---|---|
| East Asia | 256 / 452 |
| Cross-Regional | 5 / 26 |
| Europe | 2 / 219 |
| Americas | 2 / 45 |
| Africa | 1 / 220 |
| West Asia | 1 / 47 |
| **South Asia** | **0 / 208** |
| Central Asia, SE Asia, Oceania, Global | 0 |

The multi-calendar readout is named in the wiki as "the strongest user-facing feature." It currently only fires meaningfully in Japan. South Asia — freshly expanded, and the region where Vikram Samvat, Saka, Hijri, and Bengali San are most relevant — has zero. Africa has one, despite `ethiopian` and `egyptian-regnal` being modeled calendars. `korean-regnal`, `vietnamese-nien-hieu`, `juche`, `maya-long-count`, `aztec-calendar`, `roman-auc`, `olympiad`, `byzantine-am`, and `french-republican` are all defined in `calendars.json` with few or no entities pointing at them.

This is the highest-leverage backfill in the dataset: it makes an already-built feature work, with no new tree content.

### 5.5 `date_precision: approx` is load-bearing and meaningless

1,246 of 1,305 entities are `approx`. The enum offers `year`, `decade`, `century`, `millennium`, `approx`, `traditional`, `disputed`, `unknown`, `exact` — and the data uses four values, with one of them at 95%. Modern reigns with exact dates (Modi, Reiwa, Weimar) are tagged the same as Narmer.

Two consequences: the UI cannot render precision differentially because the field doesn't differentiate, and prehistory has nowhere to express its wildly different uncertainty scale. **Recommend an authoring pass mapping the obvious cases to `exact`/`year` (anything post-1500 with a documented date), plus a new value or parallel field for radiometric/`uncalibrated` prehistory dating.**

### 5.6 `Cross-Regional Empires` is absorbing things that belong in regions

The Ottoman Empire, Umayyad Caliphate, Abbasid Caliphate, and Rashidun Caliphate are all filed under Cross-Regional Empires. This is defensible in the abstract but produces the West Asia 700–1300 CE void described in §2.2: the region a user would actually click is empty during the period those polities dominated it.

The schema already has `cross_parent_ids` for exactly this, and it is used only 11 times. **Recommend re-parenting these into their regional home and using `cross_parent_ids` to keep the Cross-Regional placement**, rather than the reverse. Same argument for Mongol Empire (currently Central Asia, with 3 rulers and a 1259→1368 tail gap).

Cross-Regional Empires also holds 12 of the dataset's 28 events, including World War I, World War II, the Black Death, and the Moon Landing. It is functioning as a catch-all rather than a category.

### 5.7 Duplicate display names across siblings

Confirmed duplicates include Shōwa ×2, Jōwa ×2, Jōgen ×2, Eishō ×2, Kōwa ×2, Tenshō ×2, Kōji ×2, Jōō ×2, Kōan ×2, Enkyō ×2, plus Emperor Taizong ×2 and Emperor Gaozong ×2. These are historically correct — nengō names were reused, and Chinese temple names recur across dynasties — but they are indistinguishable in a Miller column and in search results.

The council recommended a validator rule for duplicate display names across siblings. This analysis adds: **the duplicates are mostly not siblings** (different centuries, different parents), so the sibling-scoped rule won't catch them. The real need is a **disambiguating display suffix** in the UI (`Shōwa (1312)` vs `Shōwa (1926)`, `Emperor Taizong (Tang)` vs `Emperor Taizong (Song)`), driven from parent + start year. That is a UI fix, not a data fix, but it needs a schema affordance if the disambiguator should be author-controlled rather than derived.

### 5.8 Named-year ordering in `calendars.json`

The council flagged Japanese Engi/Kanpyō as out of order in the nengō `named_years` sequence, and noted the validator's docstring promises ordering/overlap checks it does not implement. Unverified in this pass beyond confirming the validator does not run the check. Worth fixing as part of the validator work, since the nengō sequence is the one place the calendar layer cross-references entity IDs directly.

### 5.9 Documentation drift

`README.md` describes dataset 2.0.0: 1,123 entities, 28 reference frames, and a `fetch()`-based loading example. Three problems for a clean first commit:

- The counts are stale (actual: 1,305 entities, 37 frames, dataset 2.1.0).
- The loading example uses `fetch("./data/entities.json")`, which **violates the standalone-HTML5 standard** — no runtime `fetch()`, and it would be blocked by the CSP `connect-src 'none'` the standard requires, and would fail outright from `file://`. The data must be inlined at build time. Fix this before it becomes the pattern a coding agent copies.
- The `entity.schema.json` sets `additionalProperties: false`, so adding `subkind` requires a schema bump, not just an authoring convention.

### 5.10 What is clean

For balance — these were checked and are in good shape:

- **Referential integrity:** zero broken `parent_id` / `cross_parent_ids` references; `validate.py` passes with 0 errors, 0 warnings.
- **ID convention:** consistent dotted-path lowercase (`europe.mediterranean`, `south-asia.harsha.harshavardhana`). No uppercase, no underscores, no collisions.
- **Date containment:** zero children fall outside their parent's date range without the `allow_outside_parent_dates` flag. The 27 flagged cases are all legitimate.
- **Tree depth:** stays within the 4-column Miller limit the v2.0.0 architecture assumed.

---

## 6. Recommended sequence before first commit

1. **Regenerate `README.md`** against the actual v2.1.0 data, and remove the `fetch()` example in favor of a build-time inlining note. (§5.9)
2. **Extend `R()`/`P()` builder helpers** to accept `date_note`, `*_year_min/max`, `*_precision`, `links`, `sources`, `calendar_ids`, `subkind`. Nothing else in this list is authorable until this lands. (§5.1)
3. **Add optional `subkind`** to `entity.schema.json` (requires handling `additionalProperties: false`) and bump schema to 1.1.0. (§3.4, §5.9)
4. **Add a prehistory dating-regime field** — the single most important schema decision for the scope extension. (§4.1, §5.5)
5. **Validator rules:** foundational⇒summary, named-year ordering, parent cycles, duplicate display names (scoped correctly per §5.7).
6. **Then** author prehistory, with `sources` required on prehistory nodes.

Content backfill (Americas, West Asia, Korea, Africa, calendar_ids, region summaries) is P1 and can proceed in parallel with the prehistory branch, but should not precede items 2–4.

---

## 7. Underspecified decisions worth confirming

These come out of the wiki context and this analysis. Each would change downstream work if answered differently.

### 7.1 Timeline scale across a 3.3-million-year range

The picker is scoped to include the Oldowan and the Reiwa era in one tree. On a linear axis, all of recorded history is one pixel. The wiki says the Deep Time app owns the log-seconds axis and History owns the calendar/BP axis — but History's own range now spans six orders of magnitude. **Options:** (a) piecewise-compressed scrubber with a visible scale break, (b) the timeline switches to log mode automatically when a prehistory node is selected, (c) prehistory is a separate top-level mode with its own scrubber. This should be settled before prehistory nodes are authored, since it affects bucketing. **Recommend (a)** — one widget, one mental model, explicit scale break.

### 7.2 The Holocene handoff target

The family plan gives Deep Time a one-directional inbound link to History at the Holocene boundary, but no dataset node marks it. Should this be an explicit entity (a `boundary` kind? a reference frame?), or a hardcoded URL fragment on the Deep Time side? A hardcoded fragment couples the two apps' release cycles.

### 7.3 Repo shape: monorepo vs. per-app

The family wiki says **monorepo with `apps/<name>` subdirectories**, shared standards at root. The standalone-HTML5 starter checklist says "create the GitHub repo (public, MIT)" per app, and the subdomain table implies independent deploys. These are reconcilable but not identical. Since History ships first and the launcher, Units migration, Earth-Cosmos, and Decay all come later, **the first commit's directory layout depends on which it is.** Confirm before repo creation.

Related: existing `tyohDeveloper` repos are all per-project and public. No `history` repo exists yet — confirmed. The GitHub tooling here defaults new repos to private; the standard says public MIT. Worth an explicit call.

### 7.4 Whether the picker owns any calendar conversion at all

The wiki says the OmniUnit calendar layer absorbed date conversion, and the distinctive work here is the picker, the multi-script input grammar, and prehistory. But the "multi-calendar readout" is named as the strongest user-facing feature and requires conversion. **Does History bundle its own copy of the Temporal polyfill and JDN code, or is that a shared package in the monorepo?** Duplicating it means two codebases drifting; sharing it means the monorepo needs a real build-time package boundary, which raises the bar on the toolchain. Given the standalone-HTML5 "everything inlined" constraint, a shared source package that gets inlined per-app seems right, but this is a real decision.

### 7.5 `subkind` — additive field or `kind` enum expansion?

The council settled on optional `subkind`. Worth confirming it is genuinely additive, because `entity.schema.json` has `additionalProperties: false` and the picker's column rendering keys off `kind`. If `subkind` affects glyphs and column grouping, it is not purely additive to the UI even if it is to the schema.

### 7.6 Prehistory validity flags — new enum value or separate field?

`date_precision` already has nine values and is 95% `approx`. Prehistory needs to express dating *method* (¹⁴C calibrated, ¹⁴C uncalibrated, K-Ar, OSL, ESR, typological) and *asymmetric confidence*, which are orthogonal to precision. **Recommend a separate `dating_method` field plus asymmetric bounds via the existing `*_year_min/max`**, rather than overloading `date_precision`. Confirm.

### 7.7 How much of the Cross-Regional Empires re-parenting to do now

§5.6 recommends moving Ottoman and the Caliphates into West Asia with `cross_parent_ids` back to Cross-Regional. IDs are identity in this dataset, and `redirect_ids` exists precisely for this but has zero instances — meaning the redirect mechanism has never actually been exercised. Re-parenting before the first commit is cheap (no external permalinks exist yet); doing it after is a redirect-policy problem. **Recommend doing it now, pre-repo**, but it is a scope call.

### 7.8 Novice framing vs. the specialist tier

552 of 1,305 entities are `specialist` — 42% of the dataset is hidden by default under the progressive-disclosure model. For `period` specifically it is 247 of 343 (72%), because nengō are specialist. Confirm that the default view genuinely reads as complete to a novice with 42% suppressed, rather than looking sparse. Worth a design pass on what the default-tier tree actually looks like per region — East Asia in particular loses most of its apparent depth.

### 7.9 Scope of the "one ruler per ~30 years" completion target

§3.3 proposes a density benchmark. Whether that becomes a validator warning (mechanically enforced, generates a to-do list) or an authoring guideline (softer, no CI noise) is a call. A warning-level check would surface all 34 gap-flagged lineages automatically, which is useful, but would fail loudly on legitimately sparse specialist polities unless it is tier-scoped.

---

## Sources

Analysis derived from the dataset bundle and its accompanying council review, both from session `6b4f4d2d` (2026-07-20):

- `data/entities.json`, `data/calendars.json`, `data/themes.json`, `data/reference-frames.json` (v2.1.0)
- `schemas/entity.schema.json` (schema 1.0.0)
- `validate.py` (re-run 2026-08-07: 0 errors, 0 warnings)
- `CHANGELOG.md` — v2.1.0 South Asia expansion record
- `review/synthesis-v2.1.md` — model-council synthesis (GPT-5 data model · Opus UX · Gemini completeness)
- `README.md` — noted as stale at v2.0.0

Project context from the programming project knowledge wiki: `projects/tyoh-app-tools-family`, `projects/historical-time-and-date-tools`, `concepts/coding-standards-standalone-html5`.

Repository state verified against `github.com/tyohDeveloper` on 2026-08-07: no History repo exists; [OmniUnitConverter-Calculator](https://github.com/tyohDeveloper/OmniUnitConverter-Calculator) is the reference implementation.
