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

## Coding & architecture standards

Policy: `tyohDeveloper/engineering-standards` release 1.0.1.1 (tag `standards-1.0.1.1`). [`docs/CODING-STANDARDS.md`](docs/CODING-STANDARDS.md) records the adopted release, delivery profile (`none / single-file / none / none / none / interactive`, no localization scope; calendars are domain data), role mapping, enforcement matrix and local extensions; the rule text is retrieved from the hub at that tag. [`STANDARDS-ADOPTION.json`](STANDARDS-ADOPTION.json) is the machine-readable record; [`docs/EXCEPTIONS.md`](docs/EXCEPTIONS.md) lists open exceptions (C-27). [`docs/standards/portable-v2.2.md`](docs/standards/portable-v2.2.md) is the superseded predecessor, kept for history.

Key hard limits (C-11, C-12, C-6): exported function bodies ≤ 20 lines; one export per PURE file; PURE-CORE files ≤ 100 lines, other PURE/STATE/CONTROLLER files ≤ 150, VIEW files ≤ 250. `npm run check:standards` measures them against a ratcheting debt baseline (E-1).

Proposals to change a rule go to the hub, not to this repository.
