# History & Prehistory — Replit workspace notes

Offline, privacy-safe picker for historical and prehistoric periods. Builds to **one
self-contained HTML file** that runs from `file://` with no server and no network.

## Commands

```bash
npm run dev       # dev server, 0.0.0.0:5000
npm run build     # typecheck -> unit tests -> bundle -> minify -> verify
npm run test:e2e  # Playwright against the built artifact over file://
npm run validate:data
```

`npm run build` must pass before anything is considered done. CI runs the identical command.

## Hard rules

Full detail in [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — that file is canonical and wins
over this summary if they ever disagree. The five that get broken by accident:

1. **No `fetch()`, XHR, WebSocket, or Service Worker.** The dataset is inlined at build time via
   `import`. A runtime fetch fails from `file://`, is blocked by the CSP, and fails the build.
2. **No `localStorage`, `sessionStorage`, `IndexedDB`, or cookies.** State is in-memory only; use
   `location.hash` if it must survive a reload.
3. **No CDN anything.** No external fonts, scripts, styles, or images. Everything inlines.
4. **No backend, database, or server.** If a request seems to need one, the app has outgrown its
   deployment target — stop and escalate rather than adding one.
5. **No analytics, telemetry, or tracking.**

**These are machine-enforced, not advisory.** `scripts/verify-build.mjs` greps the built artifact
for every forbidden API and external URL and fails the build on a hit. Adding a `fetch()` breaks
CI; it does not ship.

## Other conventions

- `src/data/*.json` is **generated**. Edit `tools/build_data.py`, regenerate, validate, and commit
  source and output together. `tools/check_regenerated.py` fails CI if they drift.
- Logic belongs in `src/lib/` as pure functions with unit tests. `src/main.ts` is UI only.
- New test ID means updating `scripts/testid-manifest.json` in the same change.
- Bundle size is baselined in `scripts/build-baseline.json`; >5% gzip growth fails the build.
- Terse commit messages, decomposed commits.

## Branches

`main` is the clean baseline. Active design work lives on **`calendar-layer`** — the calendar
registry, chronology model, and dating-disclosure work, with the reasoning in
[`docs/DESIGN.md`](docs/DESIGN.md). Check which branch you are on before starting.
