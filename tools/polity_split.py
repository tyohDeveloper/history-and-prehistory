"""Separate states from the labels historians put on spans of time.

The `era` kind was carrying two unlike things. The Roman Republic had consuls, armies, taxes and
a foreign policy; the Stone Age had none of those because it is not that sort of thing. Filing
both as `era` meant the dataset could not say which entities were actors.

`polity` is for a thing with a government: a state, empire, kingdom, dynasty, republic,
caliphate, confederacy. `era` keeps what it should always have had: chronological labels.

Two traps made this less mechanical than it looks.

**The test is rulers, not vocabulary.** A first pass keyed on words like Empire and Dynasty, and
it split the Roman Republic from the Roman Empire -- the Republic was filed as a `period`, so a
pass over `era` never saw it, and the two halves of the same state ended up in different kinds. It
also left Ancient Egypt as an era while 143 pharaohs hung beneath it. What actually distinguishes a
state is that somebody ruled it, so the rule is: an entity with reigns among its descendants is a
polity, whatever kind it was filed as and whatever its name happens to contain.

**A name is not a reliable signal.** Egypt's Old, Middle and New Kingdoms match every keyword a
polity rule would use, and all three are *phases of one polity* rather than three states -- the
polity is Ancient Egypt, and its dynasties run through those phases. A rule keyed on the word
"Kingdom" got all three wrong, and would also have taken the Three Kingdoms, the Five Dynasties
and the Northern and Southern Dynasties, each of which names a period of division rather than a
single state.

**There is a third category neither kind fits**, so it gets its own. The Olmec, Chavín, Lapita,
Mississippian, Ancestral Puebloan, Norte Chico, Nazca and Marajoara entries are archaeological
cultures: horizons defined by material remains -- pottery, burial practice, metalwork -- whose
political organisation is frequently the open question about them. Calling them polities would
assert a state nobody has demonstrated, and calling them eras says the Olmec were a span of time.
`culture` says what they are, and says it without deciding what they were governed by.
"""

import re

# Keywords that name a form of government. Only consulted after the explicit lists below.
POLITY_WORDS = re.compile(
    r"\b(Empire|Kingdom|Dynasty|Republic|Caliphate|Sultanate|Khanate|Khaganate|Shogunate"
    r"|Emirate|Confederacy|Confederation|Federation|Horde|Tsardom|Principality|Duchy"
    r"|Viceroyalty|Monarchy|Commonwealth|Protectorate|State)\b"
)

# Words that mark a span of time rather than a government.
ERA_WORDS = re.compile(
    r"\b(Age|Ages|Period|Antiquity|Era|Prehistory|Century|Interregnum|Restoration"
    r"|Neolithic|Paleolithic|Mesolithic|Chalcolithic|Urbanization|Urbanisation"
    r"|Culture|Civilization|Civilisation|Voyaging|Settlement|Colonial|Divided|Rule)\b"
)

# Match a polity keyword but are phases of a polity, or periods of division. Kept as `era`.
# Civilisation containers. Each holds the states that actually governed, and is itself the
# cultural-historical span rather than a government -- which is the sense in which "the Roman
# Empire" is a period two thousand pages long in Gibbon and 27 BCE to 476 CE in a king list.
#
# Both senses are real and the ambiguity is genuine, so the fix is not to pick one: Ancient Rome
# carries the epoch, the Kingdom, Republic and Empire carry the states, and a naming-confusion
# caveat on the Empire says out loud that the name is used both ways. The Holy Roman Empire is
# unambiguously a polity and stays one -- it had an emperor, a diet and a chancery, and Voltaire's
# complaint about it was that it was not an empire, not that it was a period.
CIVILISATION_ERAS = {
    "europe.mediterranean.rome",
    "africa.nile.egypt",
}

# Caveat text is capped at 200 characters, which is a good constraint badly met on the first try.
DUAL_SENSE_NOTE = (
    "\"Roman Empire\" means both the state from 27 BCE and the whole Roman epoch, as in "
    "The Rise and Fall of the Roman Empire. This is the state; the epoch is Ancient Rome, above."
)

ERA_FORCE = {
    "africa.nile.egypt.old-kingdom",
    "africa.nile.egypt.middle-kingdom",
    "africa.nile.egypt.new-kingdom",
    "africa.nile.egypt.predynastic",
    "africa.nile.egypt.early-dynastic",
    "africa.nile.egypt.late-period",
    "africa.nile.egypt.roman-byzantine",
    "east-asia.china.three-kingdoms",
    "east-asia.china.north-south",
    "east-asia.china.five-dynasties",
    "east-asia.korea.three-kingdoms",
    "east-asia.korea.colonial",
    "east-asia.korea.divided",
    "west-asia.mesopotamia.phoenicia",
    "west-asia.arabia.pre-islamic",
    "africa.east.swahili",
    "americas.north.colonial",
    "americas.intermediate.taino",
    "oceania.melanesia.fijian-chiefdoms",
    "oceania.polynesia.settlement",
    "oceania.australia.colonial",
    "oceania.australia.aboriginal",
    "europe.western.iberia.reconquista",
    "east-asia.japan.kenmu",
    "global.contemporary",
    "south-asia.mahajanapadas",
}

# States that no keyword rule would catch, because their names are simply place names.
POLITY_FORCE = {
    "west-asia.mesopotamia.ur-iii",
    "west-asia.mesopotamia.kassite",
    "west-asia.iran.elam",
    "europe.central.habsburg-monarchy",
    "europe.central.prussia",
    "europe.central.nazi-germany",
    "europe.central.germany-modern",
    "europe.eastern.moscow",
    "central-asia.tibet.dalai-lama",
    "southeast-asia.mainland.funan",
    "southeast-asia.mainland.champa",
    "southeast-asia.mainland.vietnam",
    "southeast-asia.maritime.srivijaya",
    "southeast-asia.maritime.dutch-eic",
    "southeast-asia.maritime.spanish-philippines",
    "africa.north.morocco-alaouite",
    "africa.southern.great-zimbabwe",
    "americas.north.haudenosaunee",
    "americas.north.usa",
    "americas.mesoamerica.zapotec",
    "americas.mesoamerica.teotihuacan",
    "americas.mesoamerica.mexico",
    "americas.andes.tiwanaku",
    "americas.andes.chimu",
    "americas.amazon-southern.mapuche",
    "oceania.polynesia.aotearoa",
}

# Archaeological cultures. Neither kind fits and inventing a fit would be a claim.
CULTURES = {
    "south-asia.indus",
    "americas.north.mississippian",
    "americas.north.ancestral-puebloan",
    "americas.mesoamerica.olmec",
    "americas.mesoamerica.maya",
    "americas.andes.norte-chico",
    "americas.andes.chavin",
    "americas.andes.moche",
    "americas.andes.nazca",
    "americas.amazon-southern.marajoara",
    "oceania.melanesia.lapita",
}

CULTURE_NOTE = ("Filed as a culture rather than a polity or an era: an archaeological horizon "
                "defined by material remains, whose political organisation is often the open "
                "question about it.")


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}
    for group, label in ((ERA_FORCE, "ERA_FORCE"), (POLITY_FORCE, "POLITY_FORCE"),
                         (CULTURES, "CULTURES")):
        unknown = [i for i in group if i not in by_id]
        if unknown:
            raise KeyError(f"polity_split: {label} names {len(unknown)} missing id(s): {unknown}")

    # Reign descendants, computed once. Direct children are not enough: Julius Caesar sits under
    # `rome.republic.late`, not under `rome.republic`, and checking only children is the mistake
    # that twice led this project to declare a populated container empty.
    kids = {}
    for e in entities:
        kids.setdefault(e.get("parent_id"), []).append(e)

    def has_reigns(eid):
        stack = list(kids.get(eid, []))
        while stack:
            node = stack.pop()
            if node["kind"] in ("reign", "person"):
                return True
            stack.extend(kids.get(node["id"], []))
        return False

    promoted, kept, cultures = 0, 0, 0
    for e in entities:
        if e["kind"] not in ("era", "period"):
            continue
        eid = e["id"]

        if eid in CULTURES:
            e["kind"] = "culture"
            note = (e.get("date_note") or "").strip()
            if CULTURE_NOTE not in note:
                e["date_note"] = (note + " " + CULTURE_NOTE).strip()
            cultures += 1
            continue

        if eid in ERA_FORCE or eid in CIVILISATION_ERAS:
            e["kind"] = "era"
            kept += 1
            continue

        named_polity = POLITY_WORDS.search(e["name"]) and not ERA_WORDS.search(e["name"])
        named_era = ERA_WORDS.search(e["name"]) and not POLITY_WORDS.search(e["name"])

        # A name that says "Period" or "Age" vetoes promotion even when rulers sit beneath it.
        # Japan's Kamakura and Muromachi Periods have shoguns under them and were promoted by the
        # reigns test, but they are periodisations named after where a regime sat -- the regime is
        # the Kamakura Shogunate, and the period is the label for its span. Same for Egypt's Old,
        # Middle and New Kingdoms, which is why those needed forcing by hand before this veto.
        if named_era and eid not in POLITY_FORCE:
            kept += 1
            continue

        if eid in POLITY_FORCE or named_polity or has_reigns(eid):
            e["kind"] = "polity"
            promoted += 1
        else:
            kept += 1

    empire = by_id.get("europe.mediterranean.rome.empire")
    if empire is not None:
        caveats = empire.setdefault("caveats", [])
        if not any(c.get("text") == DUAL_SENSE_NOTE for c in caveats):
            caveats.append({"kind": "naming-confusion", "text": DUAL_SENSE_NOTE})

    print(f"polity_split: {promoted} promoted to polity, {kept} kept as era, "
          f"{cultures} re-kinded as culture")
