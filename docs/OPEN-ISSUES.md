<!--
  Tracked open issues. Mirrored as GitHub issues; this file is the version an
  agent reads without a network call, and the one that survives in the repo.

  Two rules for this file:

  1. An issue is only removed when the work is done, not when it is discussed.
  2. Each entry says how it was FOUND, because the pattern matters more than the
     individual bug. Five of the bugs fixed so far were found by looking at a
     screenshot and none by a test, which is itself the most useful finding in
     the project and should not be quietly forgotten.
-->

# Open issues

Status as of app v3.26.0.0 / data 0.27.0.0 — 1,653 entities, 578 sources, 402
cited, 223 unit tests, 39 e2e tests.

Mirrored as GitHub issues #2-#14. Numbers here are re-measured each release;
trust the snippets over the prose.

## Honesty gaps — data collection reduces these

These are counted, not estimated. Re-measure with the snippets given rather than
trusting the numbers here.

### 1. Unsourced dates on foundational entities

**298 of 451** foundational entities display a date with no source behind it.

| Region                   | Unsourced |
| ------------------------ | --------- |
| europe                   | 73        |
| east-asia                | 53        |
| south-asia               | 51        |
| africa                   | 30        |
| west-asia                | 27        |
| global (incl. retired cross-regional) | 37 |
| americas                 | 12        |

The app is honest about this — an unsourced date carries "This date is not yet
sourced in the dataset. Treat it as a starting point and verify it." — so this is
a coverage gap rather than a correctness lie. Every citation pass reduces it.

```bash
python3 -c "
import json
es=json.load(open('src/data/entities.json'))['entities']
f=[e for e in es if e['tier']=='foundational' and (e.get('start_year') is not None)]
print(sum(1 for e in f if not e.get('source_ids')), 'of', len(f))"
```

### 2. Missing summaries

15 foundational, 212 intermediate, 506 specialist entities have no summary.
The specialist gap is arguably correct — a reign that lasted three years may have
nothing to say beyond its dates. The 15 foundational ones are the real bug.

## Structural — data collection will NOT fix these

### 3. Postal romanisation is absent — Wade-Giles is done

**Wade-Giles resolved in v3.26.0.0** (#3). Nine dynasties carry their Wade-Giles
form; Ch'ing, Chou, Sung, T'ang, Yüan, Hsia and Chin all resolve in search.

**Postal romanisation is still absent and is blocked, not pending.** Peking,
Nanking, Canton, Amoy and Chungking are *place* names, and the dataset contains
no Chinese cities to attach them to. Needs place entities first.

### 3b. Chinese dynastic tiers are inconsistent (#13)

With Five Dynasties at `specialist`, a default-tier reader sees Tang (618-907)
and Song (960-1279) as adjacent and the 53-year interregnum vanishes. The same
holds for the Jin of 266-420 and the Northern and Southern Dynasties: **periods
of division are systematically less visible than periods of unity**, which either
is a defensible editorial line or makes Chinese history look more continuous than
it was. Needs a stated principle for what the default tier is for.

The Sui was fixed in v3.26.0.0 because it was unambiguous — it reunified China
and was hidden while conquest dynasties were about to be visible.

### 4. `name_forms` has no kind for two real classes of variant

The 54 entities with untyped `aliases` cannot all be converted, because the eight
existing kinds (endonym, exonym, formal, common, translation, scholarly,
historical, rejected) do not cover what those aliases actually are:

- **Orthographic** — the same name with diacritics stripped for ASCII search:
  Ertebølle/Ertebolle, Starčevo, Vinča, Đa Bút, Mán Bạc, Cucuteni–Trypillia.
  Not a different name, a different encoding of one.
- **Abbreviation** — PPNA, PPNB, TRB, 9/11.

Both are findability aids rather than naming claims, and flattening them into
`scholarly` or `common` would be false. Adding two kinds is the likely fix, but
it is a schema change and should be decided deliberately.

A third class is genuinely interpretive and must NOT be converted mechanically:
"Golden Age of India" for the Gupta Empire is a contested value judgement, and
Tripolye vs Cucuteni–Trypillia is a Russian/Romanian naming split. These need
scholarship, not typing.

### 5. Authored region lists carry no sources

The nine `cross_parent_ids` region lists on the multi-regional empires are
territorial claims asserted with no citation and no unsourced marker — currently
the only field in the dataset that is neither sourced nor visibly marked as
unsourced. Two are known judgement calls: Rashidun excludes Central Asia
(Khorasan came at the very end), and Columbus is limited to the Americas and
Europe rather than everywhere the consequences reached.

### 6. `researchNote` is wired to nothing

Exported from `handoff.ts` and covered by tests, but reachable from no control in
the UI. Either wire it up or delete it; a tested dead export is worse than
either, because the tests imply it works.

### 7. `npm ci` fails outside Replit

`package-lock.json` pins `http://package-firewall.replit.local/npm/`, so CI is
probably broken and all verification has been local. Workaround:

```bash
cp package-lock.json /tmp/lock.keep.json
sed -i 's|http://package-firewall\.replit\.local/npm/|https://registry.npmjs.org/|g' package-lock.json
npm ci
cp /tmp/lock.keep.json package-lock.json
```

### 8. `build_data.py` holds 3,280 lines of un-extracted inline data

Measured: 3,368 lines total, 58 imports, 30 module calls, and the remaining
~3,280 lines are inline entity data that never got extracted into modules the way
the other thirty did.

**Deliberately deferred.** The instruction is to refactor when the cost of
complexity exceeds the cost of refactoring, and it has not yet. Note for whoever
picks this up: the large generated files are *not* the problem —
`src/data/entities.json` is 27,499 lines and costs nothing, because it is queried
rather than read, and sharding it would mean knowing which shard holds an entity
before looking it up. This one file is the actual friction.

## Cultural and editorial questions still open

### 9. The caliphate naming sequence

Rashidun, Umayyad, Abbasid and Fatimid are modelled as four sequential polities,
but they are overlapping claims to a single office — and the Fatimids claimed it
while the Abbasids held Baghdad. The current structure implies a clean succession
that did not happen.

### 10. Multilingual architecture

`native_name` is the only reader-independent name field. Everything else assumes
an English-reading audience, including the decision that `name` is "the name a
reader arrives with". Localisation would force that question open.

The homograph bug fixed in v3.25.0.0 is the first concrete instance: romanisation
collapsed 昭和 and 正和 into one string, and twelve Japanese era pairs were
indistinguishable in search. Expect more of this shape.

### 11. Gupta "Golden Age of India"

Left as a flat alias deliberately. Needs scholarship on who coined the framing
and what it obscures before it can be typed as `historical` or `rejected`.

## Contested sovereignty

See `overlap-and-rival-claims.md`. Short version: the "988 overlapping pairs" figure
was misleading — overlap is normal and the dataset handles it. The real gap was
`rival_claimant_to`, now applied to four pairs, and `links` now renders at all.
More rival pairs remain (antipopes, Japan's Northern and Southern Courts, the Three
Kingdoms); each needs judgement, and none can be found by measuring dates.

## Updating the pinned baselines

`python3 tools/baselines.py` prints committed versus current for the fifteen pinned
test baselines; `--update` rewrites the drifted ones. Review the printed table, then
review `git diff`.

The brittleness of those baselines is deliberate and stays — a pinned count is a
tripwire. The *transcription* was the risk, and it misfired twice: once setting the
cited-entity baseline to 620 when the test measures something else and wanted 440,
and once changing the end-dating count to 332 when the pass had added none. Both
failed loudly. A wrong-but-*passing* baseline would not have.

The tool refuses to run when a pattern stops matching, rather than skipping the
baseline, because a silent no-op edit is how a validator rule once got "tested"
while never being in the file at all.

Not automated on purpose: the split-dating-method catalogue, which is a
hand-curated registry whose point is that a human decides membership.

## The gap report

`python3 tools/report_gaps.py` looks for places where the dataset **implies an
entity it does not contain**. It is a report, not a validator, and the build does
not fail on it: every heuristic has honest false positives, and deep-prehistory
branches dominate the raw output because gaps of 100,000 years there are real.

It was written after the same structural failure turned up twice by accident, in
unrelated regions — the Song split at 1127 with none of the states that caused
it, and Majapahit standing with no predecessor. Nothing in a schema can express
"this entity implies a missing one", so no test could have caught either.

On first run it found the two largest remaining holes immediately:

- **Central Asia** had nothing between 1400 BCE and 1206 CE in one branch.
- **Iran** jumps from the Sasanians ending 651 to the Safavids starting 1501 —
  an 850-year hole across the entire Islamic medieval period.

## Method note: where bugs actually come from

Five bugs have been found by rendering the app and looking at it, and **none** by
the test suite:

1. Eleven sources rendered their kind badge as `UNDEFINED` — three `SourceKind`
   definitions had drifted apart and from the data.
2. `citationOrder` ignored `name_forms`, so sourced name changes showed no marker.
3. Alternatives panel said "Competing dates" for alternatives carrying no year.
4. The Indus summary asserted "Sarasvati" as fact directly above the caveat
   calling that name contested.
5. Search showed two identical `Shōwa` rows.

A sixth was found by reading a rendered column rather than the app's logic: the
Sui was missing from the default view of Chinese dynasties, which no test asserted
because no test knew it should be there.

The pattern: **prose and rendering are unvalidated.** Tests check structure, and
every one of these lived in something no schema constrains. Screenshot the app
after any change that touches display.
