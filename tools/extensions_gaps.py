"""The gaps: a Netherlands to hang the companies on, France's empires, Britain's missing century, and the depopulation debate.

Four things deferred across earlier passes, each for a stated reason. The
reasons are now addressed rather than repeated.

**The VOC and WIC had no parent.** Two passes declined to author them because
the dataset had no Netherlands node at all, and filing a company that operated
from the Cape to Nagasaki under "Maritime Southeast Asia" would have been worse
than omitting it. The node exists now, so they do.

Both companies turn out to be good examples of a thing this dataset keeps
finding: a date that looks disputed but is really a process described from
different points.

* The **VOC** ends in 1798, 1799 or 1800 depending on the source, and those are
  not rival claims. The Batavian Republic assumed the company's debts in March
  1798; the charter lapsed on 31 December 1799; the state took administrative
  control in 1800. Three steps, three correct dates.
* The **WIC** is two companies. The first was declared bankrupt and dissolved by
  the States General in September 1674; a second was chartered in 1675 with much
  the same remit and ran to 1 January 1792. The dataset's old "1621-1794" figure
  conflated them, and 1794 is Britannica's date for the French invasion sweeping
  up what remained -- a third terminus again.

**Britain had a 123-year hole.** The Stuarts ended in 1714 and the Victorians
began in 1837, with nothing in between: no Hanoverians, no Georgian era, no
Regency, no Industrial Revolution at home. Filed as the Georgian era, whose own
end is genuinely disputed -- 1830 with George IV, or 1837 with William IV.

**The French colonial empire** has the same first/second structure as the
British and the same argument about it. Its second empire's end date, 5 July
1962, is flagged as what the earlier research found it to be: a convention
chosen to echo 1830 by exactly 132 years.

**And the depopulation debate**, deferred from the Americas pass because the
estimates run from 8 million to over 100 million. It is authored now precisely
*as* a dispute: Kroeber low, Dobyns at 90-112 million on an assumption of 95 per
cent mortality, Denevan at about 55 million, modern work converging near 45-60
million. It is cross-cutting context for every post-1492 end date already in the
dataset, and leaving it out was leaving those dates unexplained.
"""

S_HEIDELBERG_VOC = "heidelberg-voc-charter-1602"
S_UMASSD_VOC = "umassd-the-voc"
S_CAMBRIDGE_WIC = "cambridge-wic-bankruptcy-1674"
S_ENCYC_WIC = "encyclopedia-com-dutch-west-india-company"
S_BRIT_WIC = "britannica-dutch-west-india-company"
S_LOC_WIC_CHARTER = "loc-wic-charter-1621"
S_WIKI_GEORGIAN = "georgian-era-definition"
S_OEB_GEORGIAN = "univ-oeb-georgian-britain"
S_WIKI_FRENCH_EMPIRE = "french-colonial-empire-dates"
S_GLOBALSEC_FRENCH = "globalsecurity-french-colonial-empire"
S_SMITHSONIAN_CROSBY = "smithsonian-crosby-columbian-exchange"
S_POP_HISTORY = "population-history-indigenous-americas"

GAP_SOURCES = [
    {"id": S_HEIDELBERG_VOC, "kind": "scholarly",
     "citation": "Heidelberg University Press, on the VOC charter",
     "url": "https://books.ub.uni-heidelberg.de/arthistoricum/catalog/view/499/1049/87966",
     "note": "The charter (octrooi) signed on 20 March 1602 marked the formal creation of the "
             "Company."},
    {"id": S_UMASSD_VOC, "kind": "scholarly",
     "citation": "'The VOC 1602-1799', University of Massachusetts Dartmouth",
     "url": "https://bpb-us-w2.wpmucdn.com/sites.umassd.edu/dist/4/628/files/2017/02/thevoc.pdf"},
    {"id": S_CAMBRIDGE_WIC, "kind": "scholarly",
     "citation": "'Recapitalization or Reform? The Bankruptcy of the First Dutch West India Company and the Formation of the Second, 1674', Cambridge University Press",
     "url": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/15B612FB4C8EF77F1B24EA2513A129D2/S016511531900007Xa.pdf/recapitalization_or_reform_the_bankruptcy_of_the_first_dutch_west_india_company_and_the_formation_of_the_second_west_india_company_1674.pdf",
     "note": "The first WIC was 'disbanded and destroyed' by the States General in September "
             "1674; a second was founded with a charter largely taken from the first."},
    {"id": S_ENCYC_WIC, "kind": "reference",
     "citation": "'Dutch West India Company', Encyclopedia.com",
     "url": "https://www.encyclopedia.com/history/modern-europe/benelux-history/dutch-west-india-company",
     "note": "Chartered 3 June 1621; dissolved September 1674; the second company abolished "
             "in 1791."},
    {"id": S_BRIT_WIC, "kind": "reference",
     "citation": "'Dutch West India Company', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Dutch-West-India-Company",
     "note": "Gives 1621-1794: taken over by the state in 1791 and dissolved in the wake of "
             "the French invasion of the Dutch Republic in 1794."},
    {"id": S_LOC_WIC_CHARTER, "kind": "institutional",
     "citation": "Charter of the Dutch West India Company, 1621, Library of Congress",
     "url": "https://www.loc.gov/item/2021666732/"},
    {"id": S_WIKI_GEORGIAN, "kind": "reference",
     "citation": "'Georgian era', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Georgian_era",
     "note": "1714 to 1830, often extended to 1837. Historians debate the ending, with the "
             "deaths of George IV in 1830 or William IV in 1837 as the usual markers."},
    {"id": S_OEB_GEORGIAN, "kind": "scholarly",
     "citation": "'Britain in the 18th Century: The Georgian Era', Université Oum El Bouaghi",
     "url": "http://tele-ens.univ-oeb.dz/moodle/pluginfile.php/146951/mod_forum/attachment/5437/Lesson%20One,%2018th%20C%20Britain,%20political%20developments.pdf?forcedownload=1"},
    {"id": S_WIKI_FRENCH_EMPIRE, "kind": "reference",
     "citation": "'French colonial empire', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/French_colonial_empire",
     "note": "Gives 1534 (Cartier's claim) as the start and 1814 as the end of the first "
             "empire, by which time most of it had been lost or sold."},
    {"id": S_GLOBALSEC_FRENCH, "kind": "reference",
     "citation": "'French Colonial Empire', GlobalSecurity.org",
     "url": "https://www.globalsecurity.org/military/world/europe/fr-colony-1.htm",
     "note": "Frames the first empire as 1603-1803, ending with the Louisiana sale rather "
             "than the Napoleonic collapse."},
    {"id": S_SMITHSONIAN_CROSBY, "kind": "institutional",
     "citation": "'Alfred W. Crosby on the Columbian Exchange', Smithsonian Magazine",
     "url": "https://www.smithsonianmag.com/history/alfred-w-crosby-on-the-columbian-exchange-98116477/",
     "note": "Crosby coined the term in his 1972 book of the same name."},
    {"id": S_POP_HISTORY, "kind": "reference",
     "citation": "'Population history of the Indigenous peoples of the Americas', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Population_history_of_the_Indigenous_peoples_of_the_Americas",
     "note": "Collects the competing estimates: Kroeber low, Dobyns 90-112 million on an "
             "assumed 95 per cent epidemic mortality, Denevan about 55 million, with modern "
             "work converging near 45-60 million."},
]

CHECKED = "2026-08-09"
CAL = "calendar"


def extend(E, entities):
    from builders import make_builders
    R, P, ERA, EVENT, _, _ = make_builders(E)
    _, _, NL_ERA, _, _, _ = make_builders(E, id_prefix="europe.western.netherlands")
    _, _, FR_ERA, _, _, _ = make_builders(E, id_prefix="europe.western.france")
    _, _, BR_ERA, _, _, _ = make_builders(E, id_prefix="europe.western.britain")
    by_id = {e["id"]: e for e in entities}

    # ------------------------------------------ a parent for the companies

    R("netherlands", "The Netherlands", "europe.western", 1581, None,
      summary="The Dutch Republic and its successors, and the two chartered companies through "
              "which a small state ran a global trading empire.")

    NL_ERA("voc", "Dutch East India Company", "europe.western.netherlands", 1602, 1799,
           "foundational",
           native="Vereenigde Oostindische Compagnie",
           summary="A chartered company with the power to wage war, coin money and hold "
                   "territory, which for two centuries was the Dutch presence in Asia.",
           start_dating_method=CAL, end_dating_method=CAL,
           standing="majority", date_precision="year",
           date_note="Chartered 20 March 1602; the charter lapsed on 31 December 1799. The "
                     "1798, 1799 and 1800 dates in circulation are not rival claims but three "
                     "steps: the Batavian Republic assumed the company's debts in March 1798, "
                     "the charter lapsed at the end of 1799, and the state took administrative "
                     "control in 1800.",
           name_forms=[
               {"name": "VOC", "kind": "common"},
               {"name": "Vereenigde Oostindische Compagnie", "kind": "formal", "lang": "nl"},
               {"name": "United East India Company", "kind": "formal"},
           ],
           caveats=[{"kind": "misconception",
                     "text": "Not a company in the modern sense. Its charter granted powers of "
                             "war, treaty-making, coinage and colonial government.",
                     "source_ids": [S_HEIDELBERG_VOC]}],
           source_ids=[S_HEIDELBERG_VOC, S_UMASSD_VOC])

    NL_ERA("wic-first", "Dutch West India Company", "europe.western.netherlands", 1621, 1674,
           "intermediate",
           summary="The Atlantic counterpart of the VOC: Brazil, the Caribbean, New "
                   "Netherland, and a dominant share of the Dutch slave trade.",
           start_dating_method=CAL, end_dating_method=CAL,
           standing="majority", date_precision="year",
           date_note="Chartered 3 June 1621 and declared bankrupt by the States General in "
                     "September 1674. This is the first company; a second followed immediately "
                     "under a near-identical charter, and sources that give '1621-1794' have "
                     "run the two together.",
           source_ids=[S_LOC_WIC_CHARTER, S_CAMBRIDGE_WIC, S_ENCYC_WIC])

    NL_ERA("wic-second", "Second Dutch West India Company", "europe.western.netherlands",
           1675, 1792, "specialist",
           summary="The successor company, narrower in remit and increasingly dependent on the "
                   "slave trade.",
           start_dating_method=CAL, end_dating_method=CAL,
           standing="majority", date_precision="disputed", as_of=CHECKED,
           date_note="Chartered 1675 and wound up on 1 January 1792, having been abolished by "
                     "decision in 1791.",
           alternatives=[
               {"label": "Ends 1791 (abolition decided)", "standing": "majority",
                "end_year": 1791,
                "note": "The States General decided not to renew the patent in 1791; the "
                        "formal end followed on 1 January 1792.",
                "source_ids": [S_ENCYC_WIC]},
               {"label": "Ends 1794 (French invasion)", "standing": "minority",
                "end_year": 1794,
                "note": "Britannica dates the dissolution to the French invasion of the Dutch "
                        "Republic.",
                "source_ids": [S_BRIT_WIC]},
           ],
           source_ids=[S_CAMBRIDGE_WIC, S_ENCYC_WIC, S_BRIT_WIC])

    # ------------------------------------------------- France's two empires

    FR_ERA("colonial-empire-first", "First French Colonial Empire", "europe.western.france",
           1534, 1814, "foundational",
           summary="New France, the Caribbean sugar islands and the Indian trading posts, most "
                   "of it lost or sold within two generations.",
           start_dating_method=CAL, end_dating_method=CAL,
           standing="majority", date_precision="disputed", as_of=CHECKED,
           date_note="Both ends are choices. 1534 is Cartier's claim rather than a settlement, "
                     "and the end depends on which loss counts as terminal.",
           alternatives=[
               {"label": "1605-1803 (Port Royal to the Louisiana sale)", "standing": "majority",
                "start_year": 1605, "end_year": 1803,
                "note": "Dates the empire from the first actual colony and ends it with the "
                        "sale of Louisiana rather than the Napoleonic collapse.",
                "source_ids": [S_GLOBALSEC_FRENCH]},
           ],
           source_ids=[S_WIKI_FRENCH_EMPIRE, S_GLOBALSEC_FRENCH])

    FR_ERA("colonial-empire-second", "Second French Colonial Empire", "europe.western.france",
           1830, 1962, "foundational",
           summary="Rebuilt around Algeria and expanded across West and Central Africa and "
                   "Indochina, and dismantled in fifteen years after 1945.",
           start_dating_method=CAL, end_dating_method=CAL,
           standing="majority", date_precision="year",
           date_note="1830 is the invasion of Algiers and is essentially uncontested. The end "
                     "is Algerian independence, declared on 5 July 1962 -- a date chosen to "
                     "fall exactly 132 years after the landing, which makes it a commemorative "
                     "convention as much as an administrative fact.",
           caveats=[{"kind": "misconception",
                     "text": "5 July 1962 is a symbolic date. The Evian ceasefire was in March "
                             "and France recognised independence on 3 July.",
                     "source_ids": [S_WIKI_FRENCH_EMPIRE]}],
           source_ids=[S_WIKI_FRENCH_EMPIRE])

    # -------------------------------------------- Britain's missing century

    BR_ERA("georgian", "The Georgian Era", "europe.western", 1714, 1837, "foundational",
           summary="Hanoverian Britain: the Jacobite risings, the loss of America, the "
                   "Regency, and the industrial transformation that reshaped the country.",
           start_dating_method=CAL, end_dating_method=CAL,
           standing="majority", date_precision="disputed", as_of=CHECKED,
           date_note="1714 is George I's accession on the death of Queen Anne. The end is "
                     "disputed: 1830 with George IV, the last of the four Georges, or 1837 "
                     "with William IV, which is the boundary with the Victorian era.",
           name_forms=[
               {"name": "Hanoverian Britain", "kind": "common"},
               {"name": "House of Hanover", "kind": "formal"},
               {"name": "Regency era", "kind": "historical", "from": 1811, "to": 1820,
                "note": "Strictly the regency of George IV as Prince of Wales during his "
                        "father's illness, though used loosely for the wider period.",
                "source_ids": [S_WIKI_GEORGIAN]},
           ],
           alternatives=[
               {"label": "Ends 1830 (death of George IV)", "standing": "majority",
                "end_year": 1830,
                "note": "Ends the era with the last of the four kings it is named after.",
                "source_ids": [S_WIKI_GEORGIAN, S_OEB_GEORGIAN]},
           ],
           source_ids=[S_WIKI_GEORGIAN, S_OEB_GEORGIAN])

    # ------------------------------------ the context behind every 1492 date

    ERA("columbian-exchange", "The Columbian Exchange", "global", 1492, 1700, "foundational",
        summary="The transfer of crops, animals, people and above all disease between "
                "hemispheres, and the demographic collapse that followed in the Americas.",
        start_dating_method=CAL, end_dating_method=CAL,
        standing="majority", date_precision="disputed", as_of=CHECKED,
        date_note="The end date is a convention: the exchange has no terminus, and 1700 marks "
                  "roughly where the sharpest demographic phase closes. The pre-contact "
                  "population, and so the scale of the collapse, is one of the least settled "
                  "quantities in the discipline.",
        name_forms=[
            {"name": "Columbian Exchange", "kind": "scholarly",
             "note": "Coined by Alfred Crosby in his 1972 book of that name; the phrase is "
                     "younger than most of the scholarship it now organises.",
             "source_ids": [S_SMITHSONIAN_CROSBY]},
            {"name": "Great Dying", "kind": "common",
             "note": "Used for the depopulation specifically, and naming it separately makes "
                     "clear that 'exchange' is a very mild word for it."},
        ],
        alternatives=[
            {"label": "Pre-contact population c. 90-112 million (Dobyns)", "standing": "minority",
             "note": "Dobyns's 1966 estimate, built on an assumption of about 95 per cent "
                     "epidemic mortality.",
             "source_ids": [S_POP_HISTORY]},
            {"label": "Pre-contact population c. 55 million (Denevan)", "standing": "majority",
             "note": "Denevan's 1976 middle estimate; modern work converges near 45-60 million.",
             "source_ids": [S_POP_HISTORY]},
        ],
        caveats=[
            {"kind": "misconception",
             "text": "Estimates of the pre-contact population range from 8 million to over 100 "
                     "million. The disagreement is methodological, not evidentiary, so more "
                     "digging does not narrow it.",
             "source_ids": [S_POP_HISTORY]},
            {"kind": "naming-confusion",
             "text": "'Exchange' describes crops and livestock accurately and the human "
                     "consequence not at all: depopulation estimates run from 75 to 95 per "
                     "cent.",
             "source_ids": [S_POP_HISTORY, S_SMITHSONIAN_CROSBY]},
        ],
        source_ids=[S_SMITHSONIAN_CROSBY, S_POP_HISTORY])

    # The Dutch and French empires satisfy the cross-regional test as squarely
    # as the Spanish and Portuguese already cross-linked there.
    for eid in ("europe.western.netherlands.voc",
                "europe.western.france.colonial-empire-second"):
        e = by_id.get(eid)
        if e is not None:
            e["cross_parent_ids"] = sorted(set(list(e.get("cross_parent_ids", [])) +
                                               ["cross-regional"]))
