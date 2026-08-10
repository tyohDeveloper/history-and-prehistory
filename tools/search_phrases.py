"""Author `search_phrase` where the entity's own name is a poor thing to search for.

The app is a starting point rather than a research tool, so the handoff to a real search matters
more than most features. `handoff.searchQuery` already builds a query and appends an ancestor's
name when the entity's name collides with another *inside this dataset*.

That test is the wrong one, and the Japanese eras show why. `Wadō` appears once, so nothing
flags it, and the generated query is the bare word `Wadō` -- which outside this app is a Japanese
coin, a martial arts style, and several companies. `Shōwa` appears twice and therefore does get
context. The two eras are equally useless as bare queries and only one was fixed, because the
rule measured ambiguity in the wrong universe: what matters is whether the name is ambiguous in
the world, not whether it is ambiguous here.

So this module supplies phrases where a rule can state the domain a name needs, and hand-authors
the rest. What it does not do is add a phrase to everything: `Silk Road`, `Proto-Semitic` and
`Hadrian` are already the best queries available for those things, and a `search_phrase` that
merely restates the name is one more field to keep in sync for no gain.
"""

# Hand-authored, for entities where no rule would produce the right phrase.
EXPLICIT = {
    # Two entities called Apollo 11, one a Moon landing and one a cave in Namibia holding some
    # of the oldest known figurative art. A search for either name alone finds the spacecraft.
    "africa.prehistory.apollo-11-cave": "Apollo 11 Cave Namibia rock art",
    "africa.nile.egypt.predynastic.dynasty-0": "Dynasty 0 Egypt predynastic rulers",
    "global.contemporary": "contemporary history since 1991",
    "global.bce": "BCE Before Common Era dating",
    "global.ce": "CE Common Era dating",
    "global.multi-regional": "multi-regional empires world history",
    "west-asia.mesopotamia.israel-judah.david": "King David united monarchy historicity",
    "west-asia.mesopotamia.israel-judah.solomon": "King Solomon united monarchy historicity",
    "east-asia.china.legendary": "Three Sovereigns Five Emperors Chinese mythology",
    "east-asia.korea.gojoseon.dangun": "Dangun Wanggeom Gojoseon foundation myth",
    "global.languages.old-chinese": "Old Chinese reconstruction Shijing rhymes",
    "global.languages.classical-maya": "Classical Maya script decipherment",
    "global.traditions.great-schism": "East-West Schism 1054",
    "global.traditions.sunni-shia-split": "Sunni Shia split succession to Muhammad",
    "global.milestones.zero-as-number": "Brahmagupta zero as a number Brahmasphutasiddhanta",
    "global.milestones.movable-type": "Bi Sheng movable type Song dynasty",
    "global.milestones.packet-switching": "ARPANET packet switching 1969",
    "americas.andes": "Andes region history archaeology",
}

# Rules, applied where the branch tells you what domain the name belongs to. Each maps a
# (predicate, suffix) so the phrase says what kind of thing the name is.
BRANCH_SUFFIX = [
    ("east-asia.japan.", "period", "Japanese era name"),
    ("east-asia.japan.", "reign", "shogun Japan"),
    ("africa.nile.egypt.", "reign", "pharaoh Egypt"),
    ("west-asia.mesopotamia.", "reign", "Mesopotamian ruler"),
    ("americas.", "reign", "ruler"),
    ("oceania.", "reign", "ruler"),
]


def _needs_help(entity):
    """A single-token name is the case where a bare query goes wrong."""
    name = entity["name"]
    if len(name.split()) != 1:
        return False
    # A long distinctive name stands on its own: nobody searching "Nebuchadnezzar" gets a coin.
    return len(name) <= 9


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}
    explicit = 0
    derived = 0
    missing = []

    for eid, phrase in EXPLICIT.items():
        e = by_id.get(eid)
        if e is None:
            missing.append(eid)
            continue
        e["search_phrase"] = phrase
        explicit += 1

    for e in entities:
        if e.get("search_phrase"):
            continue
        if not _needs_help(e):
            continue
        for prefix, kind, suffix in BRANCH_SUFFIX:
            if e["id"].startswith(prefix) and e["kind"] == kind:
                e["search_phrase"] = f"{e['name']} {suffix}"
                derived += 1
                break

    print(f"search_phrases: {explicit} authored, {derived} derived from branch and kind")
    if missing:
        raise KeyError(f"search_phrases: {len(missing)} id(s) do not exist: {missing}")
