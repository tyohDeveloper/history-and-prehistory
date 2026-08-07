# History Picker — Model-Council Synthesis (v2.1.0)

**Date:** 2026-07-20
**Dataset:** v2.1.0 · 1,305 entities · 21 calendars · 16 themes · 37 anchors
**Reviewers:** GPT-5 (data model) · Opus (UX/UI) · Gemini (completeness/bias)
**Prior council reports:** `gpt5-datamodel.md`, `opus-ux.md`, `gemini-completeness.md`, `synthesis.md` (v2.0.0)
**This-round reports:** `gpt5-datamodel-v2.1.md`, `opus-ux-v2.1.md`, `gemini-completeness-v2.1.md`

---

## Headline verdict

**The South Asia gap is closed.** All three reviewers agree v2.1.0 does what it was supposed to do: South Asia went from a 27-entity token region to a 206-entity peer of Europe (249) and Africa (219), with balanced coverage across Ancient, Medieval, Sultanate/Mughal, Colonial, and Independence periods. Zero validation errors, zero warnings, no schema drift, no depth increase beyond the 4-column limit the v2.0.0 architecture was designed for. **No architectural reversal — every P0 from v2.0.0 still holds.**

But the reviewers also converge on one uncomfortable finding: **the v2.1.0 data half-adopts its own new schema.** The 2.0.0 review added `date_note`, `start_year_min/max`, `links[]`, `redirect_ids[]`, and endpoint precision — v2.1.0 barely uses any of them. Of 206 South Asian records, only 9 have `date_note`, only Ashoka has date ranges, zero have `links[]`, zero have `redirect_ids[]`, and zero have `sources`. The schema is ahead of the data. Every reviewer flags this in different words.

Beyond that, three genuinely new issues emerge — all of them small, none blocking:

1. **Kind overloading.** `reign` is now used for monarchs, prime ministers, viceroys, revolutionaries, poets, and religious founders. GPT-5 wants `subkind`; Opus wants the UI to render distinct glyphs and let the type grammar bend gracefully.
2. **The 32-child `south-asia` column** is the widest region column in the dataset. Opus's answer (in-column headers, not new column steps) is cheap and correct.
3. **Modern-leader multi-tenure bugs.** Sheikh Hasina and Benazir Bhutto had two terms each — both were modeled as one. This is now **fixed** (1,305 entities, up from 1,303).

The reviewers disagree cleanly on **what to do next**: GPT-5 wants schema/model fixes; Opus wants UI polish before another region; Gemini wants to expand the Americas. The right order — laid out below — is fix the small data bugs now, ship the small UI polish next, then decide between more content and more model.

---

## Where the reviewers agree

| Finding | GPT-5 | Opus | Gemini |
|---|---|---|---|
| **Gap closed; no architecture reversal needed** | ✓ | ✓ | ✓ |
| **`reign` kind is overloaded** (poets, PMs, viceroys, founders modeled as reigns) | Wants `subkind` | Wants kind glyphs (▣ ◆ ● ◇) + mixed-kind column layout | Doesn't flag — implicit in "phrasing concerns" |
| **Missed features from v2.0.0 (date ranges, `date_note`, `links[]`, `sources`)** | Central complaint | Mostly a UX-side observation on `calendar_ids` | Recommends adding `links[]` for EIC / Bahadur Shah II / 1857 |
| **Sheikh Hasina / Benazir single tenure is wrong** | Flagged as P0 data bug | — | — |
| **Loose reigns under region node (Nanak/Kabir/Tagore)** | Type grammar violation | Category jolt in the column view | — |
| **`south-asia` column needs sub-grouping** | Suggests chronological shelves + redirect policy | Suggests in-column headers (no new column step) | — |
| **EIC needs a cross-link to Britain** | Suggests `links[{type: part_of, entity_id: europe.western.england}]` | — | Suggests `cross_parent_id: europe.britain.empire` |
| **Hagiographic phrasing** (Samudragupta "Napoleon of India"; Baji Rao "undefeated in 41 battles") | — | — | Flagged; **fixed this round** |
| **`allow_outside_parent_dates` is well-used but under-annotated on ancient dynasties** | Ancient chronology under-annotated | Ghost-extension rendering pattern for the overhang | — |

---

## Where the reviewers disagree — and how to resolve

### 1. Should the `south-asia` column be re-shaped?

- **GPT-5:** intermediate chronological buckets (`ancient`, `classical`, `medieval`, ...) as real path segments, but *only after* redirect policy is tested (path IDs are identity).
- **Opus:** in-column non-selectable small-caps headers derived from `start_year` in a `regionGroups` config; **no schema or ID change**. This is the OmniUnit "SI BASE UNITS / DERIVED UNITS" idiom reused.
- **Gemini:** doesn't take a side.

**Resolution:** ship Opus's answer now. It's zero-data-change, matches the app's existing visual grammar, keeps IDs stable, and can be upgraded later to a real `display_group` field or path-level buckets *once* the redirect policy exists. GPT-5's structural rework is the right eventual end state but not the right next step.

### 2. Fix `kind` overloading now, or defer?

- **GPT-5:** add `subkind` **before** expanding another region — otherwise the debt compounds. Minimum values: `polity`, `dynasty`, `office_series`, `office_tenure`, `person`, `cultural_figure`, `religious_figure`, `interregnum`, `colonial_administration`.
- **Opus:** live with it in the model; render distinct glyphs in the UI (`▣` era, `◆` period, `●` reign, `◇` event). The "loose reign under region" pattern is a smell, but a UI-side glyph handles it.
- **Gemini:** silent.

**Resolution:** middle path. Add `subkind` as an **optional** field in the entity schema now (so new authoring can start using it), don't require it, don't backfill v2.1.0 wholesale. Opus's UI-side glyph fix is what actually reaches users and can ship immediately; `subkind` starts paying off the moment the next region is authored.

### 3. What's the next iteration's primary focus — data model, UX, or new content?

- **GPT-5:** model. `subkind`, date-uncertainty coverage, `links[]` population, redirect policy, validator gaps — all before another region.
- **Opus:** UX. In-column headers, native-script line, transliteration search fold, mobile breadcrumb, Independence node layout — all before another region.
- **Gemini:** content. Americas is now the biggest gap (44 entities, no post-independence coverage); after that West Asia (post-Sasanian, Islamic Golden Age, later Ottomans).

**Resolution:** all three are correct, but the order matters. **Model gaps that would break future authoring** come first (Opus's transliteration fold and font stack are also authoring-blocking, so they group with it). **Then** content expansion. If you expand Americas *before* `subkind` and the missing `links[]` habit, US Presidents and Latin American revolutionaries will accrue the same debt v2.1.0 accrued.

---

## Corrections applied in this session (post-council)

Small enough to fix now rather than defer to v2.2:

- **Duplicate slug `south-asia.harsha.harsha`** → renamed to `south-asia.harsha.harshavardhana` (breadcrumb clarity).
- **Sheikh Hasina modeled only for 1996–2001** while summary claimed longest-serving → split into `hasina` (1st term, 1996–2001) and `hasina-2` (2nd term, 2009–2024, forced from office in 2024 popular uprising).
- **Benazir Bhutto modeled only for 1988–1990** while summary said twice PM → split into `benazir` (1st term) and `benazir-2` (2nd term, 1993–1996).
- **"Napoleon of India" epithet for Samudragupta** → replaced with a neutral description referencing the Allahabad Prashasti.
- **"Undefeated in 41 battles" for Baji Rao I** → toned to "highly successful general who expanded Maratha power."

Dataset count: **1,305 entities**, zero errors, zero warnings.

---

## Consolidated recommendation for v2.2

### P0 — do before authoring the next region

**Model (from GPT-5):**
1. Add optional `subkind` field to entity schema. Don't require or backfill. Start using it in new authoring: `office_tenure` for PMs/viceroys, `cultural_figure` for Nanak/Kabir/Tagore, `interregnum` for Suri.
2. Upgrade the extension helpers (`R()` and `P()`) to accept `date_note`, `start_year_min/max`, `end_year_min/max`, `start_precision`, `end_precision`, `links`, and `allow_outside_parent_dates`. The mechanical cause of the v2.1.0 under-annotation was that the helpers didn't accept these fields.
3. Fill the validator gaps its docstring already promises: named-year ordering/overlap (Japanese Engi/Kanpyō is out of order), parent cycles, and duplicate display-name/search-name across siblings.

**UX (from Opus):**
4. In-column small-caps group headers for `south-asia` (derive from `start_year` in a UI-side `regionGroups` config). No schema change.
5. Native-script line in the readout with its own line-box (`line-height ≈1.7`), `dir="auto"`, `lang=` per entity, and tabular-figures scoped to Latin year columns only. Zero-dependency OS-first font stack (no bundled webfonts).
6. Search fold-normalization: hyphens/apostrophes/spaces/doubled letters/common vowel variants (`Ala-ud-din` ≡ `Alauddin`; `Aurangzeb` ≡ `Aurangzib`).
7. Independence node: PM/Leader buckets as full column steps (not inline "N more"), with in-column headers for the mixed-kind children (`FOUNDERS` / `HEADS OF GOVERNMENT` / `KEY EVENTS`).

### P1 — high value, do next

**Data (GPT-5 + Gemini):**
1. Populate `links[]` in South Asia. Highest-value cases: `east-india-company` ↔ `europe.western.england` (typed `part_of`), Indo-Greek ↔ Hellenistic, Bahadur Shah II ↔ Burma (exile), Suri ↔ Mughal (`interregnum_of`), Bangladesh Liberation ↔ Pakistan, and same-person links for Humayun ×2, Indira Gandhi ×2, Benazir ×2, Hasina ×2.
2. Add date uncertainty to ancient South Asian entries: Bindusara accession, Kanishka, late Mauryas, Satavahana rulers, early Gupta boundaries. Ashoka is the template.
3. Add `calendar_ids` to South Asian entries (Hijri for Sultanate/Mughal/Pakistan/Bangladesh; Vikram Samvat and Saka for Hindu-era polities; Bengali San for Bengal). Without this, the multi-calendar readout under-sells exactly the region that most needs it.
4. Backfill summaries for the 17 South Asian foundational/intermediate entries GPT-5 flagged as missing them (Mahajanapadas, Vijayanagara, Maratha, Sikh Empire, Tughlaq, Tuluva, Indira Gandhi 2nd term).

**UX (Opus):**
5. Mobile: sticky tappable breadcrumb + depth pips (`● ● ● ○`) + swipe-back gesture. The 4-deep chain is where the v2.0.0 breadcrumb hand-wave breaks at 375px.
6. Timeline: one-year tick floor + same-year cluster chip (`◈ 1839: 2 rulers ▸`) + start/end-cap glyphs (`╞`, `╡`) for transition years like 1526/Panipat.
7. Alias-authoring pass: epithets (Ranjit Singh "Lion of Punjab", Tipu "Tiger of Mysore"), regnal names (Bahadur Shah II "Zafar", Muhammad Shah "Rangila"), alternate romanizations Krishnadevaraya/Krishna Deva Raya.

### P2 — content expansion (Gemini's agenda)

Do **after** P0/P1 model & UX work lands. Not before — otherwise the new content repeats the v2.1.0 under-annotation pattern.

1. **Americas (next-biggest gap at 44 entities).** Priority additions in Gemini's report: US Presidents (Washington, Lincoln, FDR, at minimum), Latin American Wars of Independence (Bolívar, San Martín), Porfiriato + Mexican Revolution, Empire of Brazil + Pedro II.
2. **West Asia (second-biggest at 53).** Post-Sasanian Persia; Umayyad/Abbasid caliphate rulers; post-Suleiman Ottoman sultans.
3. **Post-2000 global era coverage.** Rise of China (post-1978 reforms) as an era; Arab Spring; Russo-Ukrainian War; Digital Revolution era in `global.contemporary`.
4. **Missing themes** (Gemini): "Anti-Colonial Resistance Leaders", "Silk Road Buddhism", "Great Female Rulers of South Asia".
5. **New anchors** for South Asia: Gupta Golden Age (320), Delhi Sultanate founding (1206), Shivaji's coronation (1674).
6. **Missing peripheral coverage:** Nepal (Prithvi Narayan Shah unification, 2001 Royal Massacre), Bhutan, Maldives.

---

## What NOT to do (all three reviewers agree)

- **Do not re-architect columns.** Depth is 4, fan-out top is still Heian's 88. The v2.0.0 design is correct.
- **Do not build fuzzy search / Soundex.** For 1,305 curated rows, fold-normalization + explicit aliases covers real queries without false-positive noise. This was already an anti-pattern in v2.0.0.
- **Do not bundle Noto webfonts for native-script rendering.** OS system fonts cover Devanagari/Bengali/Gurmukhi/Telugu/Arabic on every modern target. Layered font stack + `lang=` per element = zero-dependency + correct rendering.
- **Do not migrate `south-asia` path IDs into chronological buckets** until the `redirect_ids[]` policy is tested. Path IDs are identity; churn without redirects breaks URLs.
- **Do not draw sub-year timeline bars.** Data is year-granular; the "6-hour ruler" case must degrade honestly to a cluster chip, not fake precision.

---

## One-paragraph verdict

v2.1.0 successfully **closes the geographic gap that v2.0.0's review flagged** and validates the underlying architecture — no depth increase, no fan-out crisis, zero errors. The remaining work is small and non-blocking: **fix the schema-adoption drift** (helpers accept new fields; `subkind` gets added; ancient dynasties get date-ranges; `links[]` gets populated for cross-regional cases), **ship the small UI polish** (in-column headers for the 32-child region column; native-script line with proper metrics; transliteration fold; Independence-node layout; mobile breadcrumb), **then** expand to the Americas — Gemini's next-biggest gap — with the new authoring discipline in place. The five council-flagged bugs (duplicate slug, Hasina/Benazir tenures, two hagiographic summaries) are already fixed this round; the dataset is now at 1,305 entities and still clean.
