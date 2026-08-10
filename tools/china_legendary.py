"""The legendary age before the Xia, and Erlitou moved to where its argument lives.

Issue #25: `east-asia.china.legendary` was "Legendary & Neolithic China", −5000..−1600,
with no summary, no date note and no source, sitting almost entirely inside
`east-asia.china.neolithic` and existing to hold one child. Its name welded a
historiographic category onto an archaeological one — the exact conflation the Xia
dispute entity was added to keep apart — and its only child, Erlitou, was
`foundational` while the container was `intermediate`, so the child outranked its parent.

Rebuilt as what it actually is: **a tradition, presented as a tradition.**

The traditional chronology is worth recording precisely because of how it was made. The
Yellow Emperor's dates of 2697–2597 BCE were **calculated by seventeenth-century Jesuit
missionaries** working from Chinese chronicles — Martino Martini first, later reproduced
by Mayers (1874) and Giles (1892) — and entered modern Chinese usage through Sun Yat-sen
and the 1938 *Cihai*. So the canonical "traditional" dates for China's founding figures
are a European reconstruction subsequently adopted in China. That is a fact about
historiography, not about the third millennium BCE, and the dataset should say so rather
than print the years as if they were findings.

There is also no single canonical list. **Five different sets of the Three Sovereigns**
appear in Han-dynasty classics, and the Five Emperors have at least five competing
groupings. This module authors the Five Emperors as the Shiji gives them, because that is
the list with dates attached, and does **not** invent three Sovereign entities by picking
one list of five and presenting it as the tradition. The disagreement is recorded instead.

**Erlitou moves to `east-asia.china.xia`**, which already carries a caveat about the
Chronology Project assigning every Erlitou phase to the Xia. That is where the argument
lives, so that is where the evidence belongs.

The move also exposes something the old filing hid. Erlitou's dates here, −1750..−1520,
come from the 2007 accelerator mass spectrometry redating, and they **do not fit inside
the Xia**, which conventionally ends around 1600 BCE. The redating pushed the site later
and made the Xia identification harder, not easier: as one account of the work put it,
Erlitou was still developing when the Xia was supposedly ending. Filed under Xia with the
dates left as they are, that tension is visible in the readout instead of being smoothed
away by a container broad enough to swallow it.
"""

S_BERKSHIRE = "berkshire-three-sovereigns"
S_NWE_SANHUANG = "nwe-three-sovereigns"
S_SINICA_YELLOW = "sinica-yellow-emperor-era"
S_BRIT_ERLITOU = "britannica-erlitou-culture"
S_RADIOCARBON_ERLITOU = "radiocarbon-erlitou-dating"
S_WIKI_ERLITOU = "wikipedia-erlitou-culture"

CHINA_LEGENDARY_SOURCES = [
    {"id": S_BERKSHIRE, "kind": "reference",
     "citation": "'Three Sovereigns and Five Emperors', Encyclopedia of China "
                 "(Berkshire Publishing)",
     "url": "https://www.berkshirepublishing.com/ecph-china/2018/01/13/"
            "three-sovereigns-and-five-emperors/",
     "note": "Records five different lists of the Three Sovereigns in Han-dynasty "
             "classics and at least five competing groupings of the Five Emperors."},
    {"id": S_NWE_SANHUANG, "kind": "reference",
     "citation": "'Three Sovereigns and Five Emperors', New World Encyclopedia",
     "url": "https://www.newworldencyclopedia.org/entry/"
            "Three_Sovereigns_and_Five_Emperors",
     "note": "Places the mythological rulers c.2852-2205 BCE, preceding the Xia, and "
             "gives the Shiji list of the Five Emperors."},
    {"id": S_SINICA_YELLOW, "kind": "scholarly",
     "citation": "'The Origin of the Yellow Emperor Era Chronology', Institute of "
                 "History and Philology, Academia Sinica",
     "url": "https://www11.ihp.sinica.edu.tw/storage/w2_file/1097kaBVwNb.pdf",
     "note": "Traces the 2697 BCE accession date to Jesuit calculation from Chinese "
             "chronicles, reproduced by Mayers (1874) and Giles (1892)."},
    {"id": S_BRIT_ERLITOU, "kind": "reference",
     "citation": "'Erlitou culture', Encyclopaedia Britannica",
     "url": "https://www.britannica.com/topic/Erlitou-culture",
     "note": "The first state-level society in China, with palatial buildings, royal "
             "tombs and advanced bronze technology; its remains are taken as correlates "
             "of the Xia."},
    {"id": S_RADIOCARBON_ERLITOU, "kind": "scholarly",
     "citation": "'14C Dating of the Erlitou Site', Radiocarbon (Cambridge University "
                 "Press)",
     "url": "https://www.cambridge.org/core/journals/radiocarbon/article/abs/"
            "14c-dating-of-the-erlitou-site/475359D750D8F9AE70E5126CF4744A4C",
     "note": "Wiggle-matched radiocarbon work under the Xia-Shang-Zhou Chronology "
             "Project; the site's dating was contested for decades before it."},
    {"id": S_WIKI_ERLITOU, "kind": "reference",
     "citation": "'Erlitou culture', Wikipedia",
     "url": "https://en.wikipedia.org/wiki/Erlitou_culture",
     "note": "States both positions: Chinese archaeologists generally identify Erlitou "
             "as Xia, while others note no contemporary writing exists to confirm it. "
             "Wikipedia-tier; used for the shape of the dispute, not for dates."},
]

# The Shiji's Five Emperors, with the traditional regnal dates attached to them.
# Gaps between reigns are in the tradition itself and are left rather than closed.
FIVE_EMPERORS = [
    ("huangdi", "Yellow Emperor", "黃帝", -2697, -2597,
     "Traditionally united the Yellow River tribes and founded Chinese statecraft; "
     "Sima Qian began his history here.", ["Huangdi", "Xuan Yuan", "Yellow Thearch"]),
    ("zhuanxu", "Zhuanxu", "顓頊", -2514, -2436,
     "Grandson of the Yellow Emperor in the traditional genealogy, credited with "
     "reforming religious observance.", ["Gaoyang"]),
    ("emperor-ku", "Emperor Ku", "帝嚳", -2436, -2366,
     "Credited in the tradition with regulating the calendar and the seasons.",
     ["Gaoxin"]),
    ("emperor-yao", "Emperor Yao", "堯", -2358, -2258,
     "The model sage-ruler of Confucian political thought, remembered for passing the "
     "throne to the ablest man rather than to his son.", None),
    ("emperor-shun", "Emperor Shun", "舜", -2255, -2195,
     "Chosen by Yao over his own son and held up ever after as proof that virtue should "
     "outrank birth; traditionally passed the throne to Yu, founder of the Xia.", None),
]

LEGENDARY_ID = "east-asia.china.legendary"
XIA_ID = "east-asia.china.xia"
ERLITOU_OLD = "east-asia.china.legendary.erlitou"


def extend(E, entities):
    from builders import make_builders

    by_id = {e["id"]: e for e in entities}
    for required in (LEGENDARY_ID, XIA_ID, ERLITOU_OLD):
        if required not in by_id:
            raise KeyError(f"china_legendary: {required} not found")

    R, _, _, _, _, _ = make_builders(E, id_prefix=LEGENDARY_ID)

    # ── the container, rebuilt as a tradition ────────────────────────────────
    node = by_id[LEGENDARY_ID]
    node["name"] = "Legendary Age (Three Sovereigns & Five Emperors)"
    node["start_year"] = -2852
    node["end_year"] = -2070
    node["tier"] = "foundational"
    node["date_precision"] = "traditional"
    node["start_dating_method"] = "received"
    node["end_dating_method"] = "received"
    node["standing"] = "traditional"
    node["native_name"] = "三皇五帝"
    node["summary"] = (
        "The sage-rulers of Chinese tradition, placed before the Xia: god-kings credited "
        "with agriculture, medicine, writing and silk, then five emperors held up for "
        "millennia as the model of virtuous rule.")
    node["date_note"] = (
        "Traditional bounds, not findings. The tradition has no single canonical form — "
        "five different lists of the Three Sovereigns appear in Han-dynasty classics, and "
        "the Five Emperors have as many competing groupings. Only the Five Emperors are "
        "authored beneath, because theirs is the list carrying dates; picking one of five "
        "Sovereign lists and presenting it as the tradition would misrepresent it.")
    node["source_ids"] = sorted(set(node.get("source_ids", [])) |
                                {S_BERKSHIRE, S_NWE_SANHUANG})
    caveats = list(node.get("caveats", []))
    for kind, text, warrant in [
        ("contested-existence",
         "These are mythological figures. The tradition is real and consequential; the "
         "rulers are not attested archaeologically.",
         [S_BERKSHIRE, S_NWE_SANHUANG]),
        ("naming-confusion",
         "The regnal dates were calculated by 17th-century Jesuits from Chinese "
         "chronicles, then adopted in China via Sun Yat-sen and the 1938 Cihai.",
         [S_SINICA_YELLOW]),
    ]:
        assert len(text) <= 200, f"caveat is {len(text)} chars, max 200"
        if not any(c["text"] == text for c in caveats):
            caveats.append({"kind": kind, "text": text, "source_ids": warrant})
    node["caveats"] = caveats

    for slug, name, native, start, end, summary, aliases in FIVE_EMPERORS:
        R(slug, name, LEGENDARY_ID, start, end, "intermediate",
          summary=summary, aliases=aliases, native=native,
          date_precision="traditional",
          start_dating_method="received",
          end_dating_method="received",
          standing="traditional",
          source_ids=[S_NWE_SANHUANG, S_SINICA_YELLOW],
          caveats=[{"kind": "contested-existence",
                    "text": "A legendary figure. The dates are traditional, and were "
                            "fixed in their modern form by Jesuit calculation from "
                            "Chinese chronicles.",
                    "source_ids": [S_SINICA_YELLOW]}])

    # ── Erlitou, moved to where the argument about it lives ──────────────────
    erlitou = by_id[ERLITOU_OLD]
    erlitou["parent_id"] = XIA_ID
    # -1750..-1520 sits outside the Xia's conventional -2070..-1600, and that is the
    # point rather than a defect: the 2007 redating pushed the site later and made the
    # identification harder.
    erlitou["allow_outside_parent_dates"] = True
    prior = (erlitou.get("date_note") or "").strip()
    extra = (
        "These are the 2007 accelerator-mass-spectrometry figures. Earlier radiocarbon "
        "work gave c.1900-1500 BCE and Britannica still prints 1900-1350. The redating "
        "matters for the Xia question in the opposite direction to the one usually "
        "assumed: it pushes Erlitou later, so the site was still developing when the Xia "
        "is conventionally said to have ended, which makes identifying the two harder.")
    if extra not in prior:
        erlitou["date_note"] = f"{prior} {extra}".strip()
    erlitou["source_ids"] = sorted(set(erlitou.get("source_ids", [])) |
                                   {S_BRIT_ERLITOU, S_RADIOCARBON_ERLITOU})
    ecav = list(erlitou.get("caveats", []))
    etext = ("Chinese archaeologists generally read Erlitou as the Xia's material "
             "remains. No contemporary writing confirms it — the earliest Chinese script "
             "is late Shang.")
    assert len(etext) <= 200, f"{len(etext)} chars"
    if not any(c["text"] == etext for c in ecav):
        ecav.append({"kind": "contested-existence", "text": etext,
                     "source_ids": [S_WIKI_ERLITOU, S_BRIT_ERLITOU]})
    erlitou["caveats"] = ecav

    print(f"China legendary age: rebuilt as a tradition, {len(FIVE_EMPERORS)} emperors "
          f"authored, Erlitou moved to the Xia")
