"""Where a language also belongs in the history columns.

A language has one home under Languages, filed by descent, and that is complete: every language has
ancestors, so all 1,157 fit there. Historical placement is different in kind -- it is selective.
Akkadian belongs beside Sumer and Babylon; Bilua, spoken by nine thousand people on Vella Lavella,
has no historical entity to sit beside, and inventing one to hold it would be worse than leaving it
under Languages alone.

So this map is deliberately short and hand-written. Two automated attempts were rejected first:

- Token overlap between language names and entity names scored about one in three. It offered
  Amharic under Mount Royal Florida, Demotic Egyptian under Anglo-Egyptian Sudan, Middle Irish under
  the Irish Free State, and Classical Chinese under the Chinese Neolithic.
- Substring matching on anchors is worse than it looks: "Aram" finds Mataram, "Han" finds Shang,
  "Frank" finds the State of Franklin, and "Slav" finds the Mamluk Slave Dynasty.

A wrong cross-parent is not a cosmetic error. It asserts that a language belongs to a polity, in a
column a reader is using to understand that polity. Absent is better than wrong.

Every id here was looked up in the dataset rather than guessed, and `extend` fails loudly if any
stops resolving.
"""

# Language name -> the historical entity it also belongs under.
# Anchored at the most specific level that is unambiguously right. Where a language spans several
# polities -- Akkadian was written for two thousand years across Akkad, Babylon and Assyria -- the
# anchor is the region rather than any one state.
CROSS_PARENTS = {
    # --- Mesopotamia ------------------------------------------------------
    "Sumerian": "west-asia.mesopotamia.sumerian",
    "Akkadian": "west-asia.mesopotamia",
    # Neither "Old Assyrian" nor "Old Babylonian Akkadian" is a roster row -- the roster treats
    # Akkadian as one language rather than splitting its dialects -- so the two Aramaic descendants
    # that ARE present take their place.
    "Jewish Babylonian Aramaic": "west-asia.mesopotamia",
    "Syriac / Assyrian Neo-Aramaic": "west-asia.mesopotamia",
    "Elamite": "west-asia.iran.elam",
    "Kassite": "west-asia.mesopotamia",
    "Hurrian": "west-asia.mesopotamia",
    "Urartian": "west-asia.anatolia",
    "Eblaite": "west-asia.mesopotamia",

    # --- Anatolia ---------------------------------------------------------
    "Hittite": "west-asia.anatolia.hittites",
    "Cuneiform Luwian": "west-asia.anatolia.hittites",
    "Hieroglyphic Luwian": "west-asia.anatolia",
    "Palaic": "west-asia.anatolia.hittites",
    "Lydian": "west-asia.anatolia",
    "Lycian": "west-asia.anatolia",
    "Carian": "west-asia.anatolia",
    "Phrygian": "west-asia.anatolia",
    "Hattic": "west-asia.anatolia",

    # --- Levant and Arabia ------------------------------------------------
    "Phoenician": "west-asia.mesopotamia.phoenicia",
    "Punic": "west-asia.mesopotamia.phoenicia",
    "Ugaritic": "west-asia.mesopotamia",
    "Biblical Hebrew": "west-asia.mesopotamia",
    "Moabite": "west-asia.mesopotamia",
    "Ammonite": "west-asia.mesopotamia",
    "Old Aramaic": "west-asia.mesopotamia",
    "Nabataean Aramaic": "west-asia.arabia",
    "Palmyrene Aramaic": "west-asia.mesopotamia",
    "Safaitic (Old North Arabian)": "west-asia.arabia",
    "Sabaean": "west-asia.arabia",
    "Classical Arabic": "west-asia.arabia",

    # --- Iran and the steppe ----------------------------------------------
    "Old Persian": "west-asia.iran.achaemenid",
    "Avestan": "west-asia.iran",
    "Middle Persian (Pahlavi)": "west-asia.iran.sasanian",
    "Parthian": "west-asia.iran",
    "Sogdian": "central-asia",
    "Bactrian": "central-asia",
    "Khotanese Saka": "central-asia.saka",
    "Scythian": "central-asia",
    "Tocharian A": "central-asia",
    "Tocharian B": "central-asia",

    # --- Egypt and Nubia ---------------------------------------------------
    "Old Egyptian": "africa.nile.egypt",
    "Middle Egyptian": "africa.nile.egypt",
    "Late Egyptian": "africa.nile.egypt",
    "Demotic Egyptian": "africa.nile.egypt",
    "Coptic": "africa.nile.egypt",
    "Meroitic": "africa.nile.kush",
    "Old Nubian": "africa.nile.kush",
    "Ge'ez": "africa.nile.aksum",

    # --- Greece and Rome ---------------------------------------------------
    "Mycenaean Greek": "europe.mediterranean.greece",
    "Ancient Greek (Attic)": "europe.mediterranean.greece",
    "Koine Greek": "europe.mediterranean.rome.empire",
    "Medieval (Byzantine) Greek": "europe.mediterranean.byzantine",
    "Old Latin": "europe.mediterranean.rome",
    "Classical Latin": "europe.mediterranean.rome",
    "Late/Vulgar Latin": "europe.mediterranean.rome.empire",
    "Etruscan": "europe.mediterranean",
    "Oscan": "europe.mediterranean",
    "Umbrian": "europe.mediterranean",
    "Faliscan": "europe.mediterranean.rome",
    "Ancient Macedonian": "europe.mediterranean.macedon",

    # --- South and Southeast Asia -----------------------------------------
    "Vedic Sanskrit": "south-asia",
    "Classical Sanskrit": "south-asia.maurya",
    "Pali": "south-asia.maurya",
    "Tamil": "south-asia",
    "Old Tamil": "south-asia",
    "Old Khmer": "southeast-asia.mainland.khmer",
    "Old Javanese (Kawi)": "southeast-asia.maritime",
    "Old Mon": "southeast-asia.mainland",

    # --- East Asia ---------------------------------------------------------
    "Old Chinese": "east-asia.china",
    "Classical Chinese (Literary Chinese / wenyanwen)": "east-asia.china",
    "Middle Chinese": "east-asia.china.tang",
    "Old Japanese": "east-asia.japan.nara",
    "Classical Japanese (Bungo)": "east-asia.japan.heian",
    "Old Korean": "east-asia.korea",
    "Middle Korean": "east-asia.korea",
    "Jurchen": "east-asia.china.jin-jurchen",
    "Khitan": "east-asia.china.liao",
    "Tangut": "east-asia.china",
    "Old Tibetan": "central-asia.tibet.empire",
    "Classical Tibetan": "central-asia.tibet.empire",
    "Classical Mongolian": "central-asia.mongol-empire",

    # --- Europe, medieval --------------------------------------------------
    "Gothic": "europe.eastern",
    "Old Norse": "europe.western",
    "Old English": "europe.western.anglo-saxon-england",
    "Old Irish": "europe.western",
    "Primitive Irish (Ogham)": "europe.western",
    "Old Church Slavonic": "europe.eastern",
    "Church Slavonic": "europe.eastern",
    "Medieval Latin": "europe.western",
    "Classical Armenian (Grabar)": "west-asia.anatolia",

    # --- The Americas ------------------------------------------------------
    "Classical Nahuatl": "americas.mesoamerica.aztec",
    "Classical Maya (Ch'olti'an)": "americas.mesoamerica.maya",
    "Colonial Yucatec Maya": "americas.mesoamerica.maya",
    "Classical K'iche'": "americas.mesoamerica.maya",
    "Classical Zapotec": "americas.mesoamerica.zapotec",
    "Classical Mixtec": "americas.mesoamerica",
    "Classical Quechua": "americas.andes.inca",
    "Aymara": "americas.andes",
}


def extend(E, entities, tree):
    """Attach cross_parent_ids to the language rows named above."""
    ids = {e["id"] for e in entities}
    by_name = {}
    for row in tree:
        if not row.get("is_family_node") and row.get("name"):
            by_name.setdefault(row["name"], row)

    missing_anchor = sorted({a for a in CROSS_PARENTS.values() if a not in ids})
    if missing_anchor:
        raise KeyError(f"cross_parents: anchor(s) no longer exist: {missing_anchor}")

    missing_lang = sorted(n for n in CROSS_PARENTS if n not in by_name)
    applied = 0
    for name, anchor in CROSS_PARENTS.items():
        row = by_name.get(name)
        if row is None:
            continue
        row.setdefault("cross_parent_ids", [])
        if anchor not in row["cross_parent_ids"]:
            row["cross_parent_ids"].append(anchor)
            applied += 1

    print(f"cross_parents: {applied} language(s) also placed in the history columns"
          + (f"; {len(missing_lang)} named language(s) not in the roster: {missing_lang[:6]}"
             if missing_lang else ""))
    return missing_lang
