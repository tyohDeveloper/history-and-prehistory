"""Chalcolithic and Epipalaeolithic: the two gaps in the ages spine.

Both were raised as "why aren't these here?", and they have different answers.

Chalcolithic
------------
Not too tenuous — irreducibly REGIONAL. A dedicated historiography paper puts it
bluntly: "there is no general agreement about what the Copper Age actually is."
The sourced regional ranges diverge by millennia. The Balkans, Levant, Anatolia
and Mesopotamia cluster in the 6th-4th millennia BC; South Asia's Chalcolithic
cultures do not begin until the 3rd millennium and run to c. 700 BC, overlapping
the Bronze Age elsewhere; Britain and Iberia use it for a narrow 25th-22nd
century BC slice, and whether Northwest Europe has one at all is a named debate.

So this does NOT follow the "Mesolithic (Eurasia)" pattern. That pattern works
because one qualifier captures one roughly contiguous span. No single qualifier
captures a term whose global extent would be c. 6500 BC to c. 700 BC — a window
that swallows the Neolithic, the whole Bronze Age, and part of the Iron Age. A
"Chalcolithic (global)" node would be an artifact of taking the earliest start
and the latest end, describing no real shared period. Regional entries instead.

The regions with NO Chalcolithic are recorded on each entry, because the
absence is a real finding rather than missing data: most of sub-Saharan Africa
goes stone straight to iron, China folds early copper into the Late Neolithic,
the Americas never reached a continent-wide Bronze Age, and Australian
archaeology has abandoned three-age terminology entirely.

Epipalaeolithic
---------------
Deliberately NOT added as a global or Eurasian node, because that would
double-count. "Epipalaeolithic" and "Mesolithic" are largely the same idea under
two regional naming traditions: the Near East, North Africa and southern Europe
say the first, northern and western Europe say the second. Two nodes would
present one continuous sequence as two adjacent periods.

The exception is real and worth having. The Levantine Epipalaeolithic starts
around 23,000 BC — thousands of years before the dataset's Mesolithic node and
squarely inside the Palaeolithic band, where nothing currently names it. Its end
at 10,000 BC is exactly where "Mesolithic (Eurasia)" begins, so it reads as the
regional precursor feeding that seam rather than a parallel era. The existing
Natufian entity is its Late phase and is cross-linked rather than moved.
"""

from builders import make_builders

S_ROBERTS_COPPER = "roberts-copper-age-concept"
S_BALKAN_METAL = "radivojevic-balkan-metallurgy"
S_BELOVODE = "belovode-earliest-smelting"
S_ISAC_CHALCO = "isac-chalcolithic-chronology"
S_LEVANT_C14 = "levant-chalcolithic-radiocarbon"
S_ANATOLIA_OUP = "oup-anatolia-chalcolithic"
S_SUREZHA_LC = "surezha-late-chalcolithic"
S_DALMA_2025 = "dalma-2025-chronology"
S_IGNOU_CHALCO = "ignou-south-asia-chalcolithic"
S_OUP_NATUFIAN = "oup-natufian-chapter"
S_BARYOSEF_NATUFIAN = "baryosef-natufian-columbia"
S_KILLICK_AFRICA = "killick-african-metallurgy"

AGES_SOURCES = [
    {"id": S_ROBERTS_COPPER, "kind": "scholarly",
     "citation": "Roberts, 'The Copper Age — A History of the Concept', Journal of World Prehistory",
     "url": "https://link.springer.com/article/10.1007/s10963-019-09134-z",
     "note": "States there is no general agreement about what the Copper Age is; the term is regionally contingent."},
    {"id": S_BALKAN_METAL, "kind": "scholarly",
     "citation": "'Early Balkan Metallurgy: Origins, Evolution and Society, 6200-3700 BC', Journal of World Prehistory",
     "url": "https://link.springer.com/article/10.1007/s10963-021-09155-7",
     "note": "Chalcolithic proper from c. 5000 BC; copper minerals used from 6200 BC, native copper from 5500 BC."},
    {"id": S_BELOVODE, "kind": "news",
     "citation": "Science News, 'Serbian site may have hosted first copper makers' (Belovode, c. 5000 BC)",
     "url": "https://www.sciencenews.org/article/serbian-site-may-have-hosted-first-copper-makers",
     "note": "Quotes a British Museum archaeologist that the earliest-smelting status probably will not last."},
    {"id": S_ISAC_CHALCO, "kind": "scholarly",
     "citation": "ISAC, University of Chicago, 'Introduction: Culture, Chronology and the Chalcolithic'",
     "url": "https://isac.uchicago.edu/sites/default/files/uploads/shared/docs/intro_to_cultural_chronology_chalco.pdf",
     "note": "Levantine internal boundaries described as imprecisely dated."},
    {"id": S_LEVANT_C14, "kind": "scholarly",
     "citation": "'The Chalcolithic Radiocarbon Record and Its Use in Southern Levantine Archaeology', Radiocarbon",
     "url": "https://www.cambridge.org/core/journals/radiocarbon/article/chalcolithic-radiocarbon-record-and-its-use-in-southern-levantine-archaeology/17F5A00BDC7447EE70C2AA785B8CC246"},
    {"id": S_ANATOLIA_OUP, "kind": "scholarly",
     "citation": "Oxford Handbook chapter on the Chalcolithic of Eastern Anatolia and the South Caucasus",
     "url": "https://academic.oup.com/edited-volume/36332/chapter/318716798",
     "note": "At least three incompatible Anatolian sub-periodizations are in active use."},
    {"id": S_SUREZHA_LC, "kind": "scholarly",
     "citation": "ISAC, University of Chicago, Surezha excavation report with the LC1-LC5 sequence",
     "url": "https://isac.uchicago.edu/sites/default/files/uploads/shared/docs/ar/11-20/13-14/ar2013-14_Surezha.pdf"},
    {"id": S_DALMA_2025, "kind": "scholarly",
     "citation": "'Absolute Chronology of the Dalma Period in Northwestern Iran' (2025), Radiocarbon",
     "url": "https://ora.ox.ac.uk/objects/uuid:45a3fcc2-4640-4850-a0f0-cbd8b69aefa0/files/rst74cs87p",
     "note": "Refines the regional start to 5200/5100 BCE."},
    {"id": S_IGNOU_CHALCO, "kind": "institutional",
     "citation": "IGNOU / eGyanKosh, 'Chalcolithic Cultures' (Kayatha, Ahar-Banas, Malwa, Jorwe)",
     "url": "https://egyankosh.ac.in/bitstream/123456789/41362/1/Unit-3.pdf"},
    {"id": S_OUP_NATUFIAN, "kind": "scholarly",
     "citation": "Oxford Handbook chapter on the Natufian, with IntCal20-calibrated Epipalaeolithic phases",
     "url": "https://academic.oup.com/edited-volume/59635/chapter/505050944",
     "note": "Early 23,000-16,000, Middle 16,000-13,000, Late (Natufian) 13,000-10,000 cal BC."},
    {"id": S_BARYOSEF_NATUFIAN, "kind": "scholarly",
     "citation": "Bar-Yosef, 'The Natufian Culture in the Levant, Threshold to the Origins of Agriculture', Columbia University",
     "url": "https://www.columbia.edu/itc/anthropology/v1007/baryo.pdf",
     "note": "Kebaran c. 18,000-14,500 BP for the coastal Levant; end date varies across sources."},
    {"id": S_KILLICK_AFRICA, "kind": "scholarly",
     "citation": "'Origins of African Metallurgies', Oxford Research Encyclopedias",
     "url": "https://academic.oup.com/edited-volume/61643/chapter/539815102?guestAccessKey=",
     "note": "Evidence for metallurgy in Niger before 1000 BC remains in doubt; most of sub-Saharan Africa goes stone to iron."},
]

# Repeated on every Chalcolithic entry: the absence elsewhere is a finding.
_NO_CHALCOLITHIC = (
    "There is no global Chalcolithic node, deliberately. Most of sub-Saharan "
    "Africa goes from stone straight to iron; China folds early copper into the "
    "Late Neolithic; the Americas never reached a continent-wide Bronze Age; and "
    "Australian archaeology has dropped three-age terminology altogether."
)


def extend(E, entities):
    _, P, ERA, _, _, _ = make_builders(E)
    by_id = {e["id"]: e for e in entities}

    # ---- Levantine Epipalaeolithic ----------------------------------------
    wa = "west-asia.prehistory"
    epi = ERA("epipalaeolithic", "Epipalaeolithic (Levant)", wa, -23000, -10000,
              tier="intermediate",
              # Starts 10,000 years before its navigation-era parent, which begins
              # at the Natufian. The parent is a browsing container, not a claim.
              allow_outside_parent_dates=True,
              summary="The long Levantine hunter-gatherer sequence between the Upper "
                      "Palaeolithic and farming, ending where the Mesolithic begins.",
              start_dating_method="radiocarbon-calibrated",
              end_dating_method="radiocarbon-calibrated",
              standing="consensus",
              date_note="Calibrated to IntCal20. Its end at 10,000 BC is exactly where "
                        "'Mesolithic (Eurasia)' starts, and that is the point: the two are "
                        "largely the same idea under different regional naming traditions, "
                        "not adjacent periods. This entry exists because the EARLY part, "
                        "back to 23,000 BC, sits inside the Palaeolithic band where nothing "
                        "else names it. Absolute figures vary by several centuries across "
                        "calibration vintages.",
              caveats=[{"kind": "naming-confusion",
                        "text": "Not a separate stage from the Mesolithic: the Near East, "
                                "North Africa and southern Europe say Epipalaeolithic where "
                                "northern Europe says Mesolithic.",
                        "source_ids": [S_OUP_NATUFIAN]}],
              source_ids=[S_OUP_NATUFIAN])

    P("kebaran", "Kebaran", epi, -23000, -16000, "specialist",
      summary="The Early Epipalaeolithic of the Levant: small mobile groups with microlithic "
              "toolkits, through the Last Glacial Maximum.",
      start_dating_method="radiocarbon-calibrated", end_dating_method="radiocarbon-calibrated",
      standing="majority",
      date_note="The Oxford IntCal20 table gives 23,000-16,000 cal BC for the Early "
                "Epipalaeolithic as a whole. Kebaran-only figures differ across sources "
                "(c. 18,000-14,500 BP on the coast), and no single end date is settled.",
      source_ids=[S_OUP_NATUFIAN, S_BARYOSEF_NATUFIAN])

    P("geometric-kebaran", "Geometric Kebaran", epi, -16000, -13000, "specialist",
      summary="The Middle Epipalaeolithic, named for its geometric microliths, between the "
              "Kebaran and the Natufian.",
      start_dating_method="radiocarbon-calibrated", end_dating_method="radiocarbon-calibrated",
      standing="majority",
      date_note="16,000-13,000 cal BC, IntCal20.",
      source_ids=[S_OUP_NATUFIAN])

    # The Natufian IS the Late Epipalaeolithic. Cross-linked rather than moved:
    # its id and its place under west-asia.prehistory are left alone.
    natufian = by_id.get("west-asia.prehistory.natufian")
    if natufian is not None:
        natufian.setdefault("cross_parent_ids", []).append(epi)

    # ---- Chalcolithic, regionally ------------------------------------------
    ERA("chalcolithic-balkans", "Chalcolithic (Southeast Europe)", "europe.prehistory",
        -5000, -3700, tier="intermediate",
        aliases=["Copper Age", "Eneolithic"],
        summary="The Balkan Copper Age: the world's earliest known copper smelting, and the "
                "gold of the Varna cemetery.",
        start_dating_method="radiocarbon-calibrated", end_dating_method="radiocarbon-calibrated",
        standing="consensus",
        date_note="Copper minerals are worked from c. 6200 BC and native copper from c. 5500 "
                  "BC, but the Chalcolithic proper begins with smelting at c. 5000 BC. "
                  "Belovode in Serbia holds the earliest securely dated smelting anywhere, and "
                  "specialists expect that status to move. " + _NO_CHALCOLITHIC,
        caveats=[{"kind": "misconception",
                  "text": "A Copper Age is not a universal stage. Most of sub-Saharan Africa "
                          "has none at all, moving from stone tools directly to iron.",
                  "source_ids": [S_KILLICK_AFRICA]}],
        source_ids=[S_BALKAN_METAL, S_BELOVODE, S_ROBERTS_COPPER, S_KILLICK_AFRICA])

    ERA("chalcolithic", "Chalcolithic (Southern Levant)", wa, -4700, -3600,
        tier="intermediate",
        allow_outside_parent_dates=True,
        aliases=["Copper Age", "Ghassulian"],
        summary="The southern Levantine Copper Age, with copper hoards, ossuary burial and "
                "the Ghassulian culture.",
        start_dating_method="radiocarbon-calibrated", end_dating_method="radiocarbon-calibrated",
        standing="majority",
        date_note="c. 4700/4500-3700/3600 cal BC is the most consistently defended range; "
                  "some syntheses broaden it to 5000-3500 BC. Both internal boundaries are "
                  "described in the literature as imprecisely dated, and whether the "
                  "Chalcolithic overlaps Early Bronze I is disputed. " + _NO_CHALCOLITHIC,
        source_ids=[S_ISAC_CHALCO, S_LEVANT_C14, S_ROBERTS_COPPER])

    ERA("chalcolithic-anatolia", "Chalcolithic (Anatolia)", wa, -5500, -3000,
        tier="specialist",
        allow_outside_parent_dates=True,
        summary="The Anatolian Copper Age, spanning the long interval between the Neolithic "
                "villages and the Early Bronze Age.",
        start_dating_method="radiocarbon-calibrated", end_dating_method="radiocarbon-calibrated",
        standing="majority",
        date_note="c. 5500-3000 BC is the most commonly defended whole-period range, but at "
                  "least three incompatible sub-periodizations are in active use for Central, "
                  "Eastern and Western Anatolia, differing by centuries. Treat any single "
                  "Anatolian figure with caution. " + _NO_CHALCOLITHIC,
        source_ids=[S_ANATOLIA_OUP, S_ROBERTS_COPPER])

    ERA("late-chalcolithic-mesopotamia", "Late Chalcolithic (Mesopotamia)", wa, -4500, -3100,
        tier="specialist",
        allow_outside_parent_dates=True,
        summary="Terminal Ubaid through Late Uruk, the LC1-LC5 sequence that ends with the "
                "first cities and the first writing.",
        start_dating_method="radiocarbon-calibrated", end_dating_method="radiocarbon-calibrated",
        standing="majority",
        date_note="In Mesopotamian usage 'Chalcolithic' covers the pre-Bronze sequence, and "
                  "the narrower Late Chalcolithic runs c. 4500-3100 BC. Note this ends 200 "
                  "years AFTER the global Bronze Age node begins at 3300 BC: the regional "
                  "Bronze Age does not start until Uruk closes. " + _NO_CHALCOLITHIC,
        source_ids=[S_SUREZHA_LC, S_DALMA_2025, S_ROBERTS_COPPER])

    ERA("chalcolithic-south-asia", "Chalcolithic (South Asia)", "south-asia", -3000, -700,
        tier="specialist",
        summary="The Deccan and central Indian copper-using farming cultures — Kayatha, "
                "Ahar-Banas, Malwa and Jorwe — which are not a pre-Bronze stage at all.",
        start_dating_method="radiocarbon-calibrated", end_dating_method="radiocarbon-calibrated",
        standing="majority",
        date_note="No single pan-Indian range is defensible. These cultures run c. 3000/2600 "
                  "BC to c. 700 BC and are CONTEMPORARY with, not prior to, mature Harappan "
                  "Bronze Age urbanism elsewhere in the subcontinent — which is why no global "
                  "Chalcolithic node can exist. Jorwe alone runs to c. 700 BC, inside the "
                  "global Iron Age band. " + _NO_CHALCOLITHIC,
        caveats=[{"kind": "misconception",
                  "text": "Not the stage between Neolithic and Bronze Age here: South Asian "
                          "Chalcolithic cultures coexist with Bronze Age cities nearby.",
                  "source_ids": [S_IGNOU_CHALCO]}],
        source_ids=[S_IGNOU_CHALCO, S_ROBERTS_COPPER])

    # ---- Say it on the spine itself ----------------------------------------
    bronze = by_id.get("global.bronze-age")
    if bronze is not None:
        bronze.setdefault("caveats", []).append({
            "kind": "misconception",
            "text": "The clean 3300 BC seam with the Neolithic hides a regionally variable "
                    "Copper Age; see the regional Chalcolithic entries.",
            "source_ids": [S_ROBERTS_COPPER],
        })
