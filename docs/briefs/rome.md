# Brief: Roman Kingdom and Republic

Read `/home/user/workspace/hp/docs/briefs/COMMON.md` first — it defines the output format
and rules. Write to `/home/user/workspace/hp/docs/research/rome.json`.

## Part 1: the seven kings of Rome (753–509 BCE)

All seven, in order, with traditional regnal dates: Romulus, Numa Pompilius, Tullus
Hostilius, Ancus Marcius, Lucius Tarquinius Priscus, Servius Tullius, Lucius Tarquinius
Superbus.

**These are traditional, not attested.** Set `date_precision: "traditional"` on all seven
and give every one a `contested` note. The regnal list comes from Livy and Dionysius
writing centuries later; the early kings especially are legendary, and modern scholarship
treats the whole sequence with suspicion — note if your source says the reign lengths look
schematic or implausibly long. If a source distinguishes the more plausible later kings
(the Etruscan ones) from the legendary early ones, capture that.

## Part 2: notable figures of the Republic (509–27 BCE)

**Do NOT attempt a consul list.** Paired annual consuls over 500 years is ~1,000 people
and useless to a reader. Instead give **12–16 figures who changed the Republic's course**,
with the years of their significant office or command rather than a lifespan — and say
which you used in `date_agreement`.

Suggested spine, adjust with judgement: Scipio Africanus, Tiberius Gracchus, Gaius
Gracchus, Gaius Marius, Sulla, Pompey, Crassus, Cicero, Julius Caesar, Cato the Younger,
Mark Antony, Octavian (to 27 BCE only — the Empire is already in the dataset).

For each, `summary` must say what they changed, not who they were. "Held the consulship
seven times and opened the legions to the landless, making armies loyal to commanders
rather than the state" beats "a Roman general and statesman".

Add a `"role"` field to each Republic object: `"consul"`, `"dictator"`, `"tribune"`,
`"general"`, `"orator"` — whatever fits. These are not monarchs and the dataset should not
imply they were.
