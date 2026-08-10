# Pre-Publish Security Review — History & Prehistory (`/home/user/workspace/hp`)

Reviewed at git HEAD `5947092` ("release: app 3.29.0.0, data 0.30.0.0 (v0.30.0.0)"), diffed against last-reviewed tag `v3.24.0.0-app`.

## Scope of the delta reviewed
`git diff v3.24.0.0-app..HEAD -- src/main.ts src/style.css scripts/` (161 lines):
- `src/main.ts` (+41/-2): a search-result homograph disambiguator (appends native-script name when two hits share a romanized name) and a per-name-form annotation note (attributes notes to the correct name when a group has more than one annotated form).
- `src/style.css` (+16): styling for the two additions above (`.disambig`, `.name-form-note-for`).
- `scripts/normalize-lockfile.mjs` (new, 41 lines): CI-only lockfile URL rewriter.
- `scripts/build-baseline.json`: bundle-size baseline number bump (non-functional).

The "Also under `<regions>`" line predates this tag (already present at v3.24.0.0-app) but was checked anyway per the task's rendering-safety focus.

---

## Security Review Results

### BLOCK (must fix before publishing)
None.

### WARN (inform user, let them decide)
None.

### PASS
- **Unsafe DOM sinks (delta + whole repo)** — Grepped `src/`, `scripts/`, `tools/` for `eval(`, `new Function(`, `innerHTML`/`outerHTML` assignment, `insertAdjacentHTML`, `document.write(`, `dangerouslySetInnerHTML`. Zero real matches. (One grep hit at `tools/build_data.py:1719` was `_central_asia_medi​eval(` — a substring false-positive, not an `eval(` call.) All three new rendering features (`src/main.ts:83-110` disambiguator, `src/main.ts:126-134` per-name notes, `src/main.ts:346-354` "Also under" line) build DOM exclusively through the local `el()` helper (`src/main.ts:136-141`), which uses `document.createElement` + `Node.setAttribute` + `Node.append(string)` — `.append()` on a string always creates a text node, never parses HTML. Entity-derived strings (`e.name`, region names, `f.note`, `native_name`) can never execute as markup or script through this path.
- **`src/data/*.json` content cannot execute as script** — All data-derived text reaches the DOM only via `el()`'s text-node path (see above) or via `.textContent`-equivalent `append(string)` calls; no template-literal-to-`innerHTML` pattern and no `JSON.parse` result is ever fed to `eval`/`Function`.
- **URL scheme safety of `href`s** — Enumerated every `href:` assignment in `src/main.ts` (lines 556, 684, 920):
  - `src/main.ts:556` — `href: src.url` — `src.url` comes from `sourceById`, built solely from `src/data/sources.json` (`src/dataset/dataset.ts:1-27`). `tools/validate.py` rule 6a (`tools/validate.py:171-187`) enforces `^https?://` (`_SAFE_URL`) on every `sources[].url` in that file, so this is fully covered.
  - `src/main.ts:684` — `href: t.url` — `t.url` comes from `handoffTargets()` → `wikipediaSearchUrl()` (`src/research/handoff.ts:99-102`), which builds the URL from a hardcoded `https://${lang}.wikipedia.org/...` template with `encodeURIComponent(query)`; it is never taken verbatim from data, so it cannot become a `javascript:`/`data:` URI regardless of dataset content.
  - `src/main.ts:920` — `href: REPO_URL` — a hardcoded constant, not data-derived.
  - No other `href`-producing code path exists in `src/`.
  - **Validate.py coverage note (not a vulnerability, documented for completeness):** rule 6a also loops over `entity.get("links", [])[].url` (`tools/validate.py:184-187`), but per `schemas/entity.schema.json:331-372` and `src/entity/entity.ts:96`, the entity `links` array's items are `{type, entity_id, note}` with `additionalProperties: false` — there is no `url` property in that shape, so this half of the rule can never find anything to check; it's inert, not a bypass, because that field can't carry a URL in the first place. Separately, `entity.sources[].url` (`schemas/entity.schema.json:385-399`, `src/entity/entity.ts:134`) is a distinct, valid-looking optional field that **is not checked** by rule 6a and **is not rendered anywhere** in `src/main.ts` (only the global `sourceById`-backed `sources` panel is rendered, confirmed via `renderSources()` at `src/main.ts:541-573`) — and it is **not populated in any of the 1,705 entities** (checked programmatically). Since it's both unrendered and unused, it currently poses no exploitable path, but if a future change ever starts rendering `entity.sources[].url` as an href, it would bypass the existing scheme check. Worth a one-line addition to validate.py if that field is ever wired up.
- **Secrets/credentials** — Full-repo grep (patterns: OpenAI/AWS/GitHub/GitLab/Slack tokens, PEM private keys, hardcoded passwords) across all source, config, and script files, excluding `node_modules/`, `.git/`, `dist/`: zero matches. No `.env` files present anywhere in the repo.
- **Dependency audit** — `npm audit --json`: 0 critical, 0 high, 0 moderate, 0 low, 0 info vulnerabilities.
- **CORS / server endpoints** — No server code exists (static single-file app); grep for CORS/`Access-Control-Allow-Origin` patterns returned nothing. Not applicable.
- **New build script (`scripts/normalize-lockfile.mjs`)** — Reads `package-lock.json`, does a plain regex string replace of `http(s)://package-firewall.replit.local/npm/` → `https://registry.npmjs.org/`, writes the file back. No `eval`, no shell-out, no dynamic code execution, no secrets. Confirmed wired into `.github/workflows/build.yml` (lines 30, 53) exactly as documented — runs before `npm ci`, is idempotent. No security concern.
- **Runtime network calls** — No `fetch(`, `XMLHttpRequest`, `WebSocket`, `EventSource`, or `sendBeacon` anywhere in `src/`. `index.html` and the built `dist/public/index.html` both ship `Content-Security-Policy: default-src 'self' 'unsafe-inline'; connect-src 'none'; frame-src 'none'; object-src 'none'; base-uri 'none'`, which would block any runtime network call even if one were later added.
- **LLM/external API/connector usage** — No references to OpenAI/Anthropic/Perplexity APIs, no `process.env` reads, no API-key patterns anywhere in `src/`.
- **Local persistence** — No `localStorage`, `sessionStorage`, `indexedDB`, or `document.cookie` usage anywhere in `src/` (confirmed by grep; also explicitly asserted in a code comment at `src/calendars/selection.ts:4`). State lives only in the URL hash (`syncHash()`, `src/main.ts:130-134`), which is standard client-side routing, not persistence.
- **Publish artifact scope** — `dist/` is git-ignored and contains exactly one file, `dist/public/index.html`, matching the described single-file architecture. `playwright-report/` and `test-results/` are also git-ignored and won't be published.

### Minor observation (informational only, not BLOCK/WARN)
- `researchNote()` (`src/research/handoff.ts:130`) and its doc comment describing a `Blob` + `URL.createObjectURL` download are dead code — the function is defined but never called from `src/main.ts`, and no actual `Blob`/`createObjectURL` call exists in the codebase. This is a functional gap (a documented feature that isn't wired to the UI), not a security issue — it doesn't run, so it can't violate the CSP or leak anything.

---

## Conclusion
No BLOCK or WARN findings. The reviewed delta (native-script disambiguator, per-name annotation notes, "Also under regions" line, and the new lockfile-normalization script) introduces no unsafe DOM sinks, no script-execution path for JSON data, and no way for a `javascript:`/`data:` URI to reach a rendered link. All `href`s are either covered by `tools/validate.py`'s `^https?://` rule against `sources.json`, or generated by hardcoded/encoded templates that never take a raw string from data. No secrets were found, dependency audit is clean, and the app has zero runtime network calls, zero LLM/connector usage, and zero local-filesystem/storage persistence — consistent with its "no data stored, no network requests" footer claim. Safe to publish as-is.
