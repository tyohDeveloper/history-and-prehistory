"""Grade how much standing a topic itself has, separately from its dating.

`date_standing` says how settled the dates are. Nothing said how settled the *subject* was,
so Dangun and Hammurabi looked alike on that axis while differing about as much as two
entries can: one is a founding figure from a thirteenth-century chronicle, the other left a
law code carved in diorite.

The two axes are independent, which is the reason for a second field rather than a wider
first one. Dangun is `mythological` with a `traditional` dating -- the 2333 BCE figure is a
real convention, precisely recorded, about a person who very likely never lived. The
Lomekwian industry is the reverse: nobody disputes that the flakes exist, while the 3.3 Ma
date is genuinely argued. And a Sumerian King List reign can be a legendary person with
fictional numbers, failing on both axes at once.

Values, from weakest claim to strongest:

- ``mythological`` -- a figure or event of myth, not presented as history by scholarship.
  Fuxi is described in the sources themselves as a god-king.
- ``legendary`` -- tradition presents this as historical and scholarship doubts or cannot
  verify it. Romulus, Dangun, Gilgamesh-as-king.
- ``contested`` -- specialists actively disagree about whether the thing existed or is a
  coherent category. The Xia dynasty, Gojoseon, the Toltec empire.
- ``reconstructed`` -- known only by inference from indirect evidence, never attested
  directly. Proto-languages above all, and population movements read from genetics.
- ``interpretive`` -- the thing is real enough but the *category* is a modern scholarly
  construct, and one that is itself argued about. The Axial Age is the clearest case.
- omitted -- accepted. Which is most of the dataset, and saying so on 1,700 entities would
  be noise.

Assignments are explicit rather than inferred. An earlier version of this module planned to
read the `contested-existence` caveats and promote them automatically, which would have
graded Cicero and Pompey as contested: eleven such caveats existed whose entire text was the
word "omit", imported from a research file where the writer had typed the instruction into
the field. Inference from a signal that turns out to be dirty produces confident nonsense, so
every value here is stated by hand and the ids are asserted to exist.
"""

MYTHOLOGICAL = {
    "east-asia.china.legendary.fuxi",
    "east-asia.china.legendary.shennong",
    "east-asia.china.legendary.huangdi",
    "east-asia.china.legendary.zhuanxu",
    "east-asia.china.legendary.emperor-ku",
    "east-asia.china.legendary.emperor-yao",
    "east-asia.china.legendary.emperor-shun",
    "east-asia.korea.gojoseon.dangun",
}

LEGENDARY = {
    # Rome's seven kings. Livy and Dionysius wrote centuries later, and the regnal lengths
    # average an implausible thirty-five years apiece.
    "europe.mediterranean.rome.kingdom.romulus",
    "europe.mediterranean.rome.kingdom.numa-pompilius",
    "europe.mediterranean.rome.kingdom.tullus-hostilius",
    "europe.mediterranean.rome.kingdom.ancus-marcius",
    "europe.mediterranean.rome.kingdom.tarquinius-priscus",
    "europe.mediterranean.rome.kingdom.servius-tullius",
    "europe.mediterranean.rome.kingdom.tarquinius-superbus",
    "west-asia.mesopotamia.sumerian.gilgamesh",
    "africa.nile.egypt.old-kingdom.dyn6.nitocris",
    "east-asia.china.legendary",
}

CONTESTED = {
    "east-asia.china.xia",
    "east-asia.korea.gojoseon",
    "americas.mesoamerica.toltec",
    "southeast-asia.mainland.funan",
    "central-asia.sogdia",
    "central-asia.hephthalites",
    "southeast-asia.mainland.dvaravati",
    # The united monarchy's scale, not the names, is what is argued about.
    "west-asia.mesopotamia.israel-judah.david",
    "west-asia.mesopotamia.israel-judah.solomon",
    # Narmer and Menes may or may not be the same man.
    "africa.nile.egypt.early-dynastic.dyn1.narmer",
}

RECONSTRUCTED = {
    "europe.prehistory.farmer-turnover",
    "southeast-asia.prehistory.austronesian-expansion",
}

INTERPRETIVE = {
    # Categories that are themselves the argument.
    "global.mesolithic",
    "global.neolithic.agricultural-revolution",
    "global.bce",
    "global.ce",
}

ASSIGNMENTS = [
    ("mythological", MYTHOLOGICAL),
    ("legendary", LEGENDARY),
    ("contested", CONTESTED),
    ("reconstructed", RECONSTRUCTED),
    ("interpretive", INTERPRETIVE),
]


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}
    missing = []
    counts = {}

    for value, ids in ASSIGNMENTS:
        applied = 0
        for eid in sorted(ids):
            e = by_id.get(eid)
            if e is None:
                missing.append(eid)
                continue
            e["historicity"] = value
            applied += 1
        counts[value] = applied

    print("historicity: " + ", ".join(f"{v} {n}" for v, n in counts.items()))
    if missing:
        # Loud rather than silent. Guessing ids has been the single most common error in this
        # project, and a typo here would quietly grade nothing at all.
        raise KeyError(f"historicity: {len(missing)} id(s) do not exist: {missing}")
