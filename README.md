# History & Prehistory

A structured picker for historical and prehistoric periods, eras, dynasties, rulers, and events.
Ships as **one HTML file** that runs offline from `file://`, stores nothing, and makes no network requests.

Planned home: **`history.tyoh.app`** — the History member of the [tyoh.app tools family](#the-tyohapp-family).

> **Status:** app **v0.5.0** ([changelog](CHANGELOG.md)), dataset **v3.1.0**
> (1,417 entities, 114 sources, schema 2.0.0).
> App and dataset are versioned independently and the header shows both.
> The Miller-column picker, the prehistory extension back to 3.3 Ma, the multi-calendar readout,
> and the focus+context lens are in place. Calendar *input* — the multi-script grammar — is the
> last unbuilt requirement, and the disclosure surface is authored but not yet rendered (Q-31),
> which is why this is not 1.0.
> [`docs/DESIGN.md`](docs/DESIGN.md) is the living design doc and carries the open-item register;
> [`docs/gap-analysis-v2.1.0.md`](docs/gap-analysis-v2.1.0.md) is the original roadmap and is now
> largely historical.

## Quickstart

```bash
npm ci
npm run dev            # dev server on :5000
npm run build          # typecheck -> unit tests -> bundle -> minify -> verify
npm run test:e2e       # Playwright against the built artifact over file://
npm run validate:data  # JSON Schema + referential integrity (needs python3 + jsonschema)
```

`npm run build` writes a single self-contained `dist/public/index.html`. Open it directly in a
browser — no server needed.

### Running on Replit

The repo carries a working [`.replit`](.replit); importing it needs no configuration.

- **Modules** `nodejs-20` and `python-3.12`. Python is only needed for `npm run validate:data` and
  the `tools/` generators — the app builds and runs without it.
- **Run** is `npm run dev`. Vite binds `0.0.0.0:5000` to match the port mapping (`5000` → `80`) —
  a default `localhost` bind is not reachable from the Replit webview. The bind is set in
  `vite.config.ts` as well as in the `dev`/`preview` script flags, so running `npx vite` directly
  works too.
- **Deployment** is `static`, publishing `dist/public` after `npm run build`. There is no server
  to run in production — the build output is one file.

If Replit reports a merge or pull problem, check the branch first: the workspace must be on
`main`. `calendar-layer` is a stale branch, fully merged and 28 commits behind — a workspace
sitting on it cannot fast-forward. Replit's generated directories (`.config/`, `.upm/`,
`.pythonlibs/`) are gitignored so they cannot leave the tree dirty, which Replit reports as a
merge failure rather than as untracked files.

Two things that are not automatic:

- `npm run test:e2e` needs browsers first: `npx playwright install chromium`. The unit tests and
  the build need no such step.
- `npm run validate:data` needs `jsonschema` in the Python environment.

Verified from a clean clone on 2026-08-08: `npm install`, `npm run dev`, and `npm run build` all
succeed on Node 20 with no configuration changes.

## What it does

- **Miller-column tree** — Region → Era → Period → Reign/Event, wide rather than deep, with real
  date ranges on every node.
- **Progressive detail** — every node carries a tier (`foundational` / `intermediate` /
  `specialist`) so the default view stays legible and specialists can reveal the rest.
- **Diacritic- and separator-insensitive search** — `jomon` finds Jōmon; `Ala-ud-din` finds
  Alauddin. Selecting a hit rebuilds its full path in the columns.
- **Cross-parent placement** — entities that belong in more than one regional narrative (Yuan,
  Alexander) appear under each, without duplicating the record.

## Dataset

| | |
|---|---|
| Version | 3.1.0 (schema 2.0.0) |
| Entities | 1,417 — 643 reigns, 422 periods, 259 eras, 43 regions, 28 events, 12 taxa, 10 thresholds |
| Tiers | 386 foundational · 469 intermediate · 562 specialist |
| Calendars | 21 dating systems, including the full Japanese nengō sequence |
| Themes | 16 cross-cutting collections |
| Reference frames | 44 novice-friendly anchor dates |
| Sources | 114 cited works |

Authoritative sources are `schemas/` (JSON Schema) and `tools/` (Python generators + validator).
`src/data/*.json` is generated output, committed so the build is reproducible without Python.

Every entity carries `start_year` / `end_year` in **proleptic Gregorian** — negative is BCE, and
there is no year zero. That single axis is what makes cross-regional "what else was happening?"
queries cheap.

`docs/gap-analysis-v2.1.0.md` is a full audit of this dataset: regional sparsity, chronological
holes, incomplete ruler lineages, prehistory attach points, and schema debt. Read it before
authoring new content — several of its findings are load-bearing for how the next region should
be written.

### Aiming a coverage pass

Run `npm run coverage` before deciding what to author. It prints a region × era-band matrix, and
it exists because intuition about where the dataset was thin turned out to be wrong: the millennia
approaching 1000 BCE look sparse but are the densest pre-CE band, while 10,000–3,000 BCE is the
genuinely starved one.

Two rules the report enforces by construction:

- **Partition a pass by START year, never by span.** Entities have one start but a date *range*.
  Slicing on "ends before X" silently drops every long-lived entity crossing the line, and
  duration correlates with significance — so that cut is biased against the entities most worth
  having. `--spanning` lists the straddlers a naive cut would lose.
- **Never truncate an end to fit the slice.** If a culture starts inside your window and runs past
  it, author its real end. The slice governs what you pick up, not what you record.

Reigns are counted separately throughout, because forty kings of one dynasty are forty entities
and almost no additional coverage of a period. `--childless` lists eras that promise sub-structure
they do not have.

## Privacy and offline posture

This is a product property, not an implementation accident. The app is designed so that a user
with the network off sees identical behavior to a user online.

- No `fetch`, `XMLHttpRequest`, `sendBeacon`, WebSocket, EventSource, WebRTC, or Service Worker
- No `localStorage`, `sessionStorage`, `IndexedDB`, or cookies — reloading starts fresh
- No telemetry, analytics, tracking, or fingerprinting
- No CDN fonts, CDN JS, or any third-party origin referenced by the running page
- A strict CSP `<meta>` (`connect-src 'none'`) enforces it in the browser

**These are machine-checked, not just documented.** `scripts/verify-build.mjs` greps the built
artifact for every forbidden API and fails the build if one appears. It also asserts the CSP is
present, the output is a single file with no siblings, and no external URL is referenced by any
resource-loading attribute. Adding a `fetch()` breaks CI, not production.

The only network activity the app can cause is a user clicking an outbound link, which opens in a
fresh tab (`rel="noopener noreferrer"`).

## Layout

```
src/
  main.ts               VIEW — the only view file: rendering and event wiring
  style.css
  calendars/            Calendar registry, conversion, and selection
  chrono/               Year parsing, BP senses, display ranges
  temporal/             Temporal API shim and Julian-day conversion
  entity/               Entity types; tree index, path, search, formatting
  dataset/              Build-time inlined data (no runtime fetch)
  focus/                Degree-of-interest scoring for the focus+context lens
  research/             Research handoff records
  data/*.json           Generated dataset, inlined at build time
schemas/*.json          JSON Schema — the authoritative data contract
tools/                  Python dataset generators and validator
tests/
  *.test.ts             Unit tests for the pure library layer (Vitest)
  e2e/*.e2e.ts          Playwright against the built artifact over file://
scripts/
  minify-artifact.mjs   HTML-shell minification, XHTML-safe
  verify-build.mjs      The build gate described above
  testid-manifest.json  Stable production test IDs, coverage-enforced
  build-baseline.json   Recorded gzip size; >5% growth fails the build
docs/                   Gap analysis, dataset changelog, model-council reviews
```

## Stack

TypeScript (strict) · Vite · `vite-plugin-singlefile` · Vitest · Playwright ·
`html-minifier-terser` · GitHub Actions.

Directories under `src/` name domains, not layers — there is no `lib/`, `utils/`, or `helpers/`.
`docs/CODING-STANDARDS.md` §3.8 makes this binding and `tools/check_standards.py` measures it.

No UI framework. The picker is a tree renderer over a static dataset — a framework would cost
bundle budget that the 1,417-entity dataset needs, and would not remove any real complexity.
Reconsider only if the UI grows genuine client-side routing or heavy shared state.

## Contributing

CI runs the identical `npm run build` plus Playwright plus the Python dataset validator on every
push and PR. Local, CI, and Replit outputs are expected to match.

Test IDs follow `{role}-{area}-{name}[-{key}]`. Adding or removing one in `src/` means updating
`scripts/testid-manifest.json` in the same PR — the build check enforces it.

Bundle size is baselined. If a change grows gzip by more than 5%, the build fails; re-record
`scripts/build-baseline.json` deliberately, in the commit that justifies the growth.

## The tyoh.app family

| Subdomain | App | Status |
|---|---|---|
| `tyoh.app` | Hub / launcher | Planned |
| `units.tyoh.app` | [OmniUnitConverter-Calculator](https://github.com/tyohDeveloper/OmniUnitConverter-Calculator) | Currently at apex; scheduled to move |
| `history.tyoh.app` | **History & Prehistory** (this repo) | v0.5.0 · dataset v3.1.0 — picker, calendars, and lens working; not yet deployed |
| `earth-cosmos.tyoh.app` | Deep Time — cosmology, geology, evolution | Planned |
| `decay.tyoh.app` | Nuclear, particle, and atomic timescales | Planned |

Cross-links run one direction only, from smaller timescale to larger: Decay → Deep Time → History.
History is the leaf and has no outbound arrows.

## License

[MIT](LICENSE). The dataset is MIT alongside the code; individual facts are not copyrightable, and
per-entity source attribution is a tracked gap (see the gap analysis, §5.2).

## Coding & architecture standards

All code in this repository follows **[`docs/CODING-STANDARDS.md`](docs/CODING-STANDARDS.md)** — the binding rules for layer boundaries, purity, function and file size limits, naming, data externalization, testing, and dependency budgets. Read it before making changes.

Key hard limits: exported function bodies ≤ 20 lines; one export per pure-logic file; pure-core files ≤ 100 lines, other pure/state/controller files ≤ 150, view files ≤ 250 with ≤ 80 lines of markup in the return. §0 of that file maps those layer roles to this repository's actual directories.

The canonical source of truth is the `programming` project knowledge wiki page `concepts/coding-architecture-standards`; the in-repo file is a derived copy. Amend the wiki first, then propagate here.
