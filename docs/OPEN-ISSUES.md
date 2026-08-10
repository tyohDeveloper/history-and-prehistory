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

Status as of app v3.25.0.0 / data 0.26.0.0 — 1,648 entities, 561 sources, 223
unit tests, 39 e2e tests.

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

### 3. Wade-Giles is entirely absent

**In progress.** A reader holding any pre-1980s book on China searches Ch'ing,
Chou, Ch'in, Sung, T'ang, Hsia — and finds **nothing**. Verified: none of those
forms appear in any alias. Only 2 of 158 Chinese entities have `name_forms` at
all (ROC and PRC).

Postal romanisation (Peking, Nanking, Canton, Amoy, Chungking) is a second,
separate system with the same problem.

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

The pattern: **prose and rendering are unvalidated.** Tests check structure, and
every one of these lived in something no schema constrains. Screenshot the app
after any change that touches display.
