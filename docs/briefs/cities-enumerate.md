# Brief: enumerate cities from your own knowledge

**Do not search the web. Do not fetch pages. Do not cite URLs.** This brief exists because
web research under-enumerated badly — it returned 34 cities for the whole of world history,
missing Jericho, Çatalhöyük, Eridu, Uruk, Hattusa, Mohenjo-daro, Anyang, Caral and a
hundred others. Recall is the job here, and you are better at recall than a search engine
is at enumeration.

Verification is a **later, separate** step. Your job is coverage.

## Output

Write a JSON array to the path given in your objective. One object per city:

```json
{
  "slug": "catalhoyuk",
  "name": "Çatalhöyük",
  "aliases": ["Catalhoyuk", "Çatal Hüyük"],
  "region_hint": "west-asia",
  "start_year": -7400,
  "end_year": -6000,
  "date_precision": "approx",
  "modern_name": "Konya Province, Turkey",
  "still_inhabited": false,
  "peak": "7th millennium BCE",
  "summary": "Dense proto-urban settlement with no streets, entered through the roofs.",
  "confidence": "high"
}
```

- `region_hint`: one of `africa`, `americas`, `central-asia`, `east-asia`, `europe`,
  `oceania`, `south-asia`, `southeast-asia`, `west-asia`.
- `confidence`: `high` | `medium` | `low` — your own certainty about the **dates**, not
  about whether the place existed. Be honest; `low` is useful, silence is not.
- `summary`: one sentence, under 140 characters, on **why it matters**. Not where it is.
- `date_precision`: `approx` for nearly everything here. Use `traditional` when the only
  date is a legendary founding, and say so in a `contested` field.
- Negative years for BCE. There is no year 0.

## Rules on dates

- `start_year` = earliest substantial urban or proto-urban settlement.
- `end_year` = **null if the place is still inhabited today.** Damascus, Jerusalem, Varanasi,
  Athens and Beijing all get null. Do not write the current year.
- Conquest and renaming are **not** endings. Only genuinely abandoned sites get an end year.
- Approximate is fine and expected. Do not manufacture precision you do not have; set
  `confidence` to `medium` or `low` instead.

## What counts

Include: imperial capitals, religious centres, ports and trade entrepôts, palace complexes,
ceremonial centres, proto-urban settlements, and one-period cities that were abandoned and
never rebuilt. A place that mattered for two centuries and vanished still counts.

Do not restrict yourself to places with famous ruins or a tourist trade. Do not skip a city
because you are unsure of its dates — that is what `confidence` is for.

**Err heavily toward inclusion.** A list that is too long is trivially trimmed. A list that
is too short is invisible, and that is the failure being corrected.
