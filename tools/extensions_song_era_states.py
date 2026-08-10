"""The three states that ruled northern China while the Song ruled the south.

The dataset already split the Song into Northern (960-1127) and Southern
(1127-1279) but contained none of the polities that caused the split. The
Southern Song exists because the Jurchen Jin took Kaifeng in 1127 and carried off
two emperors; without the Jin in the data, a reader saw the consequence with the
cause deleted. Liao, Jin and Western Xia held the north for most of the Song
period, and their absence made the Song look like the sole government of China
for three centuries when it never was.

**Traditional historiography supports treating them as dynasties**, not as
foreign intrusions: the Yuan commissioned official histories of Liao, Jin and Song
as three parallel legitimate states. Western Xia notably got no official history,
which is a fact about the historiography rather than about the state, and is
recorded as such.

**Liao carries two founding dates, and both are kept.** 907 is the traditional
date and the one Britannica leads with, when Yelü Abaoji became khagan; 916 is
when he proclaimed himself emperor in the Chinese style, and Chinese scholarship
generally prefers it. The dataset uses 907 because it is the date a reader
arrives with, and records 916 as a sourced alternative. The disagreement is not
an error to resolve -- a Shandong University study argues the *Liaoshi*'s own use
of 907 was deliberate rather than mistaken.

**The Xia is a different problem and gets different treatment.** It is not
included as an established polity, because whether it existed is genuinely
disputed: Britannica calls it legendary, the Cambridge History of Ancient China
begins with the Shang, and the state-sponsored Xia-Shang-Zhou Chronology Project
assigns it 2070-1600 BCE and identifies it with Erlitou -- a project whose method
drew sustained criticism in Western sinology. So it is entered with a
`contested-existence` caveat carrying both positions, in the same shape used for
the ROC. This also makes "Hsia" findable, which was the original complaint.

One thing deliberately not done: the Qara Khitai (Western Liao, 1124-1218) is
mentioned in the Liao's note but not authored as an entity. It is a Central Asian
successor state rather than a Chinese one, and placing it correctly needs the same
care the multi-regional pass took, not a hurried child node.
"""

S_BRIT_LIAO = "britannica-liao-dynasty"
S_SDU_LIAO = "sdu-liao-chronology"
S_BERK_LIAO = "berkshire-liao-dynasty"
S_BRIT_JIN_J = "britannica-jin-dynasty-jurchen"
S_WIKI_JINGKANG = "wikipedia-jingkang-incident"
S_BRIT_JINGKANG = "britannica-jingkang-incident"
S_BRIT_XIXIA = "britannica-xi-xia"
S_BRIT_LIYUANHAO = "britannica-li-yuanhao"
S_CK_XIXIA = "chinaknowledge-xixia"
S_BRIT_XIA = "britannica-xia-dynasty"
S_CAM_ANCIENT = "cambridge-history-ancient-china"
S_XSZ_PROJECT = "wikipedia-xia-shang-zhou-chronology-project"
S_XIA_WIKI = "wikipedia-xia-dynasty-romanisation"

SONG_ERA_SOURCES = [
    {"id": S_BRIT_LIAO, "kind": "reference",
     "citation": "'Liao dynasty', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Liao-dynasty",
     "note": "'Traditionally, the start of the Liao period is given as 907, the last "
             "year of the Tang', while noting Chinese historians often prefer 916. "
             "Also: 'The Liao dynasty was destroyed in 1125 by the Juchen tribes.'"},
    {"id": S_SDU_LIAO, "kind": "scholarly",
     "citation": "Shandong University, study of Liao dynastic chronology",
     "url": "https://www.lhp.sdu.edu.cn/__local/C/16/CF/EADF85A008182C64BAE7A905CC6_F35AACA5_2BB5F.pdf",
     "note": "Argues scholarship agrees Abaoji proclaimed the dynasty in 916, and that "
             "the Liaoshi's use of 907 was a deliberate choice rather than an error."},
    {"id": S_BERK_LIAO, "kind": "reference",
     "citation": "'Liao Dynasty (907-1125)', Berkshire Encyclopedia of China",
     "url": "https://www.berkshirepublishing.com/ecph-china/2018/01/08/liao-dynasty-907-1125/",
     "note": "Frames 907 and 916 as two counting conventions rather than a factual "
             "dispute."},
    {"id": S_BRIT_JIN_J, "kind": "reference",
     "citation": "'Jin dynasty (1115-1234)', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Jin-dynasty-China-Mongolia-1115-1234",
     "note": "Gives the Jurchen dynasty's Wade-Giles form as Chin, identical to the "
             "earlier Jin (晉)."},
    {"id": S_WIKI_JINGKANG, "kind": "reference",
     "citation": "'Jingkang incident', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Jingkang_incident",
     "note": "The 1127 sack of Kaifeng and capture of Huizong and Qinzong, and the "
             "flight south that established the Southern Song under Gaozong."},
    {"id": S_BRIT_JINGKANG, "kind": "reference",
     "citation": "'Jingkang Incident', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/event/Jingkang-Incident-1126-1127",
     "note": "Dates the incident across 1126-1127."},
    {"id": S_BRIT_XIXIA, "kind": "reference",
     "citation": "'Xi Xia', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Xi-Xia",
     "note": "The Tangut state, and its destruction by the Mongols in 1227."},
    {"id": S_BRIT_LIYUANHAO, "kind": "reference",
     "citation": "'Li Yuanhao', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/biography/Li-Yuanhao",
     "note": "Declared himself emperor in 1038, the conventional founding of Western Xia."},
    {"id": S_CK_XIXIA, "kind": "reference",
     "citation": "'The Western Xia dynasty', ChinaKnowledge.de",
     "url": "http://www.chinaknowledge.de/History/Song/xixia.html",
     "note": "Background on the Tangut state and its script."},
    {"id": S_BRIT_XIA, "kind": "reference",
     "citation": "'Xia dynasty', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Xia-dynasty",
     "note": "Treats the Xia as legendary rather than as an established dynasty."},
    {"id": S_CAM_ANCIENT, "kind": "scholarly",
     "citation": "The Cambridge History of Ancient China",
     "url": "https://www.cambridge.org/core/books/cambridge-history-of-ancient-china/1274DEAA9CE3A6D0AC700076B70D5C22",
     "note": "Begins its historical treatment with the Shang rather than the Xia."},
    {"id": S_XSZ_PROJECT, "kind": "reference",
     "citation": "'Xia-Shang-Zhou Chronology Project', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Xia%E2%80%93Shang%E2%80%93Zhou_Chronology_Project",
     "note": "The state-sponsored project assigning the Xia 2070-1600 BCE and "
             "identifying it with Erlitou, and the substantial Western criticism of "
             "its method."},
]


def extend(E, entities):
    from builders import make_builders

    by_id = {e["id"]: e for e in entities}
    _, _, C_ERA, _, _, _ = make_builders(E, id_prefix="east-asia.china")

    # ---------------------------------------------------------------- Liao
    C_ERA("liao", "Liao Dynasty", "east-asia.china", 907, 1125, "foundational",
          native_name="遼朝",
          summary="Khitan empire ruling Manchuria, Mongolia and the northern edge of "
                  "the North China Plain, governed through separate steppe and Chinese "
                  "administrations.",
          date_note="Two founding dates are both defensible and both in use. 907 is "
                    "traditional and the year Yelü Abaoji became khagan; 916 is when he "
                    "proclaimed himself emperor in the Chinese manner, which most "
                    "Chinese scholarship prefers. A Shandong University study argues "
                    "the Liaoshi's own use of 907 was deliberate rather than an error. "
                    "Ended 1125 when Jurchen forces captured Emperor Tianzuo.",
          # The schema's `traditional` standing exists for exactly this: 907 is a
          # received counting convention, 916 is what most scholarship argues.
          # The dataset leads with 907 because it is the date a reader arrives
          # with, and says plainly that it is the traditional one.
          alternatives=[
              {"label": "916, the imperial proclamation", "standing": "majority",
               "start_year": 916,
               "note": "When Abaoji took the title huangdi, proclaimed an era name and "
                       "built a Confucian temple.",
               "source_ids": [S_SDU_LIAO, S_BERK_LIAO]},
              {"label": "907, the traditional date", "standing": "traditional",
               "start_year": 907,
               "note": "The Liaoshi's own date, which Britannica leads with.",
               "source_ids": [S_BRIT_LIAO]},
          ],
          source_ids=[S_BRIT_LIAO, S_SDU_LIAO, S_BERK_LIAO],
          name_forms=[
              {"name": "Khitan Empire", "kind": "historical",
               "note": "The founding state was the Great Khitan State, 大契丹; the "
                       "Chinese-style dynastic name came later.",
               "source_ids": [S_BRIT_LIAO]},
          ],
          cross_parent_ids=["central-asia"],
          allow_outside_parent_dates=True)

    # ------------------------------------------------------- Jurchen Jin
    # Deliberately NOT merged with east-asia.china.jin (晉, 266-420). Different
    # characters, different people, nine centuries apart -- and Wade-Giles calls
    # both of them Chin, which is precisely why both need their characters.
    C_ERA("jin-jurchen", "Jin Dynasty (Jurchen)", "east-asia.china", 1115, 1234,
          "foundational",
          native_name="金",
          summary="Jurchen empire that took northern China from the Song, ruling from "
                  "Kaifeng until the Mongol conquest.",
          date_note="Founded 1115 by Wanyan Aguda; ended with the fall of Caizhou in "
                    "February 1234 under Mongol attack. Distinct from the earlier Jin "
                    "(晉, 266-420) despite the identical English spelling.",
          source_ids=[S_BRIT_JIN_J],
          name_forms=[
              {"name": "Chin", "kind": "scholarly", "lang": "en", "to": 1982,
               "note": "Wade-Giles renders this dynasty and the earlier Jin (晉) "
                       "identically, so the older romanisation cannot tell them apart.",
               "source_ids": [S_BRIT_JIN_J]},
              {"name": "Jurchen Jin", "kind": "common",
               "note": "Used in English to separate it from the Jin of 266-420.",
               "source_ids": [S_BRIT_JIN_J]},
          ],
          cross_parent_ids=["central-asia"],
          allow_outside_parent_dates=True)

    # The event the dataset was missing: the reason Northern Song ends and
    # Southern Song begins. Placed under the Jin that carried it out and
    # cross-linked to the Northern Song it ended, so it is reachable from either.
    C_ERA("jin-jurchen.jingkang", "Jingkang Incident", "east-asia.china.jin-jurchen",
          1126, 1127, "foundational",
          summary="Jin forces sacked Kaifeng and carried off emperors Huizong and "
                  "Qinzong, ending the Northern Song.",
          date_note="Britannica dates the incident across 1126-1127. The surviving "
                    "prince fled south and took the throne as Gaozong, which is why "
                    "this dataset's Song splits at 1127.",
          source_ids=[S_WIKI_JINGKANG, S_BRIT_JINGKANG],
          cross_parent_ids=["east-asia.china.song.northern"],
          allow_outside_parent_dates=True)

    # -------------------------------------------------------- Western Xia
    C_ERA("western-xia", "Western Xia", "east-asia.china", 1038, 1227, "foundational",
          native_name="西夏",
          summary="Tangut state in the northwest, with its own script and no official "
                  "dynastic history.",
          date_note="Founded 1038 when Li Yuanhao declared himself emperor, though "
                    "Tangut autonomy in the region long predates that. Destroyed by the "
                    "Mongols in 1227, the year Genghis Khan died. Unlike Liao, Jin and "
                    "Song, it received no official history from the Yuan, which is a "
                    "fact about the historiography rather than about the state.",
          source_ids=[S_BRIT_XIXIA, S_BRIT_LIYUANHAO, S_CK_XIXIA],
          name_forms=[
              {"name": "Xi Xia", "kind": "scholarly",
               "note": "The form Britannica files it under.",
               "source_ids": [S_BRIT_XIXIA]},
              {"name": "Tangut Empire", "kind": "common",
               "source_ids": [S_CK_XIXIA]},
          ],
          allow_outside_parent_dates=True)

    # ---------------------------------------------------------------- Xia
    # Entered because readers search Hsia and Xia and should find something --
    # but entered as a dispute, not as a polity. The existing Erlitou node is the
    # archaeology; whether the archaeology is the Xia is the argument.
    C_ERA("xia", "Xia Dynasty", "east-asia.china", -2070, -1600, "foundational",
          native_name="夏朝",
          summary="Traditionally the first Chinese dynasty. Whether it existed as a "
                  "state is disputed.",
          date_note="The 2070-1600 BCE span comes from the state-sponsored "
                    "Xia-Shang-Zhou Chronology Project, which identifies the Xia with "
                    "the Erlitou culture. Those dates should be read as that project's "
                    "position rather than as an established chronology; Britannica "
                    "treats the dynasty as legendary and the Cambridge History of "
                    "Ancient China begins with the Shang.",
          source_ids=[S_BRIT_XIA, S_CAM_ANCIENT, S_XSZ_PROJECT],
          caveats=[
              {"kind": "contested-existence",
               "text": "Britannica describes the Xia as legendary, and the Cambridge "
                       "History of Ancient China starts its account at the Shang.",
               "source_ids": [S_BRIT_XIA, S_CAM_ANCIENT]},
              {"kind": "contested-existence",
               "text": "The Xia-Shang-Zhou Chronology Project assigns the Xia "
                       "2070-1600 BCE and identifies every Erlitou phase with it. Its "
                       "method drew sustained criticism in Western sinology.",
               "source_ids": [S_XSZ_PROJECT]},
          ],
          name_forms=[
              {"name": "Hsia", "kind": "scholarly", "lang": "en", "to": 1982,
               "source_ids": [S_XIA_WIKI]},
          ],
          allow_outside_parent_dates=True)

    print("Song-era states: Liao, Jurchen Jin, Western Xia, Xia, Jingkang Incident")


def fix_tiers(E, entities):
    """The Sui was hidden at the default tier while the Liao was not.

    Adding Liao, Jurchen Jin and Western Xia as foundational exposed an existing
    inconsistency rather than creating one: the Sui, which reunified China after
    almost four centuries of division, was `intermediate` and therefore invisible
    at the default tier, while conquest dynasties holding half the country were
    about to become visible. A reader at Standard tier would have met the Liao
    before the Sui.

    Only the unambiguous case is changed here. The Jin of 266-420, the Northern
    and Southern Dynasties, and the Five Dynasties are also arguably mis-tiered --
    the Five Dynasties sits at `specialist`, so the interregnum between Tang and
    Song is invisible by default and the two look adjacent -- but those are
    genuine editorial judgements about how much division a default view should
    show, and they are recorded as an open question instead of being decided here.
    """
    by_id = {e["id"]: e for e in entities}
    sui = by_id.get("east-asia.china.sui")
    if sui is not None and sui.get("tier") == "intermediate":
        sui["tier"] = "foundational"
        # The promotion immediately failed validation for having no summary,
        # which is the useful part: the entity had been invisible at the default
        # tier, so nothing ever demanded one. Promoting it exposed the gap the
        # same moment it created the obligation.
        sui.setdefault(
            "summary",
            "Reunified China after nearly four centuries of division and built the "
            "Grand Canal, at ruinous cost, in two generations.",
        )
        print("Tiers: promoted the Sui to foundational (it reunified China)")
