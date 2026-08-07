# Working in this repo

Read [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) first. It is short and it is binding.

The five rules most likely to be violated by accident:

1. **No `fetch()`.** The dataset is inlined at build time via `import`. A runtime fetch fails from
   `file://`, is blocked by the CSP, and fails the build check.
2. **No `localStorage` / `IndexedDB` / cookies.** Session state is in-memory only. Use
   `location.hash` if state must survive a reload.
3. **No CDN anything.** No external fonts, scripts, images, or styles. Everything inlines.
4. **`src/data/*.json` is generated.** Edit `tools/build_data.py`, regenerate, validate, commit
   both.
5. **New test ID means updating `scripts/testid-manifest.json`** in the same change.

Before proposing dataset content, read [`docs/gap-analysis-v2.1.0.md`](docs/gap-analysis-v2.1.0.md).
It records where the data is thin and, more importantly, which schema fields are unusable until
the Python builder helpers are extended.

Verify with `npm run build && npm run test:e2e`. Both must pass.
