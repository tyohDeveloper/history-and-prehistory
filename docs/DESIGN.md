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

**Settled.** A date has up to three anchor points — **earliest bound, consensus, latest bound** —
and *each anchor independently carries its own fuzziness*. The structure as a whole may also be
qualified.

The worked example that settled it:

> ~3500 BCE (3000 BCE .. ~4500 BCE) — we think about 3500 BCE, we know it is not later than
> 3000 BCE, but it might be as early as 4500 BCE, and even that is fuzzy.

Three anchors, and they are **not uniformly certain**: the latest bound is crisp (3000 BCE is a
hard floor), the consensus is soft, the earliest bound is soft. That asymmetry between *which
anchor* is fuzzy is the thing the model has to preserve.

### This rules out the trapezoid

The earlier recommendation was a 4-point trapezoid. The example above shows why it does not work.
Encoding it as a trapezoid forces a choice between representing 3500 as a peak — which collapses
4500 into an anonymous tail and loses it as a *stated* bound — or representing 4500 and 3500 as a
plateau, which wrongly asserts the whole span is equally likely. The trapezoid cannot hold both
"the stated early bound is 4500" and "that bound is itself uncertain," because it has no place to
put a bound's own uncertainty. Superseded.

### The model

```ts
interface FuzzyPoint {
  year: number;      // the stated value
  fuzz?: number;     // +/- years; absent or 0 means crisp
}

interface HistoricalDate {
  consensus: FuzzyPoint;   // best accepted value
  earliest?: FuzzyPoint;   // oldest plausible bound
  latest?: FuzzyPoint;     // youngest plausible bound
  method?: DatingMethod;
  note?: string;           // when scholarship is genuinely split
}
```

It degenerates the whole way down:

| Case | Encoding | Renders |
|---|---|---|
| Exact | `consensus: { year: 2001 }`, no bounds | `2001 CE` |
| Crisp range | three anchors, all `fuzz` absent | `3500 BCE (3000–4500 BCE)` |
| The example | `consensus: {-3500, fuzz 250}`, `earliest: {-4500, fuzz 500}`, `latest: {-3000}` | `~3500 BCE (3000 – ~4500 BCE)` |

The last row is the point: **the notation renders back exactly as it was written by hand.** A `~`
is precisely "this anchor has non-zero fuzz." Nothing has to be invented for the display layer,
because the authoring notation and the rendering are the same notation.

### What "consensus" means

**Settled:** what most scholars would accept as reasonable — the value an early undergraduate
course would give. Not the research frontier, not our own adjudication of a live dispute.

This matches the app's stated audience and it pairs with the existing `tier` field: `foundational`
content is what a novice sees, and the consensus date is the novice-facing number. Where
scholarship is genuinely split rather than merely uncertain, that belongs in `note` — the app
should say the field is divided rather than quietly picking a side and dressing it as consensus.

## When does a date switch to BP?

The earlier rule was a magnitude threshold: anything older than 10,000 BP renders in BP. Two
counter-examples break it, and both are ordinary rather than edge cases.

- **Stonehenge**, roughly 2500 BCE. Well inside the threshold, but it is a radiocarbon date on
  antler picks. It should read as BP.
- **Alexander and Cyrus.** Also BCE-era, some of it known to the year via king lists and eclipse
  synchronisms. Rendering those in BP would be a downgrade.

So age is the wrong axis. What separates them is **where the date came from**.

### The principle

Writing "2500 BCE" asserts a position in a calendar. For any date before the calendar existed that
is a back-projection — a proleptic claim about a reckoning nobody was keeping. Sometimes that
projection is well anchored, because a chain of attested records, king lists, and datable
astronomical events connects it to our reckoning. Often it is not, and the BCE label is borrowed
authority.

BP makes no calendar claim at all. It is a count from a fixed datum, which is exactly the right
shape for a number that came out of a measurement.

> **Use BCE/CE when the date was *reckoned* — an inscription, a king list, an eclipse
> synchronism, a dated document. Use BP when the date was *measured* — radiocarbon, luminescence,
> potassium-argon, ESR.**

That line puts Alexander in BCE and Stonehenge in BP, which is the intuition it was built to
match. It also handles a case that looks like an inconsistency and is not: **Egyptian dynastic
dates come from king lists and Sothic observations, so they render BCE; Predynastic dates come
from radiocarbon, so they render BP.** Same region, adjacent nodes in the tree, different frames —
and that is correct, because they are different kinds of claim. A single frame across that
boundary would be the error.

### Both frames, one primary

The switch decides which frame *leads*, not which one exists. The readout can carry both:

```
Stonehenge, main sarsen phase
   4,500 cal BP        (primary)
   c. 2500 BCE         (secondary)
```

That defuses most of the anxiety about where the line falls. A user who thinks in BCE is never
locked out, and a borderline call costs a reordering rather than a loss.

### Calibrated versus uncalibrated

Radiocarbon has two scales and they are not interchangeable. Uncalibrated dates ("radiocarbon
years BP") assume a constant atmospheric ¹⁴C level that is not constant; calibrated dates
("cal BP") are corrected against tree-ring and other records. The gap reaches centuries in some
periods. The dataset should record which one a value is, and the readout should print the
distinction rather than flattening both to "BP" — `DatingMethod` already separates them.

### When method is unknown

Every entity in v2.1.0 has no `method` field, so a fallback is needed and it should be
conservative. Proposed order:

1. `method` is a measurement type -> **BP**
2. `method` is calendar or attested -> **BCE/CE**
3. `method` absent -> fall back on the *fuzziness*, not the age. A date whose uncertainty is a
   large fraction of its distance from the datum is doing measurement-shaped work whatever its
   provenance, so it renders BP. A tight date renders BCE/CE.
4. Backstop: anything pre-Holocene renders BP regardless, because no calendar reaches there.

Step 3 is the interesting one — it means the *shape of the uncertainty* substitutes for knowing
the provenance, which is a reasonable proxy and degrades honestly. It is also why the fuzzy date
model and the BP question turn out to be the same question.

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
- **Fuzzy dates are opt-in** (`Q-2`, settled). `start_year`/`end_year` stay primary; fuzzy fields
  are an optional overlay. Revisit migration after prehistory has exercised it.
- **The focus view is a second view alongside the Miller columns** (`Q-5`, settled), not a
  replacement. Columns answer "where am I"; the lens answers "what is near this".
- **BP versus BCE/CE is decided by provenance, not age** — measured dates render BP, reckoned
  dates render BCE/CE, and the readout can show both with one leading.
- **Consensus means the early-undergraduate value** (`Q-3`, settled), not the research frontier.
- **Dates are three independently-fuzzy anchors** (`Q-1`, settled); the trapezoid is superseded.
- **`D` blends temporal and tree distance** (`Q-6`, settled), with density normalization so the
  lens behaves consistently across sparse prehistory and dense modern history.
- **Focus+context uses `tier` as the a-priori-importance term**, so no new per-entity authoring is
  required to make the view work.

## Open items

The live register. `Q-n` ids are stable — reference them in commits and conversation. Ordered
roughly by how much else they block.

### Blocking — date model

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

**Q-11. Do entities carry month/day precision?** Now looks like yes — "September 11, 2001" was
given as the exact-end example. But `fuzz` measured in years cannot express day precision, so the
anchor needs either an optional month/day or a continuous day-count representation with fuzz in
days. The clean version is to store every anchor as a day count with fuzz in days: an exact date
is fuzz 0, `~3500 BCE` is fuzz 91,000 days. Uniform, but heavier to author and to read in JSON.

**Q-17. Where exactly does the unknown-method fallback switch?** Step 3 of the BP rule uses
relative fuzziness as a proxy for provenance. The ratio that trips it needs a value, and it should
be checked against real cases before being fixed.

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
