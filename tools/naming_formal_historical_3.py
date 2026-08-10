"""Third naming tranche: names that carry an ideology, and one frozen by rule.

The first tranche covered states, the second people and peoples. This one covers
names whose problem is not that they are foreign but that they encode a
viewpoint -- and one case where a name is wrong on purpose.

**The dataset had already taken a side without saying so.** Its first region is
called West Asia, not the Middle East. That is the decolonised alternative:
"Near East" and "Middle East" both measure distance from London, and Mahan
coined "Middle East" in 1902 in the *National Review* while arguing the British
should hold the Persian Gulf against Russia and Germany. A scholarly article
finds General Gordon using it two years earlier. Either way it is a naval
strategist's term for a buffer zone, adopted by the people it was not about.
The region entity now carries both names, marked as exonyms, and says why the
dataset does not use them.

**Broken Hill is a mine, and Rhodesia is a man.** The Kabwe cranium was found in
1921 at the Broken Hill mine in Northern Rhodesia, and Woodward named the
species *Homo rhodesiensis* -- after Cecil Rhodes. Roksandic and colleagues
proposed in 2021 dissolving the taxon partly on the grounds that it honours a
man who disenfranchised southern Africa's black population. The place is now
Kabwe, Zambia; the entity keeps that name and files the others as what they are.

**Neanderthal is misspelled on purpose.** The Neander valley was *Neanderthal*
until Germany's 1901 orthographic reform turned *Thal* into *Tal*. The valley
changed; the species could not, because zoological nomenclature fixes the
original spelling. So *Homo neanderthalensis* preserves an orthography Germany
abolished 125 years ago, and the German common name went to *Neandertaler* while
the Latin stayed put. That is a fourth kind of name difference again: neither
exonym nor rename nor lost classification, but a spelling frozen by rule while
the world moved.

**And two labels that are arguments.** The Vietnam War is the American War in
Vietnam if you are Vietnamese. The Age of Discovery is a discovery only from one
end -- the dataset already prefers Age of Sail, and now says why.

Deliberately NOT changed: the **Gupta "Golden Age of India"**. The label is
loaded and the entity keeps it as an alias, but adjudicating whether the period
deserves it needs the scholarship on that debate, which was not in this pass.
Recording it as `common` with an unsourced editorial note would be worse than
leaving it flat.
"""

S_TANDF_MIDDLE_EAST = "tandf-mahan-gordon-middle-east"
S_WIKI_MIDDLE_EAST = "middle-east-term-origins"
S_SMITHSONIAN_KABWE = "smithsonian-kabwe-1"
S_BRIT_KABWE = "britannica-kabwe-cranium"
S_ROKSANDIC_RHODESIENSIS = "roksandic-dissolution-rhodesiensis"
S_NEANDERTAL_VALLEY = "neandertal-valley-spelling"
S_TALKORIGINS_SPELLING = "talkorigins-neandertal-spelling"

NAMING_3_SOURCES = [
    {"id": S_TANDF_MIDDLE_EAST, "kind": "scholarly",
     "citation": "Koppes, 'Captain Mahan, General Gordon, and the origins of the term Middle East', Middle Eastern Studies",
     "url": "https://www.tandfonline.com/doi/pdf/10.1080/00263207608700307",
     "note": "Both 'Middle East' and 'Near East' reflect a Europe-centred view. Mahan is the "
             "usual coiner, in 1902, but General Sir Thomas Edward Gordon used the term in "
             "1900."},
    {"id": S_WIKI_MIDDLE_EAST, "kind": "reference",
     "citation": "'Middle East', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Middle_East",
     "note": "Mahan's coinage appeared in 'The Persian Gulf and International Relations', "
             "National Review, September 1902. Scholars from the region have criticised the "
             "term as Eurocentric and colonialist."},
    {"id": S_SMITHSONIAN_KABWE, "kind": "institutional",
     "citation": "'Kabwe 1', Smithsonian Human Origins Program",
     "url": "https://humanorigins.si.edu/evidence/human-fossils/fossils/kabwe-1",
     "note": "Found 1921 at Broken Hill, now Kabwe, Zambia. Woodward assigned it to a new "
             "species, Homo rhodesiensis; most now assign it to Homo heidelbergensis."},
    {"id": S_BRIT_KABWE, "kind": "reference",
     "citation": "'Kabwe cranium', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Kabwe-cranium",
     "note": "Records that the find, as 'Rhodesian man', convinced some scholars that African "
             "Homo lagged behind Eurasian Homo in acquiring modern anatomy."},
    {"id": S_ROKSANDIC_RHODESIENSIS, "kind": "scholarly",
     "citation": "On the proposed dissolution of Homo rhodesiensis (summarised at 'Homo rhodesiensis')",
     "url": "https://en.wikipedia.org/wiki/Homo_rhodesiensis",
     "note": "Roksandic and colleagues recommended dissolving the taxon in 2021, partly "
             "because the name honours Cecil Rhodes."},
    {"id": S_NEANDERTAL_VALLEY, "kind": "reference",
     "citation": "'Neandertal (valley)', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Neandertal_(valley)",
     "note": "The 1901 German orthographic reform changed Thal to Tal. Scientific names kept "
             "the original spelling, because taxonomy retains the spelling at the time of "
             "naming."},
    {"id": S_TALKORIGINS_SPELLING, "kind": "reference",
     "citation": "'Neanderthal or Neandertal?', TalkOrigins Archive",
     "url": "https://talkorigins.org/faqs/homs/spelling.html",
     "note": "Vallois proposed in 1952 that English follow the reformed German spelling, and "
             "'-tal' has been common since."},
]

CHECKED = "2026-08-09"


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}

    def forms(eid, name_forms, name=None, caveat=None, sources=None, **extra):
        e = by_id.get(eid)
        if e is None:
            return
        if name is not None:
            e["name"] = name
        e["name_forms"] = name_forms
        for k, v in extra.items():
            e[k] = v
        if caveat is not None:
            e["caveats"] = [c for c in e.get("caveats", [])
                            if c.get("kind") != caveat["kind"]] + [caveat]
        if sources:
            e["source_ids"] = sorted(set(list(e.get("source_ids", [])) + sources))

    # ------------------------- the choice this dataset already made silently

    forms("west-asia",
          name_forms=[
              {"name": "Middle East", "kind": "exonym", "from": 1902,
               "note": "Coined by the naval strategist Mahan in 1902 for a buffer zone "
                       "guarding the route to India. Measured from London.",
               "source_ids": [S_WIKI_MIDDLE_EAST, S_TANDF_MIDDLE_EAST]},
              {"name": "Near East", "kind": "exonym",
               "note": "The older British term for the Ottoman lands, 'near' relative to "
                       "Europe and now largely superseded outside archaeology.",
               "source_ids": [S_TANDF_MIDDLE_EAST]},
              {"name": "West Asia", "kind": "common",
               "note": "The geographic term, and the one this dataset uses: it locates the "
                       "region on its own continent rather than by distance from London.",
               "source_ids": [S_TANDF_MIDDLE_EAST]},
          ],
          caveat={"kind": "naming-confusion",
                  "text": "'Near' and 'Middle' East are measured from Europe. This dataset "
                          "files the region as West Asia for that reason, which is itself a "
                          "choice rather than a neutral default.",
                  "source_ids": [S_TANDF_MIDDLE_EAST, S_WIKI_MIDDLE_EAST]},
          sources=[S_TANDF_MIDDLE_EAST, S_WIKI_MIDDLE_EAST])

    forms("central-asia",
          name_forms=[
              {"name": "Inner Asia", "kind": "scholarly",
               "note": "Overlapping rather than synonymous: Inner Asia usually reaches further "
                       "into Mongolia and Manchuria."},
              {"name": "Turkestan", "kind": "historical",
               "note": "The 19th-century Russian and British name for the region, divided into "
                       "Russian and Chinese halves."},
          ])

    forms("south-asia",
          name_forms=[
              {"name": "Indian subcontinent", "kind": "common",
               "note": "Geographic rather than political, and older than the states in it."},
              {"name": "Hindustan", "kind": "historical", "lang": "fa"},
          ])

    forms("southeast-asia.maritime",
          name_forms=[
              {"name": "Malay Archipelago", "kind": "common"},
              {"name": "Insular Southeast Asia", "kind": "scholarly"},
              {"name": "East Indies", "kind": "historical",
               "note": "The European trading name, and the reason the Caribbean ended up "
                       "called the West Indies."},
          ])

    # -------------------------------- a mine, a man, and a place's own name

    forms("africa.prehistory.kabwe",
          name_forms=[
              {"name": "Kabwe", "kind": "common",
               "note": "The Zambian town where the mine was.",
               "source_ids": [S_SMITHSONIAN_KABWE]},
              {"name": "Broken Hill", "kind": "historical",
               "note": "The colonial-era mine and town name, in what was then Northern "
                       "Rhodesia.",
               "source_ids": [S_SMITHSONIAN_KABWE, S_BRIT_KABWE]},
              {"name": "Rhodesian Man", "kind": "rejected",
               "note": "Named for Cecil Rhodes. Roksandic and colleagues proposed dissolving "
                       "the taxon in 2021 partly on that ground.",
               "source_ids": [S_ROKSANDIC_RHODESIENSIS, S_BRIT_KABWE]},
              {"name": "Homo rhodesiensis", "kind": "rejected",
               "note": "Woodward's 1921 species name, now generally folded into Homo "
                       "heidelbergensis.",
               "source_ids": [S_SMITHSONIAN_KABWE, S_ROKSANDIC_RHODESIENSIS]},
              {"name": "Kabwe 1", "kind": "scholarly",
               "source_ids": [S_SMITHSONIAN_KABWE]},
          ],
          caveat={"kind": "naming-confusion",
                  "text": "Named three times for other people: a mine, a colony, and Cecil "
                          "Rhodes. Britannica notes the 'Rhodesian man' framing was used to "
                          "argue African Homo lagged behind Eurasian.",
                  "source_ids": [S_BRIT_KABWE, S_ROKSANDIC_RHODESIENSIS]},
          sources=[S_SMITHSONIAN_KABWE, S_BRIT_KABWE, S_ROKSANDIC_RHODESIENSIS])

    forms("africa.prehistory.taforalt",
          name_forms=[
              {"name": "Taforalt", "kind": "endonym"},
              {"name": "Grotte des Pigeons", "kind": "historical", "lang": "fr",
               "note": "The French colonial-era name, still common in the literature."},
          ])

    forms("west-asia.prehistory.jericho-neolithic",
          name_forms=[
              {"name": "Tell es-Sultan", "kind": "endonym", "lang": "ar",
               "note": "The Arabic name of the mound, and what excavation reports call it."},
              {"name": "Jericho", "kind": "common",
               "note": "The biblical name, which attaches the site to a much later story."},
          ])

    # ----------------------------------- a spelling frozen by nomenclature

    forms("global.prehistory.hominins.homo-neanderthalensis",
          name_forms=[
              {"name": "Homo neanderthalensis", "kind": "scholarly",
               "note": "Keeps the pre-1901 'th' because zoological nomenclature fixes the "
                       "spelling used when a species is named.",
               "source_ids": [S_NEANDERTAL_VALLEY]},
              {"name": "Neanderthal", "kind": "common",
               "source_ids": [S_TALKORIGINS_SPELLING]},
              {"name": "Neandertal", "kind": "common",
               "note": "The reformed spelling, proposed for English by Vallois in 1952 and "
                       "common since.",
               "source_ids": [S_TALKORIGINS_SPELLING]},
              {"name": "Neandertaler", "kind": "translation", "lang": "de",
               "note": "The German common name, which did follow the reform.",
               "source_ids": [S_NEANDERTAL_VALLEY]},
          ],
          caveat={"kind": "naming-confusion",
                  "text": "The valley was respelled Neandertal in Germany's 1901 orthographic "
                          "reform. The species could not follow: taxonomy keeps the original "
                          "spelling, so the Latin preserves an abolished one.",
                  "source_ids": [S_NEANDERTAL_VALLEY, S_TALKORIGINS_SPELLING]},
          sources=[S_NEANDERTAL_VALLEY, S_TALKORIGINS_SPELLING])

    # ------------------------------------------- labels that are arguments

    forms("global.multi-regional.vietnam-war",
          name_forms=[
              {"name": "Kháng chiến chống Mỹ", "kind": "endonym", "lang": "vi",
               "note": "'Resistance war against America', the Vietnamese name. The war is "
                       "named for the other side by whoever is speaking."},
              {"name": "American War in Vietnam", "kind": "common"},
              {"name": "Second Indochina War", "kind": "scholarly",
               "note": "Places it in a sequence beginning with the French war, which neither "
                       "national name does."},
          ])

    forms("global.multi-regional.age-of-sail",
          name_forms=[
              {"name": "Age of Exploration", "kind": "common"},
              {"name": "Age of Discovery", "kind": "common",
               "note": "A discovery only from the European end. The dataset prefers Age of "
                       "Sail, which describes the technology rather than assigning a "
                       "viewpoint."},
          ],
          caveat={"kind": "naming-confusion",
                  "text": "'Discovery' presumes whose knowledge counts as new. The places "
                          "discovered were, without exception, already inhabited."})

    # ------------------------------------------- romanisation, not renaming

    for eid, other, system in (
        ("east-asia.korea.chulmun", "Jeulmun", "Revised Romanization"),
        ("east-asia.korea.mumun", "Mumun", "Revised Romanization"),
    ):
        e = by_id.get(eid)
        if e is None or other == e["name"].split()[0]:
            continue
        forms(eid, name_forms=[
            {"name": f"{other} pottery period", "kind": "translation", "lang": "ko",
             "note": f"{system} spelling. Korean romanisation changed system in 2000, so "
                     "the same word appears two ways across the literature."},
        ])
