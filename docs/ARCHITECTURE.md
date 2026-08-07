# Architecture & coding rules

Rules for anyone — human or coding agent — working in this repo. Read before making changes.
These are the standalone-HTML5 deployment-target standards as they apply here; the reference
implementation of the same pattern is
[OmniUnitConverter-Calculator](https://github.com/tyohDeveloper/OmniUnitConverter-Calculator).

## 1. Deployment target

Single-file HTML5. One `.html` artifact with all CSS, JS, and data inlined, served from a static
host or opened directly from `file://`. Offline use is a first-class distribution mode, not a
fallback.

If a requirement arrives that this target cannot meet — user accounts, cross-device sync, server
state — the app has outgrown the target. Do not bolt a backend on. Escalate the decision.

## 2. The no-network rule

The app makes **zero** outbound requests at runtime. This is enforced three ways:

1. A strict CSP `<meta>` in `index.html`: `default-src 'self' 'unsafe-inline'; connect-src 'none';
   frame-src 'none'; object-src 'none'; base-uri 'none'`.
2. `scripts/verify-build.mjs` greps the built artifact for `fetch(`, `XMLHttpRequest`,
   `sendBeacon`, `new WebSocket`, `serviceWorker`, `RTCPeerConnection`, and `EventSource`, and
   fails the build on any hit.
3. A Playwright test asserts no non-`file://` request fires on load.

**Consequence for data loading:** the dataset is imported as an ES module
(`import entities from "../data/entities.json"`) so Vite inlines it at build time. Never
`fetch("./data/entities.json")` — it fails from `file://`, the CSP blocks it, and the build check
rejects it.

`modulePreload` is disabled in `vite.config.ts` because Vite's preload polyfill injects a
`fetch()` call. A single-file artifact has nothing to preload.

## 3. The no-storage rule

No `localStorage`, `sessionStorage`, `IndexedDB`, or cookies — not for preferences, not for
last-used settings, not for anything. Reloading starts from a clean slate, and the UI says so.
Also build-checked.

If state is worth keeping, put it in `location.hash` so the **user** decides whether to persist it
by bookmarking. That is compatible with `file://` and needs zero storage APIs.

## 4. Layers

```
src/lib/*     Pure functions. No DOM, no globals, no side effects. Unit-tested.
src/main.ts   UI. Rendering and event wiring. Exercised via Playwright, not unit tests.
src/data/*    Generated JSON. Read-only and immutable at runtime.
tools/*       Python generators and validator. The authoring surface for the dataset.
```

Logic belongs in `src/lib/`. If a function can be written without touching the DOM, it goes there
and it gets a unit test. This is the boundary that keeps the test suite fast and meaningful.

## 5. Testing

- **Unit (Vitest)** — the pure library layer, plus dataset integrity assertions that run against
  the real committed JSON.
- **E2E (Playwright)** — runs against the **built artifact over `file://`**, never the dev server.
  This is the point: it catches inlining bugs, CSP violations, and offline breakage that
  `npm run dev` hides.
- **Dataset (Python)** — `tools/validate.py` checks every JSON file against its schema plus
  referential integrity. Runs as its own CI job.

`tests/dataset-integrity.test.ts` contains a `known v2.1.0 gaps are still gaps` block that asserts
current gap counts (zero `sources`, 267 `calendar_ids`, 6 of 43 region summaries). These are
**expected to fail when the gap is closed** — update the number in the same commit that closes it.
They exist so silent partial backfills cannot drift unnoticed.

## 6. Build chain

`npm run build` = `check` → `test:run` → `build:bundle` → `minify:artifact` → `verify:build`.
It fails at the first stage error. CI runs the identical command, so "works on my machine" is not
a thing that can happen.

`verify:build` enforces: single-file output with no siblings, no external URLs, no forbidden
network or storage APIs, CSP present with `connect-src 'none'`, strict-XML-parseable shell, no
`]]>` in inlined bodies, full test-ID manifest coverage, and gzip within 5% of the recorded
baseline.

## 7. Markup

Ship `.html` so browsers use the forgiving parser, but keep the markup strict-XML valid. Boolean
attributes are expanded to long form (`disabled="disabled"`) by the minifier pass, closing slashes
are preserved, and the shell is XML-parsed as a build check. This keeps the artifact portable to
XHTML serving without making parse failures user-visible.

## 8. Test IDs

Format: `{role}-{area}-{name}[-{key}]`. Examples: `input-search-query`, `region-column-0`,
`option-tree-node-east-asia.japan`.

Statically-present IDs go in `scripts/testid-manifest.json` under `required` and are coverage-
checked against the artifact. IDs built from template literals (`region-column-${depth}`) cannot
be found by a static grep — list those under `dynamic` for documentation and cover them with
Playwright instead.

## 9. Dataset changes

`src/data/*.json` is **generated**. Do not hand-edit it. Change `tools/build_data.py` or an
extension module, regenerate, run `tools/validate.py`, and commit source and output together.

Known constraint from the gap analysis (§5.1): the `R()` and `P()` builder helpers do not accept
`date_note`, `*_year_min/max`, `*_precision`, `links`, or `sources`. That is the mechanical reason
seven schema fields are unused dataset-wide. **Extend the helpers before authoring the prehistory
branch**, or prehistory will accrue the same debt — and prehistory is the branch that most needs
uncertainty ranges and source attribution.

`entity.schema.json` sets `additionalProperties: false`, so adding a field (e.g. the planned
optional `subkind`) requires a schema bump, not just an authoring convention.

## 10. Links

Every outbound link is user-initiated, opens in a new tab with `rel="noopener noreferrer"`, has
descriptive text (never a bare URL or "click here"), and carries no tracking parameters. Allowed
destinations: the sources page, this repo, the MIT license, named external references cited in a
readout, and sibling apps in the tyoh.app family.

## 11. Commits

Terse messages. Decompose large changes. One concern per commit. Plan checkpoints land in the repo
before large build phases begin, not after.

## 12. Open decisions

The live register is [`DESIGN.md`](DESIGN.md) §Open items (`Q-n` ids). Dataset-side items are in
[`gap-analysis-v2.1.0.md`](gap-analysis-v2.1.0.md) §7. Open items are tracked in these documents
rather than GitHub issues for now.

The four that block code:

1. **Timeline scale** across 3.3 Ma to present — piecewise-compressed scrubber with a visible
   scale break is the current recommendation, unresolved.
2. **Holocene handoff target** for the inbound Deep Time cross-link — no dataset node marks the
   boundary yet.
3. **Shared Temporal/JDN layer** — whether History bundles its own copy or consumes a shared
   source package. Affects the multi-calendar readout.
4. **Prehistory dating regime** — recommendation is a separate `dating_method` field plus
   asymmetric bounds via existing `*_year_min/max`, rather than overloading `date_precision`
   (currently 95% `approx`, carrying no information).
