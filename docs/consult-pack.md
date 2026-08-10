# Consultation pack: History & Prehistory dataset

1765 entities, 0 sources, 33 entity fields.

## Field usage

How often each field is actually populated. A field offered by the schema and used twice is a different thing from a field used everywhere.

| field | populated | of | notes |
|---|---|---|---|
| `aliases` | 191 | 1765 |  |
| `allow_outside_parent_dates` | 92 | 1765 |  |
| `alternatives` | 137 | 1765 |  |
| `as_of` | 63 | 1765 |  |
| `calendar_ids` | 267 | 1765 |  |
| `capital` | 1 | 1765 |  |
| `caveats` | 209 | 1765 |  |
| `cross_parent_ids` | 48 | 1765 |  |
| `date_note` | 520 | 1765 |  |
| `date_precision` | 1743 | 1765 | approx:1493, century:61, disputed:55, unknown:42 |
| `end_dating_method` | 344 | 1765 | radiocarbon-calibrated:201, calendar:54, received:25, typological:19 — never used: potassium-argon |
| `end_precision` | 22 | 1765 | unknown:14, approx:7, year:1 — never used: decade, century, millennium, traditional, disputed, exact, minimum |
| `end_year` | 1648 | 1765 |  |
| `end_year_max` | 8 | 1765 |  |
| `end_year_min` | 8 | 1765 |  |
| `id` | 1765 | 1765 |  |
| `kind` | 1765 | 1765 | reign:690, period:602, era:350, event:43 — never used: city |
| `links` | 15 | 1765 |  |
| `name` | 1765 | 1765 |  |
| `name_forms` | 99 | 1765 |  |
| `native_name` | 378 | 1765 |  |
| `notable_figures` | 1 | 1765 |  |
| `parent_id` | 1755 | 1765 |  |
| `regions` | 98 | 1765 |  |
| `source_ids` | 585 | 1765 |  |
| `standing` | 411 | 1765 | majority:257, consensus:107, traditional:26, minority:21 — never used: superseded |
| `start_dating_method` | 416 | 1765 | radiocarbon-calibrated:218, calendar:51, received:31, typological:24 — never used: potassium-argon |
| `start_precision` | 8 | 1765 | approx:7, minimum:1 — never used: year, decade, century, millennium, traditional, disputed, unknown, exact |
| `start_year` | 1723 | 1765 |  |
| `start_year_max` | 26 | 1765 |  |
| `start_year_min` | 26 | 1765 |  |
| `summary` | 1102 | 1765 |  |
| `tier` | 1765 | 1765 | specialist:606, intermediate:594, foundational:565 |

## Controlled vocabularies

- **`date_precision`**: year, decade, century, millennium, approx, traditional, disputed, unknown, exact, minimum
- **`end_dating_method`**: calendar, dendrochronology, radiocarbon-calibrated, radiocarbon-uncalibrated, argon-argon, potassium-argon, luminescence, uranium-series, esr, layer-counting, cosmogenic, magnetostratigraphy, received, typological, unknown
- **`end_precision`**: year, decade, century, millennium, approx, traditional, disputed, unknown, exact, minimum
- **`kind`**: region, era, period, reign, event, city, taxon, threshold
- **`standing`**: consensus, majority, minority, traditional, superseded
- **`start_dating_method`**: calendar, dendrochronology, radiocarbon-calibrated, radiocarbon-uncalibrated, argon-argon, potassium-argon, luminescence, uranium-series, esr, layer-counting, cosmogenic, magnetostratigraphy, received, typological, unknown
- **`start_precision`**: year, decade, century, millennium, approx, traditional, disputed, unknown, exact, minimum
- **`tier`**: foundational, intermediate, specialist
- **link `type`**: successor_state_of, predecessor_state_of, part_of, contains, conquered_by, conquered, vassal_of, suzerain_of, ruled_by_dynasty, capital_at, split_from, merged_into, co_ruler_with, regent_for, rival_claimant_to, appears_under, same_entity_as, other
- **caveat `kind`**: misconception, naming-confusion, contested-existence
- **alternative `standing`**: consensus, majority, minority, traditional, superseded
- **name_form `kind`**: endonym, exonym, formal, common, translation, scholarly, historical, rejected

## Worked examples: the hard cases

Real records, verbatim. Each strains the schema differently.

### Lomekwian Industry — lithic industry at 3.3 Ma -- the project's start point

```json
{
  "id": "global.paleolithic.lomekwian",
  "kind": "period",
  "name": "Lomekwian Industry",
  "parent_id": "global.paleolithic",
  "start_year": -3298051,
  "end_year": -2598051,
  "tier": "specialist",
  "start_year_min": -3438051,
  "start_year_max": -3308051,
  "start_dating_method": "argon-argon",
  "standing": "consensus",
  "date_note": "Named from Lomekwi 3. Kept separate from the Oldowan because the knapping technique differs, which is also why the Oldowan's 2.6 Ma start is a definitional boundary rather than the start of toolmaking.",
  "source_ids": [
    "harmand-2015-lomekwi",
    "dominguez-rodrigo-2016-lomekwi"
  ],
  "summary": "The oldest known stone toolkit: large, heavy cores and flakes struck with techniques unlike the later Oldowan.",
  "date_precision": "approx",
  "end_dating_method": "argon-argon",
  "_sources_resolved": []
}
```

### Oldowan Industry — long-running industry, typological dating

```json
{
  "id": "global.paleolithic.oldowan",
  "kind": "period",
  "name": "Oldowan Industry",
  "parent_id": "global.paleolithic",
  "start_year": -2598051,
  "end_year": -1698051,
  "tier": "foundational",
  "start_year_min": -2616051,
  "start_year_max": -2548051,
  "start_dating_method": "argon-argon",
  "standing": "consensus",
  "date_note": "Usually given as 2.6-1.7 Ma. Older claims exist, but the 3.3 Ma Lomekwi 3 tools are excluded by classifying them as Lomekwian, so the boundary is definitional as much as evidential.",
  "source_ids": [
    "braun-2019-bokol-dora"
  ],
  "summary": "The earliest widely recognised stone tools: sharp flakes struck from pebble cores.",
  "date_precision": "approx",
  "end_dating_method": "argon-argon",
  "_sources_resolved": []
}
```

### Homo sapiens — a taxon that is extant, so no end year

```json
{
  "id": "global.prehistory.hominins.homo-sapiens",
  "kind": "taxon",
  "name": "Homo sapiens",
  "parent_id": "global.prehistory.hominins",
  "start_year": -313051,
  "tier": "foundational",
  "start_year_min": -347051,
  "start_year_max": -279051,
  "start_dating_method": "luminescence",
  "standing": "consensus",
  "allow_outside_parent_dates": true,
  "date_note": "315 +/- 34 ka is the thermoluminescence age of heated flints with the Jebel Irhoud hominins in Morocco. Which fossils count as H. sapiens is itself part of the disagreement about the date.",
  "source_ids": [
    "hublin-2017-jebel-irhoud"
  ],
  "summary": "Our own species, first recognisable in Africa around 300,000 years ago.",
  "aliases": [
    "Anatomically modern humans"
  ],
  "date_precision": "approx",
  "_sources_resolved": []
}
```

### Dangun — legendary founder; existence contested, date traditional

```json
{
  "id": "east-asia.korea.gojoseon.dangun",
  "kind": "reign",
  "name": "Dangun",
  "parent_id": "east-asia.korea.gojoseon",
  "start_year": -2333,
  "end_year": -2240,
  "tier": "intermediate",
  "source_ids": [
    "korea-rulers-01"
  ],
  "date_precision": "traditional",
  "start_dating_method": "received",
  "end_dating_method": "received",
  "standing": "traditional",
  "caveats": [
    {
      "kind": "contested-existence",
      "text": "Mythological founding figure; no archaeological or contemporaneous evidence he existed, and the 2333 BCE date derives from a 15th-century CE reinterpretation of the 13th-century Samguk Yusa legend.",
      "source_ids": [
        "korea-rulers-01"
      ]
    }
  ],
  "date_note": "traditional: not an archaeological date; Britannica gives only the accession year (2333 BC) and no end date, so the -2240 end year here follows Wikipedia's traditional regnal-length convention, not an independently attested figure",
  "summary": "Legendary grandson of the god of heaven; traditional founder of Gojoseon, Korea's first kingdom, at Asadal.",
  "aliases": [
    "Tangun",
    "Dangun Wanggeom",
    "Tan'gun Wanggŏm"
  ],
  "native_name": "단군",
  "_sources_resolved": []
}
```

### Fuxi — mythic culture hero recorded as tradition, not finding

```json
{
  "id": "east-asia.china.legendary.fuxi",
  "kind": "reign",
  "name": "Fuxi",
  "parent_id": "east-asia.china.legendary",
  "start_year": -2852,
  "end_year": -2697,
  "tier": "intermediate",
  "date_precision": "traditional",
  "start_dating_method": "received",
  "end_dating_method": "received",
  "standing": "traditional",
  "source_ids": [
    "berkshire-three-sovereigns",
    "nwe-three-sovereigns"
  ],
  "date_note": "The tradition assigns the Three Sovereigns no usable regnal years — one account gives the Heavenly Sovereign a reign of 18,000 years — so these bounds mark the window before the Yellow Emperor rather than a reign length.",
  "caveats": [
    {
      "kind": "contested-existence",
      "text": "A mythological figure, described in the sources as a god-king or demigod rather than a ruler with a reign.",
      "source_ids": [
        "nwe-three-sovereigns"
      ]
    }
  ],
  "summary": "Credited in the tradition with writing, divination and the trigrams, and with Nüwa the creation of humanity.",
  "aliases": [
    "Fu Hsi",
    "Paoxi"
  ],
  "native_name": "伏羲",
  "_sources_resolved": []
}
```

### Axial Age — dynasty whose historicity is itself disputed

```json
{
  "id": "global.classical-antiquity.axial-age",
  "kind": "era",
  "name": "Axial Age",
  "parent_id": "global.classical-antiquity",
  "start_year": -800,
  "end_year": -200,
  "tier": "intermediate",
  "summary": "Concurrent religious and philosophical revolutions: Buddha, Confucius, Zoroaster, Hebrew prophets, Greek philosophers.",
  "date_precision": "approx"
}
```

### Erlitou — archaeological site attached to a disputed dynasty

```json
{
  "id": "east-asia.china.legendary.erlitou",
  "kind": "period",
  "name": "Erlitou",
  "parent_id": "east-asia.china.xia",
  "start_year": -1750,
  "end_year": -1520,
  "tier": "foundational",
  "start_dating_method": "radiocarbon-calibrated",
  "end_dating_method": "radiocarbon-calibrated",
  "standing": "majority",
  "date_precision": "century",
  "date_note": "Wiggle-matched radiocarbon compresses the occupation to roughly 1750-1520 BCE, about two centuries. The date has moved repeatedly: broadly 2100-1300 BC on 20th-century radiocarbon, 1880-1520 BC from the Xia-Shang-Zhou Chronology Project, about 1900-1500 BC in the general literature, and later still after Wu Xiaohong's 2007 work on lower-layer samples. There is also a middle position: Liu Li and Chen Xingcan read phase II as state-level organisation but prefer the neutral label 'the Erlitou State', on the grounds that Chinese scholarship has spent too much effort on dynastic labelling and too little on craft production and settlement patterns. These are the 2007 accelerator-mass-spectrometry figures. Earlier radiocarbon work gave c.1900-1500 BCE and Britannica still prints 1900-1350. The redating matters for the Xia question in the opposite direction to the one usually assumed: it pushes Erlitou later, so the site was still developing when the Xia is conventionally said to have ended, which makes identifying the two harder.",
  "alternatives": [
    {
      "label": "Erlitou is the Xia dynasty",
      "standing": "minority",
      "note": "Held by most Chinese scholars and some overseas. The Chronology Project assigned all four Erlitou phases to Xia and dated Xia's start to c. 2070 BCE.",
      "source_ids": [
        "chen-chun-erlitou-xia-dispute",
        "li-liu-2009-xia-erlitou-debate"
      ]
    }
  ],
  "caveats": [
    {
      "kind": "contested-existence",
      "text": "Most overseas scholars hold that Erlitou cannot be identified as Xia without contemporaneous writing. Shang oracle bones show no sign of a Xia concept; the name first appears in Zhou texts.",
      "source_ids": [
        "chen-chun-erlitou-xia-dispute",
        "li-liu-2009-xia-erlitou-debate"
      ]
    },
    {
      "kind": "contested-existence",
      "text": "Chinese archaeologists generally read Erlitou as the Xia's material remains. No contemporary writing confirms it — the earliest Chinese script is late Shang.",
      "source_ids": [
        "wikipedia-erlitou-culture",
        "britannica-erlitou-culture"
      ]
    }
  ],
  "allow_outside_parent_dates": true,
  "as_of": "2026-08-08",
  "source_ids": [
    "britannica-erlitou-culture",
    "chen-chun-erlitou-xia-dispute",
    "escholarship-erlitou-wiggle-match",
    "lawler-science-founding-dynasty",
    "li-liu-2009-xia-erlitou-debate",
    "radiocarbon-erlitou-dating"
  ],
  "summary": "A large early Bronze Age centre in Henan with palace foundations and bronze workshops, and the site the entire Xia argument is actually about.",
  "_sources_resolved": []
}
```

### Qajar Dynasty — reign whose start date sources disagree on

```json
{
  "id": "west-asia.iran.qajar",
  "kind": "era",
  "name": "Qajar Dynasty",
  "parent_id": "west-asia.iran",
  "start_year": 1794,
  "end_year": 1925,
  "tier": "foundational",
  "date_precision": "approx",
  "source_ids": [
    "src-west-asia-iran-qajar"
  ],
  "alternatives": [
    {
      "label": "From the start of Agha Mohammad Khan's unification campaign",
      "standing": "minority",
      "start_year": 1789,
      "end_year": 1925,
      "note": "The date this dataset used before it was sourced.",
      "source_ids": [
        "src-west-asia-iran-qajar"
      ]
    },
    {
      "label": "From Agha Mohammad Khan's coronation as shah",
      "standing": "minority",
      "start_year": 1796,
      "end_year": 1925,
      "source_ids": [
        "src-west-asia-iran-qajar"
      ]
    }
  ],
  "date_note": "Britannica dates the dynasty from 1794, when Agha Mohammad Khan eliminated his last rival. 1789 (campaign) and 1796 (coronation) are also used.",
  "summary": "The dynasty that lost the Caucasus to Russia, granted the concessions that made Iran a field of Anglo-Russian competition, and was forced into a constitution in 1906.",
  "_sources_resolved": []
}
```

### Marcus Aurelius — co-rule, needs a link not a date trick

```json
{
  "id": "europe.mediterranean.rome.empire.marcus-aurelius",
  "kind": "reign",
  "name": "Marcus Aurelius",
  "parent_id": "europe.mediterranean.rome.empire.nerva-antonine",
  "start_year": 161,
  "end_year": 180,
  "tier": "foundational",
  "date_precision": "approx",
  "links": [
    {
      "type": "co_ruler_with",
      "entity_id": "europe.mediterranean.rome.empire.lucius-verus",
      "note": "Insisted his adoptive brother be made coemperor, creating the first joint rule in Roman history."
    }
  ],
  "source_ids": [
    "britannica-marcus-aurelius",
    "oup-lucius-verus"
  ],
  "summary": "Philosopher-emperor and author of the Meditations.",
  "_sources_resolved": []
}
```

### Munmu of Silla — one person folded across two polities

```json
{
  "id": "east-asia.korea.three-kingdoms.munmu-of-silla",
  "kind": "reign",
  "name": "Munmu of Silla",
  "parent_id": "east-asia.korea.three-kingdoms",
  "start_year": 661,
  "end_year": 681,
  "tier": "intermediate",
  "source_ids": [
    "korea-rulers-07"
  ],
  "date_precision": "exact",
  "cross_parent_ids": [
    "east-asia.korea.unified-silla"
  ],
  "allow_outside_parent_dates": true,
  "date_note": "One reign spanning 2 periods in this dataset (three-kingdoms 661-668, unified-silla 668-681), authored once and reachable from both.",
  "summary": "30th king of Silla; completed the conquest of Goguryeo and Baekje, ending the Three Kingdoms period, before ruling on into Unified Silla.",
  "aliases": [
    "Kim Beopmin",
    "Kim Pommin"
  ],
  "native_name": "문무왕",
  "_sources_resolved": []
}
```

### Byblos — city currently mis-kinded as era; inhabited today

```json
{
  "id": "west-asia.mesopotamia.phoenicia.byblos",
  "kind": "era",
  "name": "Byblos",
  "parent_id": "west-asia.mesopotamia.phoenicia",
  "start_year": -3000,
  "end_year": -332,
  "tier": "foundational",
  "date_note": "Occupied far earlier than the Phoenician period proper; the start marks its Egyptian trade rather than a founding.",
  "source_ids": [
    "britannica-byblos"
  ],
  "date_precision": "approx",
  "allow_outside_parent_dates": true,
  "summary": "The oldest of the cities and the earliest to dominate, trading cedar with Egypt from the third millennium.",
  "native_name": "𐤂𐤁𐤋",
  "_sources_resolved": []
}
```

### Tenochtitlan — city mis-kinded as period; destroyed 1521

```json
{
  "id": "americas.mesoamerica.aztec.tenochtitlan",
  "kind": "period",
  "name": "Tenochtitlan",
  "parent_id": "americas.mesoamerica.aztec",
  "start_year": 1325,
  "end_year": 1521,
  "tier": "foundational",
  "start_dating_method": "calendar",
  "end_dating_method": "calendar",
  "standing": "majority",
  "date_precision": "year",
  "date_note": "1325 is the traditional founding date. The city fell on 13 August 1521. It predates the Triple Alliance by a century: the capital is older than the empire it came to head.",
  "allow_outside_parent_dates": true,
  "caveats": [
    {
      "kind": "misconception",
      "text": "1325 is a traditional date from Mexica accounts, not an archaeological one.",
      "source_ids": [
        "britannica-tenochtitlan"
      ]
    }
  ],
  "source_ids": [
    "britannica-tenochtitlan"
  ],
  "summary": "The island capital of the Mexica, and one of the largest cities in the world when Cortés reached it.",
  "native_name": "Mēxihco-Tenōchtitlan",
  "_sources_resolved": []
}
```

### Apollo 11 Moon Landing — dated to the day

```json
{
  "id": "global.short-20c.moon-landing",
  "kind": "event",
  "name": "Apollo 11 Moon Landing",
  "parent_id": "global.short-20c.cold-war",
  "start_year": 1969,
  "end_year": 1969,
  "tier": "foundational",
  "summary": "Neil Armstrong and Buzz Aldrin became the first humans to walk on the Moon (20 July 1969).",
  "date_precision": "approx"
}
```

### Axial Age — empty container; a thesis rather than a period

```json
{
  "id": "global.classical-antiquity.axial-age",
  "kind": "era",
  "name": "Axial Age",
  "parent_id": "global.classical-antiquity",
  "start_year": -800,
  "end_year": -200,
  "tier": "intermediate",
  "summary": "Concurrent religious and philosophical revolutions: Buddha, Confucius, Zoroaster, Hebrew prophets, Greek philosophers.",
  "date_precision": "approx"
}
```

### Iron Age — European periodisation applied globally

```json
{
  "id": "global.iron-age",
  "kind": "era",
  "name": "Iron Age",
  "parent_id": "global",
  "start_year": -1200,
  "end_year": -550,
  "tier": "foundational",
  "date_precision": "approx",
  "date_note": "Thomsen devised the Stone/Bronze/Iron scheme in 1837 to order northern European material. Connah's verdict on exporting it: applying it to African archaeology 'produced little more than confusion, whereas in the Americas or Australasia it has been irrelevant'.",
  "caveats": [
    {
      "kind": "naming-confusion",
      "text": "A northern European scheme applied worldwide. It has little utility for sub-Saharan Africa, much of Asia and the Americas, where specialists largely do not use it.",
      "source_ids": [
        "naser-brill-middle-nile-three-age",
        "spafa-three-age-southeast-asia"
      ]
    }
  ],
  "source_ids": [
    "naser-brill-middle-nile-three-age",
    "spafa-three-age-southeast-asia"
  ],
  "summary": "Widespread adoption of iron for weapons and tools; the age of classical antiquity's origins.",
  "_sources_resolved": []
}
```

### Late Bronze Age Collapse — systems event sharing a placeholder date with 9 others

```json
{
  "id": "global.bronze-age.collapse",
  "kind": "event",
  "name": "Late Bronze Age Collapse",
  "parent_id": "global.bronze-age",
  "start_year": -1200,
  "end_year": -1150,
  "tier": "intermediate",
  "start_year_min": -1220,
  "start_year_max": -1180,
  "end_year_min": -1150,
  "end_year_max": -1100,
  "start_precision": "approx",
  "end_precision": "approx",
  "aliases": [
    "Bronze Age Collapse"
  ],
  "summary": "Systemic collapse of Mediterranean and Near Eastern civilizations c. 1200 BCE.",
  "allow_outside_parent_dates": true
}
```

> Not found in the dataset, which is itself a finding: Chernobyl


## The open issues, distilled

Grouped by what they're really about, since many are symptoms of the same few causes.

**Coverage is uneven in ways the entity count hides.** 1,765 entities look substantial, but
East Asia's 518 is roughly half bare Japanese era-labels (`Kōhō [period] 964..968`) with
zero emperors among its 42 reigns (#32). Africa's 271 is mostly Egypt — 143 of the
continent's 152 reigns are Egyptian, leaving six named rulers for everywhere else, and
Central Africa is four entities with none (#31). West Asia, where cities and writing began,
carries 19 reigns: one Assyrian king, zero Hittites, no Rashidun caliphs (#30). Reigns by
region: East Asia 182, South Asia 159, Europe 155, Africa 152, West Asia 19, Americas 8,
Southeast Asia 3, Oceania 2 (#27). Europe still lacks the Papacy entirely, the Crusades,
the Huns, Poland, Hungary, Bohemia, Armenia, Al-Andalus (#38). 1,491 enumerated cities await
authoring (#29). Languages and proto-language families have no kind and no entities (#20).

**Whole categories of history are absent, not merely thin.** No religion exists as an entity
— the `Axial Age` node is empty. No trade or economic institution: no Silk Road, no Indian
Ocean network, and `grep -i slave` returns one hit while two Dutch West India Companies are
present. No law or governance concept: Hammurabi without his code, Justinian without the
Corpus (#34). The `threshold` kind stops dead at 1650 BCE, so there is no iron, alphabet,
printing, gunpowder, zero, or steam engine; of 43 events total, 14 are battles, and
500–1300 CE contains effectively one (#35). 26 of 690 reigns are women (#33).

**The dataset is 39% individual reigns**, which structurally cannot represent societies
without kings — pastoralists, confederacies, stateless peoples, maritime networks. 190+
containers are empty, which the audit reads as tracking king-list availability rather than
history (#37).

**Dating has real defects.** The BP→BCE conversion runs on a 1951 epoch for 145 entities and
a 1950 epoch for three, with two entities mixing both internally; `4098050BC` asserts
year-level precision on a four-million-year-old date; and `1200BC` starts ten unrelated
entities, manufacturing a synchrony that isn't there (#36). 70+ entities carry dates
contradicting their parent's (#37). Contested dates surfaced during sourcing remain
unresolved (#26).

**Sourcing is thin and deliberately so.** 298 of 451 foundational entities show an unsourced
date (#2), and the standing editorial policy is that a real thing is included with no source
rather than omitted, with citation deferred (#28). Treat missing citations as intended
state, not as an error.

**Naming and identity are unreliable, and this is the group with the most evidence behind
it.** Every item here is a mistake actually made while authoring, or a defect found by chasing
a user's bug report; the full write-up is in `consult-addendum-naming.md`.

Ids are not derivable from names and the convention varies within a single dynasty —
`Thutmose III` is `thutmose3` while Thutmose I, II and IV are `thutmose-i`, `thutmose-ii`,
`thutmose-iv`. **128 entities have an id path that contradicts their own `parent_id`**: ids
look like paths and authors read them as paths, but `global.paleolithic` is parented to
`global.prehistory`, and Roman emperors keep flat ids under `...rome.empire` while being
filed under dynasties. Some divergence is deliberate; at 128 instances nobody can tell the
deliberate cases from the accidental ones — and one was accidental, the Roman Empire being
parented to `europe.mediterranean` so that no emperor's ancestor chain passed through a node
named "Rome", which is why a user reported that searching "Rome" returned no Roman rulers.

**Display names are not unique: 15 collisions today** — Shōwa, Jōwa, Jōgen, Eishō, Kōwa,
Tenshō, Kōji, Jōō, Kōan and Enkyō each appear twice as distinct Japanese eras separable only
by `native_name`; Emperor Taizong, Gaozong and Shun each name two different men; and
`Mesoamerica` and `Andes` are each reused at two points in the region tree. Any handle keyed
on the display name collides on day one.

Regnal numbering defeats name-based duplicate detection — `thutmose` matches four people,
`ptolemy` four, `ramesses` four — and name-only matching also produces false positives across
unrelated people (Romulus against Romulus Augustulus, Tiberius Gracchus against the emperor
Tiberius). Two duplicate people were authored before a validator rule existed (#37 area).

`name_forms` has eight kinds in use (`common` 60, `scholarly` 46, `endonym` 36, `historical`
34, `exonym` 31, `formal` 24, `translation` 10, `rejected` 4) but cannot express the plainest
case of all: **"Rome" and "Roman" are the same referent in different grammatical forms.** Nor
can it hold orthographic variants (#4) or a second romanisation system alongside Wade-Giles
(#3). Multilingual architecture remains unresolved (#10).

Filing depth is unpredictable from the authoring side, not just the reader's: twice this
session an author concluded a container was empty and began authoring into it when the
entities sat one level deeper — Julius Caesar is under `...rome.republic.late`, not
`...rome.republic` (#17).

**Presentation and structure debt.** Entities are filed at inconsistent depths between
branches (#17); `researchNote` is exported and tested but wired to no control (#6);
`name_forms` has no kind for orthographic variants (#4); postal romanisation is absent (#3);
multilingual architecture is unresolved (#10); 15 foundational entities have no summary
(#12); `build_data.py` holds 3,280 lines of un-extracted inline data (#8).
