"""Mainland Southeast Asia: the Burmese hole, the Thai and Lao states, and Vietnam.

Southeast Asia was the thinnest region in the dataset by a wide margin -- 35
entities against East Asia's 491 -- and the imbalance was not evenly spread. Its
*prehistory* was well covered and fully sourced; its *history* was eighteen
entities of which one carried a source. Three specific failures stood out.

**Burma stopped in 1297.** The Pagan Kingdom ended and nothing followed, leaving
588 years blank through the Toungoo and Konbaung dynasties, the three
Anglo-Burmese wars and the colonial period.

**Đại Việt was one node covering 939-1804.** Eight hundred and sixty-five years
flattened into a single entity, in a dataset that gives China individual emperors.

**The name Đại Việt was also wrong for most of that span**, which matters more.
The dataset's own naming rule says a name should be the one a reader arrives with
and should never be left to stand alone when it misleads. Đại Việt was in use
1054-1400 and 1428-1804. Before that the state was Đại Cồ Việt; under the Hồ it
was Đại Ngu; during the Ming occupation it was the province of Jiaozhi. Applying
one name across all of it asserted a continuity of self-designation that did not
exist -- the same error the Byzantine and Golden Horde passes were about.

So Đại Việt is narrowed to what it names, and the dynastic sequence carries the
rest.

**What is deliberately not done.** The Trịnh-Nguyễn division is left unauthored.
Research recommends modelling it as two co-existing lord-domains under nominal Lê
rule, which is right, but it needs the same care the caliphate overlap needs and
would be a rushed job here. Recorded as an open question instead.
"""

# ── sources ────────────────────────────────────────────────────────────────
S_BRIT_MYANMAR = "britannica-history-of-myanmar"
S_BRIT_BURMA_BRIT = "britannica-british-in-burma"
S_BRIT_TOUNGOO = "britannica-toungoo-dynasty"
S_WIKI_TOUNGOO = "wikipedia-toungoo-dynasty"
S_BRIT_DVARAVATI = "britannica-dvaravati"
S_BRIT_MON = "britannica-mon-kingdom"
S_JSEAS_DVARAVATI = "jseas-proto-dvaravati"
S_BRIT_SUKHOTHAI = "britannica-sukhothai-kingdom"
S_BRIT_LAOS = "britannica-history-of-laos"
S_WIKI_LANXANG = "wikipedia-lan-xang"
S_EBSCO_FUNAN = "ebsco-kingdom-of-funan"
S_WIKI_KHMER = "wikipedia-khmer-empire"
S_BRIT_CHAMPA = "britannica-champa"
S_WIKI_CHAMPA = "wikipedia-champa"
S_WIKI_DAIVIET = "wikipedia-dai-viet"
S_WIKI_NGO = "wikipedia-ngo-dynasty"
S_WIKI_DINH = "wikipedia-dinh-dynasty"
S_BRIT_LYTHAITO = "britannica-ly-thai-to"
S_WIKI_LYTHANHTONG = "wikipedia-ly-thanh-tong"
S_BRIT_TRAN = "britannica-tran-dynasty"
S_WIKI_HO = "wikipedia-ho-dynasty"
S_WIKI_FOURTH_DOM = "wikipedia-fourth-chinese-domination"
S_WIKI_LE = "wikipedia-le-dynasty"
S_WIKI_MAC = "wikipedia-mac-dynasty"
S_BRIT_TAYSON = "britannica-tay-son-brothers"
S_WIKI_TAYSON = "wikipedia-tay-son-dynasty"
S_WIKI_FRINDOCHINA = "wikipedia-french-indochina"

SEA_MAINLAND_SOURCES = [
    {"id": S_BRIT_MYANMAR, "kind": "reference",
     "citation": "'History of Myanmar', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/history-of-Myanmar",
     "note": "The Pagan, post-Pagan, Toungoo and Konbaung sequence."},
    {"id": S_BRIT_BURMA_BRIT, "kind": "reference",
     "citation": "'The British in Burma, 1885-1948', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/history-of-Myanmar/The-British-in-Burma-1885-1948",
     "note": "The annexation following the Third Anglo-Burmese War and the road to "
             "independence in 1948."},
    {"id": S_BRIT_TOUNGOO, "kind": "reference",
     "citation": "'Toungoo dynasty', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Toungoo-dynasty",
     "note": "Competing start dates are reported for the dynasty; Britannica and "
             "Wikipedia do not agree on which to lead with."},
    {"id": S_WIKI_TOUNGOO, "kind": "reference",
     "citation": "'Toungoo dynasty', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Toungoo_dynasty",
     "note": "Sets out the First and Second Toungoo distinction and the 1510 date."},
    {"id": S_BRIT_DVARAVATI, "kind": "reference",
     "citation": "'Dvaravati', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Dvaravati",
     "note": "The Mon culture of the Chao Phraya basin."},
    {"id": S_BRIT_MON, "kind": "reference",
     "citation": "'Mon kingdom', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Mon-kingdom",
     "note": "Background on the Mon polities."},
    {"id": S_JSEAS_DVARAVATI, "kind": "scholarly",
     "citation": "'The Case for Proto-Dvaravati', Journal of Southeast Asian Studies",
     "url": "https://www.cambridge.org/core/journals/journal-of-southeast-asian-studies/article/abs/case-for-protodvaravati-a-review-of-the-art-historical-and-archaeological-evidence/6ABA16AADF5C3B4D62086719BEEF6A5C",
     "note": "Reviews the art-historical and archaeological evidence, and bears on "
             "whether Dvaravati was one state or a network of them."},
    {"id": S_BRIT_SUKHOTHAI, "kind": "reference",
     "citation": "'Sukhothai kingdom', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Sukhothai-kingdom",
     "note": "The traditional 1238 founding, which Michael Vickery and others have "
             "challenged along with the authenticity of the Ram Khamhaeng inscription."},
    {"id": S_BRIT_LAOS, "kind": "reference",
     "citation": "'History of Laos', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/history-of-Laos",
     "note": "Lan Xang and its division into Vientiane, Luang Phrabang and Champasak."},
    {"id": S_WIKI_LANXANG, "kind": "reference",
     "citation": "'Lan Xang', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Lan_Xang",
     "note": "Gives 1707 for the split; other accounts date the break-up to 1694."},
    {"id": S_EBSCO_FUNAN, "kind": "reference",
     "citation": "'Kingdom of Funan', EBSCO Research Starters",
     "url": "https://www.ebsco.com/research-starters/anthropology/kingdom-funan",
     "note": "Funan is a Chinese exonym and its status as a unified state is disputed, "
             "notably by Michael Vickery."},
    {"id": S_WIKI_KHMER, "kind": "reference",
     "citation": "'Khmer Empire', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Khmer_Empire",
     "note": "The 802 consecration of Jayavarman II and the 1431 Ayutthayan capture of "
             "Angkor."},
    {"id": S_BRIT_CHAMPA, "kind": "reference",
     "citation": "'Champa', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Champa-ancient-kingdom-Indochina",
     "note": "Britannica's own account is internally inconsistent about whether Champa "
             "ended in the 15th or the 17th century."},
    {"id": S_WIKI_CHAMPA, "kind": "reference",
     "citation": "'Champa', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Champa",
     "note": "Treats Champa as a confederation of polities -- Indrapura, Amaravati, "
             "Vijaya, Kauthara, Panduranga -- rather than one continuous kingdom, with "
             "annexation completed in 1832."},
    {"id": S_WIKI_DAIVIET, "kind": "reference",
     "citation": "'Đại Việt', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/%C4%90%E1%BA%A1i_Vi%E1%BB%87t",
     "note": "The name was in use 1054-1400 and 1428-1804, not continuously from 939."},
    {"id": S_WIKI_NGO, "kind": "reference",
     "citation": "'Ngô dynasty', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Ng%C3%B4_dynasty",
     "note": "Sources give both 965 and 968 for the end, depending on whether the "
             "interregnum is counted."},
    {"id": S_WIKI_DINH, "kind": "reference",
     "citation": "'Đinh dynasty', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/%C4%90inh_dynasty",
     "note": "Đại Cồ Việt, the state's name from 968."},
    {"id": S_BRIT_LYTHAITO, "kind": "reference",
     "citation": "'Ly Thai To', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/biography/Ly-Thai-To",
     "note": "Founder of the Lý dynasty in 1009."},
    {"id": S_WIKI_LYTHANHTONG, "kind": "reference",
     "citation": "'Lý Thánh Tông', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/L%C3%BD_Th%C3%A1nh_T%C3%B4ng",
     "note": "Credited with the 1054 renaming to Đại Việt, though the traditional "
             "account of that renaming has been questioned."},
    {"id": S_BRIT_TRAN, "kind": "reference",
     "citation": "'Tran dynasty', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Tran-dynasty",
     "note": "The dynasty that repelled three Mongol invasions."},
    {"id": S_WIKI_HO, "kind": "reference",
     "citation": "'Hồ dynasty', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/H%E1%BB%93_dynasty",
     "note": "Renamed the state Đại Ngu, and fell to the Ming in 1407."},
    {"id": S_WIKI_FOURTH_DOM, "kind": "reference",
     "citation": "'Fourth Chinese domination of Vietnam', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Fourth_Chinese_domination_of_Vietnam",
     "note": "The Ming administered the territory as the province of Jiaozhi, 1407-1427."},
    {"id": S_WIKI_LE, "kind": "reference",
     "citation": "'Lê dynasty', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/L%C3%AA_dynasty",
     "note": "The Later Lê, under whom real power passed to the Trịnh and Nguyễn lords."},
    {"id": S_WIKI_MAC, "kind": "reference",
     "citation": "'Mạc dynasty', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/M%E1%BA%A1c_dynasty",
     "note": "The usurpation of 1527-1592, overlapping the Lê, with a rump state "
             "surviving to 1677."},
    {"id": S_BRIT_TAYSON, "kind": "reference",
     "citation": "'Tay Son brothers', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Tay-Son-brothers",
     "note": "The rising that displaced both the Trịnh and the Nguyễn."},
    {"id": S_WIKI_TAYSON, "kind": "reference",
     "citation": "'Tây Sơn dynasty', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/T%C3%A2y_S%C6%A1n_dynasty",
     "note": "1778-1802."},
    {"id": S_WIKI_FRINDOCHINA, "kind": "reference",
     "citation": "'French Indochina', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/French_Indochina",
     "note": "The union formed in 1887 and dissolved in 1954."},
]


def extend(E, entities):
    from builders import make_builders

    by_id = {e["id"]: e for e in entities}
    _, P, ERA, EVENT, _, _ = make_builders(E, id_prefix="southeast-asia.mainland")

    def enrich(eid, **fields):
        e = by_id.get(eid)
        if e is None:
            return
        for k, v in fields.items():
            e[k] = v

    # ── Burma: the 588-year hole ──────────────────────────────────────────
    # Dvaravati is entered as a culture whose political unity is disputed,
    # because that is what the evidence supports -- the alternative is to imply
    # a Mon kingdom that may never have existed as one thing.
    ERA("dvaravati", "Dvaravati", "southeast-asia.mainland", 600, 1100, "intermediate",
        summary="Mon Buddhist culture of the Chao Phraya basin, of disputed political "
                "unity.",
        date_note="Whether Dvaravati was a single kingdom or a network of related "
                  "polities sharing a culture is unsettled. The span is approximate at "
                  "both ends; its close is especially unclear, being a gradual "
                  "absorption by Khmer and then Thai power rather than a conquest.",
        source_ids=[S_BRIT_DVARAVATI, S_BRIT_MON, S_JSEAS_DVARAVATI],
        caveats=[{"kind": "contested-existence",
                  "text": "Often described as a kingdom, but the evidence may support a "
                          "cultural network of separate polities instead.",
                  "source_ids": [S_JSEAS_DVARAVATI, S_BRIT_DVARAVATI]}],
        date_precision="approx")

    ERA("post-pagan", "Post-Pagan Burma", "southeast-asia.mainland", 1297, 1510,
        "foundational",
        summary="Two centuries of competing successor states after Pagan fell, "
                "principally Ava in the interior and Hanthawaddy in the delta.",
        date_note="A period of coexisting rivals rather than one polity: Myinsaing, "
                  "Pinya, Sagaing, then Ava against Mon Hanthawaddy. Entered as a single "
                  "span because the dataset previously left these 213 years blank "
                  "entirely, which was worse than a container.",
        source_ids=[S_BRIT_MYANMAR])

    ERA("toungoo", "Toungoo Dynasty", "southeast-asia.mainland", 1510, 1752,
        "foundational",
        summary="Reunified Burma and briefly built the largest empire in mainland "
                "Southeast Asia.",
        date_note="Scholars divide it into a First and Second Toungoo, and give "
                  "competing start dates; 1510 follows the founding of the Toungoo "
                  "state itself rather than a later imperial expansion.",
        source_ids=[S_WIKI_TOUNGOO, S_BRIT_TOUNGOO],
        alternatives=[{"label": "Later start, dating the dynasty from its imperial phase",
                       "standing": "minority",
                       "note": "Britannica and Wikipedia do not lead with the same year.",
                       "source_ids": [S_BRIT_TOUNGOO]}])

    ERA("konbaung", "Konbaung Dynasty", "southeast-asia.mainland", 1752, 1885,
        "foundational",
        summary="The last Burmese dynasty, ended by British annexation after the third "
                "of three Anglo-Burmese wars.",
        source_ids=[S_BRIT_MYANMAR, S_BRIT_BURMA_BRIT])

    ERA("british-burma", "British Burma", "southeast-asia.mainland", 1885, 1948,
        "foundational",
        summary="Annexed after the Third Anglo-Burmese War and governed as a province "
                "of British India until 1937.",
        date_note="Annexation followed the war of 1885; the formal proclamation and "
                  "administrative reorganisation ran into 1886. Independence came in "
                  "January 1948.",
        source_ids=[S_BRIT_BURMA_BRIT],
        name_forms=[{"name": "Burma", "kind": "exonym",
                     "note": "The colonial-era English name. Myanmar and Burma both "
                             "derive from the same root, and the choice between them "
                             "remains politically loaded.",
                     "source_ids": [S_BRIT_MYANMAR]}])

    # ── Thai and Lao states ───────────────────────────────────────────────
    ERA("sukhothai", "Sukhothai Kingdom", "southeast-asia.mainland", 1238, 1438,
        "foundational",
        native="สุโขทัย",
        summary="Tai kingdom of the upper Chao Phraya, traditionally cast as the first "
                "Thai state.",
        date_note="Both the 1238 founding date and the 'first Thai kingdom' framing rest "
                  "on the Ram Khamhaeng inscription, whose authenticity Michael Vickery "
                  "and others have questioned. Treat the date as traditional rather than "
                  "attested. Absorbed by Ayutthaya in 1438.",
        source_ids=[S_BRIT_SUKHOTHAI],
        alternatives=[{"label": "1238, from the Ram Khamhaeng inscription",
                       "standing": "traditional", "start_year": 1238,
                       "note": "The inscription's authenticity has been disputed since "
                               "the 1980s.",
                       "source_ids": [S_BRIT_SUKHOTHAI]}],
        caveats=[{"kind": "naming-confusion",
                  "text": "Called the first Thai kingdom by convention, but Tai polities "
                          "existed before it and the claim originates in later national "
                          "historiography.",
                  "source_ids": [S_BRIT_SUKHOTHAI]}],
        date_precision="approx")

    ERA("thonburi", "Thonburi Kingdom", "southeast-asia.mainland", 1767, 1782,
        "intermediate",
        summary="Fifteen years under Taksin, between the Burmese sack of Ayutthaya and "
                "the founding of the Chakri dynasty.")

    ERA("lan-xang", "Lan Xang", "southeast-asia.mainland", 1353, 1707, "foundational",
        native="ລ້ານຊ້າງ",
        summary="Lao kingdom of the middle Mekong, which broke into three rival "
                "successor kingdoms.",
        date_note="Divided into Vientiane, Luang Phrabang and Champasak. Accounts differ "
                  "on whether the break-up dates from 1694 or 1707.",
        source_ids=[S_BRIT_LAOS, S_WIKI_LANXANG],
        alternatives=[{"label": "1694, dating the split from the succession crisis",
                       "standing": "minority", "end_year": 1694,
                       "source_ids": [S_BRIT_LAOS]}])

    # ── sources for what was already there ────────────────────────────────
    enrich("southeast-asia.mainland.funan",
           source_ids=[S_EBSCO_FUNAN],
           date_note="Funan is what Chinese sources called it; no indigenous name is "
                     "attested. Whether it was a unified kingdom at all is disputed, "
                     "notably by Michael Vickery, who read the Chinese accounts as "
                     "describing a looser set of polities.",
           caveats=[{"kind": "naming-confusion",
                     "text": "A Chinese exonym. What the polity called itself is unknown.",
                     "source_ids": [S_EBSCO_FUNAN]},
                    {"kind": "contested-existence",
                     "text": "Its existence as a single state is questioned; the evidence "
                             "may describe several polities.",
                     "source_ids": [S_EBSCO_FUNAN]}])

    enrich("southeast-asia.mainland.khmer",
           source_ids=[S_WIKI_KHMER],
           date_note="Dated from the consecration of Jayavarman II in 802 to the "
                     "Ayutthayan capture of Angkor in 1431. Both ends are conventional "
                     "markers: Khmer kingship neither began nor ended in a single year.")

    enrich("southeast-asia.mainland.champa",
           source_ids=[S_WIKI_CHAMPA, S_BRIT_CHAMPA],
           native_name="Campā",
           date_note="Champa was a confederation of polities -- Indrapura, Amaravati, "
                     "Vijaya, Kauthara, Panduranga -- rather than one continuous "
                     "kingdom, and it ended in stages: Vijaya fell in 1471, Kauthara was "
                     "annexed in 1653, and Panduranga in 1832, which is the conventional "
                     "end date used here.",
           caveats=[{"kind": "contested-existence",
                     "text": "Usually written as one kingdom, but scholarship treats it "
                             "as a confederation of polities sharing a culture.",
                     "source_ids": [S_WIKI_CHAMPA]},
                    {"kind": "naming-confusion",
                     "text": "Campā is attested as a self-designation. Lin-yi and Chiêm "
                             "Thành are Chinese and Vietnamese names for it.",
                     "source_ids": [S_WIKI_CHAMPA]}],
           name_forms=[{"name": "Campā", "kind": "endonym",
                        "source_ids": [S_WIKI_CHAMPA]},
                       {"name": "Lin-yi", "kind": "exonym", "lang": "zh",
                        "source_ids": [S_WIKI_CHAMPA]},
                       {"name": "Chiêm Thành", "kind": "exonym", "lang": "vi",
                        "source_ids": [S_WIKI_CHAMPA]}])

    enrich("southeast-asia.mainland.ayutthaya",
           name_forms=[{"name": "Siam", "kind": "exonym",
                        "note": "The name outsiders used. Not the kingdom's name for "
                                "itself.",
                        "source_ids": [S_BRIT_SUKHOTHAI]}])

    # ── Vietnam: narrow the name, then supply the sequence ────────────────
    # The existing node claimed Đại Việt for 939-1804. It becomes the 1054-1400
    # state it actually names; everything else gets its own entity under a
    # container, and the rejected over-broad span is recorded as such.
    dv = by_id.get("southeast-asia.mainland.vietnam")
    if dv is not None:
        dv["name"] = "Vietnam (dynastic)"
        dv["native_name"] = "Việt Nam"
        dv["start_year"] = 939
        dv["end_year"] = 1945
        dv["tier"] = "foundational"
        dv["summary"] = ("Independent Vietnamese states from the end of Chinese rule to "
                         "the abdication of the last emperor.")
        dv["date_note"] = (
            "A container, not a polity. It previously stood as a single entity named Đại "
            "Việt covering 939-1804, which was wrong twice over: it flattened eight "
            "dynasties into one node, and Đại Việt was not the state's name for most of "
            "that time. The name applied 1054-1400 and 1428-1804; in between the state "
            "was Đại Cồ Việt, then Đại Ngu, then a Ming province.")
        dv["source_ids"] = [S_WIKI_DAIVIET]
        dv["name_forms"] = [
            {"name": "Đại Việt", "kind": "historical", "lang": "vi",
             "from": 1054, "to": 1804,
             "note": "The name in two separate stretches, 1054-1400 and 1428-1804 -- not "
                     "continuously.",
             "source_ids": [S_WIKI_DAIVIET, S_WIKI_LYTHANHTONG]},
            {"name": "Đại Cồ Việt", "kind": "historical", "lang": "vi",
             "from": 968, "to": 1054, "source_ids": [S_WIKI_DINH]},
            {"name": "Đại Ngu", "kind": "historical", "lang": "vi",
             "from": 1400, "to": 1407,
             "note": "The Hồ dynasty's name for the state.",
             "source_ids": [S_WIKI_HO]},
            {"name": "Đại Việt, 939-1804", "kind": "rejected",
             "note": "This dataset's earlier single span. The name did not apply before "
                     "1054 and lapsed twice.",
             "source_ids": [S_WIKI_DAIVIET]},
        ]
        dv.pop("aliases", None)

    V = "southeast-asia.mainland.vietnam"
    P("ngo", "Ngô Dynasty", V, 939, 965, "intermediate",
      summary="Founded after Bạch Đằng ended Chinese rule; collapsed into a period of "
              "warlords.",
      date_note="Sources give 965 or 968 for the end, depending on whether the "
                "interregnum of the twelve warlords is counted as part of the dynasty.",
      source_ids=[S_WIKI_NGO],
      alternatives=[{"label": "968, counting the interregnum", "standing": "minority",
                     "end_year": 968, "source_ids": [S_WIKI_NGO]}])
    P("dinh", "Đinh Dynasty", V, 968, 980, "intermediate",
      native="大瞿越",
      summary="Declared the state Đại Cồ Việt and an imperial title to match.",
      source_ids=[S_WIKI_DINH])
    P("early-le", "Early Lê Dynasty", V, 980, 1009, "intermediate",
      summary="Repelled a Song invasion, then gave way to the Lý.",
      source_ids=[S_WIKI_LE])
    P("ly", "Lý Dynasty", V, 1009, 1225, "foundational",
      summary="Two centuries of consolidation; renamed the state Đại Việt in 1054.",
      date_note="The traditional account of the 1054 renaming has itself been "
                "questioned. Sources give 1225 or 1226 for the handover to the Trần.",
      source_ids=[S_BRIT_LYTHAITO, S_WIKI_LYTHANHTONG])
    P("tran", "Trần Dynasty", V, 1225, 1400, "foundational",
      summary="Repelled three Mongol invasions.",
      source_ids=[S_BRIT_TRAN])
    P("ho", "Hồ Dynasty", V, 1400, 1407, "intermediate",
      native="大虞",
      summary="Seven years of forced reform; renamed the state Đại Ngu and fell to the "
              "Ming.",
      source_ids=[S_WIKI_HO])
    P("ming-occupation", "Ming Occupation", V, 1407, 1427, "intermediate",
      summary="Administered by the Ming as the province of Jiaozhi, not as a Vietnamese "
              "state at all.",
      date_note="Ended by Lê Lợi's rising; the Lê dynasty dates from 1428.",
      source_ids=[S_WIKI_FOURTH_DOM],
      name_forms=[{"name": "Jiaozhi", "kind": "exonym", "lang": "zh",
                   "note": "The Ming province name. The period is also called the fourth "
                           "Chinese domination.",
                   "source_ids": [S_WIKI_FOURTH_DOM]}])
    P("later-le", "Later Lê Dynasty", V, 1428, 1789, "foundational",
      summary="Nominally ruled for three and a half centuries, though for most of them "
              "real power lay with the Trịnh and Nguyễn lords.",
      date_note="The Lê emperors became figureheads after 1533. The Trịnh-Nguyễn "
                "division that actually governed the country is not yet modelled here.",
      source_ids=[S_WIKI_LE])
    P("mac", "Mạc Dynasty", V, 1527, 1592, "intermediate",
      summary="Usurped the throne and held the north, overlapping the Lê rather than "
              "succeeding them.",
      date_note="Driven from the capital in 1592; a rump state survived in the far north "
                "until 1677. Deliberately overlaps the Later Lê, because both claimed "
                "legitimacy at once.",
      source_ids=[S_WIKI_MAC],
      allow_outside_parent_dates=True)
    P("tay-son", "Tây Sơn Dynasty", V, 1778, 1802, "intermediate",
      summary="A rising from the south that swept away the Trịnh, the Nguyễn lords and "
              "the Lê, and repelled a Qing invasion.",
      source_ids=[S_BRIT_TAYSON, S_WIKI_TAYSON])
    P("nguyen", "Nguyễn Dynasty", V, 1802, 1945, "foundational",
      native="Việt Nam",
      summary="The last dynasty; adopted the name Việt Nam, then ruled under French "
              "protection from the 1880s.",
      source_ids=[S_WIKI_FRINDOCHINA],
      name_forms=[{"name": "Việt Nam", "kind": "formal", "lang": "vi", "from": 1804,
                   "source_ids": [S_WIKI_DAIVIET]}])
    ERA("french-indochina", "French Indochina", "southeast-asia.mainland", 1887, 1954,
        "foundational",
        summary="The colonial union of Vietnamese, Cambodian and Lao territories.",
        date_note="Formed in 1887 and dissolved in 1954 after Dien Bien Phu and the "
                  "Geneva agreements.",
        source_ids=[S_WIKI_FRINDOCHINA])

    print("SE Asia mainland: Burma sequence, Thai and Lao states, Vietnamese dynasties")
