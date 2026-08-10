"""Author the five new kinds, and re-file the entities that were wearing the wrong one.

The audit found whole categories missing rather than merely thin: not one religion existed as
an entity, no trade network did, the `threshold` kind stopped dead at 1650 BCE, and 39% of the
dataset was individual reigns, which structurally cannot represent a society without kings.

Five kinds close that, and each exists because an existing kind was lying about something:

``language``  A proto-language is not a period, a polity, or a species. It is reconstructed
              rather than attested, dated by glottochronology and archaeology rather than
              excavation, and it stands in a descent relation to its daughters -- which is why
              `parent_id` here means linguistic ancestor, not container. Ids stay flat so that
              re-subgrouping a family, which historical linguistics does regularly, never
              changes an entity's identity.
``tradition`` A religion, denomination, school, or legal tradition. Filing Buddhism as a
              `period` would say it ended.
``people``    An ethnolinguistic or cultural group as an actor. This is the kind that lets the
              Scythians, the Bantu-speaking peoples and the Sea Peoples appear at all: they had
              no king lists, so a reign-shaped schema rendered them invisible.
``network``   A trade or exchange system. The Silk Road is not in a region and is not a state.
``person``    A notable individual not recorded as a ruler. Confucius had no reign.

Dates follow the rebuilt spine: every endpoint carries a method, and bounds unless the method
is `calendar` or `received`. Proto-language dates are `glottochronology`, deliberately wide,
and marked `reconstructed` on the topic axis -- a reconstructed proto-language is not a
doubtful one, it is one known by inference, which is a different claim.
"""

# (slug, name, parent, start, end, method, half-width, tier, summary, extras)
LANGUAGES = [
    ("proto-afroasiatic", "Proto-Afroasiatic", None, -12000, -8000, 2000, "foundational",
     "Reconstructed ancestor of Semitic, Egyptian, Berber, Chadic and Cushitic; among the deepest families with a serious reconstruction."),
    ("proto-semitic", "Proto-Semitic", "proto-afroasiatic", -3800, -3000, 500, "foundational",
     "Ancestor of Akkadian, Hebrew, Aramaic and Arabic, reconstructed largely from their shared triconsonantal roots."),
    ("akkadian", "Akkadian", "proto-semitic", -2500, 100, 200, "foundational",
     "The first Semitic language written down, and the diplomatic language of the Bronze Age Near East."),
    ("aramaic", "Aramaic", "proto-semitic", -1100, None, 150, "intermediate",
     "Administrative language of the Achaemenid Empire and still spoken by small communities today."),
    ("hebrew", "Hebrew", "proto-semitic", -1000, None, 150, "foundational",
     "Ceased to be a vernacular for roughly seventeen centuries and was revived as one, which almost no other language has managed."),
    ("arabic", "Arabic", "proto-semitic", 300, None, 150, "foundational",
     "Spread with Islam from a peninsular vernacular to the liturgical and literary language of much of Afro-Eurasia."),
    ("egyptian", "Egyptian", "proto-afroasiatic", -3250, 1700, 150, "foundational",
     "Attested across four thousand years, from hieroglyphs to Coptic, the longest documented history of any language."),
    ("proto-indo-european", "Proto-Indo-European", None, -4500, -2500, 1000, "foundational",
     "Reconstructed ancestor of most languages of Europe and much of South Asia; its homeland is still argued."),
    ("proto-indo-iranian", "Proto-Indo-Iranian", "proto-indo-european", -2500, -1800, 300, "intermediate",
     "The branch that carried Indo-European speech into Iran and South Asia."),
    ("sanskrit", "Sanskrit", "proto-indo-iranian", -1500, None, 200, "foundational",
     "Language of the Vedas, and the grammar Panini wrote for it is still the most complete description of any ancient language."),
    ("avestan", "Avestan", "proto-indo-iranian", -1200, -400, 300, "specialist",
     "Language of the Zoroastrian liturgy, preserved orally for centuries before it was written."),
    ("hittite", "Hittite", "proto-indo-european", -1650, -1180, 100, "intermediate",
     "The earliest attested Indo-European language, and its decipherment reshaped the whole reconstruction."),
    ("ancient-greek", "Ancient Greek", "proto-indo-european", -1400, 300, 150, "foundational",
     "Written first in Linear B, then in the alphabet that carried Homer, tragedy and Greek philosophy."),
    ("latin", "Latin", "proto-indo-european", -700, None, 150, "foundational",
     "Ancestor of the Romance languages and the learned language of western Europe long after it stopped being anyone's first."),
    ("proto-uralic", "Proto-Uralic", None, -4000, -2000, 1000, "intermediate",
     "Reconstructed ancestor of Finnish, Hungarian, Estonian and the Samoyedic languages of Siberia."),
    ("proto-sino-tibetan", "Proto-Sino-Tibetan", None, -4500, -2500, 1000, "foundational",
     "Reconstructed ancestor of Chinese, Tibetan and Burmese; its internal structure is much less settled than Indo-European's."),
    ("old-chinese", "Old Chinese", "proto-sino-tibetan", -1250, -200, 150, "foundational",
     "The language of the oracle bones and the Confucian classics, reconstructed partly from rhymes in early poetry."),
    ("proto-austronesian", "Proto-Austronesian", None, -3500, -2500, 500, "foundational",
     "Ancestor of a family that spread from Taiwan across the Pacific to Madagascar, the widest pre-modern dispersal of any."),
    ("proto-bantu", "Proto-Bantu", None, -3000, -1500, 500, "foundational",
     "Ancestor of some five hundred languages across sub-Saharan Africa, spread by the Bantu expansion."),
    ("proto-dravidian", "Proto-Dravidian", None, -4000, -2000, 1000, "foundational",
     "Reconstructed ancestor of Tamil, Telugu, Kannada and Malayalam; possibly the language family of the Indus cities."),
    ("proto-japonic", "Proto-Japonic", None, -1000, 200, 400, "intermediate",
     "Ancestor of Japanese and the Ryukyuan languages, probably carried to the islands with wet-rice farming."),
    ("proto-koreanic", "Proto-Koreanic", None, -500, 500, 400, "intermediate",
     "Ancestor of Korean, whose relationship to Japonic remains one of the open questions of Asian linguistics."),
    ("sumerian", "Sumerian", None, -3100, -1800, 150, "foundational",
     "The first written language, and an isolate: no relative has ever been established for it."),
    ("elamite", "Elamite", None, -2600, -400, 200, "specialist",
     "Written beside Sumerian and Akkadian for two millennia and, like Sumerian, without known relatives."),
    ("etruscan", "Etruscan", None, -700, 100, 100, "specialist",
     "Non-Indo-European language of pre-Roman Italy, readable in script but still largely not understood."),
    ("classical-maya", "Classical Maya", None, 250, 900, 100, "intermediate",
     "The only pre-Columbian American writing system fully deciphered, recording dynastic history in its own words."),
    ("quechua", "Quechua", None, 1000, None, 300, "intermediate",
     "Spread as the administrative language of the Inca state and still spoken by millions across the Andes."),
    ("nahuatl", "Nahuatl", None, 600, None, 300, "intermediate",
     "Language of the Aztec state, and the source of chocolate, tomato, avocado and coyote."),
]

TRADITIONS = [
    ("zoroastrianism", "Zoroastrianism", None, -1200, None, 400, "foundational",
     "Persian tradition whose ideas about judgement, a final reckoning and cosmic dualism reached Judaism, Christianity and Islam."),
    ("judaism", "Judaism", None, -600, None, 200, "foundational",
     "Took its lasting shape around exile and return, and around a text rather than a temple."),
    ("hinduism", "Hinduism", None, -1500, None, 300, "foundational",
     "Less a single founding than a continuity of Vedic ritual, Upanishadic philosophy and devotional practice."),
    ("jainism", "Jainism", None, -600, None, 100, "intermediate",
     "Holds non-violence as the first principle, extended to every living thing."),
    ("buddhism", "Buddhism", None, -450, None, 100, "foundational",
     "Began as a teaching about the causes of suffering and became the first tradition to spread across Asia by persuasion."),
    ("theravada", "Theravada Buddhism", "buddhism", -250, None, 100, "intermediate",
     "The school that kept the Pali canon, dominant across Sri Lanka and mainland Southeast Asia."),
    ("mahayana", "Mahayana Buddhism", "buddhism", 100, None, 100, "intermediate",
     "Shifted the goal from personal liberation to universal awakening, and carried Buddhism to China, Korea and Japan."),
    ("vajrayana", "Vajrayana Buddhism", "mahayana", 600, None, 100, "specialist",
     "Tantric Buddhism, transmitted into Tibet and the Himalaya."),
    ("confucianism", "Confucianism", None, -500, None, 100, "foundational",
     "A tradition about conduct, family and government rather than gods, and the framework of Chinese administration for two millennia."),
    ("daoism", "Daoism", None, -400, None, 150, "foundational",
     "Philosophy and later religion built on acting with the grain of things rather than against it."),
    ("shinto", "Shinto", None, 500, None, 200, "intermediate",
     "Japanese practice centred on kami and place, defined as a distinct religion largely in response to Buddhism."),
    ("christianity", "Christianity", None, 30, None, 10, "foundational",
     "Began as a movement within Judaism and became the state religion of the empire that had executed its founder."),
    ("islam", "Islam", None, 610, None, 5, "foundational",
     "Began at Mecca and Medina and within a century governed from Iberia to the Indus."),
    ("sunni-shia-split", "The Sunni-Shia Split", "islam", 632, 680, 5, "foundational",
     "A dispute over succession to Muhammad that hardened into the enduring division of the Muslim world."),
    ("sufism", "Sufism", "islam", 800, None, 100, "intermediate",
     "The mystical current of Islam, and the form in which it most often spread through South Asia and West Africa."),
    ("great-schism", "The Great Schism", "christianity", 1054, None, 5, "foundational",
     "Formal separation of the Latin and Greek churches, after centuries of drift over authority and doctrine."),
    ("sikhism", "Sikhism", None, 1500, None, 20, "foundational",
     "Founded by Nanak in Punjab, rejecting caste and ritual in favour of one God and honest work."),
    ("manichaeism", "Manichaeism", None, 240, 1400, 50, "specialist",
     "A deliberately universal religion that reached from Rome to China and then was extinguished almost everywhere."),
]

PEOPLES = [
    ("sarmatians", "Sarmatians", "central-asia", -400, 400, 100, "intermediate",
     "Successors to the Scythians on the western steppe, and heavy cavalry the Romans learned from."),
    ("xiongnu", "Xiongnu", "central-asia", -300, 100, 100, "foundational",
     "Steppe confederation whose pressure shaped Han policy, the frontier walls, and the westward movement of peoples."),
    ("huns", "Huns", "central-asia", 370, 470, 30, "foundational",
     "Arrived on the Danube within a generation and broke the Roman order in the west without ever holding a city."),
    ("turkic-peoples", "Turkic Peoples", "central-asia", 550, None, 100, "foundational",
     "Spread from Mongolia to Anatolia over a millennium, founding states from the Gokturks to the Ottomans."),

    ("celts", "Celtic Peoples", "europe", -800, 100, 150, "foundational",
     "A shared language, art and metalwork across Iron Age Europe, never a single state."),
    ("germanic-peoples", "Germanic Peoples", "europe", -500, 800, 150, "foundational",
     "Named as an outside threat by Rome and eventually the founders of its successor kingdoms."),
    ("slavs", "Slavic Peoples", "europe", 400, None, 150, "foundational",
     "Expanded across eastern and southeastern Europe in the centuries after Rome, with little written trace of the process."),
    ("sami", "Sami", "europe", -1000, None, 500, "intermediate",
     "Reindeer-herding people of Fennoscandia, and among the few European peoples never to form a state."),
    ("bantu-peoples", "Bantu-Speaking Peoples", "africa", -3000, None, 500, "foundational",
     "Their expansion carried farming, ironworking and a language family across a third of a continent."),
    ("amazigh", "Amazigh", "africa", -2000, None, 500, "foundational",
     "Indigenous peoples of North Africa, continuous through Punic, Roman, Arab and French rule."),
    ("thule", "Thule", "americas", 1000, 1600, 100, "intermediate",
     "Ancestors of the Inuit, who crossed the American Arctic in a few centuries with dog sleds and toggling harpoons."),
    ("aboriginal-australians", "Aboriginal Australians", "oceania", -65000, None, 5000, "foundational",
     "The longest continuous cultural tradition known, with oral accounts that appear to record post-glacial sea-level rise."),
]

NETWORKS = [
    ("silk-road", "The Silk Road", -130, 1450, 50, "foundational",
     "Not one road but a relay of routes moving silk, horses, faith and plague between China, India, Persia and Rome.",
     ["east-asia", "central-asia", "south-asia", "west-asia", "europe"]),
    ("indian-ocean-trade", "Indian Ocean Trade", -1000, None, 200, "foundational",
     "Monsoon-driven and older than the Silk Road, carrying more goods by volume than any overland route.",
     ["africa", "west-asia", "south-asia", "southeast-asia", "east-asia"]),
    ("trans-saharan-trade", "Trans-Saharan Trade", 300, 1600, 100, "foundational",
     "Gold north, salt south, and the wealth that built Mali, Songhai and the libraries of Timbuktu.",
     ["africa", "europe", "west-asia"]),
    ("amber-road", "The Amber Road", -1600, 1000, 200, "specialist",
     "Baltic amber reaching the Mediterranean, and evidence of long-distance exchange well before any empire organised it.",
     ["europe"]),
    ("hanseatic-league", "The Hanseatic League", 1150, 1669, 30, "foundational",
     "A league of merchant towns that ran the northern European economy without being a state.",
     ["europe"]),
    ("atlantic-slave-trade", "The Atlantic Slave Trade", 1501, 1867, 5, "foundational",
     "Some twelve million people shipped from Africa to the Americas, and the demographic and economic foundation of the Atlantic world.",
     ["africa", "americas", "europe"]),
    ("manila-galleon", "The Manila Galleon Trade", 1565, 1815, 5, "intermediate",
     "Silver from Mexico for Chinese silk and porcelain, and the first sustained commercial link across the Pacific.",
     ["americas", "southeast-asia", "east-asia"]),
]

PERSONS = [
    ("confucius", "Confucius", "east-asia", -551, -479, 5, "foundational",
     "Taught that government rests on the character of those who govern; had no office of consequence and shaped a civilisation."),
    ("laozi", "Laozi", "east-asia", -600, -500, 100, "intermediate",
     "Traditional author of the Daodejing, and possibly a composite of several figures.", "legendary"),
    ("siddhartha-gautama", "Siddhartha Gautama", "south-asia", -480, -400, 40, "foundational",
     "Left a princely household to answer why there is suffering, and founded the tradition that became Buddhism."),
    ("mahavira", "Mahavira", "south-asia", -599, -527, 30, "intermediate",
     "Contemporary of the Buddha and the figure Jainism takes its historical shape from."),
    ("zoroaster", "Zoroaster", "central-asia", -1200, -1000, 300, "intermediate",
     "Prophet of the first tradition to frame history as a moral struggle with an end.", "legendary"),
    ("socrates", "Socrates", "europe", -470, -399, 5, "foundational",
     "Wrote nothing, was executed by his own city, and set the shape of philosophical argument since."),
    ("aristotle", "Aristotle", "europe", -384, -322, 3, "foundational",
     "Attempted a systematic account of everything, and his errors held authority nearly as long as his insights."),
    ("archimedes", "Archimedes", "europe", -287, -212, 5, "foundational",
     "Came nearer to calculus than anyone would for eighteen centuries."),
    ("al-khwarizmi", "Al-Khwarizmi", "central-asia", 780, 850, 15, "foundational",
     "His name became algorithm and his book's title became algebra."),
    ("ibn-sina", "Ibn Sina", "central-asia", 980, 1037, 3, "foundational",
     "His medical canon was the standard text in Europe and the Islamic world for six hundred years."),
    ("aryabhata", "Aryabhata", "south-asia", 476, 550, 10, "intermediate",
     "Gave a place-value system, an accurate value for pi, and a rotating Earth."),
    ("gutenberg", "Johannes Gutenberg", "europe", 1400, 1468, 10, "foundational",
     "Combined movable type, oil ink and the press into something that made copying cheap enough to change what could be thought."),
]

# Thresholds after 1650 BCE. The kind existed and stopped there, so the dataset held the
# first controlled fire and the domestic chicken but not iron, the alphabet, or the transistor.
THRESHOLDS = [
    ("iron-smelting", "Iron Smelting", -1900, 200, "Hittite-era bloomery iron; the metal that made tools cheap rather than precious."),
    ("alphabet", "Alphabetic Writing", -1850, 150, "One sign per sound rather than per syllable or word, which made literacy learnable in weeks."),
    ("zero-as-number", "Zero as a Number", 628, 20, "Brahmagupta gave rules for arithmetic with zero and with negatives, not merely a placeholder."),
    ("papermaking", "Papermaking", -100, 100, "Cheap writing material from plant fibre, in China centuries before it reached the west."),
    ("woodblock-printing", "Woodblock Printing", 650, 100, "Text carved and reproduced in quantity in Tang China, long before movable type."),
    ("movable-type", "Movable Type", 1040, 20, "Bi Sheng's ceramic type; reusable characters four centuries before Gutenberg."),
    ("gunpowder", "Gunpowder", 850, 50, "A Chinese alchemical accident that ended the military logic of the walled city."),
    ("magnetic-compass", "Magnetic Compass", 1040, 50, "Made open-water navigation repeatable rather than lucky."),
    ("printing-press", "The Printing Press", 1440, 10, "Movable metal type and a screw press in Mainz; the first information technology with a mass market."),
    ("telescope", "The Telescope", 1608, 2, "Turned the sky into something to be examined rather than contemplated."),
    ("steam-engine", "The Steam Engine", 1712, 5, "Newcomen's atmospheric engine; work no longer limited by muscle, wind or falling water."),
    ("vaccination", "Vaccination", 1796, 2, "Jenner's cowpox inoculation, and the beginning of deliberate control of infectious disease."),
    ("germ-theory", "Germ Theory of Disease", 1861, 5, "Established that specific microbes cause specific diseases, which made surgery survivable."),
    ("electric-light", "Practical Electric Lighting", 1879, 2, "Decoupled the working day from daylight."),
    ("powered-flight", "Powered Flight", 1903, 1, "Twelve seconds at Kitty Hawk."),
    ("antibiotics", "Antibiotics", 1928, 2, "Fleming's penicillin; bacterial infection stopped being a common cause of death."),
    ("nuclear-fission", "Controlled Nuclear Fission", 1942, 1, "The first self-sustaining chain reaction, under a squash court in Chicago."),
    ("transistor", "The Transistor", 1947, 1, "The switch that made computing small, cheap and eventually universal."),
    ("integrated-circuit", "The Integrated Circuit", 1958, 1, "Many components on one wafer, which is why computing kept getting cheaper."),
    ("packet-switching", "Packet-Switched Networking", 1969, 1, "The first ARPANET link; messages broken into pieces that route themselves."),
    ("genome-sequencing", "The Human Genome Sequenced", 2003, 1, "A species reading its own instructions."),
]

# Two entities already existed for things the new kinds describe better. Authoring alongside
# them would have produced exactly the duplicate pair this project has created twice before, so
# the originals are re-kinded and the new rows were deleted. Checking for that BEFORE authoring
# is the lesson; here a name-collision test caught it after.
# Regions a re-kinded entity must acquire, because the new kind requires what the old one did
# not. Re-kinding without supplying them left the Incense Route as a network naming no regions,
# which a test caught.
RE_KIND_REGIONS = {
    "west-asia.arabia.pre-islamic.incense-trade": ["west-asia", "africa", "europe"],
}

RE_KIND = {
    "central-asia.scythians": "people",
    "west-asia.arabia.pre-islamic.incense-trade": "network",
    "west-asia.mesopotamia.phoenicia.byblos": "city",
    "west-asia.mesopotamia.phoenicia.tyre": "city",
    "west-asia.mesopotamia.phoenicia.sidon": "city",
    "west-asia.mesopotamia.phoenicia.arwad": "city",
    "americas.mesoamerica.aztec.tenochtitlan": "city",
    "west-asia.anatolia.lydia.coinage": "threshold",
}

LANG_ROOT = "global.languages"
TRAD_ROOT = "global.traditions"
NET_ROOT = "global.networks"
MILE_ROOT = "global.milestones"


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}
    counts = {}

    # ---- re-kind entities wearing the wrong one -----------------------------
    for eid, kind in RE_KIND.items():
        e = by_id.get(eid)
        if e is None:
            raise KeyError(f"new_kinds: cannot re-kind missing {eid}")
        was = e["kind"]
        e["kind"] = kind
        if kind == "city" and e.get("end_year") is None:
            e["extant"] = True
        if kind == "threshold":
            # A threshold is one-sided: coinage was invented once and did not stop. `end_year`
            # is required-but-nullable, so it is set to None rather than removed -- deleting the
            # key failed schema validation, which is the schema being right.
            e["end_year"] = None
            for k in ("end_year_min", "end_year_max", "end_dating_method", "start_year_max"):
                e.pop(k, None)
        if eid in RE_KIND_REGIONS:
            e["regions"] = RE_KIND_REGIONS[eid]
        note = (e.get("date_note") or "").strip()
        extra = f"Re-filed from `{was}` to `{kind}`: the earlier kind misdescribed what this is."
        if extra not in note:
            e["date_note"] = (note + " " + extra).strip()
    counts["re-kinded"] = len(RE_KIND)

    # ---- containers ---------------------------------------------------------
    for cid, name, summary in (
        (LANG_ROOT, "Languages",
         "Language families and the languages descended from them. Placement here is by linguistic descent, not geography."),
        (TRAD_ROOT, "Religions & Traditions",
         "Religions, denominations, schools and legal traditions, filed by descent from what they grew out of."),
        (NET_ROOT, "Trade & Exchange Networks",
         "Systems of exchange that were neither states nor places, and that moved goods, people, faith and disease."),
        (MILE_ROOT, "Technological Thresholds",
         "First attainments of a capability after the prehistoric record, each a lower bound that new evidence can only move older."),
    ):
        if cid not in by_id:
            E(cid, "region", name, "global", start=None, end=None, tier="foundational",
              summary=summary)

    def _skip_zero(y):
        """There is no year 0, and a bound may not sit on it.

        The same trap the dating migration hit, in a second place: Etruscan ends around 100 CE
        with a century of slack, Mahayana starts around 100 CE, and the Xiongnu end around
        100 CE -- so subtracting the half-width lands exactly on a year that does not exist and
        the chrono layer refuses it. Widening is always the safe direction for an uncertainty
        bound, so 0 moves away from the estimate.
        """
        return -1 if y == 0 else y

    def bounded(eid, kind, name, parent, start, end, half, tier, summary, method, **extra):
        fields = dict(extra)
        fields["summary"] = summary
        fields["start_dating_method"] = method
        if start is not None:
            fields["start_year_min"] = _skip_zero(start - half)
            fields["start_year_max"] = _skip_zero(start + half)
        if end is not None:
            fields["end_dating_method"] = method
            fields["end_year_min"] = _skip_zero(end - half)
            fields["end_year_max"] = _skip_zero(end + half)
        return E(eid, kind, name, parent, start=start, end=end, tier=tier, **fields)

    # ---- languages ---------------------------------------------------------
    for slug, name, ancestor, start, end, half, tier, summary in LANGUAGES:
        parent = f"{LANG_ROOT}.{ancestor}" if ancestor else LANG_ROOT
        reconstructed = name.startswith("Proto-")
        extras = {}
        if reconstructed:
            extras["historicity"] = "reconstructed"
        if end is None:
            extras["extant"] = True
        bounded(f"{LANG_ROOT}.{slug}", "language", name, parent, start, end, half, tier,
                summary,
                "glottochronology" if reconstructed else "first-attestation",
                allow_outside_parent_dates=True, **extras)
    counts["languages"] = len(LANGUAGES)

    # ---- traditions --------------------------------------------------------
    for slug, name, ancestor, start, end, half, tier, summary in TRADITIONS:
        parent = f"{TRAD_ROOT}.{ancestor}" if ancestor else TRAD_ROOT
        extras = {"extant": True} if end is None else {}
        bounded(f"{TRAD_ROOT}.{slug}", "tradition", name, parent, start, end, half, tier,
                summary, "first-attestation", allow_outside_parent_dates=True, **extras)
    counts["traditions"] = len(TRADITIONS)

    # ---- the Sea Peoples, as a culture rather than a people -----------------
    # `people` asserts one coherent ethnolinguistic group. The Sea Peoples are a label Egyptian
    # scribes applied to a heterogeneous set of raiders -- Peleset, Shekelesh, Denyen, Weshesh and
    # others -- whose origins, relationship to one another, and even whether they were a single
    # phenomenon are all argued. `culture` claims less, and `historicity: contested` says the
    # coherence of the category is itself the disputed thing.
    bounded("west-asia.culture-sea-peoples", "culture", "Sea Peoples", "west-asia",
            -1200, -1150, 50, "foundational",
            "A name Egyptian scribes gave to raiders from several origins, tied to the collapse of the Bronze Age eastern Mediterranean.",
            "first-attestation", allow_outside_parent_dates=True, historicity="contested")

    # ---- peoples -----------------------------------------------------------
    for slug, name, region, start, end, half, tier, summary in PEOPLES:
        extras = {"extant": True} if end is None else {}
        bounded(f"{region}.peoples-{slug}", "people", name, region, start, end, half, tier,
                summary, "first-attestation", allow_outside_parent_dates=True, **extras)
    counts["peoples"] = len(PEOPLES)

    # ---- networks ----------------------------------------------------------
    for slug, name, start, end, half, tier, summary, regions in NETWORKS:
        extras = {"extant": True} if end is None else {}
        bounded(f"{NET_ROOT}.{slug}", "network", name, NET_ROOT, start, end, half, tier,
                summary, "first-attestation", regions=regions, **extras)
    counts["networks"] = len(NETWORKS)

    # ---- persons -----------------------------------------------------------
    for row in PERSONS:
        slug, name, region, start, end, half, tier, summary = row[:8]
        extras = {"historicity": row[8]} if len(row) > 8 else {}
        bounded(f"{region}.persons-{slug}", "person", name, region, start, end, half, tier,
                summary, "calendar" if half <= 5 else "first-attestation",
                allow_outside_parent_dates=True, **extras)
    counts["persons"] = len(PERSONS)

    # ---- thresholds --------------------------------------------------------
    for slug, name, start, half, summary in THRESHOLDS:
        E(f"{MILE_ROOT}.{slug}", "threshold", name, MILE_ROOT, start=start, end=None,
          tier="foundational" if abs(start) < 2000 else "intermediate",
          summary=summary,
          start_dating_method="calendar" if start > 1400 else "typological",
          # One-sided: a first attainment can only move earlier.
          **({"start_year_min": start - half} if start <= 1400 else {}))
    counts["thresholds"] = len(THRESHOLDS)

    print("new_kinds: " + ", ".join(f"{k} {v}" for k, v in counts.items()))
