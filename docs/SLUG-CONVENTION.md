# Id and slug convention

An id is the only identifier in this dataset. Links key on it, the redirect map preserves it,
and nothing else -- not the display name, not a search phrase -- is unique enough to do the
job. Display names collide fifteen times as it is, including two different places called
Andes.

This document exists because ids were being guessed. Within a single dynasty, Thutmose III
lived at `thutmose3` while Thutmose I, II and IV lived at `thutmose-i`, `thutmose-ii` and
`thutmose-iv`. An author reasoning from one to the others was right three times in four with
no way to know which time was the exception.

## Rules

1. **Lowercase ASCII, hyphen-separated.** `later-le`, not `Later_Lê`.
2. **Diacritics stripped**, not transliterated into digraphs: `le` for Lê, `showa` for Shōwa.
   Where stripping produces a collision, disambiguate with a qualifier rather than by
   reintroducing the diacritic -- see rule 7.
3. **Regnal numbers are Roman numerals**, spelled in ASCII letters and hyphen-separated:
   `thutmose-iii`, `ramesses-ii`, `cleopatra-vii`. **Never Arabic digits.** This is the rule
   the dataset most often broke.
4. **Generic type words are dropped.** `later-le`, not `later-le-dynasty`; `tang`, not
   `tang-dynasty`. The `kind` field already says what it is.
5. **Epithets are dropped unless they disambiguate.** `ptolemy-i`, not `ptolemy-i-soter`,
   because the numeral is sufficient. Keep the epithet where two rulers share a name and a
   numeral.
6. **A slug is unique among its siblings.** It need not be globally unique; the full dotted id
   provides that.
7. **Disambiguate with the shortest sufficient qualifier**, placed last: `taizong-tang`
   against `taizong-song`.

## Prefixes are mnemonic, not structural

**Nothing may parse an id as a path.** An id's dotted prefix is a human-readable hint about
where the entity usually sits, and it is allowed to disagree with `parent_id`. 128 entities
currently do disagree.

Most of that is deliberate. Roman emperors carry flat ids under `...rome.empire` while their
`parent_id` points at whichever dynasty they belong to, so that refiling an emperor between
dynasties -- a live scholarly question for several of them -- does not change his identity.
The prehistory branch does something similar.

But because the divergence is normal, an accidental case is invisible among the deliberate
ones, and one such case shipped: `europe.mediterranean.rome.empire` had `parent_id:
europe.mediterranean`, which made the Roman Empire a sibling of Ancient Rome rather than a
part of it. No ancestor chain from any emperor passed through a node named "Rome", so
searching "Rome" returned no Roman rulers, and a user reported it. The id had said
`rome.empire` the whole time.

Hence: read `parent_id` for structure, always. Read the id as a label.

## Ids are frozen

After the one-time normalisation, **an id is never changed and never reused.** Refiling an
entity changes its `parent_id`, not its id.

When a rename is genuinely unavoidable, the old id is written to `redirects` in the build
output and resolved forever. Redirect entries are not cleaned up: the cost of keeping one is a
line in a map, and the cost of dropping one is a link that silently resolves to nothing.

## Naming a thing versus identifying it

Three fields carry names and they are not interchangeable:

- **`name`** is for display. No two siblings may share one. Where the same name appears at
  different points in the tree -- ten Japanese era names do, and so do Emperor Taizong,
  Emperor Gaozong and Emperor Shun -- out-of-context display uses a **qualified name**
  derived from the parent and dates. It is computed, never authored.
- **`name_forms`** holds the variants a reader might arrive with: `common`, `formal`,
  `historical`, `endonym`, `exonym`, `scholarly`, `translation`, `rejected`, and now
  **`adjectival`** ("Roman" for Rome, "Ptolemaic" for the Ptolemies) and **`orthographic`**.
  Entries may carry a `system` naming a romanisation (`pinyin`, `wade-giles`, `postal`,
  `hepburn`, `mccune-reischauer`).
- **`search_phrase`** is a search aid only. Not unique, not an identifier, never a link
  target.

The `adjectival` kind is not cosmetic. "Rome" and "Roman" are the same referent in different
grammatical forms, and having nowhere to say so was half the reason searching "Rome" missed
the Roman Empire entirely.
