"""The Mesolithic: a category argument, and three things that were missing.

Research in `docs/mesolithic-research.md`.

`global.mesolithic` had been the widest childless era in the dataset for six
consecutive passes, and I deferred it every time. Looking properly, the reason
it was empty turns out to be the interesting part.

**The content was never missing.** Maglemose, Kongemose, Ertebølle, Star Carr,
the Azilian, the Sauveterrian and the Doggerland inundation all already exist —
under `europe.prehistory`, where they belong. `global.mesolithic` was empty in
the same way `east-asia.prehistory` was: a global node whose content lives in
regional trees.

**But the fix here is different, because the global category is exactly what
the field disputes.** "Mesolithic" is a European term. Africa uses Later Stone
Age, the Americas use Archaic, Southwest Asia uses Epipalaeolithic. Czarnik
called it a negative category — defined by not being Palaeolithic and not being
Neolithic. Elliott and Warren, writing in 2023 against Graeber and Wengrow's
global "Mesolithic" in *The Dawn of Everything*, argue that exporting the label
takes a northern European typo-chronological term and pegs the rest of the world
to a developmental stage it was never derived from. McNiven and Russell go
further, tying hunter-gatherer-stage concepts to the ideologies that justified
settler-colonial dispossession.

So `global.mesolithic` is not filled with children. It is **reframed as the
argument itself** — an entity about whether the category is valid, carrying the
regional alternatives and the critique. It stops claiming to be a container of
world regions and starts saying something true.

A pleasant consequence: `coverage.py` already excludes eras that have caveats
and no children, on the grounds that they are concepts rather than empty
containers. Giving this node its caveats makes it drop off the gap report
automatically, by the rule written three passes ago.

Also here: Muge, the Obanian, and the 8.2 kiloyear event, none of which existed;
and better dates for the three Scandinavian cultures, from Allentoft et al.'s
2024 Bayesian model over 81 radiocarbon dates.

Deliberately NOT authored: the **Tardenoisian**, again. A previous pass declined
it because sources disagreed by 3,000 years and mixed calibrated with
uncalibrated figures. This pass confirms the disagreement is still unresolved —
Thévenin against Rozoy, with no calibration status stated on either side. Two
passes have now looked at it and reached the same answer, which is worth
recording so a third does not have to.
"""

S_ELLIOTT_WARREN = "elliott-warren-2023-colonialism-mesolithic"
S_DOLITSKY = "dolitsky-1985-mesolithic-siberia"
S_RICHTER_MAHER = "richter-maher-2013-epipalaeolithic"
S_ORA_WEST_AFRICA = "ora-stone-age-west-africa"
S_ROBERTS_MICROLITHS = "roberts-south-asian-microliths"
S_MESO_SINDH = "mesolithic-sindh-terminology"
S_ALLENTOFT = "allentoft-2024-neolithic-denmark"
S_OXFORD_SCANDINAVIA = "oxford-handbook-southern-scandinavia"
S_HAVNO = "archaeofauna-havno-midden"
S_MUGE_COIMBRA = "coimbra-muge-central-portugal"
S_JACKES_LUBELL = "jackes-lubell-muge-chronology"
S_BONSALL_OBAN = "bonsall-mesolithic-kilmore-oban"
S_GARCIA_ESCARZAGA = "garcia-escarzaga-2022-8point2ka"
S_WICKS_MITHEN = "wicks-mithen-2014-scotland-8point2ka"

MESOLITHIC_SOURCES = [
    {"id": S_ELLIOTT_WARREN, "kind": "scholarly",
     "citation": "Elliott & Warren, 'Colonialism and the European Mesolithic', Norwegian Archaeological Review (2023)",
     "url": "https://www.tandfonline.com/doi/full/10.1080/00293652.2023.2182232",
     "note": "Critiques the global 'Mesolithic' of Graeber & Wengrow's The Dawn of Everything "
             "as exporting a northern European typo-chronological label."},
    {"id": S_DOLITSKY, "kind": "scholarly",
     "citation": "Dolitsky, 'A Critical Review of the Mesolithic in Relation to Siberian Archaeology', Arctic 38 (1985)",
     "url": "https://journalhosting.ucalgary.ca/index.php/arctic/article/download/65183/49097",
     "note": "Records Czarnik's point that the Mesolithic began as a negative category "
             "positioned between better-defined periods, and Braidwood calling the tripartite "
             "scheme artificial."},
    {"id": S_RICHTER_MAHER, "kind": "scholarly",
     "citation": "Richter & Maher, 'Terminology, process and change: reflections on the Epipalaeolithic of South-west Asia' (2013)",
     "url": "http://www.tandfonline.com/doi/full/10.1179/0075891413Z.00000000020"},
    {"id": S_ORA_WEST_AFRICA, "kind": "scholarly",
     "citation": "'The Stone Age Archaeology of West Africa' (Oxford Research Archive)",
     "url": "https://ora.ox.ac.uk/objects/uuid:1442d1c1-7f76-454d-97db-8fd52a4c6c1e",
     "note": "Later Stone Age was introduced by Goodwin and Van Riet Lowe in 1929 and is used "
             "in Africa in place of Mesolithic."},
    {"id": S_ROBERTS_MICROLITHS, "kind": "scholarly",
     "citation": "Roberts et al., 'Microliths in the South Asian rainforest ~45-4 ka'",
     "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6774521/",
     "note": "Microliths appear in South Asia from about 45,000 years ago, which breaks the "
             "assumed equation of microliths with a Mesolithic stage."},
    {"id": S_MESO_SINDH, "kind": "scholarly",
     "citation": "'Mesolithic Sindh' (Ca' Foscari University of Venice repository)",
     "url": "https://iris.unive.it/bitstream/10278/19301/1/MesoSindhPraehistoria.pdf",
     "note": "Documents the Possehl-Misra dispute over whether the term has any utility in "
             "South Asia."},
    {"id": S_ALLENTOFT, "kind": "scholarly",
     "citation": "Allentoft et al., '100 ancient genomes show repeated population turnovers in Neolithic Denmark', Nature (2024)",
     "url": "https://www.nature.com/articles/s41586-023-06862-3",
     "note": "Bayesian trapezoidal phase model in OxCal over 81 radiocarbon dates from 64 "
             "Danish sites."},
    {"id": S_OXFORD_SCANDINAVIA, "kind": "scholarly",
     "citation": "Oxford Handbook of Mesolithic Europe, 'Southern Scandinavia' chapter",
     "url": "https://academic.oup.com/edited-volume/59635/chapter/505049919"},
    {"id": S_HAVNO, "kind": "scholarly",
     "citation": "Havnø shell midden study, Archaeofauna",
     "url": "https://revistas.uam.es/archaeofauna/article/download/6380/6856"},
    {"id": S_MUGE_COIMBRA, "kind": "scholarly",
     "citation": "'The case of Muge, central Portugal' (University of Coimbra repository)",
     "url": "https://estudogeral.uc.pt/bitstream/10316/45835/1/cias2016_3.pdf"},
    {"id": S_JACKES_LUBELL, "kind": "scholarly",
     "citation": "Jackes & Lubell, on Muge chronology (University of Waterloo)",
     "url": "http://www.arts.uwaterloo.ca/~mkjackes/Jackes%20and%20Lubell%20incorrect.pdf"},
    {"id": S_BONSALL_OBAN, "kind": "scholarly",
     "citation": "Bonsall et al., 'A Mesolithic Site at Kilmore, near Oban, Western Scotland' (University of Edinburgh)",
     "url": "https://www.pure.ed.ac.uk/ws/files/539999/2009_BANN_FLAKES_Bonsall_etal.pdf"},
    {"id": S_GARCIA_ESCARZAGA, "kind": "scholarly",
     "citation": "García-Escárzaga et al., 'Human forager response to abrupt climate change at 8.2 ka on the Atlantic coast of Europe', Scientific Reports (2022)",
     "url": "https://www.nature.com/articles/s41598-022-10135-w",
     "note": "Dates the event in the NGRIP ice core to 8,250-8,090 cal BP, and finds "
             "intensified shellfish use and demographic growth in Atlantic refugia."},
    {"id": S_WICKS_MITHEN, "kind": "scholarly",
     "citation": "Wicks & Mithen, on the impact of the 8.2 ka event on Mesolithic western Scotland (2014, University of Reading)",
     "url": "https://centaur.reading.ac.uk/60211/",
     "note": "Bayesian analysis of radiocarbon activity events finds a dramatic population "
             "reduction synchronous with the event."},
]

CHECKED = "2026-08-08"
C14 = "radiocarbon-calibrated"
LAYER = "layer-counting"


def extend(E, entities):
    from builders import make_builders
    _, P, ERA, EVENT, _, _ = make_builders(E)
    by_id = {e["id"]: e for e in entities}
    eu = "europe.prehistory"

    # ------------------------------------------- reframe the global node

    m = by_id.get("global.mesolithic")
    if m is not None:
        m["summary"] = (
            "A European period name that much of the world does not use, and a live argument "
            "about whether it describes a real stage at all."
        )
        m["standing"] = "minority"
        m["date_precision"] = "disputed"
        m["start_dating_method"] = "typological"
        m["end_dating_method"] = "typological"
        m["date_note"] = (
            "The span here is the conventional European one and should not be read as global. "
            "Africa uses Later Stone Age, introduced by Goodwin and Van Riet Lowe in 1929; the "
            "Americas use Archaic; Southwest Asia uses Epipalaeolithic. The cultures usually "
            "meant by the word — Maglemose, Kongemose, Ertebolle, the Azilian, the "
            "Sauveterrian — sit under European prehistory in this dataset, because that is "
            "where the term has content."
        )
        # No `as_of`: what is disputed here is the category, not a rival date,
        # so there is no competing chronology to re-check on a schedule.
        m["caveats"] = list(m.get("caveats", [])) + [
            {"kind": "contested-existence",
             "text": "Czarnik argued the Mesolithic began as a negative category, defined by "
                     "being neither Palaeolithic nor Neolithic. Braidwood called the whole "
                     "tripartite scheme artificial.",
             "source_ids": [S_DOLITSKY]},
            {"kind": "misconception",
             "text": "There is no universal package of microliths, forest adaptation and "
                     "coastal sedentism. South Asian microliths appear from about 45,000 years "
                     "ago, long before any Mesolithic stage.",
             "source_ids": [S_ROBERTS_MICROLITHS, S_MESO_SINDH]},
            {"kind": "naming-confusion",
             "text": "Elliott and Warren argue exporting the term pegs the rest of the world "
                     "to a northern European developmental stage. They keep using it for "
                     "Europe, where it still earns its place.",
             "source_ids": [S_ELLIOTT_WARREN]},
        ]
        m["source_ids"] = [S_ELLIOTT_WARREN, S_DOLITSKY, S_RICHTER_MAHER, S_ORA_WEST_AFRICA,
                           S_ROBERTS_MICROLITHS, S_MESO_SINDH]

    # --------------------------- better dates for the Scandinavian three

    for eid, start, end, label in [
        ("europe.prehistory.maglemose", -9050, -6450, "11,000-8,400 cal BP"),
        ("europe.prehistory.kongemose", -6450, -5450, "8,400-7,400 cal BP"),
        ("europe.prehistory.ertebolle", -5450, -3950, "7,400-5,900 cal BP"),
    ]:
        e = by_id.get(eid)
        if e is None:
            continue
        e["start_year"] = start
        e["end_year"] = end
        e["start_dating_method"] = C14
        e["end_dating_method"] = C14
        e["standing"] = "majority"
        e["date_precision"] = "century"
        e["date_note"] = (
            f"{label}, from a Bayesian phase model over 81 radiocarbon dates from 64 Danish "
            "sites. The Oxford Handbook gives different figures for the same cultures without "
            "consistently stating calibration, so the two are not merged."
        )
        e["caveats"] = list(e.get("caveats", [])) + [
            {"kind": "misconception",
             "text": "These boundaries are modelled phase transitions with uncertainty, not "
                     "sharp events. Popular sources quote them as though one culture stopped "
                     "on a particular year.",
             "source_ids": [S_ALLENTOFT]},
        ]
        e["source_ids"] = sorted(set(list(e.get("source_ids", [])) +
                                     [S_ALLENTOFT, S_OXFORD_SCANDINAVIA]))

    erte = by_id.get("europe.prehistory.ertebolle")
    if erte is not None:
        erte["source_ids"] = sorted(set(list(erte["source_ids"]) + [S_HAVNO]))

    # --------------------------------------------------------- new work

    P("muge-middens", "The Muge Shell Middens", eu, -6550, -5050, "intermediate",
      summary="Enormous mounds of estuarine shell in the Tagus and Sado valleys, used as both "
              "settlement and cemetery by foragers who overlapped with the first farmers.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="Mesolithic central Portugal is generally dated 8,500-7,000 cal BP. Deposition "
                "at Cabeco da Amoreira specifically runs 8,000-7,350 cal BP, and the first "
                "burial at Vale de Romeiras in the Sado dates to 8,543-8,334 cal BP.",
      caveats=[{"kind": "misconception",
                "text": "Not a last stand before farming. The Muge and Sado foragers overlap "
                        "in time with incoming Neolithic groups and interact with them for "
                        "centuries.",
                "source_ids": [S_MUGE_COIMBRA, S_JACKES_LUBELL]}],
      source_ids=[S_MUGE_COIMBRA, S_JACKES_LUBELL])

    P("obanian", "The Obanian", eu, -5150, -4250, "specialist",
      summary="Shell middens around Oban and on Oronsay, Scotland's main evidence that "
              "late foragers there lived substantially off the sea.",
      start_dating_method=C14, end_dating_method=C14, standing="majority",
      date_precision="century",
      date_note="Bulk charcoal from five Oronsay middens gave 6,200-5,400 BP uncalibrated, "
                "calibrating to about 5,150-4,250 cal BC. Bulk charcoal samples average "
                "material of different ages, so these are coarser than single-entity dates.",
      source_ids=[S_BONSALL_OBAN])

    EVENT("event-8point2ka", "The 8.2 Kiloyear Event", eu, -6300, -6140, "intermediate",
          summary="An abrupt cooling that hit Mesolithic Europe unevenly — collapse in "
                  "Scotland, apparent resilience in Belgium, and growth on the Atlantic coast.",
          start_dating_method=LAYER, end_dating_method=LAYER, standing="majority",
          date_precision="century",
          date_note="Dated in the NGRIP Greenland ice core by layer counting to 8,250-8,090 "
                    "cal BP, which is far more precise than any of the archaeological "
                    "responses being matched to it.",
          alternatives=[
              {"label": "No causal link in the Scheldt basin", "standing": "minority",
               "note": "A multi-proxy Belgian study found little evidence connecting the 9.3 "
                       "and 8.2 ka coolings to changes in human behaviour there.",
               "source_ids": [S_GARCIA_ESCARZAGA]},
          ],
          caveats=[{"kind": "misconception",
                    "text": "Not a uniform catastrophe. Western Scotland shows demographic "
                            "collapse, while Atlantic Iberia shows intensified shellfish use "
                            "and population growth in the same window.",
                    "source_ids": [S_WICKS_MITHEN, S_GARCIA_ESCARZAGA]}],
          as_of=CHECKED,
          source_ids=[S_GARCIA_ESCARZAGA, S_WICKS_MITHEN])
