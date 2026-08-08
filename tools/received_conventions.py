"""Dates the field uses but the evidence does not establish.

Some chronologies are worth carrying even though their numbers are not
findings. The Namazga sequence organises the whole of Central Asian prehistory;
every regional synthesis is written in its phases. A reader who looks it up and
finds nothing learns less than one who finds it clearly labelled as a received
framework. The same is true of Rome's 753 BCE, Gojoseon's 2333 BCE, and the
regnal dates of David and Solomon.

The schema has had a word for exactly this since 3.0.0 — `standing:
"traditional"`, described there as covering "received dates such as Rome's 753
BCE founding" which "are not findings, and presenting them with the same weight
as measured or attested dates is the commonest way a history reference
misleads." Until now nothing used it. Rome's Kingdom carried
`date_precision: "traditional"` and no standing at all, and rendered in the
picker identically to a Bayesian-modelled radiocarbon date.

This module does two things: it marks the entities that were already received
conventions, and it authors the ones that were left out of earlier passes
precisely because their dates could not be sourced.

**The label has to lead.** A caveat below the fact list does not reach a reader
who scans the date and moves on, which is most readers. `standing: "traditional"`
now draws a dagger on the range in the column gutter and a banner at the top of
the readout, above the summary. That is what makes including these defensible
rather than a quiet dilution of the sourcing rule.

**What still does not get in.** A received convention has provenance: someone
proposed it, the field adopted it, and it can be named and dated as a
convention. A number that merely circulates without one does not qualify, and
`traditional` must not become a loophole for it.
"""

from builders import make_builders

# Entities that were already received conventions but said so only through
# `date_precision`, which the picker does not surface. Romulus Augustulus is
# deliberately absent: his deposition in 476 is attested, and the `traditional`
# precision there marks the "fall of Rome" convention rather than a legendary
# date for the man.
ALREADY_CONVENTIONAL = [
    "africa.nile.egypt.early-dynastic.dyn1.narmer",
    "africa.nile.egypt.old-kingdom.dyn6.nitocris",
    "east-asia.korea.gojoseon",
    "west-asia.mesopotamia.sumerian.gilgamesh",
    "west-asia.mesopotamia.israel-judah.david",
    "west-asia.mesopotamia.israel-judah.solomon",
    "europe.mediterranean.rome.kingdom",
]

S_NAMAZGA_PROBLEM = "monjukli-depe-bayesian"        # defined in extensions_central_asia
S_SARAZM_DOSSIER = "unesco-sarazm-dossier"          # ditto
S_KELTEMINAR_PNAS = "pnas-2025-central-asia-barley"  # ditto
S_ALTYN_MASSON = "masson-altyn-depe-summary"

RECEIVED_CONVENTION_SOURCES = [
    {"id": S_ALTYN_MASSON, "kind": "reference",
     "citation": "Masson's 1969 excavation summary for Altyn-Depe, trenches 7-9 (BibBase record)",
     "url": "https://bibbase.org/network/publication/masson-summary-1969",
     "note": "Gives Early and Late Namazga V phases for the site; a bibliographic record of the "
             "field report rather than the report itself."},
]


def extend(E, entities):
    _, P, ERA, _, _, _ = make_builders(E)
    by_id = {e["id"]: e for e in entities}

    for eid in ALREADY_CONVENTIONAL:
        e = by_id.get(eid)
        if e is not None:
            e["standing"] = "traditional"
            # Schema 3.1.0. These previously carried no dating method at all,
            # because none of the enum values described how the date was
            # actually arrived at. Their provenance is not unknown — it is
            # annalists and king-lists — it is just not evidence.
            e.setdefault("start_dating_method", "received")
            if e.get("end_year") is not None:
                e.setdefault("end_dating_method", "received")

    pre = "central-asia.prehistory"

    # The whole reason Central Asia's chronology is quotable at all, and the
    # reason it should not be quoted without a warning.
    ERA("namazga", "Namazga Sequence", pre, -4800, -1500, "foundational",
        allow_outside_parent_dates=True,
        summary="The six-phase framework that every account of Central Asian prehistory is "
                "written in, and which rests on pottery typology rather than radiocarbon.",
        aliases=["Namazga I-VI", "Namazga-depe sequence"],
        start_dating_method="received", end_dating_method="received",
        standing="traditional", date_precision="traditional",
        date_note="RECEIVED FRAMEWORK, NOT A DATED ONE. The phases in general circulation are "
                  "Namazga I 4800-4000, II 4000-3500, III 3500-3000, IV 3000-2500, V 2500-2200 "
                  "and VI 2200-1500 BCE, and competing bracket sets exist for most of them. "
                  "They descend from Masson's Soviet-era ceramic typology; no published "
                  "radiocarbon table for Namazga-depe itself supports them. Where independent "
                  "dating does exist it disagrees: modern reassessments compress the Namazga V "
                  "urban phase into roughly 2400-1950 or 2250-1700 BCE, and one report gives "
                  "C14 dates for a single final Namazga VI layer scattering from 1884 to 818 "
                  "BC. Use the phase names to talk to the literature; do not use these numbers "
                  "as dates.",
        caveats=[{"kind": "misconception",
                  "text": "These phase brackets are a typological convention, not measurements. "
                          "Treating Namazga V as a dated period rather than a pottery style is "
                          "the standard error.",
                  "source_ids": [S_NAMAZGA_PROBLEM]}],
        source_ids=[S_NAMAZGA_PROBLEM, S_SARAZM_DOSSIER])

    # Kelteminar is a different case and is NOT marked traditional: a fetched
    # peer-reviewed paper does give it a millennium-scale range, so it has a
    # citable date, just not a site-level one.
    P("kelteminar", "Kelteminar Culture", pre, -6000, -3000, "specialist",
      summary="Hunter-fisher-gatherers of the Aral basin and the Amu Darya delta, in contact "
              "with the farming villages to their south.",
      aliases=["Kel'teminar"],
      start_dating_method="typological", end_dating_method="typological",
      standing="minority", date_precision="millennium",
      date_note="A peer-reviewed source places Kelteminar in the sixth to fourth millennia BC "
                "in general terms, and that is the whole of the defensible dating. No "
                "site-level radiocarbon dataset with lab numbers was locatable for any "
                "Kelteminar site, and the field disagrees about the culture's geographic and "
                "temporal boundaries — the authors of that paper decline to label their own "
                "9200-7800 cal BP material at Toda-1 Cave as Kelteminar for that reason.",
      source_ids=[S_KELTEMINAR_PNAS])

    P("altyn-depe", "Altyn-Depe", pre, -2100, -1650, "specialist",
      summary="A walled town of the Namazga culture with a stepped tower, craft quarters and "
              "trade reaching Mundigak and Shahr-i Sokhta.",
      start_dating_method="received", end_dating_method="received",
      standing="traditional", date_precision="traditional",
      date_note="Dated by its Namazga V pottery, so it inherits that sequence's problem "
                "entirely. The excavator's own figures — Early Namazga V c. 2100-1850 BC, Late "
                "c. 1850-1650 — are typological. No modern radiocarbon programme for the site "
                "was locatable, so nothing here is independent of the ceramic framework.",
      source_ids=[S_ALTYN_MASSON, S_NAMAZGA_PROBLEM])
