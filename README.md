# History & Prehistory

A structured picker for historical and prehistoric periods, eras, dynasties, rulers, and events.
Ships as **one HTML file** that runs offline from `file://`, stores nothing, and makes no network requests.

Planned home: **`history.tyoh.app`** — the History member of the [tyoh.app tools family](#the-tyohapp-family).

> **Status:** v0.1.0 baseline. The v2.1.0 dataset (1,305 entities) and the Miller-column picker
> are in place. The prehistory extension, multi-calendar readout, and multi-script input grammar
> are not built yet. See [`docs/gap-analysis-v2.1.0.md`](docs/gap-analysis-v2.1.0.md) for the roadmap.

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
| Version | 2.1.0 (schema 1.0.0) |
| Entities | 1,305 — 43 regions, 248 eras, 343 periods, 643 reigns, 28 events |
| Tiers | 337 foundational · 416 intermediate · 552 specialist |
| Calendars | 21 dating systems, including the full Japanese nengō sequence |
| Themes | 16 cross-cutting collections |
| Reference frames | 37 novice-friendly anchor dates |

Authoritative sources are `schemas/` (JSON Schema) and `tools/` (Python generators + validator).
`src/data/*.json` is generated output, committed so the build is reproducible without Python.

Every entity carries `start_year` / `end_year` in **proleptic Gregorian** — negative is BCE, and
there is no year zero. That single axis is what makes cross-regional "what else was happening?"
queries cheap.

`docs/gap-analysis-v2.1.0.md` is a full audit of this dataset: regional sparsity, chronological
holes, incomplete ruler lineages, prehistory attach points, and schema debt. Read it before
authoring new content — several of its findings are load-bearing for how the next region should
be written.

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
  main.ts               UI layer — rendering and event wiring
  style.css
  lib/
    types.ts            Entity/Calendar/Theme types mirroring schemas/
    dataset.ts          Build-time inlined data (no runtime fetch)
    tree.ts             Pure functions: index, path, search, tier, formatting
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

No UI framework. The picker is a tree renderer over a static dataset — a framework would cost
bundle budget that the 1,305-entity dataset needs, and would not remove any real complexity.
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
| `history.tyoh.app` | **History & Prehistory** (this repo) | v0.1.0 baseline |
| `earth-cosmos.tyoh.app` | Deep Time — cosmology, geology, evolution | Planned |
| `decay.tyoh.app` | Nuclear, particle, and atomic timescales | Planned |

Cross-links run one direction only, from smaller timescale to larger: Decay → Deep Time → History.
History is the leaf and has no outbound arrows.

## License

[MIT](LICENSE). The dataset is MIT alongside the code; individual facts are not copyrightable, and
per-entity source attribution is a tracked gap (see the gap analysis, §5.2).
