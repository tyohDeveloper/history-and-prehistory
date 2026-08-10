"""Central Asia and the steppe: the polities between the Kushans and the Mongols.

One branch of Central Asia ran from 1400 BCE to 1206 CE with nothing in it. The
gap report found it on its first run, which is what the report is for.

**A correction comes first.** The dataset carried a single "First Turkic
Khaganate, 552-744". Research shows that span conflates three distinct polities:
the first khaganate (552 to its division around 581-603), the Eastern and Western
khaganates that followed, and the *second* khaganate of 682-744 after a period of
Tang control. Calling all of it "First" and running it to 744 is not a rounding
choice, it is three states wearing one label. Corrected, with the second khaganate
authored separately.

**Two entities are deliberately not states.**

*Saka* is a Persian exonym for eastern Iranian steppe peoples, as Scythian is a
Greek one, and the two overlap without being simply identical. What these people
called themselves is not settled. So Saka is entered as a naming relationship to
the Scythians rather than as a separate empire with borders.

*Sogdia was never unified.* Multiple sources say plainly that no Sogdian kingdom
existed -- it was a set of city-states around Samarkand and Bukhara whose
merchants ran the Silk Road network. Authoring it as an empire would invent a
polity to fill a space, which is the failure this whole pass is meant to correct,
not repeat.

**Qara Khitai closes a gap left open two releases ago.** It was flagged when the
Liao was added and deliberately postponed because it needed the two-date
treatment; it gets it here. Chinese, Persian and Arab sources treat the Naiman
usurpation of 1211 as the dynastic end, while the state itself survived to 1218.
"""

S_IRANICA_SAKA = "iranica-saka"
S_BRIT_SAKA = "britannica-saka"
S_BRIT_SOGDIANA = "britannica-sogdiana"
S_IRANICA_SOGDIA = "iranica-sogdiana"
S_IRANICA_HEPHTHALITE = "iranica-hephthalites"
S_BRIT_HEPHTHALITE = "britannica-hephthalite"
S_BRIT_TURK = "britannica-turkic-peoples"
S_WIKI_SECOND_TURK = "wikipedia-second-turkic-khaganate"
S_BRIT_UYGHUR = "britannica-uyghur"
S_BRIT_GHAZNAVID = "britannica-ghaznavid-dynasty"
S_BRIT_KARAKHANID = "britannica-qarakhanid-dynasty"
S_BRIT_KHWARAZM = "britannica-khwarezm-shah-dynasty"
S_BRIT_BUKHARA = "britannica-khanate-of-bukhara"
S_BRIT_KHIVA = "britannica-khanate-of-khiva"
S_BRIT_KOKAND = "britannica-kokand"
S_BIRAN_QARAKHITAI = "biran-qara-khitai"
S_WIKI_QARAKHITAI = "wikipedia-qara-khitai"
S_BRIT_RUSSIAN_CA = "britannica-russian-conquest-central-asia"

CENTRAL_ASIA_MEDIEVAL_SOURCES = [
    {"id": S_IRANICA_SAKA, "kind": "reference",
     "citation": "'Saka', Encyclopaedia Iranica",
     "url": "https://iranicaonline.org/articles/saka-people",
     "note": "Saka is the Persian term for eastern Iranian steppe nomads; its relation "
             "to the Greek 'Scythian' is one of overlapping exonyms rather than "
             "identity."},
    {"id": S_BRIT_SAKA, "kind": "reference",
     "citation": "'Saka', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Saka",
     "note": "Treats the Saka as a branch of the wider Scythian world."},
    {"id": S_BRIT_SOGDIANA, "kind": "reference",
     "citation": "'Sogdiana', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Sogdiana",
     "note": "A region of city-states, not a unified kingdom."},
    {"id": S_IRANICA_SOGDIA, "kind": "reference",
     "citation": "'Sogdiana', Encyclopaedia Iranica",
     "url": "https://iranicaonline.org/articles/sogdiana-i-geography",
     "note": "No unified Sogdian state is attested; the cities acted independently."},
    {"id": S_IRANICA_HEPHTHALITE, "kind": "reference",
     "citation": "'Hephthalites', Encyclopaedia Iranica",
     "url": "https://iranicaonline.org/articles/hephthalites-a-people-of-central-asia",
     "note": "Their origin and whether the name covers one people or a confederation "
             "are both disputed."},
    {"id": S_BRIT_HEPHTHALITE, "kind": "reference",
     "citation": "'Hephthalite', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Hephthalite",
     "note": "The White Huns, defeated by a Turkic-Sasanian alliance around 560."},
    {"id": S_BRIT_TURK, "kind": "reference",
     "citation": "'Turkic peoples', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Turkic-peoples",
     "note": "The first khaganate and its division into eastern and western halves."},
    {"id": S_WIKI_SECOND_TURK, "kind": "reference",
     "citation": "'Second Turkic Khaganate', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Second_Turkic_Khaganate",
     "note": "682-744, re-established after a period of Tang control and ended by the "
             "Uyghurs."},
    {"id": S_BRIT_UYGHUR, "kind": "reference",
     "citation": "'Uyghur', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Uyghur",
     "note": "The khaganate of 744-840, ended by the Yenisei Kyrgyz sack of Ordu-Baliq."},
    {"id": S_BRIT_GHAZNAVID, "kind": "reference",
     "citation": "'Ghaznavid dynasty', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Ghaznavid-dynasty",
     "note": "977-1186, centred on Ghazna, and its loss of Khorasan at Dandanaqan in "
             "1040."},
    {"id": S_BRIT_KARAKHANID, "kind": "reference",
     "citation": "'Qarakhanid dynasty', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Qarakhanid-Dynasty",
     "note": "The first Turkic dynasty to adopt Islam; later split into eastern and "
             "western branches."},
    {"id": S_BRIT_KHWARAZM, "kind": "reference",
     "citation": "'Khwarezm-Shah dynasty', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Khwarezm-Shah-dynasty",
     "note": "Destroyed by the Mongols; Jalal al-Din's death in 1231 is the usual end."},
    {"id": S_BRIT_BUKHARA, "kind": "reference",
     "citation": "'Khanate of Bukhara', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Bukhara-khanate",
     "note": "Became an emirate in 1785 and a Russian protectorate in 1868."},
    {"id": S_BRIT_KHIVA, "kind": "reference",
     "citation": "'Khiva', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Khiva-khanate",
     "note": "Russian protectorate from 1873; abolished 1920."},
    {"id": S_BRIT_KOKAND, "kind": "reference",
     "citation": "'Kokand', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Kokand",
     "note": "Annexed by Russia in 1876. Its founding is dated 1709 or 1798 depending on "
             "whether the earlier principality counts."},
    {"id": S_BIRAN_QARAKHITAI, "kind": "scholarly",
     "citation": "Biran, 'The Qara Khitai', Oxford Research Encyclopedia of Asian History",
     "url": "http://mongol.huji.ac.il/sites/default/files/Biran%202020%20Qara%20Khitai%20Oxford%20Research%20Encyclopedia%20of%20Asian%20History.pdf",
     "note": "Modern scholarship dates the state's fall to 1218, against the traditional "
             "1211."},
    {"id": S_WIKI_QARAKHITAI, "kind": "reference",
     "citation": "'Qara Khitai', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Qara_Khitai",
     "note": "Chinese, Persian and Arab sources treat the Naiman usurpation of 1211 as "
             "the dynastic end."},
    {"id": S_BRIT_RUSSIAN_CA, "kind": "reference",
     "citation": "'Central Asia: Russian rule', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Central-Asia/Russian-rule",
     "note": "The conquest of the three khanates between 1865 and 1876."},
]


def extend(E, entities):
    from builders import make_builders

    by_id = {e["id"]: e for e in entities}
    _, _, ERA, _, _, _ = make_builders(E, id_prefix="central-asia")
    STEPPE, CORE = "central-asia.steppe", "central-asia.core"

    def enrich(eid, **fields):
        e = by_id.get(eid)
        if e is None:
            return
        for k, v in fields.items():
            e[k] = v

    # ── correction: one label was covering three polities ─────────────────
    enrich("central-asia.turkic-khaganate",
           name="First Turkic Khaganate",
           start_year=552, end_year=603,
           date_note="Previously recorded as 552-744, which ran three distinct states "
                     "together. The first khaganate divided into eastern and western "
                     "halves around 581-603; the Tang then absorbed the east; and a "
                     "second khaganate was established in 682. Only the first is dated "
                     "here.",
           source_ids=[S_BRIT_TURK])
    ERA("second-turkic-khaganate", "Second Turkic Khaganate", STEPPE, 682, 744,
        "intermediate",
        summary="Re-established Turkic power on the steppe after fifty years of Tang "
                "control, and left the Orkhon inscriptions.",
        date_note="Ended when the Uyghurs and their allies overthrew the last khagan.",
        source_ids=[S_WIKI_SECOND_TURK, S_BRIT_TURK])

    # ── naming, not statehood ─────────────────────────────────────────────
    ERA("saka", "Saka", STEPPE, -600, -100, "intermediate",
        summary="Eastern Iranian steppe peoples, known by the Persian name for them.",
        date_note="Saka is what the Persians called them and Scythian is what the Greeks "
                  "called a partly overlapping set of peoples. The two terms are not "
                  "interchangeable and neither is a self-designation; what these groups "
                  "called themselves is not settled. Entered as a people rather than a "
                  "state, because no unified Saka polity is attested.",
        source_ids=[S_IRANICA_SAKA, S_BRIT_SAKA],
        caveats=[{"kind": "naming-confusion",
                  "text": "A Persian exonym overlapping the Greek exonym Scythian. "
                          "Neither is what the people called themselves.",
                  "source_ids": [S_IRANICA_SAKA]}],
        name_forms=[{"name": "Saka", "kind": "exonym", "lang": "peo",
                     "note": "The Old Persian term.", "source_ids": [S_IRANICA_SAKA]}],
        date_precision="approx")

    # Not a kingdom. Sources say so directly, and inventing one to fill the
    # space is the exact error this pass exists to correct.
    ERA("sogdia", "Sogdia", CORE, -500, 750, "foundational",
        summary="City-states around Samarkand and Bukhara whose merchants ran the Silk "
                "Road network. Never politically unified.",
        date_note="No unified Sogdian kingdom is attested at any point: the cities acted "
                  "independently under a succession of outside overlords, Achaemenid to "
                  "Arab. The span marks the period of Sogdian cultural and commercial "
                  "prominence, not the reign of a state.",
        source_ids=[S_BRIT_SOGDIANA, S_IRANICA_SOGDIA],
        caveats=[{"kind": "contested-existence",
                  "text": "A region and a culture rather than a polity. There was no "
                          "Sogdian kingdom to have borders or a reign-list.",
                  "source_ids": [S_IRANICA_SOGDIA, S_BRIT_SOGDIANA]}],
        date_precision="approx")

    # ── the missing states ────────────────────────────────────────────────
    ERA("hephthalites", "Hephthalites", CORE, 440, 560, "intermediate",
        summary="Steppe power that dominated Bactria and pressed both Sasanian Iran and "
                "the Gupta empire.",
        date_note="Their origin, and whether the name covers a single people or a "
                  "confederation, are both disputed. Broken around 560 by a Turkic and "
                  "Sasanian alliance.",
        source_ids=[S_IRANICA_HEPHTHALITE, S_BRIT_HEPHTHALITE],
        caveats=[{"kind": "contested-existence",
                  "text": "Whether the Hephthalites were one people or a confederation "
                          "under one name is unresolved.",
                  "source_ids": [S_IRANICA_HEPHTHALITE]}],
        name_forms=[{"name": "White Huns", "kind": "exonym",
                     "note": "A Greek and Latin usage. Their relation to the Huns of "
                             "Europe is itself disputed.",
                     "source_ids": [S_BRIT_HEPHTHALITE]}],
        date_precision="approx")

    ERA("uyghur-khaganate", "Uyghur Khaganate", STEPPE, 744, 840, "foundational",
        summary="Steppe empire centred on Ordu-Baliq, and for a century the Tang "
                "dynasty's indispensable ally.",
        date_note="Ended when the Yenisei Kyrgyz sacked Ordu-Baliq in 840, scattering the "
                  "Uyghurs south and west.",
        source_ids=[S_BRIT_UYGHUR])

    ERA("ghaznavid", "Ghaznavid Empire", CORE, 977, 1186, "foundational",
        summary="Turkic dynasty ruling from Ghazna, whose raids into northern India "
                "opened the way for later Muslim rule there.",
        date_note="Lost Khorasan to the Seljuks at Dandanaqan in 1040 and was thereafter "
                  "an Afghan and north Indian power rather than an Iranian one.",
        source_ids=[S_BRIT_GHAZNAVID])

    ERA("kara-khanid", "Kara-Khanid Khanate", CORE, 840, 1212, "intermediate",
        summary="The first Turkic dynasty to adopt Islam, ruling Transoxiana and "
                "Kashgaria.",
        date_note="The founding date is uncertain and usually given as around 840. Split "
                  "into eastern and western branches, both eventually absorbed by the "
                  "Qara Khitai and then the Khwarazmians.",
        source_ids=[S_BRIT_KARAKHANID],
        date_precision="approx")

    ERA("khwarazmian", "Khwarazmian Empire", CORE, 1077, 1231, "foundational",
        summary="Briefly the dominant power from Transoxiana to western Iran, destroyed "
                "by the Mongol invasion.",
        date_note="Ends with the death of Jalal al-Din in 1231, some years after the "
                  "Mongols had broken the state itself.",
        source_ids=[S_BRIT_KHWARAZM])

    # Postponed when the Liao was added because it needed the two-date treatment.
    ERA("qara-khitai", "Qara Khitai", CORE, 1124, 1218, "intermediate",
        summary="Khitan successor state in Central Asia, founded by refugees from the "
                "fall of the Liao.",
        date_note="Chinese, Persian and Arab sources treat the Naiman usurpation of 1211 "
                  "as the end of the dynasty; modern scholarship generally dates the "
                  "state's fall to the Mongol conquest of 1218. Both are recorded.",
        source_ids=[S_BIRAN_QARAKHITAI, S_WIKI_QARAKHITAI],
        alternatives=[{"label": "1211, the Naiman usurpation", "standing": "traditional",
                       "end_year": 1211,
                       "note": "The dynastic end in the traditional sources.",
                       "source_ids": [S_WIKI_QARAKHITAI]}],
        name_forms=[{"name": "Western Liao", "kind": "common",
                     "note": "Names its descent from the Liao dynasty of northern China.",
                     "source_ids": [S_BIRAN_QARAKHITAI]}])

    # ── the khanates and the Russian conquest ─────────────────────────────
    ERA("bukhara", "Khanate of Bukhara", CORE, 1501, 1920, "foundational",
        summary="Uzbek state in Transoxiana; an emirate from 1785 and a Russian "
                "protectorate from 1868.",
        source_ids=[S_BRIT_BUKHARA])
    ERA("khiva", "Khanate of Khiva", CORE, 1511, 1920, "intermediate",
        summary="Uzbek khanate on the lower Amu Darya, a Russian protectorate from 1873.",
        source_ids=[S_BRIT_KHIVA])
    ERA("kokand", "Khanate of Kokand", CORE, 1709, 1876, "intermediate",
        summary="Ferghana valley khanate, annexed outright by Russia rather than left as "
                "a protectorate.",
        date_note="Dated from 1709 or from 1798, depending on whether the earlier "
                  "principality is counted as the khanate.",
        source_ids=[S_BRIT_KOKAND],
        alternatives=[{"label": "1798", "standing": "minority", "start_year": 1798,
                       "source_ids": [S_BRIT_KOKAND]}])
    ERA("russian-turkestan", "Russian Conquest of Central Asia", CORE, 1865, 1895,
        "foundational",
        summary="Russian annexation of the three khanates, closing the last independent "
                "steppe polities.",
        date_note="Tashkent fell in 1865, Bukhara became a protectorate in 1868, Khiva in "
                  "1873, and Kokand was annexed in 1876; the border settlements ran to "
                  "the 1890s.",
        source_ids=[S_BRIT_RUSSIAN_CA])

    print("Central Asia: Turkic correction, Saka, Sogdia, and nine missing states")
