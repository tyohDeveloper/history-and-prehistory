"""Move three facts out of a dead field and into the one that renders.

`misconceptions` was a `list[str]` on the entity, populated for exactly three
entities, schema-valid, and **referenced nowhere in `src/main.ts`**. Meanwhile
`caveats` -- 175 entries, with a `misconception` kind among its three kinds --
renders as the "Worth knowing" block. Two mechanisms for one job, one of them
working, and three genuinely useful corrections sitting in the dead one.

The three were also unsourced, which `caveats` supports fixing via `source_ids`. All
three are now cited, and two are retyped: Ghana and Benin are `naming-confusion`
rather than `misconception`, because the reader is not wrong about history -- they are
being misled by a modern country sharing the name.

`misconceptions` is removed from the schema in the same pass, so the field cannot be
populated again by a future module that finds it in the schema and assumes it works.
"""

S_BRIT_GHANA = "britannica-ghana-empire"
S_WHE_BENIN = "worldhistory-kingdom-of-benin"
S_WHE_MAYA_GOV = "worldhistory-maya-government"
S_OUP_MAYA = "oup-maya-society-government"

MISCONCEPTION_SOURCES = [
    {"id": S_BRIT_GHANA, "kind": "reference",
     "citation": "'Ghana: historical West African empire', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/place/Ghana-historical-West-African-empire",
     "note": "Places the empire in southeastern Mauritania and part of Mali, and states "
             "directly that it should not be confused with the modern Republic of Ghana."},
    {"id": S_WHE_BENIN, "kind": "reference",
     "citation": "Mark Cartwright, 'Kingdom of Benin', World History Encyclopedia",
     "url": "https://www.worldhistory.org/Kingdom_of_Benin/",
     "note": "Locates the kingdom in what is now southern Nigeria and notes the modern "
             "state of Benin lies further west, named for the Bight of Benin."},
    {"id": S_WHE_MAYA_GOV, "kind": "reference",
     "citation": "'Maya Government', World History Encyclopedia",
     "url": "https://www.worldhistory.org/Maya_Government/",
     "note": "Each major Maya city remained an independent sovereign polity; the Maya "
             "did not unite as one empire, including during the Classic period."},
    {"id": S_OUP_MAYA, "kind": "scholarly",
     "citation": "'Society and Government', in The Ancient Maya (Oxford Academic)",
     "url": "https://academic.oup.com/book/55028/chapter-abstract/422824301",
     "note": "Shared ideology without political unification: no Maya empire comparable "
             "to Rome and no single centralised authority."},
]

# (entity id, caveat kind, text, sources). Text is capped at 200 characters by schema.
MIGRATIONS = [
    ("africa.west.ghana", "naming-confusion",
     "The Ghana Empire lay in what is now southeastern Mauritania and western Mali, "
     "about 400 miles from the modern Republic of Ghana, which took the name in 1957.",
     [S_BRIT_GHANA]),
    ("africa.west.benin", "naming-confusion",
     "The Benin Empire was in southern Nigeria, not the modern Republic of Benin. That "
     "country, formerly Dahomey, is named for the Bight of Benin.",
     [S_WHE_BENIN]),
    ("americas.mesoamerica.maya", "misconception",
     "The Maya never formed a single unified empire. They were dozens of independent "
     "city-states sharing a culture, script and calendar but no central authority.",
     [S_WHE_MAYA_GOV, S_OUP_MAYA]),
]


S_BRIT_GILGAMESH = "britannica-gilgamesh"
S_WHE_NITOCRIS = "worldhistory-nitocris"

LEGENDARY_SOURCES = [
    {"id": S_BRIT_GILGAMESH, "kind": "reference",
     "citation": "'Gilgamesh', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Gilgamesh",
     "note": "Separates the probable king of Uruk from the epic: no historical evidence "
             "supports the exploits narrated in the poems."},
    {"id": S_WHE_NITOCRIS, "kind": "reference",
     "citation": "Joshua J. Mark, 'Nitocris', World History Encyclopedia",
     "url": "https://www.worldhistory.org/Nitocris/",
     "note": "No inscription, monument or tomb; some scholars read the name as a scribal "
             "corruption of the male king Neitiqerty Siptah, others increasingly accept her."},
]

# The deleted `caveatsOf` generated a contested-existence caveat for any name
# containing "(legendary)" or "(traditional)". That code was unreachable, so the two
# entities it targeted carried no such caveat. Deleting dead code without preserving
# its intent would have quietly dropped a real hedge, so the caveats are authored here
# as data -- and sourced, which the generated version never was.
LEGENDARY_CAVEATS = [
    ("west-asia.mesopotamia.sumerian.gilgamesh",
     "Probably a real king of Uruk early in the 3rd millennium BCE, but no historical "
     "evidence supports the exploits the epic describes.",
     [S_BRIT_GILGAMESH]),
    ("africa.nile.egypt.old-kingdom.dyn6.nitocris",
     "Known only from Herodotus, Manetho and king lists — no inscription, monument or "
     "tomb. May be a corruption of the male king Neitiqerty Siptah.",
     [S_WHE_NITOCRIS]),
]


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}
    migrated = 0
    for eid, kind, text, warrant in MIGRATIONS:
        e = by_id.get(eid)
        if e is None:
            raise KeyError(f"misconception_migration: {eid} not found")
        assert len(text) <= 200, f"{eid}: caveat text is {len(text)} chars, max 200"
        # Drop the dead field and re-express it as something the reader can see.
        e.pop("misconceptions", None)
        caveats = list(e.get("caveats", []))
        if not any(c["kind"] == kind and c["text"] == text for c in caveats):
            caveats.append({"kind": kind, "text": text, "source_ids": warrant})
        e["caveats"] = caveats
        e["source_ids"] = sorted(set(e.get("source_ids", [])) | set(warrant))
        migrated += 1

    for eid, text, warrant in LEGENDARY_CAVEATS:
        e = by_id.get(eid)
        if e is None:
            raise KeyError(f"misconception_migration: {eid} not found")
        assert len(text) <= 200, f"{eid}: caveat text is {len(text)} chars, max 200"
        caveats = list(e.get("caveats", []))
        if not any(c["kind"] == "contested-existence" for c in caveats):
            caveats.append({"kind": "contested-existence", "text": text,
                            "source_ids": warrant})
            e["caveats"] = caveats
            e["source_ids"] = sorted(set(e.get("source_ids", [])) | set(warrant))
            migrated += 1

    stragglers = [e["id"] for e in entities if e.get("misconceptions")]
    if stragglers:
        raise AssertionError(
            f"misconception_migration: misconceptions still set on {stragglers}; "
            f"the field is being removed from the schema, so these would be lost")

    print(f"Misconceptions: {migrated} caveats migrated or authored, all sourced")
