# Design notes

**The primary living design document for this app.** Decisions, findings, and the open-items
register all live here. Open items are tracked as `Q-n` entries in §Open items rather than as
GitHub issues — issues are too formal for this stage, and the questions are too interdependent
to read well one at a time. Revisit that choice when the register stops changing shape.

## Where things stand

| | |
|---|---|
| Branch | Merged to `main`. `calendar-layer` retained but no longer ahead. |
| Wired into the UI | Multi-calendar readout, calendar picker, and the display-range layer. Disclosure and focus view are not. |
| Tests | 166 unit + 20 browser |
| Artifact | 108.9 kB gzip |
| Dataset | v3.1.0 on schema 2.0.0. 1,417 entities. Prehistory attached in all ten regions. |
| Replit | Repo is loaded there but dormant by choice; no commits from it yet |
| Last reviewed | 2026-08-07 |

Enough is built to prove the shape and expose the decisions that still need making. The app
itself still behaves exactly as the v0.1.0 baseline does.

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
| `src/temporal/temporal.ts` | Source-selection shim re-exporting `temporal-polyfill/full`. Ported from OmniUnit unchanged in substance, so both apps make the same choice the same way. |
| `src/temporal/julianJdn.ts` | Fliegel–Van Flandern JDN converters for Julian and Revised Julian, which Temporal does not implement. Ported verbatim. |
| `src/calendars/registry.ts` | 26 calendars with validity horizons, primary/variant grouping, and per-calendar caveats. |
| `src/chrono/year.ts` | Branded `IsoYear`/`HistoricalYear` types and the four sanctioned crossings. The core model: three independently-fuzzy anchors, dating method and datum, claim standing, disclosure reasons and inference, entity caveats, rollup. |
| `src/chrono/bp.ts` | BP and b2k datums, `yr`/`ka`/`Ma` scaling, uncertainty-driven rounding, and frame selection with user override. |
| `src/chrono/fromEntity.ts` | Adapter from a v2.1.0 `Entity` into the model, so the migration map is executable rather than aspirational. Includes the one-time caveat classifier. |
| `src/calendars/convert.ts` | Reads an ISO year in any of the 26 calendars, as a span, with validity. |
| `src/calendars/selection.ts` | Calendar choice parsed from and written to `location.hash`. |
| `src/research/handoff.ts` | Generated Wikipedia search links with dataset-measured disambiguation, plus the exportable research note. |

Tests: `tests/chrono.test.ts` (model), `tests/prehistory.test.ts` (eight real dating disputes),
`tests/handoff.test.ts`, alongside the baseline `tree` and `dataset-integrity` suites.

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

The model is no longer hypothetical: `src/chrono/fromEntity.ts` adapts a v2.1.0 `Entity` into
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
12. Warn when a boundary carries wide bounds and the entity also has a sibling boundary — a
    period's extent has probably been collapsed into one fuzzy date.

### Offline constraint

Wikipedia links and citation lists are permitted: user-initiated navigations to public static
content, new tab, `rel="noopener noreferrer"`. Fetching any of it at runtime is not — the CSP sets
`connect-src 'none'` and the build check greps for `fetch`. Popover content inlines at build time;
only the outbound click touches the network. See `ARCHITECTURE.md` §2 and §10.

Bundle consequence, tracked against `Q-16`: claims and sources across many entities will grow the
dataset materially. The registry keeps that linear in distinct sources rather than in citations.

## Canonical representation, and whether a date round-trips

Three questions, one architecture. Answered by measurement against the polyfill.

### Does an Islamic date survive conversion to Common Era and back?

**At day precision, yes, exactly.** 252 of 252 round trips across twelve calendars returned the
identical date, with zero loss. Calendar conversion at day granularity is a bijection — every
calendar day is one day, and the mapping is reversible.

**At year precision, no — and not "sometimes", but always.** Measured over a century of Gregorian
years:

| Calendar | Gregorian years spanning two of its years |
|---|---|
| Islamic (Umm al-Qura) | **100 / 100** |
| Hebrew | **100 / 100** |
| Persian | **100 / 100** |
| Chinese | **100 / 100** |

None of those calendars starts its year on 1 January, so every Gregorian year straddles two of
theirs. "897 AH" reduced to a Gregorian year and converted back is genuinely ambiguous between 897
and 898. The arithmetic is not at fault: the information was destroyed by reducing to year
precision, and no conversion can recover it.

This generalises the nengō result. There it was 43% of years; for lunar and solar-Hijri calendars
it is all of them.

**Consequence:** where a source states a date in its own calendar, keep the source's own number.
`NativeValue` records it verbatim alongside the canonical value. Displayed in its native calendar
a date then shows exactly what the source said; displayed elsewhere it shows a conversion that can
be hedged. This is the same argument as `nativeFrame` for b2k, generalised.

### Should ISO be the underlying representation?

**Yes for internals, no for the JSON.** Taking the parts separately:

**ISO astronomical numbering internally.** The year-zero discontinuity is a genuine source of
off-by-one errors, and astronomical numbering removes it. BP becomes plain subtraction —
`1950 − isoYear`, no branching. Temporal already uses ISO natively, so there is no conversion at
the arithmetic boundary. And CE/BCE stops being privileged: it becomes one display transform among
twenty-six, which is exactly the right shape given CE/BCE and BP are the two standard frameworks
and everything else is presentation.

There is a subtle argument in favour that is easy to miss. Today `toAstronomical` is called inside
every BP computation — the crossing happens repeatedly, in logic. With ISO internal, the crossing
happens **once at load**, at the I/O boundary. Fewer sites, all auditable, none inside arithmetic.

**Historical numbering in the JSON.** All 1,305 entities already use it, historians write BCE, and
a migration off-by-one would be almost undetectable by review — `-753` and `-752` both look
plausible for the founding of Rome. The dataset should stay human-auditable. Convert once, on load,
in `fromEntity.ts`.

### Temporal cannot hold deep time, and that decides the shape

Verified: `Temporal.PlainDate` throws a `RangeError` beyond roughly ±271,821 years. Asking for
3.3 Ma fails outright. So ISO **cannot** be the single canonical representation, whatever else is
decided.

That is not a limitation to route around. It marks a real boundary between two kinds of quantity:

| | Date regime | Deep-time regime |
|---|---|---|
| Range | within ±271,821 years | beyond it |
| A value is | a **date** | a **number of years** |
| Calendars | all 26 meaningful | none reach here |
| Round-trip | exact at day precision | n/a |
| Frames | CE/BCE, BP, b2k, any calendar | BP / ka / Ma only |

`DATE_REGIME_LIMIT_YEARS` and `isDateRegime()` make the seam explicit. It sits far outside any
calendar's meaningful range — the oldest calendar epoch in the registry is Byzantine AM at
5508 BCE — so it never bisects anything a user would expect to convert.

### The resulting three layers

```
Authoring   historical Gregorian in JSON, plus NativeValue where a source
            quoted another calendar          -753 = 753 BCE
     |      converted once, at load
Canonical   date regime:      ISO astronomical year (+ optional month/day)
            deep-time regime: years before datum, as a scalar
     |      one transform per target
Display     CE/BCE · BP · b2k · any of 26 calendars — none privileged
```

CE/BCE and BP remain **the two standard frameworks** as a product decision: they are the most
widely understood, and they are what the readout leads with. But architecturally they are now
ordinary consumers of the canonical layer, not the canonical layer itself. That is the change the
ISO proposal buys, and it is worth having.

### The native date is the fact; ISO is the index

Where a good date exists in its own cultural calendar, **store both, and treat the native one as
authoritative.** ISO remains the single model — it is what everything is indexed, sorted, and
compared on — but it is a derived cross-reference, not the underlying truth.

The Battle of Karbala happened on **10 Muḥarram 61 AH**. That is the date. It is ʿĀshūrāʾ, it is
observed annually on a Hijri anniversary, and that anniversary has no fixed Gregorian counterpart.
"13 October 680" is something we compute so the event can be placed beside Tang China. Useful, and
not what happened.

#### The conversion is less precise than the original

Measured against the polyfill for 10 Muḥarram 61 AH:

| Hijri variant | Proleptic Gregorian |
|---|---|
| `islamic-umalqura` | 0680-10-13 |
| `islamic-civil` | 0680-10-13 |
| `islamic-tbla` | 0680-10-12 |

A **two-day spread on a date the source knew exactly**, and each variant round-trips its own value
perfectly. The uncertainty is manufactured by the conversion; it is not carried by the original.

This runs opposite to the usual assumption that the stored canonical value is the precise one and
displays are approximations. `conversionFuzzDays` records it, so a readout neither presents a
derived date as sharper than the derivation allows, nor lets the derivation cast doubt on a native
date that has none.

(Historians usually quote Karbala as 10 October 680 in the **Julian** calendar, which the app's own
JDN module handles — Julian and proleptic Gregorian differ by three days in the seventh century.
Three defensible answers, and only the Hijri one is exact.)

#### Display consequence

`hasAuthoritativeNative()` is true when a native form exists, and the readout then **leads with
it**, offering ISO as the cross-reference rather than the reverse. This is a per-entity decision
derived from the data, not a user preference — relevant to `Q-18`, which asked whether frame
choice is global or per-entity. Part of the answer is now "neither": some entities carry their own.

### One axis, two kinds of view

The observation that **BP is just an extension of the ISO calendar** tidies the whole taxonomy, and
it is worth stating explicitly because the registry currently blurs it.

There is **one axis** — ISO astronomical day and year — and two different things layered on it:

| | Examples | Nature |
|---|---|---|
| **Origin views** | CE/BCE, BP (1950), b2k (2000) | Pure subtraction on the axis. Not calendars. |
| **Structural transforms** | Hijri, Hebrew, Chinese, nengō, +22 more | Own month and year structure. Genuinely different. |

CE/BCE is an origin view with a numbering quirk (no year zero). BP and b2k are the same axis with
the origin moved, which is why `bpFromYear` is one subtraction and why BP needed no separate
machinery. The 26 calendars are the only things that are structurally different, and they are the
only things that need Temporal.

So the standard frameworks — CE/BCE and BP — are not two of twenty-eight options. They are two
origins on the one axis everything is measured against, which is exactly why they can be the
defaults without privileging any culture's calendar structure.

### The ISO refactor, and how it was made safe

**Done** (`Q-27`). Internals now carry ISO astronomical years; the dataset keeps historical
numbering; the crossing happens once, in `fromEntity.ts`.

The hazard was never the arithmetic — it was that **every wrong answer looks right**. `-753` and
`-752` are both entirely plausible for the founding of Rome, so a mixed-up value survives review
indefinitely and surfaces years later as an unexplained one-year drift. A convention would not
have held. So the two schemes are now **distinct types**:

```ts
type IsoYear        = number & { readonly [IsoYearBrand]: true };
type HistoricalYear = number & { readonly [HistoricalYearBrand]: true };
```

Branding is compile-time only, so it costs nothing at runtime, and it makes the entire class of
error unwriteable rather than merely discouraged. Four functions are the only sanctioned crossings
— `isoFromHistorical`, `historicalFromIso`, `asHistorical`, `asIso` — and everything else takes one
type or the other.

**The refactor immediately proved the point.** Introducing the types surfaced **137 compile errors**
across the codebase: every place the two schemes met, listed. Two were real bugs in library code;
the rest were fixtures. Without branding those would have been silent.

Two readable constructors carry the intent at every hand-written site:

```ts
bce(753)   // 753 BCE  -> ISO -752
ce(1492)   // 1492 CE  -> ISO 1492
```

`bce(753)` says what it means. `-752` does not, and `-753` is wrong. Fixtures written this way are
*more* legible after the refactor than before, which is unusual for a numbering migration.

One test caught the shift honestly: an expectation of `{ earliest: -5000, latest: -3000 }` became
`{ earliest: -4999, latest: -2999 }` — correct, since those are 5000 BCE and 3000 BCE in ISO. It is
now written `{ earliest: bce(5000), latest: bce(3000) }`, where the intent is unmistakable.

**What it bought.** `bpFromYear` is now one subtraction. Before, it called `toAstronomical` on every
invocation, so the year-zero crossing happened inside arithmetic, at every call site wanting a BP
value. Now it happens once at load. That is the whole justification for the change, and it is why
BP really is just the ISO axis with its origin moved.

`tests/iso-migration.test.ts` round-trips **every dated boundary in all 1,305 entities** through
both conversions, checks BCE shifts by one while CE does not, and verifies that 1 BCE and 1 CE come
out exactly one year apart in BP despite there being no year zero between them in the dataset.

## The conversion layer (built)

`src/calendars/convert.ts` reads an ISO year in any of the 26 calendars. This is the commit
that imports `temporal-polyfill/full` and re-baselines the artifact.

### A reading is a span, and carries its own validity

Two things travel with every result because callers cannot be trusted to remember them.

**Spans, not points.** Only calendars whose year begins on 1 January map one Gregorian year to one
of theirs. 1603 CE is 1011–1012 AH and 5363–5364 AM. Rendering a lunar year as one number would be
wrong about half the time.

**Validity.** Every conversion is *computable* far outside where it means anything — the polyfill
returns Persian year -3521 for a Sumerian date without complaint. `readYear` never throws and never
returns a bare number it does not believe, so a caller rendering a table of twenty-six calendars
does not have to guard each cell.

### Three bugs the visual check caught that tests did not

Worth recording, because all three were invisible to the unit suite and obvious on screen.

1. **A BCE year rendered identically to a CE one.** Reading `eraYear` off a Gregorian conversion
   returns `2900` for 2900 BCE, with the era in a *separate field* — so the readout showed "2900".
   Fixed by not routing origin views through Temporal at all: CE/BCE, AD/BC and raw ISO are the
   axis with a label, not structural calendars, so `withCalendar` buys nothing and costs
   correctness. This is the origin-versus-transform distinction paying for itself in code.

2. **Pre-epoch extrapolations printed nonsense, in two different spellings.** Persian returns a
   negative year (`-3521–-3520 AP`); Islamic returns a *positive* year in a Before-Hijra era that
   counts **down** (`3630–3629 AH`), which reads as a broken range. A sign check catches the first
   and misses the second. Now detected from the epoch rather than the sign, and both render
   "before epoch" beside the flag — a number on top of "extrapolated" is noise dressed as data.

3. **Years carried thousands separators** — "2,900 BCE". Years are conventionally written
   unseparated, and the gutter already did. Separators stay for BP and ka, which are quantities
   rather than years.

### Selection lives in the URL

`location.hash` carries the chosen calendars, so persistence is the user's decision: bookmark the
link and it survives, close the tab and it does not. The only mechanism compatible with both the
no-storage rule and `file://`.

The app also listens for `hashchange`. Without it the fragment is write-only — pasting a link with
`#cal=…` into an open tab, or pressing back after changing calendars, would silently do nothing.

Capped at six calendars, and a hand-edited URL is filtered against the registry rather than
trusted.

### Bundle

**56.4 kB → 84.2 kB gzip.** Slightly above the ~80 kB projection, the difference being the
conversion layer and picker UI on top of the polyfill itself.

The regression gate did its job: the build failed with *"Gzip 84.2 kB exceeds baseline ceiling
59.2 kB — bundle regressed"* before the baseline was re-recorded deliberately, with the reason
written into `build-baseline.json`. That is the intended workflow — the number moves in a commit
that justifies it, not because someone edited it to make CI pass.

## Q-10 unblocked: the builders, the schema, and a pilot

**Done.** This was the keystone — every data-side task waited on it, and nothing could be authored
regardless of how good the model got.

### What was actually blocking

Not a missing feature. `R()` and `P()` were defined **three separate times**, as closures inside
each extension's `extend()`, each with a hand-written keyword list:

```python
def R(slug, name, parent, s, e, tier="specialist", summary=None, aliases=None):
```

That signature is the entire reason seven schema fields were unused across 1,305 entities. An
author could not populate `date_note` or `sources` because the builder had nowhere to put them,
and the natural fix — adding a keyword to one of the three copies — deepened the divergence.

`tools/builders.py` now provides one shared set taking `**kw`. Migrating to it surfaced two traps
that a search-and-replace would have silently shipped, and did:

- **Roman emperor ids sit flat under `<rome>.empire`** while `parent_id` points at the dynasty, so
  id and parent genuinely diverge. A naive swap relocated 121 emperors.
- **`P` in the Rome/Egypt module means *pharaoh*, not *period*** — it emits reigns. The same letter
  means "period" in the South Asia module. Two files, one name, opposite meanings.

Both were caught because `check_regenerated.py` diffs the regenerated dataset against the
committed one. Output is now **byte-identical** to before the refactor, which is the proof the
migration changed nothing it should not have.

The allowlist is **derived from the schema at import time** rather than hand-maintained, so the
two cannot drift — the failure mode that created the problem. A typo fails where it was written,
naming the entity, instead of surfacing as a JSON pointer into a 400 kB generated file. It caught
a real one during this work: `source_ids` was added to the schema and not to the list.

### Schema 1.1.0

Eight optional fields, so every 1.0.0 document stays valid: `subkind`, `dating_method`,
`standing`, `as_of`, `native_date`, `alternatives`, `caveats`, `source_ids`. Plus `sources.json`
as a normalized registry.

### Five validator rules, and proof they fire

Rules 1, 2, 5, 6, 10 and 11 from the list above are implemented. Each was verified by deliberately
breaking the data and confirming the objection:

| Broken | Caught |
|---|---|
| `source_ids` pointing at nothing | ✅ unresolved reference |
| alternatives with no `date_note` | ✅ "has alternatives but no date_note explaining why they differ" |
| `as_of` with no open dispute | ✅ "no open dispute to re-check" |

### The pilot

Five prehistory entities — Human Prehistory, Oldowan, Göbekli Tepe, *Homo floresiensis*, Monte
Verde II — chosen to exercise every unlocked field at least once. Fields that were **0/1305**:

| Field | Now |
|---|---|
| `dating_method` | 4 |
| `standing` | 4 |
| `source_ids` | 4 |
| `alternatives` | 2 |
| `caveats` | 1 |
| `as_of` | 1 |
| `start_year_min` | 3 → 5 |

Deliberately small. The ten regional attach points are still unwritten; this proves the chain
works, it does not pretend prehistory is covered.

It also exercises the deep-time regime for real: the Oldowan at 2.6 Ma sits outside
`DATE_REGIME_LIMIT_YEARS`, and every calendar correctly reports "before calendars" rather than
extrapolating. Monte Verde renders its live-dispute note and shows Islamic as "before epoch".

**Dataset 2.1.0 → 2.2.0, schema 1.0.0 → 1.1.0, 1,305 → 1,310 entities. Artifact 84.2 → 85.6 kB.**

## The prehistory branch, and what building it exposed

Twenty-four entities authored from sourced research (`homo-research.md`): twelve *Homo* species
and twelve stone-tool industries, every value carrying the URL it came from.

### Species and industries are separate branches

`global.prehistory.origins` holds the taxa; `global.paleolithic` holds the industries. The
temptation is to nest industries under their makers, and it is wrong twice over: the Mousterian
outlived some of the people who made it, and several industries cross species. A taxon is not a
period. *H. sapiens* is extant and would otherwise have to be filed inside an era that ended.

### The root stays at 3.3 Ma

Prehistory begins with the earliest knapped stone at Lomekwi 3, which predates the genus by half a
million years. Genus *Homo* is a node *inside* prehistory, anchored at 2.80–2.75 Ma on LD 350-1
from Ledi-Geraru, with the dissenting reading (that the mandible cannot be securely assigned to
*Homo*) recorded as an alternative rather than dropped. The toolmaking record does not break at the
taxonomic boundary, so the tree should not either.

### Building it broke three things in the display layer

None of these were visible before there was deep-time content to render.

**The chrono layer was not connected.** The readout called `tree.formatRange`, which prints the
stored year with a CE/BCE suffix. The origin of the genus rendered as `2798051 BCE` — a
year-precise position in a calendar that did not exist, on a date whose real uncertainty is tens of
thousands of years. `src/chrono/displayRange.ts` is now the join between an `Entity` and the frame
layer.

**The provenance rule was dead code.** `suggestFrame` reads `v.method`, and the dataset adapter
never copied `dating_method` onto the value. So the entire provenance-driven rule — the §"When does
a date switch to BP?" decision — never fired on a single real entity, and only the pre-Holocene age
backstop was doing any work. That backstop is precisely the age-based heuristic this design
rejected, so the app was silently running the rule it was written to avoid. Göbekli Tepe is the
case that exposes it: a radiocarbon date at 11,480 BP, just under the 11,700 backstop, falling
through to a calendar reading it should never have had.

The lesson generalises. A rule that is stated in prose, implemented, and unit-tested against
synthetic values can still be disconnected from every real input. The unit tests passed throughout.

**A range needs one unit, but not always.** Quoting both ends in the older end's unit reads best —
`2.4 Ma – 1.4 Ma` — but applied unconditionally it turns Human Prehistory into `3.3 Ma – 0.0 Ma`, a
two-million-year span rendered as zero. The shared unit is used only where the younger end is at
least 1 in it; otherwise each end takes its own and the explicit labels carry the meaning
(`3.3 Ma – 4,950 BP`).

### `end_year: null` was two claims wearing one face

For *H. sapiens* it means extant. For *H. luzonensis* it means the youngest remains have never been
dated — the species certainly ended, we cannot say when. Both rendered as "present", which put a
hominin known from a handful of foot bones among the living. `end_precision: "unknown"` separates
them.

This is the same shape as the `overlaps-parent` finding in the gap analysis: a nullable field
doing double duty, where one of the two meanings is an assertion nobody intended to make.

## The scope floor is a behaviour (issue #1)

Settled 2026-08-07. The app begins where human-like **behaviour** begins, not
where a taxon does.

Lomekwi 3 knapping at 3.3 Ma predates the oldest *Homo* fossil (Ledi-Geraru,
2.8 Ma) by about 500,000 years, so a taxonomic floor would exclude the oldest
instance of the very behaviour the app exists to track. Taxonomy is also the
least stable line available: *H. habilis* placement is disputed and the
Ledi-Geraru mandible is unnamed.

**Knapping is the line, not tool use.** Tool use extends to chimpanzees and
orangutans and therefore runs past the ~7 Ma common ancestor, which makes any
floor arbitrary and turns this into a primatology timeline. Knapping is a
manufacturing behaviour with a preservable record.

### The gate is not a content filter

The issue offered two options: retitle `origins` behaviourally and keep the
twelve species, or move the species to Deep Time. Neither literal option was
taken, because both rest on a conflation: **what sets the floor is not the same
question as what the app may contain.** The app already holds regions, reigns
and events, none of which are behaviours.

So the gate lives on `global.prehistory`, in its `date_note`, and each branch is
named for what it holds:

| Node | Holds |
|---|---|
| `global.prehistory` | the scope rule itself |
| `global.prehistory.hominins` | 12 species (was "The Genus Homo") |
| `global.paleolithic` and successors | 13 industries |
| `global.prehistory.firsts` | 10 behavioural thresholds |

Species stay because the app is about humans, proto-humans and near-humans —
that *is* the species list. Moving them to Deep Time would not relocate them so
much as delete them: that app budgets ~200 clade FAD/LAD entries for all of
life, so twelve *Homo* species would give our genus more resolution than all of
Mammalia, and its own novice framing argues against that.

### A threshold is not a period

`kind: "threshold"` with `date_precision: "minimum"` is a new node type because
`event` fits badly on three counts. An event is a bounded interval; a first is a
one-sided bound that new evidence can only move older, with the behaviour
continuing after it. The dispute shape differs too: for a period you argue about
which chronology, for a first you argue whether the evidence counts at all —
the Dikika cut marks are contested as trampling damage, not as a date. And it
renders as a marker, not a bar.

Rendering follows: "from 3.3 Ma ago", never "3.3 Ma ago – present", which would
read as an interval that happens to reach today.

### Three senses of before-present

The dataset could already express these through `dating_method`; only display
and conversion needed the distinction.

| Sense | Methods | Suffix | Convertible to CE/BCE? |
|---|---|---|---|
| calibrated | calibrated radiocarbon, layer counting | `cal BP` | yes |
| radiocarbon | UNCALIBRATED radiocarbon | `¹⁴C BP` | **no** |
| geological | Ar/Ar, K-Ar, U-series, OSL/TL, ESR, palaeomag | `ago` | yes |

The middle row breaks a premise the frame model was built on. `resolveFrame`
documented that "BP and calendar reckoning are exactly interconvertible, so this
is a display decision" and that a user preference always wins. Uncalibrated
¹⁴C years are not calendar years — the mapping is an empirical curve, not an
offset — so there is no arithmetic that yields a BCE date from one. This is the
single place the UI refuses rather than converts, and the only place an explicit
preference is overridden. Note the research turned up the same trap in the
literature: several U-series and TL ages are reported as "BP" without being
radiocarbon at all.

Geological ages are a milder case: never referenced to 1950, but at Ma scale
that is a 0.00006% error. Numerically ignorable; the label must still not claim
a datum the measurement lacks.

### A fourth piece of dead code

`NON_CALENDAR_METHODS` listed six of the ten non-calendar methods, omitting
argon-argon, uranium-series, magnetostratigraphy and layer counting. So
`isScientificDating` returned false for an Ar/Ar date. Nothing broke only
because everything dated that way is old enough for the pre-Holocene backstop to
reach the same answer by luck. It is now the complement of `{calendar,
unknown}`, so a method added later defaults to measured — the safe direction,
since BP is always expressible.

That is three of four disclosure/frame heuristics found not to run on real data
(Q-17, the `dating_method` plumbing, and this). The pattern is consistent: a
rule stated in prose, implemented, and unit-tested against synthetic values can
still be disconnected from every real input. Synthetic tests passed throughout
all three.

### Versioning

MAJOR on both. Schema 2.0.0 adds two `kind` values, so any consumer switching
exhaustively on kind breaks — which the TypeScript build demonstrated
immediately by failing on two exhaustive `Record<EntityKind, string>` maps.
Dataset 3.0.0 moves the prehistory ids.

Recorded honestly: **2.2.0 was itself mis-versioned.** It re-parented three
top-level eras and dropped four ids under a minor bump. 3.0.0 absorbs that.

## Regional prehistory (gap analysis §4.2)

All ten regions now have a prehistory branch. 1,345 → 1,417 entities, every date
carrying a fetched source.

**Industries stay on the global Paleolithic spine** and cross-parent into their
region, because an industry is not owned by a modern country. Göbekli Tepe moved
to `west-asia.prehistory` and cross-parents back into `global.neolithic`, which
is what `cross_parent_ids` is for.

### Seven entities store uncalibrated radiocarbon

Jericho, 'Ain Ghazal, Lascaux, Hongshan, the Hoabinhian, Yangtze rice and Cactus
Hill. This is the payoff for the three-senses work: the app refuses to give any
of them a calendar reading.

Jericho is the sharpest case. The familiar "tower built c. 8300 BC" is an
uncalibrated figure, and the source never labels it. Checked against calibrated
estimates for the same stages it runs 500–900 years young, so the tower is
roughly a **millennium older** in calendar terms than the usual number implies.
Its stage table is also internally inconsistent — Stage V is older than Stage III
despite being stratigraphically later.

'Ain Ghazal is the same trap with both numbers in circulation: 6750 ± 80 BC
uncalibrated against 7580 ± 110 BC calibrated for the same statues.

### Two validator rules, and what they caught

**Radiocarbon claimed beyond its range is impossible, not debatable.** Carbon
decays out of usable range by ~50 kyr. The rule caught six entities — *three of
them authored by hand in earlier sessions of this project*.

The cause is structural rather than careless, and it is worth stating plainly:
**`dating_method` is one field per entity, but a long-lived entity has two
boundaries dated by different means.** Neanderthals appear at 400 ka by
uranium-series and luminescence at Sima de los Huesos, and disappear at 40 ka by
AMS radiocarbon. Recording the end's method and letting it describe the whole
entity is the natural mistake. It stays invisible until something renders the
label, which is exactly what happened. Logged as Q-30.

**Uncalibrated radiocarbon must be declared in `date_note`.** The refusal to
convert only protects the reader if the entity says what it is, and the entire
hazard is that published sources frequently do not.

Both rules were verified by reintroducing the bugs into a copy of the data and
confirming they fire, rather than by assuming a passing run means a working
check — four dead-code findings in this project argue for the stronger test.

### Reference anchors reached 0.35% of the dataset

The eight anchor sets are cultural traditions and none begins before the
Holocene, so 42 entities older than 10,000 BCE had nothing to orient against. A
`deep-time` set now runs from the first stone tools to the start of the
Holocene; coverage 0.35% → 97.3%.

These anchors work differently from the others. "Fall of Rome" is a landmark the
reader already holds; nobody grew up knowing when the Last Glacial Maximum was,
so a deep-time anchor has to supply the scale as well as the position.

### Smaller corrections

- `global.mesolithic` is now "Mesolithic (Eurasia)". Its `date_note` already
  said the term has no counterpart in the Americas, sub-Saharan Africa or
  Australia, while the name went on claiming otherwise.
- Aboriginal Australia is open-ended. 1788 is a colonial boundary, not the end
  of a tradition that continues.
- `ReferenceFrame` did not declare `year`; it fell through the index signature
  as `unknown`, so arithmetic on it did not type-check. Fine while nothing read
  the field.
- The visual check caught four entities rendering "– present" that were not
  ongoing, and Border Cave asserting a 2.0 ka end that was a placeholder
  convention of mine rather than a finding.

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

**The part that matters for this app:** the `API` term has a candidate already authored. The
dataset's `tier` field — 386 foundational, 469 intermediate, 562 specialist across 1,417 entities —
was built for progressive disclosure, which is the filtering special case of the same idea. So a
degree-of-interest view needs no new per-entity data:

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

### Design pass, 2026-08-08

`tools/prototype_doi.py` scores the real dataset rather than reasoning about it. It is not shipped;
its job was to find out whether the function above selects a sensible neighbourhood before any of it
is written in TypeScript. It disproved three things, two of them written on this page.

**Measurements that drive everything below.** Entity density spans six orders of magnitude — 0.001
per thousand years in deep time against 680 in the last century. Local median gap between entity
midpoints runs 75,000 years to 1 year, a factor of 75,000. Any radius expressed in absolute years is
wrong by four orders of magnitude at one end, which settles density-normalization as necessary
rather than nice.

**Disproved 1 — `tier` is not global a priori importance.** It is authored per branch: East Asia is
70% specialist, Central Asia and Southeast Asia 0%, West Asia 3%. A "specialist" Japanese nengō and
a "specialist" hominin are not comparable quantities; the field records how deeply its own branch
was covered. Used raw as API it would dim East Asia for authoring reasons rather than importance
reasons. It also correlates hard with depth (0% specialist at depth 0, 59% at depth 5), so using
tier *and* depth double-counts one signal.

It survives as **tier ranked within its sibling set**, which means the same thing in every branch.
Where all siblings share a tier the rank returns neutral — the Heian period's 88 children are
uniformly `specialist`, so the field carries no local information there and must not tilt the
result either way.

**Disproved 2 — Furnas's canonical `API = −depth` is wrong for this tree.** The first prototype run
ranked "East Asia", "Global", "Europe" above every actual neighbour. Shallow nodes win on depth, and
undated container nodes dodged the temporal penalty entirely. The trunk here is eleven region nodes
that are permanently visible in the Miller columns anyway, so the lens adds nothing by surfacing
them. API is the sibling-normalized tier alone, and undated containers are scaffolding rather than
content: they are excluded from the lens.

**Disproved 3 — midpoint distance is the wrong temporal metric.** A nengō sits wholly inside the
Heian period, so the two overlap completely while their midpoints are nearly two centuries apart.
Midpoint distance penalised a node for being contemporaneous with its own parent. The metric is
**interval gap**: zero when the extents overlap, otherwise the space between them.

Overlap alone then proved too generous — "CE (Common Era)" and "Middle Ages" trivially overlap a
seven-year nengō and ranked as its temporal neighbours. An entity three hundred times longer than
the focus is *containing* it, not keeping it company, so a **log span-mismatch penalty** was added.

### Q-7 — the distortion is typographic and one-dimensional, not hyperbolic geometry

A hyperbolic disk earns its keep because circumference grows exponentially with radius while trees
grow exponentially with depth. That trade needs sibling *order* to be free, so children can be
placed radially wherever there is room. **In this dataset sibling order is temporal and is itself
the information.** The Heian period's 88 nengō are a strict sequence; fanning them around a disk
destroys the one relationship a reader needs. Max branching is 88 and median 4 — the hyperbolic
browser's strength is exactly where this dataset can least afford it.

So: position stays monotonic in time, *space allocated per node* varies with DOI, and typography
(size, weight, opacity) reinforces the allocation. That is DateLens, not the hyperbolic browser, and
it is the right precedent. It also avoids teaching a second navigation paradigm alongside the Miller
columns.

### Q-8 — the selection is the focus; one focus, two ways to move it

Two independent foci means two mental models and two things to keep in sync, and selection state is
already persisted in the URL fragment. The focus is the selected node: temporal centre from its
interval, tree distance measured from it. Moving the lens moves the selection, and selecting in the
columns moves the lens.

The "what else was happening then" case does not need a detached lens, which was the argument for
one. The validated run answers it directly: focused on Kōhei (1058–1065), the lens surfaces the Song
and Goryeo dynasties, the Abbasid Caliphate and the Chola Empire — contemporaries five hops away in
the tree that Miller columns can never show. That is the whole payoff, and it falls out of the
temporal term rather than needing separate machinery. Hover may preview a different focus, since
hover is not state.

### Q-9 — the fisheye replaces the tier control with a budget, which is not the same as removing it

A hard tier filter and a soft DOI over the same variable double-count: a specialist node far from
focus is penalised twice, once for being specialist and once for being distant. The Heian case shows
the cost — a tier filter suppresses all 88 nengō uniformly, while DOI still ranks them by time.

The control's *capability* should survive its *mechanism*. Today it is a three-step filter showing
386 / 855 / 1,417 entities. It becomes a **detail budget**: the reader says roughly how much they
want on screen, and DOI decides where to spend it. "Never show me specialist content anywhere" and
"show me more near my focus" are different requests, and the budget serves the first while the lens
serves the second.

### The function, as validated

\[ \mathrm{DOI}(x \mid f) = \lambda\,\mathrm{tier}_{\text{sib}}(x)
   - \big[\, w_T \rho \cdot d_{\text{time}} + w_S (1-\rho) \cdot d_{\text{tree}}
   + w_{\text{span}} \cdot d_{\text{span}} \,\big] \]

`d_time` is `log1p(interval gap / local median gap)`; `d_tree` is hops through the lowest common
ancestor; `d_span` is `|log10(span ratio)|`; `ρ` is a local-density term so structure dominates
where temporal neighbours are 75,000 years away and time dominates where they are one year away.

### Still open

Weights (`λ`, `w_T`, `w_S`, `w_span`) are placeholders that produce good output on four sampled foci;
they need tuning against more, and the tuning should be recorded rather than tacit. The default
budget size is unpicked. And the focus node currently does not always rank first — it is pinned in
the view rather than by the function, which is a display decision worth stating explicitly.

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
- **Replit is configured but dormant.** `.replit` and `replit.md` are on `main` so the project runs
  and a coding agent picks up the same rules, but no work happens there until the build phase
  starts. Until then this checkout is the only writer. Once Replit is live, fetch before editing
  and expect commits from another author.
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
- **ISO astronomical numbering is canonical internally; JSON keeps historical numbering.**
  Converted once at load, never inside arithmetic.
- **Two regimes, split at ±271,821 years** — Temporal's hard limit. Inside, a value is a date;
  outside, a number of years.
- **The native cultural date is authoritative where one exists**; ISO is the derived index. The
  readout leads with the native form. Conversion may be *less* precise than the original, and
  `conversionFuzzDays` records that.
- **One axis, two kinds of view.** CE/BCE, BP and b2k are origin shifts on the ISO axis, not
  calendars. Only the 26 structural calendars need Temporal.
- **Ship `temporal-polyfill/full`** (`Q-26`), for display and input both. ~24 kB gzip, imported
  together with the conversion layer rather than ahead of it.
- **The app is a starting point, not a research tool.** Handoff links are generated from the
  entity; the offline answer is a copyable URL and a downloadable research note, not a
  connectivity probe.
- **Dates are three independently-fuzzy anchors** (`Q-1`, settled); the trapezoid is superseded.
- **`D` blends temporal and tree distance** (`Q-6`, settled), with density normalization so the
  lens behaves consistently across sparse prehistory and dense modern history.
- **Focus+context uses `tier` as the a-priori-importance term**, so no new per-entity authoring is
  required to make the view work.

## Measured answers to open items

Four items were settled by measurement rather than by decision, 2026-08-07.

### Q-29 — resolved by authoring the method instead of tuning the threshold

The fuzz-ratio fallback was producing jarring results among siblings: the Bronze
Age led in BP (±300 yr on 5,250 BP is 5.7%, over the 5% threshold) while the
Iron Age beside it led in BCE. Both were right by the rule and looked like a bug
side by side.

The threshold was not touched. The proxy exists because the method is unknown,
and the fix for an unknown is to find out: `dating_method` is now authored on
the Bronze Age, the Mesolithic, the Neolithic, the agricultural revolution and
Aboriginal Australia. **No entity now selects BP on the fuzz proxy alone.**

The proxy stays for the 1,253 entities that still carry no dating signal, but it
is no longer deciding anything visible.

### Q-16 — the polyfill costs 24 kB gzip, and it buys *input*, not display

Built two probe bundles against the real toolchain:

| Bundle | gzip |
|---|---|
| `Intl.DateTimeFormat` only, no polyfill | **0.3 kB** |
| `temporal-polyfill/full`, 15 calendars exercised | **24.0 kB** |

Projected artifact with the polyfill wired in: **~80 kB gzip**, up from 56.4 kB. Comfortable
against the 3 MB ceiling, but a deliberate re-baseline of `build-baseline.json` rather than
something to let drift past the 5% regression check.

The important part is what the 24 kB is actually for. **Native `Intl` already converts and renders
any date into all 26 calendars at essentially zero cost** — that covers the multi-calendar readout
in requirement 5 outright. What `Intl` cannot do is *parse* a date expressed in a non-Gregorian
calendar, or do arithmetic in one.

So the polyfill is the price of **requirement 6, calendar input** — not of the display feature it
looks like it is paying for.

### Q-26 — settled: ship the polyfill

**Decision: yes, the 24 kB is justified, for both display and input.**

Before settling it, the free alternative was built and tested. `Intl` gives forward conversion
(ISO → calendar); parsing needs the inverse. Because calendars are monotonic in time, the inverse
can be recovered by binary search over ISO days, evaluating each candidate with `Intl`. No
dependency, no bundle cost.

It half-worked, and the half that failed is the half this app is about:

| | |
|---|---|
| Round-trips | **125 of 150** across 15 calendars |
| Mean iterations | 21.2 |
| Fan-out across 15 calendars | 3.1 ms per parse |
| Failures | BCE dates in `gregory`; Hebrew leap-month dates |

Performance was never the problem. Correctness was. The failures cluster in two places:

- **BCE dates.** `Intl`'s era is a *string*, not an ordinal, so a binary search cannot order
  across the BC/AD boundary without special-casing it. Roughly half this dataset is BCE.
- **Hebrew leap months.** Adar I / Adar II break the naive month ordering the search relies on.

Both are fixable with enough special-casing, and that is precisely the argument against: we would
be hand-rolling a calendar library, badly, to avoid depending on one. The failure modes would be
silent and would land on exactly the dates a history app cares most about.

Three further reasons the decision holds:

1. **Requirement 6 asks for input in any calendar.** The free path cannot deliver it correctly.
2. **`Intl` is display-only in another sense too** — no calendar arithmetic, so "add one year in
   the Hebrew calendar" has no answer without the polyfill.
3. **It keeps this app aligned with OmniUnit**, which already ships `temporal-polyfill/full`. Two
   apps in the same family diverging on their date layer would be a maintenance cost with no
   compensating benefit, and the shared source package under discussion assumes a common base.

**Budget consequence:** the artifact goes from 56.4 kB to roughly 80 kB gzip when the conversion
layer lands. The polyfill should be imported *with* that layer, not before it — adding 24 kB ahead
of anything that uses it would be pure cost. `scripts/build-baseline.json` gets re-recorded
deliberately in that commit, with the growth justified in the message, rather than being allowed
to slip past the 5% regression check.

### Q-11 — year-only precision is structurally insufficient, and nengō prove it

Measured the dataset's 248 nengō periods against CLDR:

- **106 of 248 (43%)** are years in which the era changes mid-year.
- **89 of 248 (36%)** resolve to the *wrong* era if you convert the start year at year precision.

Meiji begins in October 1868, Taishō in July 1912, Shōwa in December 1926. Ask "what nengō is
1912?" and there is no correct single answer. This is not an edge case; it is over a third of the
Japanese branch, which is the largest branch in the dataset.

**Answer: yes, at least some entities need month/day precision, and nengō need it structurally.**
Whether that means an optional month/day on the anchor or a continuous day-count representation is
still open — but "year-only is fine" is no longer defensible.

### Q-14 — CLDR and the dataset agree, and the question dissolves

Sampling inside each period rather than at its boundary, **213 of 248 (86%)** agree. Most of the
remaining 35 are romanization variants of the same era — Kashō/Kajō, Jōhō/Shōho, Jōan/Shōan,
Kangi/Kanki, Tenpyō-kanpō/Tenpyō-kampō — plus short one-to-two-year eras where any year-level
probe lands in a neighbour. Only Shuchō versus Hakuhō at 686 is a genuine historical difference.

But given Q-11, "which source is authoritative for nengō?" is the wrong question, because
**neither can answer a year-precision query correctly 43% of the time.**

**Resolution: never derive a nengō from a bare year.** The tree already knows which nengō the user
selected — it is a node, with a `native_name` in kanji. Display that. Use CLDR only to convert a
date the user actually supplied, which by then has a month and a day. Two sources, two jobs, no
conflict, and the ambiguity never arises.

### Q-17 — the broad-range marker was dead code

Measured the uncertainty ratio across the eight prehistory cases and the three v2.1.0 entities
carrying bounds. Observed range **0.002 to 0.092** — and the threshold was 0.10, so **nothing
fired, ever**, including cases chosen specifically for being uncertain.

| Case | ratio | | Case | ratio |
|---|---|---|---|---|
| Ashoka | 0.002 | | Neanderthal end | 0.026 |
| Younger Dryas | 0.008 | | Bronze Age | 0.057 |
| Göbekli Tepe | 0.017 | | Chauvet Phase I | 0.069 |
| Oldowan | 0.019 | | Madjedbebe | 0.092 |

Madjedbebe at 65 ± 6 ka is the clearest case that ought to fire, and the only one above 0.08.
Threshold lowered to **0.08**. Still provisional — eleven samples is not a distribution — but a
marker that never fires is worse than one calibrated loosely.

`UNKNOWN_METHOD_FUZZ_RATIO` (0.05) remains untested; it only matters where `method` is absent, and
every case measured here has one.

### A modelling error the measurement exposed

Chauvet Phase I is 37,000–33,500 cal BP. That is the **duration of an occupation phase**, not the
uncertainty of a single event — and encoding it as `earliest`/`latest` on one anchor conflates the
two, inflating apparent uncertainty and pushing the ratio toward the marker for the wrong reason.

A period's *extent* and a boundary's *uncertainty* are different quantities. The model already has
the right shape for this — a period is two boundaries, each with its own fuzz — but nothing stops
an author collapsing a span into one fuzzy date. New validator rule: a boundary carrying wide
bounds when the entity also has a sibling boundary is suspicious and should be reviewed.

## Open items

The live register. `Q-n` ids are stable — reference them in commits and conversation. Ordered
roughly by how much else they block. Ids are never reused; a settled item moves to §Resolved with
its answer rather than being deleted, so a reference in an old commit still resolves.

**13 open, 21 resolved.** Audited 2026-08-08; Q-33 and Q-34 added when the lens shipped.

**Q-30. Should `dating_method` be per-boundary rather than per-entity?** One field
cannot describe an entity whose start and end rest on different science.
Neanderthals are uranium-series at 400 ka and radiocarbon at 40 ka. The current
convention is that the field describes the START, because frame selection is
computed from the start boundary, and a validator rule now enforces physical
plausibility against it. That is a workaround. The disclosure model is already
per-boundary (`BoundaryDating`), so the dataset is the layer that is behind.
Related: Q-22, which is the same per-boundary problem for notes.

### Blocking — date model

**Q-4. Do periods inherit boundary fuzziness from neighbors?** If the Shang ends fuzzily and the
Zhou begins fuzzily, are those the same fuzzy boundary authored once, or two independent ones that
can contradict each other? Shared boundaries halve the authoring and remove a class of
inconsistency, but they couple entities that may want independent sourcing.

### Blocking — data

**Q-28. Does the registry need splitting into origins and transforms?** `common`, `gregorian`,
`iso8601` and the BP/b2k datums are origin views; the other 23 entries are structural calendars.
They currently sit in one list. Splitting would make the picker clearer and the code simpler, at
the cost of a schema change.

**Q-25. How is sub-year precision represented?** `Q-11` established that it is needed. Two shapes:
an optional month/day on each anchor, or every anchor as a continuous day count with fuzz in days
(exact date = fuzz 0, `~3500 BCE` = fuzz ~91,000 days). The second is uniform and makes all
arithmetic one subtraction; it is also much heavier to author and to read in raw JSON.

**Q-21. Which Wikipedia edition, and what about native script?** English is the default. An entity
with a `native_name` might search better on the matching language edition, but inferring language
from script is unreliable (Han characters span at least three). Options: English only, offer both
with the native search on English Wikipedia, or add an explicit `wiki_lang` field.



**Q-23. What happens when an `asOf` goes stale?** Now concrete: exactly one entity carries one
(`global.paleolithic.monte-verde`, `as_of` 2026-06-30, 39 days old at the time of writing) and its
dispute moved twice in three months. Cheapest honest answer is a validator warning past a
threshold, since a date-stamped dispute that nobody re-checks is worse than an undated one.
Original framing: A date-stamped open dispute is only honest while
someone re-checks it. Options: surface the age in the UI ("last checked 2026-06"), fail a build
check past some horizon, or accept drift. Nothing is decided.

**Q-24. Should `revised` claims show by default or stay behind the popover?** Now sized: of 44
authored alternatives, **8** are `superseded` — small enough that either choice is cheap. Note the
asymmetry the content revealed: `superseded` claims can wait behind a popover, but the 14
`misconception` caveats cannot, because they exist to correct a belief the reader arrives holding
(the *floresiensis* 12,000-year date, figurative art starting in Europe, the Jōmon "13,000 BCE").
A claim nobody believes is optional; a claim everybody believes is not. Original framing: They are settled, so
inline display is arguably noise — but the whole reason to keep them is that readers arrive
holding the old number and need to collide with it.

**Q-22. Who reviews the flagged boundary attachments, and can it stop being a one-off?**
Migration cannot infer which boundary an entity-level note belongs to. Originally 33 entities; now
**37**, because it grows with every content pass — which is the real finding. A scheduled review
never catches up with authoring, so this needs to be a rule at author time rather than a pass.
Same shape as `Q-30`: both are per-entity fields standing in for per-boundary facts.

**Q-31. What is the disclosure surface, and where does it live?** The disclosure model is built and
tested in `src/chrono/year.ts` — `disclosureReasons`, `rollupDisclosure`, `entityCaveats`,
`allClaims` — and `src/main.ts` calls none of them. So **44 rival claims, 27 caveats and 113 source
lists are authored and unreachable**; only `date_note` renders. This is the largest instance in the
project of the pattern that has already produced four dead-code findings, and unlike those it is a
whole surface rather than a plumbing slip.

It blocks `Q-23` and `Q-24`, which cannot be settled without something to settle them on. Open
sub-questions: marker in the tree row or only in the readout; popover or inline expansion; whether
source lists belong with the claim or in one footer. The a11y contract is already specified above.

~~**Q-32.** Standards debt: the §3 checker reports but does not enforce.~~ — **resolved.**
`tools/check_standards.py` now exits non-zero, and `npm run build` and CI both run it. Two regimes,
because the rules were in two states: §3.8/§3.9 naming were at zero so any violation fails outright,
while the 18 size and export violations ratchet against `DEBT_BASELINE` — the count may fall, never
rise. Failing on all 18 immediately would only have got the check disabled.

Verifying it by reintroducing the bug found a real one, for the fifth time. `src/focus/` was never
added to `LAYERS`, so the six lens files were checked against nothing for a whole feature — the same
stale-path-map failure as before, this time hiding my own new code. The true count was 19, not 18:
`intervalGap.ts` exported two functions. Split rather than baselined. An unmapped domain now fails
the check instead of defaulting quietly.


**Q-33. What are the DOI weights, and how would we know they are right?** The lens ships with
`λ=2.5, w_time=1.0, w_tree=1.0, w_span=0.6` — the prototype's placeholders, checked against four
sampled foci and no more. They are not tuned; they are un-falsified, which is a weaker claim. The
harder problem is that there is no ground truth for "the right neighbours", so tuning risks fitting
the weights to whichever foci happen to get sampled. A usable standard is probably adversarial
rather than optimal: assemble foci that should be hard — a nengō buried among 88 siblings, a
hominin whose nearest neighbour is 400,000 years away, a node whose parent is undated, an entity at
a region boundary — and require that no weight set produces an obviously absurd neighbour on any of
them. Until that exists the weights are provisional and should be described that way.

**Q-34. When does the detail-tier select come out?** Q-9 settled that the budget replaces the tier
control's mechanism. Both now ship: the budget drives the lens, the select still filters the
columns. That is the honest interim state, not the destination — two controls over "how much"
invites them to disagree, and they already can, since the select can hide a column row that the
lens still ranks. Removing the select in the same commit that introduced its replacement risked
losing both; it should come out once the lens has been used enough to trust.

## Planned changes

Decided enhancements waiting on time rather than on a decision. Unlike a `Q-n` item there is no
open question here — if one turns up while building, it becomes a `Q-n` and moves to the register.

- **Sync the versioning rule into the project wiki.** `docs/CODING-STANDARDS.md` §12 now carries
  four-part versioning, but the wiki page it derives from
  (`concepts/repository-conventions.md`) still says "Semantic versioning for anything tagged and
  released" — while citing OmniUnit's `v5.0.0.0`, a four-part version, as its example. The wiki has
  contradicted itself on this point for a while; the repo is now the correct copy and the wiki is
  the stale one, which is the reverse of the usual direction. Could not be pushed on 2026-08-08
  because the Project CLI was disabled for that session.

- **"Open Wikipedia" button on the readout.** Links to
  `https://en.wikipedia.org/w/index.php?search={topic}`, where `{topic}` is the entity shown in the
  lower panel. Two things to settle at build time rather than now: the offline guarantee means this
  must be a plain link the user chooses to follow, never a fetch or a prefetch, and the search
  string wants the entity's own name rather than its id — several names carry diacritics and
  non-Latin script, so it needs URL-encoding, not the folded search key.

### Resolved

- ~~`Q-7` Is the distortion geometric or typographic?~~ — **typographic, over a one-dimensional
  ordered time axis.** A hyperbolic disk needs sibling order to be free so children can be placed
  radially; here sibling order is temporal and is the information. The Heian period's 88 nengō are a
  strict sequence, and max branching is 88 against a median of 4 — the hyperbolic browser's strength
  lands exactly where this dataset can least afford it. DateLens is the precedent, not Lamping.
- ~~`Q-8` What sets the focus?~~ — **the selection**, with the lens and the columns as two ways to
  move one focus. Two foci means two mental models to keep in sync. The "what else was happening
  then" case that argued for a detached lens is answered by the temporal term instead: focused on
  Kōhei, the prototype surfaces Song, Goryeo, Abbasid and Chola five hops away.
- ~~`Q-9` Does the fisheye subsume the detail-tier control?~~ — **it replaces the mechanism, not the
  capability.** A hard tier filter and a soft DOI over the same variable double-count. The control
  becomes a detail budget: the reader sets roughly how much to show, DOI decides where to spend it.
- ~~`Q-29` Should the fuzz-ratio fallback decide the frame for archaeological eras?~~ — no, and
  the threshold was left alone. The proxy exists because the method is unknown, and the fix for an
  unknown is to find out: `dating_method` is now authored on the Bronze Age, Mesolithic, Neolithic,
  agricultural revolution and Aboriginal Australia. No entity now selects BP on the proxy alone.
  The proxy still covers the 1,253 entities with no dating signal, but decides nothing visible.
- ~~`Q-15` Is prehistory a separate branch or interleaved?~~ — **both**, and it did not need a
  mode switch. There is a global spine (41 entities: taxa, industries, thresholds) and a regional
  branch in each of nine regions (56 entities), joined by `cross_parent_ids` where an entity
  genuinely belongs in two places. The readout does not switch behaviour at a boundary because
  frame selection is per entity and driven by provenance, so a radiocarbon date in the Neolithic
  and an Ar/Ar date at 3.3 Ma are handled by the same code path.
- ~~`Q-18` Is the frame preference global, per-entity, or both?~~ — **both, with one case that
  overrides any preference.** `resolveFrame(value, preference)` takes `"auto" | "bp" | "calendar"`
  per call, so a global default and a per-entity override are the same mechanism. Building it
  surfaced the constraint that settles the question: an uncalibrated radiocarbon age has no
  calendar equivalent, so `"calendar"` is not a preference there but a request for a number that
  does not exist, and it is refused. What remains is a UI control, which is work rather than an
  open question.
- ~~`Q-10` Builder helpers and schema~~ — done. Shared `tools/builders.py` with a schema-derived
  allowlist, schema 1.1.0, source registry, five validator rules, and a five-entity prehistory
  pilot proving the chain end to end.
- ~~`Q-27` ISO-internal refactor~~ — done. Branded `IsoYear` / `HistoricalYear` types made the
  off-by-one a compile error; introducing them surfaced 137 sites, two of which were real bugs.
- ~~`Q-26` Is calendar input worth 24 kB?~~ — yes. The `Intl`-inversion alternative was built and
  round-tripped 125/150, failing on BCE dates and Hebrew leap months; avoiding the dependency
  would mean hand-rolling a calendar library badly. Also keeps parity with OmniUnit.
- ~~`Q-11` Sub-year precision needed?~~ — yes, structurally. 43% of nengō years contain a mid-year
  era change and 36% misattribute at year precision. Representation is now `Q-25`.
- ~~`Q-14` Nengō from CLDR or the dataset?~~ — both, for different jobs. Never derive a nengō from
  a bare year; display the selected tree node, use CLDR only for user-supplied dates.
- ~~`Q-16` Bundle budget~~ — 24.0 kB gzip for the polyfill, projecting ~80 kB total. The trade is
  now `Q-26`.
- ~~`Q-17` Broad-range threshold~~ — lowered 0.10 to 0.08; at 0.10 the marker never fired on any
  real case. `UNKNOWN_METHOD_FUZZ_RATIO` remains untested.
- ~~`Q-1` Fuzzy date encoding~~ — three independently-fuzzy anchors (earliest, consensus, latest).
  The trapezoid was superseded: it has nowhere to put a bound's own uncertainty.
- ~~`Q-3` What "consensus" means~~ — the value an early undergraduate course would give, not the
  research frontier. Where the field is genuinely split, say so rather than picking a side.
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

Nothing below exists yet. Roughly in dependency order:

- **Ambiguity-preserving date input.** Entering a date in any calendar, with candidate chips.
- **Disclosure UI.** Marker, popover, and the a11y contract in the render section above.
- **Focus+context view.** The second view beside the Miller columns.
- ~~**Schema changes.**~~ Done in schema 1.1.0 and 2.0.0.
- **Schema changes (remaining).** Per-boundary `dating_method` (Q-30),
  and the source registry — none are in `entity.schema.json` yet.
- **Validator rules.** Eleven are specified above; two are now implemented in `tools/validate.py` (radiocarbon plausibility, uncalibrated declaration).
- ~~**Prehistory content.**~~ Done: all ten regional attach points are populated. What remains is the gap
  analysis do not. This is now the largest single body of remaining work.

`Q-10` no longer gates any of it. The next largest item is prehistory content, followed by
requirement 6 (calendar input), which is the last unbuilt requirement.
