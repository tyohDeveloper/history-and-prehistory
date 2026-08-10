# Schema consultation: response

Reviewer's response to `briefs/consult-schema.md`, based on `consult-pack.md` (including
the updated distilled-issues section), `consult-addendum-naming.md` (issue #40), and a
cross-check against `inventory.txt`. Structure: the eight questions answered directly;
changes ordered by value; then the full field-by-field specification an authoring agent can
work from without follow-ups.

**The two-paragraph verdict.** The model is mostly right and the drift is mostly one
disease: the schema offers two parallel ways to say how good a date is — a mushy enum
(`date_precision`) and a precise apparatus (`*_dating_method` + `*_year_min/max`) — and
authors filled the mushy one because it was cheap and whole-entity. `approx` on 1,493
entities is not data; it is the word "approximately" typed 1,493 times. The fix is not a
finer enum. It is to delete the precision enums entirely and make the apparatus that already
exists — method plus numeric bounds — the required spine of every dated endpoint.

The second disease, per the addendum, is that **identity is unreliable in practice**: id
conventions vary within one dynasty, id paths contradict `parent_id` 128 times, display
names collide 15 times, and both authors and search have already been burned by all three.
The cure is not a new identifier field — it is repairing the id system it already has and
enforcing it with validators (Q4). Almost everything else (`alternatives`, `caveats`,
`date_note`, `tier`, the tree mechanism itself) is adequate and should be left alone.

---

## The eight questions

### Q1. `approx` × 1,493 vs bounds × 26

**Recommendation: mandatory numeric bounds, keyed to dating method — and the precision enum
is deleted, not refined.**

The three options the brief offers, in turn:

- **A finer enum: no.** The current enum already contains finer values (`year`, `decade`,
  `century`, `millennium`) and they got 61 uses combined at the whole-entity level and zero
  at the endpoints. Authors default to the vaguest legal value; a 20-value enum would
  collect the same `approx` under a different name. And no enum spans ±50 years on the
  Bronze Age Collapse and ±200,000 years on *Homo sapiens* without becoming a bad encoding
  of a number.
- **An order-of-magnitude field: no.** It is a lossy integer pretending not to be one. If
  the author knows the order of magnitude, they know rough bounds; store the bounds.
- **Mandatory bounds: yes, with the trigger corrected.** Not "bounds whenever precision is
  `approx`" — that keeps the enum alive as the thing that triggers the requirement. Instead:
  **every dated endpoint must carry a `*_dating_method`, and must carry `*_year_min` and
  `*_year_max` unless the method is `calendar` (year attested in contemporary records) or
  `received` (a traditional figure, where bounds are meaningless because the number is the
  tradition's claim, not an estimate).**

This makes the project's governing commitment operational. "Which kind of claim is this
date" is exactly what `start_dating_method`/`end_dating_method` express — the best-designed
vocabulary in the schema, currently populated on only 416/344 entities while the enum
soaked up the effort. Under this rule the method says what kind of claim it is, the bounds
say how wide it is, and the width for display ("c. 1200 BCE", "315 ± 34 ka") is **derived**
from bounds, never authored.

Objection anticipated: "authors won't find published bounds for 1,493 entities." They don't
need published bounds; they need *honest* ones. If the literature says only "c. 2100 BCE,"
author generous round bounds (say −2200/−2000) and note the convention in `date_note`. Wide
honest bounds are information; `approx` is not. Bounds may also be one-sided: `min` only =
terminus post quem, `max` only = terminus ante quem (this replaces the never-used enum value
`minimum`).

Migration is partly mechanical: `century` → ±50, `decade` → ±5, `millennium` → ±500,
`year`/`exact` → no bounds needed; `traditional` → method `received`; `disputed` → an
`alternatives` entry; `unknown` → endpoint absent. The 1,493 `approx` records need authored
bounds — do it by tier (565 foundational first), and accept that specialist-tier reigns
inside a well-dated dynasty can take the dynasty's bound-conventions in bulk (e.g. Egyptian
Old Kingdom reigns: ±25 established once at the dynasty and applied down).

The addendum does not change this answer in substance. Two connections worth noting: the
validator infrastructure that enforces method-and-bounds is the same place the new naming
validators (Q4) live, and the two migrations should share one window; and the date bounds
feed the derived qualified display name that disambiguates the Shōwa-type collisions.

Two data defects to fix in the same pass (this aligns with distilled issue #36):
(1) all BP conversions on the 1950 epoch, uniformly — no more `-3298051`-style tails;
(2) a rounding rule: **a year may not carry more significant digits than its bounds
justify** — the Lomekwian starts at −3300000 (min −3440000, max −3310000), not −3298051.
Also break the fake `1200BC` synchrony: ten entities sharing a placeholder start should each
get their own bounds even if the central estimates remain equal.

### Q2. Whole-entity vs per-endpoint precision

**Retire the whole-entity field. Per-endpoint wins — but per-endpoint *bounds*, not the
per-endpoint enums.**

The hard cases prove start and end are routinely different kinds of claim: Qajar (start
argued among 1789/1794/1796, end 1925 exact), *Homo sapiens* (measured start, no end),
Lomekwian (argon-argon start, hazier end). A single `date_precision` cannot say any of that,
which is why the dataset's 1,743 uses of it say almost nothing. The per-endpoint enum fields
died for the same reason the whole-entity one metastasized: enums are the wrong instrument.
So: **retire all three** — `date_precision`, `start_precision`, `end_precision` — in favour
of the Q1 regime (method required per endpoint; bounds required per endpoint unless
`calendar`/`received`). Note the dating-method fields are already per-endpoint, so the
schema becomes symmetric rather than more complicated.

Endpoint-level *dispute* (as opposed to width) needs no new field: the Qajar record already
shows the right pattern — an `alternatives` entry carrying only the contested endpoint.

### Q3. Two axes of uncertainty collapsed into one

**Add `historicity` for the topic axis; rename `standing` → `date_standing` for the dating
axis.**

The axes demonstrably vary independently in the dataset itself: Dangun (existence
mythological, date traditional), Lomekwian (existence consensus, date genuinely debated),
Erlitou-as-Xia (site real, identification contested). Proposal:

`historicity` — optional, default `accepted` (omit it on the ~95% of entities where nothing
is contested):

| value | meaning | in-dataset example |
|---|---|---|
| `accepted` | default; no serious doubt the topic is real and coherent | Khufu, Waterloo |
| `interpretive` | a scholarly construct or periodization, not a thing contemporaries had | Axial Age, Iron Age |
| `reconstructed` | a real past entity recovered by systematic inference rather than attestation | Proto-Indo-European (once authored) |
| `contested` | genuine scholarly dispute over existence or identification | Xia dynasty / Erlitou-as-Xia |
| `legendary` | transmitted by tradition as historical; unverifiable, possibly a real kernel | early Sumerian King List reigns |
| `mythological` | presented even in the sources as divine or supernatural | Fuxi, Dangun |

The rename of `standing` matters because once a second axis exists, a bare "standing" is
ambiguous forever after. It is one mechanical pass over 411 records. Its vocabulary is fine,
except **drop `superseded` at the entity level** (a superseded dating should be an
`alternatives` entry, never the primary record — which is why it has zero uses) and **keep
`superseded` in `alternatives[].standing`**, where it is exactly right for things like
Britannica's old Erlitou range.

`caveats` of kind `contested-existence` stay: prose companion to the machine-readable grade,
same relationship `date_note` has to the date fields.

### Q4. The searchable key phrase — which the addendum correctly reframes as the handle problem

**The stable, unique, human-legible handle is the `id` — after repair. Do not add a second
identifier. Add `search_phrase` only as a search aid, with no identity role.**

A new `handle` field that must be unique, stable, and human-legible would simply be a second
id, inheriting every maintenance problem the first one has plus a synchronization problem
between the two. Every failure documented in the addendum is curable inside the id system,
and the cures are cheap now and impossible later:

1. **A written slug convention** (fixes addendum §1). Lowercase ASCII; hyphens between
   words; diacritics stripped by a stated transliteration rule (so `Later Lê Dynasty` →
   `later-le` is *derivable*, not guessable); regnal numerals always Roman
   (`thutmose-iii`, never `thutmose3`); generic type words (Dynasty, Empire, Kingdom,
   Culture, Period) dropped from slugs; slug unique among siblings. The convention document
   is part of the spec deliverable, and the authoring validator enforces it.
2. **A one-time id normalization with a permanent redirect map** (fixes `thutmose3`).
   Rewrite nonconforming ids once — all internal references (`parent_id`,
   `cross_parent_ids`, `links[].entity_id`, only 15 of the latter) are mechanically
   rewritable — and keep a build-maintained `redirects` map (old id → new id) forever, so
   nothing external ever breaks. After this pass, **ids are frozen**: refiling an entity
   changes `parent_id`, never the id.
3. **Id prefixes are declared mnemonic, not semantic** (fixes §2). `parent_id` is the only
   truth about location; nothing may parse an id as a path. The 128 prefix/parent
   mismatches get a one-time audit — precisely the audit that would have caught the Rome
   bug, since `europe.mediterranean.rome.empire` filed under `europe.mediterranean` is
   exactly the pattern it flags. Deliberate patterns (Roman emperors keeping flat ids under
   dynasty containers) get written down as named conventions; thereafter the validator
   flags any new mismatch that is not an instance of a documented pattern.
4. **Names may collide; siblings may not** (fixes §3). Validator rule: no two children of
   the same parent share a `name` — which catches `Mesoamerica` ×2 and `Andes` ×2, since
   the same name at two points of the region tree is a filing error, not a fact about the
   world. Non-sibling collisions (two Emperor Taizongs, the ten Japanese era-name pairs)
   *are* facts about the world and are handled in display by a **derived qualified name**:
   `name` + a disambiguator computed from parent and dates — "Emperor Taizong (Tang,
   r. 626–649)", "Shōwa (1312–1317)" vs "Shōwa (1926–1989)". Derived, never authored,
   shown wherever names appear out of tree context (search results, link pickers).
5. **Link authoring goes through a resolver that hard-fails on ambiguity** (survives Shōwa,
   Thutmose III, and both Andes). Authors may write a link target as an id or as any name,
   alias, or name form; the build resolves it to an id and **errors, listing the
   candidates**, whenever the reference is ambiguous or unresolvable. The stored form is
   always the id. No silent wrong target is possible.
6. **Duplicate detection keys on identity, not fuzzy names** (fixes §4). Primary check:
   slug-uniqueness among siblings — both duplicate people authored this session would have
   collided there. Secondary fuzzy check: normalized name with the regnal numeral treated
   as a mandatory distinguishing token (so Thutmose III ≠ Thutmose IV, but a second
   Thutmose III anywhere in Egypt with overlapping dates is flagged).
7. **`search_phrase` stands as proposed**, demoted to exactly one job: the phrase a reader
   would type to research further (`"Erlitou culture Xia dynasty debate"`). Optional;
   fallback = the derived qualified name; uniqueness not required; never a link key.

Two companion fixes from addendum §5 and §6, both cheap: `name_forms` gains kinds
`adjectival` ("Roman" for Rome — half the search bug) and `orthographic`, plus an optional
`system` attribute for romanization systems (pinyin, wade-giles, postal, hepburn), closing
issues #3 and #4; and search must index `name`, `aliases`, `native_name`, and all
`name_forms`, while authoring tools must count **descendants, not children**, when testing
whether a container is empty (the Julius Caesar / King Sejong near-misses).

### Q5. Languages

**Add kind `language`, covering proto-languages, families, and attested languages alike,
with `parent_id` carrying linguistic descent.**

- **Placement:** a top-level `global.languages` branch whose internal structure *is* the
  family tree: `indo-european` → `proto-indo-european`, `proto-germanic` → … → individual
  attested languages. Descent is a genuine hierarchy, which is precisely what `parent_id`
  does; geography is supplied by `regions` (the urheimat / historical range), which finally
  gives that field a real job. Contact phenomena that break the tree — creoles with a
  lexifier and substrates, sprachbunds — use `links`, and mixed ancestry may use
  `cross_parent_ids` exactly as Munmu of Silla does.
- **Family vs proto-language:** author both where the literature distinguishes them
  (Indo-European the family, `historicity: interpretive` if desired; Proto-Indo-European the
  reconstructed ancestor, `historicity: reconstructed`). For minor families one node with
  `historicity: reconstructed` suffices — judgement left to the author.
- **Dating:** start = emergence/divergence window, invariably wide bounds; end = extinction
  (`end_year`) or `extant: true` for living languages (new field, see spec). Add to the
  dating-method vocabulary: `glottochronology` (incl. Bayesian phylolinguistics),
  `first-attestation` (earliest dated text — inherently a terminus ante quem, so typically
  `max`-only bounds), and `genetic` (aDNA-correlated dating, which also serves entities like
  the Steppe Ancestry Influx). Archaeological-correlation dating uses the existing methods.
  PIE's Steppe-vs-Anatolian dating dispute is a textbook `alternatives` case — no new
  machinery.
- **The addendum affects this question directly:** linguistic subgrouping is unstable
  scholarship — families get re-cut. Since language `parent_id` carries descent, language
  ids must be **flat** (`languages.<slug>`, e.g. `languages.proto-germanic`), never
  path-encoded, so a re-subgrouping changes `parent_id` without touching a single id. This
  is the id-prefix lesson of addendum §2 applied prospectively.
- **Links vocabulary:** add `descended_from` / `ancestor_of` for descent assertions that
  cross the tree (loanword-heavy or disputed affiliations), and note that the generic
  `preceded_by`/`succeeded_by` (Q6) covers language *replacement* (Latin → Romance in Gaul
  is descent; Gaulish → Latin in Gaul is succession).

### Q6. Dead fields

- **`capital` (1 use): retire.** The link type `capital_at` already exists and is the right
  shape (capitals move, and are cities — entities, not strings). Nothing is lost.
- **`notable_figures` (1 use): retire — it marks a missing feature.** The feature is a
  `person` kind (see Q8): Confucius, the Buddha, Newton are entities with dates, not strings
  in someone else's record.
- **`links` (15 uses): keep — this is the single worst population gap in the dataset.** The
  before-and-after graph the user names as a core requirement effectively does not exist.
  Two causes: the vocabulary is all state-specific (`successor_state_of`, `vassal_of` — no
  generic way to say "the thing to read next/previous"), and no authoring norm demanded
  links. Fix both: add generic `preceded_by`/`succeeded_by` (with `note` strongly
  recommended), and set the norm that **every foundational-tier entity carries at least one
  link**. Author either direction; the build derives the inverse.
- **`regions` (98 uses): keep, with a scoped rule.** Entities under a regional branch
  inherit geography from the tree and should leave it empty. It is required only for
  cross-regional entities — which is exactly what languages, networks, and world wars are.
  Under that rule 98 is not a scandal; it will grow with the new kinds.
- **`cross_parent_ids` (48 uses): keep unchanged.** Munmu of Silla shows it doing exactly
  its job. Niche is not dead.
- **`superseded` in `standing`:** drop at entity level, keep in `alternatives[].standing`
  (Q3).
- **`potassium-argon`: keep.** Older K-Ar determinations are still quoted in the
  literature; the value costs nothing and will eventually be used. Removing harmless enum
  values is churn.
- Related, from the same table: **kind `city` has 0 uses while Byblos sits as `era` and
  Tenochtitlan as `period`** — the kind is right and the records are wrong. Re-kind those
  two now; the 1,491 enumerated cities confirm the kind is needed, not dead.

### Q7. `threshold` stops at 1650 BCE; `event` is a third battles

**Widen `threshold` to the present. No new kind is needed for technology; two new kinds are
needed for what battles crowded out.**

The existing 26 thresholds share a clean shape: first attainment of a capability, open start
with wide bounds, no end. The alphabet, iron smelting, coinage, paper, printing, gunpowder,
the mechanical clock, the steam engine, vaccination, the telegraph, the transistor, and the
internet have exactly that shape. Nothing about the kind is prehistoric; it just stopped
being authored. Re-kind "The Invention of Coinage" from `event` to `threshold` (it is
currently mis-kinded, per the inventory). Note thresholds inherently date "earliest known
crossing," so `min`-only or asymmetric bounds are normal, and diffusion after the crossing
belongs in `summary`/`links`, not in an `end_year`.

What the post-3000-BCE world *does* lack is a kind for long-lived non-state, non-period
things — religions and law (issue #34) and trade systems. Hence `tradition` and `network`
(defined under Q8). `event` itself is fine as a kind; 14 battles out of 43 is an authoring
imbalance (and Chernobyl's absence a coverage gap), not a schema problem.

### Q8. 39% reigns; societies without kings

**Four new kinds plus one authoring rule.**

- **`people`** — an ethnolinguistic or cultural group as historical actor, with or without a
  state: Scythians, San, Comanche, the Iroquois Confederacy, Polynesian voyagers. Dates =
  emergence/coherence window; `extant: true` where applicable. This is the direct answer to
  pastoralists, confederacies, and stateless societies: they stop being modelled as failed
  king-lists.
- **`network`** — a trade/exchange/communication system: Silk Road, Indian Ocean trade,
  trans-Saharan routes, Hanseatic League, the Manila galleon. Inherently cross-regional, so
  `regions` is required on these.
- **`tradition`** — a named body of belief or practice with a founding horizon and a
  continuing life: religions and denominations, philosophical schools, legal traditions
  (Hammurabi's code, the Corpus Juris as a living tradition). Fills the "no religion
  exists as an entity" hole; the Axial Age node finally gets children.
- **`person`** — a notable individual who is not being recorded as a ruler: founders,
  prophets, scientists, explorers. `reign` stays exactly as-is for rulers; do not migrate
  reigns.

And the rule that attacks the 190+ empty containers: **a container must hold non-reign
content to exist** — at minimum a summary and either period-level phases or links. A
container whose only conceivable children are unauthored king lists is deleted or demoted to
a `date_note` on its parent. The audit's diagnosis is right: the current shape tracks
king-list availability, and no schema change fixes that without an authoring norm.

**Optional but recommended (flagging this as the one bulk change the brief did not ask
for):** split `polity` out of `era`. Today `era` means both "Bronze Age" and "Qajar
Dynasty," which is why Byblos could be filed as one. Definition: `era`/`period` =
periodizations and archaeological cultures; `polity` = a state actor (kingdom, empire,
dynasty-as-state, republic). The migration is one field, largely mechanical (an `era` with
`reign` children or a regional parent is a polity). If deferred, everything else in this
response still stands — but the asymmetry of giving stateless societies a kind (`people`)
while states squat in `era` is ugly, so I recommend doing it.

---

## Changes ordered by value

1. **Replace the precision enums with method + bounds** (Q1/Q2). Delete `date_precision`,
   `start_precision`, `end_precision`. Require `*_dating_method` on every dated endpoint;
   require `*_year_min/max` unless method is `calendar` or `received`. Mechanical migration
   where possible; authored bounds by tier for the `approx` mass. Fix the 1950/1951 epoch
   split and the significant-digits abuse in the same pass.
2. **Repair identity and naming** (Q4, issue #40). Publish the slug convention; run the
   one-time id normalization with a permanent redirect map and freeze ids; audit the 128
   id/parent mismatches and document the deliberate patterns; enforce sibling-name
   uniqueness (fixes Mesoamerica/Andes); derive qualified display names; add
   `adjectival`/`orthographic` + `system` to `name_forms`; slug-based duplicate detection.
   This ranks second because a user-facing bug (no Roman rulers under "Rome") already
   shipped from this cause, and because step 3 depends on reliable link targets.
3. **Build the before-and-after graph** (Q6/Q4). Add `preceded_by`/`succeeded_by` link
   types; the ambiguity-rejecting link resolver; every foundational entity gets ≥1 link.
   This is the user's stated requirement with 15/1,765 coverage — the largest gap between
   promise and practice after dating and identity.
4. **Add `historicity`; rename `standing` → `date_standing`** (Q3).
5. **Add kinds `language`, `tradition`, `people`, `network`, `person`; widen `threshold` to
   the present; re-kind Byblos and Tenochtitlan to `city` and Coinage to `threshold`**
   (Q5/Q7/Q8). Extend dating methods with `glottochronology`, `first-attestation`,
   `genetic`, `regnal-reckoning`, `synchronism`, `astronomical`. Language ids flat.
6. **Add `search_phrase` and `extant`** (Q4, Q5).
7. **Retire `capital` and `notable_figures`; drop entity-level `superseded`** (Q6).
8. **Optional: `polity` split from `era`** (Q8).
9. **Authoring norms:** no container without non-reign content; emptiness checked on
   descendants, not children; single-region entities leave `regions` empty; bounds honest
   rather than sourced-or-nothing.

**Conflicts with the distilled issues: none found.** This response aligns with #36 (epoch
and false precision), #37 (empty containers), #20 (languages), #34/#35 (missing categories,
threshold stall), #40 and #3/#4/#17 (naming, name forms, filing depth). Per #28 and the
brief, nothing here touches sourcing; `source_ids` is untouched.

---

## Field-by-field specification

Conventions binding throughout: years are signed integers, negative = BCE, there is no year
0 (−2333 means 2333 BCE — the dataset's existing convention). Deep-time years converted from
BP use the 1950 epoch and are rounded so a year never carries more significant digits than
its bounds justify. "Required" means the validator rejects the entity without it.

### Identity and placement

| field | type | status | rule |
|---|---|---|---|
| `id` | string, dot-separated slugs | **keep, governed** | Required. Unique, stable, never reused; frozen after the one-time normalization (refiling changes `parent_id`, never the id). The only identifier; all links key on it. Slug rules: lowercase ASCII, hyphenated, diacritics stripped per the stated transliteration rule, Roman regnal numerals, generic type words dropped, slug unique among siblings. **Prefixes are mnemonic only — nothing may parse an id as a path.** New `language` entities use flat ids: `languages.<slug>`. |
| *(dataset-level)* `redirects` | map old-id → new-id | **new build artifact, not an entity field** | Written by the normalization pass and by any future sanctioned rename; resolved by the build forever. |
| `name` | string | **keep, one new rule** | Required. Display name. Need not be globally unique, but **no two siblings may share a name** (validator). Out-of-context display uses the derived qualified name (`name` + parent/date disambiguator), which is computed, never authored. |
| `kind` | enum | **keep, vocab extended** | Required. See kind vocabulary below. |
| `parent_id` | id | **keep** | Required except top-level regions/branches. For `language`, parent = linguistic ancestor (descent tree). |
| `cross_parent_ids` | id[] | **keep** | Additional parents for entities genuinely in two containers (Munmu pattern; creoles). |
| `allow_outside_parent_dates` | bool | **keep** | Set true when dates legitimately exceed the parent's; the validator otherwise flags the 70+ existing contradictions for fixing. |
| `tier` | enum `foundational, intermediate, specialist` | **keep** | Required. Unchanged. |

### Kind vocabulary (final)

| kind | definition for the author | dates |
|---|---|---|
| `region` | geographic container; normally undated | usually none |
| `era` | broad periodization label (Bronze Age, Classical Antiquity). If the `polity` split is adopted, eras are periodizations *only* | start/end |
| `period` | archaeological culture, phase, or site occupation (Oldowan, Erlitou, Naqada II) | start/end |
| `polity` *(optional adoption)* | a state actor: kingdom, empire, dynasty-as-state, republic | start/end |
| `reign` | one ruler's tenure | start/end |
| `person` *(new)* | notable individual not recorded as ruler; dates = lifespan | start/end |
| `people` *(new)* | ethnolinguistic/cultural group as actor, stateless or not | start; end or `extant` |
| `city` | a settlement; use for Byblos, Tenochtitlan, and the 1,491 enumerated | start; end or `extant` |
| `network` *(new)* | trade/exchange/communication system; `regions` required | start/end |
| `tradition` *(new)* | religion, denomination, school, legal tradition | start; end or `extant` |
| `language` *(new)* | language, proto-language, or family; parent = ancestor | start; end or `extant` |
| `taxon` | biological taxon | start; end or `extant` |
| `threshold` | first attainment of a capability, any epoch up to the present; no end year | start only |
| `event` | a datable occurrence with a beginning and end | start/end |

### Dating — the rebuilt spine

| field | type | status | rule |
|---|---|---|---|
| `start_year`, `end_year` | int | **keep** | Best single estimate. `end_year` absent + `extant` absent = end unknown. |
| `start_year_min`, `start_year_max`, `end_year_min`, `end_year_max` | int | **keep — now load-bearing** | Earliest/latest plausible value: ±2σ for laboratory dates, the outer scholarly range otherwise. **Required for any populated endpoint whose dating method is not `calendar` or `received`.** One-sided allowed: `min` only = terminus post quem, `max` only = terminus ante quem. Must bracket the estimate. Honest round bounds are acceptable when the literature gives only "c. X"; say so in `date_note`. |
| `start_dating_method`, `end_dating_method` | enum | **keep, vocab extended** | **Required for any populated endpoint.** Vocabulary: `calendar, dendrochronology, radiocarbon-calibrated, radiocarbon-uncalibrated, argon-argon, potassium-argon, luminescence, uranium-series, esr, layer-counting, cosmogenic, magnetostratigraphy, received, typological, unknown` **plus new: `regnal-reckoning`** (dead reckoning along king lists/annals — most Egyptian dynasty dates), **`synchronism`** (anchored by cross-cultural correlation), **`astronomical`** (eclipse/astronomical retrocalculation), **`glottochronology`**, **`first-attestation`** (earliest dated text/inscription; implies terminus ante quem), **`genetic`** (aDNA/molecular-clock). |
| `date_precision` | — | **RETIRED** | Migration: `century`→±50 bounds, `decade`→±5, `millennium`→±500, `year`/`exact`→method `calendar` (verify), `traditional`→method `received`, `disputed`→author an `alternatives` entry, `unknown`→endpoint absent, `approx`→bounds authored by tier. |
| `start_precision`, `end_precision` | — | **RETIRED** | Same migration; 30 total uses. |
| `date_standing` | enum `consensus, majority, minority, traditional` | **rename of `standing`; `superseded` dropped at this level** | Standing of the primary dating. Absent = read as `majority`. Required on foundational entities and on any entity with `alternatives`. Endpoint-specific dispute is expressed via an `alternatives` entry carrying only the contested endpoint (Qajar pattern), not via per-endpoint standing fields. |
| `date_note` | string | **keep** | Prose on how/why the dates are what they are. Unchanged; it is one of the best-used fields in the dataset (520). |
| `extant` | bool | **new** | `true` = continues to the present (living language, extant taxon, ongoing polity/tradition/city). Removes the ambiguity of an absent `end_year`. Never set alongside `end_year`. |
| `as_of` | date string | **keep** | Unchanged. |
| `calendar_ids` | id[] | **keep** | Unchanged. |

### Uncertainty about the topic

| field | type | status | rule |
|---|---|---|---|
| `historicity` | enum `accepted, interpretive, reconstructed, contested, legendary, mythological` | **new** | Omit for `accepted` (the default). Definitions and exemplars as in Q3. Grades the topic; `date_standing` grades the dating; the two are set independently (Dangun: `mythological` + `date_standing: traditional`). |
| `alternatives` | struct[] | **keep** | Unchanged and exemplary (Qajar, Erlitou). `alternatives[].standing` keeps the full vocab **including `superseded`**. |
| `caveats` | struct[] | **keep** | Kinds `misconception, naming-confusion, contested-existence` unchanged; `contested-existence` remains the prose companion to `historicity`. |

### Discovery and connection

| field | type | status | rule |
|---|---|---|---|
| `search_phrase` | string | **new** | The phrase a reader would search to research further. Optional; fallback = the derived qualified name. Not unique, not an identifier, never a link key. |
| `links` | struct[] `{type, entity_id, note}` | **keep, vocab extended** | Stored `entity_id` is always an `id`. Authors may write the target as an id or any name/alias/name-form; the build resolves it and **fails listing candidates on ambiguity** — never a silent guess. Vocab: existing 18 types **plus `preceded_by`, `succeeded_by`** (generic before/after; `note` strongly recommended — say *why*) **and `descended_from`, `ancestor_of`** (linguistic/biological descent asserted across the tree). Author one direction; the build derives the inverse. Norm: every foundational entity ≥1 link. |
| `regions` | string[] | **keep, scoped** | Required for cross-regional kinds (`network`, world-spanning `event`s, `language` ranges); empty for entities whose branch already encodes geography. |

### Names and prose

| field | status |
|---|---|
| `aliases`, `native_name` | **keep** as-is. Search must index both, along with all `name_forms`. |
| `name_forms` | **keep, vocab extended**: kinds gain **`adjectival`** ("Roman" for Rome, "Ptolemaic" for the Ptolemies — addendum §5) and **`orthographic`** (issue #4); entries gain an optional **`system`** string for romanization systems (`pinyin`, `wade-giles`, `postal`, `hepburn`, `mccune-reischauer`, …), closing issue #3. |
| `summary` | **keep**; required for foundational and intermediate tiers (closes issue #12 by rule). |
| `source_ids` | **keep untouched** — sourcing is a later pass, per the brief. |

### Retired outright

| field | uses | disposition |
|---|---|---|
| `date_precision` | 1,743 | retired; migration above |
| `start_precision` / `end_precision` | 8 / 22 | retired |
| `capital` | 1 | retired; use link `capital_at` to a `city` entity |
| `notable_figures` | 1 | retired; author `person` entities instead |

### Judgements deliberately left to the author

1. **Bound width when the literature gives only "c. X"** — choose honest round bounds at the
   scale of the claim and record the convention in `date_note`.
2. **Family node vs proto-language node** — author both only where the literature
   distinguishes them; one `reconstructed` node otherwise.
3. **Creole/mixed-descent placement** — primary parent = lexifier lineage by default, with
   `cross_parent_ids`/`descended_from` for the rest; deviate with a `date_note` if the
   scholarship does.
4. **`interpretive` vs `accepted` for periodizations** — tag only where the construct itself
   is the controversy (Axial Age yes; Bronze Age in its home region, optional).
5. **Which entities merit `search_phrase`** — author it where `name` alone is a poor query;
   skip it elsewhere.
6. **Dynasty-level bound conventions for specialist reigns** — permitted and encouraged; state
   the convention once in the dynasty's `date_note`.
7. **Transliteration edge cases in slugs** (which romanization wins for a given language) —
   decided once per language in the slug-convention document, not per entity; the author
   extends that document rather than improvising.
8. **Filing-depth conventions per branch** (issue #17, addendum §6) — the author states the
   depth rule for a branch (e.g. "reigns sit under their dynasty, never directly under the
   polity") in the branch's container `date_note` or the convention doc, then follows it.
