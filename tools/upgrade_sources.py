"""Replace Wikipedia citations where a better source was available and simply not used.

Prompted by a review note: don't lean on Wikipedia, but a page that surfaces in a search
is worth examining. The second half is the sharper point. The first pass here sourced all
seven kings of Rome to a **single Wikipedia article**, and several Korean kings to
**Simple English Wikipedia**, which is a worse reference than ordinary Wikipedia. Better
sources had been available the whole time and were not opened.

Checking directly found Britannica biographies for five of the seven kings and a World
History Encyclopedia article on Gwanggaeto. Two Britannica URLs returned 404 —
`Lucius-Tarquinius-Priscus` and `Lucius-Tarquinius-Superbus` — so those two keep the
Wikipedia citation, recorded here rather than papered over.

Upgrading also surfaced disagreements that the Wikipedia-only sourcing had hidden.
Britannica's Varro-based regnal years differ from the table the first pass used, by one
year for Numa and Tullus Hostilius and by **two years at both ends for Ancus Marcius**.
The stored dates are kept, because the traditional chronology has no single correct form,
and the disagreement goes in the date note where a reader can see it. A citation that
quietly disagrees with the date attached to it is worse than no citation.

Britannica is also more forthright about historicity than the summary table was:

* Tullus Hostilius is "a legendary figure, the legend probably influenced by that of
  Romulus".
* Ancus Marcius's reign "must be regarded as largely legendary".
* The 14 books of pontifical law attributed to Numa were "clearly forgeries".
* The emperor Claudius, writing as an Etruscan historian, said Servius Tullius was an
  Etruscan interloper named Mastarna.

Those are better than anything the first pass captured, and they are the reason to open
the page rather than take the first result.
"""

# Verified by fetching each URL. The two Tarquins are absent from Britannica under these
# slugs and keep their existing citation.
KING_SOURCES = [
    {"id": "britannica-romulus-remus", "kind": "reference",
     "citation": "'Romulus and Remus', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/biography/Romulus-and-Remus",
     "note": "Treats them as the legendary founders; the legend probably originated in the "
             "4th century BCE and was set down at the end of the 3rd."},
    {"id": "britannica-numa-pompilius", "kind": "reference",
     "citation": "'Numa Pompilius', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/biography/Numa-Pompilius",
     "note": "Reigned 715-673 BCE by tradition. The religious institutions credited to him "
             "were centuries of accretion, and the law books attributed to him were "
             "forgeries."},
    {"id": "britannica-tullus-hostilius", "kind": "reference",
     "citation": "'Tullus Hostilius', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/biography/Tullus-Hostilius",
     "note": "Reigning 672-641 BCE traditionally. 'A legendary figure, the legend probably "
             "influenced by that of Romulus.'"},
    {"id": "britannica-ancus-marcius", "kind": "reference",
     "citation": "'Ancus Marcius', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/biography/Ancus-Marcius",
     "note": "Traditionally fourth king, 642-617 BCE. The details of his reign 'must be "
             "regarded as largely legendary'."},
    {"id": "britannica-servius-tullius", "kind": "reference",
     "citation": "'Servius Tullius', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/biography/Servius-Tullius",
     "note": "Flourished 578-535 BCE. The Servian reforms may be later changes read back "
             "into an uncertain past; Claudius called him an Etruscan named Mastarna."},
]

KOREA_SOURCES = [
    {"id": "worldhistory-gwanggaeto", "kind": "reference",
     "citation": "Mark Cartwright, 'Gwanggaeto the Great', World History Encyclopedia",
     "url": "https://www.worldhistory.org/Gwanggaeto_the_Great/",
     "note": "Reigned 391-413 CE, died 413; his son Jangsu reigned to 491 and raised the "
             "stele in 414 that is the earliest known Korean inscription."},
    {"id": "britannica-goguryeo", "kind": "reference",
     "citation": "'Goguryeo', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Goguryeo",
     "note": "Gives Gwanggaeto 391-412 and Jangsu 413-491. Notes Goguryeo's traditional "
             "37 BCE founding is later than historians accept, favouring the 2nd century BCE."},
]

UPGRADE_SOURCES = KING_SOURCES + KOREA_SOURCES

# entity id -> (source ids to add, note recording any disagreement)
UPGRADES = {
    "europe.mediterranean.rome.kingdom.romulus": (
        ["britannica-romulus-remus"], None),
    "europe.mediterranean.rome.kingdom.numa-pompilius": (
        ["britannica-numa-pompilius"],
        "Britannica gives 715-673; the Varro-based table used here ends the reign in 672. "
        "The traditional chronology has no single correct form."),
    "europe.mediterranean.rome.kingdom.tullus-hostilius": (
        ["britannica-tullus-hostilius"],
        "Britannica gives 672-641 against the 672-640 used here, and calls him a legendary "
        "figure whose legend was probably shaped by Romulus's."),
    "europe.mediterranean.rome.kingdom.ancus-marcius": (
        ["britannica-ancus-marcius"],
        "Britannica gives 642-617, two years earlier at both ends than the figures used "
        "here, and holds that the details of the reign are largely legendary."),
    "europe.mediterranean.rome.kingdom.servius-tullius": (
        ["britannica-servius-tullius"],
        "Britannica records him as flourishing 578-535 rather than reigning to 534, and "
        "notes Claudius identified him as an Etruscan named Mastarna."),
    "east-asia.korea.three-kingdoms.gwanggaeto-the-great": (
        ["worldhistory-gwanggaeto", "britannica-goguryeo"],
        "World History Encyclopedia gives 391-413; Britannica gives 391-412. The one-year "
        "difference turns on whether his death year is counted."),
    "east-asia.korea.three-kingdoms.jangsu": (
        ["britannica-goguryeo", "worldhistory-gwanggaeto"],
        "Britannica gives 413-491, matching the figures used here."),
}

# Kept honest: no Britannica biography exists at the obvious slug for these two, so the
# Wikipedia citation stands rather than being swapped for a worse-fitting page.
NO_BETTER_SOURCE = {
    "europe.mediterranean.rome.kingdom.tarquinius-priscus":
        "No Britannica biography found at the expected URL, so this keeps its "
        "encyclopaedic-summary citation.",
    "europe.mediterranean.rome.kingdom.tarquinius-superbus":
        "No Britannica biography found at the expected URL, so this keeps its "
        "encyclopaedic-summary citation.",
}


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}
    known = {s["id"] for s in UPGRADE_SOURCES}

    upgraded = 0
    for eid, (sids, note) in UPGRADES.items():
        entity = by_id.get(eid)
        if entity is None:
            raise KeyError(f"upgrade_sources: {eid} not found")
        for sid in sids:
            assert sid in known, f"upgrade_sources: unknown source {sid}"
        entity["source_ids"] = sorted(set(entity.get("source_ids", [])) | set(sids))
        if note:
            prior = (entity.get("date_note") or "").strip()
            if note not in prior:
                entity["date_note"] = f"{prior} {note}".strip()
        upgraded += 1

    for eid, note in NO_BETTER_SOURCE.items():
        entity = by_id.get(eid)
        if entity is None:
            raise KeyError(f"upgrade_sources: {eid} not found")
        prior = (entity.get("date_note") or "").strip()
        if note not in prior:
            entity["date_note"] = f"{prior} {note}".strip()

    print(f"Source upgrades: {upgraded} entities moved off Wikipedia-only citations, "
          f"{len(NO_BETTER_SOURCE)} kept with the gap recorded")
