"""Build seed data for the history picker.

Emits four JSON files into ./data/:
  entities.json          — the tree of Region/Era/Period/Reign/Event nodes
  calendars.json         — dating systems + named-year sequences (nengō, etc.)
  themes.json            — cross-cutting topical collections
  reference-frames.json  — novice-friendly time anchors

Coverage is intentionally broad (every region, every major era) rather than
exhaustive within one region. Add nodes over time; the schema supports it.
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

# Generated data is written to src/data so Vite inlines it at build time.
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "src" / "data"
DATA.mkdir(exist_ok=True)

# ---- Versions --------------------------------------------------------------
# Bump SCHEMA_VERSION whenever fields change or become required.
# Bump DATASET_VERSION whenever the data content changes.
# 3.7.0 adds the `site` kind -- a place that mattered without being a town, for the forty-seven
# sanctuaries, necropoleis and mound centres that had been filed as cities and said so themselves.
# Additive, so no reader of 3.6.0 data breaks; a reader of 3.7.0 data needs the new kind.
SCHEMA_VERSION = "3.7.0"
DATASET_VERSION = "0.42.0.0"
_GENERATED_AT = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _envelope(key, items, **extra):
    env = {
        "schema_version": SCHEMA_VERSION,
        "dataset_version": DATASET_VERSION,
        "generated_at": _GENERATED_AT,
        key: items,
    }
    # `redirects` rides along with the entities so a stale id resolves rather than 404s. Ids
    # are frozen; when a rename is unavoidable it is recorded here and honoured forever.
    env.update(extra)
    return env


entities = []


# Sentinel to distinguish "caller passed null explicitly" from "caller didn't pass anything".
_MISSING = object()

_TOP_LEVEL_KINDS = {"region"}  # kinds where parent_id/start/end may legitimately be null

def E(id, kind, name, parent_id=_MISSING, start=_MISSING, end=_MISSING, **kw):
    """Add an entity. Positional args cover the common case.

    Emits explicit `null` for parent_id / start_year / end_year when the caller
    intends unknown/ongoing/not-applicable, so consumers can distinguish it from
    an omitted field. Fields required by the schema are always written.
    """
    e = {"id": id, "kind": kind, "name": name}
    # parent_id: always written; null only for top-level regions
    if parent_id is _MISSING:
        e["parent_id"] = None
    else:
        e["parent_id"] = parent_id
    # start_year / end_year: always written; null means unknown-or-ongoing
    e["start_year"] = None if start is _MISSING else start
    e["end_year"] = None if end is _MISSING else end
    # tier defaults to "intermediate" if not specified, so the schema can require it
    if "tier" not in kw:
        kw["tier"] = "intermediate"
    # date_precision defaults to "approx" when we have real dates, else "unknown"
    if "date_precision" not in kw and "start_precision" not in kw and "end_precision" not in kw:
        kw["date_precision"] = "approx" if (e["start_year"] is not None or e["end_year"] is not None) else "unknown"
    for k, v in kw.items():
        if v is None or v == [] or v == "":
            continue
        e[k] = v
    entities.append(e)
    return id


# =============================================================================
# TOP-LEVEL REGIONS
# =============================================================================

E("global", "region", "Global",
  summary="Cross-regional and worldwide frames (BCE/CE, prehistoric ages, world wars).",
  tier="foundational")

E("europe", "region", "Europe", tier="foundational",
  summary="From the Aegean Bronze Age through the modern EU. Split into Mediterranean, Western, Central, Northern, and Eastern sub-branches.")
E("europe.mediterranean", "region", "Mediterranean", parent_id="europe", tier="foundational")
E("europe.western", "region", "Western Europe", parent_id="europe", tier="foundational")
E("europe.central", "region", "Central Europe", parent_id="europe", tier="foundational")
E("europe.northern", "region", "Northern Europe", parent_id="europe", tier="intermediate")
E("europe.eastern", "region", "Eastern Europe", parent_id="europe", tier="intermediate")

E("west-asia", "region", "West Asia",
  aliases=["Near East", "Middle East"], tier="foundational",
  summary="Mesopotamia, the Levant, Anatolia, Iran, and Arabia.")
E("west-asia.mesopotamia", "region", "Mesopotamia & Levant", parent_id="west-asia", tier="foundational")
E("west-asia.anatolia", "region", "Anatolia", parent_id="west-asia", tier="intermediate")
E("west-asia.iran", "region", "Iran / Persia", parent_id="west-asia", tier="foundational")
E("west-asia.arabia", "region", "Arabia", parent_id="west-asia", tier="intermediate")

E("central-asia", "region", "Central Asia & the Steppe",
  aliases=["Inner Asia"], tier="intermediate",
  summary="Silk Road oases, the Eurasian steppe, and Tibet.")
E("central-asia.core", "region", "Central Asia", parent_id="central-asia", tier="intermediate")
E("central-asia.steppe", "region", "Eurasian Steppe", parent_id="central-asia", tier="intermediate")
E("central-asia.tibet", "region", "Tibet & Himalaya", parent_id="central-asia", tier="intermediate")

E("south-asia", "region", "South Asia",
  aliases=["Indian subcontinent"], tier="foundational",
  summary="Indian subcontinent from Indus civilization through the modern republics.")

E("east-asia", "region", "East Asia", tier="foundational")
E("east-asia.china", "region", "China", parent_id="east-asia", tier="foundational")
E("east-asia.korea", "region", "Korea", parent_id="east-asia", tier="intermediate")
E("east-asia.japan", "region", "Japan", parent_id="east-asia", tier="foundational")

E("southeast-asia", "region", "Southeast Asia", tier="intermediate")
E("southeast-asia.mainland", "region", "Mainland Southeast Asia", parent_id="southeast-asia", tier="intermediate")
E("southeast-asia.maritime", "region", "Maritime Southeast Asia",
  parent_id="southeast-asia", aliases=["Malay Archipelago", "Insular Southeast Asia"], tier="intermediate")

E("africa", "region", "Africa", tier="foundational")
E("africa.nile", "region", "Nile Valley & Northeast Africa", parent_id="africa", tier="foundational")
E("africa.north", "region", "North Africa (Maghreb)", parent_id="africa", tier="intermediate")
E("africa.west", "region", "West Africa & Sahel", parent_id="africa", tier="intermediate")
E("africa.east", "region", "East Africa", parent_id="africa", tier="intermediate")
E("africa.central", "region", "Central Africa", parent_id="africa", tier="specialist")
E("africa.southern", "region", "Southern Africa", parent_id="africa", tier="intermediate")

E("americas", "region", "Americas", tier="foundational")
E("americas.north", "region", "North America", parent_id="americas", tier="foundational")
E("americas.mesoamerica", "region", "Mesoamerica", parent_id="americas", tier="foundational")
E("americas.intermediate", "region", "Intermediate Area & Caribbean", parent_id="americas", tier="specialist")
E("americas.andes", "region", "Andes", parent_id="americas", tier="foundational")
E("americas.amazon-southern", "region", "Amazon & Southern Cone", parent_id="americas", tier="specialist")

E("oceania", "region", "Oceania", tier="intermediate")
E("oceania.australia", "region", "Australia", parent_id="oceania", tier="foundational")
E("oceania.melanesia", "region", "Melanesia", parent_id="oceania", tier="intermediate")
E("oceania.micronesia", "region", "Micronesia", parent_id="oceania", tier="specialist")
E("oceania.polynesia", "region", "Polynesia", parent_id="oceania", tier="intermediate")

E("cross-regional", "region", "Cross-Regional Empires",
  tier="foundational",
  summary="Empires spanning multiple regions — cross-linked here for convenience.")


# =============================================================================
# GLOBAL / PREHISTORIC / DATING FRAMES
# =============================================================================

E("global.bce", "era", "BCE (Before Common Era)", "global",
  start=-3500, end=-1, tier="foundational",
  summary="The 'before Common Era' convention for years prior to year 1. Equivalent to BC.")
E("global.ce", "era", "CE (Common Era)", "global",
  start=1, end=None, tier="foundational",
  summary="The 'Common Era' convention for years from year 1 onward. Equivalent to AD.")

# The three stone ages hang under Human Prehistory rather than beside it.
# They were siblings of it in v2.1.0, which meant two parallel prehistory
# branches covering the same span. Ids are unchanged, so nothing needs a
# redirect: the id records where an entity was minted, the parent records
# where it sits.
E("global.paleolithic", "era", "Paleolithic (Old Stone Age)", "global.prehistory",
  start=-3300000, end=-10000, date_precision="approx", tier="foundational",
  start_dating_method="argon-argon",
  summary="The long first chapter: stone tools, fire, and hunter-gatherer life, from the "
          "earliest knapped stone through the whole span of the genus Homo.",
  date_note="Starts at the earliest known stone tools \u2014 Lomekwi 3, c. 3.3 Ma \u2014 "
            "which predate the genus Homo. Whether those count as Oldowan is a "
            "definitional argument; they are included here because the toolmaking record "
            "is continuous even where the taxonomy is not.")
E("global.mesolithic", "era", "Mesolithic (Eurasia)", "global.prehistory", start=-10000, end=-5000,
  tier="intermediate", start_dating_method="radiocarbon-calibrated", standing="consensus",
  date_note="A Eurasian term. It has no counterpart in the Americas, sub-Saharan Africa "
            "or Australia, where the post-glacial sequence is described differently.")
E("global.neolithic", "era", "Neolithic (New Stone Age)", "global.prehistory",
  start=-10000, end=-3300, tier="foundational",
  start_dating_method="radiocarbon-calibrated", standing="consensus",
  summary="Beginnings of agriculture, animal domestication, and permanent villages.")
E("global.bronze-age", "era", "Bronze Age", "global",
  start=-3300, end=-1200, tier="foundational",
  start_dating_method="calendar", standing="consensus",
  start_year_min=-3500, start_year_max=-3000,
  end_year_min=-1200, end_year_max=-1150,
  start_precision="approx", end_precision="approx",
  date_note="Regional Bronze Ages began at different dates; the collapse cluster is c. 1200-1150 BCE.")
E("global.iron-age", "era", "Iron Age", "global",
  start=-1200, end=-550, tier="foundational")
E("global.classical-antiquity", "era", "Classical Antiquity", "global",
  start=-800, end=500, tier="foundational")
E("global.late-antiquity", "era", "Late Antiquity", "global",
  start=250, end=750, tier="intermediate")
E("global.middle-ages", "era", "Middle Ages", "global",
  start=500, end=1500, tier="foundational")
E("global.early-modern", "era", "Early Modern", "global",
  start=1500, end=1800, tier="foundational")
E("global.long-19c", "era", "Long 19th Century", "global",
  start=1789, end=1914, tier="foundational")
E("global.short-20c", "era", "Short 20th Century", "global",
  start=1914, end=1991, tier="foundational")
E("global.contemporary", "era", "Contemporary", "global",
  start=1991, end=None, tier="foundational")


# =============================================================================
# EGYPT (full worked example)
# =============================================================================

egypt = "africa.nile.egypt"
# Egypt's canonical span now covers Predynastic through Roman/Byzantine so all
# children (Predynastic -6000, Roman-Byzantine 641) fall within their parent.
E(egypt, "era", "Ancient Egypt", "africa.nile",
  start=-6000, end=641, tier="foundational",
  aliases=["Pharaonic Egypt", "Nile Valley civilization"],
  calendar_ids=["egyptian-regnal"],
  summary="Continuous Nile Valley civilization from Predynastic cultures through Narmer's unification, the pharaonic dynasties, and Ptolemaic/Roman/Byzantine rule.")

# Predynastic (kept summary-level). Dates are approximate archaeological ranges.
E(f"{egypt}.predynastic", "era", "Predynastic Egypt", egypt,
  start=-6000, end=-3100, tier="intermediate",
  start_precision="approx", end_precision="year")

# Early Dynastic
E(f"{egypt}.early-dynastic", "era", "Early Dynastic Period", egypt,
  start=-3100, end=-2686, tier="intermediate",
  summary="Unification of Upper and Lower Egypt under the 1st and 2nd Dynasties.")
E(f"{egypt}.early-dynastic.dyn1", "period", "1st Dynasty", f"{egypt}.early-dynastic", start=-3100, end=-2890)
E(f"{egypt}.early-dynastic.dyn1.narmer", "reign", "Narmer / Menes", f"{egypt}.early-dynastic.dyn1",
  start=-3100, end=-3080, tier="foundational",
  date_precision="traditional",
  summary="Legendary unifier of Upper and Lower Egypt. Dates and identity as Menes are partly traditional.")
E(f"{egypt}.early-dynastic.dyn2", "period", "2nd Dynasty", f"{egypt}.early-dynastic", start=-2890, end=-2686)

# Old Kingdom
E(f"{egypt}.old-kingdom", "era", "Old Kingdom", egypt,
  start=-2686, end=-2181, tier="foundational",
  aliases=["Age of the Pyramids"],
  summary="Pyramid-building age. Djoser, Khufu, Khafre, Menkaure.")
E(f"{egypt}.old-kingdom.dyn3", "period", "3rd Dynasty", f"{egypt}.old-kingdom", start=-2686, end=-2613)
E(f"{egypt}.old-kingdom.dyn3.djoser", "reign", "Djoser", f"{egypt}.old-kingdom.dyn3",
  start=-2670, end=-2650, tier="foundational",
  summary="Commissioned the Step Pyramid at Saqqara, the world's first monumental stone building.")
E(f"{egypt}.old-kingdom.dyn4", "period", "4th Dynasty", f"{egypt}.old-kingdom", start=-2613, end=-2494)
E(f"{egypt}.old-kingdom.dyn4.sneferu", "reign", "Sneferu", f"{egypt}.old-kingdom.dyn4", start=-2613, end=-2589)
E(f"{egypt}.old-kingdom.dyn4.khufu", "reign", "Khufu", f"{egypt}.old-kingdom.dyn4",
  start=-2589, end=-2566, tier="foundational",
  aliases=["Cheops"],
  summary="Builder of the Great Pyramid of Giza.")
E(f"{egypt}.old-kingdom.dyn4.khafre", "reign", "Khafre", f"{egypt}.old-kingdom.dyn4",
  start=-2558, end=-2532, tier="foundational",
  aliases=["Chephren"],
  summary="Built the second Giza pyramid and, by tradition, the Great Sphinx.")
E(f"{egypt}.old-kingdom.dyn4.menkaure", "reign", "Menkaure", f"{egypt}.old-kingdom.dyn4", start=-2532, end=-2503)
E(f"{egypt}.old-kingdom.dyn5", "period", "5th Dynasty", f"{egypt}.old-kingdom", start=-2494, end=-2345)
E(f"{egypt}.old-kingdom.dyn6", "period", "6th Dynasty", f"{egypt}.old-kingdom", start=-2345, end=-2181)
E(f"{egypt}.old-kingdom.dyn6.pepi2", "reign", "Pepi II", f"{egypt}.old-kingdom.dyn6",
  start=-2278, end=-2184, tier="intermediate",
  summary="Traditionally credited with the longest reign in history (~94 years).")

# First Intermediate
E(f"{egypt}.fip", "era", "First Intermediate Period", egypt,
  start=-2181, end=-2055, tier="intermediate",
  summary="Political fragmentation between the Old and Middle Kingdoms.")

# Middle Kingdom
E(f"{egypt}.middle-kingdom", "era", "Middle Kingdom", egypt,
  start=-2055, end=-1650, tier="foundational")
# 11th Dynasty as a whole starts with the Theban Intefs (c. -2125), before Mentuhotep II's
# reunification (c. -2055) which is when the Middle Kingdom proper begins.
E(f"{egypt}.middle-kingdom.dyn11", "period", "11th Dynasty (reunified)", f"{egypt}.middle-kingdom",
  start=-2125, end=-1985, allow_outside_parent_dates=True,
  date_note="Early 11th Dynasty (Theban Intefs) predates the reunification that starts the Middle Kingdom.")
E(f"{egypt}.middle-kingdom.dyn11.mentuhotep2", "reign", "Mentuhotep II", f"{egypt}.middle-kingdom.dyn11",
  start=-2055, end=-2004, tier="intermediate",
  summary="Reunified Egypt, founding the Middle Kingdom.")
E(f"{egypt}.middle-kingdom.dyn12", "period", "12th Dynasty", f"{egypt}.middle-kingdom", start=-1985, end=-1773)
E(f"{egypt}.middle-kingdom.dyn13", "period", "13th Dynasty", f"{egypt}.middle-kingdom", start=-1773, end=-1650)

# Second Intermediate
E(f"{egypt}.sip", "era", "Second Intermediate Period", egypt,
  start=-1650, end=-1550, tier="intermediate",
  summary="Hyksos rule in the Delta; Theban resistance in the south.")
E(f"{egypt}.sip.dyn15-hyksos", "period", "15th Dynasty — Hyksos", f"{egypt}.sip", start=-1650, end=-1550,
  summary="Semitic-speaking rulers who introduced the horse and chariot, composite bow, and bronze weapons.")

# New Kingdom
E(f"{egypt}.new-kingdom", "era", "New Kingdom", egypt,
  start=-1550, end=-1069, tier="foundational",
  summary="Imperial age of Egypt; Valley of the Kings; Karnak/Luxor expansion.")
E(f"{egypt}.new-kingdom.dyn18", "period", "18th Dynasty", f"{egypt}.new-kingdom", start=-1550, end=-1292)
E(f"{egypt}.new-kingdom.dyn18.ahmose1", "reign", "Ahmose I", f"{egypt}.new-kingdom.dyn18",
  start=-1550, end=-1525, summary="Expelled the Hyksos and founded the New Kingdom.")
E(f"{egypt}.new-kingdom.dyn18.hatshepsut", "reign", "Hatshepsut", f"{egypt}.new-kingdom.dyn18",
  start=-1479, end=-1458, tier="foundational",
  summary="Female pharaoh who ruled as king in her own right; built the Deir el-Bahri temple.")
E(f"{egypt}.new-kingdom.dyn18.thutmose3", "reign", "Thutmose III", f"{egypt}.new-kingdom.dyn18",
  start=-1479, end=-1425, tier="intermediate",
  summary="Great warrior-pharaoh; extended the empire to its widest historical extent.")
E(f"{egypt}.new-kingdom.dyn18.amenhotep3", "reign", "Amenhotep III", f"{egypt}.new-kingdom.dyn18",
  start=-1388, end=-1351, tier="intermediate")
E(f"{egypt}.new-kingdom.dyn18.akhenaten", "reign", "Akhenaten", f"{egypt}.new-kingdom.dyn18",
  start=-1351, end=-1334, tier="foundational",
  aliases=["Amenhotep IV"],
  summary="Founded a short-lived monotheistic cult of the Aten and moved the capital to Amarna.")
E(f"{egypt}.new-kingdom.dyn18.tutankhamun", "reign", "Tutankhamun", f"{egypt}.new-kingdom.dyn18",
  start=-1332, end=-1323, tier="foundational",
  aliases=["King Tut"],
  summary="Reversed the Amarna religious reforms. His intact tomb was discovered in 1922.")
E(f"{egypt}.new-kingdom.dyn19", "period", "19th Dynasty (Ramesside)", f"{egypt}.new-kingdom", start=-1295, end=-1186)
E(f"{egypt}.new-kingdom.dyn19.seti1", "reign", "Seti I", f"{egypt}.new-kingdom.dyn19", start=-1290, end=-1279)
E(f"{egypt}.new-kingdom.dyn19.ramesses2", "reign", "Ramesses II", f"{egypt}.new-kingdom.dyn19",
  start=-1279, end=-1213, tier="foundational",
  aliases=["Ramesses the Great", "Ozymandias"],
  summary="Long-reigning warrior-pharaoh. Fought the Hittites at Kadesh and signed the world's earliest surviving peace treaty.")
E(f"{egypt}.new-kingdom.dyn20", "period", "20th Dynasty", f"{egypt}.new-kingdom", start=-1186, end=-1069)
E(f"{egypt}.new-kingdom.dyn20.ramesses3", "reign", "Ramesses III", f"{egypt}.new-kingdom.dyn20",
  start=-1186, end=-1155, tier="intermediate",
  summary="Last great New Kingdom pharaoh; repelled the Sea Peoples.")

# Third Intermediate
# TIP spans through the Kushite expulsion by the Saites; overlaps with early Dyn 26.
E(f"{egypt}.tip", "era", "Third Intermediate Period", egypt, start=-1069, end=-656, tier="intermediate")
E(f"{egypt}.tip.dyn25-kushite", "period", "25th Dynasty — Kushite (Nubian)", f"{egypt}.tip", start=-744, end=-656,
  summary="Nubian pharaohs from Kush ruled all Egypt.",
  cross_parent_ids=["africa.nile.kush"])
E(f"{egypt}.tip.dyn25.piye", "reign", "Piye", f"{egypt}.tip.dyn25-kushite", start=-744, end=-714)
E(f"{egypt}.tip.dyn25.taharqa", "reign", "Taharqa", f"{egypt}.tip.dyn25-kushite", start=-690, end=-664)

# Late Period
E(f"{egypt}.late-period", "era", "Late Period", egypt, start=-664, end=-332, tier="intermediate")
E(f"{egypt}.late-period.dyn26-saite", "period", "26th Dynasty — Saite Renaissance", f"{egypt}.late-period", start=-664, end=-525)
E(f"{egypt}.late-period.dyn27-persian1", "period", "27th Dynasty — First Persian", f"{egypt}.late-period", start=-525, end=-404,
  cross_parent_ids=["west-asia.iran.achaemenid"])

# Ptolemaic
E(f"{egypt}.ptolemaic", "era", "Ptolemaic Egypt", egypt,
  start=-332, end=-30, tier="foundational",
  summary="Greek-Macedonian dynasty founded after Alexander's conquest. Capital: Alexandria.",
  capital="Alexandria",
  cross_parent_ids=["europe.mediterranean.hellenistic"])
E(f"{egypt}.ptolemaic.ptolemy1", "reign", "Ptolemy I Soter", f"{egypt}.ptolemaic", start=-305, end=-283)
E(f"{egypt}.ptolemaic.cleopatra7", "reign", "Cleopatra VII", f"{egypt}.ptolemaic",
  start=-51, end=-30, tier="foundational",
  summary="Last active pharaoh of Egypt. Allied with Julius Caesar and Mark Antony; defeated at Actium in 31 BCE.")

# Roman/Byzantine Egypt
E(f"{egypt}.roman-byzantine", "era", "Roman & Byzantine Egypt", egypt,
  start=-30, end=641, tier="intermediate",
  cross_parent_ids=["europe.mediterranean.rome.empire"])


# =============================================================================
# KUSH & AKSUM (Northeast Africa siblings of Egypt)
# =============================================================================

E("africa.nile.kush", "era", "Kingdom of Kush", "africa.nile",
  start=-2500, end=350, tier="intermediate",
  aliases=["Nubia"],
  summary="Nubian civilization south of Egypt with capitals successively at Kerma, Napata, and Meroë.")
E("africa.nile.kush.kerma", "period", "Kerma Phase", "africa.nile.kush", start=-2500, end=-1500)
E("africa.nile.kush.napatan", "period", "Napatan Phase", "africa.nile.kush", start=-1070, end=-270)
E("africa.nile.kush.meroitic", "period", "Meroitic Phase", "africa.nile.kush", start=-270, end=350,
  summary="Meroë as capital; Meroitic script still undeciphered.")

E("africa.nile.aksum", "era", "Kingdom of Aksum", "africa.nile",
  start=100, end=940, tier="intermediate",
  summary="Highland Ethiopian empire; converted to Christianity under Ezana (c. 330 CE).")
E("africa.nile.aksum.ezana", "reign", "Ezana", "africa.nile.aksum", start=320, end=360,
  summary="Made Aksum one of the earliest Christian states.")

E("africa.nile.ethiopia", "era", "Ethiopian Empire", "africa.nile",
  start=1270, end=1974, tier="foundational",
  aliases=["Solomonic Dynasty", "Abyssinia"],
  summary="Solomonic dynasty ruled Ethiopia for seven centuries; never fully colonized.")
E("africa.nile.ethiopia.menelik2", "reign", "Menelik II", "africa.nile.ethiopia",
  start=1889, end=1913, summary="Defeated Italy at the Battle of Adwa (1896).")
E("africa.nile.ethiopia.haile-selassie", "reign", "Haile Selassie", "africa.nile.ethiopia",
  start=1930, end=1974, tier="foundational")


# =============================================================================
# JAPAN (full worked example including all nengō as periods)
# =============================================================================

jp = "east-asia.japan"

E(f"{jp}.jomon", "era", "Jōmon Period", jp,
  start=-14000, end=-300, tier="intermediate",
  native_name="縄文時代",
  start_dating_method="radiocarbon-calibrated", standing="consensus",
  summary="Hunter-gatherers who made pottery, settled in villages and grew rich on the sea "
          "— without ever taking up farming.",
  date_note="The phase framework is in calibrated years. The widely repeated start of "
            "'13,000 BCE' is an UNCALIBRATED radiocarbon number presented as a calendar "
            "date; the earliest Japanese pottery at Ōdai Yamamoto I is 13,480-12,680 BP "
            "uncalibrated, which calibrates to 16,140-14,920 cal BP.",
  caveats=[{"kind": "misconception",
            "text": "The familiar '13,000 BCE' start is an uncalibrated radiocarbon figure "
                    "read as a calendar year. Calibrated, the earliest pottery is some "
                    "3,000 years older.",
            "source_ids": ["keally-jomon-dates"]}],
  source_ids=["matsumoto-2017-jomon", "keally-jomon-dates"])
E(f"{jp}.yayoi", "era", "Yayoi Period", jp,
  start=-300, end=300, tier="intermediate",
  native_name="弥生時代")
E(f"{jp}.kofun", "era", "Kofun Period", jp,
  start=300, end=538, tier="intermediate",
  native_name="古墳時代",
  summary="Age of keyhole-shaped tumulus tombs.")

E(f"{jp}.asuka", "era", "Asuka Period", jp,
  start=538, end=710, tier="intermediate",
  native_name="飛鳥時代",
  calendar_ids=["japanese-nengo"])

E(f"{jp}.nara", "era", "Nara Period", jp,
  start=710, end=794, tier="intermediate", native_name="奈良時代",
  calendar_ids=["japanese-nengo"])

E(f"{jp}.heian", "era", "Heian Period", jp,
  start=794, end=1185, tier="foundational", native_name="平安時代",
  calendar_ids=["japanese-nengo"],
  summary="Classical age of Japanese court culture; The Tale of Genji.")

E(f"{jp}.kamakura", "era", "Kamakura Period", jp,
  start=1185, end=1333, tier="foundational", native_name="鎌倉時代",
  calendar_ids=["japanese-nengo"],
  summary="First shogunate; repelled two Mongol invasions.")

E(f"{jp}.kenmu", "era", "Kenmu Restoration", jp, start=1333, end=1336, tier="specialist", native_name="建武の新政")

E(f"{jp}.muromachi", "era", "Muromachi / Nanboku-chō Period", jp,
  start=1336, end=1573, tier="foundational", native_name="室町時代",
  calendar_ids=["japanese-nengo"])

E(f"{jp}.azuchi-momoyama", "era", "Azuchi–Momoyama Period", jp,
  start=1573, end=1603, tier="foundational", native_name="安土桃山時代",
  calendar_ids=["japanese-nengo"],
  summary="Unification wars under Oda Nobunaga, Toyotomi Hideyoshi, and Tokugawa Ieyasu.")
E(f"{jp}.azuchi-momoyama.nobunaga", "reign", "Oda Nobunaga", f"{jp}.azuchi-momoyama", start=1568, end=1582, tier="foundational")
E(f"{jp}.azuchi-momoyama.hideyoshi", "reign", "Toyotomi Hideyoshi", f"{jp}.azuchi-momoyama", start=1582, end=1598, tier="foundational")

E(f"{jp}.edo", "era", "Edo Period", jp,
  start=1603, end=1868, tier="foundational", native_name="江戸時代",
  aliases=["Tokugawa Period"],
  calendar_ids=["japanese-nengo"],
  summary="Tokugawa shogunate; long peace, sakoku isolation, cultural flowering.")
E(f"{jp}.edo.ieyasu", "reign", "Tokugawa Ieyasu", f"{jp}.edo", start=1603, end=1605, tier="foundational",
  summary="Founder of the Tokugawa shogunate.")

E(f"{jp}.modern", "era", "Modern Japan", jp, start=1868, end=None, tier="foundational",
  calendar_ids=["japanese-nengo"],
  summary="From the Meiji Restoration to the present. One nengō per emperor.")

# Modern nengō as Period entities under Modern Japan
for slug, name, native, s, e_year, summary in [
    ("meiji", "Meiji", "明治", 1868, 1912, "Meiji Restoration and rapid modernization. Emperor Meiji (Mutsuhito)."),
    ("taisho", "Taishō", "大正", 1912, 1926, "Democratic reform era; Emperor Taishō (Yoshihito)."),
    ("showa", "Shōwa", "昭和", 1926, 1989, "Longest modern era. Emperor Shōwa (Hirohito). Spans militarism, WWII, and postwar boom."),
    ("heisei", "Heisei", "平成", 1989, 2019, "Emperor Akihito. Ended by voluntary abdication."),
    ("reiwa", "Reiwa", "令和", 2019, None, "Current era. Emperor Naruhito."),
]:
    E(f"{jp}.modern.{slug}", "period", name, f"{jp}.modern",
      start=s, end=e_year, native_name=native,
      tier="foundational",
      summary=summary,
      calendar_ids=["japanese-nengo"])

# --- Pre-Meiji nengō ---------------------------------------------------------
# Every nengō from Taika (645) through Keiō (1865). Placed under the historical
# era their start year falls in. Slugs are romanized nengō with ō/ū collapsed
# to o/u; disambiguating suffix appended where the same nengō name recurs
# across centuries.
# Tuple: (slug, romaji, kanji, start_gregorian, end_gregorian, parent_era_slug)
pre_meiji_nengo = [
    # Asuka (538-710)
    ("taika",           "Taika",           "大化",         645,  650, "asuka"),
    ("hakuchi",         "Hakuchi",         "白雉",         650,  654, "asuka"),
    ("shucho",          "Shuchō",          "朱鳥",         686,  686, "asuka"),
    ("taiho",           "Taihō",           "大宝",         701,  704, "asuka"),
    ("keiun",           "Keiun",           "慶雲",         704,  708, "asuka"),
    # Nara (710-794)
    ("wado",            "Wadō",            "和銅",         708,  715, "nara"),
    ("reiki",           "Reiki",           "霊亀",         715,  717, "nara"),
    ("yoro",            "Yōrō",            "養老",         717,  724, "nara"),
    ("jinki",           "Jinki",           "神亀",         724,  729, "nara"),
    ("tenpyo",          "Tenpyō",          "天平",         729,  749, "nara"),
    ("tenpyo-kanpo",    "Tenpyō-kanpō",    "天平感宝",     749,  749, "nara"),
    ("tenpyo-shoho",    "Tenpyō-shōhō",    "天平勝宝",     749,  757, "nara"),
    ("tenpyo-hoji",     "Tenpyō-hōji",     "天平宝字",     757,  765, "nara"),
    ("tenpyo-jingo",    "Tenpyō-jingo",    "天平神護",     765,  767, "nara"),
    ("jingo-keiun",     "Jingo-keiun",     "神護景雲",     767,  770, "nara"),
    ("hoki",            "Hōki",            "宝亀",         770,  781, "nara"),
    ("ten-o",           "Ten'ō",           "天応",         781,  782, "nara"),
    ("enryaku",         "Enryaku",         "延暦",         782,  806, "nara"),
    # Heian (794-1185)
    ("daido",           "Daidō",           "大同",         806,  810, "heian"),
    ("konin",           "Kōnin",           "弘仁",         810,  824, "heian"),
    ("tencho",          "Tenchō",          "天長",         824,  834, "heian"),
    ("jowa-heian",      "Jōwa",            "承和",         834,  848, "heian"),
    ("kasho-heian",     "Kashō",           "嘉祥",         848,  851, "heian"),
    ("ninju",           "Ninju",           "仁寿",         851,  854, "heian"),
    ("saiko",           "Saikō",           "斉衡",         854,  857, "heian"),
    ("ten-an",          "Ten'an",          "天安",         857,  859, "heian"),
    ("jogan",           "Jōgan",           "貞観",         859,  877, "heian"),
    ("gangyo",          "Gangyō",          "元慶",         877,  885, "heian"),
    ("ninna",           "Ninna",           "仁和",         885,  889, "heian"),
    ("kanpyo-heian",    "Kanpyō",          "寛平",         889,  898, "heian"),
    ("shotai",          "Shōtai",          "昌泰",         898,  901, "heian"),
    ("engi",            "Engi",            "延喜",         901,  923, "heian"),
    ("encho",           "Enchō",           "延長",         923,  931, "heian"),
    ("johei",           "Jōhei",           "承平",         931,  938, "heian"),
    ("tengyo",          "Tengyō",          "天慶",         938,  947, "heian"),
    ("tenryaku",        "Tenryaku",        "天暦",         947,  957, "heian"),
    ("tentoku",         "Tentoku",         "天徳",         957,  961, "heian"),
    ("owa",             "Ōwa",             "応和",         961,  964, "heian"),
    ("koho",            "Kōhō",            "康保",         964,  968, "heian"),
    ("anna",            "Anna",            "安和",         968,  970, "heian"),
    ("tenroku",         "Tenroku",         "天禄",         970,  974, "heian"),
    ("ten-en",          "Ten'en",          "天延",         974,  976, "heian"),
    ("jogen-heian1",    "Jōgen",           "貞元",         976,  978, "heian"),
    ("tengen",          "Tengen",          "天元",         978,  983, "heian"),
    ("eikan",           "Eikan",           "永観",         983,  985, "heian"),
    ("kanna",           "Kanna",           "寛和",         985,  987, "heian"),
    ("eien",            "Eien",            "永延",         987,  989, "heian"),
    ("eiso",            "Eiso",            "永祚",         989,  990, "heian"),
    ("shoryaku",        "Shōryaku",        "正暦",         990,  995, "heian"),
    ("chotoku",         "Chōtoku",         "長徳",         995,  999, "heian"),
    ("choho-heian",     "Chōhō",           "長保",         999, 1004, "heian"),
    ("kanko",           "Kankō",           "寛弘",        1004, 1012, "heian"),
    ("chowa",           "Chōwa",           "長和",        1012, 1017, "heian"),
    ("kannin",          "Kannin",          "寛仁",        1017, 1021, "heian"),
    ("jian",            "Jian",            "治安",        1021, 1024, "heian"),
    ("manju",           "Manju",           "万寿",        1024, 1028, "heian"),
    ("chogen-heian",    "Chōgen",          "長元",        1028, 1037, "heian"),
    ("choryaku",        "Chōryaku",        "長暦",        1037, 1040, "heian"),
    ("chokyu-heian",    "Chōkyū",          "長久",        1040, 1044, "heian"),
    ("kantoku",         "Kantoku",         "寛徳",        1044, 1046, "heian"),
    ("eisho-heian1",    "Eishō",           "永承",        1046, 1053, "heian"),
    ("tengi",           "Tengi",           "天喜",        1053, 1058, "heian"),
    ("kohei",           "Kōhei",           "康平",        1058, 1065, "heian"),
    ("jiryaku",         "Jiryaku",         "治暦",        1065, 1069, "heian"),
    ("enkyu",           "Enkyū",           "延久",        1069, 1074, "heian"),
    ("joho",            "Jōhō",            "承保",        1074, 1077, "heian"),
    ("joryaku",         "Jōryaku",         "承暦",        1077, 1081, "heian"),
    ("eiho",            "Eihō",            "永保",        1081, 1084, "heian"),
    ("otoku",           "Ōtoku",           "応徳",        1084, 1087, "heian"),
    ("kanji-heian",     "Kanji",           "寛治",        1087, 1094, "heian"),
    ("kaho",            "Kahō",            "嘉保",        1094, 1096, "heian"),
    ("eicho",           "Eichō",           "永長",        1096, 1097, "heian"),
    ("jotoku",          "Jōtoku",          "承徳",        1097, 1099, "heian"),
    ("kowa-heian",      "Kōwa",            "康和",        1099, 1104, "heian"),
    ("choji",           "Chōji",           "長治",        1104, 1106, "heian"),
    ("kajo-heian",      "Kajō",            "嘉承",        1106, 1108, "heian"),
    ("tennin",          "Tennin",          "天仁",        1108, 1110, "heian"),
    ("ten-ei",          "Ten'ei",          "天永",        1110, 1113, "heian"),
    ("eikyu",           "Eikyū",           "永久",        1113, 1118, "heian"),
    ("gen-ei",          "Gen'ei",          "元永",        1118, 1120, "heian"),
    ("hoan",            "Hōan",            "保安",        1120, 1124, "heian"),
    ("tenji-heian",     "Tenji",           "天治",        1124, 1126, "heian"),
    ("daiji",           "Daiji",           "大治",        1126, 1131, "heian"),
    ("tensho-heian",    "Tenshō",          "天承",        1131, 1132, "heian"),
    ("chosho",          "Chōshō",          "長承",        1132, 1135, "heian"),
    ("hoen",            "Hōen",            "保延",        1135, 1141, "heian"),
    ("eiji",            "Eiji",            "永治",        1141, 1142, "heian"),
    ("koji-heian",      "Kōji",            "康治",        1142, 1144, "heian"),
    ("ten-yo",          "Ten'yō",          "天養",        1144, 1145, "heian"),
    ("kyuan",           "Kyūan",           "久安",        1145, 1151, "heian"),
    ("ninpei",          "Ninpei",          "仁平",        1151, 1154, "heian"),
    ("kyuju",           "Kyūju",           "久寿",        1154, 1156, "heian"),
    ("hogen",           "Hōgen",           "保元",        1156, 1159, "heian"),
    ("heiji",           "Heiji",           "平治",        1159, 1160, "heian"),
    ("eiryaku",         "Eiryaku",         "永暦",        1160, 1161, "heian"),
    ("oho",             "Ōhō",             "応保",        1161, 1163, "heian"),
    ("chokan",          "Chōkan",          "長寛",        1163, 1165, "heian"),
    ("eiman",           "Eiman",           "永万",        1165, 1166, "heian"),
    ("nin-an",          "Nin'an",          "仁安",        1166, 1169, "heian"),
    ("kao",             "Kaō",             "嘉応",        1169, 1171, "heian"),
    ("joan",            "Jōan",            "承安",        1171, 1175, "heian"),
    ("angen",           "Angen",           "安元",        1175, 1177, "heian"),
    ("jisho",           "Jishō",           "治承",        1177, 1181, "heian"),
    ("yowa",            "Yōwa",            "養和",        1181, 1182, "heian"),
    ("juei",            "Juei",            "寿永",        1182, 1185, "heian"),
    ("genryaku",        "Genryaku",        "元暦",        1184, 1185, "heian"),
    # Kamakura (1185-1333)
    # Note: two nengō romanize as "Genkō" but have different native names (元亨 / 元弘).
    # They are disambiguated by suffix in the id (genko-kamakura1 vs genko-kamakura2).
    ("bunji",           "Bunji",           "文治",        1185, 1190, "kamakura"),
    ("kenkyu",          "Kenkyū",          "建久",        1190, 1199, "kamakura"),
    ("shoji",           "Shōji",           "正治",        1199, 1201, "kamakura"),
    ("kennin",          "Kennin",          "建仁",        1201, 1204, "kamakura"),
    ("genkyu",          "Genkyū",          "元久",        1204, 1206, "kamakura"),
    ("ken-ei",          "Ken'ei",          "建永",        1206, 1207, "kamakura"),
    ("jogen-kamakura",  "Jōgen",           "承元",        1207, 1211, "kamakura"),
    ("kenryaku",        "Kenryaku",        "建暦",        1211, 1213, "kamakura"),
    ("kenpo",           "Kenpō",           "建保",        1213, 1219, "kamakura"),
    ("jokyu",           "Jōkyū",           "承久",        1219, 1222, "kamakura"),
    ("joo-kamakura",    "Jōō",             "貞応",        1222, 1224, "kamakura"),
    ("gennin",          "Gennin",          "元仁",        1224, 1225, "kamakura"),
    ("karoku",          "Karoku",          "嘉禄",        1225, 1227, "kamakura"),
    ("antei",           "Antei",           "安貞",        1227, 1229, "kamakura"),
    ("kangi",           "Kangi",           "寛喜",        1229, 1232, "kamakura"),
    ("joei",            "Jōei",            "貞永",        1232, 1233, "kamakura"),
    ("tenpuku",         "Tenpuku",         "天福",        1233, 1234, "kamakura"),
    ("bunryaku",        "Bunryaku",        "文暦",        1234, 1235, "kamakura"),
    ("katei",           "Katei",           "嘉禎",        1235, 1238, "kamakura"),
    ("ryakunin",        "Ryakunin",        "暦仁",        1238, 1239, "kamakura"),
    ("en-o",            "En'ō",            "延応",        1239, 1240, "kamakura"),
    ("ninji",           "Ninji",           "仁治",        1240, 1243, "kamakura"),
    ("kangen",          "Kangen",          "寛元",        1243, 1247, "kamakura"),
    ("hoji",            "Hōji",            "宝治",        1247, 1249, "kamakura"),
    ("kencho",          "Kenchō",          "建長",        1249, 1256, "kamakura"),
    ("kogen",           "Kōgen",           "康元",        1256, 1257, "kamakura"),
    ("shoka",           "Shōka",           "正嘉",        1257, 1259, "kamakura"),
    ("shogen",          "Shōgen",          "正元",        1259, 1260, "kamakura"),
    ("bun-o",           "Bun'ō",           "文応",        1260, 1261, "kamakura"),
    ("kocho",           "Kōchō",           "弘長",        1261, 1264, "kamakura"),
    ("bun-ei",          "Bun'ei",          "文永",        1264, 1275, "kamakura"),
    ("kenji",           "Kenji",           "建治",        1275, 1278, "kamakura"),
    ("koan-kamakura",   "Kōan",            "弘安",        1278, 1288, "kamakura"),
    ("shoo",            "Shōō",            "正応",        1288, 1293, "kamakura"),
    ("einin",           "Einin",           "永仁",        1293, 1299, "kamakura"),
    ("shoan",           "Shōan",           "正安",        1299, 1302, "kamakura"),
    ("kengen",          "Kengen",          "乾元",        1302, 1303, "kamakura"),
    ("kagen",           "Kagen",           "嘉元",        1303, 1306, "kamakura"),
    ("tokuji",          "Tokuji",          "徳治",        1306, 1308, "kamakura"),
    ("enkyo-kamakura",  "Enkyō",           "延慶",        1308, 1311, "kamakura"),
    ("ocho",            "Ōchō",            "応長",        1311, 1312, "kamakura"),
    ("showa-kamakura",  "Shōwa",           "正和",        1312, 1317, "kamakura"),
    ("bunpo",           "Bunpō",           "文保",        1317, 1319, "kamakura"),
    ("gen-o",           "Gen'ō",           "元応",        1319, 1321, "kamakura"),
    ("genko-kamakura1", "Genkō (元亨)",    "元亨",        1321, 1324, "kamakura"),
    ("shochu",          "Shōchū",          "正中",        1324, 1326, "kamakura"),
    ("karyaku",         "Karyaku",         "嘉暦",        1326, 1329, "kamakura"),
    ("gentoku",         "Gentoku",         "元徳",        1329, 1332, "kamakura"),
    ("genko-kamakura2", "Genkō (元弘)",    "元弘",        1331, 1334, "kamakura"),
    # Kenmu Restoration (1333-1336)
    ("kenmu-era",       "Kenmu",           "建武",        1334, 1336, "kenmu"),
    # Muromachi / Nanboku-chō (1336-1573)
    #   Southern Court (Daikakuji-tō)
    ("engen",           "Engen",           "延元",        1336, 1340, "muromachi"),
    ("kokoku",          "Kōkoku",          "興国",        1340, 1347, "muromachi"),
    ("shohei",          "Shōhei",          "正平",        1347, 1370, "muromachi"),
    ("kentoku",         "Kentoku",         "建徳",        1370, 1372, "muromachi"),
    ("bunchu",          "Bunchū",          "文中",        1372, 1375, "muromachi"),
    ("tenju",           "Tenju",           "天授",        1375, 1381, "muromachi"),
    ("kowa-nanboku",    "Kōwa",            "弘和",        1381, 1384, "muromachi"),
    ("genchu",          "Genchū",          "元中",        1384, 1392, "muromachi"),
    #   Northern Court (Jimyōin-tō)
    ("shokei",          "Shōkei",          "正慶",        1332, 1333, "muromachi"),
    ("ryakuo",          "Ryakuō",          "暦応",        1338, 1342, "muromachi"),
    ("koei",            "Kōei",            "康永",        1342, 1345, "muromachi"),
    ("jowa-nanboku",    "Jōwa",            "貞和",        1345, 1350, "muromachi"),
    ("kanno",           "Kannō",           "観応",        1350, 1352, "muromachi"),
    ("bunna",           "Bunna",           "文和",        1352, 1356, "muromachi"),
    ("enbun",           "Enbun",           "延文",        1356, 1361, "muromachi"),
    ("koan-nanboku",    "Kōan",            "康安",        1361, 1362, "muromachi"),
    ("joji",            "Jōji",            "貞治",        1362, 1368, "muromachi"),
    ("oan",             "Ōan",             "応安",        1368, 1375, "muromachi"),
    ("eiwa",            "Eiwa",            "永和",        1375, 1379, "muromachi"),
    ("koryaku",         "Kōryaku",         "康暦",        1379, 1381, "muromachi"),
    ("eitoku",          "Eitoku",          "永徳",        1381, 1384, "muromachi"),
    ("shitoku",         "Shitoku",         "至徳",        1384, 1387, "muromachi"),
    ("kakei",           "Kakei",           "嘉慶",        1387, 1389, "muromachi"),
    ("koo",             "Kōō",             "康応",        1389, 1390, "muromachi"),
    ("meitoku",         "Meitoku",         "明徳",        1390, 1394, "muromachi"),
    #   Post-reunification Muromachi
    ("oei",             "Ōei",             "応永",        1394, 1428, "muromachi"),
    ("shocho",          "Shōchō",          "正長",        1428, 1429, "muromachi"),
    ("eikyo",           "Eikyō",           "永享",        1429, 1441, "muromachi"),
    ("kakitsu",         "Kakitsu",         "嘉吉",        1441, 1444, "muromachi"),
    ("bun-an",          "Bun'an",          "文安",        1444, 1449, "muromachi"),
    ("hotoku",          "Hōtoku",          "宝徳",        1449, 1452, "muromachi"),
    ("kyotoku",         "Kyōtoku",         "享徳",        1452, 1455, "muromachi"),
    ("kosho",           "Kōshō",           "康正",        1455, 1457, "muromachi"),
    ("choroku",         "Chōroku",         "長禄",        1457, 1460, "muromachi"),
    ("kansho",          "Kanshō",          "寛正",        1460, 1466, "muromachi"),
    ("bunsho",          "Bunshō",          "文正",        1466, 1467, "muromachi"),
    ("onin",            "Ōnin",            "応仁",        1467, 1469, "muromachi"),
    ("bunmei",          "Bunmei",          "文明",        1469, 1487, "muromachi"),
    ("chokyo",          "Chōkyō",          "長享",        1487, 1489, "muromachi"),
    ("entoku",          "Entoku",          "延徳",        1489, 1492, "muromachi"),
    ("meio",            "Meiō",            "明応",        1492, 1501, "muromachi"),
    ("bunki",           "Bunki",           "文亀",        1501, 1504, "muromachi"),
    ("eisho-muromachi", "Eishō",           "永正",        1504, 1521, "muromachi"),
    ("daiei",           "Daiei",           "大永",        1521, 1528, "muromachi"),
    ("kyoroku",         "Kyōroku",         "享禄",        1528, 1532, "muromachi"),
    ("tenbun",          "Tenbun",          "天文",        1532, 1555, "muromachi"),
    ("koji-muromachi",  "Kōji",            "弘治",        1555, 1558, "muromachi"),
    ("eiroku",          "Eiroku",          "永禄",        1558, 1570, "muromachi"),
    ("genki",           "Genki",           "元亀",        1570, 1573, "muromachi"),
    # Azuchi-Momoyama (1573-1603)
    ("tensho-azuchi",   "Tenshō",          "天正",        1573, 1592, "azuchi-momoyama"),
    ("bunroku",         "Bunroku",         "文禄",        1592, 1596, "azuchi-momoyama"),
    ("keicho",          "Keichō",          "慶長",        1596, 1615, "azuchi-momoyama"),
    # Edo (1603-1868)
    ("genna",           "Genna",           "元和",        1615, 1624, "edo"),
    ("kan-ei",          "Kan'ei",          "寛永",        1624, 1644, "edo"),
    ("shoho",           "Shōhō",           "正保",        1644, 1648, "edo"),
    ("keian",           "Keian",           "慶安",        1648, 1652, "edo"),
    ("joo-edo",         "Jōō",             "承応",        1652, 1655, "edo"),
    ("meireki",         "Meireki",         "明暦",        1655, 1658, "edo"),
    ("manji",           "Manji",           "万治",        1658, 1661, "edo"),
    ("kanbun",          "Kanbun",          "寛文",        1661, 1673, "edo"),
    ("enpo",            "Enpō",            "延宝",        1673, 1681, "edo"),
    ("tenna",           "Tenna",           "天和",        1681, 1684, "edo"),
    ("jokyo",           "Jōkyō",           "貞享",        1684, 1688, "edo"),
    ("genroku",         "Genroku",         "元禄",        1688, 1704, "edo"),
    ("hoei",            "Hōei",            "宝永",        1704, 1711, "edo"),
    ("shotoku-edo",     "Shōtoku",         "正徳",        1711, 1716, "edo"),
    ("kyoho",           "Kyōhō",           "享保",        1716, 1736, "edo"),
    ("genbun",          "Genbun",          "元文",        1736, 1741, "edo"),
    ("kanpo",           "Kanpō",           "寛保",        1741, 1744, "edo"),
    ("enkyo-edo",       "Enkyō",           "延享",        1744, 1748, "edo"),
    ("kan-en",          "Kan'en",          "寛延",        1748, 1751, "edo"),
    ("horeki",          "Hōreki",          "宝暦",        1751, 1764, "edo"),
    ("meiwa",           "Meiwa",           "明和",        1764, 1772, "edo"),
    ("an-ei",           "An'ei",           "安永",        1772, 1781, "edo"),
    ("tenmei",          "Tenmei",          "天明",        1781, 1789, "edo"),
    ("kansei",          "Kansei",          "寛政",        1789, 1801, "edo"),
    ("kyowa",           "Kyōwa",           "享和",        1801, 1804, "edo"),
    ("bunka",           "Bunka",           "文化",        1804, 1818, "edo"),
    ("bunsei",          "Bunsei",          "文政",        1818, 1830, "edo"),
    ("tenpo-edo",       "Tenpō",           "天保",        1830, 1844, "edo"),
    ("koka",            "Kōka",            "弘化",        1844, 1848, "edo"),
    ("kaei",            "Kaei",            "嘉永",        1848, 1854, "edo"),
    ("ansei",           "Ansei",           "安政",        1854, 1860, "edo"),
    ("man-en",          "Man'en",          "万延",        1860, 1861, "edo"),
    ("bunkyu",          "Bunkyū",          "文久",        1861, 1864, "edo"),
    ("genji",           "Genji",           "元治",        1864, 1865, "edo"),
    ("keio",            "Keiō",            "慶応",        1865, 1868, "edo"),
]

# Note on 'notes' field: Northern/Southern court eras during the Nanboku-chō
# split (1336-1392) coexisted. Both are placed under the Muromachi era.
_nanboku_south = {
    "engen", "kokoku", "shohei", "kentoku", "bunchu", "tenju",
    "kowa-nanboku", "genchu",
}
_nanboku_north = {
    "shokei", "ryakuo", "koei", "jowa-nanboku", "kanno", "bunna", "enbun",
    "koan-nanboku", "joji", "oan", "eiwa", "koryaku", "eitoku", "shitoku",
    "kakei", "koo", "meitoku",
}

for slug, romaji, kanji, s_year, e_year, parent_era in pre_meiji_nengo:
    aliases = []
    court_note = None
    if slug in _nanboku_south:
        court_note = "Southern Court nengō during the Nanboku-chō schism."
    elif slug in _nanboku_north:
        court_note = "Northern Court nengō during the Nanboku-chō schism."
    E(f"{jp}.{parent_era}.{slug}", "period", romaji, f"{jp}.{parent_era}",
      start=s_year, end=e_year, native_name=kanji,
      tier="specialist",
      summary=court_note,
      calendar_ids=["japanese-nengo"])


# =============================================================================
# CHINA (dynasty family / dynasty / emperor)
# =============================================================================

cn = "east-asia.china"

E(f"{cn}.legendary", "era", "Legendary & Neolithic China", cn, start=-5000, end=-1600, tier="intermediate")
E(f"{cn}.shang", "era", "Shang Dynasty", cn, start=-1600, end=-1046, tier="foundational",
  native_name="商朝",
  summary="First historically confirmed Chinese dynasty. Oracle bones; bronze ritual vessels.")
E(f"{cn}.zhou", "era", "Zhou Dynasty", cn, start=-1046, end=-256, tier="foundational", native_name="周朝",
  summary="Longest dynasty in Chinese history. Split into Western and Eastern (Spring-Autumn + Warring States).")
E(f"{cn}.zhou.western", "period", "Western Zhou", f"{cn}.zhou", start=-1046, end=-771)
E(f"{cn}.zhou.eastern", "period", "Eastern Zhou", f"{cn}.zhou", start=-770, end=-256)
E(f"{cn}.zhou.eastern.spring-autumn", "period", "Spring and Autumn Period", f"{cn}.zhou.eastern", start=-770, end=-476,
  summary="Time of Confucius and Laozi.")
E(f"{cn}.zhou.eastern.warring-states", "period", "Warring States Period", f"{cn}.zhou.eastern",
  start=-475, end=-221, tier="foundational",
  summary="Seven kingdoms fought for supremacy; Hundred Schools of Thought.")

E(f"{cn}.qin", "era", "Qin Dynasty", cn, start=-221, end=-206, tier="foundational", native_name="秦朝",
  summary="First unified imperial state.")
E(f"{cn}.qin.shi-huang", "reign", "Qin Shi Huangdi", f"{cn}.qin",
  start=-221, end=-210, tier="foundational",
  summary="First Emperor of unified China. Standardized script, currency, and weights. Terracotta Army.")

E(f"{cn}.han", "era", "Han Dynasty", cn, start=-206, end=220, tier="foundational", native_name="漢朝",
  summary="Classical Chinese empire; namesake of the Han Chinese ethnicity.")
E(f"{cn}.han.western", "period", "Western Han", f"{cn}.han", start=-206, end=9)
E(f"{cn}.han.western.gaozu", "reign", "Emperor Gaozu (Liu Bang)", f"{cn}.han.western", start=-202, end=-195)
E(f"{cn}.han.western.wu", "reign", "Emperor Wu", f"{cn}.han.western",
  start=-141, end=-87, tier="foundational",
  summary="Made Confucianism the state ideology; opened the Silk Road via Zhang Qian.")
E(f"{cn}.han.xin", "period", "Xin Interregnum (Wang Mang)", f"{cn}.han", start=9, end=23)
E(f"{cn}.han.eastern", "period", "Eastern Han", f"{cn}.han", start=25, end=220,
  summary="Paper invented by Cai Lun (c. 105); Buddhism enters China.")

E(f"{cn}.three-kingdoms", "era", "Three Kingdoms", cn, start=220, end=280, tier="foundational", native_name="三國")
E(f"{cn}.jin", "era", "Jin Dynasty", cn, start=266, end=420, tier="intermediate")
E(f"{cn}.north-south", "era", "Northern and Southern Dynasties", cn, start=420, end=589, tier="intermediate")

E(f"{cn}.sui", "era", "Sui Dynasty", cn, start=581, end=618, tier="intermediate", native_name="隋朝")
E(f"{cn}.tang", "era", "Tang Dynasty", cn, start=618, end=907, tier="foundational", native_name="唐朝",
  summary="Golden age of Chinese poetry and cosmopolitan trade.")
E(f"{cn}.tang.taizong", "reign", "Emperor Taizong", f"{cn}.tang", start=626, end=649, tier="intermediate")
E(f"{cn}.tang.wu-zetian", "reign", "Empress Wu Zetian", f"{cn}.tang",
  start=690, end=705, tier="foundational",
  summary="Only woman to rule China as emperor in her own right.")
E(f"{cn}.tang.xuanzong", "reign", "Emperor Xuanzong", f"{cn}.tang", start=712, end=756)

E(f"{cn}.five-dynasties", "era", "Five Dynasties and Ten Kingdoms", cn, start=907, end=979, tier="specialist")

E(f"{cn}.song", "era", "Song Dynasty", cn, start=960, end=1279, tier="foundational", native_name="宋朝",
  summary="Economic and technological golden age: printing, gunpowder, compass, paper money.")
E(f"{cn}.song.northern", "period", "Northern Song", f"{cn}.song", start=960, end=1127)
E(f"{cn}.song.southern", "period", "Southern Song", f"{cn}.song", start=1127, end=1279)

E(f"{cn}.yuan", "era", "Yuan Dynasty", cn, start=1271, end=1370, tier="foundational", native_name="元朝",
  date_note="Yuan formally ended in 1368 when the Ming took Beijing; Huizong ruled from Mongolia until 1370 (Northern Yuan).",
  summary="Mongol-ruled China under the descendants of Genghis Khan.",
  cross_parent_ids=["central-asia.mongol-empire"],
  links=[
      {"type": "successor_state_of", "entity_id": "central-asia.mongol-empire",
       "start_year": 1271, "end_year": 1368,
       "note": "Mongol-ruled dynasty in China after the fragmentation of the unified empire."},
      {"type": "predecessor_state_of", "entity_id": f"{cn}.ming",
       "note": "Overthrown by the Ming, which claimed the Mandate of Heaven."},
  ])
E(f"{cn}.yuan.kublai", "reign", "Kublai Khan", f"{cn}.yuan",
  start=1260, end=1294, tier="foundational",
  summary="Grandson of Genghis; founder of the Yuan Dynasty.")

E(f"{cn}.ming", "era", "Ming Dynasty", cn, start=1368, end=1644, tier="foundational", native_name="明朝",
  summary="Restored Han Chinese rule; Zheng He's voyages; Forbidden City built.")
E(f"{cn}.ming.hongwu", "reign", "Hongwu Emperor", f"{cn}.ming", start=1368, end=1398, tier="intermediate")
E(f"{cn}.ming.yongle", "reign", "Yongle Emperor", f"{cn}.ming", start=1402, end=1424, tier="foundational",
  summary="Commissioned Zheng He's treasure voyages; moved capital to Beijing.")

E(f"{cn}.qing", "era", "Qing Dynasty", cn, start=1644, end=1912, tier="foundational", native_name="清朝",
  summary="Manchu-ruled last imperial dynasty.")
E(f"{cn}.qing.kangxi", "reign", "Kangxi Emperor", f"{cn}.qing", start=1661, end=1722, tier="foundational")
E(f"{cn}.qing.qianlong", "reign", "Qianlong Emperor", f"{cn}.qing", start=1735, end=1796, tier="foundational")
E(f"{cn}.qing.cixi", "reign", "Empress Dowager Cixi", f"{cn}.qing", start=1861, end=1908, tier="intermediate")

E(f"{cn}.roc", "era", "Republic of China", cn, start=1912, end=1949, tier="foundational")
E(f"{cn}.prc", "era", "People's Republic of China", cn, start=1949, end=None, tier="foundational")


# =============================================================================
# KOREA (condensed)
# =============================================================================

kr = "east-asia.korea"
E(f"{kr}.gojoseon", "era", "Gojoseon", kr, start=-2333, end=-108, date_precision="traditional", tier="specialist")
E(f"{kr}.three-kingdoms", "era", "Three Kingdoms of Korea", kr, start=-57, end=668, tier="intermediate",
  summary="Goguryeo, Baekje, Silla.")
E(f"{kr}.unified-silla", "era", "Unified Silla", kr, start=668, end=935, tier="intermediate")
E(f"{kr}.goryeo", "era", "Goryeo Dynasty", kr, start=918, end=1392, tier="foundational",
  summary="Origin of the name 'Korea'; celadon ceramics; movable metal type.")
E(f"{kr}.joseon", "era", "Joseon Dynasty", kr, start=1392, end=1897, tier="foundational",
  summary="Long-lived Confucian monarchy; Hangul script created under Sejong the Great.")
E(f"{kr}.joseon.sejong", "reign", "King Sejong the Great", f"{kr}.joseon", start=1418, end=1450, tier="foundational")
E(f"{kr}.korean-empire", "era", "Korean Empire", kr, start=1897, end=1910, tier="intermediate")
E(f"{kr}.colonial", "era", "Japanese Colonial Rule", kr, start=1910, end=1945, tier="foundational")
E(f"{kr}.divided", "era", "Divided Korea", kr, start=1945, end=None, tier="foundational")


# =============================================================================
# MESOPOTAMIA (condensed but full arc)
# =============================================================================

mes = "west-asia.mesopotamia"
E(f"{mes}.sumerian", "era", "Sumerian Early Dynastic", mes, start=-2900, end=-2334, tier="foundational",
  summary="World's first cities: Uruk, Ur, Lagash, Kish.")
E(f"{mes}.sumerian.gilgamesh", "reign", "Gilgamesh (legendary)", f"{mes}.sumerian",
  start=-2700, end=-2600, date_precision="traditional", tier="foundational",
  summary="Legendary king of Uruk; hero of the eponymous epic.")
E(f"{mes}.akkadian", "era", "Akkadian Empire", mes, start=-2334, end=-2154, tier="foundational",
  summary="First empire in world history.")
E(f"{mes}.akkadian.sargon", "reign", "Sargon of Akkad", f"{mes}.akkadian", start=-2334, end=-2279, tier="foundational")
E(f"{mes}.ur3", "era", "Ur III (Neo-Sumerian)", mes, start=-2112, end=-2004, tier="intermediate")
E(f"{mes}.old-babylonian", "era", "Old Babylonian Empire", mes, start=-2000, end=-1600, tier="foundational",
  date_precision="disputed",
  date_note="Middle Chronology, like every date in this era and the Kassite era that follows "
            "it. The whole 2nd-millennium Mesopotamian sequence shifts together depending on "
            "which chronology is adopted; see Hammurabi's reign for the detail.",
  source_ids=["isac-dating-fall-of-babylon"])
# 1792-1750 shipped here for ten releases as a bare fact. It is the MIDDLE
# CHRONOLOGY figure, and the competing schemes move it by up to 120 years --
# the same failure class as Monte Verde, a number quoted without the frame that
# produced it. Everything from Ur III to the Kassites moves with it.
E(f"{mes}.old-babylonian.hammurabi", "reign", "Hammurabi", f"{mes}.old-babylonian",
  start=-1792, end=-1750, tier="foundational",
  summary="Famous for the Code of Hammurabi, one of the earliest surviving law codes.",
  start_dating_method="calendar", end_dating_method="calendar",
  standing="majority", date_precision="disputed",
  date_note="These are Middle Chronology dates, which is the usual default but only one of "
            "four schemes in use. The High, Low and Ultra-Low chronologies place the same "
            "reign progressively later or earlier, across a spread of roughly 120 years. "
            "There is no independent dating here: the sequence rests on king-lists anchored "
            "to the Venus Tablet of Ammi-saduqa, whose observations are astronomically "
            "periodic and so fit several real years equally well.",
  alternatives=[
      {"label": "Low Chronology, c. 1728-1686 BC", "standing": "minority",
       "start_year": -1728, "end_year": -1686, "dating_method": "calendar",
       "note": "One of the lower readings of the same Venus observations.",
       "source_ids": ["isac-dating-fall-of-babylon"]},
  ],
  caveats=[{"kind": "misconception",
            "text": "Quoted almost everywhere as simply Hammurabi's dates. Sources differing "
                    "by decades are usually not in error; they have chosen a different "
                    "chronology.",
            "source_ids": ["isac-dating-fall-of-babylon"]}],
  as_of="2026-08-08",
  source_ids=["isac-dating-fall-of-babylon"])
E(f"{mes}.kassite", "era", "Kassite Babylon", mes, start=-1595, end=-1155, tier="specialist")
E(f"{mes}.assyrian", "era", "Assyrian Empires", mes, start=-2025, end=-609, tier="foundational")
E(f"{mes}.assyrian.middle", "period", "Middle Assyrian Empire", f"{mes}.assyrian", start=-1365, end=-1050)
E(f"{mes}.assyrian.neo", "period", "Neo-Assyrian Empire", f"{mes}.assyrian", start=-911, end=-609, tier="foundational",
  summary="Mass deportations as imperial policy; library of Nineveh.")
E(f"{mes}.assyrian.neo.ashurbanipal", "reign", "Ashurbanipal", f"{mes}.assyrian.neo", start=-669, end=-631, tier="intermediate")
E(f"{mes}.neo-babylonian", "era", "Neo-Babylonian Empire", mes, start=-626, end=-539, tier="foundational")
E(f"{mes}.neo-babylonian.nebuchadnezzar2", "reign", "Nebuchadnezzar II", f"{mes}.neo-babylonian",
  start=-605, end=-562, tier="foundational",
  summary="Destroyed Jerusalem (587 BCE); traditional builder of the Hanging Gardens.")


# =============================================================================
# LEVANT & ISRAEL/JUDAH (condensed)
# =============================================================================

E(f"{mes}.israel-judah", "era", "Kingdoms of Israel and Judah", mes, start=-1050, end=-586, tier="foundational",
  summary="Iron Age Hebrew kingdoms.")
E(f"{mes}.israel-judah.david", "reign", "David", f"{mes}.israel-judah",
  start=-1010, end=-970, date_precision="traditional", tier="foundational")
E(f"{mes}.israel-judah.solomon", "reign", "Solomon", f"{mes}.israel-judah",
  start=-970, end=-931, date_precision="traditional", tier="foundational")

E(f"{mes}.phoenicia", "era", "Phoenician City-States", mes, start=-1500, end=-539, tier="intermediate",
  summary="Tyre, Sidon, Byblos. Founded Carthage and colonized the Mediterranean.")


# =============================================================================
# IRAN / PERSIA
# =============================================================================

ir = "west-asia.iran"
E(f"{ir}.elam", "era", "Elam", ir, start=-3200, end=-539, tier="specialist")
E(f"{ir}.median", "era", "Median Empire", ir, start=-678, end=-549, tier="intermediate")
E(f"{ir}.achaemenid", "era", "Achaemenid Empire", ir, start=-550, end=-330, tier="foundational",
  summary="First Persian empire; largest of its time.")
E(f"{ir}.achaemenid.cyrus2", "reign", "Cyrus II the Great", f"{ir}.achaemenid",
  start=-559, end=-530, tier="foundational",
  summary="Founder of the Achaemenid Empire; freed the Jews from Babylonian exile.")
E(f"{ir}.achaemenid.cambyses2", "reign", "Cambyses II", f"{ir}.achaemenid", start=-530, end=-522,
  summary="Conquered Egypt (525 BCE).")
E(f"{ir}.achaemenid.darius1", "reign", "Darius I the Great", f"{ir}.achaemenid",
  start=-522, end=-486, tier="foundational",
  summary="Great organizer; built Persepolis; invaded Greece and lost at Marathon.")
E(f"{ir}.achaemenid.xerxes1", "reign", "Xerxes I", f"{ir}.achaemenid",
  start=-486, end=-465, tier="foundational",
  summary="Led the second Persian invasion of Greece; lost at Salamis and Plataea.")
E(f"{ir}.achaemenid.darius3", "reign", "Darius III", f"{ir}.achaemenid", start=-336, end=-330,
  summary="Last Achaemenid; defeated by Alexander the Great.")
E(f"{ir}.seleucid", "era", "Seleucid Empire", ir, start=-312, end=-63, tier="foundational",
  cross_parent_ids=["europe.mediterranean.hellenistic"])
E(f"{ir}.parthian", "era", "Parthian (Arsacid) Empire", ir, start=-247, end=224, tier="foundational")
E(f"{ir}.parthian.mithridates1", "reign", "Mithridates I", f"{ir}.parthian", start=-171, end=-138)
E(f"{ir}.sasanian", "era", "Sasanian Empire", ir, start=224, end=651, tier="foundational",
  summary="Last pre-Islamic Persian empire; peer superpower of Rome/Byzantium.")
E(f"{ir}.sasanian.ardashir1", "reign", "Ardashir I", f"{ir}.sasanian", start=224, end=242, tier="intermediate")
E(f"{ir}.sasanian.shapur1", "reign", "Shapur I", f"{ir}.sasanian", start=240, end=270, tier="foundational",
  summary="Captured Roman Emperor Valerian alive at Edessa (260 CE).")
E(f"{ir}.sasanian.khosrow1", "reign", "Khosrow I Anushirvan", f"{ir}.sasanian", start=531, end=579, tier="foundational",
  summary="Golden-age king; legal and administrative reforms.")
E(f"{ir}.sasanian.khosrow2", "reign", "Khosrow II Parviz", f"{ir}.sasanian", start=590, end=628, tier="intermediate")
E(f"{ir}.safavid", "era", "Safavid Empire", ir, start=1501, end=1736, tier="foundational",
  summary="Made Shia Islam the state religion.")
E(f"{ir}.safavid.abbas1", "reign", "Abbas I the Great", f"{ir}.safavid", start=1588, end=1629, tier="intermediate")
E(f"{ir}.qajar", "era", "Qajar Dynasty", ir, start=1789, end=1925, tier="intermediate")
E(f"{ir}.pahlavi", "era", "Pahlavi Dynasty", ir, start=1925, end=1979, tier="foundational")
E(f"{ir}.islamic-republic", "era", "Islamic Republic of Iran", ir, start=1979, end=None, tier="foundational")


# =============================================================================
# ISLAMIC CALIPHATES (cross-regional but rooted in West Asia)
# =============================================================================

isl = "west-asia.arabia"
E(f"{isl}.pre-islamic", "era", "Pre-Islamic Arabia", isl, start=-3000, end=610, tier="intermediate")
E(f"{isl}.rise-islam", "era", "Rise of Islam", isl, start=610, end=632, tier="foundational")
E(f"{isl}.rise-islam.muhammad", "reign", "Prophet Muhammad", f"{isl}.rise-islam",
  start=610, end=632, tier="foundational",
  calendar_ids=["hijri"])

E("global.multi-regional.rashidun", "era", "Rashidun Caliphate", "cross-regional", start=632, end=661, tier="foundational",
  calendar_ids=["hijri"],
  summary="First four 'rightly guided' caliphs; rapid conquest of Persia, Levant, and Egypt.")
E("global.multi-regional.umayyad", "era", "Umayyad Caliphate", "cross-regional", start=661, end=750, tier="foundational",
  calendar_ids=["hijri"],
  summary="Dynasty ruling from Damascus. Reached from Iberia to Central Asia.")
E("global.multi-regional.abbasid", "era", "Abbasid Caliphate", "cross-regional", start=750, end=1258, tier="foundational",
  calendar_ids=["hijri"],
  summary="Ruled from Baghdad; Islamic Golden Age. Ended by Mongol sack of Baghdad.")
E("global.multi-regional.abbasid.harun", "reign", "Harun al-Rashid", "global.multi-regional.abbasid", start=786, end=809, tier="foundational")
E("global.multi-regional.fatimid", "era", "Fatimid Caliphate", "cross-regional", start=909, end=1171, tier="intermediate",
  calendar_ids=["hijri"],
  summary="Isma'ili Shia caliphate; founded Cairo and Al-Azhar.")
E("global.multi-regional.ottoman", "era", "Ottoman Empire", "cross-regional", start=1299, end=1922, tier="foundational",
  calendar_ids=["hijri"],
  summary="Multi-continental empire spanning Anatolia, the Balkans, North Africa, and the Arab world.")
E("global.multi-regional.ottoman.mehmed2", "reign", "Mehmed II the Conqueror", "global.multi-regional.ottoman", start=1451, end=1481, tier="foundational",
  summary="Conquered Constantinople in 1453, ending the Byzantine Empire.")
E("global.multi-regional.ottoman.suleiman", "reign", "Suleiman I the Magnificent", "global.multi-regional.ottoman", start=1520, end=1566, tier="foundational")


# =============================================================================
# GREECE
# =============================================================================

gr = "europe.mediterranean.greece"
E(gr, "era", "Ancient Greece", "europe.mediterranean", start=-3000, end=-146, tier="foundational")
E(f"{gr}.minoan", "period", "Minoan Civilization", gr, start=-3000, end=-1450, tier="intermediate",
  summary="Bronze Age Cretan civilization; palace at Knossos.")
E(f"{gr}.mycenaean", "period", "Mycenaean Civilization", gr, start=-1600, end=-1100, tier="foundational")
E(f"{gr}.dark-age", "period", "Greek Dark Ages", gr, start=-1100, end=-800, tier="intermediate")
E(f"{gr}.archaic", "period", "Archaic Greece", gr, start=-800, end=-480, tier="foundational")
E(f"{gr}.classical", "period", "Classical Greece", gr, start=-480, end=-323, tier="foundational",
  summary="Age of Athens' Golden Age, the Peloponnesian War, and philosophers Socrates, Plato, and Aristotle.")
E(f"{gr}.classical.pericles", "reign", "Pericles (statesman)", f"{gr}.classical", start=-461, end=-429, tier="foundational")
E("europe.mediterranean.macedon", "period", "Kingdom of Macedon",
  "europe.mediterranean", start=-808, end=-146, tier="foundational")
E("europe.mediterranean.macedon.philip2", "reign", "Philip II of Macedon", "europe.mediterranean.macedon",
  start=-359, end=-336, tier="foundational")
E("europe.mediterranean.macedon.alexander", "reign", "Alexander the Great", "europe.mediterranean.macedon",
  start=-336, end=-323, tier="foundational",
  aliases=["Alexander III of Macedon"],
  summary="Conquered the Achaemenid Empire, reaching India. Ushered in the Hellenistic Age.",
  cross_parent_ids=["west-asia.iran.achaemenid"])
E("europe.mediterranean.hellenistic", "era", "Hellenistic Period", "europe.mediterranean",
  start=-323, end=-31, tier="foundational")


# =============================================================================
# ROME
# =============================================================================

rome = "europe.mediterranean.rome"
E(rome, "era", "Ancient Rome", "europe.mediterranean", start=-753, end=476, tier="foundational",
  calendar_ids=["roman-auc"])

E(f"{rome}.kingdom", "period", "Roman Kingdom", rome, start=-753, end=-509, tier="intermediate",
  date_precision="traditional",
  summary="Seven legendary kings from Romulus to Tarquin the Proud.")
E(f"{rome}.republic", "period", "Roman Republic", rome, start=-509, end=-27, tier="foundational")
E(f"{rome}.republic.early", "period", "Early Republic", f"{rome}.republic", start=-509, end=-287)
E(f"{rome}.republic.middle", "period", "Middle Republic (Punic Wars)", f"{rome}.republic", start=-287, end=-133)
E(f"{rome}.republic.late", "period", "Late Republic", f"{rome}.republic", start=-133, end=-27, tier="foundational")
E(f"{rome}.republic.late.caesar", "reign", "Julius Caesar", f"{rome}.republic.late",
  start=-49, end=-44, tier="foundational",
  summary="Dictator perpetuo; assassinated on the Ides of March, 44 BCE.")

E(f"{rome}.empire", "era", "Roman Empire", "europe.mediterranean", start=-27, end=476, tier="foundational")
E(f"{rome}.empire.julio-claudian", "period", "Julio-Claudian Dynasty", f"{rome}.empire", start=-27, end=68)
E(f"{rome}.empire.augustus", "reign", "Augustus", f"{rome}.empire.julio-claudian",
  start=-27, end=14, tier="foundational",
  aliases=["Octavian"],
  summary="First Roman emperor; founder of the Principate.")
E(f"{rome}.empire.nero", "reign", "Nero", f"{rome}.empire.julio-claudian", start=54, end=68, tier="foundational")
E(f"{rome}.empire.flavian", "period", "Flavian Dynasty", f"{rome}.empire", start=69, end=96)
E(f"{rome}.empire.nerva-antonine", "period", "Nerva–Antonine Dynasty", f"{rome}.empire", start=96, end=192, tier="foundational",
  summary="Five Good Emperors; Pax Romana at its peak.")
E(f"{rome}.empire.trajan", "reign", "Trajan", f"{rome}.empire.nerva-antonine", start=98, end=117, tier="foundational",
  summary="Extended Rome to its greatest territorial extent.")
E(f"{rome}.empire.hadrian", "reign", "Hadrian", f"{rome}.empire.nerva-antonine", start=117, end=138, tier="foundational")
E(f"{rome}.empire.marcus-aurelius", "reign", "Marcus Aurelius", f"{rome}.empire.nerva-antonine", start=161, end=180, tier="foundational")
E(f"{rome}.empire.constantine", "reign", "Constantine the Great", f"{rome}.empire",
  start=306, end=337, tier="foundational",
  summary="Legalized Christianity; founded Constantinople.")

E("europe.mediterranean.byzantine", "era", "Byzantine Empire", "europe.mediterranean",
  start=330, end=1453, tier="foundational",
  aliases=["Eastern Roman Empire"],
  summary="Roman Empire's Greek-speaking continuation, based in Constantinople.")
E("europe.mediterranean.byzantine.justinian", "reign", "Justinian I", "europe.mediterranean.byzantine",
  start=527, end=565, tier="foundational",
  summary="Reconquered much of the western Mediterranean; codified Roman law; built Hagia Sophia.")
E("europe.mediterranean.byzantine.constantine11", "reign", "Constantine XI Palaiologos",
  "europe.mediterranean.byzantine", start=1449, end=1453, tier="intermediate",
  summary="Last Byzantine emperor; killed defending Constantinople.")


# =============================================================================
# WESTERN EUROPE (medieval, early modern, modern)
# =============================================================================

we = "europe.western"
E(f"{we}.migration", "era", "Migration Period", we, start=376, end=800, tier="intermediate")
E(f"{we}.carolingian", "era", "Carolingian Empire", we, start=751, end=888, tier="foundational")
E(f"{we}.carolingian.charlemagne", "reign", "Charlemagne", f"{we}.carolingian",
  start=768, end=814, tier="foundational",
  summary="First Emperor of the Romans since antiquity; crowned by Pope Leo III in 800.")

E(f"{we}.france", "era", "France (Medieval to Modern)", we, start=987, end=None, tier="foundational")
E(f"{we}.france.capetian", "period", "Capetian France", f"{we}.france", start=987, end=1328, tier="intermediate")
E(f"{we}.france.valois", "period", "Valois France", f"{we}.france", start=1328, end=1589, tier="intermediate")
E(f"{we}.france.bourbon", "period", "Bourbon France", f"{we}.france", start=1589, end=1792, tier="foundational")
E(f"{we}.france.bourbon.louis14", "reign", "Louis XIV (Sun King)", f"{we}.france.bourbon",
  start=1643, end=1715, tier="foundational",
  summary="Longest reign of any European monarch; built Versailles.")
E(f"{we}.france.revolution", "period", "French Revolution", f"{we}.france", start=1789, end=1799, tier="foundational",
  calendar_ids=["french-republican"])
E(f"{we}.france.napoleon", "period", "Napoleonic Era", f"{we}.france", start=1799, end=1815, tier="foundational")
E(f"{we}.france.napoleon.napoleon1", "reign", "Napoleon I", f"{we}.france.napoleon",
  start=1804, end=1814, tier="foundational",
  summary="Emperor of the French; conquered most of continental Europe before defeat at Waterloo (1815).")

E(f"{we}.england", "era", "England (Medieval to Modern)", we, start=927, end=None, tier="foundational")
E(f"{we}.england.norman", "period", "Norman England", f"{we}.england", start=1066, end=1154, tier="foundational")
E(f"{we}.england.norman.william1", "reign", "William the Conqueror", f"{we}.england.norman",
  start=1066, end=1087, tier="foundational")
E(f"{we}.england.plantagenet", "period", "Plantagenet England", f"{we}.england", start=1154, end=1485, tier="intermediate")
E(f"{we}.england.tudor", "period", "Tudor England", f"{we}.england", start=1485, end=1603, tier="foundational")
E(f"{we}.england.tudor.henry8", "reign", "Henry VIII", f"{we}.england.tudor", start=1509, end=1547, tier="foundational")
E(f"{we}.england.tudor.elizabeth1", "reign", "Elizabeth I", f"{we}.england.tudor", start=1558, end=1603, tier="foundational")
E(f"{we}.england.stuart", "period", "Stuart England / Britain", f"{we}.england", start=1603, end=1714, tier="intermediate")
E(f"{we}.britain.victorian", "period", "Victorian Britain", f"{we}.england", start=1837, end=1901, tier="foundational")
E(f"{we}.britain.victorian.victoria", "reign", "Queen Victoria", f"{we}.britain.victorian", start=1837, end=1901, tier="foundational")

E(f"{we}.iberia.reconquista", "era", "Reconquista & Iberian Unification", we, start=711, end=1492, tier="intermediate")
E(f"{we}.iberia.spanish-empire", "era", "Spanish Empire", we, start=1492, end=1898, tier="foundational")
E(f"{we}.iberia.portuguese-empire", "era", "Portuguese Empire", we, start=1415, end=1999, tier="foundational")


# =============================================================================
# CENTRAL EUROPE
# =============================================================================

ce = "europe.central"
E(f"{ce}.hre", "era", "Holy Roman Empire", ce, start=800, end=1806, tier="foundational",
  summary="Multi-ethnic complex of European territories notionally under an elected emperor.")
E(f"{ce}.hre.ottonian", "period", "Ottonian Dynasty", f"{ce}.hre", start=919, end=1024)
E(f"{ce}.hre.hohenstaufen", "period", "Hohenstaufen Dynasty", f"{ce}.hre", start=1138, end=1254)
E(f"{ce}.hre.habsburg", "period", "Habsburg Era", f"{ce}.hre", start=1438, end=1806, tier="foundational")
E(f"{ce}.hre.charles5", "reign", "Charles V", f"{ce}.hre.habsburg", start=1519, end=1556, tier="foundational")
E(f"{ce}.habsburg-monarchy", "era", "Habsburg / Austria-Hungary", ce, start=1526, end=1918, tier="intermediate")
E(f"{ce}.prussia", "era", "Rise of Prussia", ce, start=1701, end=1871, tier="intermediate")
E(f"{ce}.german-empire", "era", "German Empire", ce, start=1871, end=1918, tier="foundational")
E(f"{ce}.weimar", "era", "Weimar Republic", ce, start=1918, end=1933, tier="intermediate")
E(f"{ce}.nazi-germany", "era", "Nazi Germany", ce, start=1933, end=1945, tier="foundational")
E(f"{ce}.germany-modern", "era", "Post-War Germany", ce, start=1945, end=None, tier="foundational")


# =============================================================================
# NORTHERN EUROPE
# =============================================================================

ne = "europe.northern"
E(f"{ne}.viking-age", "era", "Viking Age", ne, start=793, end=1066, tier="foundational",
  summary="Norse expansion across northern Europe and the North Atlantic.")
E(f"{ne}.viking-age.cnut", "reign", "Cnut the Great", f"{ne}.viking-age", start=1016, end=1035, tier="intermediate")
E(f"{ne}.kalmar", "era", "Kalmar Union", ne, start=1397, end=1523, tier="intermediate")
E(f"{ne}.swedish-empire", "era", "Swedish Empire", ne, start=1611, end=1721, tier="intermediate")


# =============================================================================
# EASTERN EUROPE
# =============================================================================

ee = "europe.eastern"
E(f"{ee}.kievan-rus", "era", "Kievan Rus'", ee, start=862, end=1240, tier="foundational")
E(f"{ee}.kievan-rus.vladimir", "reign", "Vladimir the Great", f"{ee}.kievan-rus", start=980, end=1015, tier="intermediate")
E(f"{ee}.moscow", "era", "Grand Duchy of Moscow", ee, start=1263, end=1547, tier="intermediate")
E(f"{ee}.tsardom", "era", "Tsardom of Russia", ee, start=1547, end=1721, tier="foundational")
E(f"{ee}.tsardom.ivan4", "reign", "Ivan IV the Terrible", f"{ee}.tsardom", start=1547, end=1584, tier="foundational")
E(f"{ee}.russian-empire", "era", "Russian Empire", ee, start=1721, end=1917, tier="foundational")
E(f"{ee}.russian-empire.peter1", "reign", "Peter the Great", f"{ee}.russian-empire", start=1682, end=1725, tier="foundational")
E(f"{ee}.russian-empire.catherine2", "reign", "Catherine the Great", f"{ee}.russian-empire", start=1762, end=1796, tier="foundational")
E(f"{ee}.soviet", "era", "Soviet Union", ee, start=1922, end=1991, tier="foundational")
E(f"{ee}.soviet.lenin", "reign", "Vladimir Lenin", f"{ee}.soviet", start=1917, end=1924, tier="foundational")
E(f"{ee}.soviet.stalin", "reign", "Joseph Stalin", f"{ee}.soviet", start=1924, end=1953, tier="foundational")
E(f"{ee}.russia-modern", "era", "Russian Federation", ee, start=1991, end=None, tier="foundational")
E(f"{ee}.plc", "era", "Polish-Lithuanian Commonwealth", ee, start=1569, end=1795, tier="intermediate")


# =============================================================================
# CENTRAL ASIA & STEPPE
# =============================================================================

ca = "central-asia"
E(f"{ca}.scythians", "era", "Scythians", f"{ca}.steppe", start=-900, end=-200, tier="intermediate")
E(f"{ca}.xiongnu", "era", "Xiongnu Empire", f"{ca}.steppe", start=-209, end=93, tier="intermediate",
  summary="First great nomadic empire on the Mongolian plateau.")
E(f"{ca}.xiongnu.modu", "reign", "Modu Chanyu", f"{ca}.xiongnu", start=-209, end=-174, tier="intermediate")
E(f"{ca}.kushan", "era", "Kushan Empire", f"{ca}.core", start=30, end=375, tier="foundational",
  summary="Yuezhi-descended empire linking China, India, and Rome via the Silk Road.",
  cross_parent_ids=["south-asia"])
E(f"{ca}.kushan.kanishka", "reign", "Kanishka the Great", f"{ca}.kushan", start=127, end=150, tier="intermediate")
E(f"{ca}.turkic-khaganate", "era", "First Turkic Khaganate", f"{ca}.steppe", start=552, end=744, tier="intermediate")
E(f"{ca}.samanid", "era", "Samanid Empire", f"{ca}.core", start=819, end=999, tier="intermediate")
E(f"{ca}.seljuk", "era", "Seljuk Empire", f"{ca}.core", start=1037, end=1194, tier="intermediate")

E("central-asia.mongol-empire", "era", "Mongol Empire", ca, start=1206, end=1368, tier="foundational",
  summary="Largest contiguous empire in world history.")
E("central-asia.mongol-empire.genghis", "reign", "Genghis Khan", "central-asia.mongol-empire",
  start=1206, end=1227, tier="foundational")
E("central-asia.mongol-empire.ogedei", "reign", "Ögedei Khan", "central-asia.mongol-empire", start=1229, end=1241)
E("central-asia.mongol-empire.mongke", "reign", "Möngke Khan", "central-asia.mongol-empire", start=1251, end=1259)
E("central-asia.mongol-empire.ilkhanate", "period", "Ilkhanate", "central-asia.mongol-empire", start=1256, end=1335,
  cross_parent_ids=[f"{ir}"])
E("central-asia.mongol-empire.chagatai", "period", "Chagatai Khanate", "central-asia.mongol-empire", start=1226, end=1687)
E("central-asia.mongol-empire.golden-horde", "period", "Golden Horde", "central-asia.mongol-empire", start=1240, end=1502,
  cross_parent_ids=["europe.eastern"])

E(f"{ca}.timurid", "era", "Timurid Empire", f"{ca}.core", start=1370, end=1507, tier="intermediate")
E(f"{ca}.timurid.timur", "reign", "Timur (Tamerlane)", f"{ca}.timurid", start=1370, end=1405, tier="foundational")


# =============================================================================
# TIBET
# =============================================================================

tb = "central-asia.tibet"
E(f"{tb}.empire", "era", "Tibetan Empire", tb, start=618, end=842, tier="intermediate")
E(f"{tb}.empire.songtsen", "reign", "Songtsen Gampo", f"{tb}.empire", start=618, end=650, tier="intermediate")
E(f"{tb}.dalai-lama", "era", "Ganden Phodrang (Dalai Lama Rule)", tb, start=1642, end=1959, tier="intermediate")


# =============================================================================
# SOUTH ASIA
# =============================================================================

sa = "south-asia"
E(f"{sa}.indus", "era", "Indus Valley Civilization", sa, start=-3300, end=-1300, tier="foundational",
  aliases=["Harappan Civilization"],
  summary="Bronze Age civilization along the Indus and Sarasvati rivers.")
E(f"{sa}.vedic", "era", "Vedic Period", sa, start=-1500, end=-500, tier="foundational")
E(f"{sa}.mahajanapadas", "era", "Mahajanapadas (Second Urbanization)", sa, start=-600, end=-345, tier="intermediate")
E(f"{sa}.maurya", "era", "Maurya Empire", sa, start=-322, end=-185, tier="foundational",
  summary="First empire to unify most of the Indian subcontinent.")
E(f"{sa}.maurya.chandragupta", "reign", "Chandragupta Maurya", f"{sa}.maurya", start=-322, end=-297, tier="foundational")
E(f"{sa}.maurya.ashoka", "reign", "Ashoka the Great", f"{sa}.maurya", start=-268, end=-232, tier="foundational",
  start_year_min=-273, start_year_max=-265,
  date_precision="approx",
  date_note="Accession dates vary by source; some traditions place him from 273 BCE.",
  summary="After the Kalinga War, embraced Buddhism and spread it via edicts and missions.")
E(f"{sa}.shunga", "era", "Shunga Empire", sa, start=-185, end=-73, tier="specialist",
  date_note="Sources place the dynasty's end at -75 (Devabhuti's overthrow attempt) or -73 (his death).")
E(f"{sa}.satavahana", "era", "Satavahana Empire", sa, start=-230, end=220, tier="intermediate",
  date_note="Founded under Simuka c. -230; imperial phase from c. -100.")
E(f"{sa}.indo-greek", "era", "Indo-Greek Kingdoms", sa, start=-200, end=10, tier="intermediate",
  cross_parent_ids=["europe.mediterranean.hellenistic"])
E(f"{sa}.gupta", "era", "Gupta Empire", sa, start=319, end=550, tier="foundational",
  aliases=["Golden Age of India"])
E(f"{sa}.gupta.chandragupta2", "reign", "Chandragupta II (Vikramaditya)", f"{sa}.gupta", start=380, end=415, tier="intermediate")
E(f"{sa}.chola", "era", "Chola Empire", sa, start=848, end=1279, tier="foundational",
  summary="Great Tamil maritime empire; reached Southeast Asia.")
E(f"{sa}.chola.rajaraja1", "reign", "Rajaraja I", f"{sa}.chola", start=985, end=1014, tier="intermediate")
E(f"{sa}.chola.rajendra1", "reign", "Rajendra I", f"{sa}.chola", start=1014, end=1044, tier="intermediate")
E(f"{sa}.delhi-sultanate", "era", "Delhi Sultanate", sa, start=1206, end=1526, tier="foundational")
E(f"{sa}.vijayanagara", "era", "Vijayanagara Empire", sa, start=1336, end=1646, tier="intermediate")
E(f"{sa}.mughal", "era", "Mughal Empire", sa, start=1526, end=1857, tier="foundational")
E(f"{sa}.mughal.babur", "reign", "Babur", f"{sa}.mughal", start=1526, end=1530, tier="foundational")
E(f"{sa}.mughal.akbar", "reign", "Akbar the Great", f"{sa}.mughal", start=1556, end=1605, tier="foundational")
E(f"{sa}.mughal.shah-jahan", "reign", "Shah Jahan", f"{sa}.mughal", start=1628, end=1658, tier="foundational",
  summary="Built the Taj Mahal.")
E(f"{sa}.mughal.aurangzeb", "reign", "Aurangzeb", f"{sa}.mughal", start=1658, end=1707, tier="foundational")
E(f"{sa}.maratha", "era", "Maratha Confederacy", sa, start=1674, end=1818, tier="intermediate")
E(f"{sa}.sikh-empire", "era", "Sikh Empire", sa, start=1799, end=1849, tier="intermediate")
E(f"{sa}.british-raj", "era", "British Raj", sa, start=1858, end=1947, tier="foundational")
E(f"{sa}.independence", "era", "Post-Independence South Asia", sa, start=1947, end=None, tier="foundational")


# =============================================================================
# SOUTHEAST ASIA
# =============================================================================

sea = "southeast-asia"
E(f"{sea}.mainland.funan", "era", "Funan", f"{sea}.mainland", start=68, end=550, tier="intermediate")
E(f"{sea}.mainland.champa", "era", "Champa", f"{sea}.mainland", start=192, end=1832, tier="intermediate")
E(f"{sea}.mainland.khmer", "era", "Khmer Empire (Angkor)", f"{sea}.mainland", start=802, end=1431, tier="foundational",
  summary="Southeast Asia's greatest classical empire. Built Angkor Wat and Angkor Thom.")
E(f"{sea}.mainland.khmer.suryavarman2", "reign", "Suryavarman II", f"{sea}.mainland.khmer", start=1113, end=1150, tier="intermediate",
  summary="Built Angkor Wat.")
E(f"{sea}.mainland.khmer.jayavarman7", "reign", "Jayavarman VII", f"{sea}.mainland.khmer", start=1181, end=1218, tier="intermediate",
  summary="Built Angkor Thom and the Bayon.")
E(f"{sea}.mainland.vietnam", "era", "Đại Việt", f"{sea}.mainland", start=939, end=1804, tier="intermediate")
E(f"{sea}.mainland.pagan", "era", "Pagan Kingdom", f"{sea}.mainland", start=849, end=1297, tier="intermediate")
E(f"{sea}.mainland.ayutthaya", "era", "Ayutthaya Kingdom", f"{sea}.mainland", start=1351, end=1767, tier="intermediate")
E(f"{sea}.mainland.rattanakosin", "era", "Rattanakosin (Chakri Dynasty)", f"{sea}.mainland", start=1782, end=None, tier="intermediate")

E(f"{sea}.maritime.srivijaya", "era", "Srivijaya", f"{sea}.maritime", start=650, end=1377, tier="intermediate",
  summary="Sumatran maritime empire that dominated the Malacca Strait.")
E(f"{sea}.maritime.majapahit", "era", "Majapahit Empire", f"{sea}.maritime", start=1293, end=1527, tier="foundational",
  summary="Javanese thalassocracy at Southeast Asia's peak of classical influence.")
E(f"{sea}.maritime.majapahit.hayam-wuruk", "reign", "Hayam Wuruk", f"{sea}.maritime.majapahit", start=1350, end=1389, tier="intermediate")
E(f"{sea}.maritime.malacca", "era", "Sultanate of Malacca", f"{sea}.maritime", start=1400, end=1511, tier="intermediate")
E(f"{sea}.maritime.dutch-eic", "era", "Dutch East Indies", f"{sea}.maritime", start=1800, end=1949, tier="intermediate")
E(f"{sea}.maritime.spanish-philippines", "era", "Spanish Philippines", f"{sea}.maritime", start=1565, end=1898, tier="intermediate")
E(f"{sea}.maritime.indonesia", "era", "Republic of Indonesia", f"{sea}.maritime", start=1945, end=None, tier="foundational")


# =============================================================================
# NORTH AFRICA
# =============================================================================

na = "africa.north"
E(f"{na}.carthage", "era", "Carthaginian Empire", na, start=-814, end=-146, tier="foundational",
  summary="Phoenician-founded maritime empire of the western Mediterranean.")
E(f"{na}.carthage.hannibal", "reign", "Hannibal Barca (general)", f"{na}.carthage", start=-221, end=-183, tier="foundational")
E(f"{na}.almoravid", "era", "Almoravid Empire", na, start=1040, end=1147, tier="intermediate")
E(f"{na}.almohad", "era", "Almohad Caliphate", na, start=1121, end=1269, tier="intermediate")
E(f"{na}.morocco-alaouite", "era", "Alaouite Morocco", na, start=1631, end=None, tier="intermediate")


# =============================================================================
# WEST AFRICA & SAHEL
# =============================================================================

wa = "africa.west"
E(f"{wa}.ghana", "era", "Ghana Empire", wa, start=300, end=1240, tier="foundational",
  aliases=["Wagadu"])
E(f"{wa}.mali", "era", "Mali Empire", wa, start=1235, end=1670, tier="foundational")
E(f"{wa}.mali.sundiata", "reign", "Sundiata Keita", f"{wa}.mali", start=1235, end=1255, tier="foundational")
E(f"{wa}.mali.mansa-musa", "reign", "Mansa Musa", f"{wa}.mali", start=1312, end=1337, tier="foundational",
  summary="Historically wealthiest ruler; famous 1324 hajj to Mecca.")
E(f"{wa}.songhai", "era", "Songhai Empire", wa, start=1464, end=1591, tier="foundational")
E(f"{wa}.songhai.sunni-ali", "reign", "Sunni Ali", f"{wa}.songhai", start=1464, end=1492, tier="intermediate")
E(f"{wa}.songhai.askia-muhammad", "reign", "Askia Muhammad I", f"{wa}.songhai", start=1493, end=1528, tier="intermediate")
E(f"{wa}.kanem-bornu", "era", "Kanem–Bornu Empire", wa, start=700, end=1900, tier="intermediate")
E(f"{wa}.benin", "era", "Benin Empire", wa, start=1180, end=1897, tier="intermediate")
E(f"{wa}.oyo", "era", "Oyo Empire", wa, start=1400, end=1836, tier="intermediate")
E(f"{wa}.ashanti", "era", "Ashanti Empire", wa, start=1670, end=1902, tier="intermediate")
E(f"{wa}.dahomey", "era", "Kingdom of Dahomey", wa, start=1600, end=1904, tier="intermediate")
E(f"{wa}.sokoto", "era", "Sokoto Caliphate", wa, start=1804, end=1903, tier="intermediate")


# =============================================================================
# EAST AFRICA & SOUTHERN AFRICA
# =============================================================================

E("africa.east.swahili", "era", "Swahili Coast City-States", "africa.east", start=900, end=1500, tier="intermediate",
  summary="Network of Indian-Ocean trading cities: Kilwa, Mombasa, Zanzibar, Sofala.")
E("africa.east.zanzibar-sultanate", "era", "Sultanate of Zanzibar", "africa.east", start=1856, end=1964, tier="intermediate")

E("africa.southern.great-zimbabwe", "era", "Great Zimbabwe", "africa.southern", start=1100, end=1450, tier="foundational")
E("africa.southern.mutapa", "era", "Mutapa Empire", "africa.southern", start=1430, end=1760, tier="intermediate")
E("africa.southern.zulu", "era", "Zulu Kingdom", "africa.southern", start=1816, end=1897, tier="foundational")
E("africa.southern.zulu.shaka", "reign", "Shaka Zulu", "africa.southern.zulu", start=1816, end=1828, tier="foundational")

E("africa.central.kongo", "era", "Kingdom of Kongo", "africa.central", start=1390, end=1914, tier="intermediate")
E("africa.central.luba", "era", "Luba Empire", "africa.central", start=1585, end=1889, tier="specialist")
E("africa.central.lunda", "era", "Lunda Empire", "africa.central", start=1665, end=1887, tier="specialist")


# =============================================================================
# AMERICAS
# =============================================================================

# North America
na_am = "americas.north"
E(f"{na_am}.mississippian", "era", "Mississippian Culture", na_am, start=800, end=1600, tier="intermediate",
  summary="Mound-building cultures across the American southeast and midwest. Cahokia was North America's largest pre-Columbian city.")
E(f"{na_am}.ancestral-puebloan", "era", "Ancestral Puebloan", na_am, start=100, end=1600, tier="intermediate")
E(f"{na_am}.haudenosaunee", "era", "Haudenosaunee (Iroquois) Confederacy", na_am, start=1450, end=None, tier="intermediate")
E(f"{na_am}.comanche", "era", "Comanche Empire", na_am, start=1750, end=1875, tier="specialist")
E(f"{na_am}.colonial", "era", "Colonial North America", na_am, start=1492, end=1783, tier="foundational")
E(f"{na_am}.usa", "era", "United States", na_am, start=1776, end=None, tier="foundational")
E(f"{na_am}.usa.civil-war", "period", "Civil War & Reconstruction", f"{na_am}.usa", start=1861, end=1877, tier="foundational")

# Mesoamerica
meso = "americas.mesoamerica"
E(f"{meso}.olmec", "era", "Olmec Civilization", meso, start=-1500, end=-400, tier="foundational",
  summary="Mother culture of Mesoamerica.")
E(f"{meso}.zapotec", "era", "Zapotec (Monte Albán)", meso, start=-500, end=800, tier="intermediate")
E(f"{meso}.teotihuacan", "era", "Teotihuacan", meso, start=-100, end=550, tier="foundational",
  summary="One of the largest cities in the ancient world.")
E(f"{meso}.maya", "era", "Maya Civilization", meso, start=-2000, end=1697, tier="foundational",
  calendar_ids=["maya-long-count"])
E(f"{meso}.maya.classic", "period", "Classic Maya", f"{meso}.maya", start=250, end=900, tier="foundational")
E(f"{meso}.maya.postclassic", "period", "Postclassic Maya", f"{meso}.maya", start=900, end=1697)
E(f"{meso}.toltec", "era", "Toltec Empire", meso, start=900, end=1150, tier="intermediate")
E(f"{meso}.purepecha", "era", "Purépecha (Tarascan) Empire", meso, start=1300, end=1530, tier="specialist")
E(f"{meso}.aztec", "era", "Aztec Empire", meso, start=1428, end=1521, tier="foundational",
  aliases=["Mexica Triple Alliance"],
  calendar_ids=["aztec-calendar"])
E(f"{meso}.aztec.itzcoatl", "reign", "Itzcoatl", f"{meso}.aztec", start=1427, end=1440, tier="intermediate")
E(f"{meso}.aztec.moctezuma1", "reign", "Moctezuma I", f"{meso}.aztec", start=1440, end=1469, tier="intermediate")
E(f"{meso}.aztec.ahuitzotl", "reign", "Ahuitzotl", f"{meso}.aztec", start=1486, end=1502, tier="intermediate")
E(f"{meso}.aztec.moctezuma2", "reign", "Moctezuma II", f"{meso}.aztec", start=1502, end=1520, tier="foundational")
E(f"{meso}.new-spain", "era", "Viceroyalty of New Spain", meso, start=1521, end=1821, tier="foundational")
E(f"{meso}.mexico", "era", "Mexico (independent)", meso, start=1821, end=None, tier="foundational")

# Andes
an = "americas.andes"
E(f"{an}.norte-chico", "era", "Norte Chico / Caral", an, start=-3000, end=-1800, tier="intermediate",
  summary="Oldest known civilization in the Americas.")
E(f"{an}.chavin", "era", "Chavín", an, start=-900, end=-200, tier="intermediate")
E(f"{an}.moche", "era", "Moche", an, start=100, end=700, tier="intermediate")
E(f"{an}.nazca", "era", "Nazca", an, start=-100, end=800, tier="intermediate")
E(f"{an}.tiwanaku", "era", "Tiwanaku", an, start=500, end=1000, tier="intermediate")
E(f"{an}.wari", "era", "Wari Empire", an, start=600, end=1000, tier="intermediate")
E(f"{an}.chimu", "era", "Chimú (Chimor)", an, start=900, end=1470, tier="intermediate")
E(f"{an}.inca", "era", "Inca Empire", an, start=1438, end=1533, tier="foundational",
  native_name="Tawantinsuyu",
  summary="Largest pre-Columbian empire; stretched ~4,000 km along the Andes.")
E(f"{an}.inca.pachacuti", "reign", "Pachacuti", f"{an}.inca", start=1438, end=1471, tier="foundational")
E(f"{an}.inca.topa", "reign", "Topa Inca Yupanqui", f"{an}.inca", start=1471, end=1493, tier="intermediate")
E(f"{an}.inca.huayna-capac", "reign", "Huayna Capac", f"{an}.inca", start=1493, end=1527, tier="intermediate")
E(f"{an}.inca.atahualpa", "reign", "Atahualpa", f"{an}.inca", start=1532, end=1533, tier="foundational")
E(f"{an}.vilcabamba", "era", "Neo-Inca State at Vilcabamba", an, start=1537, end=1572, tier="specialist")
E(f"{an}.viceroyalty-peru", "era", "Viceroyalty of Peru", an, start=1542, end=1824, tier="intermediate")

E("americas.intermediate.taino", "era", "Taíno Chiefdoms", "americas.intermediate", start=1200, end=1500, tier="intermediate")
E("americas.amazon-southern.marajoara", "era", "Marajoara Culture", "americas.amazon-southern", start=400, end=1400, tier="specialist")
E("americas.amazon-southern.mapuche", "era", "Mapuche / Araucanía", "americas.amazon-southern", start=1000, end=1883, tier="intermediate")


# =============================================================================
# OCEANIA
# =============================================================================

E("oceania.australia.aboriginal", "era", "Aboriginal Australia", "oceania.australia",
  start=-65000, end=None, date_precision="approx", tier="foundational",
  start_dating_method="luminescence", standing="consensus",
  summary="One of the longest continuous cultural traditions in human history.",
  date_note="The 65 ka arrival rests on optically stimulated luminescence at Madjedbebe, "
            "well beyond the radiocarbon range. 1788 is a colonial boundary, not an end: "
            "Aboriginal cultures and traditions continue to the present.",
  source_ids=["clarkson-2017-madjedbebe", "ahrc-aboriginal-history"])
E("oceania.australia.colonial", "era", "Colonial Australia", "oceania.australia", start=1788, end=1901, tier="foundational")
E("oceania.australia.commonwealth", "era", "Commonwealth of Australia", "oceania.australia", start=1901, end=None, tier="foundational")

E("oceania.melanesia.lapita", "era", "Lapita Culture", "oceania.melanesia", start=-1501, end=-734,
  date_precision="approx", tier="intermediate",
  summary="An ancestral Austronesian seafaring culture that spread from the Bismarck Archipelago into Remote Oceania.",
  start_dating_method="radiocarbon-calibrated", standing="majority",
  date_note="The Bismarck start is 3450-3350 cal BP and the Tonga/Samoa end is 2703-2683 cal BP. Marine-shell reservoir corrections are central to this chronology.",
  alternatives=[{"label": "Earlier shell-inclusive start", "standing": "minority", "start_year": -1601,
                 "end_year": -1501, "dating_method": "radiocarbon-calibrated",
                 "note": "Shell-inclusive dates can extend the start to about 3550 cal BP after reservoir correction.",
                 "source_ids": ["specht-lapita"]}],
  source_ids=["specht-lapita"])
E("oceania.melanesia.fijian-chiefdoms", "era", "Fijian Chiefdoms", "oceania.melanesia", start=500, end=1874, tier="specialist")

E("oceania.micronesia.saudeleur", "era", "Saudeleur Dynasty (Nan Madol)", "oceania.micronesia",
  start=1100, end=1628, tier="specialist",
  summary="Built the megalithic city of Nan Madol on Pohnpei.")
E("oceania.micronesia.yap", "era", "Yapese Empire (Sawei)", "oceania.micronesia", start=1400, end=1700, tier="specialist")

E("oceania.polynesia.settlement", "era", "Polynesian Voyaging & Settlement", "oceania.polynesia",
  start=1025, end=1290, tier="foundational",
  summary="A rapid expansion from West to East Polynesia that reached remote islands, including Aotearoa, in the late thirteenth century.",
  start_dating_method="radiocarbon-calibrated", standing="consensus",
  date_note="A review of 1,434 radiocarbon dates supports 1025-1120 CE for East Polynesian settlement and 1230-1280 CE for Aotearoa, with modelled Rapa Nui about 1200 CE.",
  alternatives=[{"label": "Long chronology", "standing": "minority", "start_year": 300,
                 "end_year": 950, "dating_method": "radiocarbon-calibrated",
                 "note": "Earlier shell-inclusive chronologies placed the eastern expansion as early as 300 CE, but are superseded by short-lived samples.",
                 "source_ids": ["wilmshurst-2011-polynesia"]}],
  source_ids=["wilmshurst-2011-polynesia"])
E("oceania.polynesia.tui-tonga", "era", "Tuʻi Tonga Empire", "oceania.polynesia", start=950, end=1865, tier="intermediate")
E("oceania.polynesia.hawaii", "era", "Kingdom of Hawaii", "oceania.polynesia", start=1795, end=1898, tier="foundational")
E("oceania.polynesia.hawaii.kamehameha1", "reign", "Kamehameha I", "oceania.polynesia.hawaii", start=1795, end=1819, tier="foundational")
E("oceania.polynesia.hawaii.liliuokalani", "reign", "Queen Liliʻuokalani", "oceania.polynesia.hawaii", start=1891, end=1893, tier="intermediate")
E("oceania.polynesia.tonga", "era", "Kingdom of Tonga", "oceania.polynesia", start=1845, end=None, tier="intermediate")
E("oceania.polynesia.aotearoa", "era", "Māori Aotearoa", "oceania.polynesia", start=1250, end=1840, tier="foundational")
E("oceania.polynesia.new-zealand", "era", "New Zealand (post-Waitangi)", "oceania.polynesia", start=1840, end=None, tier="foundational")


# =============================================================================
# CROSS-REGIONAL EVENTS
# =============================================================================

E("global.bronze-age.collapse", "event", "Late Bronze Age Collapse", "global.bronze-age",
  start=-1200, end=-1150, tier="intermediate",
  start_year_min=-1220, start_year_max=-1180,
  end_year_min=-1150, end_year_max=-1100,
  start_precision="approx", end_precision="approx",
  aliases=["Bronze Age Collapse"],
  summary="Systemic collapse of Mediterranean and Near Eastern civilizations c. 1200 BCE.",
  # The Collapse straddles the boundary it defines: it ends the Bronze Age
  # and opens the Iron Age, so it cannot sit wholly inside either.
  allow_outside_parent_dates=True)
E("global.classical-antiquity.axial-age", "era", "Axial Age", "global.classical-antiquity", start=-800, end=-200, tier="intermediate",
  summary="Concurrent religious and philosophical revolutions: Buddha, Confucius, Zoroaster, Hebrew prophets, Greek philosophers.")
E("global.middle-ages.black-death", "event", "Black Death", "global.middle-ages", start=1346, end=1353, tier="foundational",
  summary="Bubonic plague pandemic that killed 30–60% of Europe's population and swept Asia and North Africa.")
E("global.multi-regional.age-of-sail", "era", "Age of Exploration / Age of Sail", "cross-regional", start=1418, end=1815, tier="foundational")
E("global.multi-regional.columbus", "event", "Columbus reaches the Americas", "cross-regional", start=1492, end=1492, tier="foundational")
E("global.short-20c.ww1", "event", "World War I", "global.short-20c", start=1914, end=1918, tier="foundational")
E("global.short-20c.ww2", "event", "World War II", "global.short-20c", start=1939, end=1945, tier="foundational")
E("global.short-20c.cold-war", "era", "Cold War", "global.short-20c", start=1947, end=1991, tier="foundational")


# =============================================================================
# PHASE 0: Missing global eras, movements, and events
# =============================================================================

# --- Major early-modern / modern European movements ---
E("europe.renaissance", "era", "The Renaissance", "europe",
  start=1300, end=1600, tier="foundational",
  start_precision="approx", end_precision="approx",
  aliases=["European Renaissance", "Italian Renaissance"],
  summary="European cultural, artistic, and intellectual rebirth beginning in Italy and radiating outward; recovery of Greco-Roman texts; humanism.")
E("europe.renaissance.italian", "period", "Italian Renaissance", "europe.renaissance",
  start=1300, end=1600, tier="foundational",
  summary="Florentine, Venetian, and Roman flowering; Petrarch, Dante, Leonardo, Michelangelo, Raphael.")
E("europe.renaissance.northern", "period", "Northern Renaissance", "europe.renaissance",
  start=1450, end=1600, tier="intermediate",
  summary="Renaissance north of the Alps: Erasmus, Dürer, van Eyck, printing revolution.")

E("europe.reformation", "era", "The Reformation", "europe",
  start=1517, end=1648, tier="foundational",
  aliases=["Protestant Reformation"],
  summary="Religious and political upheaval that fractured Latin Christendom, triggered by Luther's Ninety-Five Theses and ended by the Peace of Westphalia.")
E("europe.reformation.luther", "reign", "Martin Luther (theologian)", "europe.reformation",
  start=1517, end=1546, tier="foundational",
  summary="German monk whose Ninety-Five Theses (1517) launched the Protestant Reformation.")
E("europe.reformation.thirty-years-war", "event", "Thirty Years' War", "europe.reformation",
  start=1618, end=1648, tier="foundational",
  summary="Devastating pan-European religious and political war ending with the Peace of Westphalia.")

E("europe.scientific-revolution", "era", "Scientific Revolution", "europe",
  start=1543, end=1700, tier="foundational",
  summary="Emergence of modern science: Copernicus, Galileo, Kepler, Newton. Overturned Aristotelian and Ptolemaic worldviews.")

E("europe.enlightenment", "era", "The Enlightenment", "europe",
  start=1680, end=1815, tier="foundational",
  aliases=["Age of Reason", "Age of Enlightenment"],
  start_precision="approx", end_precision="approx",
  summary="Intellectual movement emphasizing reason, individual liberty, and skepticism of tradition; foundation of modern democratic thought.")

# --- Industrial Revolution and 19th-century movements ---
E("global.industrial-revolution", "era", "Industrial Revolution", "global",
  start=1760, end=1840, tier="foundational",
  start_precision="approx", end_precision="approx",
  aliases=["First Industrial Revolution"],
  summary="Transition from agrarian and craft economies to mechanized industry, beginning in Britain and spreading globally. Steam power, textiles, railways.")
E("global.second-industrial-revolution", "era", "Second Industrial Revolution", "global",
  start=1870, end=1914, tier="intermediate",
  aliases=["Technological Revolution"],
  summary="Steel, electricity, chemicals, internal combustion, mass production; the age of Edison, Tesla, Ford.")

E("global.multi-regional.scramble-for-africa", "era", "Scramble for Africa", "cross-regional",
  start=1881, end=1914, tier="foundational",
  aliases=["Partition of Africa", "Colonization of Africa"],
  summary="European colonial partition of Africa, formalized by the Berlin Conference (1884–85).")
E("global.multi-regional.berlin-conference", "event", "Berlin Conference", "global.multi-regional.scramble-for-africa",
  start=1884, end=1885, tier="intermediate",
  summary="European powers agreed rules for the partition of Africa; no African representatives present.")

E("global.multi-regional.decolonization", "era", "Decolonization", "cross-regional",
  start=1945, end=1997, tier="foundational",
  summary="Dissolution of European colonial empires after WWII; independence for most of Africa, Asia, and the Pacific.")

# --- Napoleonic Wars and specific 19th-century events ---
E("europe.western.france.napoleon.napoleonic-wars", "era", "Napoleonic Wars", "europe.western.france.napoleon",
  start=1803, end=1815, tier="foundational",
  summary="Series of conflicts pitting Napoleon's France against shifting European coalitions. Reshaped the continent.")
E("europe.western.france.napoleon.austerlitz", "event", "Battle of Austerlitz", "europe.western.france.napoleon",
  start=1805, end=1805, tier="intermediate",
  summary="Napoleon's masterpiece; defeat of the Third Coalition (Austria and Russia).")
E("europe.western.france.napoleon.trafalgar", "event", "Battle of Trafalgar", "europe.western.france.napoleon",
  start=1805, end=1805, tier="intermediate",
  summary="Nelson's decisive naval victory over the Franco-Spanish fleet; secured British naval supremacy for a century.")
E("europe.western.france.napoleon.waterloo", "event", "Battle of Waterloo", "europe.western.france.napoleon",
  start=1815, end=1815, tier="foundational",
  summary="Napoleon's final defeat at the hands of Wellington and Blücher; end of the Napoleonic era.")

# --- Late Roman Republic events ---
E(f"{rome}.republic.late.caesar-assassination", "event", "Assassination of Julius Caesar", f"{rome}.republic.late",
  start=-44, end=-44, tier="foundational",
  summary="Caesar assassinated on the Ides of March, 44 BCE, by a conspiracy of senators.")
E(f"{rome}.republic.late.actium", "event", "Battle of Actium", f"{rome}.republic.late",
  start=-31, end=-31, tier="foundational",
  summary="Octavian's naval victory over Antony and Cleopatra; effective end of the Republic.")

# --- Modern conflicts and Cold War events ---
E("global.short-20c.korean-war", "event", "Korean War", "global.short-20c.cold-war",
  start=1950, end=1953, tier="foundational",
  summary="First major hot conflict of the Cold War; UN-backed South Korea vs. Chinese/Soviet-backed North.")
E("global.short-20c.vietnam-war", "event", "Vietnam War", "global.short-20c.cold-war",
  start=1955, end=1975, tier="foundational",
  aliases=["Second Indochina War", "American War in Vietnam"],
  summary="Prolonged conflict ending with North Vietnamese victory and reunification.")
E("global.short-20c.cuban-missile-crisis", "event", "Cuban Missile Crisis", "global.short-20c.cold-war",
  start=1962, end=1962, tier="foundational",
  summary="Thirteen-day nuclear standoff between the US and USSR over Soviet missiles in Cuba — the closest the Cold War came to nuclear war.")
E("global.short-20c.moon-landing", "event", "Apollo 11 Moon Landing", "global.short-20c.cold-war",
  start=1969, end=1969, tier="foundational",
  summary="Neil Armstrong and Buzz Aldrin became the first humans to walk on the Moon (20 July 1969).")
E("global.short-20c.berlin-wall-fall", "event", "Fall of the Berlin Wall", "global.short-20c.cold-war",
  start=1989, end=1989, tier="foundational",
  summary="Symbolic end of the Cold War division of Europe; East Germans crossed freely on 9 November 1989.")
E("global.short-20c.soviet-dissolution", "event", "Dissolution of the Soviet Union", "global.short-20c.cold-war",
  start=1991, end=1991, tier="foundational",
  summary="Formal end of the USSR on 26 December 1991; 15 successor republics.")

# --- Post-Cold War events ---
E("global.contemporary.september-11", "event", "September 11 Attacks", "global.contemporary",
  start=2001, end=2001, tier="foundational",
  aliases=["9/11", "9-11"],
  summary="Coordinated al-Qaeda attacks on the United States; triggered the War on Terror.")
E("global.contemporary.war-on-terror", "era", "War on Terror", "global.contemporary",
  start=2001, end=2021, tier="foundational",
  aliases=["Global War on Terrorism"],
  summary="US-led military campaign following 9/11; wars in Afghanistan (2001–2021) and Iraq (2003–2011).")
E("global.contemporary.gfc", "event", "Global Financial Crisis", "global.contemporary",
  start=2007, end=2009, tier="foundational",
  aliases=["Great Recession", "2008 Financial Crisis"],
  summary="Worldwide financial crisis triggered by the US subprime mortgage collapse; deepest downturn since the Great Depression.")
E("global.contemporary.covid", "event", "COVID-19 Pandemic", "global.contemporary",
  start=2020, end=2023, tier="foundational",
  aliases=["COVID pandemic", "Coronavirus pandemic"],
  end_precision="approx",
  summary="Global pandemic caused by SARS-CoV-2; declared over as an emergency by the WHO in May 2023.")

# --- Bronze Age subdivisions and neolithic events ---
E("global.neolithic.agricultural-revolution", "event", "Neolithic (Agricultural) Revolution", "global.neolithic",
  start=-10000, end=-4500, tier="foundational",
  start_dating_method="radiocarbon-calibrated", standing="consensus",
  start_precision="approx", end_precision="approx",
  aliases=["Neolithic Revolution", "First Agricultural Revolution"],
  summary="Independent transitions to farming and animal domestication in the Fertile Crescent, China, Mesoamerica, and elsewhere.")
E("global.bronze-age.early", "period", "Early Bronze Age", "global.bronze-age",
  start=-3300, end=-2100, tier="intermediate")
E("global.bronze-age.middle", "period", "Middle Bronze Age", "global.bronze-age",
  start=-2100, end=-1550, tier="intermediate")
E("global.bronze-age.late", "period", "Late Bronze Age", "global.bronze-age",
  start=-1550, end=-1200, tier="intermediate")


# =============================================================================
# EXTENSIONS: Roman + Byzantine emperors, Chinese emperors, Egyptian pharaohs
# =============================================================================

from extensions_rome_china_egypt import extend as _extend
_extend(E, rome, cn, egypt)

from extensions_south_asia import extend as _extend_south_asia
_extend_south_asia(E, sa)

from extensions_prehistory import extend as _extend_prehistory
_extend_prehistory(E, "global")

from extensions_regional_prehistory import extend as _extend_regional_prehistory
_extend_regional_prehistory(E, "global")

from extensions_africa import extend as _extend_africa
_extend_africa(E, "global")

# Reframes global.neolithic.agricultural-revolution in place and gives it its
# centres, so it must run before the ages spine derives spans from the corpus.
from extensions_neolithic import extend as _extend_neolithic
_extend_neolithic(E, entities)

from extensions_europe import extend as _extend_europe
_extend_europe(E, entities)

# Reads the finished Americas corpus to enrich White Sands in place, so it runs
# after the prehistory modules that created it.
from extensions_americas import extend as _extend_americas
_extend_americas(E, entities)

from extensions_central_asia import extend as _extend_central_asia
_extend_central_asia(E, entities)

# Reads the finished corpus to enrich Ban Chiang and Lapita in place.
from extensions_seasia_oceania import extend as _extend_seasia_oceania
from extensions_indus import extend as _extend_indus
from extensions_east_asia import extend as _extend_east_asia
from extensions_west_asia import extend as _extend_west_asia
from extensions_arabia import extend as _extend_arabia
from extensions_egypt import extend as _extend_egypt
from citations_mediterranean import extend as _cite_mediterranean
from extensions_mesolithic import extend as _extend_mesolithic
from extensions_empires import extend as _extend_empires
from extensions_naming import extend as _extend_naming
from extensions_americas_civ import extend as _extend_americas_civ
from naming_formal_historical import extend as _naming_formal_historical
from naming_formal_historical_2 import extend as _naming_formal_historical_2
from naming_formal_historical_3 import extend as _naming_formal_historical_3
from naming_formal_historical_4 import extend as _naming_formal_historical_4
from extensions_gaps import GAP_SOURCES  # noqa: E402
from multiregional_definition import extend as _cross_regional_definition
from extensions_gaps import extend as _extend_gaps
from regions_multiregional import extend as _regions_multiregional
from romanisation_chinese import extend as _romanisation_chinese
from extensions_song_era_states import extend as _song_era_states, fix_tiers as _fix_china_tiers
from extensions_sea_mainland import extend as _sea_mainland
from extensions_sea_maritime import extend as _sea_maritime
from extensions_central_asia_medieval import extend as _central_asia_medieval
from extensions_iran_islamic import extend as _iran_islamic
from citations_cross_region import extend as _cross_region_citations
from extensions_phoenicia import extend as _phoenicia
from extensions_vedic import extend as _vedic
from rival_claims import extend as _rival_claims
from tier_promotions import extend as _tier_promotions
from misconception_migration import extend as _misconception_migration
from container_summaries import extend as _container_summaries
from promoted_sourcing import extend as _promoted_sourcing
from china_legendary import extend as _china_legendary
import reigns_from_research
from reigns_from_research import extend as _reigns_from_research
from upgrade_sources import extend as _upgrade_sources
from co_rulers import extend as _co_rulers
from fix_rome_parent import extend as _fix_rome_parent
from migrate_dating import extend as _migrate_dating
from normalize_ids import extend as _normalize_ids, rewrite_refs as _rewrite_refs
from name_repair import extend as _name_repair
from derive_links import extend as _derive_links
from historicity import extend as _historicity
from search_phrases import extend as _search_phrases
from polity_split import extend as _polity_split
from contemporary_placement import extend as _contemporary_placement
from review_triage import extend as _review_triage, extend_dating as _review_dating
from drop_derived_bounds import extend as _drop_derived_bounds
from new_kinds import extend as _new_kinds
from author_cities import extend as _author_cities
_extend_seasia_oceania(E, entities)
_extend_indus(E, entities)
_extend_east_asia(E, entities)
_extend_west_asia(E, entities)
_extend_arabia(E, entities)
_extend_egypt(E, entities)
# Enrichment, not authoring: attaches sources to entities that predate the rule.
_cite_mediterranean(E, entities)
_extend_mesolithic(E, entities)
_extend_empires(E, entities)
_extend_naming(E, entities)
_extend_americas_civ(E, entities)
_naming_formal_historical(E, entities)
_naming_formal_historical_2(E, entities)
_naming_formal_historical_3(E, entities)
_naming_formal_historical_4(E, entities)
_cross_regional_definition(E, entities)
_extend_gaps(E, entities)
_sea_mainland(E, entities)
_sea_maritime(E, entities)
_central_asia_medieval(E, entities)
_iran_islamic(E, entities)
_phoenicia(E, entities)
_vedic(E, entities)
_rival_claims(E, entities)
_misconception_migration(E, entities)
_tier_promotions(E, entities)
_container_summaries(E, entities)
_promoted_sourcing(E, entities)
_cross_region_citations(E, entities)
_song_era_states(E, entities)
_fix_china_tiers(E, entities)
# After _song_era_states (which authors the Xia) and _fix_china_tiers, so the Xia
# exists to reparent Erlitou onto and the rebuilt tier is not overwritten.
_china_legendary(E, entities)
_reigns_from_research(E, entities)
_upgrade_sources(E, entities)
_co_rulers(E, entities)
_fix_rome_parent(E, entities)
_romanisation_chinese(E, entities)
_regions_multiregional(E, entities)

# Marks received conventions across the corpus, so it runs after every module
# that could author one.
from received_conventions import extend as _extend_received
_extend_received(E, entities)

# Must run last: it reads the finished corpus to derive its spans and to attach
# cross-parent links to entities other modules created.
from extensions_ages import extend as _extend_ages
_extend_ages(E, entities)

from prehistory_crosslinks import extend as _extend_crosslinks
_extend_crosslinks(E, entities)


# =============================================================================
# POST-PROCESS: flag legitimate parent/child date overlaps
# =============================================================================
# These are entities whose start/end dates fall outside their parent's range for
# real historical reasons — rulers who held office before founding the state
# they later ruled, nengō spanning era boundaries, restored rulers with two
# tenures, etc. Marking them here silences the containment warning.

_legitimate_outside_parent = {
    # Nengō that span Japanese historical-era boundaries
    "east-asia.japan.nara.wado":            "Nengō began 708 in Asuka, continued into Nara (710).",
    "east-asia.japan.nara.enryaku":         "Nengō 782-806 spans the Nara-Heian boundary (794).",
    "east-asia.japan.kamakura.genko-kamakura2": "Nengō 1331-1334 spans the Kamakura-Kenmu boundary (1333).",
    "east-asia.japan.muromachi.shokei":     "Northern-Court nengō predating the formal Muromachi start (1336).",
    "east-asia.japan.azuchi-momoyama.keicho": "Nengō 1596-1615 spans Azuchi-Momoyama into early Edo.",
    # Warlords in reigns before their formal era began
    "east-asia.japan.azuchi-momoyama.nobunaga": "Oda Nobunaga's rule began 1568, before the formal Azuchi-Momoyama era start (1573).",
    "east-asia.china.zhou.eastern.warring-states": "Warring States is a historiographic period that outlasted the nominal Eastern Zhou.",
    "east-asia.china.yuan.kublai":          "Kublai was Great Khan from 1260; founded the Yuan dynasty in 1271.",
    "west-asia.iran.achaemenid.cyrus2":     "Cyrus II ruled Persia from 559, becoming founder of the Achaemenid empire in 550.",
    "europe.eastern.russian-empire.peter1": "Peter I reigned as tsar from 1682; declared himself emperor in 1721, founding the Russian Empire.",
    "europe.eastern.soviet.lenin":          "Lenin led the Russian SFSR from 1917; the USSR was formally created in 1922.",
    "central-asia.mongol-empire.chagatai":  "Chagatai Khanate long outlived the unified Mongol Empire; a successor state.",
    "central-asia.mongol-empire.golden-horde": "Golden Horde outlived the unified Mongol Empire; a successor state.",
    "americas.mesoamerica.aztec.itzcoatl":  "Itzcoatl began his reign in 1427; the Triple Alliance was founded in 1428.",
    "europe.mediterranean.rome.empire.galba": "Galba was proclaimed emperor in 68, before the Year of the Four Emperors year (69).",
    "europe.mediterranean.rome.empire.pescennius-niger": "Rival claimant into 194, after the nominal Year of Five Emperors year (193).",
    "europe.mediterranean.rome.empire.clodius-albinus": "Rival claimant into 197, well after the nominal 193 year.",
    "europe.mediterranean.rome.empire.carinus": "Carinus continued reigning into 285, one year past Diocletian's accession that starts the Dominate.",
    "europe.mediterranean.rome.empire.jovian": "Jovian's reign spilled slightly into 364, technically after Constantinian dynasty end.",
    "europe.mediterranean.rome.empire.valentinian-iii": "Valentinian III was a Theodosian emperor placed under the Western Collapse bucket for chronological grouping.",
    # South Asia independence-era leaders active before formal 1947 independence
    "south-asia.independence.gandhi": "Gandhi's political leadership began in 1915, three decades before Independence; his date range starts before the parent's 1947 for historiographic reasons.",
    "south-asia.independence.jinnah": "Jinnah's political leadership began in 1913; his date range starts before the parent's 1947 for historiographic reasons.",
    "south-asia.independence.ambedkar": "Ambedkar's political leadership began in 1927; his date range starts before the parent's 1947 for historiographic reasons.",
    "south-asia.independence.subhas-bose": "Bose's INA leadership predated 1947 Independence.",
    "south-asia.british-raj.mountbatten": "Mountbatten continued as Governor-General of independent India into 1948, after the formal end of the Raj.",
}

for _eid, _note in _legitimate_outside_parent.items():
    for _e in entities:
        if _e["id"] == _eid:
            _e["allow_outside_parent_dates"] = True
            if not _e.get("date_note"):
                _e["date_note"] = _note
            break


# =============================================================================
# POST-PROCESS: backfill summaries on foundational-tier entities
# =============================================================================
# These are entities the validator flags as foundational-without-summary. Adding
# one-line summaries here keeps the seed data hand-editable while ensuring
# every high-visibility node has help text.

_backfill_summaries = {
    # Global periodization frames
    "global.paleolithic": "Old Stone Age. Human evolution and hunter-gatherer societies before the invention of agriculture.",
    "global.bronze-age": "Age of bronze metallurgy, ending in the systemic Late Bronze Age Collapse c. 1200 BCE.",
    "global.iron-age": "Widespread adoption of iron for weapons and tools; the age of classical antiquity's origins.",
    "global.classical-antiquity": "The Greek and Roman world, roughly from Homer to the fall of Western Rome.",
    "global.middle-ages": "Between the fall of Rome and the Renaissance; medieval Christendom, the Islamic Golden Age, Tang-Song China, and Kamakura Japan.",
    "global.early-modern": "Age of exploration, colonial empires, and gunpowder; from ~1500 to the eve of the Napoleonic Wars.",
    "global.long-19c": "Historians' 'long nineteenth century' from the French Revolution to World War I.",
    "global.short-20c": "Hobsbawm's 'short twentieth century' from WWI to the collapse of the Soviet Union.",
    "global.contemporary": "Post-Cold-War world: globalization, digital revolution, climate crisis.",
    # Egypt / Africa
    "africa.nile.egypt.middle-kingdom": "Second great age of pharaonic Egypt after reunification under Mentuhotep II; classical Egyptian literature.",
    "africa.nile.ethiopia.haile-selassie": "Long-reigning modernizing Ethiopian emperor; deposed in the 1974 revolution.",
    # East Asia
    "east-asia.japan.muromachi": "Ashikaga shōgunate; culturally rich but politically fragmenting into the Sengoku warring-states era.",
    "east-asia.japan.azuchi-momoyama.nobunaga": "Ruthless unifier who broke the political power of Buddhist monasteries and rival warlords.",
    "east-asia.japan.azuchi-momoyama.hideyoshi": "Peasant-born unifier who completed Nobunaga's project and invaded Korea (Imjin War).",
    "east-asia.china.three-kingdoms": "Wei, Shu, and Wu — the era of the Romance of the Three Kingdoms.",
    "east-asia.china.qing.kangxi": "Longest-reigning Qing emperor; consolidated Manchu rule and expanded the empire.",
    "east-asia.china.qing.qianlong": "Cultural peak of the Qing; long reign ending in stagnation.",
    "east-asia.china.roc": "Post-imperial China, ending on the mainland with the Communist victory in 1949; continues on Taiwan.",
    "east-asia.china.prc": "Founded by Mao Zedong in 1949; the world's most populous state until 2023.",
    "east-asia.korea.joseon.sejong": "Fourth Joseon king; commissioned the Hangul script.",
    "east-asia.korea.colonial": "Japanese annexation of Korea (1910–1945); ended by WWII.",
    "east-asia.korea.divided": "Postwar division into North and South Korea after the Korean War.",
    # West Asia
    "west-asia.mesopotamia.akkadian.sargon": "Founder of the Akkadian Empire; considered the first empire-builder in world history.",
    "west-asia.mesopotamia.old-babylonian": "Amorite dynasty of Babylon; Hammurabi's law code.",
    "west-asia.mesopotamia.assyrian": "Ancient Mesopotamian empires that dominated the Near East in the Iron Age.",
    "west-asia.mesopotamia.neo-babylonian": "Chaldean dynasty that overthrew Assyria; Nebuchadnezzar destroyed Jerusalem in 587 BCE.",
    "west-asia.mesopotamia.israel-judah.david": "Traditional second king of Israel; united the northern and southern kingdoms.",
    "west-asia.mesopotamia.israel-judah.solomon": "Traditional builder of the First Temple in Jerusalem.",
    "west-asia.iran.seleucid": "Hellenistic successor state to Alexander's eastern conquests; the biggest single Diadochi kingdom.",
    "west-asia.iran.parthian": "Iranian empire that ruled Persia and Mesopotamia for four centuries; Rome's chief eastern rival.",
    "west-asia.iran.pahlavi": "Last royal dynasty of Iran; overthrown by the 1979 Islamic Revolution.",
    "west-asia.iran.islamic-republic": "Theocratic state established by Ayatollah Khomeini after the 1979 revolution.",
    "west-asia.arabia.rise-islam": "Muhammad's prophetic career and the birth of Islam.",
    "west-asia.arabia.rise-islam.muhammad": "Founder of Islam; united most of Arabia under his rule by 632.",
    "global.multi-regional.abbasid.harun": "Fifth Abbasid caliph; his court is the setting of many One Thousand and One Nights tales.",
    "global.multi-regional.ottoman.suleiman": "Longest-reigning Ottoman sultan; peak of Ottoman power and cultural achievement.",
    # Europe (Mediterranean)
    "europe.mediterranean.greece": "Cradle of Western philosophy, drama, historiography, and democracy.",
    "europe.mediterranean.greece.mycenaean": "Late Bronze Age Greek civilization; the world of Homer's epics.",
    "europe.mediterranean.greece.archaic": "Formative period of the polis, colonization, and archaic art.",
    "europe.mediterranean.greece.classical.pericles": "Athenian statesman who led the city through its cultural Golden Age.",
    "europe.mediterranean.macedon": "Northern Greek kingdom that under Philip II and Alexander conquered the classical world.",
    "europe.mediterranean.macedon.philip2": "Reorganized the Macedonian army and unified Greece under Macedonian hegemony.",
    "europe.mediterranean.hellenistic": "Age of Greek-influenced kingdoms from Alexander's death to Actium.",
    "europe.mediterranean.rome": "From the legendary founding to the fall of the Western Empire; the political and cultural core of the ancient Mediterranean.",
    "europe.mediterranean.rome.republic": "Non-monarchical Rome governed by the Senate and elected magistrates.",
    "europe.mediterranean.rome.republic.late": "Era of Marius, Sulla, Pompey, Caesar, and Octavian; ended by civil wars that produced the Empire.",
    "europe.mediterranean.rome.empire": "Monarchical Roman state from Augustus's Principate to the deposition of Romulus Augustulus.",
    "europe.mediterranean.rome.empire.nero": "Fifth Roman emperor; committed suicide after being declared a public enemy.",
    "europe.mediterranean.rome.empire.hadrian": "Consolidator emperor who built Hadrian's Wall in Britain.",
    "europe.mediterranean.rome.empire.marcus-aurelius": "Philosopher-emperor and author of the Meditations.",
    # Europe (Western)
    "europe.western.carolingian": "Frankish empire founded by Charlemagne; briefly reunified western Europe.",
    "europe.western.france": "Kingdom (later republic) of France from Hugh Capet to the present.",
    "europe.western.france.bourbon": "Longest-ruling French royal house; ended by the French Revolution.",
    "europe.western.france.revolution": "Overthrew the Bourbon monarchy and reshaped modern politics.",
    "europe.western.france.napoleon": "Napoleon Bonaparte's dominance of Europe from consul to emperor and exile.",
    "europe.western.england": "Kingdom of England (later Great Britain, then United Kingdom).",
    "europe.western.england.norman": "Norman-French dynasty founded by William the Conqueror.",
    "europe.western.england.norman.william1": "Conquered England at Hastings (1066).",
    "europe.western.england.tudor": "House that ruled England 1485–1603 including Henry VIII and Elizabeth I.",
    "europe.western.england.tudor.henry8": "Broke with Rome to form the Church of England; had six wives.",
    "europe.western.england.tudor.elizabeth1": "Presided over England's Elizabethan Golden Age of drama and exploration.",
    "europe.western.britain.victorian": "Long reign of Queen Victoria; peak of the British Empire.",
    "europe.western.britain.victorian.victoria": "Symbol of the age that bears her name; her descendants sit on many European thrones.",
    "europe.western.iberia.spanish-empire": "First truly global empire; the leading colonial power of the 16th century.",
    "europe.western.iberia.portuguese-empire": "Pioneered European maritime exploration; earliest and longest-lived colonial empire.",
    "europe.central.hre.habsburg": "Habsburg dynasty held the Holy Roman Emperor title almost continuously from 1438 to 1806.",
    "europe.central.hre.charles5": "Ruled an empire on which the sun never set: Spain, the HRE, Naples, the Netherlands, and Spanish America.",
    "europe.central.german-empire": "Unified German state 1871–1918 under the Hohenzollerns; collapsed at the end of WWI.",
    "europe.central.nazi-germany": "Totalitarian state under Hitler; started WWII in Europe and perpetrated the Holocaust.",
    "europe.central.germany-modern": "Federal Republic of Germany from 1949 (reunified 1990).",
    "europe.eastern.kievan-rus": "Medieval East Slavic federation; ancestor state of modern Russia, Ukraine, and Belarus.",
    "europe.eastern.tsardom": "Russian state from Ivan IV's assumption of the tsar title to Peter I's imperial declaration.",
    "europe.eastern.tsardom.ivan4": "Ivan the Terrible; expanded Russia and established the Oprichnina reign of terror.",
    "europe.eastern.russian-empire": "Multi-national empire from Peter the Great to the abdication of Nicholas II.",
    "europe.eastern.russian-empire.peter1": "Westernizing tsar who founded St. Petersburg and made Russia a major European power.",
    "europe.eastern.russian-empire.catherine2": "German-born empress who expanded Russia to the Black Sea and patronized the arts.",
    "europe.eastern.soviet": "Union of Soviet Socialist Republics (USSR); communist superpower 1922–1991.",
    "europe.eastern.soviet.lenin": "Bolshevik leader; founded the Soviet state after the October Revolution.",
    "europe.eastern.soviet.stalin": "Longtime dictator; industrialized the USSR at enormous human cost and led it through WWII.",
    "europe.eastern.russia-modern": "Russian Federation from 1991 to the present.",
    "central-asia.mongol-empire.genghis": "Genghis Khan; founder of the largest contiguous land empire in world history.",
    "central-asia.timurid.timur": "Tamerlane; last of the great steppe conquerors, sacked Delhi and Damascus.",
    "south-asia.vedic": "Age of the Vedas; formation of Hindu religious tradition and Sanskrit literature.",
    "south-asia.maurya.chandragupta": "Founder of the Maurya Empire; unified most of the Indian subcontinent.",
    "south-asia.gupta": "Classical Indian empire often called the 'Golden Age of India'.",
    "south-asia.delhi-sultanate": "Muslim sultanates ruling northern India from Delhi (1206–1526).",
    "south-asia.mughal": "Turco-Mongol Muslim empire that ruled most of South Asia at its peak.",
    "south-asia.mughal.babur": "Founder of the Mughal Empire; descendant of both Timur and Genghis Khan.",
    "south-asia.mughal.akbar": "Great Mughal emperor; expanded the empire and pursued religious tolerance.",
    "south-asia.mughal.aurangzeb": "Last of the six great Mughals; his overexpansion set the stage for imperial decline.",
    "south-asia.british-raj": "Direct British Crown rule of India, 1858–1947.",
    "south-asia.independence": "Post-1947 independent states of the subcontinent.",
    "southeast-asia.maritime.indonesia": "Southeast Asian archipelagic republic; world's fourth-most-populous country.",
    "africa.north.carthage.hannibal": "Carthaginian general; crossed the Alps with elephants and terrorized Roman Italy for 15 years.",
    "africa.west.ghana": "Sahelian trading empire, unrelated to the modern nation of Ghana.",
    "africa.west.mali": "West African empire; the world's largest gold source in the 14th century.",
    "africa.west.mali.sundiata": "Founder of the Mali Empire; hero of the Epic of Sundiata.",
    "africa.west.songhai": "Largest state in West African history; overthrown by a Moroccan invasion in 1591.",
    "africa.southern.great-zimbabwe": "Shona kingdom in southern Africa; famed for its stone-built capital.",
    "africa.southern.zulu": "South African kingdom that fiercely resisted British colonization.",
    "africa.southern.zulu.shaka": "Founder of the Zulu military kingdom; revolutionized African warfare.",
    "americas.north.colonial": "European colonial presence in North America from Columbus to the American Revolution.",
    "americas.north.usa": "United States of America from independence (1776) to the present.",
    "americas.north.usa.civil-war": "Union defeated the Confederacy; ended slavery and reshaped the American republic.",
    "americas.mesoamerica.maya": "Long-lived Mesoamerican civilization known for writing, mathematics, and monumental architecture.",
    "americas.mesoamerica.maya.classic": "Classic Maya florescence of city-states and hieroglyphic writing.",
    "americas.mesoamerica.aztec": "Mexica Triple Alliance dominating central Mexico until Spanish conquest.",
    "americas.mesoamerica.aztec.moctezuma2": "Aztec emperor at the time of the Spanish conquest.",
    "americas.mesoamerica.new-spain": "Spanish colonial viceroyalty covering Mexico, Central America, and the Caribbean.",
    "americas.mesoamerica.mexico": "Independent Mexico from 1821 to the present.",
    "americas.andes.inca.pachacuti": "Ninth Sapa Inca; transformed a small Andean state into an empire.",
    "americas.andes.inca.atahualpa": "Last independent Sapa Inca; captured and executed by Pizarro.",
    "oceania.australia.colonial": "British colonial period in Australia, 1788–1901.",
    "oceania.australia.commonwealth": "Federated Commonwealth of Australia from 1901.",
    "oceania.polynesia.hawaii": "Unified Hawaiian Kingdom under the Kamehameha dynasty until US annexation in 1898.",
    "oceania.polynesia.aotearoa": "Māori settlement and society of New Zealand before 1840.",
    "oceania.polynesia.new-zealand": "Post-Treaty-of-Waitangi Aotearoa/New Zealand.",
    "global.classical-antiquity.axial-age": "Concurrent religious/philosophical revolutions in Greece, Israel, Persia, India, and China.",
    "global.multi-regional.age-of-sail": "European maritime exploration and colonial expansion, roughly Columbus to Napoleon.",
    "global.multi-regional.columbus": "Christopher Columbus's first landfall in the Bahamas; opened sustained contact between the Old World and the Americas.",
    "global.short-20c.ww1": "World War I — the first industrialized total war; ended four empires.",
    "global.short-20c.ww2": "World War II — the deadliest conflict in human history; ended with the atomic bombings of Japan.",
    "global.short-20c.cold-war": "US–USSR geopolitical rivalry, 1947–1991; defined the second half of the 20th century.",
    "europe.mediterranean.rome.empire.constantinian": "Roman imperial dynasty led by Constantine the Great and his successors; Christianization of the Empire.",
    "europe.mediterranean.rome.empire.western-collapse": "Final disintegration of the Western Roman Empire during a rapid succession of short-lived emperors.",
    "oceania.polynesia.hawaii.kamehameha1": "Warrior chief who unified the Hawaiian Islands into a single kingdom.",
}

for _eid, _summary in _backfill_summaries.items():
    for _e in entities:
        if _e["id"] == _eid and not _e.get("summary"):
            _e["summary"] = _summary
            break


# =============================================================================
# WRITE ENTITIES
# =============================================================================

# Ensure no duplicate ids
seen = set()
for e in entities:
    if e["id"] in seen:
        raise SystemExit(f"Duplicate entity id: {e['id']}")
    seen.add(e["id"])

# Ensure parents exist
for e in entities:
    p = e.get("parent_id")
    if p and p not in seen:
        raise SystemExit(f"Missing parent for {e['id']}: {p}")

# Q-30: per-boundary end dating. Runs after every extension has contributed,
# so it sees the final corpus rather than a partial one. See tools/end_dating.py
# for why this derives rather than inherits, and where it refuses to.
from end_dating import apply_end_dating_methods  # noqa: E402

_explicit, _derived, _unset = apply_end_dating_methods(entities)
print(
    f"End dating: {_explicit} explicit, {_derived} derived, {_unset} left unset "
    f"(end rests on different science from the start)"
)

# Adjectival and qualified names are added before aliases are derived, so the adjectival
# forms become searchable aliases like every other name form. Running it afterwards left
# "Roman" indexed nowhere, which is the bug this was meant to fix.
_new_kinds(E, entities)
_author_cities(E, entities)
# Also before normalisation, for the same reason: these are new entities, and the canonical form
# of their ids has to be settled before anything references them.
from author_modern import extend as _author_modern
_author_modern(E, entities)
# Immediately after, and still before normalisation: rule 9 compares people by overlapping dates
# rather than by name, and caught 24 tenures the merge's string comparison could not see.
from modern_dedupe import extend as _modern_dedupe
_modern_dedupe(E, entities)

# Before normalisation, like the other authoring modules. The Languages branch also absorbs the
# old global.languages entities, so it must run before anything reads language ids.
from author_languages import extend as _author_languages
_LANGUAGE_REDIRECTS = _author_languages(E, entities)
from modern_dedupe import reparent_anachronisms as _reparent_anachronisms, \
    resolve_collisions as _resolve_collisions
from modern_dedupe import reparent_off_places as _reparent_off_places
_reparent_off_places(E, entities)
_reparent_anachronisms(E, entities)

# Immediately after the last module that authors entities, and before every module that
# REFERENCES one by id. Running it last meant polity_split was matching against pre-normalisation
# ids -- it looked for `ur-iii` while the entity was still `ur3` -- so a correct id list failed.
# Canonicalise once, then let everything downstream use the canonical form.
_ID_REDIRECTS = _normalize_ids(E, entities) or {}
# The old global.languages ids must keep resolving; nothing referenced them internally, but a
# reader may have one bookmarked.
_ID_REDIRECTS.update(_LANGUAGE_REDIRECTS or {})
# AFTER normalisation, because it names entities by id and the seed carried `william1` where the
# canonical form is `william-i`. Placed before it, the lookup silently matched nothing and the
# duplicate survived -- the same ordering mistake this file already documents twice above.
_resolve_collisions(E, entities)
from modern_dedupe import resolve_cross_tree_names as _resolve_cross_tree
_resolve_cross_tree(E, entities)
# After new_kinds, so names introduced there are checked for collisions too.
_name_repair(E, entities)
_migrate_dating(E, entities)
_historicity(E, entities)
_search_phrases(E, entities)
_polity_split(E, entities)
_contemporary_placement(E, entities)
_review_triage(E, entities)
_review_dating(E, entities)
_drop_derived_bounds(E, entities)

# Last of the correction modules, and after normalisation, because every patch names an entity
# by id.
from apply_corrections import extend as _apply_corrections
_apply_corrections(E, entities)
from apply_corrections import flag_overruns as _flag_overruns
_flag_overruns(E, entities)

# Link derivation runs AFTER the corrections, because it reads dates to decide what succeeds what.
# Placed before them, it derived a succession from Lamphun at 600 BCE and the correction then moved
# Lamphun to 750 CE, leaving a link asserting abutment across thirteen centuries.
_derive_links(E, entities)

# Aliases are derived from name_forms LAST, because several later modules add name forms and
# this has now been got wrong in both directions: running it before name_repair left the
# adjectival forms ("Roman" for the Roman Empire) indexed nowhere, and moving name_repair after
# it to fix a different ordering bug re-broke exactly that. Deriving at the end is the only
# position that does not depend on which module ran when.
# Search must match on every name a reader might arrive with, including ones
# the UI files under headings like "Rejected name". Deriving `aliases` from
# `name_forms` rather than asking authors to maintain both is the only way the
# two cannot drift apart -- and drift here means a reader searching "Anasazi"
# silently gets nothing.
_nf_entities = 0
for _e in entities:
    _forms = _e.get("name_forms")
    if not _forms:
        continue
    _nf_entities += 1
    _names = [f["name"] for f in _forms]
    # The display name is not its own alias.
    _merged = [n for n in dict.fromkeys(list(_e.get("aliases", [])) + _names)
               if n != _e["name"]]
    if _merged:
        _e["aliases"] = _merged
print(f"Name forms: {_nf_entities} entities carry structured names")

# Immediately before the write, because this rewrites every entity's dating fields and so
# must see the final state. Two earlier placements were both wrong: one ran before later
# modules had authored their entities, and one ran after this file had already been written,
# which meant its work was silently discarded.
# After the dating migration, not before. Succession is derived from how closely one entity's
# end abuts the next one's start, and the migration rounds deep-time dates -- so deriving first
# measured gaps that the rounding then changed, leaving links whose own tolerance rule they no
# longer satisfied.

with open(DATA / "entities.json", "w") as f:
    json.dump(_envelope("entities", entities, redirects=_ID_REDIRECTS), f, indent=2, ensure_ascii=False)
print(f"Wrote entities.json — {len(entities)} entities")


# =============================================================================
# CALENDARS
# =============================================================================

# Japanese nengō (subset — most-cited era names)
nengo_named = [
    ("Taika", "大化", 645, 650),
    ("Hakuchi", "白雉", 650, 654),
    ("Shuchō", "朱鳥", 686, 686),
    ("Taihō", "大宝", 701, 704),
    ("Wadō", "和銅", 708, 715),
    ("Tenpyō", "天平", 729, 749),
    ("Enryaku", "延暦", 782, 806),
    ("Kōnin", "弘仁", 810, 824),
    ("Engi", "延喜", 901, 923),
    ("Kanpyō", "寛平", 889, 898),
    ("Genryaku", "元暦", 1184, 1185),
    ("Bunji", "文治", 1185, 1190),
    ("Kenkyū", "建久", 1190, 1199),
    ("Jōkyū", "承久", 1219, 1222),
    ("Bun'ei", "文永", 1264, 1275),
    ("Kōan", "弘安", 1278, 1288),
    ("Genkō", "元弘", 1331, 1334),
    ("Kenmu", "建武", 1334, 1336),
    ("Ōei", "応永", 1394, 1428),
    ("Ōnin", "応仁", 1467, 1469),
    ("Tenshō", "天正", 1573, 1592),
    ("Bunroku", "文禄", 1592, 1596),
    ("Keichō", "慶長", 1596, 1615),
    ("Genna", "元和", 1615, 1624),
    ("Kan'ei", "寛永", 1624, 1644),
    ("Genroku", "元禄", 1688, 1704),
    ("Kyōhō", "享保", 1716, 1736),
    ("Kansei", "寛政", 1789, 1801),
    ("Bunka", "文化", 1804, 1818),
    ("Tenpō", "天保", 1830, 1844),
    ("Kaei", "嘉永", 1848, 1854),
    ("Ansei", "安政", 1854, 1860),
    ("Bunkyū", "文久", 1861, 1864),
    ("Genji", "元治", 1864, 1865),
    ("Keiō", "慶応", 1865, 1868),
    ("Meiji", "明治", 1868, 1912),
    ("Taishō", "大正", 1912, 1926),
    ("Shōwa", "昭和", 1926, 1989),
    ("Heisei", "平成", 1989, 2019),
    ("Reiwa", "令和", 2019, None),
]

calendars = [
    {
        "id": "gregorian",
        "name": "Gregorian",
        "kind": "solar",
        "epoch_year": 1,
        "direction": "both",
        "notes": "Adopted in 1582 by Catholic Europe; used proleptically before that date. The default modern calendar.",
        "conversion": {"gregorian_offset": 0}
    },
    {
        "id": "julian",
        "name": "Julian",
        "kind": "solar",
        "epoch_year": -45,
        "direction": "forward",
        "notes": "Introduced by Julius Caesar in 45 BCE. Drifted about 11 days behind the Gregorian by 1582."
    },
    {
        "id": "ce-bce",
        "name": "CE / BCE (Common Era)",
        "kind": "solar",
        "epoch_year": 1,
        "direction": "both",
        "notes": "Religion-neutral labeling of the same year numbers as AD/BC. No year 0."
    },
    {
        "id": "hijri",
        "name": "Islamic (Hijri, AH)",
        "kind": "lunar",
        "epoch_year": 622,
        "direction": "forward",
        "notes": "Lunar calendar starting from Muhammad's Hijra (622 CE). ~354-day year drifts ~11 days/year against solar; ~33 lunar years ≈ 32 solar years.",
        "conversion": {"formula": "gregorian ≈ 622 + (hijri * 0.970224)"}
    },
    {
        "id": "solar-hijri",
        "name": "Iranian (Solar Hijri, SH)",
        "kind": "solar",
        "epoch_year": 622,
        "direction": "forward",
        "notes": "Same epoch as Islamic Hijri but solar. Modern Iranian and Afghan calendar.",
        "conversion": {"gregorian_offset": 621}
    },
    {
        "id": "buddhist-era",
        "name": "Buddhist Era (BE, Thai)",
        "kind": "solar",
        "epoch_year": -543,
        "direction": "forward",
        "notes": "Based on the traditional date of the Buddha's parinirvana. Thai reckoning: BE = CE + 543.",
        "conversion": {"gregorian_offset": -543}
    },
    {
        "id": "hebrew-am",
        "name": "Hebrew (Anno Mundi)",
        "kind": "lunisolar",
        "epoch_year": -3761,
        "direction": "forward",
        "notes": "AM = CE + 3761 (approximate; year change is Rosh Hashanah, not January 1).",
        "conversion": {"gregorian_offset": -3760}
    },
    {
        "id": "ethiopian",
        "name": "Ethiopian",
        "kind": "solar",
        "epoch_year": 8,
        "direction": "forward",
        "notes": "About 7-8 years behind Gregorian. Ethiopia officially uses this calendar.",
        "conversion": {"gregorian_offset": 7}
    },
    {
        "id": "roman-auc",
        "name": "Ab Urbe Condita (AUC)",
        "kind": "regnal",
        "epoch_year": -753,
        "direction": "forward",
        "notes": "'From the founding of the City' — Rome. AUC 1 = 753 BCE by tradition.",
        "conversion": {"gregorian_offset": -754}
    },
    {
        "id": "maya-long-count",
        "name": "Maya Long Count",
        "kind": "cyclic",
        "epoch_year": -3114,
        "direction": "forward",
        "notes": "Counts days from a mythological creation date (Aug 11, 3114 BCE proleptic Gregorian). Positional in base-20 with a base-18 exception."
    },
    {
        "id": "aztec-calendar",
        "name": "Aztec Calendar Round",
        "kind": "cyclic",
        "epoch_year": None,
        "direction": "forward",
        "notes": "Two interlocking cycles (260-day tonalpohualli + 365-day xiuhpohualli) yielding a 52-year Calendar Round."
    },
    {
        "id": "chinese-sexagenary",
        "name": "Chinese Sexagenary Cycle",
        "kind": "cyclic",
        "epoch_year": -2637,
        "direction": "forward",
        "notes": "60-year repeating cycle combining 10 Heavenly Stems and 12 Earthly Branches. Used across East Asia."
    },
    {
        "id": "japanese-nengo",
        "name": "Japanese Nengō (Era Names)",
        "kind": "era-name",
        "epoch_year": 645,
        "direction": "forward",
        "notes": "Era names declared by the imperial court, from Taika (645) onward. Multiple per emperor before Meiji; one per emperor from 1868.",
        "named_years": [
            {
                **{
                    "name": name,
                    "native": native,
                    "start_gregorian": s,
                    "end_gregorian": e_year,
                },
                **({"entity_id": eid} if (eid := {
                    "Meiji": "east-asia.japan.modern.meiji",
                    "Taish\u014d": "east-asia.japan.modern.taisho",
                    "Sh\u014dwa": "east-asia.japan.modern.showa",
                    "Heisei": "east-asia.japan.modern.heisei",
                    "Reiwa": "east-asia.japan.modern.reiwa",
                }.get(name)) else {}),
            }
            for name, native, s, e_year in nengo_named
        ]
    },
    {
        "id": "chinese-regnal",
        "name": "Chinese Regnal Era Names",
        "kind": "era-name",
        "epoch_year": -140,
        "direction": "forward",
        "notes": "Emperors declared reign era names beginning with Emperor Wu of Han. Individual emperors could have multiple.",
        "named_years": [
            {"name": "Jianyuan", "native": "建元", "start_gregorian": -140, "end_gregorian": -135, "notes": "First named Chinese era, under Emperor Wu of Han."},
            {"name": "Kaiyuan", "native": "開元", "start_gregorian": 713, "end_gregorian": 741, "notes": "Golden age under Tang Xuanzong."},
            {"name": "Yongle", "native": "永樂", "start_gregorian": 1403, "end_gregorian": 1424, "notes": "Ming Yongle Emperor."},
            {"name": "Kangxi", "native": "康熙", "start_gregorian": 1662, "end_gregorian": 1722, "notes": "Qing Kangxi Emperor."},
            {"name": "Qianlong", "native": "乾隆", "start_gregorian": 1736, "end_gregorian": 1796, "notes": "Qing Qianlong Emperor."},
            {"name": "Guangxu", "native": "光緒", "start_gregorian": 1875, "end_gregorian": 1908, "notes": "Late Qing."},
            {"name": "Xuantong", "native": "宣統", "start_gregorian": 1909, "end_gregorian": 1912, "notes": "Last Qing era (Puyi)."}
        ]
    },
    {
        "id": "korean-regnal",
        "name": "Korean Regnal Eras",
        "kind": "era-name",
        "epoch_year": 536,
        "direction": "forward",
        "notes": "Korean states used their own regnal era names in Silla and again in the Korean Empire (1897–1910).",
        "named_years": [
            {"name": "Gwangmu", "native": "光武", "start_gregorian": 1897, "end_gregorian": 1907, "notes": "Emperor Gojong's Korean Empire era."},
            {"name": "Yunghui", "native": "隆熙", "start_gregorian": 1907, "end_gregorian": 1910}
        ]
    },
    {
        "id": "juche",
        "name": "Juche (North Korean)",
        "kind": "solar",
        "epoch_year": 1912,
        "direction": "forward",
        "notes": "North Korean calendar counting from Kim Il-sung's birth year (1912). Juche 1 = 1912 CE.",
        "conversion": {"gregorian_offset": 1911}
    },
    {
        "id": "vietnamese-nien-hieu",
        "name": "Vietnamese Nien Hieu (Era Names)",
        "kind": "era-name",
        "epoch_year": 544,
        "direction": "forward",
        "notes": "Vietnamese dynasties adopted a Chinese-style era-name system beginning with the Early Lý (544). Emperors could have multiple."
    },
    {
        "id": "egyptian-regnal",
        "name": "Egyptian Regnal Years",
        "kind": "regnal",
        "epoch_year": None,
        "direction": "forward",
        "notes": "Years counted from each pharaoh's accession; reset on each reign. No continuous count."
    },
    {
        "id": "french-republican",
        "name": "French Republican",
        "kind": "solar",
        "epoch_year": 1792,
        "direction": "forward",
        "notes": "Revolutionary calendar in use 1792–1806 (and briefly 1871). Year 1 began 22 Sept 1792; 12 months of 30 days plus 5 (or 6) 'complementary days'.",
        "conversion": {"gregorian_offset": 1791}
    },
    {
        "id": "olympiad",
        "name": "Greek Olympiad",
        "kind": "cyclic",
        "epoch_year": -776,
        "direction": "forward",
        "notes": "4-year cycles counted from the first ancient Olympics (776 BCE). Used by Greek historians."
    },
    {
        "id": "byzantine-am",
        "name": "Byzantine Anno Mundi",
        "kind": "solar",
        "epoch_year": -5508,
        "direction": "forward",
        "notes": "Byzantine 'year of the world' from a computed creation. AM = CE + 5508/5509.",
        "conversion": {"gregorian_offset": -5508}
    }
]

with open(DATA / "calendars.json", "w") as f:
    _n = _rewrite_refs(calendars, _ID_REDIRECTS)
    if _n:
        print(f"normalize_ids: rewrote {_n} id reference(s) in calendars")
    json.dump(_envelope("calendars", calendars), f, indent=2, ensure_ascii=False)
print(f"Wrote calendars.json — {len(calendars)} calendars")


# =============================================================================
# THEMES
# =============================================================================

def theme(id, name, description, ids, sort="chronological"):
    return {"id": id, "name": name, "description": description, "entity_ids": ids, "sort": sort}

themes = [
    theme("empires-classical", "Classical Empires",
          "Great empires of antiquity that shaped the ancient world.",
          [
              "west-asia.mesopotamia.akkadian",
              "west-asia.iran.achaemenid",
              "europe.mediterranean.macedon",
              "south-asia.maurya",
              "east-asia.china.han",
              f"{rome}.empire",
              "west-asia.iran.parthian",
              "central-asia.kushan",
              "west-asia.iran.sasanian",
          ]),
    theme("golden-ages", "Golden Ages",
          "Peak eras of art, science, and cultural flowering.",
          [
              "africa.nile.egypt.new-kingdom.dyn18",
              f"{gr}.classical",
              f"{rome}.empire.nerva-antonine",
              "south-asia.gupta",
              "east-asia.china.tang",
              "east-asia.japan.heian",
              "global.multi-regional.abbasid",
              "east-asia.china.song",
              "east-asia.japan.edo",
              "south-asia.mughal",
          ]),
    theme("world-empires", "World-Spanning Empires",
          "Empires that reshaped multiple continents.",
          [
              "west-asia.iran.achaemenid",
              f"{rome}.empire",
              "global.multi-regional.umayyad",
              "global.multi-regional.abbasid",
              "central-asia.mongol-empire",
              "global.multi-regional.ottoman",
              "south-asia.mughal",
              "europe.western.iberia.spanish-empire",
              "europe.western.france.napoleon",
              "europe.eastern.russian-empire",
          ]),
    theme("revolutions", "Revolutions",
          "Political and social upheavals that overturned old orders.",
          [
              "europe.western.france.revolution",
              "americas.north.usa",
              "east-asia.japan.modern.meiji",
              "europe.eastern.soviet.lenin",
              "east-asia.china.prc",
              "west-asia.iran.islamic-republic",
          ]),
    theme("collapses", "Collapses & Dark Ages",
          "Times when established orders unraveled.",
          [
              "global.bronze-age.collapse",
              "africa.nile.egypt.fip",
              "africa.nile.egypt.sip",
              "africa.nile.egypt.tip",
              f"{gr}.dark-age",
              "east-asia.china.three-kingdoms",
              "global.middle-ages.black-death",
          ]),
    theme("silk-road", "Silk Road Eras",
          "Periods when long-distance Eurasian trade flourished.",
          [
              "east-asia.china.han.western",
              "central-asia.kushan",
              "east-asia.china.tang",
              "global.multi-regional.abbasid",
              "central-asia.mongol-empire",
              "central-asia.timurid",
          ]),
    theme("great-founders", "Empire Founders",
          "Individuals who founded or refounded major states.",
          [
              "africa.nile.egypt.early-dynastic.dyn1.narmer",
              "west-asia.mesopotamia.akkadian.sargon",
              "west-asia.iran.achaemenid.cyrus2",
              "europe.mediterranean.macedon.alexander",
              "south-asia.maurya.chandragupta",
              "east-asia.china.qin.shi-huang",
              f"{rome}.empire.augustus",
              "central-asia.mongol-empire.genghis",
              "africa.west.mali.sundiata",
              "americas.andes.inca.pachacuti",
              "americas.mesoamerica.aztec.itzcoatl",
              "south-asia.mughal.babur",
              "oceania.polynesia.hawaii.kamehameha1",
          ]),
    theme("women-rulers", "Women Rulers",
          "Empresses, queens, and female heads of state.",
          [
              "africa.nile.egypt.new-kingdom.dyn18.hatshepsut",
              "africa.nile.egypt.ptolemaic.cleopatra7",
              "east-asia.china.tang.wu-zetian",
              "europe.western.england.tudor.elizabeth1",
              "europe.western.britain.victorian.victoria",
              "europe.eastern.russian-empire.catherine2",
              "east-asia.china.qing.cixi",
              "oceania.polynesia.hawaii.liliuokalani",
          ]),
    theme("indian-ocean-world", "Indian Ocean World",
          "Maritime powers of the Indian Ocean trade network.",
          [
              "south-asia.chola",
              "africa.east.swahili",
              "southeast-asia.maritime.srivijaya",
              "southeast-asia.maritime.majapahit",
              "africa.nile.aksum",
              "west-asia.arabia.pre-islamic",
              "africa.east.zanzibar-sultanate",
          ]),
    # --- Phase 0: added themes ---
    theme("islamic-world", "The Greater Islamic World",
          "Muslim-ruled polities from the Rashidun conquests through the great early-modern empires.",
          [
              "west-asia.arabia.rise-islam",
              "global.multi-regional.rashidun",
              "global.multi-regional.umayyad",
              "global.multi-regional.abbasid",
              "global.multi-regional.fatimid",
              "west-asia.iran.safavid",
              "south-asia.mughal",
              "global.multi-regional.ottoman",
              "africa.west.mali",
              "africa.west.songhai",
              "africa.west.sokoto",
              "africa.north.almoravid",
              "africa.north.almohad",
          ]),
    theme("industrialization", "Industrialization",
          "The two industrial revolutions and their global spread.",
          [
              "global.industrial-revolution",
              "global.second-industrial-revolution",
              f"{we}.britain.victorian",
              "europe.central.german-empire",
              "east-asia.japan.modern.meiji",
              "americas.north.usa",
          ]),
    theme("world-religions", "Birth of Major Religions",
          "Founding periods and figures of the major world religions.",
          [
              "west-asia.mesopotamia.israel-judah",
              "south-asia.mahajanapadas",
              "east-asia.china.zhou.eastern.spring-autumn",
              "west-asia.arabia.rise-islam.muhammad",
              "south-asia.maurya.ashoka",
              "africa.nile.aksum.ezana",
          ]),
    theme("cold-war-proxy", "Cold War Proxy Conflicts",
          "Regional conflicts in which the US and USSR backed opposing sides.",
          [
              "global.short-20c.korean-war",
              "global.short-20c.vietnam-war",
              "global.short-20c.cuban-missile-crisis",
              "global.short-20c.berlin-wall-fall",
              "global.short-20c.soviet-dissolution",
          ]),
    theme("decolonization", "Decolonization",
          "Dissolution of European colonial empires and emergence of independent post-colonial states.",
          [
              "global.multi-regional.decolonization",
              "south-asia.independence",
              f"{sea}.maritime.indonesia",
              "africa.nile.ethiopia.haile-selassie",
              "africa.southern.zulu",
          ]),
    theme("mesoamerican-civilizations", "Mesoamerican Civilizations",
          "Pre-Columbian civilizations of Mexico and Central America.",
          [
              f"{meso}.olmec",
              f"{meso}.zapotec",
              f"{meso}.teotihuacan",
              f"{meso}.maya",
              f"{meso}.toltec",
              f"{meso}.aztec",
          ]),
    theme("early-modern-europe", "Early Modern European Transformations",
          "Renaissance, Reformation, Scientific Revolution, and Enlightenment.",
          [
              "europe.renaissance",
              "europe.reformation",
              "europe.scientific-revolution",
              "europe.enlightenment",
          ]),
]


# =============================================================================
# SOURCES — normalized registry
# =============================================================================
# Referenced from entities by id rather than inlined. One chronology work cited
# by two hundred entities is stored once, which keeps the artifact linear in
# distinct sources rather than in citations.
#
# Deliberately small: the app is a starting point, not a research tool, and
# most entities are backed by a generated Wikipedia search rather than a
# citation. Sources are for the minority of cases where a specific work IS the
# substance of the claim. See docs/DESIGN.md, "Sources: the exception".

sources = [
    {
        "id": "dominguez-rodrigo-2016-lomekwi",
        "kind": "scholarly",
        "citation": "Domínguez-Rodrigo & Alcalá (2016), critique of the Lomekwi 3 context, PaleoAnthropology 2016:46-53",
        "url": "https://paleoanthro.org/media/journal/content/PA20160046.pdf",
        "note": "Minority: argues the assemblage is not demonstrably in primary context.",
    },
    {
        "id": "mcpherron-2010-dikika",
        "kind": "scholarly",
        "citation": "McPherron et al. (2010), 'Evidence for stone-tool-assisted consumption of animal tissues before 3.39 million years ago at Dikika, Ethiopia', Nature",
        "url": "https://www.nature.com/articles/nature09248",
    },
    {
        "id": "dominguez-rodrigo-2010-dikika",
        "kind": "scholarly",
        "citation": "Domínguez-Rodrigo, Pickering & Bunn (2010), 'Configurational approach to identifying the earliest hominin butchers', PNAS 107:20929-20934",
        "url": "https://www.pnas.org/doi/10.1073/pnas.1013711107",
        "note": "Majority: argues the Dikika marks are trampling damage.",
    },
    {
        "id": "berna-2012-wonderwerk",
        "kind": "scholarly",
        "citation": "Berna et al. (2012), 'Microstratigraphic evidence of in situ fire in the Acheulean strata of Wonderwerk Cave, South Africa', PNAS",
        "url": "https://www.pnas.org/doi/10.1073/pnas.1117620109",
    },
    {
        "id": "plos-2026-wonderwerk-st11",
        "kind": "scholarly",
        "citation": "PLOS ONE (2026), evidence for burning in Wonderwerk Stratum 11, 1.79-1.07 Ma",
        "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0347480",
    },
    {
        "id": "deino-2002-kapthurin",
        "kind": "scholarly",
        "citation": "Deino & McBrearty (2002), 40Ar/39Ar dating of the Kapthurin Formation, Baringo, Kenya, Journal of Human Evolution",
        "url": "http://in-africa.org/wp-content/uploads/2012/12/Deino-McBrearty-2002-JHE-date-of-Kapthurin.pdf",
    },
    {
        "id": "brooks-2018-olorgesailie",
        "kind": "scholarly",
        "citation": "Brooks et al. (2018), long-distance stone transport and pigment use in the Middle Stone Age, Science",
        "url": "https://www.science.org/doi/10.1126/science.aao2646",
    },
    {
        "id": "arnold-2014-sima",
        "kind": "scholarly",
        "citation": "Arnold et al. (2014), luminescence dating and palaeomagnetic age constraint on the hominins from Sima de los Huesos, Atapuerca",
        "url": "https://cir.cenieh.es/bitstream/20.500.12136/315/1/Luminescence%20dating%20and%20palaeomagnetic%20age%20constraint%20on%20hominins%20from%20Sima%20de%20los%20Huesos,%20Atapuerca,%20Spain_Arnold_et_al_2014.pdf",
    },
    {
        "id": "valladas-1988-qafzeh",
        "kind": "scholarly",
        "citation": "Valladas et al. (1988), thermoluminescence dating of Mousterian burials at Qafzeh, Israel, Nature 331:614",
        "url": "https://www.nature.com/articles/331614a0",
    },
    {
        "id": "smithsonian-qafzeh-burial",
        "kind": "scholarly",
        "citation": "Smithsonian Human Origins — Qafzeh: oldest intentional burial",
        "url": "https://humanorigins.si.edu/evidence/behavior/burial/qafzeh-oldest-intentional-burial",
    },
    {
        "id": "oktaviana-2024-sulawesi",
        "kind": "scholarly",
        "citation": "Oktaviana et al. (2024), 'Narrative cave art in Indonesia by 51,200 years ago', Nature",
        "url": "https://www.nature.com/articles/s41586-024-07541-7",
    },
    {
        "id": "henshilwood-2002-blombos",
        "kind": "scholarly",
        "citation": "Henshilwood et al. (2002), 'Emergence of modern human behavior: Middle Stone Age engravings from South Africa', Science",
        "url": "https://www.science.org/doi/10.1126/science.1067575",
    },
    {
        "id": "henshilwood-2018-blombos-drawing",
        "kind": "scholarly",
        "citation": "Henshilwood et al. (2018), 'An abstract drawing from the 73,000-year-old levels at Blombos Cave, South Africa', Nature 562:115-118",
        "url": "https://www.nature.com/articles/s41586-018-0514-3",
    },
    {
        "id": "sehasseh-2021-bizmoune",
        "kind": "scholarly",
        "citation": "Sehasseh et al. (2021), 'Early Middle Stone Age personal ornaments from Bizmoune Cave, Essaouira, Morocco', Science Advances",
        "url": "https://www.science.org/doi/10.1126/sciadv.abi8620",
    },
    {
        "id": "clarkson-2017-madjedbebe",
        "kind": "scholarly",
        "citation": "Clarkson et al. (2017), 'Human occupation of northern Australia by 65,000 years ago', Nature",
        "url": "https://faculty.washington.edu/bmarwick/PDFs/Clarkson_Jacobs_Marwick_2017.pdf",
    },
    {
        "id": "clarkson-2018-reply",
        "kind": "scholarly",
        "citation": "Clarkson et al. (2018), reply to critiques of the Madjedbebe chronology, Australian Archaeology",
        "url": "http://faculty.washington.edu/bmarwick/PDFs/Clarkson-Roberts-Jacobs-Marwick-et-al-2018-AA-reply.pdf",
        "note": "Records the sceptical reading of about 53 ka.",
    },
    {
        "id": "zohar-2022-cooking",
        "kind": "scholarly",
        "citation": "Zohar et al. (2022), 'Evidence for the cooking of fish 780,000 years ago at Gesher Benot Ya'aqov, Israel', Nature Ecology & Evolution",
        "url": "https://www.nature.com/articles/s41559-022-01910-z",
    },
    {
        "id": "joordens-2015-trinil",
        "kind": "scholarly",
        "citation": "Joordens et al. (2015), 'Homo erectus at Trinil on Java used shells for tool production and engraving', Nature",
        "url": "https://www.nature.com/articles/nature13962",
    },
    {
        "id": "deino-2012-olduvai",
        "kind": "scholarly",
        "citation": "Deino (2012), 40Ar/39Ar dating of Olduvai Gorge Beds I-II",
        "url": "https://pubmed.ncbi.nlm.nih.gov/22809744/",
    },
    {
        "id": "vidal-2022-omo",
        "kind": "scholarly",
        "citation": "Vidal et al. (2022), 'Age of the oldest known Homo sapiens from eastern Africa', Nature",
        "url": "https://www.nature.com/articles/s41586-021-04275-8",
    },
    {
        "id": "bader-2022-msa",
        "kind": "scholarly",
        "citation": "Bader et al. (2022), the Middle Stone Age of southern Africa",
        "url": "https://www.hadw-bw.de/sites/default/files/documents/Bader%20et%20al.%202022_MSA%20of%20South%20Africa.pdf",
    },
    {
        "id": "jacobs-2006-blombos",
        "kind": "scholarly",
        "citation": "Jacobs et al. (2006), single-grain OSL ages for Blombos Cave, Journal of Human Evolution",
        "url": "http://in-africa.org/wp-content/uploads/2012/12/Jacobs-et-al-2006-JHE-OSL-dates-for-Blombos.pdf",
    },
    {
        "id": "klasies-river-guide",
        "kind": "scholarly",
        "citation": "Klasies River Mouth site guide, Stellenbosch University",
        "url": "http://academic.sun.ac.za/archaeology/krguide2001.pdf",
    },
    {
        "id": "backwell-2018-border-cave",
        "kind": "scholarly",
        "citation": "Backwell et al. (2018), the Border Cave sequence, Journal of Field Archaeology",
        "url": "https://hal.science/hal-04722241v1/file/Backwell%20et%20al_Border%20Cave%20chapter.pdf",
    },
    {
        "id": "mcgee-2017-ahp",
        "kind": "scholarly",
        "citation": "McGee & deMenocal (2017), the African Humid Period",
        "url": "https://www.ldeo.columbia.edu/~peter/site/Home_files/McGee.deMenocal2017.pdf",
    },
    {
        "id": "wendorf-1998-nabta",
        "kind": "scholarly",
        "citation": "Wendorf & Schild (1998), Nabta Playa and its role in Northeastern African prehistory",
        "url": "https://www.kar.zcu.cz/studium/materialy/egy/texty-pro-studenty-2012/NabtaPlaya.pdf",
    },
    {
        "id": "malville-1998-nabta",
        "kind": "scholarly",
        "citation": "Malville et al. (1998), megaliths and Neolithic astronomy in southern Egypt, Nature 392:488-491",
        "url": "https://www.nature.com/articles/33131",
    },
    {
        "id": "ppnd-summary",
        "kind": "scholarly",
        "citation": "Benz, Platform for Neolithic Radiocarbon Dates (PPND) chronology summary, ex oriente",
        "url": "https://www.exoriente.org/associated_projects/ppnd_summary.php",
    },
    {
        "id": "oxford-natufian",
        "kind": "scholarly",
        "citation": "Nilsson Stutz et al., the Natufian, Oxford Handbook",
        "url": "https://academic.oup.com/edited-volume/59635/chapter/505050944",
    },
    {
        "id": "orton-catalhoyuk",
        "kind": "scholarly",
        "citation": "Orton et al., 'A tale of two tells': dating Catalhoyuk West",
        "url": "https://eprints.whiterose.ac.uk/id/eprint/132693/1/tale_of_two_tells_dating_the_catalhoyuk_west_mound.pdf",
    },
    {
        "id": "halaf-chronology",
        "kind": "scholarly",
        "citation": "Halaf and Late Neolithic chronology of northern Mesopotamia, DergiPark",
        "url": "https://dergipark.org.tr/en/download/article-file/1184094",
    },
    {
        "id": "beyond-the-ubaid",
        "kind": "scholarly",
        "citation": "Carter & Philip (eds), Beyond the Ubaid, Oriental Institute SAOC 63",
        "url": "https://isac.uchicago.edu/sites/default/files/uploads/shared/docs/saoc63.pdf",
    },
    {
        "id": "bar-yosef-jericho",
        "kind": "scholarly",
        "citation": "Bar-Yosef, the walls of Jericho: an alternative interpretation",
        "url": "https://dash.harvard.edu/server/api/core/bitstreams/7312037d-1ce8-6bd4-e053-0100007fdf3b/content",
        "note": "Stage dates are UNCALIBRATED radiocarbon and are not labelled as such in the source.",
    },
    {
        "id": "ppnd-jericho",
        "kind": "scholarly",
        "citation": "PPND site entry for Jericho / Tell es-Sultan, ex oriente",
        "url": "https://www.exoriente.org/associated_projects/ppnd_site.php?s=36",
    },
    {
        "id": "grissom-ain-ghazal",
        "kind": "scholarly",
        "citation": "Grissom, the statues of 'Ain Ghazal, Smithsonian",
        "url": "https://repository.si.edu/server/api/core/bitstreams/73bd63c6-4d5d-42a0-a679-b530a8d81b88/content",
        "note": "Gives uncalibrated 6750 +/- 80 BC and the calibrated equivalent 7580 +/- 110 BC.",
    },
    {
        "id": "ppnd-ain-ghazal",
        "kind": "scholarly",
        "citation": "PPND site entry for 'Ain Ghazal, ex oriente",
        "url": "https://www.exoriente.org/associated_projects/ppnd_site.php?s=10",
    },
    {
        "id": "harmand-2015-lomekwi",
        "kind": "scholarly",
        "citation": "Harmand et al. (2015), '3.3-million-year-old stone tools from Lomekwi 3, West Turkana, Kenya', Nature",
        "url": "https://www.nature.com/articles/nature14464",
    },
    {
        "id": "smithsonian-human-origins",
        "kind": "reference",
        "citation": "Smithsonian National Museum of Natural History, Human Origins Program",
        "url": "https://humanorigins.si.edu/evidence/human-fossils/species",
    },
    {
        "id": "villmoare-2015-ledi-geraru",
        "kind": "scholarly",
        "citation": "Villmoare et al. (2015), 'Early Homo at 2.8 Ma from Ledi-Geraru, Afar, Ethiopia', Science",
        "url": "https://pubmed.ncbi.nlm.nih.gov/25739410/",
    },
    {
        "id": "hawks-2015-ledi-geraru-dissent",
        "kind": "scholarly",
        "citation": "Hawks, de Ruiter & Berger (2015), comment on the attribution of LD 350-1 to Homo",
        "url": "https://pubmed.ncbi.nlm.nih.gov/26089505/",
        "note": "Minority position: argues LD 350-1 cannot be unequivocally assigned to Homo.",
    },
    {
        "id": "nature-2025-gurumaha-tuff",
        "kind": "scholarly",
        "citation": "Nature (2025), Ar/Ar constraint on the Gurumaha Tuff, 2.782 +/- 0.006 Ma",
        "url": "https://www.nature.com/articles/s41586-025-09390-4",
    },
    {
        "id": "rizal-2020-ngandong",
        "kind": "scholarly",
        "citation": "Rizal et al. (2020), 'Last appearance of Homo erectus at Ngandong, Java, 117,000-108,000 years ago', Nature",
        "url": "https://www.nature.com/articles/s41586-019-1863-2",
    },
    {
        "id": "falgueres-gran-dolina",
        "kind": "scholarly",
        "citation": "Falgueres et al., ESR/U-series chronology of Gran Dolina TD6, Atapuerca",
        "url": "https://hal.science/hal-01911095",
    },
    {
        "id": "douka-2019-denisova",
        "kind": "scholarly",
        "citation": "Douka et al. (2019), 'Age estimates for hominin fossils and the onset of the Upper Palaeolithic at Denisova Cave', Nature",
        "url": "https://www.nature.com/articles/s41586-018-0870-z",
    },
    {
        "id": "nhm-luzonensis",
        "kind": "reference",
        "citation": "Natural History Museum, London — Homo luzonensis",
        "url": "https://www.nhm.ac.uk/discover/homo-luzonensis-your-guide-to-the-species.html",
    },
    {
        "id": "hublin-2017-jebel-irhoud",
        "kind": "scholarly",
        "citation": "Hublin et al. (2017), 'New fossils from Jebel Irhoud, Morocco and the pan-African origin of Homo sapiens', Nature",
        "url": "https://pubmed.ncbi.nlm.nih.gov/28593953/",
    },
    {
        "id": "ji-2021-homo-longi",
        "kind": "scholarly",
        "citation": "Ji et al. (2021), description of the Harbin cranium as Homo longi, The Innovation",
        "url": "https://www.cell.com/the-innovation/fulltext/S2666-6758(21)00057-9",
    },
    {
        "id": "fu-2025-harbin-proteome",
        "kind": "scholarly",
        "citation": "Fu et al. (2025), palaeoproteomic analysis placing the Harbin cranium with Denisova 3",
        "url": "https://pubmed.ncbi.nlm.nih.gov/40531192/",
    },
    {
        "id": "lepre-2011-kokiselei",
        "kind": "scholarly",
        "citation": "Lepre et al. (2011), 'An earlier origin for the Acheulian', Nature",
        "url": "https://www.nature.com/articles/nature10372",
    },
    {
        "id": "marin-arroyo-2018-cantabria",
        "kind": "scholarly",
        "citation": "Marin-Arroyo et al. (2018), chronology of the Middle to Upper Palaeolithic transition in Cantabrian Spain, PLOS ONE",
        "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0194708",
    },
    {
        "id": "banks-2013-aurignacian",
        "kind": "scholarly",
        "citation": "Banks et al. (2013), Proto-Aurignacian and Early Aurignacian chronology",
        "url": "https://pubmed.ncbi.nlm.nih.gov/23245623/",
    },
    {
        "id": "rios-garaizar-2022-chatelperronian",
        "kind": "scholarly",
        "citation": "Rios-Garaizar et al. (2022), Chatelperronian chronology in southwest Europe, PLOS ONE",
        "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0265219",
    },
    {
        "id": "cascalheira-2015-solutrean",
        "kind": "scholarly",
        "citation": "Cascalheira & Bicho (2015), Bayesian analysis of the Solutrean sequence, PLOS ONE",
        "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0122560",
    },
    {
        "id": "wurz-2013-msa",
        "kind": "scholarly",
        "citation": "Wurz (2013), 'Technological trends in the Middle Stone Age of South Africa', Current Anthropology",
        "url": "https://www.journals.uchicago.edu/doi/10.1086/673283",
    },
    {
        "id": "jacobs-2008-msa",
        "kind": "scholarly",
        "citation": "Jacobs et al. (2008), 'Ages for the Middle Stone Age of southern Africa', Science",
        "url": "https://pubmed.ncbi.nlm.nih.gov/18974351/",
    },
    {
        "id": "villa-2012-border-cave",
        "kind": "scholarly",
        "citation": "Villa et al. (2012), 'Border Cave and the beginning of the Later Stone Age in South Africa', PNAS",
        "url": "https://www.pnas.org/doi/10.1073/pnas.1202629109",
    },
    {
        "id": "plos-2022-el-mnasra",
        "kind": "scholarly",
        "citation": "PLOS ONE (2022), chronology of the Aterian at El Mnasra, Morocco",
        "url": "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0261282",
    },
    {
        "id": "braun-2019-bokol-dora",
        "kind": "scholarly",
        "citation": "Braun et al. (2019), 'Earliest known Oldowan artifacts at >2.58 Ma', PNAS 116(24)",
        "url": "https://www.pnas.org/doi/10.1073/pnas.1820177116",
    },
    {
        "id": "dietrich-2013-gobekli",
        "kind": "scholarly",
        "citation": "Dietrich & Schmidt et al., radiocarbon chronology of Göbekli Tepe",
        "url": "https://www.dainst.blog/the-tepe-telegrams/",
    },
    {
        "id": "sutikna-2016-flores",
        "kind": "scholarly",
        "citation": "Sutikna et al. (2016), 'Revised stratigraphy and chronology for Homo floresiensis at Liang Bua', Nature 532",
        "url": "https://www.nature.com/articles/nature17179",
    },
    {
        "id": "dillehay-1997-monte-verde",
        "kind": "scholarly",
        "citation": "Dillehay, Monte Verde: A Late Pleistocene Settlement in Chile (1997)",
    },
    {
        "id": "surovell-2026-monte-verde",
        "kind": "scholarly",
        "citation": "Surovell et al. (2026), reanalysis proposing a Holocene age for Monte Verde II, Science",
        "note": "Minority position. Rebutted by ~30 specialists in May 2026; authors replied June 2026.",
    },
    {
        "id": "arsuaga-2014-sima",
        "kind": "scholarly",
        "citation": "Arsuaga et al. (2014), Sima de los Huesos",
        "url": "https://cnrs.hal.science/hal-03739291/document"
    },
    {
        "id": "higham-2014-neanderthal",
        "kind": "scholarly",
        "citation": "Higham et al. (2014), Neanderthal disappearance",
        "url": "https://www.nature.com/articles/nature13621"
    },
    {
        "id": "quiles-2016-chauvet",
        "kind": "scholarly",
        "citation": "Quiles et al. (2016), Chauvet Cave chronology",
        "url": "https://www.pnas.org/doi/10.1073/pnas.1523158113"
    },
    {
        "id": "pettitt-bahn-2015-chauvet",
        "kind": "scholarly",
        "citation": "Pettitt and Bahn (2015), alternative Chauvet chronology",
        "url": "https://www.cambridge.org/core/journals/antiquity/article/an-alternative-chronology-for-the-art-of-chauvet-cave/723AB31F4E88629A2B7323BDD4845450"
    },
    {
        "id": "culture-gouv-lascaux",
        "kind": "scholarly",
        "citation": "French Ministry of Culture, dating Lascaux",
        "url": "https://archeologie.culture.gouv.fr/lascaux/en/dating-figures-lascaux"
    },
    {
        "id": "garcia-diez-2013-altamira",
        "kind": "scholarly",
        "citation": "García-Diez et al. (2013), Altamira uranium-series dates",
        "url": "https://cir.cenieh.es/bitstream/20.500.12136/420/1/Uranium%20series%20dating%20reveals%20a%20long%20sequence%20of%20rock%20art%20at%20Altamira%20Cave%20(Santillana%20del%20Mar,%20Cantabria)_Garc%C3%ADa-Diez_et_al_2013.pdf"
    },
    {
        "id": "jakucs-2016-lbk",
        "kind": "scholarly",
        "citation": "Jakucs et al. (2016), LBK chronology",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC5040754/"
    },
    {
        "id": "schulz-paulsson-2019-megaliths",
        "kind": "scholarly",
        "citation": "Schulz Paulsson (2019), megalith chronology",
        "url": "https://www.pnas.org/doi/10.1073/pnas.1813268116"
    },
    {
        "id": "darvill-2012-stonehenge",
        "kind": "scholarly",
        "citation": "Darvill et al. (2012), Stonehenge chronology",
        "url": "https://eprints.bournemouth.ac.uk/20587/1/Antiquity%202012%20(Stonehenge%20Remodelled).pdf"
    },
    {
        "id": "papac-2021-corded-ware",
        "kind": "scholarly",
        "citation": "Papac et al. (2021), Corded Ware genomics and dates",
        "url": "https://www.stephanschiffels.de/pdfs/Papac2021-up.pdf"
    },
    {
        "id": "olalde-2018-beaker",
        "kind": "scholarly",
        "citation": "Olalde et al. (2018), Bell Beaker phenomenon",
        "url": "https://www.pure.ed.ac.uk/ws/portalfiles/portal/56097393/OlaldeEtalN2018TheBeakerPhenomenon.pdf"
    },
    {
        "id": "kutschera-otzi",
        "kind": "scholarly",
        "citation": "Kutschera, radiocarbon dating of the Iceman",
        "url": "https://www2.chemistry.msu.edu/courses/cem485/lectures/icemanage.pdf"
    },
    {
        "id": "taylor-2021-botai",
        "kind": "scholarly",
        "citation": "Taylor and Barrón-Ortiz (2021), Botai horse management",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8018961/"
    },
    {
        "id": "poliakov-2023-afanasievo",
        "kind": "scholarly",
        "citation": "Poliakov, Svyatko and Stepanova, Afanasievo chronology review",
        "url": "https://pureadmin.qub.ac.uk/ws/portalfiles/portal/203637844/ReviewOf.pdf"
    },
    {
        "id": "grigoriev-2021-andronovo",
        "kind": "scholarly",
        "citation": "Grigoriev (2021), Andronovo problem",
        "url": "https://www.degruyterbrill.com/document/doi/10.1515/opar-2020-0123/html?lang=en"
    },
    {
        "id": "lamberg-karlovsky-bmac",
        "kind": "scholarly",
        "citation": "Lamberg-Karlovsky, BMAC chronology",
        "url": "https://repositorio.uam.es/bitstream/handle/10486/660123/3902.pdf?isAllowed=y&sequence=1"
    },
    {
        "id": "lazaridis-2025-yamnaya",
        "kind": "scholarly",
        "citation": "Lazaridis et al. (2025), genetic origin of Indo-Europeans",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11922553/"
    },
    {
        "id": "matsumoto-2017-jomon",
        "kind": "scholarly",
        "citation": "Matsumoto, Habu and Matsui (2017), Jōmon chronology",
        "url": "https://junkohabu.com/wp-content/uploads/2018/02/matsumoto-habumatsui-2017.pdf"
    },
    {
        "id": "keally-jomon-dates",
        "kind": "scholarly",
        "citation": "Keally, Jōmon radiocarbon dates",
        "url": "http://www.t-net.ne.jp/~keally/Chronologies/jomon-dates.html"
    },
    {
        "id": "zhang-2013-peiligang",
        "kind": "scholarly",
        "citation": "Zhang et al. (2013), Peiligang chronology",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3524165/"
    },
    {
        "id": "frontiers-2021-yangshao",
        "kind": "scholarly",
        "citation": "Frontiers (2021), Yangshao chronology",
        "url": "https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2021.662391/full"
    },
    {
        "id": "cass-hongshan",
        "kind": "scholarly",
        "citation": "Chinese Academy of Social Sciences, Hongshan chronology",
        "url": "http://kaogu.cssn.cn/ywb/research_work/other_topics/201411/W020180124632420705403.pdf"
    },
    {
        "id": "haidai-longshan",
        "kind": "scholarly",
        "citation": "Haidai, Longshan chronology",
        "url": "https://www.sciencedirect.com/science/article/abs/pii/S2352409X16305648"
    },
    {
        "id": "liu-2017-liangzhu",
        "kind": "scholarly",
        "citation": "Liu et al. (2017), Liangzhu chronology",
        "url": "https://www.pnas.org/doi/10.1073/pnas.1710516114"
    },
    {
        "id": "zhang-1999-jiahu",
        "kind": "scholarly",
        "citation": "Zhang et al. (1999), Jiahu bone flutes",
        "url": "https://pubmed.ncbi.nlm.nih.gov/16862110/"
    },
    {
        "id": "mutin-2025-mehrgarh",
        "kind": "scholarly",
        "citation": "Mutin et al. (2025), re-dating Mehrgarh",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12000376/"
    },
    {
        "id": "sarkar-2016-bhirrana",
        "kind": "scholarly",
        "citation": "Sarkar et al. (2016), Bhirrana chronology",
        "url": "https://www.nature.com/articles/srep26555"
    },
    {
        "id": "asi-bhirrana-review",
        "kind": "scholarly",
        "citation": "Archaeological Survey of India, Bhirrana review",
        "url": "https://cdnbbsr.s3waas.gov.in/s3a70dc40477bc2adceef4d2c90f47eb82/uploads/2023/02/2023021535.pdf"
    },
    {
        "id": "kenoyer-2000-ravi",
        "kind": "scholarly",
        "citation": "Kenoyer (2000), Ravi Phase at Harappa",
        "url": "https://www.harappa.com/sites/default/files/pdf/Kenoyer2000_The%20Ravi%20Phase%20A%20New%20Cultural%20Manifestation%20at%20H.pdf"
    },
    {
        "id": "patel-agnihotri-lahuradewa",
        "kind": "scholarly",
        "citation": "Patel and Agnihotri, Lahuradewa environmental record",
        "url": "https://palaeontologicalsociety.in/vol67_1/10.%20JPSI-IBSV-Patel-Agnihotri.pdf"
    },
    {
        "id": "forestier-2013-hoabinhian",
        "kind": "scholarly",
        "citation": "Forestier et al. (2013), Hoabinhian chronology",
        "url": "https://sciencepress.mnhn.fr/sites/default/files/articles/pdf/comptes-rendus-palevol2013v12f1a06.pdf"
    },
    {
        "id": "ji-2016-hoabinhian",
        "kind": "scholarly",
        "citation": "Ji et al. (2016), early Hoabinhian chronology",
        "url": "https://os.pennds.org/archaeobib_filestore/pdf_articles/QI/2016_400_Jietal.pdf"
    },
    {
        "id": "higham-2015-ban-chiang",
        "kind": "scholarly",
        "citation": "Higham et al. (2015), Ban Chiang chronology",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4575132/"
    },
    {
        "id": "barker-2007-niah",
        "kind": "scholarly",
        "citation": "Barker et al. (2007), Niah Cave chronology",
        "url": "https://pubmed.ncbi.nlm.nih.gov/17161859/"
    },
    {
        "id": "zheng-2016-rice",
        "kind": "scholarly",
        "citation": "Zheng et al. (2016), early rice cultivation",
        "url": "https://www.nature.com/articles/srep28136"
    },
    {
        "id": "pico-2022-beringia",
        "kind": "scholarly",
        "citation": "Pico et al. (2022), Beringia coastal route",
        "url": "https://www.pnas.org/doi/10.1073/pnas.2206742119"
    },
    {
        "id": "waters-2019-preclovis",
        "kind": "scholarly",
        "citation": "Waters et al. (2019), pre-Clovis occupation",
        "url": "https://www.science.org/doi/10.1126/science.aat5447"
    },
    {
        "id": "bennett-2021-white-sands",
        "kind": "scholarly",
        "citation": "Bennett et al. (2021), White Sands footprints",
        "url": "https://www.science.org/doi/10.1126/science.abg7586"
    },
    {
        "id": "pigati-2023-white-sands",
        "kind": "scholarly",
        "citation": "Pigati et al. (2023), White Sands independent chronology",
        "url": "https://www.science.org/doi/10.1126/science.adh5007"
    },
    {
        "id": "madsen-2022-white-sands",
        "kind": "scholarly",
        "citation": "Madsen et al. (2022), White Sands reservoir critique",
        "url": "https://www.science.org/doi/10.1126/science.abm6987"
    },
    {
        "id": "waters-2020-clovis",
        "kind": "scholarly",
        "citation": "Waters (2020), Clovis age range",
        "url": "https://pubmed.ncbi.nlm.nih.gov/33087355/"
    },
    {
        "id": "waters-stafford-2007-clovis",
        "kind": "scholarly",
        "citation": "Waters and Stafford (2007), Clovis radiocarbon re-dating",
        "url": "https://liberalarts.tamu.edu/wp-content/uploads/sites/14/2019/09/Waters-and-Stafford-Clovis-Dating.pdf"
    },
    {
        "id": "buchanan-2021-folsom",
        "kind": "scholarly",
        "citation": "Buchanan et al. (2021), Folsom chronology",
        "url": "http://marcusjhamilton.weebly.com/uploads/2/5/5/3/25533140/buchanan_et_al_2021.pdf"
    },
    {
        "id": "cambridge-paleoindian-archaic",
        "kind": "scholarly",
        "citation": "Cambridge, Paleoindian and Archaic periods",
        "url": "https://resolve.cambridge.org/core/services/aop-cambridge-core/content/view/C86E356FC4CC78806D2E1B92E2A4F869/9781139017831c54_p923-942_CBO.pdf/paleoindian_and_archaic_periods_in_north_america.pdf"
    },
    {
        "id": "nps-archaic",
        "kind": "scholarly",
        "citation": "National Park Service, Archaic Period",
        "url": "https://www.nps.gov/articles/archaic-period.htm"
    },
    {
        "id": "encyclopedia-virginia-cactus-hill",
        "kind": "scholarly",
        "citation": "Encyclopedia Virginia, Cactus Hill",
        "url": "https://encyclopediavirginia.org/entries/cactus-hill-archaeological-site/"
    },
    {
        "id": "jenkins-paisley-geochronology",
        "kind": "scholarly",
        "citation": "Jenkins et al., Paisley Caves geochronology",
        "url": "https://pages.uoregon.edu/ftrock/pdfs/jenkins_geochronology.pdf"
    },
    {
        "id": "bradshaw-2021-sahul",
        "kind": "scholarly",
        "citation": "Bradshaw et al. (2021), Sahul occupation",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC8085232/"
    },
    {
        "id": "bowler-2003-mungo",
        "kind": "scholarly",
        "citation": "Bowler et al. (2003), Lake Mungo chronology",
        "url": "https://pubmed.ncbi.nlm.nih.gov/12594511/"
    },
    {
        "id": "ahrc-aboriginal-history",
        "kind": "scholarly",
        "citation": "Australian Human Rights Commission, Aboriginal history",
        "url": "https://bth.humanrights.gov.au/significance/historical-context-ancient-history"
    },
    {
        "id": "specht-lapita",
        "kind": "scholarly",
        "citation": "Specht, Lapita chronology",
        "url": "https://press-files.anu.edu.au/downloads/press/p61051/pdf/ch0327.pdf"
    },
    {
        "id": "wilmshurst-2011-polynesia",
        "kind": "scholarly",
        "citation": "Wilmshurst et al. (2011), Polynesian settlement chronology",
        "url": "https://faculty.washington.edu/plape/pacificarchaut12/Wilmshurst%20et%20al%202010.pdf"
    },
]

from extensions_africa import AFRICA_SOURCES  # noqa: E402
sources.extend(AFRICA_SOURCES)

# The authority behind the Languages branch: its genealogical classification, its isolate flag and
# its Most Extensive Description ranking. CC-BY 4.0, so redistributable inside the app with
# attribution -- which is why it was chosen over Ethnologue, whose terms cap fair use at a thousand
# words per project and require a commercial licence to ship.
sources.append({
    "id": "glottolog-5-3",
    "kind": "reference",
    "citation": ("Hammarström, Forkel, Haspelmath & Bank (2026), Glottolog 5.3, "
                 "Max Planck Institute for Evolutionary Anthropology"),
    "url": "https://glottolog.org/",
    "note": ("Genealogical classification, languoid level, isolate status and documentation depth. "
             "Dates are not from Glottolog, which dates nothing; see each entity's date note."),
})
# The roster itself, for the rows Glottolog could not classify: reconstructions, which have no
# glottocode because they are not attested varieties, and a few ancient stages whose codes did not
# resolve. Placement for those came from the research passes rather than from Glottolog.
sources.append({
    "id": "roster-tier-1",
    "kind": "reference",
    "citation": ("History & Prehistory language roster (2026), compiled from Glottolog 5.3, "
                 "Wikipedia, Britannica and regional scholarship across fourteen research passes"),
    "url": "https://glottolog.org/",
    "note": ("Used where Glottolog has no entry: reconstructed proto-languages and attested stages "
             "without a glottocode. Placement and dates are the roster's, not Glottolog's."),
})
from extensions_ages import AGES_SOURCES  # noqa: E402
sources.extend(AGES_SOURCES)
from extensions_neolithic import NEOLITHIC_SOURCES  # noqa: E402
sources.extend(NEOLITHIC_SOURCES)
from extensions_europe import EUROPE_SOURCES  # noqa: E402
sources.extend(EUROPE_SOURCES)
from extensions_americas import AMERICAS_SOURCES  # noqa: E402
sources.extend(AMERICAS_SOURCES)
from extensions_central_asia import CENTRAL_ASIA_SOURCES  # noqa: E402
from extensions_central_asia_medieval import CENTRAL_ASIA_MEDIEVAL_SOURCES  # noqa: E402
from extensions_iran_islamic import IRAN_ISLAMIC_SOURCES  # noqa: E402
from citations_cross_region import CROSS_REGION_SOURCES  # noqa: E402
from extensions_phoenicia import PHOENICIA_SOURCES  # noqa: E402
from extensions_vedic import VEDIC_SOURCES  # noqa: E402
from rival_claims import RIVAL_SOURCES  # noqa: E402
from misconception_migration import MISCONCEPTION_SOURCES  # noqa: E402
from misconception_migration import LEGENDARY_SOURCES  # noqa: E402
from promoted_sourcing import PROMOTED_SOURCES  # noqa: E402
from china_legendary import CHINA_LEGENDARY_SOURCES  # noqa: E402
from upgrade_sources import UPGRADE_SOURCES  # noqa: E402
from co_rulers import CO_RULER_SOURCES  # noqa: E402
sources.extend(CENTRAL_ASIA_SOURCES)
sources.extend(CENTRAL_ASIA_MEDIEVAL_SOURCES)
sources.extend(IRAN_ISLAMIC_SOURCES)
sources.extend(CROSS_REGION_SOURCES)
sources.extend(PHOENICIA_SOURCES)
sources.extend(VEDIC_SOURCES)
sources.extend(RIVAL_SOURCES)
sources.extend(MISCONCEPTION_SOURCES)
sources.extend(LEGENDARY_SOURCES)
sources.extend(PROMOTED_SOURCES)
sources.extend(CHINA_LEGENDARY_SOURCES)
# Built at runtime from docs/research/*.json, so read after the module has run.
sources.extend(reigns_from_research.RESEARCH_REIGN_SOURCES)
sources.extend(UPGRADE_SOURCES)
sources.extend(CO_RULER_SOURCES)
from extensions_seasia_oceania import SEASIA_OCEANIA_SOURCES  # noqa: E402
from extensions_indus import INDUS_SOURCES  # noqa: E402
from extensions_east_asia import EAST_ASIA_SOURCES  # noqa: E402
from extensions_west_asia import WEST_ASIA_SOURCES  # noqa: E402
from extensions_arabia import ARABIA_SOURCES  # noqa: E402
from extensions_egypt import EGYPT_SOURCES  # noqa: E402
from citations_mediterranean import MEDITERRANEAN_SOURCES  # noqa: E402
from romanisation_chinese import ROMANISATION_SOURCES  # noqa: E402
from extensions_song_era_states import SONG_ERA_SOURCES  # noqa: E402
from extensions_sea_mainland import SEA_MAINLAND_SOURCES  # noqa: E402
from extensions_sea_maritime import SEA_MARITIME_SOURCES  # noqa: E402
from extensions_mesolithic import MESOLITHIC_SOURCES  # noqa: E402
from extensions_empires import EMPIRE_SOURCES  # noqa: E402
from extensions_naming import NAMING_SOURCES  # noqa: E402
from extensions_americas_civ import AMERICAS_CIV_SOURCES  # noqa: E402
from naming_formal_historical import FORMAL_HISTORICAL_SOURCES  # noqa: E402
from naming_formal_historical_2 import NAMING_2_SOURCES  # noqa: E402
from naming_formal_historical_3 import NAMING_3_SOURCES  # noqa: E402
from naming_formal_historical_4 import NAMING_4_SOURCES  # noqa: E402
sources.extend(SEASIA_OCEANIA_SOURCES)
sources.extend(INDUS_SOURCES)
sources.extend(EAST_ASIA_SOURCES)
sources.extend(WEST_ASIA_SOURCES)
sources.extend(ARABIA_SOURCES)
sources.extend(EGYPT_SOURCES)
sources.extend(MEDITERRANEAN_SOURCES)
sources.extend(ROMANISATION_SOURCES)
sources.extend(SONG_ERA_SOURCES)
sources.extend(SEA_MAINLAND_SOURCES)
sources.extend(SEA_MARITIME_SOURCES)
sources.extend(MESOLITHIC_SOURCES)
sources.extend(EMPIRE_SOURCES)
sources.extend(NAMING_SOURCES)
sources.extend(AMERICAS_CIV_SOURCES)
sources.extend(FORMAL_HISTORICAL_SOURCES)
sources.extend(NAMING_2_SOURCES)
sources.extend(NAMING_3_SOURCES)
sources.extend(NAMING_4_SOURCES)
sources.extend(GAP_SOURCES)
from received_conventions import RECEIVED_CONVENTION_SOURCES  # noqa: E402
sources.extend(RECEIVED_CONVENTION_SOURCES)

with open(DATA / "sources.json", "w") as f:
    json.dump({"schema_version": SCHEMA_VERSION, "dataset_version": DATASET_VERSION,
               "generated_at": _GENERATED_AT, "sources": sources}, f, indent=2, ensure_ascii=False)
    f.write("\n")
print(f"Wrote sources.json — {len(sources)} sources")

# A worklist rather than a footnote: eighteen languages whose start year is a regional settlement
# estimate standing in for a divergence date nobody has produced. Published as a theme so the set
# can be opened and worked through, and so it shrinks visibly as real dates land.
from author_languages import NEEDS_DATING_REVIEW as _NEEDS_DATING
if _NEEDS_DATING:
    themes.append({
        "id": "needs-dating-review",
        "name": "Needs Dating Review",
        "description": (
            "Languages whose start year is a regional settlement estimate rather than a date for "
            "the language itself. Where no divergence estimate exists, the research fell back to "
            "when the region was first settled, which says when people arrived and nothing about "
            "when the language began. Held here as a worklist."),
        "entity_ids": list(_NEEDS_DATING),
    })

with open(DATA / "themes.json", "w") as f:
    _n = _rewrite_refs(themes, _ID_REDIRECTS)
    if _n:
        print(f"normalize_ids: rewrote {_n} id reference(s) in themes")
    json.dump(_envelope("themes", themes), f, indent=2, ensure_ascii=False)
print(f"Wrote themes.json — {len(themes)} themes")


# =============================================================================
# REFERENCE FRAMES (novice anchors)
# =============================================================================

frames = [
    # Deep-time anchors.
    #
    # The other eight sets are cultural traditions and none of them reaches
    # before the Holocene, so 42 entities older than 10,000 BCE had no anchor
    # at all - the set covered 0.35% of the dataset's span. A reader looking at
    # the Acheulean got no help placing it.
    #
    # These are scale references rather than landmarks: nobody grew up knowing
    # when the Last Glacial Maximum was, so the anchor has to do more work.
    {"id": "lucy", "name": "Lucy walks upright", "year": -3178051, "anchor_set": "deep-time",
     "summary": "The Australopithecus afarensis skeleton from Hadar in Ethiopia. Bipedal, small-brained, and 600,000 years before anyone knapped a stone.",
     "entity_id": "africa.prehistory.hadar"},
    {"id": "laetoli-footprints", "name": "Oldest footprints", "year": -3658051, "anchor_set": "deep-time",
     "summary": "Hominins walked across wet volcanic ash at Laetoli in Tanzania and the prints set. The oldest direct record of upright walking, older than any stone tool.",
     "entity_id": "africa.prehistory.laetoli"},
    {"id": "first-stone-tools", "name": "First stone tools", "year": -3298051, "anchor_set": "deep-time",
     "summary": "The oldest known deliberately knapped stone, at Lomekwi 3 in Kenya. Half a million years before the oldest fossil of our own genus.",
     "entity_id": "global.prehistory.firsts.stone-knapping"},
    {"id": "first-homo", "name": "First Homo fossil", "year": -2798051, "anchor_set": "deep-time",
     "summary": "The oldest fossil attributed to our genus, from Ledi-Geraru in Ethiopia.",
     "entity_id": "global.prehistory.hominins"},
    {"id": "first-fire", "name": "Controlled fire", "year": -998051, "anchor_set": "deep-time",
     "summary": "The earliest secure evidence of fire kept and used on purpose, at Wonderwerk Cave in South Africa.",
     "entity_id": "global.prehistory.firsts.controlled-fire"},
    {"id": "first-sapiens", "name": "First Homo sapiens", "year": -313050, "anchor_set": "deep-time",
     "summary": "The earliest fossils of our own species, from Jebel Irhoud in Morocco. Roughly a tenth of the way back to the first stone tools.",
     "entity_id": "global.prehistory.hominins.homo-sapiens"},
    {"id": "neanderthal-extinction", "name": "Neanderthals disappear", "year": -38051, "anchor_set": "deep-time",
     "summary": "The last traces of Neanderthals, after some 360,000 years across Europe and western Asia.",
     "entity_id": "global.prehistory.hominins.homo-neanderthalensis"},
    {"id": "last-glacial-maximum", "name": "Last Glacial Maximum", "year": -24050, "anchor_set": "deep-time",
     "summary": "The coldest point of the last Ice Age, when ice sheets reached their greatest extent and sea level was about 120 m lower than today.",
     "entity_id": "global.paleolithic"},
    {"id": "holocene-start", "name": "Start of the Holocene", "year": -9750, "anchor_set": "deep-time",
     "summary": "The end of the last Ice Age and the start of the present geological epoch, 11,700 years before 1950. Farming begins within two thousand years of it, nearly everywhere independently.",
     "entity_id": "global.neolithic"},

    # Western anchors
    {"id": "life-jesus", "name": "Life of Jesus", "year": -4, "end_year": 30, "anchor_set": "western",
     "summary": "Traditional dates for the life of Jesus of Nazareth."},
    {"id": "fall-rome-west", "name": "Fall of Western Rome", "year": 476, "anchor_set": "western",
     "summary": "Deposition of Romulus Augustulus; conventional end of the Western Roman Empire.",
     "entity_id": f"{rome}.empire"},
    {"id": "fall-constantinople", "name": "Fall of Constantinople", "year": 1453, "anchor_set": "western",
     "summary": "Ottoman conquest ends the Byzantine Empire; conventional end of the Middle Ages.",
     "entity_id": "global.multi-regional.ottoman.mehmed2"},
    {"id": "columbus", "name": "Columbus reaches the Americas", "year": 1492, "anchor_set": "western",
     "summary": "Christopher Columbus's first landfall in the Bahamas; the beginning of sustained European contact with the Americas.",
     "entity_id": "global.multi-regional.columbus"},
    {"id": "american-revolution", "name": "American Revolution", "year": 1775, "end_year": 1783, "anchor_set": "western",
     "summary": "Colonial revolt that produced the first successful independence movement in the Americas."},
    {"id": "french-revolution", "name": "French Revolution", "year": 1789, "anchor_set": "western",
     "summary": "Overthrew the French monarchy and ancien régime; template for modern political revolutions.",
     "entity_id": "europe.western.france.revolution"},
    {"id": "ww1", "name": "World War I", "year": 1914, "end_year": 1918, "anchor_set": "global",
     "summary": "First industrialized total war; collapsed four empires (Russian, German, Austro-Hungarian, Ottoman).",
     "entity_id": "global.short-20c.ww1"},
    {"id": "ww2", "name": "World War II", "year": 1939, "end_year": 1945, "anchor_set": "global",
     "summary": "Global war fought in Europe, Asia, and the Pacific; ended with Axis defeat and the atomic bombings of Hiroshima and Nagasaki.",
     "entity_id": "global.short-20c.ww2"},

    # East Asian anchors
    {"id": "confucius", "name": "Life of Confucius", "year": -551, "end_year": -479, "anchor_set": "east-asian",
     "summary": "Life of the Chinese philosopher Kongzi."},
    {"id": "buddha", "name": "Life of the Buddha", "year": -563, "end_year": -483, "anchor_set": "south-asian",
     "summary": "Traditional dates (varies by tradition)."},
    {"id": "qin-unification", "name": "Qin Unification of China", "year": -221, "anchor_set": "east-asian",
     "summary": "Qin Shi Huangdi ended the Warring States period and founded the first unified Chinese empire.",
     "entity_id": "east-asia.china.qin.shi-huang"},
    {"id": "meiji-restoration", "name": "Meiji Restoration", "year": 1868, "anchor_set": "east-asian",
     "summary": "Ended the Tokugawa shogunate and restored imperial authority under Emperor Meiji; launched Japan's rapid modernization.",
     "entity_id": "east-asia.japan.modern.meiji"},
    {"id": "prc-founding", "name": "Founding of the PRC", "year": 1949, "anchor_set": "east-asian",
     "summary": "Mao Zedong proclaimed the People's Republic of China after Communist victory in the Chinese Civil War.",
     "entity_id": "east-asia.china.prc"},

    # Islamic anchors
    {"id": "muhammad", "name": "Life of Muhammad", "year": 570, "end_year": 632, "anchor_set": "islamic",
     "summary": "Life of the Prophet Muhammad, founder of Islam. His flight from Mecca to Medina in 622 marks Year 1 of the Islamic calendar.",
     "entity_id": "west-asia.arabia.rise-islam.muhammad"},
    {"id": "hijra", "name": "The Hijra (Muhammad's migration)", "year": 622, "anchor_set": "islamic",
     "summary": "Year 1 of the Islamic calendar."},
    {"id": "sack-baghdad", "name": "Mongol Sack of Baghdad", "year": 1258, "anchor_set": "islamic",
     "summary": "Hülegü Khan's Mongols destroyed Baghdad and ended the Abbasid Caliphate; a symbolic close to the Islamic Golden Age.",
     "entity_id": "global.multi-regional.abbasid"},

    # South Asian
    {"id": "ashoka-conversion", "name": "Ashoka's conversion (Kalinga War)", "year": -261, "anchor_set": "south-asian",
     "summary": "Mauryan emperor Ashoka's remorse after the bloody conquest of Kalinga led him to embrace Buddhism and pacifism.",
     "entity_id": "south-asia.maurya.ashoka"},
    {"id": "indian-independence", "name": "Indian Independence & Partition", "year": 1947, "anchor_set": "south-asian",
     "summary": "End of the British Raj; partition into independent India and Pakistan produced one of history's largest forced migrations.",
     "entity_id": "south-asia.independence"},

    # African
    {"id": "great-pyramid", "name": "Great Pyramid of Giza built", "year": -2560, "anchor_set": "african",
     "summary": "Traditional date of the Great Pyramid of Khufu at Giza; the oldest of the Seven Wonders and the only one still standing.",
     "entity_id": "africa.nile.egypt.old-kingdom.dyn4.khufu"},
    {"id": "mansa-musa-hajj", "name": "Mansa Musa's Hajj", "year": 1324, "anchor_set": "african",
     "summary": "Mansa Musa of Mali's pilgrimage to Mecca was so lavish it crashed Egyptian gold prices for a decade.",
     "entity_id": "africa.west.mali.mansa-musa"},
    {"id": "adwa", "name": "Battle of Adwa", "year": 1896, "anchor_set": "african",
     "summary": "Ethiopian victory over Italy; kept Ethiopia the only major African state to remain uncolonized in the age of European empires.",
     "entity_id": "africa.nile.ethiopia.menelik2"},

    # Americas
    {"id": "cahokia-peak", "name": "Cahokia at peak", "year": 1100, "anchor_set": "americas",
     "summary": "Mississippian city near modern St. Louis; the largest pre-Columbian settlement in North America.",
     "entity_id": "americas.north.mississippian"},
    {"id": "aztec-fall", "name": "Fall of Tenochtitlan", "year": 1521, "anchor_set": "americas",
     "summary": "Spanish conquistadors under Cortés, allied with Tlaxcala and other indigenous nations, took the Aztec capital.",
     "entity_id": "americas.mesoamerica.aztec.moctezuma2"},
    {"id": "inca-fall", "name": "Fall of the Inca", "year": 1533, "anchor_set": "americas",
     "summary": "Pizarro executed Atahualpa; effective end of the Inca Empire, though the Vilcabamba state resisted until 1572.",
     "entity_id": "americas.andes.inca.atahualpa"},

    # Oceanic
    {"id": "polynesia-settlement", "name": "Settlement of Aotearoa (Māori)", "year": 1280, "anchor_set": "oceanic",
     "summary": "Approximate date of first Polynesian settlement of New Zealand; last major landmass on Earth to be settled by humans.",
     "entity_id": "oceania.polynesia.aotearoa"},
    {"id": "cook-first-voyage", "name": "Cook's first Pacific voyage", "year": 1768, "end_year": 1771, "anchor_set": "oceanic",
     "summary": "James Cook's HMS Endeavour voyage mapped New Zealand and the eastern coast of Australia."},

    # Global prehistoric
    {"id": "agriculture-origin", "name": "Origin of agriculture", "year": -10000, "anchor_set": "global",
     "summary": "Independent agricultural revolutions began around this time in the Fertile Crescent, China, and Mesoamerica."},
    {"id": "writing-origin", "name": "Origin of writing", "year": -3200, "anchor_set": "global",
     "summary": "Earliest known writing systems: Sumerian cuneiform and Egyptian hieroglyphs."},

    # --- Phase 0: additional anchors ---
    # Western / European
    {"id": "waterloo", "name": "Battle of Waterloo", "year": 1815, "anchor_set": "western",
     "summary": "Napoleon's final defeat; the reset point for 19th-century European order.",
     "entity_id": "europe.western.france.napoleon.waterloo"},
    # Islamic
    {"id": "fall-granada", "name": "Fall of Granada", "year": 1492, "anchor_set": "islamic",
     "summary": "End of Muslim rule in Iberia; completion of the Reconquista."},
    {"id": "siege-vienna", "name": "Siege of Vienna", "year": 1529, "anchor_set": "islamic",
     "summary": "High-water mark of Ottoman expansion into Europe under Suleiman the Magnificent."},
    # South Asian
    {"id": "mughal-founding", "name": "Founding of the Mughal Empire", "year": 1526, "anchor_set": "south-asian",
     "summary": "Babur's victory at Panipat established Mughal rule in northern India.",
     "entity_id": "south-asia.mughal.babur"},
    # East Asian
    {"id": "opium-war-1", "name": "First Opium War", "year": 1839, "end_year": 1842, "anchor_set": "east-asian",
     "summary": "British defeat of Qing China; opened the treaty-port century and marked China's decline."},
    # Global 20th–21st century
    {"id": "hiroshima", "name": "Atomic bombing of Hiroshima", "year": 1945, "anchor_set": "global",
     "summary": "First combat use of a nuclear weapon; helped end WWII in the Pacific."},
    {"id": "moon-landing-anchor", "name": "Apollo 11 Moon Landing", "year": 1969, "anchor_set": "global",
     "summary": "First human landing on the Moon.",
     "entity_id": "global.short-20c.moon-landing"},
    {"id": "berlin-wall-anchor", "name": "Fall of the Berlin Wall", "year": 1989, "anchor_set": "global",
     "summary": "Symbolic end of the Cold War division of Europe.",
     "entity_id": "global.short-20c.berlin-wall-fall"},
    {"id": "nine-eleven", "name": "September 11 Attacks", "year": 2001, "anchor_set": "global",
     "summary": "al-Qaeda attacks on the United States; catalyst for the War on Terror.",
     "entity_id": "global.contemporary.september-11"},
]

with open(DATA / "reference-frames.json", "w") as f:
    _n = _rewrite_refs(frames, _ID_REDIRECTS)
    if _n:
        print(f"normalize_ids: rewrote {_n} id reference(s) in frames")
    json.dump(_envelope("frames", frames), f, indent=2, ensure_ascii=False)
print(f"Wrote reference-frames.json — {len(frames)} anchors")

print("\nAll files written to", DATA)
