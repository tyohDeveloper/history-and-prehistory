"""Wade-Giles forms for Chinese dynasties, so pre-1980s books remain searchable.

Anyone reading a book printed before about 1980 meets Ch'ing, Chou, Sung and
T'ang, and until now the dataset returned nothing for any of them. The names were
not wrong, they were simply written in the romanisation that scholarship used for
fifty years and then abandoned.

**Only the forms that actually differ are recorded.** Shang, Han, Sui, Ming and
the Three Kingdoms states Wei, Shu and Wu are spelled identically in both
systems, so an alias for them would be pure noise -- it would claim a name change
where none happened. That leaves eight dynasties where the difference is real,
and in six of those it is severe enough that a reader would not recognise the
modern form at all.

**The interesting case is Jin.** The two Jin dynasties are written with different
characters and different tones -- 晉 Jìn for 266-420 and 金 Jīn for the Jurchen
state -- but Wade-Giles renders *both* as "Chin". So the older romanisation is
strictly less able to distinguish them than the modern one is. Wade-Giles cannot
disambiguate here at all, which is why the earlier Jin gains its missing
character: 晉 is the only thing that separates the two once the Jurchen state is
added. This is the mirror image of the Japanese era problem, where romanisation
collapsed two distinct kanji; here it collapses two distinct dynasties.

**Yuan is a quieter trap.** Wade-Giles is Yüan, differing from Pinyin only by the
umlaut -- but older printing frequently dropped it, so the same book may contain
both spellings. It gets a form for the same reason the others do.

**Postal romanisation is deliberately not done here.** Peking, Nanking, Canton and
Amoy are a separate system that applies to *place* names, and the dataset
currently contains no Chinese cities -- there is nothing to attach them to. Noted
as an open issue rather than half-applied.
"""

S_LOC = "loc-chinese-romanization-table"
S_BRIT_JIN = "britannica-jin-dynasty-jurchen"
S_BRIT_FIVE = "britannica-five-dynasties"
S_XIA_WIKI = "wikipedia-xia-dynasty-romanisation"
S_NANBEI = "wikipedia-northern-southern-dynasties"

ROMANISATION_SOURCES = [
    {
        "id": S_LOC,
        "kind": "primary",
        "citation": "Library of Congress, ALA-LC Romanization Tables: Chinese",
        "url": "https://www.loc.gov/catdir/cpso/romanization/chinese.pdf",
        "note": "The authority for Wade-Giles/Pinyin correspondence. Draws its "
                "Wade-Giles forms from the 1997 ALA-LC tables and its Pinyin from "
                "Xiandai Hanyu Cidian (1983).",
    },
    {
        "id": S_BRIT_JIN,
        "kind": "reference",
        "citation": "Encyclopaedia Britannica, Jin dynasty (1115-1234)",
        "url": "https://www.britannica.com/topic/Jin-dynasty-China-Mongolia-1115-1234",
        "note": "Gives the Jurchen dynasty's Wade-Giles form as Chin -- identical to "
                "the earlier Jin, which is the collision.",
    },
    {
        "id": S_BRIT_FIVE,
        "kind": "reference",
        "citation": "Encyclopaedia Britannica, Five Dynasties",
        "url": "https://www.britannica.com/event/Five-Dynasties",
        "note": "Confirms Wade-Giles Wu-tai against Pinyin Wudai.",
    },
    {
        "id": S_XIA_WIKI,
        "kind": "reference",
        "citation": "Wikipedia, Xia dynasty",
        "url": "https://en.wikipedia.org/wiki/Xia_dynasty",
        "note": "Gives Wade-Giles Hsia. Used because the Library of Congress table "
                "does not list dynasty names as such, only the syllable "
                "correspondence hsia/xia that this follows.",
    },
    {
        "id": S_NANBEI,
        "kind": "reference",
        "citation": "Wikipedia, Northern and Southern dynasties",
        "url": "https://en.wikipedia.org/wiki/Northern_and_Southern_dynasties",
        "note": "Source for characters and Pinyin. The Wade-Giles hyphenation could "
                "not be confirmed against the Library of Congress or Britannica and "
                "is recorded as probable rather than certain.",
    },
]

# (entity id, Wade-Giles form, source, optional note)
# Only where the two systems actually differ. Shang, Han, Sui, Ming, Wei, Shu and
# Wu are identical in both and are deliberately absent.
WADE_GILES = [
    ("east-asia.china.zhou", "Chou", S_LOC, None),
    ("east-asia.china.qin", "Ch'in", S_LOC, None),
    ("east-asia.china.jin", "Chin", S_LOC,
     "Wade-Giles gives Chin for both this dynasty (晉) and the later Jurchen Jin "
     "(金), so it cannot tell them apart. The characters can."),
    ("east-asia.china.tang", "T'ang", S_LOC, None),
    ("east-asia.china.song", "Sung", S_LOC, None),
    ("east-asia.china.yuan", "Yüan", S_LOC,
     "Differs from Pinyin only by the umlaut, which older printing often dropped, "
     "so one book may use both spellings."),
    ("east-asia.china.qing", "Ch'ing", S_LOC, None),
    ("east-asia.china.north-south", "Nan-Pei Ch'ao", S_NANBEI,
     "Hyphenation not confirmed against a primary romanisation table. Older "
     "literature often calls the era the Six Dynasties instead."),
    ("east-asia.china.five-dynasties", "Wu-tai", S_BRIT_FIVE, None),
]

# Characters missing from entities that need them. The Jin is the load-bearing
# one: without 晉 there is nothing to distinguish it from the Jurchen Jin.
NATIVE = {
    "east-asia.china.jin": "晉",
    "east-asia.china.north-south": "南北朝",
    "east-asia.china.five-dynasties": "五代十國",
    "east-asia.china.legendary": None,
}


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}

    added = 0
    for eid, wg, src, note in WADE_GILES:
        e = by_id.get(eid)
        if e is None:
            continue
        forms = list(e.get("name_forms", []))
        if any(f["name"] == wg for f in forms):
            continue
        form = {
            "name": wg,
            "kind": "scholarly",
            "lang": "en",
            "to": 1982,
            "source_ids": [src],
        }
        if note is not None:
            form["note"] = note
        forms.append(form)
        e["name_forms"] = forms
        added += 1

    for eid, ch in NATIVE.items():
        e = by_id.get(eid)
        if e is None or ch is None:
            continue
        e.setdefault("native_name", ch)

    print(f"Romanisation: Wade-Giles forms on {added} Chinese dynasties")
