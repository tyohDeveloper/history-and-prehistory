"""Formal and historical names, rolled out across the entities that had them.

`name_forms` shipped in 0.20.0.0 with eight entities using it. Two of its eight
kinds went unexercised: `formal` and `historical`. This applies them.

**Two more slash hacks turn up.** `Iran / Persia` and `Habsburg / Austria-Hungary`
were doing what `Haudenosaunee (Iroquois)` did -- cramming two names into one
display field because there was nowhere else to put the second one. Both are
now single names with the alternatives typed.

**The `historical` kind earns its date fields immediately.** Several of these
names did not merely differ, they *changed*, on a date, by decision:

* **Persia to Iran** is the crispest. Iran was always the endonym; Persia is the
  Greek exonym Europe used. In December 1934 the Iranian foreign ministry gave
  foreign governments three months' notice, and from 21 March 1935 -- Nowruz --
  asked them to use Iran. That is not a scholarly reinterpretation like
  "Byzantine"; it is a government changing what other governments must call it.
* **The Holy Roman Empire** accreted its title in layers, and the sources
  disagree about when. `sacrum imperium` appears under Barbarossa's chancery in
  1157; `sacrum Romanum imperium` is dated to 1184 by one account and 1254 by
  another, when it became standard chancery terminology. "Of the German Nation"
  first appears in a document in 1474 and is fixed by the Diet of Cologne in
  1512 -- though some references still call that form unofficial. The competing
  dates are recorded rather than picked.
* **The Ottoman state** was Devlet-i Aliyye, "the Exalted State", from its
  founding; "Osmaniyye" was added during the Tanzimat, giving the Sublime
  Ottoman State. Western Europe called it the Turkish Empire, which it never
  called itself.

**And the case that started this.** `germany-modern` gets the treatment the user
named directly: `Deutschland` as the translation, `Bundesrepublik Deutschland`
as the formal name, `Germany` as the common one. One referent, three registers,
previously indistinguishable.

Note what `formal` reveals about the two Chinas. For the PRC and the ROC the
*display* name already is the formal name, and what is missing is the common
one -- "China" and "Taiwan". Those commonly-used short forms are precisely what
the sovereignty dispute is about, so they are tagged `common` with the
contested-existence caveat already on the ROC doing the explaining. The
mechanism does not resolve that dispute and should not pretend to.

Deliberately NOT dated: **Austria-Hungary from 1867**. The Ausgleich date is not
in doubt, but it was not in the sourcing pass behind this module, and the rule
here has been that a date in the dataset carries a citation. It is recorded as a
`historical` form with a note and no `from` year rather than with an uncited
one.
"""

S_NA_PERSIA_IRAN = "national-archives-persia-iran"
S_SUP_DISCOVERY_IRAN = "sup-discovery-of-iran"
S_ENCYC_HRE = "encyclopedia-com-holy-roman-empire"
S_OUP_SACRUM = "oup-sacrum-imperium-lombard"
S_HERALDICA_HRE = "heraldica-holy-roman-empire"
S_BRIT_HRE = "britannica-hre-after-frederick-ii"
S_EPFL_OTTOMAN = "epfl-ottoman-empire"
S_GHI_UNIFICATION = "ghi-unification-treaty-1990"
S_LOC_REUNIFICATION = "loc-german-reunification"

FORMAL_HISTORICAL_SOURCES = [
    {"id": S_NA_PERSIA_IRAN, "kind": "primary",
     "citation": "'From Persia to Iran, via Inglistan', The National Archives (UK) blog",
     "url": "https://blog.nationalarchives.gov.uk/persia-iran-via-inglistan/",
     "note": "In 1934 foreign governments were informed that from 21 March 1935 the country "
             "should officially be called Iran."},
    {"id": S_SUP_DISCOVERY_IRAN, "kind": "scholarly",
     "citation": "The Discovery of Iran, introduction, Stanford University Press",
     "url": "https://www.sup.org/books/middle-east-studies/discovery-iran/excerpt/introduction-excerpt",
     "note": "Dates the demand to 4 December 1934, giving three months' notice before the "
             "change took effect."},
    {"id": S_ENCYC_HRE, "kind": "reference",
     "citation": "'Holy Roman Empire', Encyclopedia.com",
     "url": "https://www.encyclopedia.com/history/modern-europe/german-history/holy-roman-empire",
     "note": "'Holy' first attached under Frederick Barbarossa's chancery in 1157; the full "
             "'of the German Nation' first used officially in 1474 and the official title "
             "from 1512."},
    {"id": S_OUP_SACRUM, "kind": "scholarly",
     "citation": "'Sacrum imperium: Lombard Influence and the Sacralization of the Empire', German History (Oxford Academic)",
     "url": "https://academic.oup.com/gh/article/39/2/147/6043923?rss=1",
     "note": "sacrum imperium adopted 1157, expanded to sacrum Romanum imperium in 1184, and "
             "standard chancery terminology only from 1254."},
    {"id": S_HERALDICA_HRE, "kind": "reference",
     "citation": "'The Holy Roman Empire', Heraldica",
     "url": "https://www.heraldica.org/topics/national/hre.htm",
     "note": "Gives 1254 as the first appearance of the two expressions together as sacrum "
             "Romanum imperium."},
    {"id": S_BRIT_HRE, "kind": "reference",
     "citation": "'Holy Roman Empire: the empire after Frederick II', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Holy-Roman-Empire/The-empire-after-Frederick-II"},
    {"id": S_EPFL_OTTOMAN, "kind": "reference",
     "citation": "'Ottoman Empire', EPFL Data Science Lab reference corpus",
     "url": "https://dlab.epfl.ch/wikispeedia/wpcd/wp/o/Ottoman_Empire.htm",
     "note": "Devlet-i Aliye-yi Osmaniyye, 'the Sublime Ottoman State'; known in the West as "
             "the Turkish Empire."},
    {"id": S_GHI_UNIFICATION, "kind": "primary",
     "citation": "Treaty of 31 August 1990 on the Establishment of German Unity (German Historical Institute, Washington)",
     "url": "https://germanhistorydocs.ghi-dc.org/pdf/eng/Unification_Treaty.pdf",
     "note": "Article 1: the accession of the German Democratic Republic takes effect on "
             "3 October 1990."},
    {"id": S_LOC_REUNIFICATION, "kind": "institutional",
     "citation": "'FALQs: 35 Years of German Reunification', Library of Congress",
     "url": "https://blogs.loc.gov/law/2025/11/falqs-35-years-of-german-reunification/",
     "note": "Legally an accession rather than a merger: the Federal Republic continued as "
             "the same subject of international law and the GDR ceased to exist."},
]

CHECKED = "2026-08-09"


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}

    def forms(eid, name=None, native=None, caveat=None, sources=None, **kw):
        e = by_id.get(eid)
        if e is None:
            return
        if name is not None:
            e["name"] = name
        if native is not None:
            e["native_name"] = native
        e["name_forms"] = kw["name_forms"]
        if caveat is not None:
            e["caveats"] = [c for c in e.get("caveats", [])
                            if c.get("kind") != caveat["kind"]] + [caveat]
        if sources:
            e["source_ids"] = sorted(set(list(e.get("source_ids", [])) + sources))

    # ------------------------------------------------ a government's decision

    forms("west-asia.iran",
          # Was "Iran / Persia" -- the same slash hack as "Haudenosaunee
          # (Iroquois)", for the same reason: nowhere to put the second name.
          name="Iran",
          name_forms=[
              {"name": "Iran", "kind": "endonym", "lang": "fa",
               "note": "Always the internal name. The 1935 change was to what foreigners "
                       "were asked to say, not to what Iranians called their country.",
               "source_ids": [S_NA_PERSIA_IRAN]},
              # One entry, not two. Listing Persia as both `historical` and
              # `exonym` printed the same word twice under different headings,
              # which reads as two different names.
              {"name": "Persia", "kind": "historical", "to": 1935, "lang": "el",
               "note": "The Greek-derived exonym Europe used. Foreign governments were asked "
                       "to drop it with effect from 21 March 1935.",
               "source_ids": [S_NA_PERSIA_IRAN, S_SUP_DISCOVERY_IRAN]},
          ],
          caveat={"kind": "naming-confusion",
                  "text": "Persia was never the country's own name. Iran is the endonym, and "
                          "in 1934 the government gave foreign states three months' notice to "
                          "start using it.",
                  "source_ids": [S_NA_PERSIA_IRAN, S_SUP_DISCOVERY_IRAN]},
          sources=[S_NA_PERSIA_IRAN, S_SUP_DISCOVERY_IRAN])

    # --------------------------------------------- a title assembled in layers

    hre = by_id.get("europe.central.hre")
    if hre is not None:
        hre["native_name"] = "Sacrum Romanum Imperium"
        hre["name_forms"] = [
            {"name": "Sacrum Romanum Imperium", "kind": "formal", "lang": "la",
             "note": "'Holy' attaches under Barbarossa's chancery in 1157; the full phrase is "
                     "dated to 1184 by one account and to 1254 by others.",
             "source_ids": [S_OUP_SACRUM, S_HERALDICA_HRE, S_ENCYC_HRE]},
            {"name": "Heiliges Römisches Reich", "kind": "translation", "lang": "de"},
            {"name": "Holy Roman Empire of the German Nation", "kind": "historical",
             "from": 1474,
             "note": "First in a document in 1474 and the official style after the Diet of "
                     "Cologne in 1512, though some references still call the longer form "
                     "unofficial.",
             "source_ids": [S_ENCYC_HRE, S_BRIT_HRE]},
            {"name": "Sacrum Imperium Romanum Nationis Germanicae", "kind": "historical",
             "from": 1512, "lang": "la",
             "source_ids": [S_ENCYC_HRE]},
        ]
        hre["date_note"] = (
            "The 800 start is Charlemagne's coronation, a convention: contemporaries did not "
            "call it the Holy Roman Empire and the title was assembled over four centuries. "
            "'Holy' appears in 1157, the full 'sacrum Romanum imperium' in 1184 or 1254 "
            "depending on the source, and 'of the German Nation' from 1474."
        )
        hre["date_precision"] = hre.get("date_precision", "year")
        hre["as_of"] = CHECKED
        hre["alternatives"] = [
            {"label": "Title 'sacrum Romanum imperium' standard only from 1254",
             "standing": "majority",
             "note": "German History dates the expanded phrase to 1184 but its adoption as "
                     "standard chancery terminology to 1254.",
             "source_ids": [S_OUP_SACRUM, S_HERALDICA_HRE]},
        ]
        hre["source_ids"] = sorted(set(list(hre.get("source_ids", [])) +
                                       [S_OUP_SACRUM, S_HERALDICA_HRE, S_ENCYC_HRE, S_BRIT_HRE]))

    forms("cross-regional.ottoman",
          native="دولت عليه عثمانیه",
          name_forms=[
              {"name": "Devlet-i ʿAlīye-i ʿOsmānīye", "kind": "formal", "lang": "ota",
               "note": "'The Sublime Ottoman State'.",
               "source_ids": [S_EPFL_OTTOMAN]},
              {"name": "Devlet-i Aliyye", "kind": "historical",
               "note": "'The Exalted State', used from the founding; 'Osmaniyye' was added "
                       "during the Tanzimat.",
               "source_ids": [S_EPFL_OTTOMAN]},
              {"name": "Osmanlı İmparatorluğu", "kind": "translation", "lang": "tr"},
              {"name": "Turkish Empire", "kind": "exonym",
               "note": "The usual Western European name. The state did not call itself Turkish.",
               "source_ids": [S_EPFL_OTTOMAN]},
          ],
          sources=[S_EPFL_OTTOMAN])

    # ------------------------------------------- one referent, three registers

    forms("europe.central.germany-modern",
          native="Bundesrepublik Deutschland",
          name_forms=[
              {"name": "Bundesrepublik Deutschland", "kind": "formal", "lang": "de"},
              {"name": "Federal Republic of Germany", "kind": "formal"},
              {"name": "Deutschland", "kind": "translation", "lang": "de"},
              {"name": "Germany", "kind": "common"},
              {"name": "West Germany", "kind": "historical", "to": 1990,
               "note": "An informal name for the same continuous state, not a predecessor of "
                       "it: the GDR acceded to the Federal Republic on 3 October 1990.",
               "source_ids": [S_GHI_UNIFICATION, S_LOC_REUNIFICATION]},
              {"name": "Deutsche Demokratische Republik", "kind": "historical", "to": 1990,
               "lang": "de",
               "note": "A separate state until it acceded; it ceased to exist rather than "
                       "merging.",
               "source_ids": [S_LOC_REUNIFICATION]},
          ])

    # Was "North Africa (Maghreb)": the same two-names-one-field workaround.
    forms("africa.north",
          name="North Africa",
          name_forms=[
              {"name": "Maghreb", "kind": "endonym", "lang": "ar",
               "note": "Arabic for 'the west'. Usually the western part rather than the whole "
                       "of North Africa, so the two are not quite synonyms."},
              {"name": "Barbary Coast", "kind": "historical",
               "note": "An early modern European name for the coast, now avoided."},
          ])

    forms("europe.central.habsburg-monarchy",
          # Also a slash name. No `from` year on the Austria-Hungary form: the
          # 1867 Ausgleich is not in doubt, but it was not in this module's
          # sourcing pass, and an uncited date is exactly what this dataset
          # spent three releases removing.
          name="The Habsburg Monarchy",
          name_forms=[
              {"name": "Austria-Hungary", "kind": "historical",
               "note": "The dual monarchy's name after the Compromise, for the last half "
                       "century of its existence."},
              {"name": "Habsburg Empire", "kind": "common"},
              {"name": "Österreich-Ungarn", "kind": "translation", "lang": "de"},
              {"name": "Austrian Empire", "kind": "historical"},
          ])

    forms("americas.north.usa",
          name_forms=[
              {"name": "United States of America", "kind": "formal"},
              {"name": "USA", "kind": "common"},
              {"name": "America", "kind": "common",
               "note": "Ambiguous: also the name of two continents, which is why this dataset "
                       "files the country under North America rather than the reverse."},
          ])

    forms("europe.eastern.russian-empire",
          native="Россійская Имперія",
          name_forms=[
              {"name": "Rossiyskaya Imperiya", "kind": "formal", "lang": "ru"},
              {"name": "Imperial Russia", "kind": "common"},
              {"name": "Tsarist Russia", "kind": "common"},
          ])

    forms("africa.nile.ethiopia",
          name_forms=[
              {"name": "Abyssinia", "kind": "historical",
               "note": "The usual European name into the 20th century, from Arabic Habasha. "
                       "Ethiopia is the older and the preferred form."},
              {"name": "Solomonic Dynasty", "kind": "scholarly"},
          ])

    # ---------------------- where the common name is what the dispute is about

    forms("east-asia.china.prc",
          name_forms=[
              {"name": "People's Republic of China", "kind": "formal"},
              {"name": "中华人民共和国", "kind": "formal", "lang": "zh-Hans"},
              {"name": "China", "kind": "common",
               "note": "The short form is not neutral: which state it denotes is the "
                       "substance of the dispute recorded on the Republic of China."},
              {"name": "PRC", "kind": "common"},
              {"name": "Mainland China", "kind": "common"},
          ])

    forms("east-asia.china.roc",
          name_forms=[
              {"name": "Republic of China", "kind": "formal"},
              {"name": "中華民國", "kind": "formal", "lang": "zh-Hant"},
              {"name": "Taiwan", "kind": "common", "from": 1949,
               "note": "The everyday name since the government relocated. Using it as the "
                       "state's name is itself a position in the dispute."},
              {"name": "ROC", "kind": "common"},
              {"name": "Nationalist China", "kind": "historical", "to": 1949},
              {"name": "Republican Era", "kind": "scholarly",
               "note": "How the 1912-1949 mainland period is usually named in Chinese "
                       "historiography."},
          ])

    forms("east-asia.korea.divided",
          name_forms=[
              {"name": "Democratic People's Republic of Korea", "kind": "formal"},
              {"name": "Republic of Korea", "kind": "formal"},
              {"name": "North Korea", "kind": "common"},
              {"name": "South Korea", "kind": "common"},
              {"name": "DPRK", "kind": "common"},
              {"name": "ROK", "kind": "common"},
              {"name": "Chosŏn", "kind": "endonym", "lang": "ko",
               "note": "The North's word for the nation."},
              {"name": "Hanguk", "kind": "endonym", "lang": "ko",
               "note": "The South's word for the same nation."},
          ])

    # --------------------------------- typing the forms Byzantium already had

    forms("europe.mediterranean.byzantine",
          name_forms=[
              {"name": "Βασιλεία τῶν Ῥωμαίων", "kind": "endonym", "lang": "grc",
               "note": "'Empire of the Romans'. Its subjects called themselves Romans."},
              {"name": "Basileia ton Rhomaion", "kind": "formal", "lang": "grc"},
              {"name": "Eastern Roman Empire", "kind": "scholarly"},
              {"name": "Rhomania", "kind": "endonym", "lang": "grc",
               "note": "The everyday word for the country, as against the formal style."},
              {"name": "Byzantium", "kind": "exonym"},
          ])

    # "Old Stone Age" and "New Stone Age" are straight synonyms, unlike
    # "Chalcolithic (Anatolia)", where the parenthetical is the only thing
    # separating five sibling entities. That difference is not mechanically
    # detectable, so only the genuine synonyms move.
    forms("global.paleolithic",
          name="Paleolithic",
          name_forms=[
              {"name": "Old Stone Age", "kind": "common",
               "note": "The English calque of the Greek. Part of the three-age scheme whose "
                       "worldwide application is contested on this entity's parent."},
              {"name": "Palaeolithic", "kind": "translation", "lang": "en-GB"},
          ])

    forms("global.neolithic",
          name="Neolithic",
          name_forms=[
              {"name": "New Stone Age", "kind": "common"},
          ])

    forms("southeast-asia.maritime.dutch-eic",
          name_forms=[
              {"name": "Nederlands-Indië", "kind": "formal", "lang": "nl"},
              {"name": "Netherlands East Indies", "kind": "formal"},
              {"name": "Dutch East Indies", "kind": "common"},
              {"name": "Indonesia", "kind": "historical", "from": 1945,
               "note": "The successor state, proclaimed in 1945 and recognised by the "
                       "Netherlands in 1949."},
          ])
