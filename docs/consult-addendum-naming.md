# Addendum: naming and identity failures observed in practice

This is evidence rather than theory. Every item below is a mistake actually made while
authoring this dataset, or a defect found by chasing a user's bug report. They bear directly
on question 4 (the key phrase as identifier) and on the naming issues #3, #4 and #10.

The general shape of the problem: **an author cannot predict where a thing lives or what it
is called, so they guess, and the guess is wrong in a way nothing catches.**

## 1. Ids are not derivable from names, and the convention varies within one dynasty

```
'Thutmose III'  ->  africa.nile.egypt.new-kingdom.dyn18.thutmose3
'Thutmose I'    ->  africa.nile.egypt.new-kingdom.dyn18.thutmose-i
'Thutmose II'   ->  africa.nile.egypt.new-kingdom.dyn18.thutmose-ii
'Thutmose IV'   ->  africa.nile.egypt.new-kingdom.dyn18.thutmose-iv
```

One Arabic numeral among three Roman. Four siblings, two conventions. An author who reasons
"Thutmose III becomes `thutmose-iii`" is right three times out of four and there is no way to
tell which time is the exception without looking.

Similarly `'Later Lê Dynasty'` lives at `southeast-asia.mainland.later-le` — the diacritic is
dropped and the word "dynasty" is dropped, both reasonable, neither stated.

## 2. The id path contradicts `parent_id` for 128 entities

Ids look like paths, so authors read them as paths. They are not reliable as paths:

```
global.paleolithic                        id implies: global
                                          actual parent: global.prehistory
europe.mediterranean.rome.empire.augustus id implies: europe.mediterranean.rome.empire
                                          actual parent: ...rome.empire.julio-claudian
europe.mediterranean.rome.empire.trajan   id implies: europe.mediterranean.rome.empire
                                          actual parent: ...rome.empire.nerva-antonine
```

Some of this is deliberate — Roman emperors keep flat ids while being filed under dynasties,
which is documented. But 128 instances means the reader cannot tell the deliberate cases from
the accidental ones. And one *was* accidental: `europe.mediterranean.rome.empire` itself had
`parent_id: europe.mediterranean`, so the Roman Empire was a sibling of Ancient Rome while
the Kingdom and Republic were its children. No ancestor chain from any emperor passed through
a node named "Rome", which is why a user reported that searching "Rome" returned no rulers.
The id said `rome.empire` and had said so all along.

## 3. Display names are not unique — fifteen collisions today

```
Shōwa x2, Jōwa x2, Jōgen x2, Eishō x2, Kōwa x2, Tenshō x2, Kōji x2, Jōō x2,
Kōan x2, Enkyō x2, Emperor Taizong x2, Emperor Gaozong x2, Emperor Shun x2,
Mesoamerica x2, Andes x2
```

The Japanese cases are distinct era names that romanise identically and are separable only by
`native_name`. Emperor Taizong and Gaozong are different men in different dynasties. And
`Mesoamerica` and `Andes` are the same name reused at two points in the region tree.

This matters for question 4 specifically. **A key phrase keyed on the display name would
collide fifteen times on day one**, and the before-and-after links the user wants would
resolve ambiguously or silently pick the wrong target.

## 4. Regnal numbering defeats name-based duplicate detection

A validator rule was added to stop duplicate people being authored, matching on token subset
plus overlapping dates plus shared region. Regnal numbering makes this fragile:

```
'thutmose'   -> Thutmose I, II, III, IV
'ramesses'   -> Ramesses I, II, III, IV
'ptolemy'    -> Ptolemy I Soter, II Philadelphus, III Euergetes, IV Philopator
'mentuhotep' -> Mentuhotep II, III, IV
'amenhotep'  -> Amenhotep I, II, III
'tokugawa'   -> Ieyasu, Hidetada, Iemitsu, Ietsuna
```

Name alone also produces false matches across unrelated people — Romulus against Romulus
Augustulus, Tiberius Gracchus against the emperor Tiberius. Two duplicate people were in fact
authored during this session before the rule existed.

## 5. Grammatical and derived forms have no home

`name_forms` is populated 99 times with kinds already in use: `historical` 34, `exonym` 31,
`common` 60, `endonym` 36, `scholarly` 46, `translation` 10, `formal` 24, `rejected` 4.

What is missing is the plainest case of all. **"Rome" and "Roman" are the same referent in
different grammatical forms**, and nothing in the model can say so — which is half the reason
the search failure above was possible. Neither can it hold orthographic variants (issue #4)
or a second romanisation system such as postal alongside Wade-Giles (issue #3).

## 6. Filing depth is unpredictable, so authors look in the wrong place

Twice this session an author concluded a container was empty and began authoring into it,
when the entities were one level deeper. Julius Caesar sits under
`europe.mediterranean.rome.republic.late`, not under `...republic`. King Sejong was similarly
missed. Both near-misses would have created duplicates. This is issue #17 seen from the
authoring side rather than the reader's.

## What we would like you to take from this

Question 4 is not really "should there be a key-phrase field." It is: **what is the stable,
unique, human-legible handle for a topic**, given that ids are unpredictable and contradict
their own paths 128 times, and display names collide 15 times? The user wants before-and-after
links expressed in those handles, so whatever you propose has to survive Shōwa, Thutmose III,
and two different places called Andes.

If your answer to question 5 (languages) or question 1 (the `approx` collapse) is affected by
any of this, say so.
