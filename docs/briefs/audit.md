# Brief: audit the dataset for holes

Read `/home/user/workspace/hp/docs/inventory.txt`. It is the complete dataset — 1,765
entities as an indented tree, plus counts by century, by kind, and by region.

**Do not search the web.** Work from your own knowledge of world history. Search can
confirm a fact already suspected; it cannot report what nobody thought to include. That
absence is the whole question here.

## What "a hole" means

Not "this entry could be more detailed." A hole is something a knowledgeable reader would
expect to find and cannot. Rank by how badly its absence distorts the picture.

## Output

Write markdown to the path in your objective. For each finding:

```
### <short name of the hole>
**Severity:** high | medium | low
**What is missing:** specific names — polities, people, events, concepts. Name them.
**Where it belongs:** the existing parent in the tree, quoted from inventory.txt.
**Why it matters:** one or two sentences on what a reader gets wrong without it.
**Rough dates:** approximate is fine.
```

Then finish with a section `## The five worst` — an ordered list, most damaging first.

## Rules

- **Be specific.** "More on Africa" is useless. "No Kanem-Bornu, which ran from the 9th
  century to 1900 and is the longest-lived dynasty in African history" is a finding.
- **Name names.** Every finding must list actual entities that could be authored.
- **Quote the tree.** Confirm a thing is absent before reporting it — the inventory is
  complete, so if it is not there, it is not in the dataset. Check aliases and alternate
  spellings before declaring something missing.
- **Do not pad.** Twenty real findings beat sixty speculative ones.
- **Say when coverage is genuinely fine.** A clean bill of health on some axis is
  information too.

## Known context, so you do not spend findings on it

- Cities are being added right now in a separate effort. **Do not report missing cities.**
- The dataset covers deep prehistory and geology deliberately; that is not padding.
- Roughly two thirds of entities carry no citation. That is a known, accepted state — the
  policy is to include a real thing and cite it later. **Do not report missing citations.**
- `region` nodes are grouping containers, not claims about historical polities.
