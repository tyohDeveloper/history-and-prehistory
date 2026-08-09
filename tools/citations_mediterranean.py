"""Sources for Greece and Rome, and two dates that turned out to be wrong.

Research in `docs/mediterranean-citations.md`.

This module fixes a problem of the dataset's own making. 616 entities displayed
a date with no source behind them, and the worst of them were the most famous:
Mycenaean Greece, the Roman Republic, Classical Athens, Byzantium. Everything
authored since the sourcing rule existed is scrupulous; everything from before
it was bare. The rigour was inverted, so a visitor's first click landed on the
weakest part of the dataset while Namazga — a Turkmen pottery sequence almost
nobody will look up — carried three sources and a dagger.

This is the first tranche: the seventeen foundational Mediterranean entities.

**Two dates are corrected outright, not merely cited.**

`europe.mediterranean.greece` started at 3000 BCE. The British Museum, Cambridge
and Smarthistory all put the start of the Greek Bronze Age at about **3200**.
3000 was a rounding of a convention, off by two centuries.

`europe.mediterranean.macedon` started at **808 BCE**, which is a king-list
back-calculation to the possibly-fictional Karanos. Britannica, the Oxford
Companion to Classical Literature and the Lexicon of Argead Macedonia all date
the historically attested kingdom to about **700 BCE** under Perdiccas I —
Herodotus credits Perdiccas and not Karanos at all. The entity now starts at 700
and carries the legend as a `received` alternative. This is structurally the
same error as Rome's 753, and it had been sitting one row away from it.

**Four received conventions are now labelled as such.**

Rome's 753 BCE is Varro's antiquarian back-calculation, which the Oxford
Classical Dictionary calls "artificial manipulation" that "does not accord with
any archaeological starting point". Ancient authors proposed at least six
different years, from Timaeus's 841 to Cincius's 728. The Republic's 509 is
Varronian too, and modern scholarship prefers 508/507.

476 CE is Gibbon's marker. A UCL thesis puts it flatly: "476 is not the year in
which the empire ended, and never was." Gibbon's own footnote conceded the year
"is not positively ascertained". Britannica declines to give a year at all.

330 CE for Byzantium is one of at least six live conventions, and the field's own
standard reference, the Oxford Dictionary of Byzantium, deliberately avoids
calling anything before the 7th century Byzantine.

**One label, not a date, is flagged.** "Crisis of the Third Century" smuggles a
judgement into a name: Lewitt, Witschel and others reject the coherent-systemic-
collapse reading the word "crisis" asserts.

The Thera dispute is attached to Mycenaean Greece, where it does the most work:
radiocarbon and the Egyptian synchronisms disagree by roughly a century and that
propagates through every Late Bronze Age Aegean date.
"""

S_OCD_ROME = "ocd-rome-foundation"
S_BM_GREECE = "british-museum-greece-rome-department"
S_BM_VISITOR = "british-museum-visitor-guide-bronze-age"
S_CAMB_AEGEAN = "cambridge-aegean-bronze-age-excerpt"
S_SMARTHISTORY_GR = "smarthistory-ancient-greece-intro"
S_LEIDEN_MYC = "leiden-mycenaean-chronology"
S_ODYSSEUS_MYCENAE = "greek-culture-ministry-mycenae"
S_CAMB_MYC_HIGH = "cambridge-mycenaean-high-chronology"
S_BRITANNICA_ARGEAD = "britannica-argead-dynasty"
S_ARGEAD_LEXICON = "lexicon-of-argead-macedonia"
S_MULDER_ROME = "mulder-rome-foundation-dates"
S_CONVERSATION_ROME = "conversation-rome-foundation-archaeology"
S_UCL_476 = "ucl-thesis-fall-of-western-empire"
S_UNRV_ROMULUS = "unrv-romulus-augustulus"
S_LATOMUS_ODOACER = "latomus-2024-odoacer-deposition"
S_WHE_MAPS = "world-history-roman-empire-maps"
S_ODB_PREFACE = "oxford-dictionary-of-byzantium-preface"
S_EHW_CONSTANTINOPLE = "hellenic-world-constantinople-foundation"
S_OUP_CONSTANTINOPLE = "oup-constantine-dedicates-constantinople"
S_NAM_ARCHAIC = "national-archaeological-museum-athens-archaic"
S_PERSEUS_AUGUSTUS = "perseus-harpers-augustus-imperator"
S_THERA_2025 = "bruins-van-der-plicht-2025-thera"
S_THERA_2023 = "sci-reports-2023-thera-olive"

MEDITERRANEAN_SOURCES = [
    {"id": S_OCD_ROME, "kind": "scholarly",
     "citation": "Cornell, 'Rome (history)', Oxford Classical Dictionary",
     "url": "https://academic.oup.com/edited-volume/61673/chapter/550496605",
     "note": "'The conventional foundation date, fixed at 753 BCE by Varro, is the result of "
             "artificial manipulation, and does not accord with any archaeological starting "
             "point.'"},
    {"id": S_BM_GREECE, "kind": "reference",
     "citation": "British Museum, Department of Greece and Rome",
     "url": "https://www.britishmuseum.org/our-work/departments/greece-and-rome",
     "note": "Dates the beginning of the Greek Bronze Age to about 3200 BC."},
    {"id": S_BM_VISITOR, "kind": "reference",
     "citation": "British Museum, Visitor Journey large-print gallery guide",
     "url": "https://www.britishmuseum.org/sites/default/files/2020-11/Visitor_Journey_large_print_guide_British_Museum.pdf",
     "note": "'The Greek Bronze Age lasted from about 3200 to 1100 BC'; Mycenaean period "
             "1600-1100 BC."},
    {"id": S_CAMB_AEGEAN, "kind": "scholarly",
     "citation": "Cambridge University Press, Aegean Bronze Age volume excerpt",
     "url": "https://assets.cambridge.org/97810094/93123/excerpt/9781009493123_excerpt.pdf"},
    {"id": S_SMARTHISTORY_GR, "kind": "reference",
     "citation": "Smarthistory, 'Ancient Greece, an introduction'",
     "url": "https://smarthistory.org/ancient-greece-an-introduction/"},
    {"id": S_LEIDEN_MYC, "kind": "scholarly",
     "citation": "Leiden University doctoral dissertation on Mycenaean chronology",
     "url": "https://scholarlypublications.universiteitleiden.nl/access/item:4098120/view"},
    {"id": S_ODYSSEUS_MYCENAE, "kind": "reference",
     "citation": "Greek Ministry of Culture, Odysseus portal, Mycenae",
     "url": "http://odysseus.culture.gr/h/3/eh351.jsp?obj_id=2573"},
    {"id": S_CAMB_MYC_HIGH, "kind": "scholarly",
     "citation": "Cambridge University Press excerpt citing Shelmerdine (2008) on the Aegean high chronology",
     "url": "https://assets.cambridge.org/97811071/07540/excerpt/9781107107540_excerpt.pdf",
     "note": "The high chronology places the start of Late Helladic I at about 1700 BCE."},
    {"id": S_BRITANNICA_ARGEAD, "kind": "reference",
     "citation": "Encyclopaedia Britannica, 'Argead Dynasty'",
     "url": "https://www.britannica.com/topic/Argead-dynasty",
     "note": "Dates the ruling house of Macedonia from about 700 BC under Perdiccas I, a "
             "century later than the Karanos king-list figure."},
    {"id": S_ARGEAD_LEXICON, "kind": "scholarly",
     "citation": "Lexicon of Argead Macedonia",
     "url": "https://dokumen.pub/lexicon-of-argead-macedonia-3732904059-9783732904051-9783732996018.html",
     "note": "Places the mythic foundation of the Argead line in the mid-7th century BC."},
    {"id": S_MULDER_ROME, "kind": "scholarly",
     "citation": "Mulder, thesis on ancient accounts of Rome's foundation (Utrecht University)",
     "url": "https://studenttheses.uu.nl/",
     "note": "Catalogues the ancient disagreement: Timaeus 841, Polybius and Diodorus 750, "
             "Dionysius 751, Livy 749, Fabius Pictor 747, Cincius 728 BC."},
    {"id": S_CONVERSATION_ROME, "kind": "press",
     "citation": "Swift, 'Archaeology adds another twist to Rome's foundation story', The Conversation",
     "url": "https://theconversation.com/archaeology-adds-another-twist-to-romes-foundation-story-by-ageing-it-100-years",
     "note": "Explains Varro's back-calculation through the consular lists, and the 9th-century "
             "settlement evidence that does not fit it."},
    {"id": S_UCL_476, "kind": "scholarly",
     "citation": "Campbell-Moffat, doctoral thesis on the end of the Western Roman Empire (UCL Discovery)",
     "url": "https://discovery.ucl.ac.uk/",
     "note": "'476 is not the year in which the empire ended, and never was.' Quotes Gibbon's "
             "own footnote conceding the year 'is not positively ascertained'."},
    {"id": S_UNRV_ROMULUS, "kind": "reference",
     "citation": "UNRV Roman History, 'Romulus Augustulus'",
     "url": "https://www.unrv.com/emperors/romulus-augustulus.php"},
    {"id": S_LATOMUS_ODOACER, "kind": "scholarly",
     "citation": "'When did Odoacer depose Romulus Augustulus?', Latomus (2024)",
     "url": "https://www.academia.edu/124406620/When_did_Odoacer_depose_Romulus_Augustulus_",
     "note": "Argues even the day, 4 September 476, is questionable given contradictions "
             "among the surviving sources."},
    {"id": S_WHE_MAPS, "kind": "reference",
     "citation": "World History Encyclopedia, the Roman Empire in maps",
     "url": "https://www.worldhistory.org/collection/189/the-roman-empire-in-10-maps/9/"},
    {"id": S_ODB_PREFACE, "kind": "scholarly",
     "citation": "The Oxford Dictionary of Byzantium, preface",
     "url": "https://archive.org/details/oxforddictionary0000unse",
     "note": "The field's standard reference uses 'late Roman' or 'late antique' for the 4th "
             "to mid-7th centuries and reserves 'Byzantine' for the 7th century onward."},
    {"id": S_EHW_CONSTANTINOPLE, "kind": "scholarly",
     "citation": "Encyclopaedia of the Hellenic World, foundation of Constantinople",
     "url": "http://www.ehw.gr/constantinople/",
     "note": "Cites Dagron: the foundation was a long process over many years that tradition "
             "gradually epitomised into a single date."},
    {"id": S_OUP_CONSTANTINOPLE, "kind": "reference",
     "citation": "Oxford University Press blog, 'Constantine dedicates Constantinople'",
     "url": "https://blog.oup.com/2012/05/constantine-dedicates-constantinople/"},
    {"id": S_NAM_ARCHAIC, "kind": "reference",
     "citation": "National Archaeological Museum, Athens, on the Archaic period",
     "url": "https://www.namuseum.gr/en/collection/archaiki-periodos-2/",
     "note": "Notes that 'Archaic' is an 18th-century coinage, applied retrospectively."},
    {"id": S_PERSEUS_AUGUSTUS, "kind": "scholarly",
     "citation": "Harpers Dictionary of Classical Antiquities, 'Augustus, Imperator' (Perseus, Tufts)",
     "url": "http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.04.0062:alphabetic+letter=A:entry+group=1:entry=augustus-imperator-harpers"},
    {"id": S_THERA_2025, "kind": "scholarly",
     "citation": "Bruins & van der Plicht, on the Thera eruption date, PLOS ONE (2025)",
     "url": "https://journals.plos.org/plosone/",
     "note": "The radiocarbon and Egyptian-synchronism chronologies have narrowed but not "
             "converged."},
    {"id": S_THERA_2023, "kind": "scholarly",
     "citation": "Olive-shrub study of the Thera eruption, Scientific Reports (2023)",
     "url": "https://www.nature.com/srep/"},
]

# `traditional` is a STANDING and `received` is a DATING METHOD. They describe
# different axes -- how well accepted a claim is, and how the number was arrived
# at -- and this module first shipped with `received` in the standing field. The
# schema rejected it, which is what the enum is for.
CHECKED = "2026-08-08"
CAL = "calendar"
RECEIVED = "received"
TYPO = "typological"


def extend(E, entities):
    """Attach sources to entities authored before the sourcing rule existed."""
    by_id = {e["id"]: e for e in entities}

    def enrich(eid, **fields):
        e = by_id.get(eid)
        if e is None:
            return None
        for k, v in fields.items():
            e[k] = v
        return e

    # ------------------------------------------------------------ Greece

    # Was 3000 BCE. Every institutional source fetched says about 3200.
    g = enrich(
        "europe.mediterranean.greece",
        start_year=-3200,
        start_dating_method=TYPO, end_dating_method=CAL, standing="majority",
        date_precision="century",
        date_note="Corrected from 3000 BCE, which was a rounding. The British Museum, "
                  "Cambridge and Smarthistory all place the start of the Greek Bronze Age at "
                  "about 3200 BC. Note the two ends are different kinds of date: a "
                  "periodisation boundary at the start, and the Roman sack of Corinth in 146 "
                  "BCE at the end.",
        source_ids=[S_BM_GREECE, S_BM_VISITOR, S_CAMB_AEGEAN, S_SMARTHISTORY_GR],
    )
    if g is not None:
        g["caveats"] = list(g.get("caveats", [])) + [
            {"kind": "misconception",
             "text": "A round 3000 BCE circulates widely for the start of Greek prehistory. "
                     "It is a rounding of the 3200 BC convention, not a separate finding.",
             "source_ids": [S_BM_VISITOR]},
        ]

    m = enrich(
        "europe.mediterranean.greece.mycenaean",
        start_dating_method=TYPO, end_dating_method=TYPO, standing="majority",
        date_precision="disputed",
        date_note="1600-1100 BC is the British Museum's convention and a defensible one, but "
                  "not the only one: start dates of 1750, 1700 and 1675 BCE are all in print. "
                  "The whole Aegean absolute chronology this sits inside is unresolved, "
                  "because radiocarbon dating of the Thera eruption and the Egyptian "
                  "synchronisms disagree by roughly a century.",
        as_of=CHECKED,
        source_ids=[S_BM_VISITOR, S_LEIDEN_MYC, S_ODYSSEUS_MYCENAE, S_CAMB_MYC_HIGH],
    )
    if m is not None:
        m["alternatives"] = list(m.get("alternatives", [])) + [
            {"label": "Aegean high chronology, from c. 1700 BCE", "standing": "minority",
             "start_year": -1700, "end_year": -1100, "dating_method": TYPO,
             "note": "Follows the radiocarbon dating of the Thera eruption rather than the "
                     "Egyptian synchronisms, and pushes the Late Bronze Age Aegean about a "
                     "century earlier.",
             "source_ids": [S_CAMB_MYC_HIGH, S_THERA_2025]},
        ]
        m["caveats"] = list(m.get("caveats", [])) + [
            {"kind": "misconception",
             "text": "Aegean Bronze Age dates are not independently fixed. They inherit the "
                     "unresolved Thera dispute, which recent work has narrowed without "
                     "settling.",
             "source_ids": [S_THERA_2025, S_THERA_2023]},
        ]

    enrich(
        "europe.mediterranean.greece.archaic",
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_precision="century",
        date_note="A modern retrospective label, coined in the 18th century, not a period the "
                  "Greeks recognised. The end is usually pinned to the Persian Wars, which "
                  "some schemes date to 479 rather than 480 BCE.",
        source_ids=[S_NAM_ARCHAIC, S_SMARTHISTORY_GR],
    )

    enrich(
        "europe.mediterranean.greece.classical",
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_note="Bracketed by two attested events, the end of the Persian Wars and the death "
                  "of Alexander in 323 BCE, but 'Classical' is itself a modern retrospective "
                  "category rather than a contemporary one.",
        source_ids=[S_SMARTHISTORY_GR, S_BM_GREECE],
    )

    enrich(
        "europe.mediterranean.hellenistic",
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_note="From Alexander's death in 323 BCE to Actium in 31. The term was coined by "
                  "Droysen in the 19th century; no one living through it called it that.",
        source_ids=[S_SMARTHISTORY_GR, S_BM_GREECE],
    )

    # ----------------------------------------------------------- Macedon

    # Was 808 BCE: a king-list back-calculation to a founder Herodotus does not
    # even name. Same error as Rome's 753, one row away from it in the tree.
    mac = enrich(
        "europe.mediterranean.macedon",
        start_year=-700,
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_precision="century",
        date_note="Corrected from 808 BCE. Britannica, the Oxford Companion to Classical "
                  "Literature and the Lexicon of Argead Macedonia all date the historically "
                  "attested kingdom to about 700 BC under Perdiccas I. The end, Roman "
                  "annexation in 146 BCE, is securely attested.",
        as_of=CHECKED,
        source_ids=[S_BRITANNICA_ARGEAD, S_ARGEAD_LEXICON],
    )
    if mac is not None:
        mac["alternatives"] = list(mac.get("alternatives", [])) + [
            {"label": "Traditional foundation by Karanos, 808 BCE", "standing": "traditional",
             "start_year": -808, "end_year": -146, "dating_method": RECEIVED,
             "note": "A king-list back-calculation to a founder ancient authors themselves "
                     "disputed. Herodotus credits Perdiccas I instead and does not mention "
                     "Karanos.",
             "source_ids": [S_BRITANNICA_ARGEAD, S_ARGEAD_LEXICON]},
        ]
        mac["caveats"] = list(mac.get("caveats", [])) + [
            {"kind": "misconception",
             "text": "808 BCE is still widely printed as Macedon's founding. It is legend "
                     "systematised into a king-list, structurally the same as Rome's 753.",
             "source_ids": [S_BRITANNICA_ARGEAD]},
        ]

    # -------------------------------------------------------------- Rome

    r = enrich(
        "europe.mediterranean.rome",
        start_dating_method=RECEIVED, end_dating_method=CAL, standing="traditional",
        date_precision="traditional",
        date_note="Both ends are conventions rather than facts. 753 BCE is Varro's "
                  "back-calculation, which the Oxford Classical Dictionary calls artificial "
                  "manipulation that does not accord with any archaeological starting point. "
                  "476 CE is Gibbon's marker, which Britannica declines to give at all, "
                  "preferring 'the 5th century'.",
        as_of=CHECKED,
        source_ids=[S_OCD_ROME, S_MULDER_ROME, S_CONVERSATION_ROME, S_UCL_476],
    )
    if r is not None:
        r["alternatives"] = list(r.get("alternatives", [])) + [
            {"label": "Ancient authors gave at least six founding years", "standing": "traditional",
             "start_year": -841, "end_year": 476, "dating_method": RECEIVED,
             "note": "Timaeus 841, Polybius and Diodorus 750, Dionysius 751, Livy 749, Fabius "
                     "Pictor 747, Cincius 728 BC. Varro's 753 won on authority, not evidence.",
             "source_ids": [S_MULDER_ROME]},
        ]
        r["caveats"] = list(r.get("caveats", [])) + [
            {"kind": "misconception",
             "text": "Settlement on the Palatine is attested well before 753 BCE and an "
                     "urbanised city-state considerably after it. The traditional year matches "
                     "neither.",
             "source_ids": [S_OCD_ROME, S_CONVERSATION_ROME]},
        ]

    rep = enrich(
        "europe.mediterranean.rome.republic",
        start_dating_method=RECEIVED, end_dating_method=CAL, standing="majority",
        date_precision="disputed",
        date_note="509 BCE is the Varronian date and the Oxford Classical Dictionary describes "
                  "the Varronian scheme as incorrect in places; modern scholarship generally "
                  "prefers 508 or 507. The end, 27 BCE, is securely attested.",
        source_ids=[S_OCD_ROME, S_PERSEUS_AUGUSTUS],
    )
    if rep is not None:
        rep["caveats"] = list(rep.get("caveats", [])) + [
            {"kind": "misconception",
             "text": "509 BCE is a Varronian reckoning, not an attested year. The expulsion of "
                     "the kings is not dated by any contemporary record.",
             "source_ids": [S_OCD_ROME]},
        ]

    enrich(
        "europe.mediterranean.rome.republic.late",
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_note="A modern periodisation running from the tribunate of Tiberius Gracchus in "
                  "133 BCE. Its end is variously given as 44, 31 or 27 BCE depending on "
                  "whether the marker is Caesar's death, Actium, or the settlement with the "
                  "Senate.",
        source_ids=[S_PERSEUS_AUGUSTUS, S_WHE_MAPS],
    )

    enrich(
        "europe.mediterranean.rome.republic.late.caesar-assassination",
        start_dating_method=CAL, standing="consensus", date_precision="year",
        date_note="15 March 44 BCE. Attested by contemporaries and among the most securely "
                  "dated events in Roman history.",
        source_ids=[S_PERSEUS_AUGUSTUS],
    )

    enrich(
        "europe.mediterranean.rome.republic.late.actium",
        start_dating_method=CAL, standing="consensus", date_precision="year",
        date_note="2 September 31 BCE, securely attested.",
        source_ids=[S_PERSEUS_AUGUSTUS, S_WHE_MAPS],
    )

    emp = enrich(
        "europe.mediterranean.rome.empire",
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_precision="disputed",
        date_note="The start is solid: the Senate granted Octavian the title Augustus on 16 "
                  "January 27 BCE. The end is not. 476 CE is an 18th-century convention "
                  "popularised by Gibbon, whose own footnote conceded the year is not "
                  "positively ascertained, and a 2024 paper argues even the day is doubtful.",
        as_of=CHECKED,
        source_ids=[S_PERSEUS_AUGUSTUS, S_UCL_476, S_UNRV_ROMULUS, S_LATOMUS_ODOACER],
    )
    if emp is not None:
        emp["alternatives"] = list(emp.get("alternatives", [])) + [
            {"label": "Ends 480 CE, with Julius Nepos", "standing": "minority",
             "start_year": -27, "end_year": 480, "dating_method": CAL,
             "note": "Nepos was the last legitimate western emperor and outlived Romulus "
                     "Augustulus's deposition by four years.",
             "source_ids": [S_WHE_MAPS, S_UNRV_ROMULUS]},
            {"label": "Ends 410 CE, with the sack of Rome", "standing": "minority",
             "start_year": -27, "end_year": 410, "dating_method": CAL,
             "note": "One of several rival markers, alongside the Rhine crossing of 406 and "
                     "the Vandal sack of 455.",
             "source_ids": [S_UCL_476]},
        ]
        emp["caveats"] = list(emp.get("caveats", [])) + [
            {"kind": "misconception",
             "text": "A UCL thesis puts it plainly: 476 is not the year in which the empire "
                     "ended, and never was. Britannica gives no year, only the 5th century.",
             "source_ids": [S_UCL_476]},
        ]

    enrich(
        "europe.mediterranean.rome.empire.nerva-antonine",
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_note="Bracketed by two attested accessions and one attested murder, that of "
                  "Commodus at the end of 192 CE.",
        source_ids=[S_WHE_MAPS],
    )

    crisis = enrich(
        "europe.mediterranean.rome.empire.crisis-of-third-century",
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_note="The years are attested. The label is the problem: 'crisis' asserts a "
                  "coherent systemic collapse, and a substantial body of archaeological work "
                  "argues the evidence does not support one empire-wide.",
        source_ids=[S_WHE_MAPS],
    )
    if crisis is not None:
        crisis["caveats"] = list(crisis.get("caveats", [])) + [
            {"kind": "naming-confusion",
             "text": "Lewitt, Witschel and others reject the total-crisis model. The name "
                     "smuggles in an interpretation, which is unusual for a dating label.",
             "source_ids": [S_WHE_MAPS]},
        ]

    enrich(
        "europe.mediterranean.rome.empire.constantinian",
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_note="Some schemes begin the dynasty at 305 rather than 306 CE, depending on "
                  "whether Constantius I's accession or Constantine's acclamation is taken as "
                  "the start.",
        source_ids=[S_OUP_CONSTANTINOPLE, S_WHE_MAPS],
    )

    enrich(
        "europe.mediterranean.rome.empire.western-collapse",
        start_dating_method=CAL, end_dating_method=CAL, standing="minority",
        date_precision="disputed",
        date_note="455-480 CE brackets the Vandal sack of Rome and the death of Julius Nepos, "
                  "which is one defensible framing among several. The choice of any bracket "
                  "here is a historiographical position rather than a finding.",
        source_ids=[S_UCL_476, S_UNRV_ROMULUS, S_WHE_MAPS],
    )

    # --------------------------------------------------------- Byzantium

    byz = enrich(
        "europe.mediterranean.byzantine",
        start_dating_method=CAL, end_dating_method=CAL, standing="majority",
        date_precision="disputed",
        date_note="The dedication of Constantinople in 330 CE is securely attested; using it "
                  "as the start of a distinct empire is a choice. At least six conventions are "
                  "in use, beginning at Diocletian, Constantine, Theodosius, 395, 476, "
                  "Anastasius, Justinian or Heraclius. The end, 29 May 1453, is not in doubt.",
        as_of=CHECKED,
        source_ids=[S_ODB_PREFACE, S_EHW_CONSTANTINOPLE, S_OUP_CONSTANTINOPLE],
    )
    if byz is not None:
        byz["alternatives"] = list(byz.get("alternatives", [])) + [
            {"label": "Byzantine begins in the 7th century", "standing": "minority",
             "start_year": 610, "end_year": 1453, "dating_method": CAL,
             "note": "The Oxford Dictionary of Byzantium uses 'late Roman' for the 4th to "
                     "mid-7th centuries and reserves 'Byzantine' for what follows.",
             "source_ids": [S_ODB_PREFACE]},
            {"label": "Byzantine begins with the division of 395", "standing": "minority",
             "start_year": 395, "end_year": 1453, "dating_method": CAL,
             "note": "Takes the permanent administrative split after Theodosius I as the "
                     "starting point.",
             "source_ids": [S_EHW_CONSTANTINOPLE]},
        ]
        byz["caveats"] = list(byz.get("caveats", [])) + [
            {"kind": "naming-confusion",
             "text": "Nobody in it called it Byzantine; they called it Roman. The field's own "
                     "standard reference avoids the word before the 7th century.",
             "source_ids": [S_ODB_PREFACE]},
        ]
