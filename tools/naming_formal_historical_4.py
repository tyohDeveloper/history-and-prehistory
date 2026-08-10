"""Fourth naming tranche: endonyms recoverable from cuneiform, and a name that is a claim about who owns the past.

Also a consistency fix that should have happened three releases ago.

**The Golden Horde still was not using the mechanism built for it.** It was the
case that prompted all of this -- a 16th-century Russian coinage sitting where a
polity's own name should be -- and it had been carrying flat `aliases` plus a
caveat since before `name_forms` existed. Now typed like everything else, with
Ulug Ulus as the endonym.

**Cuneiform means some endonyms are recoverable exactly.** Uruk is Akkadian; the
city's own Sumerian name was **Unug**, written 𒀕𒆠. It reached English through
the Bible as Erech and through Greek as Orchoe, and the site is Warka in Arabic
today -- possibly the root of "Iraq". Five names, four languages, one place, and
we know which one its inhabitants used. Chogha Zanbil is the same: the modern
Persian name of a mound whose Elamite name, **Dur-Untash**, is written on its own
bricks.

**And a name that is an argument about who owns the past.** Calling the Indus
civilization "Sindhu-Sarasvati" ties it to the Rigvedic river Sarasvati, and
through that to Vedic culture. The identification of the Sarasvati with the
Ghaggar-Hakra is not fringe -- it dates to 1855 and generations of indologists,
geologists and archaeologists have endorsed it. But as a *renaming* it does
work: as Kumar sets out, identifying the two lets the Harappans be Aryanised, and
the Aryans be indigenous, and the Hindu community be the exclusive proprietor of
the Indian past. Other historians call the label hyper-nationalist. Both halves
of that are recorded, because a reader who meets only one has been handled.

**Shaffer's terminology is not a synonym but a rival scheme.** Integration Era
and Localization Era are not other words for Mature and Late Harappan; they come
from a different model, organised by interaction intensity rather than urban
phase, with its own boundaries -- Shaffer's Regionalization begins around 4000
BCE where Coningham and Young put it at 5000. Filed `scholarly` with that said
explicitly rather than implying interchangeability.

**One more silent editorial choice, stated.** This dataset calls it the Neolithic
*Transition*, not the Neolithic *Revolution*. That is the same kind of choice as
Age of Sail over Age of Discovery, and like that one it was sitting unexplained.
Childe's "revolution" is the famous label and implies a speed the evidence does
not support -- the dataset's own entities put the process at four thousand years
in Southwest Asia.
"""

S_ENCYC_ERECH = "encyclopedia-com-erech"
S_UNIVE_HAKRA = "unive-hakra-cultural-horizon"
S_KENOYER_TRADITION = "kenoyer-1991-indus-valley-tradition"
S_KUMAR_ARYANS = "kumar-2022-why-aryans-still-matter"
S_IE_NAMING_CIV = "indian-express-naming-oldest-civilisation"

NAMING_4_SOURCES = [
    {"id": S_ENCYC_ERECH, "kind": "reference",
     "citation": "'Erech', Encyclopedia.com",
     "url": "https://www.encyclopedia.com/religion/encyclopedias-almanacs-transcripts-and-maps/erech",
     "note": "Sumerian Unug, Akkadian Uruk, modern Warka; Erech is the biblical form."},
    {"id": S_UNIVE_HAKRA, "kind": "scholarly",
     "citation": "'The Hakra Cultural Horizon in the Greater Indus Valley', Ca' Foscari University of Venice",
     "url": "https://iris.unive.it/retrieve/b13823e4-7893-47b2-8cdf-c26a8f94402b/956395-1229871.pdf",
     "note": "Sets out Shaffer's Tradition/Phase/Era model against the conventional "
             "Early/Mature/Late Harappan phases."},
    {"id": S_KENOYER_TRADITION, "kind": "scholarly",
     "citation": "Kenoyer, 'The Indus Valley Tradition of Pakistan and western India' (1991)",
     "url": "https://www.harappa.com/sites/default/files/pdf/Kenoyer1991%20Indus%20Valley%20Tradition.pdf",
     "note": "Describes the Eras by interaction intensity: the Integration Era shows "
             "widespread homogeneity, the Localization Era altered interaction networks."},
    {"id": S_KUMAR_ARYANS, "kind": "scholarly",
     "citation": "Ashish Kumar, 'Why the Aryans Still Matter? History, Historiography and Politics', SAGE (2022)",
     "url": "https://journals.sagepub.com/doi/10.1177/2455328X211063048",
     "note": "Identifying the Rigvedic Sarasvati with the Ghaggar-Hakra allows the Harappan "
             "civilization to be Aryanised and the Aryans located within India, supporting an "
             "exclusive Hindu claim on the Indian past."},
    {"id": S_IE_NAMING_CIV, "kind": "news",
     "citation": "'Naming the oldest civilisation of India: Indus, Harappan or Sindhu-Sarasvati?', The Indian Express",
     "url": "https://indianexpress.com/article/research/naming-the-oldest-civilisation-of-india-indus-harappan-or-sindhu-sarasvati-9701782/",
     "note": "Some historians call the Sarasvati label hyper-nationalist; against that, the "
             "Ghaggar-Sarasvati identification dates from 1855 and has been endorsed by "
             "generations of specialists."},
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

    # ------------------- the case that started this, finally using the field

    forms("central-asia.mongol-empire.golden-horde",
          name_forms=[
              {"name": "Ulug Ulus", "kind": "endonym",
               "note": "'Great State' in Turkic, attested in the Horde's own written sources."},
              {"name": "Ulus of Jochi", "kind": "endonym",
               "note": "The Jochid inheritance, and how contemporaries placed it within the "
                       "Mongol succession."},
              {"name": "Jochid ulus", "kind": "scholarly"},
              {"name": "Golden Horde", "kind": "exonym",
               "note": "A Russian coinage first attested in the 16th century, long after the "
                       "polity it names."},
              {"name": "Kipchak Khanate", "kind": "scholarly",
               "note": "After the Turkic majority of its nomadic population."},
          ])

    # ----------------------------- endonyms recoverable from the tablets

    forms("west-asia.prehistory.late-chalcolithic-mesopotamia.uruk-period",
          name_forms=[
              {"name": "Unug", "kind": "endonym", "lang": "sux",
               "note": "The city's Sumerian name, written 𒀕𒆠. Uruk is the Akkadian form.",
               "source_ids": [S_ENCYC_ERECH]},
              {"name": "Uruk", "kind": "exonym", "lang": "akk",
               "source_ids": [S_ENCYC_ERECH]},
              {"name": "Erech", "kind": "exonym",
               "note": "The biblical form, and how the name first reached English.",
               "source_ids": [S_ENCYC_ERECH]},
              {"name": "Warka", "kind": "common", "lang": "ar",
               "note": "The modern Arabic name of the site, possibly the root of 'Iraq'.",
               "source_ids": [S_ENCYC_ERECH]},
          ],
          sources=[S_ENCYC_ERECH])

    forms("west-asia.iran.elam.middle-elamite.chogha-zanbil",
          name_forms=[
              {"name": "Dur-Untash", "kind": "endonym", "lang": "elx",
               "note": "'Fortress of Untash', its Elamite name, stamped on its own bricks."},
              {"name": "Chogha Zanbil", "kind": "common", "lang": "fa",
               "note": "The modern Persian name of the mound, roughly 'basket hill'."},
              {"name": "Tchogha Zanbil", "kind": "translation",
               "note": "The French transliteration, used by UNESCO."},
          ])

    forms("west-asia.iran.elam.susa",
          name_forms=[
              {"name": "Shushan", "kind": "endonym", "lang": "elx"},
              {"name": "Susa", "kind": "exonym", "lang": "grc",
               "note": "The Greek form, which is how Europe received the name."},
              {"name": "Shush", "kind": "common", "lang": "fa",
               "note": "The modern Iranian town on the site."},
          ])

    forms("europe.prehistory.newgrange",
          name_forms=[
              {"name": "Sí an Bhrú", "kind": "endonym", "lang": "ga",
               "note": "The Irish name of the monument itself."},
              {"name": "Brú na Bóinne", "kind": "endonym", "lang": "ga",
               "note": "'Palace of the Boyne', properly the whole complex rather than this "
                       "mound alone."},
              {"name": "Newgrange", "kind": "common",
               "note": "An English farm name, from the grange land of Mellifont Abbey."},
          ])

    # ------------------------- a name that is a claim about who owns the past

    # The summary asserted "along the Indus and Sarasvati rivers" -- using the
    # contested name as a bare fact directly above a caveat calling it
    # contested. Same failure as the ROC: the prose was making a claim the
    # apparatus was busy qualifying.
    forms("south-asia.indus",
          summary="Bronze Age civilization along the Indus and the Ghaggar-Hakra.",
          name_forms=[
              {"name": "Harappan Civilization", "kind": "scholarly",
               "note": "Named for the first site excavated, which is convention rather than "
                       "precedence: Harappa was simply dug first."},
              {"name": "Indus Valley Civilization", "kind": "common"},
              {"name": "Sindhu-Sarasvati Civilization", "kind": "common",
               "note": "Ties the civilization to the Rigvedic Sarasvati. The river "
                       "identification is long-standing; the renaming is contested as "
                       "nationalist.",
               "source_ids": [S_KUMAR_ARYANS, S_IE_NAMING_CIV]},
          ],
          caveat={"kind": "naming-confusion",
                  "text": "Which name you use is a position. 'Sindhu-Sarasvati' makes the "
                          "Harappans Vedic; some historians call that hyper-nationalist, while "
                          "the underlying river identification dates to 1855.",
                  "source_ids": [S_KUMAR_ARYANS, S_IE_NAMING_CIV]},
          sources=[S_KUMAR_ARYANS, S_IE_NAMING_CIV])

    forms("south-asia.indus.ghaggar-hakra",
          name_forms=[
              {"name": "Sarasvati question", "kind": "common",
               "note": "Names the debate after the Vedic river, which is the claim the debate "
                       "is about.",
               "source_ids": [S_KUMAR_ARYANS, S_IE_NAMING_CIV]},
              {"name": "Ghaggar-Hakra", "kind": "scholarly",
               "note": "The modern hydronym, used because it does not presuppose the "
                       "identification.",
               "source_ids": [S_IE_NAMING_CIV]},
          ],
          sources=[S_KUMAR_ARYANS, S_IE_NAMING_CIV])

    # ------------------------------ a rival scheme, not a set of synonyms

    for eid, era, phase in (
        ("south-asia.indus.kot-diji", "Regionalization Era", "Early Harappan"),
        ("south-asia.indus.mature", "Integration Era", "Mature Harappan"),
        ("south-asia.indus.late", "Localization Era", "Late Harappan"),
    ):
        e = by_id.get(eid)
        if e is None:
            continue
        keep = [a for a in e.get("aliases", []) if a not in (era,)]
        forms(eid, name_forms=(
            [{"name": a, "kind": "scholarly"} for a in keep] +
            [{"name": era, "kind": "scholarly",
              "note": f"Shaffer's term, not a synonym for {phase}: it comes from a model "
                      "organised by interaction intensity, with its own boundaries.",
              "source_ids": [S_UNIVE_HAKRA, S_KENOYER_TRADITION]}]
        ), sources=[S_UNIVE_HAKRA, S_KENOYER_TRADITION])

    # ------------------------------- another silent choice, made explicit

    forms("global.neolithic.agricultural-revolution",
          name_forms=[
              {"name": "Neolithic Revolution", "kind": "common",
               "note": "Childe's label, and the famous one. It implies a speed this dataset's "
                       "own entities contradict."},
              {"name": "Agricultural Revolution", "kind": "common"},
              {"name": "First Agricultural Revolution", "kind": "scholarly"},
          ],
          caveat={"kind": "naming-confusion",
                  "text": "Called a Transition here rather than a Revolution: the process took "
                          "roughly four thousand years in Southwest Asia, which is not what "
                          "the word revolution conveys."})

    # ------------------------------------------------ conventions and nicknames

    forms("east-asia.japan.edo",
          name_forms=[
              {"name": "Tokugawa Period", "kind": "scholarly",
               "note": "The same span named for the ruling house rather than the capital -- "
                       "two conventions, dynasty or place, used interchangeably."},
              {"name": "Edo Jidai", "kind": "endonym", "lang": "ja"},
          ])

    forms("europe.reformation",
          name_forms=[
              {"name": "Protestant Reformation", "kind": "common",
               "note": "Names the movement by its outcome and from one side; Catholic writing "
                       "long preferred 'Protestant revolt'."},
              {"name": "European Reformation", "kind": "scholarly"},
          ])

    forms("south-asia.indo-greek.menander-i",
          name_forms=[
              {"name": "Menander I Soter", "kind": "formal", "lang": "grc",
               "note": "'Saviour', from his coinage."},
              {"name": "Milinda", "kind": "endonym", "lang": "pi",
               "note": "His name in the Pali Milindapanha, where he debates a Buddhist monk "
                       "and converts. He is remembered in two traditions under two names."},
          ])

    forms("africa.nile.egypt.new-kingdom.dyn18.tutankhamun",
          name_forms=[
              {"name": "Tutankhaten", "kind": "historical",
               "note": "His name at accession, honouring the Aten. He changed it to honour "
                       "Amun instead, reversing his father's religion."},
              {"name": "King Tut", "kind": "common",
               "note": "A 1920s press abbreviation, which is why the least consequential "
                       "pharaoh is the most famous."},
          ])

    forms("global.prehistory.hominins.homo-longi",
          name_forms=[
              {"name": "Homo longi", "kind": "scholarly",
               "note": "'Dragon' for Heilongjiang, the Black Dragon River province."},
              {"name": "Dragon Man", "kind": "common"},
              {"name": "Harbin cranium", "kind": "scholarly",
               "note": "The specimen name, preferred by those who doubt the species is "
                       "distinct."},
          ])

    forms("africa.nile.egypt.old-kingdom",
          name_forms=[
              {"name": "Age of the Pyramids", "kind": "common",
               "note": "True of this period but not only of it: pyramids were built for a "
                       "thousand years after it ended."},
          ])
