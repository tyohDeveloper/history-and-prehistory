# Brief: review the data for correctness

**Do not search the web.** Work from your own knowledge. This is a judgement pass, not a
verification pass — verification happens later as a single sourcing sweep. What is wanted here is
your reaction as someone who knows the material: **which of these entries is wrong?**

## Why this brief exists

Every automated guard in this project checks structure and consistency, and none of them knows
whether a claim is true. Three things shipped as a result, each structurally valid and factually
absurd:

- The Fall of the Berlin Wall, an event dated to the evening of 9 November 1989, carried an
  uncertainty of plus-or-minus a century and displayed as "66 – 65 BP".
- The September 11 attacks were renamed `september-xi`, because a rule for regnal numerals read
  the 11 as one.
- Eleven entities including Cicero and Pompey carried a caveat whose entire text was the word
  "omit", telling readers their existence was in doubt.

In every case the only thing that caught it was a person glancing at one entry. You are that person,
at scale.

## What to look for

Ranked by how badly it misleads a reader:

1. **Dates that are simply wrong.** A reign in the wrong century, a city founded after it was
   abandoned, a polity outliving its own empire, an event off by decades.
2. **Uncertainty that is wrong in either direction.** Plus-or-minus a century on a date known to the
   day, or no bounds at all on a date nobody can place within a millennium.
3. **Implausible spans.** A ruler reigning 70 years in a period where 20 was long, a dynasty whose
   reigns cannot fit inside it, a city whose founding predates agriculture in its region.
4. **Wrong `dated_by`.** `calendar` on something known only from archaeology, `typological` on a
   dated inscription, `received` on a measured date.
5. **Wrong `historicity`.** Something legendary presented as accepted, or a well-attested figure
   marked contested. Absent means accepted.
6. **Summaries that overstate.** A claim the evidence will not carry, a contested reading given as
   settled, or a summary that is simply inaccurate.
7. **Wrong placement.** `under` shows the ancestry. An entity filed beneath something it never
   belonged to, or filed in one place when a reader would look in another.
8. **Missing obvious alternate names.** The name a reader is most likely to arrive with.

## What NOT to report

- **Missing citations.** Roughly three quarters of entities are unsourced by policy; `sourced` is
  shown only as context.
- **Missing entities.** Coverage gaps are tracked separately. Report a wrong entry, not an absent one
  — with one exception: if a row's existence only makes sense alongside something absent (a dynasty
  with no rulers, a war with no participants), say so.
- **Style, wording preferences, or British-versus-American spelling.**

## Output

Write markdown to the path in your objective. One entry per finding:

```
### <id>
**Field:** which field is wrong
**Currently:** what it says
**Should be:** what it should say, or "unclear — here is the problem"
**Confidence:** high | medium | low — your certainty that the current value is WRONG
**Why:** one or two sentences
```

Then a final section `## The twenty worst`, ordered by how badly each misleads.

**Rank by confidence and be honest about it.** A hundred findings you are sure of beats a thousand
that might be quibbles. If a value is defensible but you would have chosen differently, either skip
it or mark it `low`. If a whole class of entries looks systematically off — all the dates in one
region, every entry of one kind — say that once as a pattern rather than a hundred times.
