# Changelog

App releases. The dataset is versioned independently — see
[`docs/DATASET-CHANGELOG.md`](docs/DATASET-CHANGELOG.md). The header shows both.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions are four-part,
`MAJOR.MAJORFIX.MINORFIX.SPELLING`, and are **not** semver — see
[`docs/CODING-STANDARDS.md`](docs/CODING-STANDARDS.md) §12. App and data are tracked separately and
their numbers are unrelated: the app leads with `3` because it works as intended, the data with `0`
because it is materially incomplete.

## [Unreleased]

Open work is tracked as `Q-n` items in [`docs/DESIGN.md`](docs/DESIGN.md) — 14 open at the time of
this release.

## [3.12.0.0-app] — 2026-08-08

### Changed

- `tools/coverage.py` now also excludes NAVIGATION eras from the childless
  report. `east-asia.prehistory` spans 14,000–300 BCE holding nothing, and the
  report called it the single biggest gap in the dataset — while Jomon sat
  fully subdivided under Japan and the Chinese Neolithic under China, exactly
  where that node's own summary says they belong. It is a cross-link, not a
  container. Acting on the report as written would have duplicated 1,500 years
  of existing coverage.
- Ships dataset 0.14.0.0. Build size baseline rebased to 193,218 bytes gzip.

## [3.11.1.0-app] — 2026-08-08

### Removed

- The Wikipedia search URL is no longer printed under the handoff button. It
  was there for a real reason — opened from a `file://` path the link is dead,
  and the user's fallback is to copy the search down — but a percent-encoded
  URL on every single entity is noise, and the button label already says where
  it goes. The offline fallback stays in `researchNote`, which writes the same
  URL into a downloadable text file. That is the right home for it: an offline
  user can keep a file, and cannot keep a line of screen text.
- The e2e test now asserts the URL is ABSENT, so this cannot quietly come back.

## [3.11.0.0-app] — 2026-08-08

### Changed

- `tools/coverage.py` now prints the childless-node report by DEFAULT rather
  than behind `--childless`. The region-by-band matrix cannot see a structural
  gap: a two-thousand-year era with no children counts as one entity in one
  band, exactly like a node that is properly subdivided. The Indus Civilisation
  sat undifferentiated for ten releases while the South Asia row looked merely
  thin. The report existed the whole time; nobody passed the flag. A report that
  must be asked for is a report that gets missed.
- The same report now excludes synthesis eras — a node with caveats and no
  children is a concept, not an empty container, and listing "The Anatolian
  Farmer Turnover" as a gap sends the next pass after work that should not be
  done.
- Ships dataset 0.13.0.0. Build size baseline rebased to 184,848 bytes gzip.

### Added

- Two tests that pin the structural fix: the widest previously-childless eras
  must keep their children, and the 1964 Harappan chronology must ship as
  `superseded` rather than as a live rival.

## [3.10.0.0-app] — 2026-08-08

### Added

- **How a date was arrived at is now shown.** 248 entities carried
  `start_dating_method` and nothing rendered it — the same gap as caveats and
  citations before them, and arguably the worst of the three, since the method
  is what separates "we measured this" from "this was handed down". A `Dated by`
  row now appears in the readout, splitting into `Dated by (start)` and
  `Dated by (end)` where the two boundaries rest on different science, which is
  the whole reason Q-30 split the field in schema 3.0.0.
- `received` as a dating method (schema 3.1.0) — see the dataset changelog.

### Fixed

- `main.ts` had grown its own copy of `DATING_METHOD_LABEL` before the existing
  one in `chrono/year.ts` was noticed. Removed; the canonical map is imported.
  This is the divergence `builders.py` was written to stop, reappearing.
- `received` is registered in `CALENDAR_METHODS`, so `isScientificDating()` does
  not claim Rome's 753 BCE was measured by an instrument.

### Changed

- Ships dataset 0.12.0.0 and schema 3.1.0.
- Build size baseline rebased to 177,797 bytes gzip.

## [3.9.0.0-app] — 2026-08-08

### Added

- **Received conventions are now visible as such.** `standing: "traditional"`
  has been in the schema since 3.0.0, described there as covering dates that
  "are not findings, and presenting them with the same weight as measured or
  attested dates is the commonest way a history reference misleads". Nothing
  used it. Rome's 753 BCE carried `date_precision: "traditional"` and no
  standing, and rendered in the picker identically to a Bayesian radiocarbon
  range.
  - A dagger on the range in the column gutter, which is where most reading
    happens.
  - A banner at the top of the readout, above the summary: "Received
    convention, not a finding. Shown because it is widely cited; the evidence
    does not establish it."
  - Nine entities now carry it — Rome's Kingdom, Gojoseon, Gilgamesh, David,
    Solomon, Narmer, Nitocris, and the two new Central Asian entries.

### Fixed

- **A received convention is no longer quoted in BP.** BP is the idiom of
  radiometric measurement; rendering a pottery-typology bracket as "6,749 BP"
  lends it authority it does not have and invents a digit — 4800 BCE has two
  significant figures, 6,749 BP appears to have four. On `auto` these now stay
  in calendar reckoning. An explicit user preference still wins.

### Changed

- Ships dataset 0.11.0.0: the Namazga sequence, Kelteminar and Altyn-Depe.
- Build size baseline rebased to 176,130 bytes gzip.

See [`docs/DATASET-CHANGELOG.md`](docs/DATASET-CHANGELOG.md) for 0.11.0.0.

## [3.8.0.0-app] — 2026-08-08

### Added

- **The validator now looks for cal BP figures stored as calendar years** — the
  class of error that put Monte Verde 1,950 years out in 0.9.0.0. It fires when
  an entity's own prose quotes a BP figure that its year field is the exact
  negation of. Carries an explicit note that it would NOT have caught Monte
  Verde, whose note never quoted the number; it covers a real subset of the
  problem, not the whole class.
- A dataset-wide test that no entity asserts the same rival claim twice. Added
  after enriching Ban Chiang re-introduced a superseded 3600 BCE chronology it
  already carried, so the panel showed the same claim twice at the same date.

### Changed

- Ships dataset 0.10.0.0: Central Asia, the Austronesian expansion and Oceania.
- Build size baseline rebased to 176,186 bytes gzip. Content: 24 entities and 46
  sources.

See [`docs/DATASET-CHANGELOG.md`](docs/DATASET-CHANGELOG.md) for 0.10.0.0.

## [3.7.0.0-app] — 2026-08-08

### Fixed

- **The column gutter converted uncalibrated radiocarbon ages to BCE, which the
  readout explicitly refuses to do.** The same entity read "8851-4651 BCE" in the
  column and "10.8 - 6.6 ka ¹⁴C BP" three inches away in the panel, which is the
  exact false precision `renderCalendarRows` was written to prevent. `shortRange`
  now defers to the readout's formatter for these. Affects 14 entities; found
  while reviewing new Ecuadorian data, but pre-existing.

### Changed

- Ships dataset 0.9.0.0: the European Mesolithic and the arrival of farming, the
  Holocene Americas, and a units fix to Monte Verde.
- Build size baseline rebased to 163,818 bytes gzip. Content: 39 net new
  entities and 58 new sources.

See [`docs/DATASET-CHANGELOG.md`](docs/DATASET-CHANGELOG.md) for 0.9.0.0.

## [3.6.0.0-app] — 2026-08-08

### Added

- **Source citations are rendered.** 175 entities carried `source_ids` pointing
  at 203 source records, and the app showed none of them — it told every reader,
  on every entity, that its dates were "a starting point, not a citation". That
  was true only because nothing rendered the citations that existed.
  - A numbered `Sources` block per entity: citation as the link text (§10
    requires descriptive text, never a bare URL), the source kind, the URL as
    selectable text for offline use, and the source's own note where it has one
    — usually the part explaining that a source is a minority position or
    revises an earlier date.
  - Superscript markers tie each caveat and each competing date to the specific
    source backing it, so "Botai is superseded" is checkable rather than
    asserted.
  - Numbering is **per entity**, not global. A global scheme would print "[147]"
    on a panel showing three sources and imply 146 more were hidden.
  - Non-peer-reviewed kinds (`reference`, `news`) are marked in accent;
    peer-reviewed is the default and is left unemphasised.
  - The research handoff no longer claims a date is uncited when it is. It now
    says the opposite for the 175 entities that are sourced, and keeps the
    warning for the 1,305 that are not.

### Changed

- `src/data/sources.json` now enters the bundle. Build size baseline rebased to
  148,460 bytes gzip, +17.3 kB. That is the cost of the data, not a code
  regression, and it was a deliberate call — the full file rather than a
  trimmed id/citation/url lookup, because `kind` and `note` are worth the extra
  3 kB.

## [3.5.0.0-app] — 2026-08-08

### Added

- **The epistemic layer is now rendered.** 62 entities carried `caveats`, 56
  carried `alternatives`, 180 carried `standing` and 175 carried `source_ids`,
  and no code path read any of them. `caveatsOf` and `entityCaveats` existed in
  `chrono/` and were unit-tested, but `main.ts` never called them, so the whole
  point of the dataset — that it says where the received story is wrong — was
  invisible. Same failure as the research handoff in 3.2.0.0: model and tests
  present, no wiring.
  - "Worth knowing" block, above the calendar readout, because a misconception
    about what a date *means* outranks the same date in four calendars.
  - "Competing dates" block for rival claims, kept apart rather than averaged
    into a range that would imply the middle is likeliest.
  - `Standing` and `Dispute last checked` rows in the fact list.
  - A `superseded` rival renders struck through, so Botai does not read as a
    live competitor to the Volga-Don horse date.
  - Costs 0.6 kB gzip. Source citations are **not** yet rendered: the trimmed
    lookup for the 202 referenced sources is 14.6 kB gzip, which would exceed
    the build ceiling, and that is a size-budget decision rather than an
    oversight.

### Changed

- Ships dataset 0.8.0.0: the Neolithic transition reframed, its eight centres
  of origin, and eleven behavioural firsts.
- Build size baseline rebased to 130,161 bytes gzip, and now measured with
  `zlib.gzipSync` to match `scripts/verify-build.mjs`. The previous baseline was
  recorded with a different compressor, so it was not comparable to the value
  the check computes.

See [`docs/DATASET-CHANGELOG.md`](docs/DATASET-CHANGELOG.md) for 0.8.0.0.

## [3.4.0.0-app] — 2026-08-08

### Changed

- Ships dataset 0.7.0.0: regional Chalcolithic entries, the Levantine
  Epipalaeolithic, and East Asian / Oceanian prehistory navigation. No app code
  changed; the version moves because the shipped artifact does.
- Build size baseline rebased to 125,780 bytes gzip. Content, not code.

See [`docs/DATASET-CHANGELOG.md`](docs/DATASET-CHANGELOG.md) for 0.7.0.0.

## [3.3.0.0-app] — 2026-08-08

### Changed

- **Dating is per-boundary (Q-30, schema 3.0.0).** `datingOf` no longer applies
  the start's method to the end. It was labelling a radiocarbon end as
  argon-argon whenever the start was volcanic, invisibly, because the end had no
  method of its own to carry. Four entities in the corpus genuinely differ at
  each end.
- `cosmogenic` added to `DatingMethod`, its BP sense and its display label.
  Sterkfontein and Swartkrans rest on it and could not previously be recorded.
- Build size baseline rebased to 122,646 bytes gzip, up 6.8 kB. That is content
  — 31 entities with notes, alternatives and caveats, plus 46 source records —
  not a code regression.

### Fixed

- The E2E version assertion pinned the previous release; updated with the data
  track's move to 0.6.0.0 and the corpus to 1,448 entities.

See [`docs/DATASET-CHANGELOG.md`](docs/DATASET-CHANGELOG.md) for the 0.6.0.0
data release this ships alongside.

## [3.2.0.0-app] — 2026-08-08

### Added

- **The research handoff is now rendered.** The readout panel shows a "Search Wikipedia for …"
  link for the selected entity, opening in a new tab with `rel="noopener noreferrer"`, descriptive
  text and no tracking parameters (ARCHITECTURE §10). Queries are disambiguated where the dataset
  actually repeats a name, so Emperor Taizong searches as `Emperor Taizong Tang Dynasty`.
- The handoff URL is also rendered as selectable text beneath the link. Opened offline the link
  goes nowhere, and `src/research/handoff.ts` states that the fallback is to read the URL and run
  the search later — which only works if the URL is actually on screen.
- `panel-handoff-root` added to the required test-ID manifest; `link-handoff-{targetId}` and
  `text-handoff-url-{targetId}` added as dynamic ids. Three E2E cases cover the link contract,
  disambiguation, and the absence of any network request.

### Fixed

- `src/research/handoff.ts` and its 11 unit tests had been in the tree since the research-handoff
  work landed, but `src/main.ts` never imported them, so no handoff was reachable in the running
  app. `CHANGELOG` and `docs/DESIGN.md` already described the feature as shipped. The unit tests
  passed throughout because they exercise the URL builder in isolation — the part that worked.
- The E2E version-stamp assertion had the two tracks the wrong way round since the renumbering,
  checking for app `v0.5.0` and `data 3.1.0` when those are the data and app versions respectively.
  It was the one red test in the E2E suite; now pinned to `v3.2.0.0` and `data 0.5.0.1`.

## [3.1.2.0-app] — 2026-08-08

### Fixed

- Removed `src/lib/{types,tree,dataset}.ts`. They had no importers and duplicated the `entity`,
  `dataset` and `chrono` domains; §3.8 violations went from 2 back to 0, total §3 from 20 to 18.
- Removed `pnpm-lock.yaml`. CI runs `npm ci` and `release.mjs` syncs `package-lock.json`, so a
  second lockfile only lets the workspace and CI disagree.
- Dropped the unused `@replit/connectors-sdk` runtime dependency.
- `tests/dataset-integrity.test.ts` pinned `5.0.0.1` against data reading `0.5.0.1` and had been
  failing since the renumbering. 177 passing again.

## [3.1.1.0-app] — 2026-08-08

First tagged release. It was cut as `v0.5.0` under three-part semver, then renumbered when
four-part versioning was adopted: the app became **3.1.1.0** and the dataset it ships moved from
`3.1.0` to the data track's **0.5.0.1**, tagged `v3.1.1.0-app` and `v0.5.0.1-data`. The original
`v0.5.0` tag no longer exists on the remote, so this file points at the tags that do.

Nothing between `0.1.0` and `0.5.0` was ever released: `package.json` sat at `0.1.0` from the first
commit while the work below landed, so this changelog starts here rather than inventing a release
history to fill the gap.

Ships as one self-contained HTML file that runs offline from `file://`, stores nothing, and makes
no network requests.

### Added

- **Miller-column picker** over 1,417 entities, with a detail-tier filter and diacritic-folded
  search.
- **Multi-calendar readout** — 21 dating systems, including the full Japanese nengō sequence.
  Built on `temporal-polyfill`, with a Julian-day conversion layer.
- **Prehistory back to 3.3 Ma**, scoped by a behavioural gate — the earliest lithic tool shaping
  (Lomekwi 3) rather than membership in genus *Homo*. Adds 12 hominin taxa, 12 stone-tool
  industries, and 10 behavioural thresholds.
- **Regional prehistory** for all ten regions.
- **Focus+context lens** — a degree-of-interest ranking beside the columns that surfaces
  contemporaries the column view cannot reach. Focused on a Heian nengō it finds Song China and
  Goryeo Korea. Distance is density-normalized, which is what lets one formula work across a
  dataset whose entity density spans six orders of magnitude. A detail budget replaces the tier
  filter as the amount control.
- **Disclosure model** — per-boundary dating, named uncertainty reasons, entity caveats, rival
  claims, and a 114-work source registry. Authored and validated; see Known limitations.
- **Research handoff links**, generated rather than curated.
- **44 reference anchor dates** extending into deep time.
- **Build gates** — single-file and offline-safe verification, XML well-formedness, a coverage-
  enforced test-ID manifest, and a gzip size baseline that fails the build on >5% growth.
- **CI** running the same build, Playwright, and the Python dataset validator on every push.

### Changed

- **Internals moved to ISO astronomical years** (Q-27). The dataset keeps historical numbering and
  the crossing happens exactly once, in `fromEntity.ts`. The hazard was that every wrong answer
  looks plausible — −753 and −752 are both believable for the founding of Rome, so an off-by-one
  survives review indefinitely. A convention would not have held; a type boundary does.
- **The native cultural date is authoritative**; ISO is the index, not the source of truth.
- **Dates render in the frame their provenance calls for**, driven by dating method rather than by
  age. Three senses of BP are distinguished — `cal BP`, `¹⁴C BP`, and informal `ago`.
- **Uncalibrated radiocarbon is refused rather than converted.** Seven entities carry it; turning
  a `¹⁴C BP` figure into a calendar year without a calibration curve would fabricate precision.
- **Schema 1.0.0 → 2.0.0**, adding the `taxon` and `threshold` kinds and `date_precision: minimum`.
- **Directories under `src/` name domains, not layers.** `src/lib` was eliminated and `types.ts`
  split by domain, clearing §3.8 and §3.9 of the coding standards.

### Fixed

- `eraYear` read off a Gregorian conversion returned 2900.
- Uncertainty denominator and duplicate uncertainty markers.
- `dating_method` never reached `suggestFrame`, so a field authored on five entities decided
  nothing.
- `NON_CALENDAR_METHODS` was missing 4 of 10 methods.
- `check_standards.py` silently stopped covering renamed directories — violations fell from 20 to 8
  with no code improved, which is the standards checker falling to the rule it exists to enforce.
- 32 literal `\uXXXX` sequences in `docs/DESIGN.md`, written by an edit that put JSON-escaped text
  into markdown.
- Replit's generated directories (`.config/`, `.upm/`, `.pythonlibs/` and friends) were not
  gitignored, so a Replit workspace went dirty on startup and its git integration refused to pull
  — reported as a merge failure rather than as untracked files.

### Known limitations

- **Calendar input is not built.** The multi-script input grammar is the last unbuilt requirement.
- **The disclosure surface is authored but unreachable** (Q-31) — 44 rival claims across 42
  entities, 27 caveats, 3 misconceptions and 113 per-entity source lists exist in the data and are
  never read by `src/main.ts`. Of the disclosure fields only `date_note` reaches the screen, on 151
  entities. The 114-work source registry ships as IDs, not citations.
- **Two controls over "how much"** (Q-34): the detail-tier select and the lens budget both ship and
  can disagree.
- **The lens weights are provisional** (Q-33) — checked against four sampled foci, not tuned.
- **`dating_method` is per-entity but dating is per-boundary** (Q-30). Neanderthals are
  uranium-series at 400 ka and radiocarbon at 40 ka; one field cannot say that.

These are why this release is `0.5.0` and not `1.0.0`.

[Unreleased]: https://github.com/tyohDeveloper/history-and-prehistory/compare/v3.1.2.0-app...HEAD
[3.1.2.0-app]: https://github.com/tyohDeveloper/history-and-prehistory/releases/tag/v3.1.2.0-app
[3.1.1.0-app]: https://github.com/tyohDeveloper/history-and-prehistory/releases/tag/v3.1.1.0-app
