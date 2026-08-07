# Opus Review v2.1.0 — UX/UI Implications of the South Asia Expansion

**Reviewer:** Opus (UX/UI focus)
**Target:** History-period picker embedded in the compiled TypeScript app at [tyoh.app](https://tyoh.app)
**Dataset:** v2.1.0 — 1,303 entities · 21 calendars · 16 themes · 37 anchors (South Asia grown 26 → 206)
**North star (unchanged):** *OmniUnit & Calculator* — a dark near-black canvas, orange accent, small-caps micro-labels, precision dropdown, Smart-Paste/Copy affordances. The picker must feel like the same author shipped it the same day.
**Date:** 2026-07-20
**Prior review:** `opus-ux.md` (v2.0.0). This is a delta, not a rewrite — read them together.

---

## Executive summary

The v2.1.0 expansion **validates the v2.0.0 architecture rather than straining it.** I measured the actual data, and the two things the South Asia set could have broken — depth and fan-out — both stayed inside the envelope the Miller-column design was chosen to handle:

- **Depth did not increase.** South Asia's deepest chain is still 4 levels (region → era → dynasty-period → reign): `South Asia › Delhi Sultanate › Mamluk Dynasty › Razia Sultana`. That is exactly the "4 columns + detail" case v2.0.0 was sized for. Max depth across the *whole* dataset is unchanged.
- **Fan-out added one new mid-tier hotspot, not a new worst case.** The top of the fan-out table is still Japanese: Heian 88, Muromachi 65, Kamakura 58, Edo 50. South Asia's biggest node is `south-asia` itself at **32 direct children** (the bundle's "33" counts a since-renamed node), slotting in below Byzantine's 35. `mughal` is 17, `china.tang` grew to 21, `rome.crisis-3c` is 21. None of these approach the Heian 88 that already forced the column design. The pattern holds.

So the headline is: **do not re-architect.** The v2.0.0 P0 stack (Miller columns + command-bar search + multi-calendar Copy-able readout + additive Detail tiers + hash URLs, in OmniUnit's skin) survives intact. But the expansion surfaces **five genuinely new, mostly small UX problems** that the v2.0.0 review could not have seen, because the data to expose them didn't exist yet:

1. **The `south-asia` column is now a 32-row wall that mixes eras with three loose "reign" figures** (Guru Nanak, Kabir, Tagore parented directly to the region). It needs light **sub-region grouping** — but as *headers inside one column*, not new column steps.
2. **`south-asia.independence` is a mixed-kind bag of 10 children** — 4 founders, 2 nested "PMs/Leaders" period buckets, 2 events, 2 loose reigns. This is the messiest single node in the new data and needs a specific layout answer.
3. **Six new writing systems** (Devanagari, Bengali, Gurmukhi, Telugu, Urdu/Perso-Arabic, plus the Persian-derived Nastaʿliq feel) hit a dark, terse, tabular-figure UI that was never font-tested for complex scripts. This needs an explicit **font stack + line-metrics** decision or the readout will clip diacritics and jump baselines.
4. **The data models sub-year reigns at year granularity** (Kharak Singh `1839–1839`, Nau Nihal `1839–1840`), so the "6-hour ruler" and "same-day multi-emperor" cases the brief worries about **cannot be drawn honestly at any zoom** — this is as much a data note as a UI one, and the timeline must degrade gracefully into a stacked "N rulers this year" chip.
5. **Transliterated names** (Iltutmish, Krishnadevaraya, Aurangzeb, Ranjit Singh) don't match Western reading/typing habits, and the `aliases[]` array is still far too sparse (only ~11 South Asian entities carry any alias) to be the answer on its own.

None of these is a P0-blocker to the architecture. Two of them (grouping headers, independence layout) are cheap. Two (fonts, transliteration search) are data/CSS work the author should budget for now, before the next region lands. Details, wireframes, and a re-prioritized list follow.

---

## Reassessment of the v2.0.0 P0/P1 recommendations

| v2.0.0 item | Verdict after 2.1.0 | Change |
|---|---|---|
| **P0.1 Miller columns + detail pane** | **Holds.** Depth still ≤4; fan-out top unchanged. | Add **in-column group headers** for high-fan-out region nodes (§1). No structural change. |
| **P0.2 Global command-bar search** | **Holds, now more load-bearing.** With 180 hard-to-spell names, search is *the* entry path for South Asia. | Add **transliteration/alias handling** and grow `aliases[]` (§5). |
| **P0.3 Multi-calendar Copy-able readout** | **Holds.** The Islamic/Hijri readout matters more now (Sultanates, Mughals). | Add **native-script line** with correct font stack + metrics (§3). |
| **P0.4 Additive Detail tiers** | **Holds cleanly.** Tier mix is sane: of `south-asia`'s children the loose reigns are foundational, so Detail=Foundational still yields a coherent column. | The "+N more (Specialist)" footer now also hides, e.g., Western Chalukya/Aravidu — behavior is correct, no change. |
| **P0.5 Hash state (entity ids)** | **Holds.** New ids are clean dot-slugs (`south-asia.delhi-sultanate.mamluk.razia-sultana`). | None. |
| **P0.6 OmniUnit skin, tabular figures** | **Holds, with a caveat.** Tabular-lining figures are Latin-only; the *native-script* line must opt out of `font-variant-numeric: tabular-nums` and use its own metrics (§3). | Scope the tabular rule to the Latin year columns only. |
| **P1.1 Contemporaries timeline (SVG swimlanes)** | **Holds and gets its best demo yet.** 1526/Panipat is a genuinely dense, exciting cross-region moment (§6). | Add a **year-granularity floor** + "N rulers this year" stacking (§4). |
| **P1.2 Warped/log axis** | **Holds.** South Asia is dense post-1200, sparse pre-1000 — same shape as the global set. | None. |
| **P1.3 Cross-regional canonical + ⤴** | **Holds; barely exercised by this batch.** South Asia added almost no `cross_parent_ids` (Panipat/Babur live cleanly under Mughal). | None. |
| **P1.5 Mobile single-column + breadcrumb** | **Needs a real fix.** The 4-deep chains at 375px are exactly where the breadcrumb affordance was hand-waved. See §2. | **Upgrade breadcrumb to a first-class, always-visible, tappable path** (§2). |
| **P1.7 A11y listbox keyboarding** | **Holds; extended.** Add `lang=` per native-script node so screen readers switch pronunciation dictionaries (§3). | Minor add. |

**Net:** zero P0 reversals. The architecture was correctly sized. What follows is additive.

---

## 1. Fan-out after 2.1.0 — does the column view still hold?

**Yes.** Measured fan-out (direct children), whole dataset:

```
88  east-asia.japan.heian
65  east-asia.japan.muromachi
58  east-asia.japan.kamakura
50  east-asia.japan.edo
35  europe...byzantine
32  south-asia                ← NEW hotspot (region node itself)
21  east-asia.china.tang      (was 6)
21  europe...rome.crisis-3c
18  africa...ptolemaic
17  east-asia.china.ming
17  south-asia.mughal         (was 4)
```

A 32-tall column scrolls fine — Heian's 88 already proved columns survive far worse. **The column model is not in danger.** But `south-asia` is now the *worst-organized* column even if not the tallest, for two reasons the raw count hides:

1. It **mixes 29 eras with 3 loose `reign` figures** parented straight to the region — Guru Nanak (1469), Kabir (1440), Rabindranath Tagore (1878) sit as peers of "Gupta Empire" and "Mughal Empire." Scanning a column of empires and suddenly hitting "Guru Nanak" is a category jolt.
2. Chronology alone doesn't chunk it — 29 eras spanning −3300 → present is a lot to eyeball.

### Recommendation: in-column sub-region group headers (NOT new column steps)

Add **non-selectable small-caps section headers inside the single `south-asia` column** — the OmniUnit "SI BASE UNITS / DERIVED UNITS" idiom, reused verbatim. Do **not** insert an Ancient/Medieval/Modern/Colonial *column* — that would add a level of depth the data doesn't have and push Razia to 5 columns. Group *within* the existing column:

```
┌ SOUTH ASIA ──────────────────┐
│ ANCIENT                       │  ← small-caps header, dim, non-selectable
│  ▣ Indus Valley           ›   │
│  ▣ Vedic Period           ›   │
│  ▣ Maurya Empire          ›   │
│  ▣ Gupta Empire           ›   │
│ ───────────────────────────   │
│ CLASSICAL / EARLY-MED         │
│  ▣ Chola Empire           ›   │
│  ▣ Pallava · Pala · Rashtra…› │
│ ───────────────────────────   │
│ SULTANATES & VIJAYANAGARA     │
│  ▣ Delhi Sultanate        ›   │
│  ▣ Vijayanagara Empire    ›   │
│  ▣ Bahmani · Bengal · Deccan› │
│ ───────────────────────────   │
│ EARLY-MODERN EMPIRES          │
│  ▣ Mughal Empire          ›   │
│  ▣ Maratha Confederacy    ›   │
│  ▣ Sikh Empire · Mysore   ›   │
│ ───────────────────────────   │
│ COLONIAL & MODERN             │
│  ▣ East India Company     ›   │
│  ▣ British Raj            ›   │
│  ◆ Post-Independence      ›   │
│ ───────────────────────────   │
│ FIGURES                       │  ← the 3 loose reigns get their own bucket
│  ● Guru Nanak                 │
│  ● Kabir                      │
│  ● Rabindranath Tagore        │
└───────────────────────────────┘
```

Two ways to source the grouping, cheapest first:
- **Zero-data option:** derive the buckets in the UI purely from `start_year` thresholds (a `regionGroups` config keyed by region id). Works today, no schema change.
- **Cleaner option (suggest to data team, not required):** add an optional `group` string on region-level children. This future-proofs other big region columns (East Asia will want the same when Japan's eras crowd in).

The **"loose reigns under a region" pattern is the real smell.** Nanak/Kabir/Tagore as direct region children breaks the region→era→period→reign grammar. UI can paper over it with a "FIGURES" bucket, but flag to the data team: these ideally belong under a `south-asia.cultural-figures` era (or Tagore under British Raj, Nanak adjacent to Sikh Empire) so the tree stays typed. This will recur with every region that adds poets/saints/scientists.

**Verdict on the brief's question:** yes, `south-asia` should get Ancient/Medieval/Modern/Colonial groupings — **as in-column headers, not as an extra column.** It shrinks the *perceived* column without adding depth.

---

## 2. The 4-deep chain at 375px — breadcrumb affordance

Confirmed the three brief chains against the data — all are **4 columns deep** (region counts as column 1):

```
South Asia › Delhi Sultanate › Mamluk (Slave) Dynasty › Razia Sultana
South Asia › Maratha Confederacy › Peshwa Era › Baji Rao I
South Asia › Post-Independence › Prime Ministers of India › Nehru
```

On **desktop this is fine** — 4 columns + detail pane fits, exactly as designed. On **375px mobile it is the case that breaks the v2.0.0 hand-wave.** With one list visible at a time, reaching Nehru is four blind taps, and my v2.0.0 sketch showed a passive breadcrumb (`‹ East Asia › Japan › Edo`) that's easy to lose. Four is past the threshold where users forget where they are.

### Recommendation: promote the breadcrumb to a first-class, sticky, tappable path with depth pips

```
┌ 375px ─────────────────────────────┐
│ 🔎 Search history…            ⌘K   │
├────────────────────────────────────┤
│ ● ● ● ○        ‹ back              │  ← depth pips: 3 of 4 deep, filled = you-are-here
│ South Asia › Delhi Sult… › Mamluk  │  ← each crumb tappable; middle crumb truncates
├────────────────────────────────────┤
│  ● Qutb ud-Din Aibak          ›    │
│  ● Iltutmish                  ›    │
│  ● Razia Sultana              ›    │  ← foundational, will fill bottom sheet on tap
│  ● Ghiyas ud-Din Balban       ›    │
├────────────────────────────────────┤
│  Detail: [Found][+Int][+Spec]      │
└────────────────────────────────────┘
```

Specifics:
- **Sticky breadcrumb bar** pinned below search; never scrolls away. Each crumb is a tap target back to that level (≥44px hit area even if visually compact).
- **Depth pips** (`● ● ● ○`) give an at-a-glance "how deep am I" that a text breadcrumb alone doesn't — cheap, dark-UI-friendly, matches OmniUnit's terse glyph language.
- **Middle-crumb truncation with ellipsis**, keeping first (region) and last (current) full — the standard mobile breadcrumb collapse. Tapping the ellipsis expands the full path in a sheet.
- **Swipe-right = up one level** (iOS back-gesture muscle memory), mirroring the "‹ back" affordance so the crumb bar and the gesture agree.
- The **detail/calendar readout stays a bottom sheet** (v2.0.0 §9) — unchanged and correct; it gives the multi-calendar block full width, which matters more now that Hijri/Vikram Samvat readouts are common.

This is a mobile-only upgrade; desktop columns already answer "where am I" spatially.

---

## 3. Native-script rendering — typography implications

The 2.1.0 data adds **12 native-name entities across six new writing systems**, verified:

- **Devanagari** — हर्षवर्धन (Harsha), महात्मा गांधी, जवाहरलाल नेहरू, छत्रपती शिवाजी महाराज, भीमराव रामजी आंबेडकर
- **Bengali** — রবীন্দ্রনাথ ঠাকুর (Tagore)
- **Gurmukhi** — ਗੁਰੂ ਨਾਨਕ (Nanak), ਮਹਾਰਾਜਾ ਰਣਜੀਤ ਸਿੰਘ (Ranjit Singh)
- **Telugu** — రుద్రమదేవి (Rudrama Devi)
- **Perso-Arabic / Urdu** — رضیہ سلطانہ (Razia), محمد علی جناح (Jinnah), ٹیپو سلطان (Tipu)

These join existing kanji, Hangul, Chinese, Ge'ez, and Cyrillic. Three concrete problems for a dark, terse, tabular UI:

**(a) Vertical metrics blow up the row.** Devanagari's shirorekha (top bar) + below-baseline conjuncts, Bengali's ascenders/descenders, and Gurmukhi/Telugu marks are **taller than Latin caps-to-baseline**. If native names share the Latin row's `line-height`, they clip or shove the baseline. Fix: give the native-name line its **own line-box** with generous `line-height` (≈1.6–1.8), never crammed onto the same baseline as the Latin name. In the readout, native name is its **own labeled line** under the Latin name — not inline beside it.

**(b) RTL vs LTR mixing.** Urdu/Perso-Arabic is **RTL**; the surrounding UI, dates, and Latin name are LTR. Set `dir="auto"` (or explicit `dir="rtl"` when the script is Arabic-range) on the native-name element so رضیہ سلطانہ renders right-aligned within its own line and doesn't scramble adjacent punctuation. Do **not** let it flip the whole row.

**(c) Tabular figures are Latin-only.** The v2.0.0 rule "monospaced/tabular figures for all years" must be **scoped to the Latin year columns.** Never apply `font-variant-numeric: tabular-nums` to the native-name element — Indic/Perso-Arabic digits and glyphs don't have tabular variants and will look broken. Fence the rule to `.year, .cal-value` classes only.

### Font-stack recommendation (zero-dependency, OS-first, matches the terse dark aesthetic)

The author ships a single dependency-free HTML file — **do not bundle Noto webfonts (megabytes).** Rely on the OS system stack, which on every modern target (macOS/iOS/Windows/Android/Linux) ships high-quality Indic + Arabic faces. Declare a layered stack and let the browser pick per-codepoint:

```css
:root {
  --ui-sans: -apple-system, "Segoe UI", Roboto, system-ui, sans-serif;

  /* native-name line: system Indic/Arabic first, then UI sans fallback */
  --native: "Noto Sans Devanagari", "Noto Sans Bengali", "Noto Sans Gurmukhi",
            "Noto Sans Telugu", "Noto Naskh Arabic", "Noto Nastaliq Urdu",
            /* macOS/iOS built-ins */ "Kohinoor Devanagari", "Bangla MN",
            "Gurmukhi MN", "Kohinoor Telugu", "Geeza Pro",
            /* Windows built-ins */ "Nirmala UI", "Aldhabi",
            var(--ui-sans);
}
.native-name {
  font-family: var(--native);
  line-height: 1.7;
  font-variant-numeric: normal;   /* never tabular */
  font-feature-settings: normal;
}
.native-name[dir="rtl"] { text-align: right; }
```

- **Named webfont families are aspirational**, not shipped — if the OS happens to have Noto (many Linux/Android do) it's used; otherwise the OS's own Indic/Arabic face (Kohinoor, Nirmala UI, Geeza Pro) resolves. This keeps the file zero-dependency while rendering all six scripts correctly on virtually every device.
- **Nastaʿliq for Urdu is a nice-to-have, not a requirement.** True Nastaʿliq (`Noto Nastaliq Urdu`, `Aldhabi`) is only present on some systems; naskh fallback is perfectly legible and correct. Don't gate the design on Nastaʿliq.
- **Tag `lang` on the element** (`<span class="native-name" lang="hi">`, `lang="ur"`, `lang="bn"`, `lang="pa"`, `lang="te"`). This (i) lets the browser pick the *right* face when a font covers multiple scripts, and (ii) lets screen readers switch pronunciation dictionaries (a11y win, ties to §P1.7).

### Where it shows in the column-view row

Keep column rows **Latin-only** for scan speed and alignment — a Gurmukhi name in a 32-row column would break the tabular rhythm. Show the native name **only in the detail/readout pane**, as its own line under the Latin name, exactly like OmniUnit stacks a value under its small-caps label:

```
◆ Razia Sultana                              [ Copy all ]
reign · 1236 – 1240 · Delhi Sultanate › Mamluk
رضیہ سلطانہ                                   ← native line, RTL, own metrics
```

Native-script **search** still works (typing رضیہ or ਨਾਨਕ matches via `native_name`), per v2.0.0 §8 — that's a match function, not a layout concern.

---

## 4. Wildly different reign lengths — timeline tick resolution

Measured range in the new data:

- **Long:** Kabir 78y, Guru Nanak 70y, Nandivarman II 65y, Amoghavarsha 64y; plus ongoing Modi (2014–present) and Ranjit Singh's 38y empire.
- **Short (as stored):** Humayun-restored `1555–1556`, Jahandar Shah `1712–1713`, **Kharak Singh `1839–1839`**, Nau Nihal `1839–1840`, Mountbatten `1947–1948`.

**Critical data reality:** the "6-hour rulers" and "same-day multi-emperor" cases the brief worries about **are not in the data as sub-year values.** The schema stores integer years; Kharak Singh is `1839–1839`, a zero-width bar. There is **no month/day precision to render.** So the honest answer is:

**The timeline's tick floor is one year, and it must never pretend finer.** Attempting to draw "6 hours" would be false precision — a credibility killer for this technical audience (v2.0.0 anti-pattern #9). Instead:

### Tick / zoom resolution mapping (revised for the transition-year problem)

- **Century band (zoomed out):** era/period bars only; reigns collapse into parent. Kharak Singh invisible — correct.
- **Decade band (mid):** period bars + foundational reigns as bars. A zero/one-year reign renders as a **minimum-width tick (≈2–3px) with no label**, so it's visible-as-a-mark but doesn't claim width it doesn't have.
- **Year band (max zoom, 1 year = the floor):** individual reigns as bars. **When ≥2 reigns share a start year in one swimlane, stack them into a "same-year" cluster chip** rather than overlapping zero-width bars:

```
 1839 ─┬─────────────────────
 SIKH   │ Ranjit Singh ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╡   ← ends 1839
        │ ◈ 1839: 2 rulers ▸        ← Kharak Singh + Nau Nihal collapsed; click to expand
        │ Sher Singh ▓▓▓╡
```

Expanding the `◈ 1839: 2 rulers` chip lists them **ordered by `start_year` then by array order** (the data's implicit succession), each linking into the picker. This is the only honest way to show "several rulers in one year" when the data has no intra-year ordering. It also handles the **Delhi 1290 case** cleanly: I verified 1290 has three overlapping entities — `Mamluk` (ends 1290), `Khalji` (starts 1290), and `Jalal ud-Din Khalji` (starts 1290) — which at year granularity would stack ambiguously; the cluster chip disambiguates ("◈ 1290: dynasty change ▸").

### Long-reign vs short-reign coexistence

A 78-year Kabir bar next to a 1-year Jahandar bar is **fine on a warped-but-locally-linear axis** — the long bar is long, the short one is a tick. The failure mode is only *labeling*: don't label sub-decade bars at the century band. Label priority = tier (foundational labels first) + available width, identical to the v2.0.0 label-collision rule. No new mechanism needed beyond the same-year cluster chip.

**Suggest to data team (not required for UI):** if intra-year succession matters (it does for the "6-hour ruler" story), add an optional `sequence` integer or `start_precision: "day"` with an ISO date. Until then, the UI correctly shows year granularity and clusters ties. **Don't fake sub-year bars.**

---

## 5. Search prominence for transliterated South Asian names

The concern is real: **Iltutmish, Krishnadevaraya, Aurangzeb, Ranjit Singh, Farrukhsiyar** don't map to Western spelling/typing reflexes, and I confirmed `aliases[]` is **very thin** — only ~11 South Asian entities carry any alias, and several are event/era aliases ("Sepoy Mutiny"), not personal-name variants. Relying on `aliases[]` alone is insufficient.

### Recommendation: three layers, cheapest first — do all three, none is heavy

**(a) Diacritic + separator folding in the existing matcher (near-free, do now).**
The v2.0.0 search is already "diacritic-folded prefix+substring." Extend the fold to also normalize the **spelling noise that plagues transliteration**: strip/normalize apostrophes and hyphens, collapse doubled letters, and fold common digraphs. Concretely, index a `searchKey` that maps `Alauddin` and `Ala-ud-din` and `Ala ud Din` to the same token; `Aurangzeb`/`Aurangzib`; `Firoz`/`Firuz`/`Feroze`. This is a ~15-line normalization table, no dependency, and it fixes the 80% case (spacing/hyphen/vowel variants of the *same* romanization) without any content authoring.

**(b) Grow `aliases[]` for the genuinely different names (data task, do now).**
Folding won't catch names that are *different strings*, only the picker knows are the same:
- **Titles/epithets:** Ranjit Singh → "Lion of Punjab"; Tipu → "Tiger of Mysore"; Samudragupta → "Napoleon of India"; Baji Rao I → (none needed, but Nana Saheb is already inline on Balaji Baji Rao — pull it into `aliases[]`).
- **Regnal vs personal:** Bahadur Shah II → "Zafar"; Muhammad Shah → "Rangila".
- **Alternate romanizations that folding can't reach:** Krishnadevaraya → "Krishna Deva Raya", "Krishna Raya".
This is authoring, not engineering — but it's the highest-trust layer because the "↳ alias 'Lion of Punjab'" match line (v2.0.0 §8) *shows the user why it matched*.

**(c) Native-script + `lang`-aware match (already designed).**
Typing رنجیت or ਰਣਜੀਤ matches via `native_name` (v2.0.0). No change; just confirm the fold doesn't strip the native field.

**What NOT to build:** a phonetic/Soundex or fuzzy-edit-distance engine. It's out of scope (v2.0.0 anti-pattern #4), and for a curated 1,303-row set, (a)+(b) covers the real queries without the false-positive noise fuzzy matching brings. **Fold aggressively; alias deliberately; skip fuzzy.**

**Answer to the brief:** `aliases[]` alone is *not* sufficient (too sparse). The fix is **fold-normalization in the matcher (engineering, once) + a real alias-authoring pass (data, ongoing).** Auto-generating transliteration variants at runtime is unnecessary once folding handles separator/vowel noise.

---

## 6. The "contemporaries" swimlane at 1526 (Panipat)

This is the timeline's best possible demo, and the data delivers. I queried every foundational/intermediate era/period/reign spanning **1526** and it's genuinely rich — 13 South Asia, 17 Europe, plus East Asia, West Asia, and cross-regional. Here is the sketch, drawn from the **actual entities**:

```
   year ▸ [ 1526 ]   =  Vikram Samvat 1583 · AH 932 · Sexagenary 丙戌        [→ open in picker]
════════════════════════════════════════════┃═══════════════════════════════════════════
                                         cursor at 1526
 SOUTH ASIA │ Delhi Sultanate ▓▓▓▓▓▓▓▓▓▓▓▓▓╡          ← ENDS 1526 (Ibrahim Lodi ╡ killed)
            │      Lodi Dyn ▓▓▓▓▓▓▓▓▓╡ · Ibrahim Lodi ▓╡
            │ Mughal Empire ╞▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓…      ← STARTS 1526 (Babur ╞▓)
            │ Vijayanagara ▓▓▓▓▓▓┃▓▓▓▓  · Krishnadevaraya ▓▓┃▓▓ (r. to 1529)
            │ Bahmani ▓▓▓┃╡ · Bengal Sult. ▓▓▓┃▓▓ · Deccan Sult. ▓┃▓▓▓
            │ Guru Nanak ▓▓┃▓▓▓ (alive)
 EAST ASIA  │ Ming ▓▓▓▓▓▓┃▓▓▓▓  · Jiajing Emperor ▓┃▓▓  · Muromachi ▓▓┃▓ · Joseon ▓▓┃▓
 WEST ASIA  │ Safavid ▓┃▓▓▓▓▓
 CROSS-REG  │ Ottoman ▓▓▓▓┃▓▓▓  · Suleiman the Magnificent ▓┃▓▓  · Age of Sail ▓▓┃▓▓▓
 EUROPE     │ Holy Roman Empire ▓▓▓▓▓▓┃▓▓ · Charles V ▓┃▓▓ (HRE) · Habsburg ╞▓ (Austria)
            │ Tudor England ▓▓┃▓ · Henry VIII ▓┃▓▓  · France (Valois) ▓▓┃▓
            │ Reformation ▓┃▓▓ · Martin Luther ▓┃▓▓  · Italian Renaissance ▓▓┃▓
            │ Spanish Empire ▓▓┃▓▓ · Portuguese Empire ▓▓▓┃▓▓  · Muscovy ▓▓┃▓
 [ Americas ▾ 10 more ]   [ Africa ▾ ]   [ Oceania ▾ ]      ← collapsed rows w/ counts
════════════════════════════════════════════┃═══════════════════════════════════════════
```

**The "aha" this frames:** the cursor lands exactly on a **dynastic hinge** — Delhi Sultanate/Lodi *end* (╡) and Mughal Empire *begin* (╞) on the same 1526 line, while Krishnadevaraya still reigns in the south, Suleiman and Charles V and Henry VIII are all simultaneously on stage, and Babur, Suleiman, and Charles V are near-exact contemporaries. That's a spectacular teaching moment and the single best argument for shipping the timeline.

### What gets visually noisy — and the fixes

1. **Europe is the noisy row, not South Asia.** 17 overlapping Europe entities (empires + Renaissance + Reformation + three monarchies) will collide. **Fix: sub-lane Europe by kind** — a thin "structures" lane (HRE, empires, Renaissance/Reformation *eras*) above a "rulers" lane (Henry VIII, Charles V, Luther). Or apply the Detail filter to the timeline too: at Foundational, Europe drops to ~5 bars.
2. **The 1526 same-line start/end collision** (Delhi ends, Mughal starts) needs the **╡ end-cap and ╞ start-cap glyphs** so the eye reads "one ended, one began here," not "one continuous bar." This is the timeline analog of the §4 same-year cluster.
3. **Empire vs ruler nesting** (Krishnadevaraya inside Vijayanagara; Charles V inside HRE; Suleiman inside Ottoman) — render the **ruler as a thinner inset bar within the era's band**, not a separate row, so the reader sees "who ruled this polity at the cursor" without doubling the row count.
4. **Regions with no cross-region drama at 1526** (Americas pre-contact-ish, Africa, Oceania) collapse to a **`▾ N more` counted row** — present but not spending vertical budget. Verified counts exist (Americas 10, Africa 9) so the counts are real, not decorative.
5. **Calendar readout of the cursor year** (top strip: `1526 = VS 1583 · AH 932 · 丙戌`) ties the timeline back to the multi-calendar core — this is *why* it lives in a converter.

At **375px**, show only the region of the current selection (South Asia) + the cursor + a "swap region" chip, per v2.0.0 §9 — the 1526 full-swimlane is a desktop showpiece.

---

## 7. The Independence → PMs sub-period structure

This is the **messiest node in the new data**, and worth a precise answer. Measured children of `south-asia.independence` (a foundational `era` named "Post-Independence South Asia", ongoing):

- **4 loose founder reigns:** Gandhi, Jinnah, Ambedkar, Subhas Bose
- **2 nested period buckets:** `india-prime-ministers` (9 reigns: Nehru→Modi) and `pakistan-leaders` (6 reigns)
- **2 events:** Bangladesh Liberation War (1971), Sri Lankan Civil War (1983–2009)
- **2 more loose reigns:** Mujib, Hasina (Bangladesh)

So it's **10 direct children of three different kinds** — not the tidy "4 founders + 2 buckets" the brief assumed. That mixed-kind bag is the actual UX problem.

### Recommendation: full column steps for the PM/Leader buckets — do NOT inline "N more"

Make `Prime Ministers of India` and `Leaders of Pakistan` **real, drillable period columns** (a 4th column step), for three reasons:

1. **Consistency beats special-casing.** Every other period in the tree (Mamluk, Khalji, Peshwa Era, Tuluva) is a column step. Making PMs an inline "N more" expander would make *this one node* behave differently from all its siblings — a worse mental model than one more click. The path `Post-Independence › Prime Ministers of India › Nehru` is the same 4-deep shape as Razia and Baji Rao, which desktop handles and mobile now handles via the §2 breadcrumb.
2. **9 and 6 are column-sized, not glance-sized.** Inline "N more" is right for hiding a *tail* (e.g., "+42 specialist" under Edo). A full 9-item PM list is a browsing destination, not a tail — it wants its own scannable column with dates, not an expand-in-place that shoves the 8 sibling nodes down.
3. **It keeps the parent column readable.** If PMs inlined, the `independence` column would balloon from 10 rows to 25. As column steps, `independence` stays a clean 10-row column and the depth is paid only when you go there.

### But fix the mixed-kind ordering with in-column headers (same tool as §1)

Within the `Post-Independence` column, group the 10 mixed children so events/founders/buckets don't interleave confusingly:

```
┌ POST-INDEPENDENCE ────────────┐
│ FOUNDERS                      │
│  ● Mahatma Gandhi             │
│  ● Muhammad Ali Jinnah        │
│  ● B. R. Ambedkar             │
│  ● Subhas Chandra Bose        │
│ ─────────────────────────     │
│ HEADS OF GOVERNMENT           │
│  ◆ Prime Ministers of India ›│  ← full column step (9)
│  ◆ Leaders of Pakistan      ›│  ← full column step (6)
│  ● Sheikh Mujibur Rahman      │
│  ● Sheikh Hasina              │
│ ─────────────────────────     │
│ KEY EVENTS                    │
│  ◇ Bangladesh Liberation War │
│  ◇ Sri Lankan Civil War      │
└───────────────────────────────┘
```

**Where "N more" *does* belong here:** the PM list has an ongoing tail (Modi is `end:null`). Inside the *PMs column*, if Detail=Foundational hides Shastri/Rajiv/etc. (intermediate), use the standard dim "+4 more (Intermediate) ›" footer (v2.0.0 §2). That's the correct, consistent use of the affordance — hiding a tier tail, not restructuring the hierarchy.

**Data note:** the node is named "Post-Independence South Asia" but the id is `south-asia.independence`; keep the id (URLs depend on it) — this is fine, just don't let the label/id mismatch confuse future authoring.

---

## 8. UX concerns the v2.0.0 review missed, surfaced by the deeper ruler data

1. **Loose reigns parented to region/era break the type grammar.** Nanak/Kabir/Tagore under `south-asia`; Mujib/Hasina/Gandhi under the `independence` era as peers of period-buckets. The v2.0.0 review assumed a clean region→era→period→reign nesting; the real data has reigns at *every* level. **UI implication:** the column renderer must handle "mixed-kind children" as a first-class case (glyph per kind: ▣ era, ◆ period, ● reign, ◇ event) and the group-header pattern (§1, §7) is the mitigation. **Data implication (flag to team):** consider requiring reigns to sit under a period/era, even a thin one, so the tree stays predictable as more regions add cultural figures.

2. **`allow_outside_parent_dates` reigns will visually escape their parent bar.** Gandhi is `1915–1948` but his parent `independence` starts 1947; Mountbatten runs into 1948 past the Raj's end. On the timeline, a child bar extending *beyond* its parent's band looks like a rendering bug. **Fix:** when `allow_outside_parent_dates` is set, render the overhang with a **dashed/ghosted extension** and surface the `date_note` ("leadership began 1915, three decades before Independence") in the readout, so the overhang reads as intentional, not broken.

3. **Ongoing reigns (`end_year: null`) need a live "→ present" treatment, now common.** Modi, and the two open period-buckets, are ongoing. The timeline must render null-end as an **open-ended bar with a "→" cap to the present cursor**, and the readout must print "2014 – present," never "2014 – null" or a hardcoded year. Minor, but there are now enough ongoing entities that a null slipping through would be visible.

4. **Repeated-tenure entities create duplicate-looking rows.** Humayun (1530–1540) + Humayun (restored) (1555–1556); Indira Gandhi + Indira Gandhi (second term). In a column these read as accidental duplicates. **Fix:** in the column row, show the disambiguating suffix (already in the name) *and* on the timeline draw them as **two bars of one linked entity** with a hairline connector, so "same person, two reigns" is legible rather than looking like a data dupe. Cheap, and it's a recurring pattern (many dynasties have restored/interregnum rulers).

5. **Calendar readout must default to the *regionally appropriate* systems.** For a Delhi Sultanate or Mughal entity, lead the readout with **Hijri (AH)** and **Vikram Samvat / Saka**, not just Gregorian + an East-Asian sexagenary that's irrelevant here. The v2.0.0 "own calendars inline via `calendar_ids`" rule handles this *if the data populates `calendar_ids`* on the new entities — I did not see calendar_ids on the sampled South Asian entities. **Flag to data team:** back-populate `calendar_ids` (Hijri for Sultanate/Mughal/Pakistan, Vikram Samvat/Saka for Hindu-era polities, Bengali San for Bengal) or the readout will fall back to Gregorian-only and undersell the multi-calendar feature for exactly the region that most needs it.

6. **Same-name different-lineage collisions in search.** "Bahadur Shah I" (Mughal, 1707) vs "Bahadur Shah II" (Mughal, 1837); multiple "Bhutto"s; "Indira Gandhi" twice. The v2.0.0 "show ancestor breadcrumb + date in each search result" rule already handles this — **confirm it's implemented**, because South Asia is where it earns its keep.

---

## Prioritized recommendations for the next iteration

### P0 — do before the next region lands (cheap, prevents debt)
- **P0.1 In-column group headers** for high-fan-out region nodes (`south-asia` first; East Asia next). Derive buckets from `start_year` config; no schema change. (§1)
- **P0.2 Native-script line in the readout** with (a) its own line-box + `line-height ≈1.7`, (b) `dir="auto"`/`lang=` per script, (c) tabular-figures scoped to Latin year columns only, (d) the OS-first font stack (no bundled webfonts). (§3)
- **P0.3 Search fold-normalization** for transliteration noise (hyphens/spaces/vowels/doubled letters) + confirm native-script and ancestor-breadcrumb result lines. (§5, §8.6)
- **P0.4 Independence node: PM/Leader buckets as full column steps + in-column headers**, not inline "N more." (§7)

### P1 — high value, do next
- **P1.1 Mobile sticky tappable breadcrumb + depth pips + swipe-up** for the 4-deep chains. (§2)
- **P1.2 Timeline year-granularity floor + same-year cluster chip** (`◈ 1839: 2 rulers ▸`) and start/end-cap glyphs (╞ ╡) for transition years. (§4, §6)
- **P1.3 1526 contemporaries as the timeline's flagship view** — Europe sub-laned by kind, ruler-inside-era inset bars, collapsed `▾ N more` region rows, cursor calendar strip. (§6)
- **P1.4 `allow_outside_parent_dates` ghost-extension + `date_note` surfacing**, and ongoing `→ present` caps. (§8.2, §8.3)
- **P1.5 Alias-authoring pass** (epithets, regnal names, alternate romanizations) — data task, feeds the trusted "↳ alias" match line. (§5)

### P2 — polish / data hygiene (flag to data team)
- **P2.1 Back-populate `calendar_ids`** (Hijri, Vikram Samvat/Saka, Bengali San) on South Asian entities so the readout leads with regionally-correct systems. (§8.5)
- **P2.2 Re-home loose region-level reigns** (Nanak/Kabir/Tagore) under a `cultural-figures` era or appropriate polity, so the tree stays typed. (§1, §8.1)
- **P2.3 Linked repeated-tenure rendering** (Humayun ×2, Indira ×2) — connector bar on timeline, kept disambiguated in columns. (§8.4)
- **P2.4 Optional `sequence`/day-precision** if intra-year succession is ever needed for the "6-hour ruler" story — until then, cluster ties honestly. (§4)

---

### One-paragraph verdict
The South Asia expansion **did not break the v2.0.0 design — it stress-tested and confirmed it.** Depth held at 4, fan-out's worst case is still Heian's 88, and every P0 from last round survives. The new work is small and additive: **group the tall region column with in-line headers, give six new scripts a proper font line, teach search to forgive transliteration spelling, make the Independence buckets normal column steps, and give the timeline an honest one-year floor with a same-year cluster chip.** Ship those, back-populate `calendar_ids` for the region that most needs the multi-calendar feature, and 1526/Panipat becomes the demo that sells the whole timeline — all still inside OmniUnit's dark, terse, Copy-everything skin.
