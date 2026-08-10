"""Summaries for the geographic containers, which are the app's highest-traffic nodes.

Thirty-two containers reached the top tier with no summary, including `east-asia.china`,
`africa` and `americas`. Clicking "China" and getting a bare date range is a poor result
for the most-visited node in the dataset.

These are deliberately **not** sourced, on the same reasoning that exempts links into
`global` from validator Rule 7: a container summary describes what this dataset chose to
group under a heading. It is a statement about the taxonomy, not a claim about the past,
and demanding an external citation for an editorial grouping decision would be a
category error -- the kind of rule that gets worked around rather than obeyed.

What they do carry is honesty about the grouping. "Southeast Asia", "the Middle East"
and "Eastern Europe" are modern conveniences applied backwards over millennia in which
nobody used them, and several of these summaries say so. The standing editorial line is
to stay as culturally neutral as possible while acknowledging that the world is not
culturally neutral in any way, so where a grouping is a modern imposition, the summary
names it rather than presenting the container as natural.
"""

SUMMARIES = {
    # ── Europe ───────────────────────────────────────────────────────────────
    "europe.mediterranean": "The Greek, Roman and Byzantine worlds and the sea that "
        "connected them, treated as one region because its societies were more closely "
        "linked to each other by water than to their own inland neighbours.",
    "europe.western": "Iberia, France, the Low Countries and the British Isles, from "
        "the post-Roman kingdoms through the Atlantic empires.",
    "europe.central": "The German-speaking lands, the Alps and the Carpathian basin: "
        "the Holy Roman Empire and the Habsburg and Prussian states that succeeded it.",
    "europe.northern": "Scandinavia, the Baltic and Finland, including the Norse "
        "expansion that reached Greenland and North America.",
    "europe.eastern": "The lands between the Baltic and the Black Sea: Kievan Rus', "
        "Poland-Lithuania, Muscovy and the Russian states that grew from them. The "
        "boundary with Central Europe is political and has moved repeatedly.",
    # ── West Asia ────────────────────────────────────────────────────────────
    "west-asia.mesopotamia": "The Tigris-Euphrates floodplain and the Levantine coast, "
        "where writing, cities and law codes first appear in the record.",
    "west-asia.anatolia": "The peninsula between the Aegean and the Caucasus: Hittite, "
        "Phrygian, Lydian, Greek, Roman, Byzantine and Turkish in succession.",
    "west-asia.iran": "The Iranian plateau and its empires, from Elam and the "
        "Achaemenids to the Safavids and the modern state.",
    "west-asia.arabia": "The peninsula and its incense kingdoms before Islam, and the "
        "states that followed.",
    # ── Central Asia ─────────────────────────────────────────────────────────
    "central-asia.core": "The oasis cities and river valleys of Transoxiana and "
        "Khorasan — Samarkand, Bukhara, Merv — repeatedly the hinge between the "
        "settled empires around them.",
    "central-asia.steppe": "The grassland corridor from Mongolia to Hungary, and the "
        "mobile polities that formed across it. Their borders were seasonal and their "
        "records are usually written by their neighbours.",
    # ── East Asia ────────────────────────────────────────────────────────────
    "east-asia": "China, Korea and Japan, plus the steppe and maritime peripheries "
        "they contested, linked by a shared script, canon and diplomatic order.",
    "east-asia.china": "The longest continuously documented state tradition on record, "
        "from the Neolithic cultures of the Yellow and Yangtze valleys to the present. "
        "Dynastic names organise it, but they conceal as much as they reveal: several "
        "were regional, several overlapped, and some conquered from outside.",
    "east-asia.korea": "The peninsula from Gojoseon and the Three Kingdoms through "
        "Silla, Goryeo and Joseon to the modern division.",
    "east-asia.japan": "The archipelago from Jōmon foraging societies through the "
        "imperial court, the shogunates and the modern state. Its eras are named "
        "reign periods, which is why so many appear here.",
    # ── Southeast Asia ───────────────────────────────────────────────────────
    "southeast-asia": "The mainland peninsulas and the island world between India and "
        "China. The name is a twentieth-century military coinage; the region's own "
        "states organised themselves around river valleys and sea lanes, not around "
        "this category.",
    "southeast-asia.mainland": "The Irrawaddy, Chao Phraya, Mekong and Red River "
        "valleys: the Burmese, Thai, Lao, Khmer, Cham and Vietnamese states.",
    "southeast-asia.maritime": "The archipelagos and straits — Srivijaya, Majapahit, "
        "the sultanates, the Philippine polities — where control meant control of "
        "shipping rather than of territory.",
    # ── Africa ───────────────────────────────────────────────────────────────
    "africa": "The continent where the human lineage originates, and the states, "
        "trade systems and empires that followed across a landmass big enough to hold "
        "several unconnected histories at once.",
    "africa.nile": "The Nile corridor and the Horn: Egypt, Nubia and Kush, Aksum and "
        "Ethiopia — societies shaped by a river that floods on schedule.",
    "africa.north": "The Maghreb and the Mediterranean littoral: Carthage, Roman "
        "Africa, the Berber dynasties and the Islamic states.",
    "africa.west": "The Sahel and the forest belt, where Ghana, Mali, Songhai, "
        "Kanem-Bornu and Benin grew on the trade crossing the Sahara.",
    "africa.east": "The Swahili coast and the interlacustrine kingdoms, connected by "
        "monsoon trade to Arabia, India and China.",
    "africa.southern": "From Great Zimbabwe and Mapungubwe to the Mutapa state and the "
        "Zulu kingdom.",
    # ── Americas ─────────────────────────────────────────────────────────────
    "americas": "Two continents settled from Asia in the late Pleistocene, whose "
        "societies developed in near-total isolation from Afro-Eurasia until 1492 — "
        "which makes their parallels with it, agriculture and cities and states, the "
        "most useful controlled comparison in human history.",
    "americas.north": "North of Mesoamerica: the Ancestral Puebloan and Mississippian "
        "societies, the Arctic and subarctic peoples, and the nations encountered and "
        "displaced by European settlement.",
    "americas.mesoamerica": "From central Mexico to Honduras: Olmec, Zapotec, Maya, "
        "Teotihuacan, Toltec, Purépecha and Aztec, sharing a calendar, a ballgame and "
        "a writing tradition.",
    "americas.andes": "The Pacific coast and highlands from Norte Chico through Moche, "
        "Nazca and Wari to the Inca — states built without the wheel, the arch or a "
        "writing system as usually defined.",
    # ── Oceania ──────────────────────────────────────────────────────────────
    "oceania": "Australia, New Guinea and the Pacific islands: the longest continuous "
        "cultural traditions known, alongside the last major human migration, which "
        "settled the remotest islands on Earth by deliberate open-ocean voyaging.",
    "oceania.australia": "The continent held by Aboriginal and Torres Strait Islander "
        "peoples for tens of thousands of years before British colonisation.",
    "oceania.melanesia": "New Guinea and the islands east of it, among the most "
        "linguistically diverse places on Earth and an independent centre of "
        "agricultural origin.",
    "central-asia.tibet": "The plateau and the Himalaya: the Tibetan Empire that once "
        "rivalled Tang China, and the Buddhist polity that followed it.",
    "africa.central": "The Congo basin and its forests, where the Kingdom of Kongo and "
        "the Luba and Lunda states formed. Thinly represented here relative to its "
        "importance, which is a gap in this dataset rather than in the history.",
    "americas.intermediate": "The isthmus and the Caribbean, between the Mesoamerican and "
        "Andean worlds and connected to both.",
    "americas.amazon-southern": "Amazonia and the southern cone, including the earthworks "
        "and managed forests that overturned the idea of the basin as untouched wilderness.",
    "oceania.micronesia": "The small islands of the western Pacific, including the "
        "megalithic city of Nan Madol built on artificial islets.",
    "oceania.polynesia": "The triangle from Hawaii to New Zealand to Rapa Nui, settled "
        "by navigators who crossed thousands of kilometres of open ocean and, in "
        "several cases, returned.",
}


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}
    missing = [i for i in SUMMARIES if i not in by_id]
    if missing:
        raise KeyError(f"container_summaries: unknown ids {missing}")

    written = 0
    for eid, text in SUMMARIES.items():
        e = by_id[eid]
        # Never overwrite an authored summary; this pass only fills blanks.
        if (e.get("summary") or "").strip():
            continue
        e["summary"] = text
        written += 1
    print(f"Container summaries: {written} written")
