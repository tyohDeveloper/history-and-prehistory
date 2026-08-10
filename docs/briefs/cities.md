# Brief: major cities

Read `/home/user/workspace/hp/docs/briefs/COMMON.md` first for format and rules — including
the rule that you **never omit a real place for want of a citation**. Write to
`/home/user/workspace/hp/docs/research/cities.json` as a JSON array.

The dataset currently has almost no cities. **Athens, Sparta, Alexandria, Constantinople,
Carthage and Rome-the-city do not exist in it at all.** That is the gap.

## Scope: 30–36 cities

Weight toward cities that a reader would expect to find and that anchor a civilisation.
Cover every region — do not let this become a Mediterranean list.

Suggested, adjust with judgement: **Rome, Athens, Sparta, Alexandria, Constantinople,
Carthage, Jerusalem, Babylon, Ur, Uruk, Nineveh, Persepolis, Memphis, Thebes (Egypt),
Meroë, Timbuktu, Great Zimbabwe, Baghdad, Damascus, Córdoba, Samarkand, Chang'an,
Beijing, Kyoto, Nara, Gyeongju, Angkor, Pataliputra, Varanasi, Tenochtitlan, Cusco,
Cahokia, Teotihuacan, Nan Madol.**

Some already exist in the dataset as empires or sites rather than cities (Great Zimbabwe,
Teotihuacan, Tenochtitlan, Angkor). Include them anyway and note it in a `"note"` field —
a later step will reconcile rather than duplicate.

## Per-city fields

Use the COMMON.md object shape, plus:

- `"region_hint"`: one of `africa`, `americas`, `central-asia`, `east-asia`, `europe`,
  `oceania`, `south-asia`, `southeast-asia`, `west-asia`. Your best guess at where it belongs.
- `"modern_name"`: the present-day name and country if different — Constantinople →
  "Istanbul, Turkey". Null if unchanged.
- `"still_inhabited"`: `true` or `false`.
- `"peak"`: optional short phrase for when it mattered most, e.g. "5th century BCE".

## Dates: read this carefully

A city is not a period, and this is the hard part of the brief.

- `start_year` = **earliest substantial urban settlement**, as archaeology gives it, not a
  legendary founding date. If the only date available is legendary (Rome's 753 BCE), give it
  and set `date_precision: "traditional"` with a `contested` note saying so.
- `end_year` = **null if still inhabited.** Do not put the current year. Only give an end
  year for cities that were abandoned or destroyed and not reoccupied — Nineveh, Persepolis,
  Nan Madol, Cahokia.
- Being conquered is **not** an end. Constantinople does not end in 1453; it becomes
  Istanbul. Record that in `modern_name`, not by ending the city.

That distinction is the single most important thing in this brief. A city that runs from
2500 BCE to the present is normal and correct.

## Summaries

One sentence, under 140 characters, on **why the city matters** — not where it is. "Where
the assembly, the jury courts and the tragic theatre were invented" beats "an important
city in Greece".
