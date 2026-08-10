# Common brief for ruler-list research

You are filling ruler gaps in a history reference dataset. Output is consumed by a
Python authoring module, so **format matters as much as content**.

## Output format

Write a JSON array to the file named in your specific brief. One object per ruler:

```json
{
  "slug": "numa-pompilius",
  "name": "Numa Pompilius",
  "start_year": -715,
  "end_year": -673,
  "summary": "One sentence, under 140 chars, on why this person matters.",
  "aliases": ["optional", "alternate names"],
  "date_precision": "exact | approx | traditional",
  "contested": "omit unless the person's historicity is genuinely disputed; if so, one sentence under 200 chars",
  "source": {"citation": "'Page title', Publisher", "url": "https://...", "kind": "reference | institutional | scholarly"},
  "date_agreement": "matches | differs: source says X..Y | traditional: not an archaeological date"
}
```

## Rules

- **Negative years are BCE.** -715 = 715 BCE. Year 0 does not exist; do not emit it.
- **`slug`** must be lowercase ASCII, hyphenated, no diacritics: `tarquinius-superbus`.
- **Every ruler needs a `source` with a real, working URL** to a specific page. Prefer
  encyclopaedias, museums, universities. Wikipedia is acceptable where nothing better
  exists — say so in `kind` by writing `reference` and noting it.
  One shared source for the whole list is fine — repeat the same object.
- **Do not invent dates.** If a reign's dates are unknown or wildly disputed, say so in
  `date_agreement` and give the conventional figures with `date_precision: traditional`.
- **Flag legendary or semi-legendary figures** with `contested`. This dataset cares more
  about being honest that a date is traditional than about looking precise.
- Summaries: concrete and specific. "Second king of Rome; credited with founding Roman
  religious institutions" beats "an important early king".
- Keep the list to the scope named in your brief. Do not pad it.

## Do not settle for the first result

A page that surfaces in a search is worth opening. The first pass of this work sourced all
seven kings of Rome to a **single Wikipedia article**, and several Korean kings to **Simple
English Wikipedia** — while Britannica biographies of the individual kings and a World
History Encyclopedia article on Gwanggaeto were sitting in the same result sets, unopened.

Opening them changed the content, not just the citation: Britannica calls Tullus Hostilius
"a legendary figure, the legend probably influenced by that of Romulus", says Ancus
Marcius's reign "must be regarded as largely legendary", and notes the pontifical books
attributed to Numa were "clearly forgeries". None of that came through the summary table.

So: scan what the search returned, open the plausible non-Wikipedia results, and only fall
back to Wikipedia when you have actually checked and found nothing better. Say in `kind`
when you have done that.

## Verify before you write

Open the URLs you cite and confirm the dates appear there. A citation that disagrees
with the date attached to it is worse than no citation, because it looks like
verification. Report disagreements in `date_agreement` rather than smoothing them.
