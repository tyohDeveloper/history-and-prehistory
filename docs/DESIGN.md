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

## Scope: a starting point, not a research tool

**Settled, and it constrains everything else.** This app shows how things relate and roughly when
they happened. It is a big-picture orientation surface. Anyone who wants the argument itself has to
go and read it elsewhere, and that is the intended outcome rather than a shortfall.

What the app owes a curious user is a good push in the right direction. What it does not owe them
— and could not honestly sustain across 1,305 entities — is a curated bibliography.

This resolves several open items at once:

- **Handoff links are generated, not authored.** A Wikipedia search URL built from the entity name
  costs nothing to maintain, cannot rot, and covers every entity including ones nobody has edited.
  Curating 1,305 article links would be a permanent maintenance liability for a marginal gain.
- **The `Source` registry is demoted from mechanism to exception.** It stays for the rare case
  where one specific work genuinely *is* the answer — a calibration curve, a named chronology —
  but it is not how most entities get backed up. See `Q-19`.
- **The disclosure popover stays short.** Name the complication in a sentence, then hand off. It
  is not the place to adjudicate a chronological dispute.

### Generated handoff

`/w/index.php?search=` is the right URL form: it redirects straight to the article when the query
matches one exactly, and falls back to the results page when it does not. A well-known subject
lands on its article; an ambiguous one lands somewhere useful. No tracking parameters.

Disambiguation is applied **exactly where ambiguity is known to exist**, by scanning the dataset
for repeated names rather than by guessing. The tree then supplies the discriminator a reader
would have supplied themselves:

| Entity | Generated query |
|---|---|
| Emperor Taizong (×2) | `Emperor Taizong Tang Dynasty` / `Emperor Taizong Northern Song` |
| Shōwa (×2) | `Shōwa Modern Japan` / `Shōwa Kamakura Period` |
| Jōwa (×2) | `Jōwa Heian Period` / `Jōwa Muromachi / Nanboku-chō Period` |
| Ancient Rome | `Ancient Rome` — unique, left alone |

This is the second job the tree does for free, alongside supplying the a-priori-importance term
for focus+context. Neither needed new per-entity authoring.

### Offline

Opened without a network, the link goes nowhere. That is accepted rather than engineered around —
and the app does **not** probe for connectivity. `navigator.onLine` is unreliable, and testing it
would be exactly the environment sniffing this app's privacy posture rules out.

Two affordances make the dead link survivable, and both work identically offline:

1. **The URL is shown as copyable text**, so it can be written down and run later.
2. **The selection exports as a plain-text research note** — hierarchy, dates, dating caveats, the
   search to run, and blank space to write in. Generated client-side via `Blob` +
   `URL.createObjectURL()`, which the standalone-HTML5 standard explicitly permits; nothing leaves
   the machine and no server is involved.

The note closes with "Dates are a starting point, not a citation. Verify before relying on them."
An app that hands people numbers should say what those numbers are worth.

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

### Recording and display are different decisions

BP and calendar reckoning are exactly interconvertible, so **which frame is shown is a UI
decision, never a storage one.** Any date can be rendered either way. Someone reading about Cyrus
may legitimately want BP, and nothing should prevent it. The provenance rule above therefore
supplies a *default*; an explicit user preference always wins.

What is *not* recoverable after the fact is the frame a source originally quoted in, and it
matters. A source reading "4500 BP" is quoting to the nearest century. Storing that as -2550 and
re-rendering it as "2550 BCE" silently claims a precision the source never offered. So
`nativeFrame` is recorded alongside the value, and the readout can show the source's own number
verbatim when displaying in that frame.

The practical split:

| Concern | Where it lives |
|---|---|
| Anchor values and fuzz | Data |
| Dating method (provenance) | Data |
| Frame the source quoted | Data (`nativeFrame`) |
| Which frame leads | UI default from provenance, user-overridable |
| Which frame is secondary | UI |

Low-precision material will in practice only ever have BP dates, and that is fine — it falls out
of the same mechanism rather than needing a special case.

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

## Progressive disclosure for complicated dates

Some dating situations are genuinely messy — radiocarbon disagreeing with king lists, the
high/middle/low variants of Egyptian chronology, a boundary that is an argument about definitions
rather than evidence. The readout must not explain all of that inline, and must not pretend it
does not exist.

**Show the basics; name the kind of complication; offer a way through.**

### Two surfaces: boundary dating, and entity caveats

Dating disclosure attaches to a **boundary**. The Roman Empire's start is uncontroversial; its end
is one of the most argued dates in the field — 476, 480, 1453 — and the argument is definitional
rather than evidential. Boundaries carry their own disputes, so `BoundaryDating` is per start and
per end.

But not every caveat is about a date, and auditing the existing dataset made that obvious. Its
three `misconceptions` entries are:

> "Ghana Empire was not located in the modern nation of Ghana."
> "Benin Empire was in southern Nigeria, not the modern nation of Benin."
> "The Maya never formed a single unified empire; they were a network of city-states."

None of those is chronological. They are geographic and conceptual corrections belonging to the
subject, and hanging them off a start date would be nonsense. So `EntityCaveat` is a second,
separate surface with its own kinds — `misconception`, `naming-confusion`, `contested-existence`.

`naming-confusion` earns its own kind because the pattern is everywhere in history: Ghana, Benin,
the Holy Roman Empire, the Byzantine Empire, Latin America. And it matters more than most caveats
for this audience — a reader who leaves believing the Ghana Empire sat in modern Ghana has been
actively misled, which is worse than being left uncertain.

`contested-existence` moved here too. Whether Gilgamesh or David existed is a question about the
subject, not about a boundary. The dataset already flags Gilgamesh as legendary.

### Rival claims are not one wide range

Competing chronologies are not imprecision. Flattening three rival positions into a single fuzzy
interval misrepresents all three: it implies the middle is likeliest, when the actual claim is
that the field disagrees about which is right. So alternatives are separate `DatingClaim`s, each
with its own value, label, standing, and sources.

`standing` separates `traditional` from the rest deliberately. "Rome founded 753 BCE" and "Narmer
c. 3100 BCE" are received dates, not findings, and giving them the same weight as measured or
attested dates is the commonest way a history reference misleads. The dataset already flags a few
with `date_precision: "traditional"`; this promotes that from a precision flag to a statement
about standing, which is what it always was.

### The marker names the complication

A generic asterisk makes every complication look alike. They are not alike — "scholars disagree"
and "depends where you draw the line" call for completely different reading, and a user should be
able to tell which awaits before deciding to open anything.

| Reason | Marker reads | Inferred? |
|---|---|---|
| `rival-chronologies` | Chronologies differ | yes, from alternatives sharing a method |
| `method-conflict` | Methods disagree | yes, from alternatives with differing methods |
| `definitional` | Depends on definition | **no — must be authored** |
| `traditional-date` | Traditional date | yes, from `standing` |
| `overlaps-parent` | Crosses its period | yes, from `outsideParent` |
| `calibration` | Calibration-dependent | no |
| `wide-uncertainty` | Broad range | yes, from fuzz vs. age |

Five of the seven are derived, which is deliberate: authoring effort should go to the reasons that
genuinely need a human. Nothing about the number 476 reveals it is a definitional choice, so that
must be written down. That a claim marked `traditional` is a traditional date does not.

**`overlaps-parent` is the commonest real case and the model originally had no room for it.**
27 entities carry `allow_outside_parent_dates`: Oda Nobunaga's rule begins before the era named
after him, and nengō routinely straddle period boundaries. Nothing is disputed and nothing is
wrong — but it looks like a data error, and "this is intentional" is exactly the kind of thing a
starting-point tool should say. Note this is the *opposite* of a dispute, which is why it needs
its own wording rather than a shared marker.

When several apply, `disclosureSummary()` returns the most consequential by fixed priority:
`definitional` > `rival-chronologies` > `method-conflict` > `traditional-date` >
`overlaps-parent` > `calibration` > `wide-uncertainty`.

### Claim ordering, and never hiding a superseded date

Primary always leads. The rest sort by standing: consensus, majority, minority, traditional,
superseded.

Superseded claims sort last but are **never hidden**. A reader who met the old date somewhere else
needs to find it here and be told it is old. Dropping it silently leaves them concluding the app
is wrong, which is the worst of the available outcomes.

### Each claim renders in its own frame

Where claims disagree because their *methods* disagree, they will usually want different frames —
the radiocarbon claim in BP, the king-list claim in BCE. The popover renders each in its own
frame rather than forcing one, because the frame difference is part of what the reader needs to
see. Forcing a common frame would hide the very distinction the disclosure exists to surface.

### Brevity is enforced

`MAX_CAVEAT_LENGTH` caps notes and caveats at 200 characters. Prose is where "starting point, not
research tool" quietly erodes; a hard limit keeps a caveat to something absorbed in passing and
pushes anything longer out to the handoff link, where the argument belongs.

### Render contract

- **No disclosure** — the date line renders plain. `hasDisclosure()` is false and nothing is
  added. A marker on every date is the same as no marker; it stops carrying information.
- **Disclosure present** — the date line gets a dotted underline plus the summary phrase in small
  caps beside it. The phrase is the affordance; it is not hidden behind a hover.
- **Opened** — a popover lists every claim with its label, value, standing, and method; then the
  note; then sources as named links. Primary first, visually distinguished.
- **Accessibility** — the marker is a real `<button>`, reachable by keyboard and touch, with
  `aria-expanded` and `aria-controls`. Hover is never the only route. At the `specialist` tier,
  alternatives may render inline rather than behind the popover.
- **Test IDs** — `button-disclosure-{boundary}`, `panel-disclosure-{boundary}`,
  `list-disclosure-claims`, per `ARCHITECTURE.md` §8.

### Sources: the exception, not the mechanism

Given the scope decision above, most entities are backed by a generated search link rather than a
citation. The `Source` registry remains for the minority of cases where a specific work is the
substance of the claim — IntCal20 for a calibration, a named chronology for an Egyptian date.

Where it is used, sources live in an id-keyed `sources.json` referenced by id. Deduplication is
the reason: one chronology reference cited by two hundred entities is stored once, not two hundred
times, in a bundle under budget. The dataset already normalizes calendars and themes this way.

`kind` distinguishes `scholarly`, `reference`, `primary`, and `dataset` — a Wikipedia link and an
excavation report are not the same sort of backing.

The gap-analysis complaint that `sources` is empty on all 1,305 entities (§5.2) is therefore
**partly withdrawn**. Universal per-entity sourcing was the wrong target for a tool of this scope.
What the sources page should list is the dataset's own provenance plus the handful of curated
works behind contested dates — not 1,305 citations.

### Migrating from v2.1.0

The existing dataset already carries most of this in weaker form. The mapping:

| v2.1.0 field | Uses | Maps to |
|---|---|---|
| `date_precision: "traditional"` | 8 | `standing: "traditional"` — resolves `Q-20`, yes migrate |
| `allow_outside_parent_dates` | 27 | `outsideParent: true` -> `overlaps-parent` |
| `date_note` | 33 | Boundary `note`. Mostly explains overlap, not dispute |
| `misconceptions` | 3 | `EntityCaveat` — split by kind between misconception and naming-confusion |
| `start_year_min/max`, `end_year_min/max` | 3 | Fuzzy anchors on `earliest`/`latest` |
| `sources` | 0 | Registry ids, where curated at all |

Two things fall out of this audit. First, `date_note` and `allow_outside_parent_dates` overlap
almost exactly — nearly every note explains an overlap. That is a strong signal the model was
missing the concept, which it was. Second, the traditional dates are exactly the eight one would
predict: Narmer, Gojoseon, Gilgamesh, David, Solomon, the Roman Kingdom, Romulus Augustulus,
Nitocris. Legendary founders and dynastic origin stories. The existing authoring was right; it
just lacked a field that said what it meant.

### Measured against the real dataset

The model is no longer hypothetical: `src/lib/chrono/fromEntity.ts` adapts a v2.1.0 `Entity` into
it, so the migration map above is executable and testable rather than aspirational. Running it
over all 1,305 entities:

| Metric | Value |
|---|---|
| Dated boundaries | 2,500 |
| Boundaries showing a marker | 49 — **2.0%** |
| Entities needing boundary review | 33 |
| Entity caveats produced | 5 |

**2.0% is the number that matters.** A disclosure marker only works while it stays rare; one that
appears on most records stops being read and becomes decoration. Two percent means it retains
signal. It is also a budget: if authoring pushes marker density past roughly one in ten, the
mechanism has been over-applied and it is the authoring that should change, not the threshold.

Marker breakdown — only two reasons fire on current data:

- `overlaps-parent` — **27**, over half of all markers
- `traditional-date` — 16 (8 entities × two boundaries)

`rival-chronologies` and `method-conflict` cannot fire yet because nothing has alternatives
authored. `wide-uncertainty` does not fire because only three entities carry bounds at all, and
those are well constrained. Both will activate with prehistory.

That `overlaps-parent` is the single commonest disclosure in the real data — a reason the model
did not have until the audit — is the clearest evidence the audit was worth doing.

### Two defects the measurement exposed

**The uncertainty ratio used the wrong denominator.** It divided by `|year|`, which collapses
toward year zero: a date of 1 CE with a five-year error scored a ratio of 5.0, so everything near
the era boundary read as wildly uncertain. Fixed to use distance from the BP datum, which is
monotonic across the whole range and never collapses.

The fix also produces better *judgement*, not merely better arithmetic. The same fifty-year error
is unremarkable on a Bronze Age date and glaring on a Victorian one, and the datum-relative metric
reproduces that automatically — which is how historians read precision anyway.

**Eight entities marked the same thing twice.** Every legendary founder — Narmer, Gojoseon,
Gilgamesh, David, Solomon, the Roman Kingdom, Romulus Augustulus, Nitocris — has a traditional
accession *and* a traditional death, so both boundaries produced "Traditional date". Rendering it
twice on one record is exactly the noise a marker cannot afford. `rollupDisclosure()` collapses
identical markers into one entity-level statement.

### The caveat classifier

The one-time migration heuristic in `classifyCaveat` got all five right:

| Entity | Assigned | Source text |
|---|---|---|
| Ghana Empire | `naming-confusion` | "not located in the modern nation of Ghana" |
| Benin Empire | `naming-confusion` | "in southern Nigeria, not the modern nation of Benin" |
| Maya Civilization | `misconception` | "never formed a single unified empire" |
| Gilgamesh (legendary) | `contested-existence` | inferred from the display name |
| Nitocris (traditional) | `contested-existence` | inferred from the display name |

It is deliberately conservative — only an explicit name-versus-place construction promotes to
`naming-confusion`. Erring toward the generic label costs a slightly vague heading; erring the
other way would file a factual correction under a heading that misdescribes it. Delete the
function once the field is authored directly.

### Migration is lossy in one specific way

v2.1.0 stores `date_note` and `allow_outside_parent_dates` **per entity**, while disclosure
attaches **per boundary**. The old schema cannot say which end a note is about, and the notes
themselves show why that matters: "Oda Nobunaga's rule began 1568, before the formal era start" is
plainly about the start, while "nengō 782–806 spans the Nara–Heian boundary" is about neither end
in particular.

The adapter attaches both to the start boundary — right more often than not — and sets
`needsBoundaryReview`. **33 entities carry that flag** and want a human pass before the migration
is trusted.

### Stress-tested against eight real prehistory cases

Prehistory was where this model was most likely to break, so it was tested against real cases with
real disputes rather than invented fixtures. Sourced values are in
[`prehistory-dating-research.md`](prehistory-dating-research.md); the cases are encoded in
`tests/prehistory.test.ts`. Four changes came out of it.

| Case | Stresses | Outcome |
|---|---|---|
| Oldowan, c. 2.6 Ma | Ma scale, definitional | Lomekwi 3 at 3.3 Ma excluded by *naming* it Lomekwian |
| *H. floresiensis* | Large revision, ~18 ka → ~60 ka | Forced the `revised` reason |
| Chauvet Cave | Evidence challenged, not dated | Forced `evidence-disputed` |
| Madjedbebe, 65 ± 6 ka | Rival readings of one OSL programme | Handled |
| Neanderthal extinction | Contamination-driven revision | Forced `revised` |
| Younger Dryas | b2k datum, ±99 yr counting error | Forced datum support |
| Göbekli Tepe | Definitional; phase scheme abandoned | Handled |
| Monte Verde II | Live dispute, mid-2026 | Forced `asOf` |

#### 1. b2k is a separate datum, not a rounding detail

Ice-core chronologies quote **b2k** — years before 2000 CE — while radiocarbon uses BP at 1950. A
50-year systematic offset. It sounds negligible and is not: the Younger Dryas termination is
11,703 b2k with a maximum counting error of 99 years, so silently treating b2k as BP moves the
date by **half its own stated uncertainty**. The literature is explicit about this, and the advice
for datasets is to store b2k, BP, and BCE separately with the offset applied.

`b2k` is therefore a first-class display frame, and a quoted `nativeFrame` now wins over every
other rule in `suggestFrame()` — it is the only way to reproduce a source's own number, including
its datum and its rounding.

#### 2. A settled revision is not a live disagreement

The sharpest finding, and the model got it wrong before these cases were tried. *H. floresiensis*
moved from ~18 ka to ~60 ka in 2016 when the dated deposits turned out to be a younger unit
overlying the remains. Neanderthal late survival at 28 ka collapsed once ultrafiltration removed
modern-carbon contamination from old bone.

Both produced two claims with different methods, so the model reported **"Methods disagree"** —
which is false. They agreed; one side lost. A reader told there is a live methodological argument
about Flores would take away something untrue.

So when *every* alternative is `superseded`, the reason is `revised` — "Date revised" — and
superseded claims are now excluded when deciding whether live claims conflict, so a dead claim's
method cannot manufacture a disagreement among living ones. The old value stays reachable, because
readers meet ~18 ka in books published before 2016 and need to find it here.

#### 3. Challenging the evidence is not offering a rival date

The Chauvet critique does not propose a better number from a better method. It argues the
radiocarbon dates charcoal rather than paint, so the technique does not date the art at all.
`method-conflict` would tell a reader to expect a competing figure, and none is on offer.
`evidence-disputed` — "Evidence questioned" — is its own reason, and it outranks everything else
in the priority order.

Madjedbebe is the useful contrast: both sides run OSL, and the argument is about stratigraphic
integrity. Same evidence type, rival readings, so `rival-chronologies`. The model now separates
the three cleanly.

#### 4. Open disputes need a shelf life

Monte Verde II is under active challenge as of mid-2026: a March 2026 reanalysis proposed a
Holocene age some six thousand years younger, roughly thirty specialists rebutted it in May, and
the authors replied in June. Recording that state is genuinely useful. Recording it *without a
date* is a trap, because a reader cannot tell whether the argument was resolved last week.

`asOf` carries an ISO review date, and only where a dispute is genuinely open — settled dates do
not get one, and a validator should reject them if they do.

#### What did not need changing

Deep-time rendering held up unmodified. The Oldowan quotes as `2.6 Ma` rather than a spurious
seven-digit year, Chauvet in `ka`, and the uncertainty-driven rounding produced sensible output at
every scale from 99 years to 68,000. The Younger Dryas termination — precise, ratified, and
uncontested — correctly shows **no marker at all**, which is the behaviour that makes the marker
worth having on the other seven.

### Validator rules this implies

Enforceable in `tools/validate.py`, and worth enforcing because each catches a real authoring
failure:

1. `alternatives` non-empty requires `note` — if claims differ, say why.
2. `standing: "superseded"` requires a `note` or a sourced replacement — superseded by what?
3. Every `sourceIds` entry must resolve in the registry (referential integrity, as for themes).
4. `reasons` containing `definitional` or `contested-existence` requires `note` — these cannot be
   inferred, so an unexplained one is an authoring stub.
5. At most one claim per boundary with `standing: "consensus"`.
6. Warn when a registry source is cited by nothing.
7. Notes and caveats must not exceed `MAX_CAVEAT_LENGTH`.
8. `outsideParent: true` requires a `note` — "this is intentional" is useless without saying why.
9. An `EntityCaveat` of kind `contested-existence` should pair with `standing: "traditional"` on
   the entity's dates, or explain why not.
10. `asOf` is required when any alternative has live standing, and forbidden when every
    alternative is `superseded` — a settled question has nothing to re-check.
11. A value with `nativeFrame: "b2k"` must carry a `layer-counting` or otherwise ice-core method;
    b2k on a radiocarbon date is almost certainly an authoring slip.

### Offline constraint

Wikipedia links and citation lists are permitted: user-initiated navigations to public static
content, new tab, `rel="noopener noreferrer"`. Fetching any of it at runtime is not — the CSP sets
`connect-src 'none'` and the build check greps for `fetch`. Popover content inlines at build time;
only the outbound click touches the network. See `ARCHITECTURE.md` §2 and §10.

Bundle consequence, tracked against `Q-16`: claims and sources across many entities will grow the
dataset materially. The registry keeps that linear in distinct sources rather than in citations.

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
- **Frame is a display choice, overridable by the user.** Provenance sets the default only.
  `nativeFrame` records what the source quoted so precision is not inflated by conversion.
- **Rival chronologies are separate claims, not one wide range**, revealed by an on-demand popover
  rather than shown inline.
- **Disclosure attaches to a boundary, not an entity** — a start and an end carry different
  arguments.
- **The marker names the kind of complication** rather than showing a generic mark, and four of
  the seven reasons are inferred so authoring effort goes where a human is actually needed.
- **Sources are a normalized id-keyed registry**, not inlined per entity — and used only where a
  specific work is the substance of the claim.
- **Entity caveats are a second surface**, separate from boundary dating: misconceptions and
  naming confusions are not chronological.
- **Superseded claims are ranked last but never hidden.**
- **Notes and caveats are length-capped** at 200 characters.
- **Marker density budget: 2% today, ~10% ceiling.** Past that the mechanism is over-applied and
  authoring should change, not the threshold.
- **Identical markers on both boundaries collapse** to one entity-level statement.
- **b2k is a first-class datum**, and a quoted `nativeFrame` overrides every other frame rule.
- **A settled revision is not a dispute.** All-superseded alternatives read as "Date revised", and
  superseded claims are excluded when testing whether live claims conflict.
- **Open disputes carry an `asOf` review date**; settled ones must not.
- **The app is a starting point, not a research tool.** Handoff links are generated from the
  entity; the offline answer is a copyable URL and a downloadable research note, not a
  connectivity probe.
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

**Q-21. Which Wikipedia edition, and what about native script?** English is the default. An entity
with a `native_name` might search better on the matching language edition, but inferring language
from script is unreliable (Han characters span at least three). Options: English only, offer both
with the native search on English Wikipedia, or add an explicit `wiki_lang` field.

**Q-18. Is the frame preference global, per-entity, or both?** A global "always BP" toggle is
simple. A per-entity override is more precise but adds state the URL fragment would have to carry.

**Q-17. Both fuzziness thresholds are unvalidated.** `UNKNOWN_METHOD_FUZZ_RATIO` (0.05, chooses BP
over calendar) and `WIDE_UNCERTAINTY_RATIO` (0.10, trips the broad-range marker) are currently
guesses. Only three entities carry bounds, so tuning against them would be overfitting to three
data points. Revisit once prehistory supplies real ranges. The one encouraging sign: the canonical
worked example — ~3500 BCE (3000 .. ~4500 BCE) — trips the broad-range marker at 27%, comfortably
clear of the threshold.

**Q-23. What happens when an `asOf` goes stale?** A date-stamped open dispute is only honest while
someone re-checks it. Options: surface the age in the UI ("last checked 2026-06"), fail a build
check past some horizon, or accept drift. Nothing is decided.

**Q-24. Should `revised` claims show by default or stay behind the popover?** They are settled, so
inline display is arguably noise — but the whole reason to keep them is that readers arrive
holding the old number and need to collide with it.

**Q-22. Who reviews the 33 flagged boundary attachments?** Migration cannot infer which boundary an
entity-level note belongs to. The flag is set; the pass is not scheduled.

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
- ~~`Q-20` Migrate `date_precision: "traditional"` to `standing`?~~ — yes. Eight entities, all
  legendary founders or dynastic origin stories; the field was always about standing, not
  resolution.
- ~~`Q-19` Must a consensus claim be sourced?~~ — no. The app is a starting point and does not
  claim scholarly authority; generated handoff replaces per-entity citation.
- ~~Per-app repos or monorepo~~ — per-app, settled 2026-08-07.
- ~~GitHub issues or design docs~~ — design docs, for now.

## Not yet built

Year-to-calendar span conversion, the ambiguity-preserving input parser, the multi-calendar
readout, calendar selection UI, and tests for any of it.
