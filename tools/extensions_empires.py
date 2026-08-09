"""Empires: the missing British one, and four names that were doing damage.

Research in `docs/empires-research.md`.

Two jobs here, and the naming one matters more than the additions.

**The naming principle, stated for the first time.** The dataset already had two
mechanisms and used them inconsistently. `aliases` renders as "Also known as"
and makes an entity findable. A `naming-confusion` caveat renders under "Worth
knowing", carries sources, and explains why a name misleads. Between them they
cover the problem, but they had been applied to the *easy* cases -- Cheops,
King Tut, Ozymandias -- and skipped on the hard ones. The Golden Horde had
neither, despite its name being a documented 16th-century Russian invention.

The rule from here: **file under the name the polity used where one is
recoverable; carry the common name as an alias so search still works; and when
the common name embeds a claim, say so in a caveat with a source.** Findability
and truth are different jobs and the schema already has a field for each.

Applied here to the Ulus of Jochi. Not yet applied to the caliphates, the PRC
and ROC, or Korea, which need it and are noted as outstanding.

**The British Empire did not exist in this dataset.** England ran to the Stuarts
and then jumped to the Victorian era; there was no empire, no Act of Union, and
nothing at all after 1901. It is added here with both ends held open, because
neither end is a fact:

* The **start** is a definitional fork rather than a dispute. Nobody disagrees
  about what happened in 1497, 1583 or 1607; they disagree about which one
  counts. That is a different kind of uncertainty from a contested radiocarbon
  date and the note says so.
* The **end** has four live positions -- 1947, 1956, 1960, 1997 -- with named
  proponents and no winner.
* The **First/Second Empire split** is recorded as genuinely contested, not as
  settled periodisation. Britannica and the tertiary literature use it; Marshall
  and Cambridge specialists argue the two overlapped and the break is artificial.
* Pre-1707 activity was **English**, not British. The empire is filed from 1583
  but the note carries the distinction.

Also: the Dutch East Indies entry is flagged for what its identifier implies but
its dates deny, and Spain's 1898 is scoped to the empire it actually ends.

Deliberately NOT authored: the **VOC** itself, the **Dutch West India Company**,
and the **French colonial empire**. The VOC and WIC have no sensible parent
because there is no Netherlands node in the dataset at all -- filing a company
that operated from the Cape to Nagasaki under "Maritime Southeast Asia" would be
worse than leaving it out. That is a gap to fix with a Netherlands node, not a
place to wedge an entity. The WIC additionally needs splitting into two charters
(1621-1674, then c. 1675-1791/92) and sources differ on the final year.
"""

S_BURBANK_COOPER = "burbank-cooper-empires-world-history"
S_OWHE = "oxford-world-history-of-empire"
S_OSTROWSKI = "ostrowski-golden-horde"
S_IRANICA_HORDE = "iranica-golden-horde"
S_CAMB_MONGOL = "cambridge-history-mongol-empire-horde"
S_BRIT_HORDE = "britannica-golden-horde"
S_BRIT_LOSS_COLONIES = "britannica-loss-american-colonies"
S_MARSHALL = "marshall-making-unmaking-empires"
S_CAMB_FIRST_SECOND = "cambridge-first-second-empire"
S_BROWN_BRIT_ACADEMY = "brown-british-academy-states"
S_AIIA_SUEZ = "aiia-suez-death-of-empire"
S_MACINNES = "macinnes-union-and-empire"
S_BRIT_TIMELINE = "britannica-british-empire-timeline"
S_ELCANO = "elcano-spanish-withdrawal-sahara"
S_MURCIA_1898 = "murcia-1898-spanish-empire"
S_BRIT_TORDESILLAS = "britannica-treaty-tordesillas"
S_AVALON_TORDESILLAS = "avalon-tordesillas"
S_BROWN_EJPH_PORTUGAL = "brown-ejph-portuguese-empire"
S_BRIT_INDONESIA = "britannica-dutch-rule-indonesia"
S_LOC_WIC = "loc-dutch-west-india-company"

EMPIRE_SOURCES = [
    {"id": S_BURBANK_COOPER, "kind": "scholarly",
     "citation": "Burbank & Cooper, Empires in World History: Power and the Politics of Difference (review, Project MUSE)",
     "url": "https://muse.jhu.edu/article/713800",
     "note": "Treats the caliphates, the Mongol empire and the European maritime empires as "
             "comparable phenomena rather than separate historiographical worlds."},
    {"id": S_OWHE, "kind": "scholarly",
     "citation": "The Oxford World History of Empire, project overview (Stanford)",
     "url": "https://web.stanford.edu/~scheidel/OWHE.pdf",
     "note": "Frames cross-empire comparison as a deliberate corrective to older siloed, "
             "single-region imperial history."},
    {"id": S_OSTROWSKI, "kind": "scholarly",
     "citation": "Ostrowski, on the Golden Horde (Harvard)",
     "url": "https://donostrowski2.bitbucket.io/mm/golden2.pdf",
     "note": "'Golden Horde' is a retrospective Russian coinage first attested in the 16th "
             "century, never a contemporary self-designation."},
    {"id": S_IRANICA_HORDE, "kind": "reference",
     "citation": "'Golden Horde', Encyclopaedia Iranica",
     "url": "https://www.iranicaonline.org/articles/golden-horde/",
     "note": "Gives the contemporary designation as the ulus of Jochi."},
    {"id": S_CAMB_MONGOL, "kind": "scholarly",
     "citation": "'The Golden Horde, c. 1260-1502', The Cambridge History of the Mongol Empire",
     "url": "https://www.cambridge.org/core/books/cambridge-history-of-the-mongol-empire/golden-horde-c-12601502/194D20494453E0AC8373BE9ADFB8B8D6",
     "note": "Dates the polity's independent existence from about 1260, later than the "
             "conventional 1240s."},
    {"id": S_BRIT_HORDE, "kind": "reference",
     "citation": "'Golden Horde', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Golden-Horde"},
    {"id": S_BRIT_LOSS_COLONIES, "kind": "reference",
     "citation": "'Loss of the American colonies', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Western-colonialism/Loss-of-the-American-colonies",
     "note": "States the standard framing: a first empire centred on North America in 1763, "
             "a second centred on India by 1815."},
    {"id": S_MARSHALL, "kind": "scholarly",
     "citation": "P. J. Marshall, The Making and Unmaking of Empires (Oxford University Press)",
     "url": "https://academic.oup.com/book/2601",
     "note": "Contests the First/Second Empire split, arguing losses in America and gains in "
             "India were part of a single process."},
    {"id": S_CAMB_FIRST_SECOND, "kind": "scholarly",
     "citation": "Cambridge University Press, on First and Second British Empire periodisation",
     "url": "https://assets.cambridge.org/97805215/90815/excerpt/9780521590815_excerpt.pdf",
     "note": "Records specialist protest against any easy separation, on the grounds the two "
             "overlapped in time."},
    {"id": S_BROWN_BRIT_ACADEMY, "kind": "scholarly",
     "citation": "Judith Brown, 'The making and breaking of states', Journal of the British Academy",
     "url": "https://www.thebritishacademy.ac.uk/documents/1547/JBA-001-133-Brown.pdf"},
    {"id": S_AIIA_SUEZ, "kind": "scholarly",
     "citation": "'The Suez dispute and the death of empire', Australian Institute of International Affairs",
     "url": "https://www.internationalaffairs.org.au/australianoutlook/the-suez-dispute-and-the-death-of-empire/",
     "note": "Reports diplomatic historians as agreed that the 1956 invasion of Egypt "
             "signalled the approaching demise of empire."},
    {"id": S_MACINNES, "kind": "scholarly",
     "citation": "Allan I. Macinnes, Union and Empire: The Making of the United Kingdom in 1707",
     "url": "https://pureportal.strath.ac.uk/en/publications/union-and-empire-the-making-of-the-united-kingdom-in-1707/",
     "note": "Sets the Acts of Union in a colonial context; the state of Great Britain dates "
             "from 1707, so earlier overseas activity is English."},
    {"id": S_BRIT_TIMELINE, "kind": "reference",
     "citation": "'British Empire Timeline', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/summary/British-Empire-Timeline"},
    {"id": S_ELCANO, "kind": "scholarly",
     "citation": "'Fifty years since the Spanish withdrawal from the Western Sahara', Real Instituto Elcano",
     "url": "https://www.realinstitutoelcano.org/en/analyses/between-principles-and-national-interest-50-years-since-the-spanish-withdrawal-from-the-western-sahara/",
     "note": "The 1975-76 withdrawal from the Western Sahara is the end of Spain's last "
             "significant overseas territory."},
    {"id": S_MURCIA_1898, "kind": "scholarly",
     "citation": "On 1898 and the end of the Spanish overseas empire, Anales de Historia Contemporanea (Universidad de Murcia)",
     "url": "https://revistas.um.es/analeshc/article/download/87411/84141/356521"},
    {"id": S_BRIT_TORDESILLAS, "kind": "reference",
     "citation": "'Treaty of Tordesillas', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/event/Treaty-of-Tordesillas"},
    {"id": S_AVALON_TORDESILLAS, "kind": "primary",
     "citation": "Treaty of Tordesillas, 1494 (text), Yale Avalon Project",
     "url": "https://avalon.law.yale.edu/15th_century/mod001.asp"},
    {"id": S_BROWN_EJPH_PORTUGAL, "kind": "scholarly",
     "citation": "e-Journal of Portuguese History (Brown University), on Portuguese imperial periodisation",
     "url": "https://www.brown.edu/Departments/Portuguese_Brazilian_Studies/ejph/html/issue27/pdf/v14n1a04.pdf"},
    {"id": S_BRIT_INDONESIA, "kind": "reference",
     "citation": "'History of Indonesia: Dutch rule from 1815 to c. 1920', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/history-of-Indonesia/Dutch-rule-from-1815-to-c-1920"},
    {"id": S_LOC_WIC, "kind": "reference",
     "citation": "Dutch West India Company records, Library of Congress",
     "url": "https://www.loc.gov/item/2021666732/"},
]

CHECKED = "2026-08-09"
CAL = "calendar"


def extend(E, entities):
    from builders import make_builders
    _, P, ERA, EVENT, _, _ = make_builders(E)
    # Britain's ids sit under `europe.western.britain` while their parent is
    # `europe.western`, matching how the Iberian empires are already filed:
    # there is no `britain` node, only an id path. Same divergence the Roman
    # emperors use.
    _, _, BR_ERA, BR_EVENT, _, _ = make_builders(E, id_prefix="europe.western.britain")
    by_id = {e["id"]: e for e in entities}

    # ------------------------------------------ the name the polity used

    h = by_id.get("central-asia.mongol-empire.golden-horde")
    if h is not None:
        h["name"] = "Ulus of Jochi"
        h["aliases"] = ["Golden Horde", "Jochid ulus", "Kipchak Khanate"]
        h["summary"] = (
            "The Jochid inheritance of the Mongol empire, ruling the western steppe and the "
            "Rus principalities. Known in English by a name it never used."
        )
        h["start_year"] = 1242
        h["date_precision"] = "disputed"
        # Calendar at both ends: the disagreement is about which event counts as
        # a beginning, not about how any of the candidate dates were derived.
        # That is a definitional fork, which `date_precision: disputed` carries.
        h["start_dating_method"] = CAL
        h["end_dating_method"] = CAL
        h["standing"] = "majority"
        h["date_note"] = (
            "The start depends on what is being dated -- the grant of the ulus, the western "
            "campaign, or effective independence from the Great Khan -- and specialists place "
            "it anywhere from the 1220s to the 1260s. 1502 is comparatively firm."
        )
        h["as_of"] = CHECKED
        h["alternatives"] = [
            {"label": "c. 1224/25 (grant of the ulus to Jochi's line)", "standing": "minority",
             "start_year": 1225,
             "note": "Dates the polity from the appanage itself rather than from its "
                     "independence.",
             "source_ids": [S_IRANICA_HORDE]},
            {"label": "1236-40 (the western campaign)", "standing": "minority",
             "start_year": 1236,
             "note": "Dates it from the conquest of the Rus principalities and the Kipchak "
                     "steppe.",
             "source_ids": [S_BRIT_HORDE]},
            {"label": "c. 1260 (effective independence)", "standing": "majority",
             "start_year": 1260,
             "note": "The Cambridge History of the Mongol Empire treats the Horde as a "
                     "separate polity only from about 1260.",
             "source_ids": [S_CAMB_MONGOL]},
        ]
        h["caveats"] = list(h.get("caveats", [])) + [
            {"kind": "naming-confusion",
             "text": "'Golden Horde' is a Russian coinage first attested in the 16th century, "
                     "long after the fact. Contemporaries called it the ulus of Jochi.",
             "source_ids": [S_OSTROWSKI, S_IRANICA_HORDE]},
        ]
        h["source_ids"] = sorted(set(list(h.get("source_ids", [])) +
                                     [S_OSTROWSKI, S_IRANICA_HORDE, S_CAMB_MONGOL, S_BRIT_HORDE]))

    # ------------------------------------------------- the missing empire

    BR_ERA("empire", "The British Empire", "europe.western", 1583, 1997, "foundational",
        aliases=["First British Empire", "Second British Empire"],
        summary="The largest empire in history by area, and an entity whose beginning and end "
                "are both matters of definition rather than record.",
        start_dating_method=CAL, end_dating_method=CAL,
        standing="majority", date_precision="disputed",
        date_note="Neither end is a fact. The span given is the widest defensible one: "
                  "Gilbert's Newfoundland claim to the Hong Kong handover, after which Britain "
                  "held no significant overseas territory for the first time since 1707. "
                  "Activity before the Acts of Union in 1707 was English, not British.",
        as_of=CHECKED,
        alternatives=[
            {"label": "Start 1497 (Cabot's voyage)", "standing": "minority",
             "start_year": 1497,
             "note": "Dates the empire from England's first overseas claim rather than any "
                     "settlement.",
             "source_ids": [S_BRIT_TIMELINE]},
            {"label": "Start 1607 (Jamestown)", "standing": "majority",
             "start_year": 1607,
             "note": "Dates it from the first permanent settlement, the most commonly cited "
                     "criterion.",
             "source_ids": [S_BRIT_TIMELINE]},
            {"label": "End 1947 (Indian independence)", "standing": "majority",
             "end_year": 1947,
             "note": "The most common institutional marker for the end of the imperial core.",
             "source_ids": [S_BROWN_BRIT_ACADEMY]},
            {"label": "End 1956 (Suez)", "standing": "majority",
             "end_year": 1956,
             "note": "Diplomatic historians treat Suez as the moment imperial power was "
                     "publicly exposed as spent.",
             "source_ids": [S_AIIA_SUEZ]},
        ],
        caveats=[
            {"kind": "misconception",
             "text": "The start is a definitional fork, not a dispute about evidence. Nobody "
                     "disagrees about what happened in 1497, 1583 or 1607, only about which "
                     "one counts as a beginning.",
             "source_ids": [S_BRIT_TIMELINE]},
            {"kind": "naming-confusion",
             "text": "The split into a First and Second Empire hinging on 1783 is standard in "
                     "tertiary sources but contested by specialists, who argue the two "
                     "overlapped and the break is artificial.",
             "source_ids": [S_MARSHALL, S_CAMB_FIRST_SECOND, S_BRIT_LOSS_COLONIES]},
        ],
        source_ids=[S_BRIT_TIMELINE, S_BRIT_LOSS_COLONIES, S_MARSHALL, S_CAMB_FIRST_SECOND,
                    S_BROWN_BRIT_ACADEMY, S_AIIA_SUEZ, S_MACINNES])

    BR_EVENT("acts-of-union", "The Acts of Union", "europe.western", 1707, 1707, "intermediate",
          summary="England and Scotland became one state, which is the point at which an "
                  "English empire can properly be called British.",
          start_dating_method=CAL, end_dating_method=CAL,
          standing="consensus", date_precision="exact",
          date_note="Ratified 1 May 1707.",
          source_ids=[S_MACINNES])

    # ----------------------------------------------- sourcing the Iberians

    sp = by_id.get("europe.western.iberia.spanish-empire")
    if sp is not None:
        sp["date_precision"] = "disputed"
        sp["start_dating_method"] = CAL
        sp["end_dating_method"] = CAL
        sp["standing"] = "majority"
        sp["date_note"] = (
            "1898 ends the American and Pacific empire, which is the empire usually meant. It "
            "is not the end of Spanish overseas territory: the withdrawal from the Western "
            "Sahara in 1975-76 is the later terminus."
        )
        sp["as_of"] = CHECKED
        sp["alternatives"] = [
            {"label": "End 1975-76 (withdrawal from the Western Sahara)", "standing": "majority",
             "end_year": 1976,
             "note": "The end of Spain's last significant overseas territory, and the terminus "
                     "used when the second colonial empire is counted.",
             "source_ids": [S_ELCANO]},
        ]
        sp["source_ids"] = sorted(set(list(sp.get("source_ids", [])) +
                                      [S_MURCIA_1898, S_ELCANO, S_BRIT_TORDESILLAS,
                                       S_AVALON_TORDESILLAS]))

    pt = by_id.get("europe.western.iberia.portuguese-empire")
    if pt is not None:
        pt["start_dating_method"] = CAL
        pt["end_dating_method"] = CAL
        pt["standing"] = "majority"
        pt["date_precision"] = "year"
        pt["date_note"] = (
            "Ceuta in 1415 to the Macau handover in 1999, a span of 584 years. Unusually for "
            "an empire of this size, both ends are largely uncontested."
        )
        pt["source_ids"] = sorted(set(list(pt.get("source_ids", [])) +
                                      [S_BROWN_EJPH_PORTUGAL, S_BRIT_TORDESILLAS,
                                       S_AVALON_TORDESILLAS]))

    # ------------------------- an identifier that contradicts its own dates

    di = by_id.get("southeast-asia.maritime.dutch-eic")
    if di is not None:
        di["aliases"] = ["Netherlands East Indies", "Nederlands-Indie"]
        di["start_dating_method"] = CAL
        di["end_dating_method"] = CAL
        di["standing"] = "majority"
        di["date_precision"] = "disputed"
        di["date_note"] = (
            "This is the state colony, not the company. The Dutch East India Company's charter "
            "lapsed on 31 December 1799 and its possessions were nationalised, so the period "
            "beginning in 1800 is by definition not company rule. Direct Dutch administration "
            "was interrupted by French and British control from 1806 to 1816."
        )
        di["as_of"] = CHECKED
        di["alternatives"] = [
            {"label": "End 1945 (Indonesian proclamation of independence)", "standing": "majority",
             "end_year": 1945,
             "note": "Indonesia dates independence from the 1945 proclamation; 1949 is the "
                     "year the Netherlands recognised it.",
             "source_ids": [S_BRIT_INDONESIA]},
        ]
        di["caveats"] = list(di.get("caveats", [])) + [
            {"kind": "naming-confusion",
             "text": "The identifier says East India Company, but the company was wound up "
                     "before this period begins. Company rule is a separate, earlier thing.",
             "source_ids": [S_BRIT_INDONESIA, S_LOC_WIC]},
        ]
        di["source_ids"] = sorted(set(list(di.get("source_ids", [])) +
                                      [S_BRIT_INDONESIA, S_LOC_WIC]))

    # ------------------------------ warrant for the cross-regional grouping

    cr = by_id.get("cross-regional")
    if cr is not None:
        cr["summary"] = (
            "Empires and imperial processes that spanned more than one world region, gathered "
            "so they can be compared with each other."
        )
        cr["date_note"] = (
            "Grouping the caliphates, the Mongol empire and the European maritime empires "
            "together is a deliberate scholarly move rather than a filing convenience. Burbank "
            "and Cooper treat them as comparable, and the Oxford World History of Empire frames "
            "the comparison as a corrective to older single-region imperial history."
        )
        cr["source_ids"] = [S_BURBANK_COOPER, S_OWHE]
