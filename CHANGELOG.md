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
