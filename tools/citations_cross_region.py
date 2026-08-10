"""Sources for the nine geographic cross-links that had none.

A cross-link that reaches into another world region is a factual claim: saying
Ptolemaic Egypt belongs under the Hellenistic world, or that the Kushans held
South Asia, asserts something about the past that a reader should be able to
check. Nine such links carried no source at all, and the entities carrying them
had no source either, so there was nothing to check against.

**Links into `global` are excluded on purpose, and are not part of this pass.**
Placing the Mongol Empire under Multi-Regional Empires is this dataset's own
taxonomy, not a claim about the world. Demanding an external citation for the
dataset's classification decisions would be a category error, and the validator
rule added alongside this module is scoped to match -- otherwise every taxonomy
change would need a footnote, the rule would feel arbitrary, and it would end up
grandfathered into uselessness.

Several of these claims look near-tautological -- Ptolemaic Egypt *is* a
Hellenistic kingdom -- and that is exactly why they were never sourced. But
"obvious" is how the unsourced Sarasvati assertion and the wrong Greece and
Macedon dates got in. The cost of a citation on a claim everybody knows is one
line; the cost of the habit of skipping it is on record in this changelog.
"""

S_BRIT_CUSHITE = "britannica-cushite-dynasty"
S_BRIT_NUBIA = "britannica-nubia"
S_BRIT_ACH_EGYPT = "britannica-achaemenid-dynasty-egypt"
S_UCL_DYN27 = "ucl-digital-egypt-dynasty27"
S_BRIT_PTOLEMAIC = "britannica-ptolemaic-dynasty"
S_BRIT_HELLENISTIC_AGE = "britannica-hellenistic-age"
S_BRIT_YUAN_MONGOL = "britannica-mongol-empire-yuan"
S_BRIT_KUSHAN = "britannica-kushan-dynasty"
S_OUP_KUSHAN = "oup-kushan-empire"
S_BRIT_INDO_GREEK = "britannica-indo-greek-kingdom"

CROSS_REGION_SOURCES = [
    {"id": S_BRIT_CUSHITE, "kind": "reference",
     "citation": "'Cushite dynasty', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Cushite-dynasty",
     "note": "The 25th Egyptian dynasty was Kushite, which is the warrant for reaching "
             "it from Kush as well as from Egypt."},
    {"id": S_BRIT_NUBIA, "kind": "reference",
     "citation": "'Nubia', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Nubia",
     "note": "Shabaka conquered all of Egypt about 715 BCE, moved his capital to "
             "Memphis, and founded the 25th dynasty, 'called Kushite in the king lists'."},
    {"id": S_BRIT_ACH_EGYPT, "kind": "reference",
     "citation": "'Achaemenid dynasty (Egypt)', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Achaemenid-dynasty",
     "note": "'In ancient Egypt, the 27th dynasty (525-404 BCE), established after Egypt "
             "was conquered by the Persian Achaemenian Empire.'"},
    {"id": S_UCL_DYN27, "kind": "reference",
     "citation": "'27th Dynasty', Digital Egypt, University College London",
     "url": "https://www.ucl.ac.uk/museums-static/digitalegypt/chronology/dynasty27.html",
     "note": "'In the Hellenistic kinglists this is the term for the first period of "
             "Achaemenid Persian rule over Egypt, 525-404 BC.'"},
    {"id": S_BRIT_PTOLEMAIC, "kind": "reference",
     "citation": "'Ptolemaic dynasty', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Ptolemaic-dynasty",
     "note": "'Ptolemaic Egypt was the wealthiest of the kingdoms that emerged in the "
             "aftermath of Alexander the Great's death... and the last to fall under "
             "direct Roman dominion.'"},
    {"id": S_BRIT_HELLENISTIC_AGE, "kind": "reference",
     "citation": "'Hellenistic age', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/event/Hellenistic-Age",
     "note": "Defines the age as running from Alexander's death in 323 BCE to Rome's "
             "conquest of Egypt in 30 BCE, and names the Antigonid, Seleucid and "
             "Ptolemaic kingdoms as its three powers."},
    {"id": S_BRIT_YUAN_MONGOL, "kind": "reference",
     "citation": "'Mongol empire: The Yuan dynasty in China', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Mongol-empire/The-Yuan-dynasty-in-China-1279-1368",
     "note": "Treats the Yuan as the Chinese component of the Mongol empire."},
    {"id": S_BRIT_KUSHAN, "kind": "reference",
     "citation": "'Kushan dynasty', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Kushan-dynasty",
     "note": "'Ruled over most of the northern Indian subcontinent, Afghanistan, and "
             "parts of Central Asia during the first three centuries of the Common Era.'"},
    {"id": S_OUP_KUSHAN, "kind": "scholarly",
     "citation": "'The Kushan Empire', Oxford University Press",
     "url": "https://academic.oup.com/book/39071/chapter/338392096?searchresult=1",
     "note": "Gives the extent as covering Afghanistan and Pakistan entirely and 'much "
             "of northern and central India'."},
    {"id": S_BRIT_INDO_GREEK, "kind": "reference",
     "citation": "'Indo-Greek kingdom', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Indo-Greek-kingdom",
     "note": "Descended from Greco-Bactrian rule; 'Hellenistic influence on the culture "
             "of Central Asia and northwestern India has been considerable.'"},
]

# entity id -> sources that warrant its cross-region placement
WARRANTS = {
    "africa.nile.egypt.tip.dyn25-kushite": [S_BRIT_CUSHITE, S_BRIT_NUBIA],
    "africa.nile.egypt.late-period.dyn27-persian1": [S_BRIT_ACH_EGYPT, S_UCL_DYN27],
    "africa.nile.egypt.ptolemaic": [S_BRIT_PTOLEMAIC, S_BRIT_HELLENISTIC_AGE],
    "africa.nile.egypt.roman-byzantine": [S_BRIT_HELLENISTIC_AGE],
    "east-asia.china.yuan": [S_BRIT_YUAN_MONGOL],
    "west-asia.iran.seleucid": [S_BRIT_HELLENISTIC_AGE],
    "europe.mediterranean.macedon.alexander": [S_BRIT_HELLENISTIC_AGE],
    "central-asia.kushan": [S_BRIT_KUSHAN, S_OUP_KUSHAN],
    "south-asia.indo-greek": [S_BRIT_INDO_GREEK],
}


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}
    done = 0
    for eid, warrant in WARRANTS.items():
        e = by_id.get(eid)
        if e is None:
            continue
        e["source_ids"] = sorted(set(e.get("source_ids", [])) | set(warrant))
        done += 1
    print(f"Cross-region citations: {done} geographic placements now sourced")
