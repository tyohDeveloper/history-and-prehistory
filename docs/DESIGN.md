# Design notes

**The primary living design document for this app.** Decisions, findings, and the open-items
register all live here. Open items are tracked as `Q-n` entries in §Open items rather than as
GitHub issues — issues are too formal for this stage, and the questions are too interdependent
to read well one at a time. Revisit that choice when the register stops changing shape.

**Status: work in progress, not merged.** Lives on branch `calendar-layer`. Enough is built to
prove the shape and expose the decisions that still need making. Nothing is wired into the UI, so
`main` remains a clean baseline.

Related: [`gap-analysis-v2.1.0.md`](gap-analysis-v2.1.0.md) §7 holds dataset-side open items;
[`ARCHITECTURE.md`](ARCHITECTURE.md) §12 cross-references the code-blocking ones.

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
9. A date runs from exact to a triple: **(later boundary, most likely / consensus, early
   boundary)**. All three can themselves be fuzzy, the early boundary especially.
10. Users mostly **focus on one era**. Detail before and after it matters less. The natural
    presentation is a **hyperbolic / perspective surface**: near the focus things are large, and
    they condense as they fall away.

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

## The date model (requirement 9)

A date is not a number here. It runs on a spectrum from exact to a fuzzy interval, and the
interval widens as you go back. The stated shape is a triple — later boundary, consensus, early
boundary — with each element itself possibly fuzzy.

That is, in the standard vocabulary, a **fuzzy number**. Membership rises across the early
boundary, plateaus over the consensus, and falls across the later boundary. Encoding options:

| Option | Encoding | Exact date | Simple range | Fuzzy boundaries |
|---|---|---|---|---|
| **A. Hard triple** | `early, consensus, late` | 3 equal values | yes | no — boundaries are crisp |
| **B. Triple + per-point fuzz** | 3 values + 3 half-widths | 6 fields | yes | yes, symmetric only |
| **C. Trapezoid (recommended)** | `outerEarly, innerEarly, innerLate, outerLate` | 4 equal values | `inner == outer` | yes, asymmetric |

**Recommendation: C, the 4-point trapezoid.** It degenerates cleanly in every direction — all four
equal is an exact date, inner pair equal is a triangular distribution with a single consensus
point, inner equal to outer is a crisp range — so one representation covers the whole spectrum
without optional sub-structures or a discriminated union. It expresses asymmetry natively, which
matters because the early boundary is the fuzzy one: an Aurignacian start might be
`48,000 / 45,000 / 43,000 / 42,000 BP`, with a long tail older and a short one younger. And it is
the conventional representation, so the arithmetic is known rather than invented.

### Does a trapezoid cost screen space?

No — and the reason is worth stating plainly, because it is easy to conflate the two: **the
trapezoid is a storage encoding, not a rendering.** Four numbers in JSON occupy no pixels. How
uncertainty is *displayed* is a separate decision, and every option below reads from the same
stored shape:

| Space available | Rendering | Example |
|---|---|---|
| Column gutter (~60 px) | Consensus only, or outer range | `45 ka` · `48–42 ka` |
| Readout line | Core range, tail parenthesised | `45–43 ka (possibly 48–42)` |
| Timeline bar | Solid core, tapered or gradient shoulders | same footprint as a hard-edged bar |
| Expanded detail | All four points, method, source | `48.0 / 45.0 / 43.0 / 42.0 ka, OSL` |

The timeline row is the one that might seem expensive and is not: a bar with soft ends occupies
exactly the same box as a bar with hard ends. Fuzziness is rendered as *softness at edges you were
already drawing*, not as extra elements. If anything it is cheaper than the honest alternative,
which is a hard bar plus a separate error-bar annotation.

The decisive point: **the simpler encodings do not save screen space either.** A hard triple still
has to render as some range, and that range is the same width. What the simpler options save is
*authoring fields*, not pixels. So screen real estate is not a reason to prefer A or B over C —
authoring burden is, and `Q-2` settles that by making the whole thing opt-in.

Where the trapezoid genuinely costs something is **cognitive load in the expanded view**, if all
four numbers are shown at once. Mitigation is progressive disclosure: consensus and core range by
default, the tails on demand.

Cost: four numbers per boundary, and a period has two boundaries — so up to eight per entity. See
`Q-2` on whether that is an acceptable authoring burden.

Note this composes: a period's **core** (definitely inside) runs from the early boundary's inner
edge to the later boundary's inner edge, and its **support** (possibly inside) runs outer to
outer. That is close to how phase boundaries are actually discussed, which is a good sign.

## Focus and context (requirement 10)

The described behavior — focus large, falling away with perspective compression — is
**focus+context**, and it is well studied. Furnas formalized it as a degree-of-interest function
where interest rises with an item's intrinsic importance and falls with its distance from the
user's focus ([Generalized fisheye views](https://dl.acm.org/doi/pdf/10.1145/22627.22342)):

\[ \mathrm{DOI}(x \mid f) = \mathrm{API}(x) - D(f, x) \]

Lamping, Rao, and Pirolli's hyperbolic browser is the specifically *hyperbolic* realization: lay
the hierarchy out on the hyperbolic plane and map it to a disk, so space per node falls off
continuously with distance from the center ([CHI '95](https://dl.acm.org/doi/pdf/10.1145/223904.223956)).
The reason it suits hierarchies is a geometric coincidence worth knowing: circumference on the
hyperbolic plane grows exponentially with radius, and trees grow exponentially with depth. And a
fisheye *calendar* is not hypothetical either — DateLens applied the same distortion to date grids
([Bederson et al.](https://www.microsoft.com/en-us/research/wp-content/uploads/2004/03/tochidatelens.pdf)).

**The part that matters for this app:** the `API` term in Furnas's function is already authored.
The dataset's `tier` field — 337 foundational, 416 intermediate, 552 specialist across all 1,305
entities — is exactly a priori importance. It was built for progressive disclosure, which is the
filtering special case of the same idea. So a degree-of-interest view needs no new per-entity data:

\[ \mathrm{DOI}(x \mid f) = w_t \cdot \mathrm{tier}(x) - w_d \cdot D(f, x) \]

**And it may dissolve the open timeline-scale problem.** `Q-3` in the earlier register asked how to
put 3.3 Ma and a 15-year reign on one axis; the answers on the table were a piecewise-compressed
scrubber or a mode switch. If temporal distance enters `D` logarithmically, the compression is a
property of the view rather than a special case bolted onto the axis — the Paleolithic is simply
very far from a focus on the Edo period and gets correspondingly little space. That is a better
answer than either previous option, and it arrives free.

### Distance must adapt to local density

Settled: `D` is a weighted blend of temporal and tree distance (`Q-6`). The reasoning that decided
it also implies a refinement worth recording.

Prehistory and modern history have opposite shapes. Prehistory is **sparse in entities and vast in
time** — a few nodes scattered across hundreds of millennia. Modern history is **dense in entities
and compressed in time** — dozens of nodes inside a single century. A distance term calibrated in
absolute years is therefore wrong at one end or the other no matter where it is tuned: any
threshold generous enough to give the Aurignacian neighbours will swamp a focus on the 1930s.

Log-scaling temporal distance helps but does not fix it, because it addresses magnitude, not
density. The more robust formulation is **rank- or density-normalized distance** — "the nearest
*n* nodes in time" rather than "nodes within *x* years", or raw distance divided by the local
median gap. That makes the lens behave the same way whether it is over the Pleistocene or over the
Cold War, which is the actual goal.

This also gives the tree term a clear job. In sparse prehistory, temporal neighbours are far away
and uninformative, so structural proximity should dominate. In dense modern history there are
plenty of temporal neighbours, so the temporal term can carry more weight. The blend weights may
themselves want to be density-dependent rather than constant.

Open: whether the distortion is geometric or typographic (`Q-7`), and what sets the focus (`Q-8`).

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
- **Open items live in this document**, not in GitHub issues, until the register stabilizes.
- **Fuzzy dates are a 4-point trapezoid** (provisional — pending `Q-1`). Encoding only; it does not
  dictate how uncertainty is drawn.
- **Fuzzy dates are opt-in** (`Q-2`, settled). `start_year`/`end_year` stay primary; fuzzy fields
  are an optional overlay. Revisit migration after prehistory has exercised it.
- **The focus view is a second view alongside the Miller columns** (`Q-5`, settled), not a
  replacement. Columns answer "where am I"; the lens answers "what is near this".
- **`D` blends temporal and tree distance** (`Q-6`, settled), with density normalization so the
  lens behaves consistently across sparse prehistory and dense modern history.
- **Focus+context uses `tier` as the a-priori-importance term**, so no new per-entity authoring is
  required to make the view work.

## Open items

The live register. `Q-n` ids are stable — reference them in commits and conversation. Ordered
roughly by how much else they block.

### Blocking — date model

**Q-1. Trapezoid, or something simpler?** Recommendation is the 4-point trapezoid above. Confirm,
or pick A/B from that table.

**Q-3. Does `consensus` mean "scholarly consensus" or "our editorial pick"?** These diverge on
contested chronologies — Egyptian New Kingdom, Indus decline, Homeric dating. If it is consensus,
it wants a source. If it is editorial, it wants to say so.

**Q-4. Do periods inherit boundary fuzziness from neighbors?** If the Shang ends fuzzily and the
Zhou begins fuzzily, are those the same fuzzy boundary authored once, or two independent ones that
can contradict each other? Shared boundaries halve the authoring and remove a class of
inconsistency, but they couple entities that may want independent sourcing.

### Blocking — focus and context

**Q-7. Is the distortion geometric or typographic?** True hyperbolic layout distorts positions and
sizes continuously. A cheaper reading is that near-focus items get more space and larger type
while distant ones shrink to a line or a tick — DateLens-style semantic zoom rather than a
Poincaré disk. The cheap version is much easier to keep accessible and legible.

**Q-8. What sets the focus?** The current tree selection, an independently draggable lens, or
both? A lens that moves independently of selection is more powerful and adds a second piece of
state the user has to understand.

**Q-9. Does the fisheye subsume the detail-tier control?** If `tier` is the API term, the existing
Essentials / Standard / Everything selector becomes a weight on that term rather than a filter.
That could replace the control, or make it redundant, or confuse users who expect a filter.

### Blocking — data

**Q-10. When does the dataset gain fuzzy bounds and `dating_method`?** The Python builder helpers
cannot emit them today (gap analysis §5.1), so this gates all prehistory authoring.

**Q-11. Do entities ever carry month/day precision, or stay year-only?** Calendar conversion is
exact for a full date and a span for a bare year. Affects the readout's shape.

### Non-blocking

**Q-12. How are simultaneous calendars chosen?** User selection persisted in the URL fragment, or
derived from the selected region via the dataset's `calendar_ids` — which exists for this and is
populated only on East Asian entities.

**Q-13. What does calendar input resolve to?** Typing `AH 897` — select the matching node, filter
the tree, or just display the conversion?

**Q-14. Nengō from CLDR or from the dataset?** `Intl` already renders pre-Meiji era names; the
dataset also ships ~250 nengō period nodes. Two sources of truth.

**Q-15. Is prehistory a separate branch or interleaved?** Affects whether the readout switches
frames per node or the app has a mode.

**Q-16. Bundle budget.** `temporal-polyfill/full` is installed but not yet imported, so the
artifact is still ~56 kB gzip. Wiring it in moves that materially. Set the ceiling first.

### Resolved

- ~~Timeline scale across six orders of magnitude~~ — likely dissolved by logarithmic temporal
  distance in the DOI function. Confirm once `Q-6` is settled.
- ~~`Q-2` Authoring scope~~ — opt-in overlay now, revisit migration after prehistory.
- ~~`Q-5` Focus view vs columns~~ — second view alongside, not a replacement.
- ~~`Q-6` Distance term~~ — weighted blend, density-normalized.
- ~~Per-app repos or monorepo~~ — per-app, settled 2026-08-07.
- ~~GitHub issues or design docs~~ — design docs, for now.

## Not yet built

Year-to-calendar span conversion, the ambiguity-preserving input parser, the multi-calendar
readout, calendar selection UI, and tests for any of it.
