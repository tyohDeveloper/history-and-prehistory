# Corrections extraction report

Input: the six `docs/review-findings-*.md` files (4,702 lines, 449 finding blocks).
Output: `docs/review/corrections.json` — **136 patch entries** covering 54 accepted findings.

Every accepted finding was re-checked against `src/data/entities.json` before being emitted, so
`from` values are the live values in the dataset as of this pass.

## Per-file tally

| File | High-confidence findings | Accepted | Dropped as moot | Dropped: ambiguous / not field-applicable | Dropped: bad id | Patch entries |
|---|---|---|---|---|---|---|
| review-findings-reigns.md | 14 | 3 | 4 | 7 | 0 | 3 |
| review-findings-cities-1.md | 18 | 10 | 2 | 6 | 0 | 40 |
| review-findings-cities-2.md | 28 | 12 | 8 | 8 | 0 | 21 |
| review-findings-polities.md | 29 | 22 | 1 | 6 | 0 | 58 |
| review-findings-periods.md | 11 | 6 | 2 | 3 | 0 | 8 |
| review-findings-concepts.md | 15 | 4 | 3 | 8 | 0 | 6 |
| **Total** | **115** | **57 blocks → 54 applied** | **20** | **38** | **0** | **136** |

Medium, low, medium-high and low-medium findings (334 blocks) were ignored per instruction.
One finding block covers two entities in several cases, which is why entry counts exceed finding
counts.

## Breakdown by field

| Field | Entries |
|---|---|
| kind | 52 |
| start_dating_method | 29 |
| aliases | 15 |
| end_year | 13 |
| extant | 9 |
| start_year | 5 |
| historicity | 5 |
| summary | 4 |
| parent_id | 3 |
| end_dating_method | 1 |

No bounds/uncertainty fields are emitted. All field names are validated against
`schemas/entity.schema.json`; all `kind`, `historicity` and dating-method values are schema enum
members.

## Ids

- Reviewer id corrected: `east-asia.city-taihe` → **`east-asia.city-taihe-dali`** (name "Taihe",
  the Nanzhao capital). No other accepted finding had a nonexistent id.
- Dropped for an unresolvable id: **0**.

## Dropped as moot (20)

- **Bounds / uncertainty** (fabricated bounds since deleted): reigns P1, P2; polities PATTERN‑1
  bounds half and `americas.north.haudenosaunee`; periods P1 (51 nengō) and
  `americas.andes.inca.machu-picchu`; concepts P1, `west-asia.iran.arab-conquest`.
- **Already re-kinded to `site`**: cities‑1 PATTERN‑1 and the 14 self-declared NOTCITY rows;
  cities‑2 Stonehenge, Masada, Qumran, Yazılıkaya, Didyma, Konark, Olympia/Nemea,
  Tara/Þingvellir.
- **Already fixed**: `europe.western.netherlands` is now `kind: polity`;
  `oceania.peoples-aboriginal-australians` is now `luminescence`; the 51 nengō already carry
  `calendar` start/end dating methods; `africa.nile.egypt.tip.dyn25.piye` and `.taharqa` already
  point at the existing `dyn25-kushite` parent.

## Dropped as ambiguous or not expressible as a field patch (38)

Representative cases:

- **Entity splits / merges**, which no single-field patch can express: Zhongzong and Justinian II
  (interrupted reigns), Gurganj/Konye-Urgench, Cebu/Sugbu, Ryazan, Tarxien's three temple sites
  (only its `kind` was patched).
- **Id renames**: `europe.city-cologne-dorestad`, `west-asia.city-dezful-jundishapur`,
  `south-asia.city-sirsukh-sialkot`, `europe.city-naples-cuma`,
  `africa.city-koumbi-tegdaoust-note`.
- **Two candidate target values offered**, so the choice would be mine, not the reviewer's:
  `date_standing` "minority or majority" on `stone-knapping` and `cooking` (both still
  `consensus`); `dated_by` "received or typological" on `global.languages.avestan` and the sack of
  Babylon; `historicity` "legendary or contested" for Thinis, Njimi, Khyunglung, Yumbulagang;
  Ōtsu (rename or un-end); Hammurabi ("not `calendar`", no replacement named).
- **No concrete value given**: the regional `Prehistory` container starts (polities PATTERN‑3,
  `west-asia.prehistory`, `east-asia.prehistory`), `global.bce`/`global.ce`,
  `global.multi-regional`, the India/Pakistan office-holder lists, `global.paleolithic.later-stone-age`,
  `europe.city-mystras` ("c. 1830s"), `global.prehistory.hominins.homo-luzonensis`
  ("roughly −65,000 to −48,000"), Byblos's start ("−5000 or earlier"),
  `southeast-asia.prehistory.yangtze-rice` (reparent or merge).
- **File-wide metadata patterns with no per-row id list or a mixed target**: reigns P3/P4/P5/P7,
  cities‑1 PATTERN‑2 (`typological` → "calendar or received" for ~30 named foundations),
  concepts P2/P3/P5, periods P4 (bare nengō), the Jenne-jeno vs Dia priority clash.
- **Judgement-dependent members of accepted patterns**: within polities PATTERN‑1 I applied
  `start_dating_method: calendar` only to foundings fixed by annals, and excluded Kievan Rus' 862
  (Primary Chronicle legend), the Khmer Empire 802, the Chola 848 and Rise of Islam 610, whose
  dates are traditional or approximate rather than calendrical.

## Notes on how accepted patterns were applied

- Conquest-is-not-an-ending cases emit two entries each (`end_year: null` **and** `extant: true`):
  Tenochtitlan, Aquileia, Tahert, Tyre, Sidon, Byblos, Arwad, Anuradhapura.
- `aliases` entries are complete replacement arrays; only annotation-style entries named by the
  reviewer were removed ("flooded", "Cerne?", "… nearby", "… capital", the date-bearing Đại Việt
  alias). `africa.city-buhen` becomes an empty array because its only alias was
  "flooded by Lake Nasser".
- Not-a-city rows still typed `city` were moved to the new `site` kind (the only schema kind that
  fits sanctuaries, necropoleis, earthworks and engineered landscapes); none of them has children,
  so the re-kinding is safe. `southeast-asia.city-mataram-medang` went to `polity` instead, per its
  own summary.
- `summary` corrections are minimal in-place edits of the wrong clause, not rewrites.
