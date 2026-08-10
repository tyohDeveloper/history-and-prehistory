"""Iran between the Sasanians and the Safavids: an 850-year hole.

The Iran branch ran from the Sasanian collapse in 651 straight to the Safavids in
1501, skipping the whole Islamic medieval period. The gap report found it.

**Part of the hole was an artefact of filing, not of missing data.** The Seljuks,
the Ilkhanate, the Timurids, the Khwarazmians and the Samanids were all already in
the dataset -- filed under Central Asia. An Iranian reader could not see them,
even though the Seljuk capitals were Nishapur, Ray, Isfahan and Hamadan, and every
Ilkhanid capital was in Iran. So this pass cross-links as much as it authors, which
is what the multi-regional machinery was built for.

**The cross-links are graded, not binary**, because the research came back graded:

* Seljuk, Ilkhanate, Khwarazmian, Samanid -- straightforwardly Iranian, linked.
* Ghaznavid -- held Khorasan and briefly Ray and Hamadan, then lost them at
  Dandanaqan in 1040 and became an Afghan and north Indian power. Linked, with the
  time limit stated.
* Timurid -- control over Iran was loose and only under Shah Rokh, per
  Britannica's own hedged framing. Linked, with the hedge recorded rather than
  quietly dropped.

Getting this wrong is possible in two directions, and only one of them is
visible: claiming a Central Asian dynasty ruled Iran is a false statement, while
hiding dynasties that plainly governed Iran is a silent omission. The second is
what the dataset was doing.

**"Iranian Intermezzo" is used as Britannica uses it**, as a section title for the
native Iranian dynasties between Arab and Turkic rule -- not invented here.
"""

S_IRANICA_TAHIRID = "iranica-tahirids"
S_BRIT_TAHIRID = "britannica-tahirid-dynasty"
S_BRIT_SAFFARID = "britannica-saffarid-dynasty"
S_BRIT_BUYID = "britannica-buyid-dynasty"
S_BRIT_INTERMEZZO = "britannica-iranian-intermezzo"
S_IRANICA_QARAQOYUNLU = "iranica-qara-qoyunlu"
S_IRANICA_AQQOYUNLU = "iranica-aq-qoyunlu"
S_BRIT_YAZDEGERD = "britannica-yazdegerd-iii"
S_BRIT_IRAN_ISLAMIC = "britannica-iran-islamic-conquest"
S_BRIT_ZAND = "britannica-zand-dynasty"
S_IRANICA_ZAND = "iranica-zand-dynasty"
S_WIKI_AFSHARID = "wikipedia-afsharid-dynasty"
S_WIKI_IRAN_MONARCHS = "wikipedia-list-monarchs-iran"

IRAN_ISLAMIC_SOURCES = [
    {"id": S_BRIT_YAZDEGERD, "kind": "reference",
     "citation": "'Yazdegerd III', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/biography/Yazdegerd-III",
     "note": "His death in 651 is the conventional end of the Sasanian empire."},
    {"id": S_BRIT_IRAN_ISLAMIC, "kind": "reference",
     "citation": "'Iran: The advent of Islam', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Iran/The-advent-of-Islam",
     "note": "The Arab conquest, with Nahavand in 642 as the decisive engagement."},
    {"id": S_BRIT_INTERMEZZO, "kind": "reference",
     "citation": "'Iran: The Iranian intermezzo', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Iran/The-Iranian-intermezzo",
     "note": "Britannica's own section title for the native Iranian dynasties of "
             "roughly 821-1055, between Arab and Turkic rule."},
    {"id": S_IRANICA_TAHIRID, "kind": "reference",
     "citation": "'Tahirids', Encyclopaedia Iranica",
     "url": "https://iranicaonline.org/articles/tahirids",
     "note": "821-873, governing Khorasan from Nishapur under nominal Abbasid authority."},
    {"id": S_BRIT_TAHIRID, "kind": "reference",
     "citation": "'Tahirid dynasty', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Tahirid-dynasty",
     "note": "Displaced by the Saffarids."},
    {"id": S_BRIT_SAFFARID, "kind": "reference",
     "citation": "'Saffarid dynasty', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Saffarid-dynasty",
     "note": "Rose from Sistan in 861; its end is dated 1002 or 1003 with the Ghaznavid "
             "conquest."},
    {"id": S_BRIT_BUYID, "kind": "reference",
     "citation": "'Buyid dynasty', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Buyid-dynasty",
     "note": "Shia dynasty that took Baghdad in 945 and held the Abbasid caliphs as "
             "figureheads."},
    {"id": S_IRANICA_QARAQOYUNLU, "kind": "reference",
     "citation": "'Qara Qoyunlu', Encyclopaedia Iranica",
     "url": "https://iranicaonline.org/articles/qara-qoyunlu",
     "note": "Turkoman confederation, defeated by the Aq Qoyunlu in 1468."},
    {"id": S_BRIT_ZAND, "kind": "reference",
     "citation": "'Zand dynasty', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Zand-dynasty",
     "note": "Dates the dynasty 1750-79, against Encyclopaedia Iranica's 1751-94. "
             "Notes Karim Khan never claimed the title shahanshah, ruling as vakil for "
             "a Safavid figurehead."},
    {"id": S_IRANICA_ZAND, "kind": "reference",
     "citation": "'Zand dynasty', Encyclopaedia Iranica",
     "url": "https://www.iranicaonline.org/articles/zand-dynasty/",
     "note": "1751-94, ruling Persia excluding Khorasan from Shiraz, until the Qajar "
             "founding."},
    {"id": S_WIKI_AFSHARID, "kind": "reference",
     "citation": "'Afsharid dynasty', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Afsharid_dynasty",
     "note": "Founded 1736 by Nader Shah on deposing Abbas III; the line continued in "
             "Khorasan after his assassination in 1747."},
    {"id": S_WIKI_IRAN_MONARCHS, "kind": "reference",
     "citation": "'List of monarchs of Iran', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/List_of_monarchs_of_Iran",
     "note": "Gives the Afsharids 1736-1796 and the Zand 1751-1794, and states plainly "
             "that the two competed for supremacy rather than succeeding one another."},
    {"id": S_IRANICA_AQQOYUNLU, "kind": "reference",
     "citation": "'Aq Qoyunlu', Encyclopaedia Iranica",
     "url": "https://iranicaonline.org/articles/aq-qoyunlu-confederation",
     "note": "Held western Iran until Ismail I took Tabriz in 1501, founding the "
             "Safavid state."},
]

# Entities already in the dataset that also belong to Iran, with the qualification
# each one needs. A bare cross-link would assert more than the sources support.
IRAN_REACH = {
    "central-asia.seljuk": None,
    "central-asia.samanid": None,
    "central-asia.khwarazmian": None,
    "central-asia.mongol-empire.ilkhanate": None,
    "central-asia.ghaznavid":
        "Held Khorasan, and briefly Ray and Hamadan, until Dandanaqan in 1040. After "
        "that it was an Afghan and north Indian power rather than an Iranian one.",
    "central-asia.timurid":
        "Control over Iran was loose and effectively limited to the reign of Shah Rokh; "
        "Britannica's own framing is hedged.",
    # The caliphates governed Iran outright between the Sasanians and the
    # Tahirids, but were reachable only from Arabia, Mesopotamia and Central
    # Asia -- so the Iran branch showed 651-821 as empty when it was merely
    # filed elsewhere. The gap report caught this on the pass that closed the
    # larger hole, which is the argument for re-running it after every change
    # rather than once.
    "global.multi-regional.rashidun": None,
    "global.multi-regional.umayyad": None,
    "global.multi-regional.abbasid": None,
}


def extend(E, entities):
    from builders import make_builders

    by_id = {e["id"]: e for e in entities}
    _, _, ERA, EVENT, _, _ = make_builders(E, id_prefix="west-asia.iran")
    IRAN = "west-asia.iran"

    EVENT("arab-conquest", "Arab Conquest of Iran", IRAN, 633, 651, "foundational",
          summary="Eighteen years that ended the Sasanian empire and began the Islamic "
                  "period in Iran.",
          date_note="Nahavand in 642 was the decisive engagement; the conventional end "
                    "is the death of the last Sasanian king, Yazdegerd III, in 651.",
          source_ids=[S_BRIT_IRAN_ISLAMIC, S_BRIT_YAZDEGERD])

    ERA("intermezzo", "The Iranian Intermezzo", IRAN, 821, 1055, "foundational",
        summary="Native Iranian dynasties ruling between Arab and Turkic domination.",
        date_note="Not a coinage of this dataset: Britannica uses 'the Iranian "
                  "intermezzo' as a section heading for this period. It is a framing "
                  "rather than a polity, and the dynasties inside it overlapped and "
                  "fought each other.",
        source_ids=[S_BRIT_INTERMEZZO])

    ERA("tahirid", "Tahirid Dynasty", "west-asia.iran.intermezzo", 821, 873,
        "intermediate",
        summary="Governed Khorasan from Nishapur, nominally for the Abbasids and in "
                "practice for themselves.",
        source_ids=[S_IRANICA_TAHIRID, S_BRIT_TAHIRID])
    ERA("saffarid", "Saffarid Dynasty", "west-asia.iran.intermezzo", 861, 1003,
        "intermediate",
        summary="Rose from Sistan under a coppersmith turned warlord and briefly "
                "threatened Baghdad itself.",
        date_note="The end is given as 1002 or 1003, with the Ghaznavid conquest.",
        source_ids=[S_BRIT_SAFFARID],
        allow_outside_parent_dates=True)
    ERA("buyid", "Buyid Dynasty", "west-asia.iran.intermezzo", 934, 1062, "foundational",
        summary="Shia dynasty from the Caspian highlands that took Baghdad and ruled "
                "through the Abbasid caliphs it kept as figureheads.",
        date_note="Entered Baghdad in 945. The arrangement left the caliphate intact as "
                  "an institution while removing its power, which is why the Abbasid "
                  "line continues past this point in the dataset.",
        source_ids=[S_BRIT_BUYID],
        allow_outside_parent_dates=True)

    ERA("qara-qoyunlu", "Qara Qoyunlu", IRAN, 1374, 1468, "intermediate",
        summary="Turkoman confederation holding Azerbaijan and western Iran.",
        source_ids=[S_IRANICA_QARAQOYUNLU])
    ERA("aq-qoyunlu", "Aq Qoyunlu", IRAN, 1378, 1501, "intermediate",
        summary="Turkoman confederation that displaced the Qara Qoyunlu and was in turn "
                "displaced by the Safavids.",
        date_note="Ended when Ismail I took Tabriz in 1501, which is also the Safavid "
                  "founding: one event, two entries.",
        source_ids=[S_IRANICA_AQQOYUNLU])

    # The 53 years between the Safavid and Qajar entries were not empty; they
    # held two dynasties that ruled at the same time as each other. Nader Shah's
    # Afsharids kept Khorasan after his assassination while the Zand held
    # everything else from Shiraz, so these overlap deliberately, as the Mạc and
    # Lê do.
    ERA("afsharid", "Afsharid Dynasty", IRAN, 1736, 1796, "foundational",
        summary="Nader Shah's conquest state, which outlasted him only in Khorasan.",
        date_note="Founded in 1736 when Nader deposed the last Safavid. After his "
                  "assassination in 1747 the dynasty held only Khorasan, under his "
                  "grandson Shahrokh, until the Qajar victory in 1796.",
        source_ids=[S_WIKI_AFSHARID, S_WIKI_IRAN_MONARCHS])
    ERA("zand", "Zand Dynasty", IRAN, 1751, 1794, "foundational",
        summary="Ruled Iran except Khorasan from Shiraz, remembered for an unusually "
                "peaceful reign.",
        date_note="Encyclopaedia Iranica gives 1751-94; Britannica gives 1750-79, which "
                  "counts only Karim Khan's own rule. He never took the title "
                  "shahanshah, governing as vakil for a Safavid figurehead. Overlaps the "
                  "Afsharids, who held Khorasan throughout.",
        source_ids=[S_IRANICA_ZAND, S_BRIT_ZAND, S_WIKI_IRAN_MONARCHS],
        alternatives=[{"label": "1750-79, counting only Karim Khan's rule",
                       "standing": "minority", "start_year": 1750, "end_year": 1779,
                       "source_ids": [S_BRIT_ZAND]}])

    # ── make the already-present dynasties reachable from Iran ────────────
    linked = 0
    for eid, note in IRAN_REACH.items():
        e = by_id.get(eid)
        if e is None:
            continue
        e["cross_parent_ids"] = sorted(set(e.get("cross_parent_ids", [])) | {IRAN})
        if note is not None:
            e["date_note"] = (e.get("date_note", "") + " " + note).strip()
        linked += 1

    print(f"Islamic Iran: intermezzo and Turkoman states, {linked} dynasties "
          f"cross-linked to Iran")
