"""Co-rulers and regents, as typed links rather than something the reader must infer.

Prompted by a review note: the ruler model has to cope with more than one person holding
power at once — multiple rulers in a single year, and a regent alongside a nominal
monarch. Checking what the dataset could already express was more interesting than
expected.

**Simultaneity was already representable and already represented.** Twenty-six reigns
have identical start and end years, which is how the Year of the Four Emperors works here:
Otho and Vitellius both sit at 69, Pertinax and Didius Julianus both at 193. Twenty-nine
parent-and-year buckets hold two or more reigns beginning together — Hatshepsut with
Thutmose III, Marcus Aurelius with Lucius Verus, Cleopatra VII with Ptolemy XIII, Cixi
with the Tongzhi emperor.

**What was missing is any statement of the relationship.** The schema has had
`co_ruler_with` and `regent_for` link types the whole time and **neither had ever been
used**. The relationship was left for the reader to infer from overlapping dates, or
smuggled into a name string — the dataset's one regency was recorded as the entity
*"Merneith (regent)"*, with the regency in the label and no link saying regent for whom.

Now that `links` renders, these become visible statements. The nuances are worth having:

* Marcus Aurelius and Lucius Verus were **the first joint Augusti**, and Oxford's
  classical dictionary records Verus as equal "in all respects except for the position of
  pontifex maximus" — formally equal, practically not, which is exactly the kind of thing
  a bare date overlap cannot say.
* Hatshepsut was **first regent for Thutmose III and then his co-ruler**, having had
  herself crowned. Both relationships are recorded, because the sequence is the point.
* Cixi was regent for **two** emperors, her son and her adopted nephew, across nearly
  half a century, and shared the office with Ci'an until 1881.
"""

S_BRIT_MARCUS = "britannica-marcus-aurelius"
S_OUP_VERUS = "oup-lucius-verus"
S_BRIT_HATSHEPSUT = "britannica-hatshepsut"
S_BRIT_THUTMOSE3 = "britannica-thutmose-iii"
S_BRIT_CIXI = "britannica-cixi"

CO_RULER_SOURCES = [
    {"id": S_BRIT_MARCUS, "kind": "reference",
     "citation": "'Marcus Aurelius', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/biography/Marcus-Aurelius-Roman-emperor",
     "note": "Marcus insisted his adoptive brother be made coemperor: for the first time "
             "the empire had two joint emperors of formally equal constitutional status."},
    {"id": S_OUP_VERUS, "kind": "scholarly",
     "citation": "'Verus, Lucius, Roman emperor, 161-169 CE', Oxford Classical Dictionary "
                 "(Oxford Academic)",
     "url": "https://academic.oup.com/edited-volume/61673/chapter-abstract/548207304",
     "note": "The first joint Augustus, 'equal in all respects except for the position of "
             "pontifex maximus'."},
    {"id": S_BRIT_HATSHEPSUT, "kind": "reference",
     "citation": "'Hatshepsut', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/biography/Hatshepsut",
     "note": "Coregent c.1479-73 BCE and king in her own right c.1473-58; she and Thutmose "
             "III were corulers with Hatshepsut 'very much the dominant king'."},
    {"id": S_BRIT_THUTMOSE3, "kind": "reference",
     "citation": "'Thutmose III', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/biography/Thutmose-III",
     "note": "Hatshepsut acted as regent, then assumed the attributes and insignia of a "
             "king and 'to all intents and purposes reigned in his stead'."},
    {"id": S_BRIT_CIXI, "kind": "reference",
     "citation": "'Cixi', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/biography/Cixi",
     "note": "Mother of the Tongzhi emperor and adoptive mother of the Guangxu emperor; "
             "regent before each came of age and influential long after."},
]

# (a, b, type, note on a, note on b or None if one-directional, sources)
RELATIONSHIPS = [
    ("europe.mediterranean.rome.empire.marcus-aurelius",
     "europe.mediterranean.rome.empire.lucius-verus",
     "co_ruler_with",
     "Insisted his adoptive brother be made coemperor, creating the first joint rule in "
     "Roman history.",
     "Equal in constitutional status but not in authority: equal in all respects except "
     "pontifex maximus, which Marcus kept.",
     [S_BRIT_MARCUS, S_OUP_VERUS]),
    ("africa.nile.egypt.new-kingdom.dyn18.hatshepsut",
     "africa.nile.egypt.new-kingdom.dyn18.thutmose3",
     "co_ruler_with",
     "Corulers after she had herself crowned, with Hatshepsut the dominant of the two.",
     "Nominally king from 1479 BCE, but Hatshepsut reigned in his stead for roughly two "
     "decades.",
     [S_BRIT_HATSHEPSUT, S_BRIT_THUTMOSE3]),
    ("africa.nile.egypt.new-kingdom.dyn18.hatshepsut",
     "africa.nile.egypt.new-kingdom.dyn18.thutmose3",
     "regent_for",
     "Regent for her stepson from his accession, before taking the kingship outright.",
     None,
     [S_BRIT_HATSHEPSUT, S_BRIT_THUTMOSE3]),
    ("east-asia.china.qing.cixi", "east-asia.china.qing.tongzhi",
     "regent_for",
     "Regent for her six-year-old son from 1861, initially sharing the office with Ci'an.",
     None, [S_BRIT_CIXI]),
    ("east-asia.china.qing.cixi", "east-asia.china.qing.guangxu",
     "regent_for",
     "Regent again for her adopted three-year-old nephew, sole holder of the office after "
     "Ci'an's death in 1881.",
     None, [S_BRIT_CIXI]),
]


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}

    def add_link(a, b, kind, note, warrant):
        entity = by_id.get(a)
        if entity is None or b not in by_id:
            raise KeyError(f"co_rulers: cannot link {a} -> {b}; check the ids")
        links = list(entity.get("links", []))
        if any(l["entity_id"] == b and l["type"] == kind for l in links):
            return
        links.append({"type": kind, "entity_id": b, "note": note})
        entity["links"] = links
        entity["source_ids"] = sorted(set(entity.get("source_ids", [])) | set(warrant))

    made = 0
    for a, b, kind, note_a, note_b, warrant in RELATIONSHIPS:
        add_link(a, b, kind, note_a, warrant)
        made += 1
        # `co_ruler_with` is symmetric in meaning, so it is written both ways. `regent_for`
        # is not -- the monarch was not regent for the regent -- and is left directional.
        if kind == "co_ruler_with" and note_b is not None:
            add_link(b, a, kind, note_b, warrant)

    # The one regency already in the dataset hid the relationship in the entity's name.
    merneith = by_id.get("africa.nile.egypt.early-dynastic.dyn1.merneith")
    if merneith is not None:
        prior = (merneith.get("date_note") or "").strip()
        extra = ("Recorded here as a regency in the name itself. Whom she was regent for is "
                 "not modelled, because the First Dynasty succession is too uncertain to "
                 "assert it.")
        if extra not in prior:
            merneith["date_note"] = f"{prior} {extra}".strip()

    print(f"Co-rulers and regents: {made} relationships typed "
          f"(co_ruler_with and regent_for had never been used)")
