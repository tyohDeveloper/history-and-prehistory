# Overlapping polities and rival claims

## The premise was wrong, and measuring it is what showed that

The question opened with what looked like a structural gap: the dataset models
sequences of periods, but history is full of simultaneous polities, and **988 sibling
pairs have overlapping spans** with nothing distinguishing legitimate overlap from
contested sovereignty.

Examining those 988 changed the answer.

The largest overlaps are archaeological sites and stone-tool industries — Turkana
Basin against Sterkfontein, Acheulean against Middle Stone Age. Those coexist by
nature; a site does not succeed another site. Restricting to historical-era polities
still left **298 pairs overlapping by 25 years or more**, and nearly all of those are
neighbours rather than rivals:

| Pair | Overlap | What it is |
| --- | --- | --- |
| Champa / Vietnam | 893 y | Two states, adjacent, both real |
| Tyre / Sidon / Arwad | 868 y | Independent Phoenician cities |
| Ghana / Kanem–Bornu | 540 y | Different parts of the Sahel |
| Moche / Nazca | 700 y | Different Peruvian valleys |
| Mississippian / Ancestral Puebloan | 800 y | Different halves of a continent |

**Overlap is the normal condition of history.** The dataset already represents it
correctly, and marking all of it would have produced noise attached to nearly every
polity in the file. The original recommendation was to add a marker for overlap; that
recommendation was wrong, and the count that motivated it was doing no work.

## What was actually missing

Two entities claiming the **same office or sovereignty at the same time**. That is a
semantic relation, not a temporal one — no arithmetic over dates can find it, which
is why counting overlaps could never have located it. Four cases:

- **Fatimid and Abbasid** — 262 years of simultaneous, mutually exclusive claims to
  the caliphate. The four caliphates were filed as a clean succession, and because
  the Fatimids sort after the Abbasids in the column, the interface actively implied
  one followed the other.
- **Mạc and Later Lê** — a usurpation already modelled as an overlap, with nothing
  saying why the two coexisted.
- **Afsharid and Zand** — the Afsharids held Khorasan while the Zand held the rest of
  Iran, both claiming the whole.
- **Trịnh and Nguyễn** — never authored, because there was no way to express what
  they were: two lord-domains at war with each other while both claiming to serve the
  same Lê emperor. Now recorded as rivals to each other rather than as successive
  periods, since neither displaced the other — the Tây Sơn displaced both.

## The display had to come first

`links` was authored, schema-validated and covered by tests for several releases
while reaching **no part of the interface**. The Yuan has carried
`successor_state_of: central-asia.mongol-empire` that no reader could see.

That is the same defect as `researchNote` (issue #6): a field whose presence implies
a capability the app does not have. Adding `rival_claimant_to` to an unrendered field
would have produced more invisible data and called the problem solved, so relations
are rendered as of this release — with the target as a button, because a relation
naming an entity the reader cannot reach is half a relation.

## What now guards it

- **validate.py Rule 8** — no self-links, and `rival_claimant_to` must be recorded on
  both sides. Symmetry matters because a one-sided claim would make the readout depend
  on which entity the reader happened to open. Dangling targets turned out to be
  covered by an existing check already; planting one produced two error lines, so the
  duplicate was removed.
- **Four unit tests and one e2e test**, each verified by planting the regression it is
  meant to catch.
- **A hard failure on a missing anchor** in `tools/rival_claims.py`. The first version
  pointed at `southeast-asia.mainland.vietnam.later-le`, which does not exist — the
  Vietnamese dynasty ids sit at `southeast-asia.mainland.*` while their `parent_id`
  points at the container. The whole Trịnh block was skipped in silence while the
  summary line still reported the entities as authored. It now raises.

## Still open

`rival_claimant_to` is applied to four pairs. There are almost certainly more —
antipopes and rival Holy Roman claimants, the Northern and Southern Courts in Japan,
the Three Kingdoms period in China, the Sengoku claimants. Those need the same
per-case judgement rather than a sweep, and none of them can be found by measuring
date overlap.
