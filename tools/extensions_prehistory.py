"""Pilot prehistory entities.

Deliberately small. The point is not coverage — the ten regional attach points
from the gap analysis are still unwritten — but to prove end-to-end that the
schema 1.1.0 fields are authorable, validate, and reach the UI. Every field
unlocked by the builder work is exercised at least once here:

    uncertainty bounds   Oldowan, Gobekli Tepe
    dating_method        all four
    standing             consensus and superseded
    alternatives         Homo floresiensis, Monte Verde
    as_of                Monte Verde (live dispute)
    caveats              Homo floresiensis
    source_ids           all four
    date_note            all four

Dates and disputes are drawn from docs/prehistory-dating-research.md, which
carries the citations. If these look sparse against 1,305 historical entities,
that is the honest state: prehistory content is the next body of work, not
something this pilot pretends to have done.
"""

from builders import make_builders


def extend(E, glob):
    _, P, ERA, _ = make_builders(E)

    pre = f"{glob}.prehistory"
    E(pre, "era", "Human Prehistory", glob, start=-3300000, end=-3000,
      tier="foundational",
      summary="From the first stone tools to the earliest written records. Dated by "
              "measurement rather than reckoning, so quoted in years before present.",
      date_note="End is diachronous: writing appears at different times in different regions.")

    P("oldowan", "Oldowan Industry", pre, -2600000, -1700000, "foundational",
      summary="The earliest widely recognised stone tool industry, defined by simple "
              "flakes struck from cores.",
      start_year_min=-2618000, start_year_max=-2550000,
      dating_method="argon-argon",
      standing="consensus",
      date_note="Lomekwi 3 tools at 3.3 Ma are excluded by classifying them as Lomekwian "
                "rather than Oldowan, so the boundary is definitional as much as evidential.",
      source_ids=["braun-2019-bokol-dora"])

    P("gobekli-tepe", "Göbekli Tepe", pre, -9530, -8000, "foundational",
      native="Göbekli Tepe",
      summary="Monumental enclosures built by pre-agricultural communities in southeastern "
              "Anatolia, overturning the assumption that monuments require farming.",
      start_year_min=-9745, start_year_max=-9314,
      dating_method="radiocarbon-calibrated",
      standing="consensus",
      date_note="Only 11 radiocarbon dates exist. Kinzel and Clare abandoned the Layer "
                "III/II/I scheme for at least eight phases, so phase labels in older "
                "sources do not map cleanly.",
      source_ids=["dietrich-2013-gobekli"])

    P("homo-floresiensis", "Homo floresiensis", pre, -100000, -50000, "intermediate",
      aliases=["Flores hobbit"],
      summary="A small-bodied hominin known from Liang Bua cave on Flores, Indonesia.",
      dating_method="luminescence",
      standing="consensus",
      date_note="Youngest skeletal remains around 60 ka, with artefacts to about 50 ka.",
      alternatives=[{
          "label": "Original 2004 chronology",
          "standing": "superseded",
          "start_year": -18000,
          "end_year": -12000,
          "dating_method": "radiocarbon-calibrated",
          "note": "Withdrawn in 2016: the dated deposits proved to be a younger unit "
                  "unconformably overlying the remains.",
          "source_ids": ["sutikna-2016-flores"],
      }],
      caveats=[{
          "kind": "misconception",
          "text": "Often reported as surviving until 12,000 years ago. That date was "
                  "corrected to around 60,000 in 2016.",
          "source_ids": ["sutikna-2016-flores"],
      }],
      source_ids=["sutikna-2016-flores"])

    P("monte-verde", "Monte Verde II", pre, -14500, -14000, "intermediate",
      summary="A settlement site in southern Chile whose age broke the Clovis-first model "
              "of the peopling of the Americas.",
      dating_method="radiocarbon-calibrated",
      standing="consensus",
      as_of="2026-06-30",
      date_note="Under active challenge: a March 2026 reanalysis proposed a Holocene age, "
                "roughly thirty specialists rebutted it in May, and the authors replied in June.",
      alternatives=[{
          "label": "Surovell et al. 2026",
          "standing": "minority",
          "start_year": -8200,
          "end_year": -4200,
          "dating_method": "radiocarbon-calibrated",
          "note": "Argues the dated material is intrusive and the occupation is mid-Holocene.",
          "source_ids": ["surovell-2026-monte-verde"],
      }],
      source_ids=["dillehay-1997-monte-verde", "surovell-2026-monte-verde"])
