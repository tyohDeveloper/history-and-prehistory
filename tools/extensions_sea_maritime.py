"""Maritime Southeast Asia: the Javanese sequence, the sultanates, the Philippines.

Majapahit stood in the dataset with no predecessor. A reader met the largest
empire in Javanese history arriving from nowhere in 1293, with the four centuries
that produced Borobudur and Prambanan simply absent. That is the same failure the
Song had before the Jin was added -- a consequence with its cause deleted -- and
it turned up independently in a different region, which suggests the pattern is
worth checking for deliberately rather than stumbling on.

**Two entities here need unusual care, for opposite reasons.**

*Srivijaya was not identified until 1918*, when George Cœdès assembled it from
Chinese accounts and inscriptions. Its nature is still argued over -- thalassocracy,
mandala, or something looser -- and even its capital is not settled. So the entity
records that the polity is a modern reconstruction from fragmentary evidence, which
is a different kind of claim from a state that named itself in its own documents.

*The pre-Spanish Philippine polities run the opposite risk.* Tondo is solidly
attested, by the Laguna Copperplate Inscription among other evidence. Cebu,
Butuan and Maynila are much thinner, and the surrounding literature contains a
known fabrication: the Code of Kalantiaw, invented in 1913 and treated as
authentic for decades. So Tondo is authored and the rest are not -- the honest
answer to "what pre-colonial states were there" is "one we can evidence here, and
others we cannot", not a tidy list.

**Dates that look precise but are not.** Majapahit's 1527 end is conventional,
tied to Demak's conquest of Kediri; one chronogram gives 1478 and recent work
dates the real collapse to 1513-1528. Aceh's 1496 founding competes with 1480,
1507 and 1514. Sulu's with 1457. Each is recorded as an alternative rather than
smoothed into a range, because a wide range would imply the middle is likeliest
when the actual claim is that sources disagree.

**Brunei carries a caveat the others do not.** It runs from roughly 1368 to the
present, but was a British protectorate from 1888 to 1984 -- so an unbroken span
would assert continuous sovereignty that lapsed for nearly a century.

**Indonesia's two dates are both kept.** The republic was proclaimed in 1945 and
recognised by the Netherlands in 1949. Which one counts is exactly the sort of
question this dataset should not quietly decide.
"""

S_BRIT_JAVA = "britannica-indonesia-central-java"
S_BRIT_KADIRI = "britannica-kadiri"
S_BRIT_MAJAPAHIT = "britannica-majapahit-empire"
S_WIKI_MAJAPAHIT = "wikipedia-majapahit"
S_WIKI_SRIVIJAYA = "wikipedia-srivijaya"
S_BRIT_MALACCA = "britannica-sultanate-of-malacca"
S_WIKI_SINGHASARI = "wikipedia-singhasari"
S_WIKI_MEDANG = "wikipedia-medang-kingdom"
S_WIKI_ACEH = "wikipedia-aceh-sultanate"
S_WIKI_BRUNEI = "wikipedia-bruneian-empire"
S_WIKI_SULU = "wikipedia-sultanate-of-sulu"
S_WIKI_TONDO = "wikipedia-tondo-polity"
S_WIKI_LCI = "wikipedia-laguna-copperplate"
S_WIKI_KALANTIAW = "wikipedia-code-of-kalantiaw"
S_WIKI_MATARAM_SULT = "wikipedia-mataram-sultanate"
S_WIKI_DEMAK = "wikipedia-demak-sultanate"
S_WIKI_INDONESIA_IND = "wikipedia-indonesian-independence"
S_BRIT_PHILIPPINES = "britannica-philippines-spanish-period"

SEA_MARITIME_SOURCES = [
    {"id": S_BRIT_JAVA, "kind": "reference",
     "citation": "'Indonesia: Central Java from c. 700 to c. 1000', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Indonesia/Central-Java-from-c-700-to-c-1000",
     "note": "The Central Javanese period, Borobudur and Prambanan, and the Sailendra "
             "and Sanjaya question."},
    {"id": S_WIKI_MEDANG, "kind": "reference",
     "citation": "'Medang Kingdom', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Medang_Kingdom",
     "note": "Whether Sailendra and Sanjaya were two dynasties, one, or a power-sharing "
             "arrangement is unresolved."},
    {"id": S_BRIT_KADIRI, "kind": "reference",
     "citation": "'Kadiri', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Kadiri",
     "note": "The Kediri kingdom, 1042-1222."},
    {"id": S_WIKI_SINGHASARI, "kind": "reference",
     "citation": "'Singhasari', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Singhasari",
     "note": "1222-1292, ending in the succession crisis that produced Majapahit."},
    {"id": S_BRIT_MAJAPAHIT, "kind": "reference",
     "citation": "'Majapahit empire', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Majapahit-empire",
     "note": "Founded 1293 after the Yuan expedition was repelled."},
    {"id": S_WIKI_MAJAPAHIT, "kind": "reference",
     "citation": "'Majapahit', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Majapahit",
     "note": "The 1527 end date is conventional; a chronogram gives 1478 and recent work "
             "dates the collapse to 1513-1528."},
    {"id": S_WIKI_SRIVIJAYA, "kind": "reference",
     "citation": "'Srivijaya', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Srivijaya",
     "note": "Identified as a polity by George Cœdès in 1918 from Chinese and "
             "inscriptional sources. Its nature and capital remain disputed."},
    {"id": S_BRIT_MALACCA, "kind": "reference",
     "citation": "'Sultanate of Malacca', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/sultanate-of-Malacca",
     "note": "Founded about 1400 and taken by the Portuguese in 1511."},
    {"id": S_WIKI_ACEH, "kind": "reference",
     "citation": "'Aceh Sultanate', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Aceh_Sultanate",
     "note": "Founding variously given as 1496, 1480, 1507 and 1514."},
    {"id": S_WIKI_BRUNEI, "kind": "reference",
     "citation": "'Bruneian Empire', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Bruneian_Empire",
     "note": "A British protectorate from 1888 until full independence in 1984."},
    {"id": S_WIKI_SULU, "kind": "reference",
     "citation": "'Sultanate of Sulu', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Sultanate_of_Sulu",
     "note": "Founding given as 1405 or 1457."},
    {"id": S_WIKI_TONDO, "kind": "reference",
     "citation": "'Tondo (historical polity)', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Tondo_(historical_polity)",
     "note": "The best-evidenced pre-colonial Philippine polity."},
    {"id": S_WIKI_LCI, "kind": "primary",
     "citation": "'Laguna Copperplate Inscription', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Laguna_Copperplate_Inscription",
     "note": "Dated 900 CE, the earliest known written document from the Philippines, and "
             "the principal evidence for Tondo."},
    {"id": S_WIKI_KALANTIAW, "kind": "reference",
     "citation": "'Code of Kalantiaw', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Code_of_Kalantiaw",
     "note": "A 1913 fabrication that circulated as authentic pre-colonial law for "
             "decades. The reason claims about Philippine pre-colonial states need "
             "checking individually."},
    {"id": S_WIKI_DEMAK, "kind": "reference",
     "citation": "'Demak Sultanate', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Demak_Sultanate",
     "note": "The first Islamic state on Java; its end is given as 1548 or 1554."},
    {"id": S_WIKI_MATARAM_SULT, "kind": "reference",
     "citation": "'Mataram Sultanate', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Mataram_Sultanate",
     "note": "1587-1755, ending with the Treaty of Giyanti. Distinct from the much "
             "earlier Medang/Mataram kingdom."},
    {"id": S_WIKI_INDONESIA_IND, "kind": "reference",
     "citation": "'Proclamation of Indonesian Independence', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Proclamation_of_Indonesian_Independence",
     "note": "Proclaimed 17 August 1945; Dutch recognition followed the 1949 Hague "
             "agreement."},
    {"id": S_BRIT_PHILIPPINES, "kind": "reference",
     "citation": "'Philippines: The Spanish period', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Philippines/The-Spanish-period",
     "note": "Spanish rule from 1565 and its end in 1898."},
]


def extend(E, entities):
    from builders import make_builders

    by_id = {e["id"]: e for e in entities}
    _, P, ERA, _, _, _ = make_builders(E, id_prefix="southeast-asia.maritime")
    M = "southeast-asia.maritime"

    def enrich(eid, **fields):
        e = by_id.get(eid)
        if e is None:
            return
        for k, v in fields.items():
            e[k] = v

    # ── the Javanese sequence Majapahit was missing ───────────────────────
    ERA("medang", "Medang Kingdom", M, 732, 1006, "foundational",
        summary="The Central Javanese period, which built Borobudur and Prambanan.",
        date_note="Also called Mataram, and not to be confused with the Islamic Mataram "
                  "Sultanate of 1587-1755. Whether the Sailendra and Sanjaya lines were "
                  "two dynasties, one, or a power-sharing arrangement is unresolved. The "
                  "end is given as 1006 or 1016.",
        source_ids=[S_BRIT_JAVA, S_WIKI_MEDANG],
        caveats=[{"kind": "naming-confusion",
                  "text": "Frequently called Mataram, which collides with the later "
                          "Islamic sultanate of the same name.",
                  "source_ids": [S_WIKI_MEDANG]}],
        name_forms=[{"name": "Mataram Kingdom", "kind": "common",
                     "note": "Ambiguous: the Islamic Mataram Sultanate is a different "
                             "state six centuries later.",
                     "source_ids": [S_WIKI_MEDANG]}],
        date_precision="approx")
    ERA("kahuripan", "Kahuripan", M, 1019, 1045, "intermediate",
        summary="Airlangga's kingdom, divided between his sons at his abdication.",
        date_note="The division produced Kediri and Janggala.",
        source_ids=[S_BRIT_KADIRI])
    ERA("kediri", "Kediri Kingdom", M, 1042, 1222, "foundational",
        summary="East Javanese kingdom, remembered above all for its literature.",
        source_ids=[S_BRIT_KADIRI])
    ERA("singhasari", "Singhasari Kingdom", M, 1222, 1292, "foundational",
        summary="Displaced Kediri and expanded Javanese power outward; ended in the "
                "succession crisis that produced Majapahit.",
        source_ids=[S_WIKI_SINGHASARI])

    # ── Islamic Java ──────────────────────────────────────────────────────
    ERA("demak", "Demak Sultanate", M, 1475, 1554, "intermediate",
        summary="The first Islamic state on Java, and the power that finished Majapahit.",
        date_note="The end is given as either 1548 or 1554.",
        source_ids=[S_WIKI_DEMAK],
        alternatives=[{"label": "1548", "standing": "minority", "end_year": 1548,
                       "source_ids": [S_WIKI_DEMAK]}])
    ERA("mataram-sultanate", "Mataram Sultanate", M, 1587, 1755, "foundational",
        summary="The dominant Javanese state of the 17th century, partitioned under Dutch "
                "pressure.",
        date_note="Ended with the Treaty of Giyanti in 1755, which split it between "
                  "Yogyakarta and Surakarta. A different state from the Medang/Mataram "
                  "kingdom of 732-1006.",
        source_ids=[S_WIKI_MATARAM_SULT])

    # ── the sultanates ────────────────────────────────────────────────────
    ERA("aceh", "Aceh Sultanate", M, 1496, 1903, "foundational",
        summary="North Sumatran sultanate and a major pepper power, which fought the "
                "Dutch for three decades.",
        date_note="Four founding dates circulate -- 1496, 1480, 1507 and 1514. Ended by "
                  "Dutch conquest in 1903 after the Aceh War.",
        source_ids=[S_WIKI_ACEH],
        alternatives=[{"label": "1480", "standing": "minority", "start_year": 1480,
                       "source_ids": [S_WIKI_ACEH]},
                      {"label": "1507", "standing": "minority", "start_year": 1507,
                       "source_ids": [S_WIKI_ACEH]}])
    ERA("brunei", "Bruneian Empire", M, 1368, 1888, "foundational",
        summary="Bornean sultanate that dominated the northwest coast before contracting "
                "under British and Sarawak pressure.",
        date_note="Ends here in 1888, when Brunei became a British protectorate. The "
                  "sultanate itself continues and is independent again from 1984, so "
                  "this span covers its sovereign period rather than its existence -- "
                  "running it unbroken to the present would assert a sovereignty that "
                  "lapsed for ninety-six years.",
        source_ids=[S_WIKI_BRUNEI],
        date_precision="approx")
    ERA("sulu", "Sultanate of Sulu", M, 1405, 1915, "intermediate",
        summary="Sultanate of the Sulu archipelago, which resisted Spanish control for "
                "three centuries.",
        date_note="Founding given as 1405 or 1457. Sovereignty was relinquished in 1915 "
                  "under American administration.",
        source_ids=[S_WIKI_SULU],
        alternatives=[{"label": "1457", "standing": "minority", "start_year": 1457,
                       "source_ids": [S_WIKI_SULU]}])

    # ── the Philippines before 1565 ───────────────────────────────────────
    # Only Tondo. Cebu, Butuan and Maynila are far more thinly evidenced, and
    # this is a field where a 1913 forgery circulated as law for decades, so a
    # confident list would be the wrong output.
    ERA("tondo", "Tondo", M, 900, 1589, "intermediate",
        summary="Polity on Manila Bay, attested from 900 CE by the earliest surviving "
                "Philippine document.",
        date_note="The 900 date comes from the Laguna Copperplate Inscription, which "
                  "gives a floor rather than a founding. Other pre-colonial polities -- "
                  "Cebu, Butuan, Maynila -- are much more thinly evidenced and are not "
                  "authored here; the literature also contains the Code of Kalantiaw, a "
                  "1913 fabrication long treated as genuine, so claims in this area need "
                  "checking one at a time.",
        source_ids=[S_WIKI_TONDO, S_WIKI_LCI, S_WIKI_KALANTIAW],
        date_precision="approx")

    # ── sources for what was already there ────────────────────────────────
    enrich("southeast-asia.maritime.srivijaya",
           source_ids=[S_WIKI_SRIVIJAYA],
           date_note="Srivijaya was not identified as a polity until 1918, when George "
                     "Cœdès reconstructed it from Chinese accounts and inscriptions. Its "
                     "nature is still argued -- thalassocracy, mandala, or a looser "
                     "arrangement -- and even its capital is unsettled, with Palembang "
                     "the usual candidate. Treat the span as the period the "
                     "reconstruction covers, not as a reign-list.",
           caveats=[{"kind": "contested-existence",
                     "text": "A modern scholarly reconstruction from fragmentary "
                             "evidence, not a state that named itself in surviving "
                             "documents of its own.",
                     "source_ids": [S_WIKI_SRIVIJAYA]}],
           date_precision="approx")

    enrich("southeast-asia.maritime.majapahit",
           source_ids=[S_BRIT_MAJAPAHIT, S_WIKI_MAJAPAHIT],
           date_note="Founded 1293 after the Yuan expedition was repelled. The 1527 end "
                     "is conventional, tied to Demak's conquest of Kediri; a chronogram "
                     "gives 1478, and recent work dates the actual collapse to 1513-1528.",
           alternatives=[{"label": "1478, from the traditional chronogram",
                          "standing": "traditional", "end_year": 1478,
                          "source_ids": [S_WIKI_MAJAPAHIT]}])

    enrich("southeast-asia.maritime.malacca", source_ids=[S_BRIT_MALACCA],
           name_forms=[{"name": "Melaka", "kind": "endonym", "lang": "ms",
                        "source_ids": [S_BRIT_MALACCA]}])

    enrich("southeast-asia.maritime.spanish-philippines",
           source_ids=[S_BRIT_PHILIPPINES])

    enrich("southeast-asia.maritime.indonesia",
           source_ids=[S_WIKI_INDONESIA_IND],
           date_note="Independence was proclaimed on 17 August 1945; the Netherlands did "
                     "not recognise it until the Hague agreement of 1949. Both dates are "
                     "defensible and the choice between them is a political question, "
                     "not a factual one.",
           alternatives=[{"label": "1949, Dutch recognition", "standing": "minority",
                          "start_year": 1949,
                          "note": "The date the former colonial power accepted.",
                          "source_ids": [S_WIKI_INDONESIA_IND]}])

    print("SE Asia maritime: Javanese sequence, sultanates, Tondo")
