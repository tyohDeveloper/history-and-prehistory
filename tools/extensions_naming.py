"""Names: one rule, applied the same way twice, and a date that took a side.

This corrects yesterday's release, which got the principle half right and then
applied it inconsistently.

**What went wrong.** 0.18.0.0 renamed the Golden Horde to "Ulus of Jochi" on the
grounds that the common name is a 16th-century Russian coinage. That reasoning
is sound and the sources hold. But the Byzantine Empire has *exactly* the same
problem -- nobody in it ever called it Byzantine -- and it was left named
"Byzantine Empire" with the endonym as an alias. Two identical problems, two
opposite treatments, shipped in the same dataset.

Worse, the rename traded away something valuable. A reference work whose whole
job is to be looked things up in should not hide the term people arrive with.
Search still found it, but a reader *browsing* Central Asia saw a name they had
no reason to recognise.

**The rule, now stated once and applied to both.**

* `name` is the name a reader will arrive with. This is a reference tool; being
  findable and recognisable is not a compromise, it is the function.
* `native_name` is what the polity called itself, where recoverable. It renders
  directly under the title, so it is impossible to miss.
* `aliases` carry the remaining variants so search catches all of them.
* A `naming-confusion` caveat, with sources, explains what the common name gets
  wrong and who coined it.

Neutrality here does not come from suppressing the exonym. It comes from never
letting the exonym stand alone and unexplained. So the Golden Horde is the
Golden Horde again, with Ulug Ulus -- "Great State", its own name for itself --
displayed under the title, and Byzantium gets the same treatment for the first
time.

**A harder case, and a worse bug.** `east-asia.china.roc` was dated 1912-1949 as
a bare fact. But whether the Republic of China ended in 1949 is one of the most
actively contested questions in international law. The PRC's formal position is
that it ended on 1 October 1949; Taiwan's government portal states it relocated
and has exercised jurisdiction ever since; and a third academic position holds
it was never a state in its own right to begin with. Publishing 1949 with no
qualification silently adopts the first of the three.

This is a different species from the Golden Horde. Byzantium is a retrospective
mislabel of a dead polity -- nobody's interests are at stake. The ROC is a live
sovereignty dispute in which each name is official to someone, and where
`naming-confusion` would be the wrong instrument because it implies a mistake to
correct. Handled with `contested-existence` and competing dates instead.

**The three-age system.** Bronze Age and Iron Age carried no sources and, for
the Iron Age, no caveats, while the dataset applies them worldwide. Thomsen
devised the scheme in 1837 for northern European material. Connah's assessment
is blunt: applying it to African archaeology "produced little more than
confusion, whereas in the Americas or Australasia it has been irrelevant". The
user's own observation -- that these labels are Eurocentric, ubiquitous, and
flawed all at once -- is now recorded on the entities themselves.
"""

S_HERMITAGE = "hermitage-golden-horde"
S_KAZAKH_GOV = "kazakhstan-gov-ulug-ulus"
S_SPRINGER_HORDE = "springer-great-horde-agony"
S_ENCYC_BYZ = "encyclopedia-com-byzantine"
S_VANTRICHT = "van-tricht-basileia-ton-rhomaion"
S_NASER_BRILL = "naser-brill-middle-nile-three-age"
S_SPAFA = "spafa-three-age-southeast-asia"
S_TAIWAN_GOV = "taiwan-gov-history"
S_PRC_ONE_CHINA = "prc-one-china-principle"
S_BROOKINGS_ROC = "brookings-roc-cross-strait"
S_SOOCHOW_ROC = "soochow-roc-statehood"
S_IIAS_KOREA = "iias-hanguk-or-joseon"
S_MUSE_KOREA = "muse-what-is-south-korea"

NAMING_SOURCES = [
    {"id": S_HERMITAGE, "kind": "reference",
     "citation": "'The History and Culture of the Golden Horde', State Hermitage Museum",
     "url": "https://www.hermitagemuseum.org/explore/buildings/rooms/room_1694?lng=en",
     "note": "The state's own name for itself was Ulug Ulus, 'Great State' in Turkic."},
    {"id": S_KAZAKH_GOV, "kind": "reference",
     "citation": "'Kazakhstan's 750th anniversary of the Golden Horde', Government of Kazakhstan",
     "url": "https://www.gov.kz/memleket/entities/mfa-vienna/press/news/details/110329?lang=en",
     "note": "Gives Ulug Ulus as the historical name used in Turkic written sources, both "
             "inside the Horde and outside it."},
    {"id": S_SPRINGER_HORDE, "kind": "scholarly",
     "citation": "'The Agony of the Yoke: The Great Horde as a Fading Threat to Muscovite Rus', Herald of the Russian Academy of Sciences",
     "url": "https://link.springer.com/article/10.1134/S1019331622110119",
     "note": "Notes the Russian 'Great Horde' is probably a calque of the Turkic Ulug Ordu, "
             "though some historians dispute the derivation."},
    {"id": S_ENCYC_BYZ, "kind": "reference",
     "citation": "'Byzantine Empire, The', Encyclopedia.com",
     "url": "https://www.encyclopedia.com/religion/encyclopedias-almanacs-transcripts-and-maps/byzantine-empire",
     "note": "Basileia ton Rhomaion is the scholarly designation; the empire's formal name "
             "remained the Roman Empire and its subjects called themselves Romans."},
    {"id": S_VANTRICHT, "kind": "scholarly",
     "citation": "Van Tricht, 'Claiming the Basileia ton Rhomaion', SAGE (2017)",
     "url": "https://journals.sagepub.com/doi/10.1177/0971945817718651"},
    {"id": S_NASER_BRILL, "kind": "scholarly",
     "citation": "Naser, 'Walking the Line: Bronze and Iron Age as Terms in Middle Nile Valley Archaeology?', Brill",
     "url": "https://brill.com/view/journals/ow/5/1/article-p1_009.xml",
     "note": "Quotes Connah: applying the three-age model to African archaeology 'produced "
             "little more than confusion, whereas in the Americas or Australasia it has been "
             "irrelevant'. Thomsen devised it in 1837 for northern European material."},
    {"id": S_SPAFA, "kind": "scholarly",
     "citation": "'The Three-Age System: A Struggle for Southeast Asian Prehistoric Periodisation', SPAFA Journal",
     "url": "https://www.spafajournal.org/index.php/spafajournal/article/download/623/713/2181"},
    {"id": S_TAIWAN_GOV, "kind": "primary",
     "citation": "'History', Government Portal of the Republic of China (Taiwan)",
     "url": "https://www.taiwan.gov.tw/content_3.php",
     "note": "States the ROC government relocated to Taiwan in 1949 and has exercised "
             "jurisdiction there since."},
    {"id": S_PRC_ONE_CHINA, "kind": "primary",
     "citation": "'The One-China Principle and the Taiwan Issue', Government of the People's Republic of China",
     "url": "http://www.china.org.cn/english/taiwan/7956.htm",
     "note": "States the PRC replaced the ROC on 1 October 1949, 'thereby bringing the "
             "historical status of the Republic of China to an end'."},
    {"id": S_BROOKINGS_ROC, "kind": "scholarly",
     "citation": "Bush, 'The Significance of the Republic of China for Cross-Strait Relations', Brookings Institution",
     "url": "https://www.brookings.edu/articles/the-significance-of-the-republic-of-china-for-cross-strait-relations/",
     "note": "Sets out both positions and notes Beijing has a vested interest in the claim "
             "that it is the sole successor state."},
    {"id": S_SOOCHOW_ROC, "kind": "scholarly",
     "citation": "'The Republic of China's Statehood and Taiwan's Legal Status', Soochow University",
     "url": "https://scups.ppo.scu.edu.tw/upload/f20220531092634obteu1.pdf"},
    {"id": S_IIAS_KOREA, "kind": "scholarly",
     "citation": "'Hanguk or Joseon?', International Institute for Asian Studies",
     "url": "https://www.iias.asia/the-newsletter/article/hanguk-or-joseon",
     "note": "The North uses Joseon and the South uses Hanguk for the same nation. The "
             "distinction is not mirrored in English, where both become 'Korea'."},
    {"id": S_MUSE_KOREA, "kind": "scholarly",
     "citation": "'Introduction: What Is South Korea?', Project MUSE",
     "url": "https://muse.jhu.edu/pub/342/edited_volume/chapter/3003758"},
]

CHECKED = "2026-08-09"


def extend(E, entities):
    by_id = {e["id"]: e for e in entities}

    def add_caveat(e, kind, text, sources, replaces_kind=False):
        """Append a caveat, optionally superseding an earlier one of the same kind.

        Exact-text dedup is not enough when this module *rewords* a caveat a
        previous pass wrote: the Golden Horde ended up displaying two near-
        identical naming notes. Entities legitimately carry two caveats of one
        kind -- Ban Chiang has two distinct misconceptions -- so this is opt-in
        rather than automatic.
        """
        keep = []
        for c in e.get("caveats", []):
            if c.get("text") == text:
                continue
            if replaces_kind and c.get("kind") == kind:
                continue
            keep.append(c)
        e["caveats"] = keep + [{"kind": kind, "text": text, "source_ids": sources}]

    def add_sources(e, ids):
        e["source_ids"] = sorted(set(list(e.get("source_ids", [])) + ids))

    # ------------------------------------------------ correcting yesterday

    h = by_id.get("central-asia.mongol-empire.golden-horde")
    if h is not None:
        # Reverted. 0.18.0.0 made this "Ulus of Jochi", which was inconsistent
        # with how the identical Byzantine problem was already handled and hid
        # the term readers arrive with. The endonym moves to `native_name`,
        # where it renders under the title instead of replacing it.
        h["name"] = "Golden Horde"
        h["native_name"] = "Ulug Ulus"
        h["aliases"] = ["Ulus of Jochi", "Jochid ulus", "Kipchak Khanate", "Ulug Ulus"]
        h["summary"] = (
            "The Jochid inheritance of the Mongol empire, ruling the western steppe and the "
            "Rus principalities. It called itself the Great State."
        )
        add_caveat(h, "naming-confusion",
                   "'Golden Horde' is a Russian coinage first attested in the 16th century, "
                   "long after the fact. It called itself Ulug Ulus, 'Great State', and is "
                   "also known as the ulus of Jochi.",
                   [S_HERMITAGE, S_KAZAKH_GOV, S_SPRINGER_HORDE], replaces_kind=True)
        add_sources(h, [S_HERMITAGE, S_KAZAKH_GOV, S_SPRINGER_HORDE])

    b = by_id.get("europe.mediterranean.byzantine")
    if b is not None:
        b["native_name"] = "Βασιλεία τῶν Ῥωμαίων"
        b["aliases"] = sorted(set(list(b.get("aliases", [])) +
                                  ["Basileia ton Rhomaion", "Rhomania", "Byzantium"]))
        add_sources(b, [S_ENCYC_BYZ, S_VANTRICHT])

    # ---------------------------------- a live dispute, not a dead mislabel

    roc = by_id.get("east-asia.china.roc")
    if roc is not None:
        roc["native_name"] = "中華民國"
        roc["aliases"] = ["ROC", "Nationalist China", "Republican Era"]
        roc["date_precision"] = "disputed"
        roc["standing"] = "majority"
        roc["date_note"] = (
            "1912-1949 is the mainland period, not an uncontested lifespan. Whether the "
            "Republic of China ended in 1949 is a live dispute in international law: the PRC "
            "holds that it did, Taiwan's government states it relocated and has governed "
            "there ever since, and a third position holds it was a government of the state of "
            "China rather than a state in its own right."
        )
        roc["as_of"] = CHECKED
        roc["alternatives"] = [
            {"label": "Ongoing since 1912 (relocated to Taiwan in 1949)", "standing": "majority",
             "note": "Taiwan's official position: the government relocated and has exercised "
                     "jurisdiction continuously since.",
             "source_ids": [S_TAIWAN_GOV, S_BROOKINGS_ROC]},
            {"label": "Ended 1 October 1949", "standing": "majority",
             "end_year": 1949,
             "note": "The PRC's formal position, that its proclamation brought the historical "
                     "status of the ROC to an end.",
             "source_ids": [S_PRC_ONE_CHINA]},
        ]
        add_caveat(roc, "contested-existence",
                   "Whether this entity still exists is disputed between two governments. The "
                   "end date shown is the loss of the mainland, which is not the same claim as "
                   "dissolution.",
                   [S_TAIWAN_GOV, S_PRC_ONE_CHINA, S_BROOKINGS_ROC, S_SOOCHOW_ROC])
        add_sources(roc, [S_TAIWAN_GOV, S_PRC_ONE_CHINA, S_BROOKINGS_ROC, S_SOOCHOW_ROC])

    prc = by_id.get("east-asia.china.prc")
    if prc is not None:
        prc["native_name"] = "中华人民共和国"
        prc["aliases"] = ["PRC", "Communist China", "Mainland China"]
        add_sources(prc, [S_PRC_ONE_CHINA])

    k = by_id.get("east-asia.korea.divided")
    if k is not None:
        k["aliases"] = ["North Korea", "South Korea", "DPRK", "Republic of Korea"]
        k["date_note"] = (
            "The two states do not share a word for the nation they both claim. The North "
            "uses Joseon, the South uses Hanguk, and English flattens both to 'Korea', which "
            "conceals a disagreement rather than resolving it."
        )
        add_caveat(k, "naming-confusion",
                   "There is no neutral Korean term for the country. Choosing Joseon or "
                   "Hanguk takes a side; English 'Korea' only looks neutral because it "
                   "discards the distinction.",
                   [S_IIAS_KOREA, S_MUSE_KOREA])
        add_sources(k, [S_IIAS_KOREA, S_MUSE_KOREA])

    # --------------------------------- a Danish scheme applied to the world

    three_age = (
        "Thomsen devised the Stone/Bronze/Iron scheme in 1837 to order northern European "
        "material. Connah's verdict on exporting it: applying it to African archaeology "
        "'produced little more than confusion, whereas in the Americas or Australasia it has "
        "been irrelevant'."
    )
    for eid in ("global.bronze-age", "global.iron-age"):
        e = by_id.get(eid)
        if e is None:
            continue
        e["date_note"] = (e.get("date_note", "") + " " if e.get("date_note") else "") + three_age
        add_caveat(e, "naming-confusion",
                   "A northern European scheme applied worldwide. It has little utility for "
                   "sub-Saharan Africa, much of Asia and the Americas, where specialists "
                   "largely do not use it.",
                   [S_NASER_BRILL, S_SPAFA])
        add_sources(e, [S_NASER_BRILL, S_SPAFA])
