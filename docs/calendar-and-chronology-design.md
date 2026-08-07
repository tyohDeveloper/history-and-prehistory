# Calendar & chronology layer — design checkpoint

**Status: work in progress, not merged.** Lives on branch `calendar-layer`.
Enough is built to prove the shape and to expose the decisions that still need making.
Nothing is wired into the UI yet, so `main` remains a clean baseline.

## Requirements as stated

1. Each app is its own standalone project. The hub only links out. *(Settled — this repo exists.)*
2. This app carries the **full** temporal library, same as the unit converter. All the calendars
   the converter supports are supported here.
3. **There is no separate converter.** Calendar handling is a display concern, not a tool.
4. The base reckoning is common **CE/BCE**.
5. The readout should eventually show **several calendars at once** — a Mesopotamian researcher
   wants Common and Islamic side by side.
6. The date picker should allow **entering** dates in any calendar, not just reading them.
7. Prehistory works in **BP**, not calendars.
8. Precision degrades going back, so **ranges become necessary** — and at BP scale, large ones.

Requirements 7 and 8 are the ones that reshaped the design. They are not a display mode bolted
onto a calendar app; they change what a date *is* in the value model.

## What is built

| Module | Purpose |
|---|---|
| `src/lib/temporal/temporal.ts` | Source-selection shim re-exporting `temporal-polyfill/full`. Ported from OmniUnit unchanged in substance, so both apps make the same choice the same way. |
| `src/lib/temporal/julianJdn.ts` | Fliegel-Van Flandern JDN converters for Julian and Revised Julian, which Temporal does not implement. Ported verbatim. |
| `src/lib/calendars/registry.ts` | 26 calendars with validity horizons, primary/variant grouping, and per-calendar caveats. |
| `src/lib/chrono/year.ts` | `YearValue` — point estimate plus optional bounds plus dating method. Historical/astronomical year-numbering crossings isolated to two functions. |
| `src/lib/chrono/bp.ts` | BP from the 1950 datum, `yr`/`ka`/`Ma` scaling, uncertainty-driven rounding, and the rule for when BP is preferred over calendars. |

## Findings that constrain the design

**Temporal has no `julian` calendar.** Confirmed by probe; `withCalendar("julian")` throws. This is
why the JDN module exists and why Julian and Revised Julian are separate backends in the registry.

**Exotic calendars extrapolate nonsense before their epoch, silently.** Asking the polyfill for a
3300 BCE date returns Persian year `-3921`, Coptic `-3584`, Indian `Śaka -3378`. These are
arithmetically real and historically meaningless. Every calendar therefore declares a
`validFrom`/`validTo` window, and the readout must be able to say "outside the meaningful range
of this calendar" instead of printing a confident absurdity. This is the single most important
thing the registry does.

**A Gregorian year maps to a *span* in lunar calendars.** 1492 CE is AH 897–898. 2026 CE is
AM 5786–5787. Rendering a lunar year as a single number is wrong roughly half the time, so the
conversion function returns a span, not a point. Byzantine AM (September start), Olympiad
(midsummer start), and French Republican (equinox start) have the same property for a different
reason.

**CLDR gives pre-Meiji nengō for free.** `Intl` renders 1492 as "4 Entoku (1489–1492)". Worth
knowing before hand-rolling anything against the dataset's own `named_years`.

**BP is not "years ago".** The datum is fixed at 1950 CE. At Holocene scale the ~76-year offset is
real; at Pleistocene scale it is noise. Implemented exactly, via astronomical year numbering so
the absent year zero does not introduce an off-by-one: 1 BCE is 1950 BP, 1 CE is 1949 BP.

**Rounding is a correctness concern at depth, not cosmetics.** "3,300,000 BP" asserts seven
significant figures for a boundary uncertain by hundreds of millennia. The digits are not merely
useless — they are false. Rounding is therefore driven by the uncertainty interval, and where an
explicit range exists the range is rendered *instead of* the point estimate, because at that scale
the range is the claim. Current behavior:

| Input | Renders as |
|---|---|
| 8000 BCE | `9,949 BP` |
| 3.3 Ma point | `3.3 Ma` |
| 3.4–3.2 Ma range | `3.4–3.2 Ma` |
| Natufian, 13000–9500 BCE | `15–11 ka` |

## Decisions taken (reversible, flagging for review)

- **BP threshold at 10,000 BP**, deliberately near the Holocene boundary (~11,700 BP) where Deep
  Time hands off. No calendar in the registry has a meaningful epoch anywhere near it.
- **Dating method forces BP.** A radiocarbon date renders in BP regardless of magnitude, because a
  calibrated ¹⁴C date and a historically attested date are not the same kind of claim and should
  not look identical.
- **Registry carries 26 calendars** — the converter's 19, plus arithmetic reckonings the entity
  dataset already declares that a history app needs: Roman AUC, Olympiad, Byzantine AM, sexagenary,
  Maya Long Count, Juche, French Republican.
- **`dating_method` as a new field**, not a new `date_precision` enum value. Method and precision
  are orthogonal; `date_precision` is already 95% `approx` and carries no information.

## Open questions

Blocking, in rough priority order.

1. **Does the entity dataset gain `min`/`max` bounds and `dating_method`, and when?** The value
   model supports them; the v2.1.0 data has bounds on 3 entities and no method field at all. The
   BP work is only as good as the data feeding it. This is gap-analysis §5.1 — the Python builder
   helpers cannot currently emit these fields.

2. **Timeline scale across six orders of magnitude.** Still unresolved from the gap analysis. It
   now matters more, because BP ranges at Ma scale cannot share a linear axis with a 15-year reign.

3. **How many calendars at once, and how are they chosen?** Requirement 5 says several. Open:
   is it a persistent user selection (URL fragment, since we store nothing), or derived from the
   selected region — Islamic auto-appearing under West Asia the way `calendar_ids` was presumably
   meant to work? The dataset's `calendar_ids` field exists for this but is populated on only
   East Asian entities.

4. **What does calendar *input* resolve to?** Typing `AH 897` — does it select the matching tree
   node, filter the tree, or just display the conversion? The wiki calls for ambiguity-preserving
   parsing with candidate chips, but not what happens after a candidate is picked.

5. **Do entities carry full dates or only years?** Everything in v2.1.0 is year-only. Calendar
   conversion is exact for a date and a span for a year. If reigns eventually get month/day
   precision, the readout changes shape.

6. **Is prehistory a separate branch of the tree, or interleaved?** Affects whether the readout
   switches frames per-node or the whole app has a mode.

7. **Nengō from CLDR or from the dataset?** CLDR already knows pre-Meiji era names. The dataset
   also ships ~250 nengō as `period` nodes with `named_years` cross-references. Two sources of
   truth; pick one.

8. **Bundle budget.** `temporal-polyfill/full` is installed but not yet imported by the app, so the
   artifact is still ~56 kB gzip against the recorded baseline. Wiring it in will move that
   materially. Worth deciding the ceiling before, not after.

## Not yet built

Year-to-calendar span conversion, the ambiguity-preserving input parser, the multi-calendar
readout, calendar selection UI, and tests for any of it.
