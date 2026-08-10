"""Make the Essentials view navigable and gapless.

`foundational` is the "Essentials" setting in the UI, `intermediate` is "Standard"
(the default), `specialist` is "Everything". Essentials is meant to be the clean
overview, and it was the most broken of the three.

**Three of ten regions were missing entirely.** Verified in the browser, not inferred:
at Essentials the region column listed africa, americas, east-asia, europe, global,
south-asia, west-asia — no `central-asia`, no `oceania`, no `southeast-asia`. Those
three region nodes were `intermediate`, and `visibleAtTier` filters a flat list without
walking the tree, so an entire region vanished from the drill-down. Sixty-five
Southeast Asian and fifty-six Central Asian entities had been authored into branches
the Essentials reader could not reach.

That also corrects the framing in issue #21, which said "a foundational reader sees no
Korean history". True, but Essentials is not the default view — Standard is, and Korea
appears there. The defect is real and narrower than stated.

Two passes:

**Containers.** A child cannot be reached by drilling if its parent is hidden, so a
container must not be less prominent than the things inside it. This promotes regions
and sub-regions that hold substantial authored content.

**Gap fillers.** Entities that close a hole in an Essentials-tier sequence, found by
`tools/report_tier_gaps.py`. Korea ran 1,218 years between the Mumun Period and Goryeo;
Egypt skipped from the New Kingdom to Ptolemaic rule; England went from Norman to Tudor
with the Plantagenets filed one tier down, taking Magna Carta, the Hundred Years' War
and the Black Death with them.

Ruler sequences are deliberately left alone. A gap between two Tokugawa shoguns is
unlisted rulers, not missing history, and promoting individual reigns to close it would
defeat the point of having tiers.
"""

# ── containers ────────────────────────────────────────────────────────────────
# Promoted to foundational so the Essentials drill-down can reach their contents.
CONTAINERS_TO_FOUNDATIONAL = [
    # The three regions absent from Essentials altogether.
    "central-asia",
    "oceania",
    "southeast-asia",
    # Their main subdivisions, or the regions above would open onto nothing.
    "central-asia.core",
    "central-asia.steppe",
    "southeast-asia.mainland",
    "southeast-asia.maritime",
    "oceania.polynesia",
    "oceania.melanesia",
    # Substantial branches that were hidden at Essentials.
    "east-asia.korea",          # 10 children, none reachable at Essentials
    "europe.eastern",           # 7 children: Kievan Rus', Muscovy, Russia, Poland
    "europe.northern",          # Scandinavia and the Norse
    "africa.west",              # 9 children: Ghana, Mali, Songhai, Benin, Kanem-Bornu
    "africa.southern",
    "africa.east",
    "africa.north",
    "west-asia.anatolia",       # Hittites, Lydia, Phrygia
    "west-asia.arabia",         # pre-Islamic Arabia and the incense states
    # Five South Asian polities that ranked below their own rulers: Shivaji was
    # foundational while the Maratha Confederacy was not, so at Essentials the ruler
    # appeared with no state to belong to. Found by the stranded-parent test rather than
    # by inspection. This also reverses the earlier decision to leave Harsha's Empire
    # alone -- that judgement was about closing date gaps and missed that Harsha's own
    # ruler entity already outranked the empire.
    "south-asia.harsha",
    "south-asia.kakatiya",
    "south-asia.maratha",
    "south-asia.sikh-empire",
    "south-asia.mysore",
]

# Thinner branches: raised out of specialist, but not claimed as essential.
CONTAINERS_TO_INTERMEDIATE = [
    "africa.central",
    "americas.amazon-southern",
    "americas.intermediate",
    "oceania.micronesia",
    "central-asia.tibet",
    "west-asia.arabia.pre-islamic.wadi-suq",
]

# ── gap fillers ───────────────────────────────────────────────────────────────
# Each closes a hole in an Essentials-tier sequence. Grouped by the sequence they
# repair, because the justification is the sequence rather than the entity alone.
GAP_FILLERS_TO_FOUNDATIONAL = [
    # Korea: 1,218 years between the Mumun Period (-300) and Goryeo (918).
    "east-asia.korea.gojoseon",
    "east-asia.korea.three-kingdoms",
    "east-asia.korea.unified-silla",
    # Egypt: the intermediate periods and the Late Period are standard
    # periodisation. Old, Middle and New Kingdom were already foundational, so
    # leaving the periods between them hidden made Egypt a sequence of peaks.
    "africa.nile.egypt.fip",
    "africa.nile.egypt.sip",
    "africa.nile.egypt.tip",
    "africa.nile.egypt.late-period",
    "africa.nile.aksum",
    # England: Norman -> Tudor skipped 331 years of Plantagenet rule.
    "europe.western.england.plantagenet",
    "europe.western.england.stuart",
    # Europe, other
    "europe.mediterranean.greece.dark-age",
    "europe.eastern.moscow",
    "europe.western.iberia.reconquista",
    "europe.central.habsburg-monarchy",
    "europe.central.prussia",
    "europe.mediterranean.rome.empire.severan",
    "europe.mediterranean.rome.empire.valentinianic-theodosian",
    # China: Three Kingdoms (ends 280) -> Sui (581) was a 301-year hole, six times
    # the Tang-Song gap that issue #13 was filed about and previously unnoticed.
    "east-asia.china.jin",
    "east-asia.china.north-south",
    # The gap tool did not flag this one, and cannot: after promoting the Jin and the
    # Northern and Southern Dynasties, the 907-960 window at Essentials was *covered* --
    # by the Liao, a Khitan state. So there was no date gap, but the sequence read
    # Tang -> Liao -> Song, implying a steppe dynasty succeeded the Tang in China proper.
    # Coverage is not the same as continuity, which is the limit of measuring by dates.
    "east-asia.china.five-dynasties",
    # Africa
    "africa.southern.mutapa",
    # Iran and Central Asia
    "west-asia.iran.qajar",
    "west-asia.iran.aq-qoyunlu",
    "west-asia.iran.qara-qoyunlu",
    "central-asia.samanid",
    "central-asia.timurid",
    "central-asia.hephthalites",
    "central-asia.kara-khanid",
    # Mesoamerica: Teotihuacan -> Aztec was 878 years.
    "americas.mesoamerica.zapotec",
    "americas.mesoamerica.toltec",
    # South Asia: Maurya -> Gupta -> Chola left two long holes. These are the
    # standard regional powers of the intervening centuries.
    "south-asia.mahajanapadas",
    "south-asia.indo-greek",
    "south-asia.satavahana",
    "south-asia.pallava",
    "south-asia.chalukya-badami",
    "south-asia.rashtrakuta",
    "south-asia.pala",
    # Mesopotamia
    "west-asia.mesopotamia.ur3",
    "west-asia.mesopotamia.kassite",
    # Found by re-running report_tier_gaps.py AFTER the promotions above: promoting
    # the Toltecs changed the sequence to Toltec (ends 1150) -> Aztec (1428), opening
    # a new 278-year hole that only the Purépecha fill. The first draft of this module
    # listed the Purépecha as deliberately not promoted, reasoning from the
    # pre-promotion state. Closing gaps moves the gaps.
    "americas.mesoamerica.purepecha",
]

# Considered and deliberately NOT promoted:
#   south-asia.shunga        -- covered by Satavahana (-230..220)
#   europe.mediterranean.rome.empire.five-emperors -- a single year, and an event
#   south-asia.ghaggar-hakra -- a dispute entity, not a period; the 100-year hole
#                               between Harappan Deurbanisation and the Late
#                               Harappan Phase is missing data, not a tier problem
NOT_PROMOTED = [
    "south-asia.shunga",
]


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}
    moved = {"foundational": 0, "intermediate": 0}

    def retier(ids, target):
        missing = [i for i in ids if i not in by_id]
        if missing:
            # A silent skip here would leave the Essentials view broken while the
            # summary line claimed otherwise, which is exactly how the Trịnh block
            # failed in v3.31.0.0.
            raise KeyError(f"tier_promotions: unknown ids {missing}")
        for i in ids:
            if by_id[i]["tier"] != target:
                by_id[i]["tier"] = target
                moved[target] += 1

    retier(CONTAINERS_TO_FOUNDATIONAL, "foundational")
    retier(GAP_FILLERS_TO_FOUNDATIONAL, "foundational")
    retier(CONTAINERS_TO_INTERMEDIATE, "intermediate")
    # Assert the negative list really was left alone.
    for i in NOT_PROMOTED:
        if i in by_id and by_id[i]["tier"] == "foundational":
            raise AssertionError(f"tier_promotions: {i} should not be foundational")

    print(f"Tiers: {moved['foundational']} -> foundational, "
          f"{moved['intermediate']} -> intermediate")
