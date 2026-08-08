# Pending project-wiki edits

Three edits that could not be written on 2026-08-08 because the Project CLI was disabled for that
session (`pplx project is not available: the Project CLI is not enabled for this session`, every
`pplx project *` subcommand). Apply them from a session where `pplx project knowledge sync` works,
then delete this file.

They matter more than housekeeping: **edits 2 and 3 are why `src/lib` keeps coming back.** The wiki
prohibits `lib` as a directory name in one page and instructs agents to create `src/lib/` in two
others. A coding agent reading the layout instruction is following the wiki, not ignoring it.

---

## 1. `concepts/repository-conventions.md` line 30 — versioning

The rule contradicts its own example: it mandates semver while citing a four-part version.

**Replace:**

```
- **Semantic versioning for anything tagged and released** — OmniUnit's v5.0.0.0 already follows a version scheme; new repos use semver from the first release[cite:5].
```

**With:**

```
- **Four-part versioning for anything tagged and released** — `MAJOR.MAJORFIX.MINORFIX.SPELLING`, significance falling left to right: major application or database change; major bug fixing, multi-file changes, minor UI changes; minor bug fixes; spelling. Deliberately not semver — semver encodes an API compatibility promise, and these apps have no API consumers, so it has one slot where this scheme needs three. OmniUnit already uses it at v5.0.0.0[cite:5]; History & Prehistory uses it on two independent tracks, app and data, tagged `<id>-app` and `<id>-data`. A leading digit is a readiness claim: History's app is 3.1.x.x because it works as intended while its data is 0.5.x.x because it is materially incomplete. Never tidy one track to match the other.
```

## 2. `concepts/coding-standards-standalone-html5.md` line 109 — prescribes `src/lib/`

**Replace:**

```
3. **Copy the OmniUnit repo layout:** `src/` for TypeScript, `src/lib/` for pure-library functions, `src/data/` for JSON, `docs/` for reference material, `.github/workflows/` for CI.
```

**With:**

```
3. **Repo layout:** `src/` for TypeScript with one directory per domain, `src/data/` for JSON, `docs/` for reference material, `.github/workflows/` for CI. Domain directories name what they own — History & Prehistory uses `calendars/`, `chrono/`, `temporal/`, `entity/`, `dataset/`, `focus/`, `research/`. There is no `src/lib/`: it is prohibited by the naming rule in `coding-architecture-standards`, and prescribing it here is what caused it to be recreated repeatedly in History & Prehistory.
```

## 3. `concepts/coding-standards-hosted-postgres.md` line 98 — prescribes `src/lib/`

**Replace:**

```
4. **Repo layout:** `src/server/` for routes and middleware, `src/db/` for schema and migrations, `src/lib/` for pure logic, `src/client/` for frontend if colocated, `tests/` for E2E and integration.
```

**With:**

```
4. **Repo layout:** `src/server/` for routes and middleware, `src/db/` for schema and migrations, `src/client/` for frontend if colocated, `tests/` for E2E and integration. Pure logic goes in domain-named directories, never `src/lib/` — see the naming rule in `coding-architecture-standards`.
```

---

## Verifying afterwards

```bash
grep -rn "src/lib\|semver" concepts/    # should return nothing
```

The repo side is already done: `docs/CODING-STANDARDS.md` §12 carries four-part versioning, and
`tools/check_standards.py` fails the build on any shape-named path.
