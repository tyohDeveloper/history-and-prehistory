"""The Vedic period: 1,000 years in one block, over the most contested ground here.

`coverage.py` flagged Vedic Period as a childless 1500-500 BCE block. Filling it
needs more care than the other gaps, for two reasons.

**The dating is textual, not excavated.** The Rigveda and the later texts are
dated by internal linguistic evidence -- comparative philology, the Mitanni
synchronism, the relative stratigraphy of the language itself. That is a completely
different kind of claim from a radiocarbon date, and this dataset already
distinguishes dating methods precisely so the difference can be stated instead of
smoothed away.

These entities carry **`received`**, not `typological`, and the first attempt got
this wrong. `typological` puts a date on the scientific side of the frame rule, so
the readout rendered the Vedic period as **"3,449 - 2,449 BP"** -- years before
present, for a period every source in the world expresses in BCE. That is the same
failure as Chaco Canyon rendering as "1,100 - 700 BP", which the `dendrochronology`
work was added to fix.

`received` is also the more accurate description. The schema defines it as a date
"arrived at by transmission rather than by measurement or attestation" and cites
typology-derived brackets as an example. A date inferred from the internal
stratigraphy of a language and handed down through scholarship is exactly that.

**The Indo-Aryan migration question is genuinely contested and politically
loaded**, and the dataset's job is to represent the dispute rather than to settle
it. Three claims get conflated in public argument and are kept apart here:

* a *linguistic* claim, that Indo-Aryan arrived from outside;
* an *archaeological* claim, about material continuity or its absence;
* a *genetic* claim, about steppe ancestry in modern and ancient genomes.

The genetics entity already exists in this dataset, sourced, at
`south-asia.steppe-ancestry` -- so the Vedic node links to it rather than
re-litigating it, and the caveats name proponents on both sides instead of
gesturing at "some scholars".

**The end date is a convention about language, not about politics.** 500 BCE is
tied to Panini and the close of the Vedic corpus; the political and economic
transition -- the mahajanapadas, the second urbanisation, the Buddha and Mahavira
-- is more consistently dated around 600 BCE. Both are recorded, and the existing
Mahajanapadas node already begins at 600, so the overlap is now explicit rather
than an accidental gap.

**Painted Grey Ware belongs to the Later Vedic phase only**, not to the period as
a whole -- a distinction the single block silently erased.
"""

S_BRIT_INDIA_HIST = "britannica-india-history"
S_BRIT_VEDIC = "britannica-vedic-religion"
S_WITZEL_EJVS = "witzel-early-indian-history-linguistic"
S_NARASIMHAN = "narasimhan-2019-genomic-formation"
S_THAPAR_EARLY = "thapar-early-india"
S_BRYANT = "bryant-quest-origins-vedic-culture"
S_PGW = "pgw-archaeology"
S_BRIT_MAHAJANAPADA = "britannica-mahajanapada"

VEDIC_SOURCES = [
    {"id": S_BRIT_INDIA_HIST, "kind": "reference",
     "citation": "'India: History', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/India/History",
     "note": "The conventional Early and Later Vedic division and the transition to the "
             "mahajanapadas."},
    {"id": S_BRIT_VEDIC, "kind": "reference",
     "citation": "'Vedic religion', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Vedic-religion",
     "note": "The corpus and its ordering: Rigveda, the other Vedas, Brahmanas, "
             "Upanishads."},
    {"id": S_WITZEL_EJVS, "kind": "scholarly",
     "citation": "Witzel, 'Early Indian history: linguistic and textual parameters', "
                 "Electronic Journal of Vedic Studies",
     "url": "https://web.archive.org/web/20180527150828/http:/www.people.fas.harvard.edu/~witzel/EJVS-7-3.htm",
     "note": "The linguistic-stratigraphic case for dating the Vedic texts, and a "
             "three-stage subdivision of the Rigvedic period."},
    {"id": S_NARASIMHAN, "kind": "scholarly",
     "citation": "Narasimhan et al., 'The formation of human populations in South and "
                 "Central Asia', Science (2019)",
     "url": "https://reich.hms.harvard.edu/sites/reich.hms.harvard.edu/files/inline-files/eaat7487.full_.pdf",
     "note": "Ancient DNA evidence for steppe ancestry entering South Asia in the second "
             "millennium BCE. A genetic claim, which does not by itself date a text or "
             "identify a language."},
    {"id": S_THAPAR_EARLY, "kind": "scholarly",
     "citation": "Thapar, Early India: From the Origins to AD 1300",
     "url": "https://www.ucpress.edu/books/early-india/paper",
     "note": "The mainstream account of Vedic society and a qualified discontinuity "
             "reading of the Indus-to-Vedic transition."},
    {"id": S_BRYANT, "kind": "scholarly",
     "citation": "Bryant, The Quest for the Origins of Vedic Culture (Oxford, 2001)",
     "url": "https://academic.oup.com/book/9484/chapter/156449269",
     "note": "A survey that sets out the Indigenous Aryan arguments and the mainstream "
             "replies without adopting either, and is cited by both sides."},
    {"id": S_PGW, "kind": "scholarly",
     "citation": "Studies of the Painted Grey Ware horizon",
     "url": "https://hal.science/hal-03097955v1/document",
     "note": "Associates Painted Grey Ware with the Later Vedic phase specifically, "
             "roughly 1200-600 BCE, rather than with the whole Vedic period."},
    {"id": S_BRIT_MAHAJANAPADA, "kind": "reference",
     "citation": "'Mahajanapada', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/mahajanapada",
     "note": "The sixteen great realms and the second urbanisation of the Ganges plain."},
]


def extend(E, entities):
    from builders import make_builders

    by_id = {e["id"]: e for e in entities}
    _, P, ERA, _, _, _ = make_builders(E, id_prefix="south-asia.vedic")
    V = "south-asia.vedic"

    v = by_id.get(V)
    if v is None:
        return

    v["tier"] = "foundational"
    v["summary"] = ("The period of the Vedic corpus in northern South Asia, dated from "
                    "the texts rather than from excavation.")
    v["date_note"] = (
        "Both ends are conventions and neither is measured. The 1500 BCE start rests on "
        "linguistic dating of the Rigveda, not on a datable event or layer. The 500 BCE "
        "end is tied to Panini and the closing of the corpus -- a fact about language; "
        "the political and economic transition to the mahajanapadas and the second "
        "urbanisation is more consistently dated around 600 BCE, and this dataset's "
        "Mahajanapadas entity begins there, so the two deliberately overlap.")
    v["date_precision"] = "approx"
    v["start_dating_method"] = "received"
    v["source_ids"] = [S_BRIT_INDIA_HIST, S_WITZEL_EJVS, S_THAPAR_EARLY]
    v["alternatives"] = [
        {"label": "Ends c. 600 BCE, on the political transition", "standing": "majority",
         "end_year": -600, "dating_method": "received",
         "note": "The mahajanapadas, the second urbanisation, the Buddha and Mahavira.",
         "source_ids": [S_BRIT_INDIA_HIST, S_BRIT_MAHAJANAPADA]},
    ]
    v["caveats"] = [
        {"kind": "misconception",
         "text": "Dated by comparative linguistics and internal textual evidence, not by "
                 "excavation. These texts are not archaeological layers.",
         "source_ids": [S_WITZEL_EJVS]},
        {"kind": "contested-existence",
         "text": "How Indo-Aryan speech arrived is disputed: Witzel, Parpola and "
                 "Anthony argue steppe migration; Talageri, Elst and Danino argue "
                 "against it. Bryant surveys both.",
         "source_ids": [S_WITZEL_EJVS, S_BRYANT]},
        {"kind": "contested-existence",
         "text": "Three claims get merged here: language origin, material continuity, "
                 "and steppe ancestry in genomes. Evidence for one is not evidence "
                 "for another.",
         "source_ids": [S_NARASIMHAN, S_BRYANT]},
    ]
    # The genetics already exist here, sourced. Link rather than re-argue.
    v["links"] = sorted(
        (v.get("links") or []) + [
            # `other` rather than a stronger type on purpose. Saying the genetics are
            # "part of" or "predecessor to" the Vedic period would assert the very
            # connection that is disputed. The link says only: this is related and a
            # reader should see it.
            {"entity_id": "south-asia.steppe-ancestry", "type": "other",
             "note": "The genetic evidence, which is a separate claim from the "
                     "linguistic and archaeological ones."},
        ],
        key=lambda l: l["entity_id"])

    P("rigvedic", "Early Vedic (Rigvedic)", V, -1500, -1000, "foundational",
      summary="The period of the Rigveda: pastoral, mobile, and in the northwest.",
      date_note="Dated linguistically. Witzel subdivides the Rigvedic period into three "
                "stages on the internal stratigraphy of the language. No excavated "
                "horizon dates these texts.",
      source_ids=[S_WITZEL_EJVS, S_BRIT_VEDIC],
      start_dating_method="received", date_precision="approx")
    P("later-vedic", "Later Vedic", V, -1000, -500, "foundational",
      summary="Eastward settlement into the Ganges plain, iron, larger polities, and the "
              "Brahmanas and early Upanishads.",
      date_note="The Painted Grey Ware horizon is associated with this phase in "
                "particular, roughly 1200-600 BCE — not with the Vedic period as a "
                "whole, which is what a single undivided block implied.",
      source_ids=[S_BRIT_INDIA_HIST, S_PGW, S_THAPAR_EARLY],
      start_dating_method="received", date_precision="approx")
    ERA("corpus", "The Vedic Corpus", V, -1500, -500, "intermediate",
        summary="Rigveda, then the other three Vedas, the Brahmanas, and the Upanishads.",
        date_note="Relative order is firm; absolute dates are not. The Rigveda is the "
                  "best anchored, partly through the Mitanni synchronism; the Upanishads "
                  "are the least, with proposals spanning 700 BCE to 100 CE.",
        source_ids=[S_BRIT_VEDIC, S_WITZEL_EJVS],
        start_dating_method="received", date_precision="approx")

    m = by_id.get("south-asia.mahajanapadas")
    if m is not None:
        m["source_ids"] = sorted(set(m.get("source_ids", [])) | {S_BRIT_MAHAJANAPADA,
                                                                 S_BRIT_INDIA_HIST})
        m["date_note"] = (
            "Overlaps the Later Vedic period on purpose: the second urbanisation is "
            "under way while the Vedic corpus is still closing, and the conventional "
            "Vedic end date of 500 BCE describes the language rather than the "
            "politics.").strip()

    print("Vedic: Early and Later split, corpus dated typologically, migration dispute")
