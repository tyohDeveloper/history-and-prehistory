# Brief: schema and coverage consultation

You are reviewing the data model of a working application, not designing one from scratch.
Read `/home/user/workspace/hp/docs/consult-pack.md` in full before answering. It contains
the 33-field entity schema, every controlled vocabulary, a table of how often each field is
actually populated, seventeen real records chosen because each strains the model in a
different direction, and the 24 open issues distilled.

Also read `/home/user/workspace/hp/docs/inventory.txt` — all 1,765 entities as an indented
tree — and cross-check anything you assert about coverage against it.

**Do not search the web.** Work from your own knowledge and from the pack.

---

## What the application is

A comprehensive timeline of humanity. It begins at the earliest hominin tool use — stone
knapping at Lomekwi, 3.3 million years ago — and runs to the present. Between those points
it aims to hold:

hominin species and the close relatives of *Homo sapiens*; proto-language families and
actual languages; foraging, agriculture, and animal domestication; lithic and metal
technology; religions; regions and cities; polities, empires, kingdoms; dynasties;
political and military rulers; major technological shifts; and events.

Its governing intellectual commitment is that **dating is fuzzy until it isn't**. A date
3.3 million years old, a date from a king list, and a date from a dated inscription are
three different kinds of claim, and the application is supposed to say which is which rather
than presenting them all as numbers on one line.

For each topic it wants to record, and this is the user's own formulation:

- the topic name
- a short description of the **accuracy and precision** of its dates
- the degree of **certainty, consensus, or controversy** — about the topic itself, and
  separately about its dating
- **how the dates were established**
- a sentence to a paragraph about the topic
- a **searchable key phrase** so a reader can go research further
- the **hierarchy of contexts** it sits in
- important **before-and-after links**, expressed via those key phrases

Scholarly citations are deliberately **out of scope**. Sourcing will be done later as a
single pass across the whole dataset, once its shape and coverage are settled.

---

## The questions

Most of that list already has a field. The pack shows you which. What we want from you is
judgement about the model as it actually stands, not a redesign of what works.

Address these directly:

**1. `date_precision: approx` is used on 1,493 of 1,765 entities, while
`start_year_min`/`start_year_max` are populated on 26.** So the dataset says "approximately"
1,493 times and quantifies the approximation 26 times. That single bucket is spanning
±50 years on the Bronze Age collapse and ±200,000 years on a hominin species. Is the fix a
finer enum, mandatory bounds whenever precision is `approx`, an order-of-magnitude field, or
something else? This is the question we most want answered.

**2. `start_precision` is populated 8 times and `end_precision` 22, while whole-entity
`date_precision` carries 1,743.** The per-endpoint fields are effectively dead, so an entity
with a precisely known beginning and a vague end cannot express that in practice. Should the
whole-entity field be retired in favour of per-endpoint ones, or the reverse?

**3. Two axes of uncertainty are currently collapsed into one.** `standing`
(consensus/majority/minority/traditional/superseded) grades the *dating*. Whether the topic
itself is real or coherent is captured only by a prose `caveats` entry of kind
`contested-existence`. But these vary independently: Dangun's existence is contested and his
date is traditional; the Lomekwian industry is not in doubt while its 3.3 Ma date is
genuinely debated; a Sumerian King List reign may be a legendary person with fictional
numbers. Propose how to grade the topic axis.

**4. There is no field for the searchable key phrase.** Note that the user wants
before-and-after links keyed on these phrases, which makes the phrase an identifier as well
as a search string — it must be unique and stable. We already have stable ids. Should the
key phrase be a separate authored field, derived, or something else?

**5. There is no kind for languages.** Existing kinds: `region`, `era`, `period`, `reign`,
`event`, `city`, `taxon`, `threshold`. A proto-language family is not a period, a polity, or
a species; it is reconstructed rather than attested, its dates come from glottochronology and
archaeology rather than excavation, and it stands in a descent relation to its daughters.
Propose how languages are modelled, including their dating methods and their relation to the
existing `links` vocabulary.

**6. Fields that are effectively dead:** `capital` (1 use), `notable_figures` (1), `links`
(15 of 1,765), `regions` (98), `cross_parent_ids` (48). `superseded` and `potassium-argon`
are in enums and never used. Say which of these should be removed, which are worth
populating, and which indicate a missing feature rather than a dead field. Note especially
that `links` at 15 uses means the before-and-after graph the user is asking for barely
exists yet.

**7. The `threshold` kind stops at 1650 BCE and `event` is 14 battles out of 43.** Both were
built for prehistory and never widened. Should `threshold` cover the alphabet, printing,
gunpowder and the transistor, or does the post-3000-BCE world need different kinds?

**8. 39% of entities are individual reigns**, and 190+ containers are empty. Societies
without kings — pastoralists, confederacies, stateless peoples, maritime trade networks —
have no natural representation. Propose what kinds or structures they need.

Where the current model is adequate, say so plainly and briefly. A short list of real
problems is worth more than a long list of refinements.

---

## Output

Write `/home/user/workspace/hp/docs/consult-response-schema.md`: a clear recommendation on
each of the eight numbered questions, then a summary of the changes you would make ordered
by value, and finally the **field-by-field specification** of your proposal — enough that
someone can author entities against it without asking you a follow-up question. Name the
new fields, give their types and controlled vocabularies, and say which existing fields you
are retiring, renaming, or leaving alone.

A second agent will author a worked exemplar set against your specification, so it needs to
be unambiguous. Call out anywhere you deliberately left a judgement to the author.

If your recommendations conflict with anything in the distilled issues, say so explicitly
rather than quietly working around it.

Do not propose citation or sourcing fields beyond the `source_ids` that already exist.
Sourcing is a later, separate pass.
