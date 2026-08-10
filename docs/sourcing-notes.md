# Sourcing Notes — Disagreements and Contested Dating

This file covers only the entities from `needs-sourcing.json` where the best available
source disagreed with our stored `start_year`/`end_year`, or where the dating/label is
genuinely contested among historians. See `sourcing-results.json` for the full 29-entity
citation list.

## Special-care entities (flagged by the task)

### `east-asia.korea.gojoseon` — Gojoseon (-2333..-108)
The **-2333 start date is legendary, not archaeological.** It comes from the Dangun
foundation myth. [GlobalSecurity.org](https://www.globalsecurity.org/military/world/rok/history-gojoseon.htm)
states plainly: "Among serious historians of Korea ... the traditional founding dates of
Gojoseon at 2333 BC and the myth of Dan'gun is considered pure myth. There is no
archeological evidence and very little textual evidence to support it." The end date
(-108) is on firmer ground — it matches the Han dynasty's conquest of Gojoseon in 108 BCE,
per [World History Encyclopedia](https://www.worldhistory.org/Gojoseon/). Recommend the app
UI itself flag the start year as legendary/traditional rather than historical.

### `europe.mediterranean.greece.dark-age` — Greek Dark Ages (-1100..-800)
"Greek Dark Ages" is a **disputed label**. [TheCollector.com](https://www.thecollector.com/timeline-ancient-greece/)
gives the matching range (c. 1100–c. 800 BCE) but explicitly notes: "That label is
disputed, and alternative names for the period, such as Protogeometric, Geometric, or
Early Iron Age, are often used." [World History Encyclopedia](https://www.worldhistory.org/Greek_Dark_Age/)
corroborates the dates and cross-references the period as overlapping the wider Iron Age
(c. 1200–550 BCE). Recommend "Early Iron Age" as an alternate/preferred label in the UI.

### `west-asia.mesopotamia.kassite` — Kassite Babylon (-1595..-1155)
These dates are specifically the **middle chronology** figures for Mesopotamian history —
the version most commonly used in scientific publications. Confirmed exactly by the
[Met Museum's Kassite-period essay](https://www.metmuseum.org/essays/the-middle-babylonian-kassite-period-ca-1595-1155-b-c-in-mesopotamia),
which explains 1595 BC marks the Hittite sack of Babylon. Short or long chronology
would shift both endpoints by several decades. No disagreement with our stated dates,
but the chronology dependency should be documented if a citation footnote is shown.

### `europe.central.habsburg-monarchy` — Habsburg Monarchy (1526..1918)
Dates match exactly, per Britannica's [House of Habsburg summary](https://www.britannica.com/summary/House-of-Habsburg),
but only when "Habsburg Monarchy" is understood as the composite Hungary+Bohemia+Austria
realm dating from Ferdinand I's 1526 acquisition of the Hungarian and Bohemian crowns.
Habsburg rule of Austria itself is far older (1282). This is a defensible, conventional
scoping choice, not an error.

### `europe.western.england.stuart` — Stuart England / Britain (1603..1714)
Dates match exactly per [Britannica's House of Stuart article](https://www.britannica.com/topic/House-of-Stuart),
but Stuart rule was **not continuous**: the monarchy was abolished 1649–1660 during the
Commonwealth/Protectorate (Cromwell), then restored. 1603–1714 is a defensible
conventional simplification that elides an 11-year interregnum.

## Other disagreements found

### `africa.nile.egypt.sip` — Second Intermediate Period (-1650..-1550)
No source matches exactly, and this is **not really a sourcing gap so much as an
unsettled scholarly question**: [UCL's Digital Egypt chronology](https://www.ucl.ac.uk/museums-static/digitalegypt/2inter/index.html)
states outright "there is no general agreement in Egyptology either about the length or
about how to define the Second Intermediate Period." UCL itself gives c. 1700–1550 BC;
other sources range from c. 1782–c. 1539 BCE (World History Encyclopedia) to
c. 1640–1550 BCE (Met Museum educator materials). Our -1650..-1550 falls within the
plausible range but isn't uniquely confirmed by any single authoritative source.

### `africa.nile.aksum` — Kingdom of Aksum (100..940)
[Britannica](https://www.britannica.com/place/Aksum-ancient-kingdom-Africa) gives a longer
span, c. 100–c. 1100. Aksum's actual collapse date is itself disputed across sources —
Wikipedia and Portuguese Wikipedia put it at c. 940–960, closer to our 940 end year, while
Britannica's broader Aksumite-successor framing runs to 1100.

### `west-asia.iran.qajar` — Qajar Dynasty (1789..1925)
[Britannica](https://www.britannica.com/topic/Qajar-dynasty) states the dynasty ruled
"from 1794 to 1925," not 1789. The 1789 start (used in Wikipedia's infobox) marks when
Agha Mohammad Khan began his unification campaign; 1794 marks when he eliminated his last
rivals; some Britannica pages elsewhere use 1796 (his formal coronation as shah). The end
year 1925 is uncontested. Recommend either updating the start year to 1794 or documenting
which milestone (campaign start vs. victory vs. coronation) the app intends to track.

### `europe.central.prussia` — Rise of Prussia (1701..1871)
The **Kingdom of Prussia's actual lifespan was 1701–1918**, confirmed by both
[Wikipedia](https://en.wikipedia.org/wiki/Kingdom_of_Prussia) and
[Britannica's Prussia article](https://www.britannica.com/place/Prussia). Our 1871 end
year reflects a "Rise of Prussia" narrative framing that stops at German unification
(the 1871 proclamation of the German Empire), not the state's dissolution. This is a
defensible editorial choice given the entity's name, but it should not be read as the
end of Prussia as a polity.

### `europe.eastern.moscow` — Grand Duchy of Moscow (1263..1547)
Genuine cross-source disagreement: [Wikipedia's infobox](https://en.wikipedia.org/wiki/Grand_Principality_of_Moscow)
gives 1263–1478/1547 (close to ours), but Britannica's own "Grand Principality of Moscow"
page gives a distinctly different c. 1251–1505. No museum/academic source was found that
resolves this; recommend treating 1263 (Daniel I's line) and 1547 (Ivan IV's coronation
as tsar, ending the "grand principality" label) as the more commonly cited convention,
while flagging that Britannica's own dating differs.

### `south-asia.rashtrakuta` — Rashtrakuta Dynasty (735..982)
Most sources (French/Dutch Wikipedia, [World History Encyclopedia's Rashtrakuta timeline](https://www.worldhistory.org/timeline/Rashtrakuta_Dynasty/))
place the dynasty's founding at **753 CE** (Dantidurga's defeat of the last Badami
Chalukya king), not 735. Britannica gives yet another range, 755–975. The end year 982
(Indra IV's death by the Jain ritual of Sallekhana) is well-corroborated and matches ours
exactly. Recommend updating the start year to 753 unless 735 reflects an intentional
"Dantidurga's earlier career" framing.

### `south-asia.satavahana` — Satavahana Empire (-230..220)
Widely regarded as one of the most **chronologically contested dynasties in ancient
Indian history.** Most sources converge near c. 230 BCE–220 CE (matching ours), but a
Maharashtra government gazetteer argues for c. 222 BCE–226 CE, and Britannica's own
dynasty page declines to commit to firm year bounds, noting some scholars trace the
family's origin to the 3rd century BCE and others to the late 1st century BCE.

### `africa.southern.mutapa` — Mutapa Empire (1430..1760) — most contested entity found
Three incompatible date ranges exist across otherwise-reputable sources:
- [New World Encyclopedia](https://www.newworldencyclopedia.org/entry/Mutapa_Empire): c. 1450–1629 for the "first" Mutapa state, plus an entirely separate "second Mutapa state" 1803–1902.
- Britannica ("Matapa"): 1301–1700.
- Wikipedia and several non-English editions (Czech, Portuguese, Dutch): 1430–1760, matching our stored range.

No single authoritative citation confirms 1430–1760 outside Wikipedia-tier sources;
flagged accordingly in the results file.

## Minor notes (dates match but with caveats)

- **`south-asia.pallava`** (275..897): Matches Wikipedia and multiple secondary sources exactly, but Britannica uses a vaguer "early 4th to late 9th century" framing that starts later than 275.
- **`south-asia.chalukya-badami`** (543..753): Britannica gives 543–757, a 4-year difference at the end, within normal tolerance.
- **`east-asia.china.jin`** (266..420): Britannica gives 265–420, a 1-year rounding difference at the start.
