# African Prehistory — Sourced Dataset-Authoring Brief

> **Provenance.** This is the research pass behind dataset 0.6.0.0, kept in the
> repo for the same reason the regional briefs are: every number in the shipped
> data should be traceable to the page it came from. Entities authored from this
> brief live in `tools/extensions_africa.py`; sources are registered in
> `AFRICA_SOURCES` in the same file.
>
> **Not everything here was authored.** Nabta Playa and the African Humid Period
> already existed in the dataset and were left untouched. Laetoli was authored as
> a site rather than as a behavioural first, because a bipedalism threshold would
> move the app's 3.3 Ma floor onto an anatomical trait. Figures flagged below as
> `n.a.` or "not independently confirmed" were NOT shipped; where a number could
> not be defended it was carried as an `alternative` or omitted.

Prepared for `github.com/tyohDeveloper/history-and-prehistory`. Every numeric date below carries the URL of the page actually fetched during this research pass. Where a number could not be confirmed from a fetched primary/institutional source, it is marked `n.a.` with an explanation. Wikipedia is used only to locate primary literature and is never cited as the dating authority; where a number rests only on a Wikipedia paraphrase and no primary source could be independently fetched, that is flagged explicitly.

Already-existing nodes (NOT re-researched, per instructions): African Prehistory (era), Olduvai Gorge, Omo Kibish, Border Cave, Klasies River Mouth, Blombos Cave, Lomekwian, Oldowan, Acheulean, Middle Stone Age, Later Stone Age, Aterian, Still Bay, Howiesons Poort, Mousterian.

---

## THEME 1 — EARLY HOMININ / PALEOLITHIC SITES

### 1. Lake Turkana Complex (Koobi Fora / Nariokotome–Turkana Boy / Kokiselei)

**What it is / why it matters:** A cluster of fossil- and artifact-bearing localities on the eastern and western shores of Lake Turkana, Kenya, spanning roughly 4.1–0.7 Ma. It preserves the most continuous tuff-dated hominin and archaeological sequence in East Africa, including the most complete early *Homo erectus* skeleton (Turkana Boy) and the Lomekwi 3 and Kokiselei stone-tool assemblages that bracket the origin of flaked-stone technology and early bifacial shaping.

- kind: period
- region: africa
- start: ~4.10 Ma (Moiti Tuff, base of dated hominin-bearing sequence) — argon-argon/K-Ar, McDougall, "K-Ar and 40Ar/39Ar dating of the hominid-bearing Pliocene-Pleistocene sequence at Koobi Fora, Lake Turkana, northern Kenya," *GSA Bulletin* 96(2):159, https://pubs.geoscienceworld.org/gsa/gsabulletin/article-abstract/96/2/159/191263/K-Ar-and-40Ar-39Ar-dating-of-the-hominid-bearing (Moiti Tuff 4.10±0.07 Ma)
- end (for this brief's purpose, Silbo Tuff cap): 0.74±0.01 Ma — same McDougall GSA Bulletin source
- start_year_min/max: 4.10±0.07 Ma (tuff-specific, not the whole complex)
- dating_method (start boundary): argon-argon / K-Ar (tuff dating)
- dating_method (end boundary, as used for this complex's youngest tuff): argon-argon / K-Ar
- date_precision: exact (for individual tuffs); approx (for complex-wide span)
- standing: consensus (radiometric tuff framework itself is not disputed; specific fossil placements within it can be)

Key dated horizons (all argon-argon/K-Ar, McDougall GSA Bulletin, same URL): Toroto Tuff 3.32±0.02 Ma; Ninikaa Tuff 3.06±0.03 Ma; KBS Tuff 1.88±0.02 Ma; Malbe Tuff 1.86±0.02 Ma; Chari Tuff 1.39±0.02 Ma.

**Turkana Boy (KNM-WT 15000):** Reported "close to 1.6 Myr" in the original description — Brown, Harris, Leakey & Walker (1985), "Early *Homo erectus* skeleton from west Lake Turkana, Kenya," *Nature* 316:788–792, https://doi.org/10.1038/316788a0 (no explicit ± uncertainty or method stated in the fetched text of that paper). The Smithsonian's summary gives "about 1.6 million years ago" — https://humanorigins.si.edu/evidence/human-fossils/fossils/knm-wt-15000. dating_method: argon-argon (by bracketing tuffs, not direct dating of the skeleton); date_precision: approx; standing: consensus.

**Lomekwi 3 (Lomekwian tools):** 3.3 Ma — Harmand et al. (2015), "3.3-million-year-old stone tools from Lomekwi 3, West Turkana, Kenya," *Nature* 521:310–315, https://doi.org/10.1038/nature14464. The fetched excerpt did not state the specific dating method or uncertainty bound used for this figure; treat the method field as `n.a.` pending direct access to the paper's methods section. date_precision: approx; standing: consensus (site itself undisputed; note the global "Lomekwian" industry node already exists elsewhere in the dataset — this entry only concerns the Turkana-complex findspot).

**Kokiselei 6:** Bifacial (proto-Acheulean-style) shaping "before the Acheulean," ~1.8 Ma, reported via Journal of Human Evolution-adjacent literature (Lepre, Roche, Kent et al.); the specific paper URL fetched (https://www.sciencedirect.com/science/article/abs/pii/S0047248421001135) did not resolve to a confirmable abstract in this pass — mark exact citation as `n.a.` pending re-fetch; treat 1.8 Ma as approx/contested-attribution pending confirmation.

**Misconception to flag:** Popular sources often treat "Lake Turkana" as a single site; it is a multi-locality complex (Koobi Fora on the east side, Nariokotome/Kokiselei on the west) with different tuff sequences and should not be dated as one uniform horizon.

**Literature-moved flag:** None specific to this pass beyond ordinary refinement of the tuff sequence; the underlying K-Ar/Ar-Ar framework has been stable since the 1980s–2000s.

---

### 2. Sterkfontein / Cradle of Humankind

**What it is / why it matters:** A dolomitic cave system in Gauteng, South Africa, yielding *Australopithecus africanus* ("Mrs. Ples," Sts 5) and *Australopithecus prometheus* ("Little Foot," StW 573), among the richest early-hominin assemblages in Africa. It is also the site of the most actively contested absolute chronology in African paleoanthropology.

- kind: period
- region: africa
- standing: **contested** (active, unresolved, multi-decade dating dispute — flag prominently)

**Little Foot (StW 573), Member 2 / Silberberg Grotto:**
- Cosmogenic nuclide (26Al/10Be) isochron burial age: 3.67±0.16 Ma — Granger, Gibbon, Kuman, Clarke, Bruxelles & Caffee (2015), "New cosmogenic burial ages for Sterkfontein Member 2 Australopithecus and Member 5 Oldowan," *Nature* 522:85–88, summarized at https://pubmed.ncbi.nlm.nih.gov/25830884/ and https://www.purdue.edu/newsroom/releases/2015/Q2/new-instrument-dates-old-skeleton-little-foot-3.67-million-years-old.html. dating_method: cosmogenic. date_precision: approx (±0.16 Ma).
- **Competing** U-Pb flowstone dates: 2.17±0.17 Ma and 2.24(+0.09/−0.07) Ma — Walker, Pickering & Kramers, "U-Pb Isotopic Age of the StW 573 Hominid from Sterkfontein, South Africa," *Science*, https://www.science.org/doi/10.1126/science.1132916. dating_method: uranium-series.
- Bruxelles et al. (2014), "Stratigraphic analysis of the Sterkfontein StW 573 *Australopithecus* skeleton and implications for its age," https://pubmed.ncbi.nlm.nih.gov/24698198/, argues the flowstone dates are minimum ages only, and the true age is likely older, given complex void-filling stratigraphy.
- Ongoing exchange: "Reply to Granger et al.: Multiple, independent lines of evidence suggest Sterkfontein is less than 2.8 My old," *PNAS* (2023), https://www.pnas.org/doi/10.1073/pnas.2301351120, disputes the cosmogenic age.
- A 2024 biochronological paper independently supports ~3.6 Ma: https://pmc.ncbi.nlm.nih.gov/articles/PMC11624294/ ("A biochronological date of 3.6 million years for 'Little Foot' (StW 573)").

**Member 4 (*A. africanus*, incl. Mrs. Ples):**
- Cosmogenic dating (2022): lower-middle Member 4 = 3.41±0.11 Ma; upper-middle = 3.49±0.19 Ma; Jacovec Cavern = 3.61±0.09 Ma — Granger et al. (2022), *PNAS*, https://pubmed.ncbi.nlm.nih.gov/35759668/. dating_method: cosmogenic.
- **Competing** multidisciplinary U-Pb + ESR + paleomagnetism age: 2.61–2.07 Ma — Pickering & Herries (2020), "A new multidisciplinary age of 2.61–2.07 Ma for the Sterkfontein Member 4 australopiths," https://opal.latrobe.edu.au/articles/chapter/A_new_multidisciplinary_age_of_2_61_2_07_Ma_for_the_Sterkfontein_Member_4_australopiths/28432415. dating_method: uranium-series + esr + magnetostratigraphy (combined).
- Original 2010 U-Pb reappraisal: Member 2 = 2.8±0.28 to 2.6±0.30 Ma; Member 4 = 2.65±0.30 to 2.01±0.05 Ma — Pickering & Kramers (2010), "Re-appraisal of the stratigraphy and determination of new U-Pb dates for the Sterkfontein hominin site, South Africa," https://pubmed.ncbi.nlm.nih.gov/20605190/.

date_precision: contested/approx throughout, given the ~1.3 million-year gap between competing chronologies for the same deposits.

**Dispute summary (report exactly):** Two independent dating methods — cosmogenic nuclide burial dating (favoring ~3.4–3.7 Ma for both Member 2 and Member 4) versus U-Pb flowstone/ESR/paleomagnetic dating (favoring ~2.0–2.6 Ma) — disagree by roughly 1–1.5 million years for the same deposits. This is not resolved as of the most recent fetched sources (2022–2024). Any dataset entry MUST state both figures and flag "contested," not present either as settled consensus.

**Misconception to flag:** Popular summaries often quote a single number (commonly "3.67 Ma" for Little Foot, following the loudest recent headline) without noting the still-active U-Pb-based counter-chronology.

**Literature-moved flag:** Yes — active back-and-forth as recently as 2022–2024 (Granger et al. 2022 *PNAS*; Frost et al. reply 2023 *PNAS*; Thackeray/Dykes biochronology 2023–2024).

---

### 3. Swartkrans

**What it is / why it matters:** A cave in the Cradle of Humankind, South Africa, with the earliest well-dated occurrence of *Paranthropus robustus* and among the earliest Oldowan-type stone tools in southern Africa, alongside early evidence for possible hominin fire use.

- kind: period
- region: africa
- start (Member 1, Lower Bank): 2.22±0.09 Ma — Kuman et al. (2021), "A new absolute date from Swartkrans Cave for the oldest occurrences of *Paranthropus robustus* and Oldowan stone tools in South Africa," https://pubmed.ncbi.nlm.nih.gov/34020297/. This is stated to agree within 1σ with an independent U-Pb flowstone age of 2.25±0.08 Ma (same source).
- dating_method (start): cosmogenic (26Al/10Be isochron burial dating), cross-checked with uranium-series
- Member 1, Hanging Remnant bracket: U-Pb 2.248±0.052 Ma (older) to capping flowstone 1.80±0.01 Ma (younger) — same Kuman et al. 2021 source.
- Member 3: cosmogenic burial age 0.96±0.09 Ma — Granger et al., "Cosmogenic nuclide burial dating of hominin-bearing Pleistocene cave deposits at Swartkrans, South Africa," https://ui.adsabs.harvard.edu/abs/2014QuGeo..24...10G/abstract. dating_method (end, Member 3): cosmogenic.
- date_precision: exact (isochron and U-Pb both give tight bounds); standing: consensus (post-2014/2021 absolute dating superseded older faunal-only estimates).

**Misconception to flag:** Older faunal-correlation dates (e.g., ~2–1 Ma from bovids, Vrba 1975; <1.9 Ma from primates, Delson 1988) are now superseded by isochron cosmogenic and U-Pb dating; any source still quoting only faunal ages is out of date.

**Literature-moved flag:** Yes — the 2021 Kuman et al. absolute date is a meaningful refinement/confirmation of the site's foundational chronology, replacing decades of faunal-correlation-only estimates for Member 1's base.

---

### 4. Rising Star / Dinaledi Chamber (*Homo naledi*)

**What it is / why it matters:** A cave system in the Cradle of Humankind, South Africa, containing the fossils of *Homo naledi*, a small-brained hominin whose surprisingly young age (contemporaneous with early *Homo sapiens*) reshaped views of hominin diversity in the Middle Pleistocene.

- kind: taxon
- region: africa
- age (depositional / fossil): 236,000–335,000 years (combined best estimate) — Dirks, Roberts, Hilbert-Wolf et al. (2017), "The age of *Homo naledi* and associated sediments in the Rising Star Cave, South Africa," *eLife* 6:e24231, https://elifesciences.org/articles/24231
- dating_method (start/older bound): combination of OSL (sediment), uranium-thorium and paleomagnetism (flowstones)
- dating_method (end/younger bound): U-series/ESR (teeth), same source
- date_precision: approx (broad multi-method combined range)
- standing: consensus on the age itself (2017 multi-method paper); the *behavioral* interpretation (claimed deliberate burial by Berger et al. 2017, https://elifesciences.org/articles/26775.pdf) is separately and actively debated, but that is an interpretive dispute, not a dating dispute.

Supporting detail: sediment sub-unit 3b depositional window was initially 236,000–414,000 years before narrowing; individual tooth samples (US-ESR maximum age model) gave 229,000 (+60,000/−46,000) years and 276,000 (+59,000/−77,000) years respectively — same *eLife* 2017 source.

**Misconception to flag:** *H. naledi*'s small brain and primitive-looking skeleton led to initial assumptions of a much older (Pliocene/Early Pleistocene) age; the confirmed Middle Pleistocene age means it was contemporaneous with early *H. sapiens* in Africa — a major and still under-appreciated point.

**Literature-moved flag:** The 2017 age determination was itself the "literature moved" event, overturning assumptions based on morphology alone; no further major revision found in this search pass.

---

### 5. Hadar ("Lucy," *Australopithecus afarensis*)

**What it is / why it matters:** A site in the Afar region of Ethiopia that produced AL 288-1 ("Lucy"), the most famous *A. afarensis* skeleton, foundational to understanding early bipedalism.

- kind: taxon
- region: africa
- age: "just less than 3.18 million years old" — Institute of Human Origins, Arizona State University, https://iho.asu.edu/aboutLucy
- dating_method: argon-argon (40Ar/39Ar) on volcanic ash (tuff) layers in the Kada Hadar member, supported by paleomagnetic, paleontological, and sedimentological cross-checks (same IHO/ASU source)
- date_precision: approx (no explicit ± given on the fetched IHO page)
- standing: consensus
- Cross-reference: Smithsonian gives the rounder figure "about 3.2 million years old" — https://humanorigins.si.edu/evidence/human-fossils/fossils/al-288-1

**Misconception to flag:** The commonly repeated round number "3.2 million years" obscures that the currently favored figure (per IHO/ASU) is slightly younger, "just less than 3.18 Ma"; datasets citing "3.2 Ma" are not wrong but are using an older rounding convention. Also, the original 1970s K-Ar dating (~3 Ma ± 200,000 years, affected by contaminants) has been superseded by refined argon-argon dating — do not cite the original K-Ar figure as current.

**Literature-moved flag:** No recent (last few years) revision found in this pass; treat as stable consensus.

---

### 6. Laetoli Footprints

**What it is / why it matters:** A site in Tanzania preserving the oldest confirmed hominin footprints, directly demonstrating upright bipedal locomotion in *Australopithecus afarensis* millions of years before stone tools appear.

- kind: threshold
- region: africa
- age (Site G footprints): 3.66 Ma — Masao et al. (2016), "New footprints from Laetoli (Tanzania) provide evidence for marked body size variation in *Australopithecus afarensis*," *eLife*, https://elifesciences.org/articles/19568, citing the Deino (2011) recalibration for the 3.66 Ma figure.
- dating_method: argon-argon / K-Ar on volcanic tuffs (Deino 2011 recalibration)
- date_precision: exact (as stated: "3.66 million years ago (Ma) (Deino, 2011)")
- standing: consensus

**New Site S footprints:** Discovered/reported in the same 2016 *eLife* paper, contemporaneous with Site G at the same 3.66 Ma horizon, but preserving a much larger individual (S1), implying greater body-size variation/sexual dimorphism within *A. afarensis* than previously inferred from Site G alone. A 2021 follow-up paper extends the locomotor-diversity interpretation: "Footprint evidence of early hominin locomotor diversity at Laetoli, Tanzania," https://pubmed.ncbi.nlm.nih.gov/34853470/.

**Misconception to flag:** The footprints are sometimes treated as evidence of a single narrow-statured population; the Site S discovery (2016) complicates this by showing much larger individuals at the same horizon.

**Literature-moved flag:** Yes — Site S (2016 discovery) and its 2021 follow-up meaningfully revise the picture of body-size variation at Laetoli; this postdates most older tertiary summaries of the site.

**Caveat:** The broader "Upper Laetolil Beds" bracket (~3.8–3.5 Ma) commonly cited in secondary sources for the whole formation was not independently confirmed from a primary paper in this pass; use only the Site G/S figure of 3.66 Ma, which is directly sourced.

---

### 7. Jebel Irhoud

**What it is / why it matters:** A site in Morocco that produced the oldest securely dated *Homo sapiens* fossils, pushing back the emergence of the species by roughly 100,000 years relative to the previous consensus and replacing a single East-African-origin model with a "pan-African" mosaic model of modern human origins. This is the single most important "literature moved" example in this brief.

- kind: taxon
- region: africa
- age: 315±34 thousand years (weighted average; thermoluminescence on heated flints in layers 6–7, cross-validated with U-series/ESR on teeth) — Richter, Grün, Joannes-Boyau et al. (2017), "The age of the hominin fossils from Jebel Irhoud, Morocco, and the origins of the Middle Stone Age," *Nature* 546:293–296; companion paper Hublin, Ben-Ncer, Bailey et al. (2017), "New fossils from Jebel Irhoud (Morocco) and the pan-African origin of *Homo sapiens*," *Nature* 546:289–292, DOI 10.1038/nature22336, abstract at https://pubmed.ncbi.nlm.nih.gov/28593953/, stating "an age of 315±34 thousand years (thermoluminescence dating)." Press materials: https://uni-tuebingen.de/uploads/media/17-06-07_Irhoud_Press_Release_Univ_Tue.pdf
- dating_method (primary): luminescence (thermoluminescence); cross-checked with uranium-series/ESR
- date_precision: approx (±34 ka)
- standing: consensus (post-2017; this superseded prior classifications)
- Individually re-dated Irhoud 3 mandible: 286±32 ka (compatible with the weighted average) — same Richter et al. 2017 paper.

**Misconception to flag:** Jebel Irhoud fossils were originally (mid-20th century) classified as archaic/Neanderthal-related and dated to ~40,000 years; the 2017 re-dating and reclassification correctly identifies them as early *Homo sapiens* at ~300,000 years — do not perpetuate the old ~40 ka / "Neanderthal-related" framing.

**Literature-moved flag:** YES — flagship example. The 2017 *Nature* papers pushed the oldest confirmed *H. sapiens* back from ~195–200 ka (then-consensus, based on Omo I) to ~300 ka, and shifted the origin model from single-region (East Africa) to "pan-African."

---

### 8. Herto (*Homo sapiens idaltu*)

**What it is / why it matters:** A locality in the Middle Awash, Ethiopia (Bouri Formation), that produced *Homo sapiens idaltu*, among the oldest anatomically near-modern human fossils, informative for tracing the emergence of *H. sapiens* in the Horn of Africa.

- kind: taxon
- region: africa
- age: 160,000–154,000 years — White, Asfaw, DeGusta, Gilbert, Richards, Suwa & Howell, reported in the June 2003 issue of *Nature* ("Pleistocene *Homo sapiens* from Middle Awash, Ethiopia"); dated via a combination of argon-argon (led by the Berkeley Geochronology Center, P. Renne) and tephra chemistry correlation (WoldeGabriel, Hart). Press release: https://newsarchive.berkeley.edu/news/media/releases/2003/06/11_idaltu.shtml
- dating_method: argon-argon, cross-checked by tephra (volcanic ash) chemical correlation
- date_precision: approx
- standing: consensus
- **Caveat:** the exact *Nature* DOI/volume/page for the primary 2003 paper was not independently re-confirmed by direct fetch in this pass (only the Berkeley press release was fetched); treat the full bibliographic citation beyond author/year/journal-name as `n.a.` pending direct verification, though the 160–154 ka figure and dating methods are corroborated by the press release.

**Context (cross-reference only — Omo Kibish is an already-existing node, not re-researched here):** Omo I was re-dated in 2005 to ~195±5 ka via argon-argon on feldspars (McDougall et al. 2005), and further revised in a 2022 *Nature* paper to a **minimum** age of 233±22 ka: "Age of the oldest known *Homo sapiens* from eastern Africa," https://www.nature.com/articles/s41586-021-04275-8 (also indexed at https://research-portal.st-andrews.ac.uk/en/publications/age-of-the-oldest-known-ihomo-sapiensi-from-eastern-africa/). This 2022 Omo revision is relevant context for interpreting Herto's place in the *H. sapiens* fossil record, even though Omo Kibish itself is excluded from new entities per the task's instructions.

**Misconception to flag:** Herto is sometimes described loosely as "the oldest *Homo sapiens*," a title that has shifted at least three times in the literature (Omo I ~195 ka → Omo I ~233 ka minimum (2022) → Jebel Irhoud ~315 ka (2017), which is older than both Omo dates). Herto at 160–154 ka is younger than all of these and should not be described as the oldest.

**Literature-moved flag:** Indirectly, via the 2022 Omo Kibish revision reshuffling the relative ranking of East African early-*sapiens* sites.

---

### 9. Kabwe / Broken Hill Skull

**What it is / why it matters:** A cranium from Zambia (originally described as "*Homo rhodesiensis*," now usually assigned to *Homo heidelbergensis* or an African lineage close to the origin of *H. sapiens*/Neanderthals). It is a flagship example of a major, very recent (2020) redating that shows a specimen previously assumed to be ~500,000 years old is instead only around 300,000 years old.

- kind: taxon
- region: africa
- age: 299±25 thousand years (mean ± 2σ, best estimate) — Grün, Pomeroy, Stringer et al. (2020), "Dating the skull from Broken Hill, Zambia, and its position in human evolution," *Nature* 580:372–375, DOI 10.1038/s41586-020-2165-4, https://pubmed.ncbi.nlm.nih.gov/32296179/. A commonly cited range is 324,000–274,000 years — https://phys.org/news/2020-04-fossil-skull-modern-human-ancestry.html and https://www.sciencenews.org/article/broken-hill-skull-fossil-may-be-from-african-ghost-population (which states 324,000–276,000).
- dating_method: uranium-series (direct dating of the skull itself and associated bone material)
- date_precision: approx (±25 ka at 2σ)
- standing: now consensus around ~299 ka best estimate, though the site's formation history (unsystematic 1921 mining recovery; the original site has been fully quarried away) means several associated dates are minimum-only.

Additional dated material from the assemblage (same broad Grün et al. 2020 dataset, summarized via a University College London-hosted PDF, https://discovery.ucl.ac.uk/id/eprint/10219096/1/Miedzianogora%20et%20al%202025%20HomoHeidelbergensisMSA%20AfrArchRev.pdf): femur midshaft 169–162±9 ka (U-series); femur head 158.1±0.8 ka (U-series); pelvis 145(+48/−23) ka and, separately, 117.6±0.5 ka. This spread (roughly 301,000–102,000 years across different bones) suggests either multiple individuals or reworked deposits, and several of these figures are explicitly flagged in the literature as U-series minimum ages only.

**Misconception to flag — this is THE key one for this entity:** For most of the 20th century and into recent popular accounts, the Kabwe skull was routinely described as ~500,000 years old. The 2020 direct-dating study shows the skull itself is actually roughly 200,000 years younger than that figure. Any source still stating "500,000 years" for the Kabwe cranium specifically (as opposed to the wider Middle Pleistocene human-fossil record) is using the superseded figure.

**Literature-moved flag:** YES — flagship example. This is a 2020 primary redating that overturned a number in near-universal circulation for decades.

---

### 10. Bodo Cranium

**What it is / why it matters:** A cranium from the Middle Awash, Ethiopia, classified as *Homo heidelbergensis* (or, per a 2021 taxonomic proposal, "*Homo bodoensis*"), notable for cut-marks suggestive of early defleshing/ritual practice and for anchoring the mid-Pleistocene African hominin record.

- kind: taxon
- region: africa
- age: ~0.6 Ma (600,000 years), from the Upper Bodo Sand Unit
- dating_method: argon-argon (laser-fusion 40Ar/39Ar on vitric tephra)
- exact figure: weighted mean 0.64±0.03 Ma — Clark, de Heinzelin, Schick et al. (1994), "African *Homo erectus*: Old Radiometric Ages and Young Oldowan Assemblages in the Middle Awash Valley, Ethiopia," *Science*, https://www.science.org/doi/10.1126/science.8009220; corroborated with individual determinations of 0.74 and 0.55 Ma pooled to the 0.64 Ma weighted mean in Rightmire (1996), *Journal of Human Evolution*, PDF at http://in-africa.org/wp-content/uploads/2012/12/Rightmire-1996-JHE-Bodo.pdf
- date_precision: exact (±0.03 Ma on the weighted mean)
- standing: consensus on the age; taxonomic classification is a separate, active dispute (traditional *H. heidelbergensis* assignment vs. the 2021 proposal of a new species "*Homo bodoensis*") — this is a taxonomic dispute, not a dating dispute, and should be flagged as such if the app's schema distinguishes the two.

**Literature-moved flag:** The 2021 "*Homo bodoensis*" taxonomic proposal is recent but concerns classification, not the age itself.

---

### 11. Gona (Earliest Oldowan)

**What it is / why it matters:** A locality in the Afar region, Ethiopia, that produced what was for years considered the world's oldest confirmed stone tools, anchoring the ~2.6 Ma start of the Oldowan industry (the Oldowan itself is an already-existing global node in this dataset — this entry covers the Gona findspot specifically).

- kind: period
- region: africa
- age: 2.6–2.5 Ma
- dating_method: argon-argon (single-crystal laser fusion on overlying tuff, 2.53±0.15 Ma) plus paleomagnetic dating of the underlying Gauss–Matuyama boundary (2.58 Ma) — Semaw, Renne, Harris et al. (1997), "2.5-million-year-old stone tools from Gona, Ethiopia," *Nature* 385:333–336, https://doi.org/10.1038/385333a0; follow-up: Semaw et al. (2003), "2.6-Million-year-old stone tools and associated bones from OGS-6 and OGS-7, Gona, Afar, Ethiopia," *Journal of Human Evolution*, PDF at https://scholarblogs.emory.edu/stoutlab/files/2013/07/Semaw-et-al-2003.pdf
- date_precision: exact (argon-argon and paleomagnetic cross-check agree closely)
- standing: consensus on the site's own age, but its status as "the earliest" is now **contested/relative** (see below)

**Literature-moved flag:** In 2019, Bokol Dora 1 (BD 1) at Ledi-Geraru, Ethiopia, was dated slightly *older* than Gona, at 2.61–2.58 Ma, described as "establishing ~2.6 Ma as a firm date for the earliest Oldowan" — per the review "Searching for the emergence of stone tool making in eastern Africa" (2019), https://pmc.ncbi.nlm.nih.gov/articles/PMC6575166/. Gona's long-standing claim to "the earliest Oldowan" now has close, dated competition; frame Gona as "among the earliest confirmed Oldowan localities," not as the unique oldest.

---

### 12. Melka Kunture

**What it is / why it matters:** A high-elevation Ethiopian complex with an exceptionally long Oldowan-to-MSA sequence, including what may be the earliest known Acheulean technocomplex — but this claim is currently the subject of an active, unresolved 2021–2023 dating dispute.

- kind: period
- region: africa
- Oldowan (Garba IV E–F): ~1.7 Ma (older estimates of up to ~2.0 Ma from the 1970s–80s are now considered untenable given detailed chronostratigraphic work — precise primary citation for the untenability claim was not independently re-confirmed in this pass; treat as `n.a.` for a specific refuting paper, though the ~1.7 Ma figure itself is corroborated by the sources below)
- Early Acheulean (Garba IVD): **contested, actively disputed**
  - Newer claim: Garba IVD = 1.95 Ma, Gombore IB = 1.66 Ma, described as "the earliest Acheulean technocomplex discovered so far" — magnetostratigraphic analysis, Perini et al. (2021), elaborated in a 2023 Springer paper, "Isotopic insights into the Early Acheulean (1.95 Ma–1.66 Ma) high-elevation paleoenvironments at Melka Kunture," https://link.springer.com/article/10.1007/s12520-023-01879-1
  - Older/previous claim: ~1.6 Ma via argon-argon on the Grazia tuff (<1.719±0.199 Ma)
  - **Competing, skeptical position:** "Claims for 1.9–2.0 Ma old early Acheulian and Oldowan occupations at Melka Kunture are not supported by a robust age model," https://ouci.dntb.gov.ua/en/works/9ZQp3Pal/ — this directly disputes the 1.95 Ma figure.
  - dating_method (contested boundary): magnetostratigraphy (newer claim) vs. argon-argon (older claim); date_precision: contested; standing: **contested**
- Later Acheulean, Gombore II: ~0.8 Ma, constrained between 0.875±0.010 Ma and 0.709±0.013 Ma — Morgan et al. (2012), PDF at https://www.melkakunture.it/biblio/download/Morgan-al-2012.pdf. dating_method: argon-argon.
- Garba I (final Acheulean): ~0.5–0.6 Ma; Garba III (Acheulean-to-MSA transition): ~0.2 Ma (both from secondary summary material; not independently re-verified against a primary paper in this pass — treat precision as approx/`n.a.` pending direct confirmation).

**Dispute summary (report exactly):** Whether Melka Kunture hosts the world's oldest Acheulean technocomplex at ~1.95–1.66 Ma (Perini et al. 2021/2023) is actively contested by at least one 2021–2023 paper arguing the age model is not robust. Do not present the ~1.95 Ma figure as settled; present both positions.

**Literature-moved flag:** YES — this is a live, unresolved 2021–2023 dispute, one of the most recent in this entire brief.

---

### 13. Olorgesailie

**What it is / why it matters:** A long-lived basin in Kenya's Rift Valley documenting the Acheulean-to-Middle Stone Age transition, associated with major 2018 findings tying technological and behavioral change to Middle Pleistocene environmental instability.

- kind: period
- region: africa
- Late Acheulean assemblages: 615,000–499,000 years ago — Deino, Behrensmeyer, Brooks et al. (2018), "Chronology of the Acheulean to Middle Stone Age transition in eastern Africa," *Science* 360, https://www.science.org/doi/10.1126/science.aao2216 (companion papers by Potts et al. and Brooks et al. in the same 15 March 2018 *Science* issue)
- dating_method: argon-argon (40Ar/39Ar) and uranium-series
- MSA onset: "most likely by ~320,000 years ago, but at least by 305,000 years ago" — same Deino et al. 2018 source, establishing Olorgesailie as containing the oldest known repository of MSA artifacts in eastern Africa at the time of publication
- Overall Acheulean-bearing span at the site (Oltulelei Formation): 1.2 Ma to 499,000 years old
- date_precision: approx (ranges, not single exact points); standing: consensus (this 2018 paper set the current benchmark and has not been independently contradicted in this search pass)

**Literature-moved flag:** YES — the 2018 *Science* package is itself a major, relatively recent finding that reset the benchmark for the Acheulean-to-MSA transition date and tied it to documented environmental instability; treat pre-2018 secondary sources on Olorgesailie's chronology as potentially outdated.

---

### 14. Kalambo Falls

**What it is / why it matters:** A site on the Zambia–Tanzania border that in 2023 produced the earliest known deliberately worked wood structure in the archaeological record — two interlocking, notched logs — predating the emergence of *Homo sapiens* in Africa and vastly predating any previously known wood structure. This is one of the most recent major discoveries in this entire brief.

- kind: threshold
- region: africa
- age: at least 476±23 kyr (thousand years) for the earliest wood objects (samples BLB5, BLB3, "lower green band") — Barham, Duller, Candy et al. (2023), "Evidence for the earliest structural use of wood at least 476,000 years ago," *Nature* 622:107–111, DOI 10.1038/s41586-023-06557-9, https://www.nature.com/articles/s41586-023-06557-9
- dating_method: luminescence (single-grain quartz OSL for younger samples; post-IR IRSL on feldspars for older samples)
- date_precision: minimum (explicitly reported as "at least" 476±23 kyr)
- standing: consensus (new finding, not contested in this pass, though inherently a very recent and singular result)
- Additional wood objects in overlying bands: 390±25 kyr (blue band) and 324±15 kyr (yellow band) — same *Nature* 2023 source

**Misconception to flag:** Popular coverage sometimes implies this is "the oldest wooden object," full stop; more precisely it is the oldest known example of wood shaped and joined into a structure (two notched, interlocking logs), which is a distinct and stronger claim than merely "oldest worked wood fragment."

**Literature-moved flag:** YES — this is a brand-new node/finding as of September 2023, essentially unknown to any pre-2023 secondary source; ensure any existing app content does not omit it.

---

## THEME 2 — LATER STONE AGE / TERMINAL PLEISTOCENE

### 15. Sibudu Cave

**What it is / why it matters:** A rock shelter in KwaZulu-Natal, South Africa, with one of the most finely resolved MSA sequences in southern Africa, spanning pre-Still Bay through Howiesons Poort to the final MSA, and central to debates over the pace and geographic synchrony of MSA techno-complex transitions.

- kind: period
- region: africa
- Pre-Still Bay: >77 ka. Still Bay: ~77–70 ka down to ~64.7±2.3 ka (transition into Howiesons Poort).
- Howiesons Poort (HP) at Sibudu: single-grain OSL ages generally 65–58 ka; a specific layer (GR, quartz bifacial points) is reported as 61.7±2 ka in some papers and 63.8±2.5 ka in others — a minor inconsistency across sources that should be flagged rather than silently resolved. Primary attribution: Jacobs et al. (2008), "Ages for the Middle Stone Age of southern Africa," *Science* — **caveat:** this primary paper was referenced only via secondary citations in this research pass and was not independently re-fetched; treat the exact figures as sourced to the citing papers, not to a direct read of Jacobs et al. 2008 itself.
- Post-HP, late MSA, and final MSA (three phases): weighted mean OSL ages 58.5±1.4 ka, 47.7±1.4 ka, and 38.6±1.9 ka respectively, separated by two occupational hiatuses (10.8±1.3 ka and 9.1±3.6 ka) — Jacobs et al., "New ages for the post-Howieson's Poort, late and final Middle Stone Age at Sibudu Cave, South Africa," *Journal of Archaeological Science* 35:1790–1807, cited via https://digitalcommons.usf.edu/cgi/viewcontent.cgi?article=6191&context=kip_articles (secondary citation; primary paper not independently re-fetched in this pass).
- dating_method throughout: luminescence (single-grain OSL)
- date_precision: exact for individual layers (tight ± values), but standing: **contested** at the level of the "short chronology vs. extended chronology" debate below.

**Dispute summary (report exactly):** A "short chronology" for the Howiesons Poort (Jacobs et al. 2008: HP lasted only ~5,000 years, 64.8–59.5 ka) competes with an "extended chronology" proposed via thermoluminescence at the related site of Diepkloof, suggesting the HP persisted to as late as 50 ka (Tribolo et al. 2013). This controversy is described as unresolved as of 2020 in a broad review — https://academic.oup.com/edited-volume/61643/chapter/539817021 — though note this review source discusses the HP dating debate across multiple sites (including but not limited to Sibudu) and is not Sibudu-specific; treat with appropriate caution as a broader regional framing rather than a Sibudu-only finding.

**Literature-moved flag:** The short-vs-extended HP chronology debate remains open; no fully resolving paper was found in this pass.

---

### 16. Pinnacle Point

**What it is / why it matters:** A complex of caves on South Africa's southern Cape coast (notably PP5-6 and PP13B) with early evidence for coastal/marine resource use, heat treatment of stone, and pigment use, and one of the most recently (2025) refined absolute chronologies in this entire brief.

- kind: period
- region: africa
- Overall MSA occupation span at PP5-6: commonly summarized as ~110,000–50,000 years ago in recent press coverage, or more precisely ~92–49 ka / ~89–51 ka in academic papers, dated via optically stimulated luminescence with Bayesian statistical age modeling (169 sample dates at PP5-6 alone; ~400 across the wider project) — 2025 paper, "A high-resolution chronology for the archaeological deposits at Pinnacle Point 5–6, Western Cape Province, South Africa," *Quaternary Science Reviews*, described at https://news.asu.edu/b/20250528-archaeologists-use-sediment-and-sunlight-date-important-site-south-african-coast and indexed at https://asu.elsevierpure.com/en/publications/a-high-resolution-chronology-for-the-archaeological-deposits-at-p/ (publication dated 2025-04-15)
- dating_method: luminescence (single-grain OSL, Bayesian age modeling)
- date_precision: approx (ranges, refined by the 2025 Bayesian model)
- standing: consensus (2025 paper is a refinement, not an overturn, of the prior chronology)

Individual stratigraphic units (earlier 2017 paper, https://pmc.ncbi.nlm.nih.gov/articles/PMC5371328/): Yellow Brown Sand 96±6 ka (MIS 5); Yellowish Brown Sand and Roofspall 89±5 ka; Ashy Light Brown Sand 72±3 ka (MIS 4); Shelly Ashy Dark Brown Sand 71±3 ka (oldest backed pieces here); Black Brown Compact Sand and Roofspall 52±3 ka (MIS 3). PP13B (a separate cave at the same complex) has a discontinuous sequence ~170,000–90,000 years.

**Literature-moved flag:** YES — the 2025 *Quaternary Science Reviews* paper is a very recent (within months of this brief) high-resolution re-dating; any existing app content sourced from pre-2025 material should be checked against it.

**Caveat:** The broader "170,000–40,000 years" figure sometimes quoted for the whole Pinnacle Point complex traces to older secondary (Wikipedia-style) framing and was not independently confirmed from a primary paper in this pass; prefer the PP5-6-specific, source-linked figures above.

---

### 17. Diepkloof Rock Shelter

**What it is / why it matters:** A site in South Africa's Western Cape with one of the best-preserved MSA sequences, notable for engraved ostrich eggshell containers that constitute some of the earliest known deliberately produced graphic/symbolic markings.

- kind: period
- region: africa
- Engraved ostrich eggshell (EOES) tradition: dated to approximately 60,000 years ago — Texier, Porraz, Parkington et al. (2010), "A Howiesons Poort tradition of engraving ostrich eggshell containers dated to 60,000 years ago at Diepkloof Rock Shelter, South Africa," *PNAS*, https://pmc.ncbi.nlm.nih.gov/articles/PMC2851956/
- dating_method: optically stimulated luminescence (OSL) primarily, with thermoluminescence used for at least one layer boundary
- Specific HP-layer OSL dates: 58.1±1.9 ka to 63.3±2.2 ka (layer "John"); thermoluminescence estimate for the boundary between layers Darryl/Frank and John: 61±4 ka. Production of the EOES tradition is placed securely between 55–65 ka (same PNAS 2010 source).
- date_precision: exact for individual layers; standing: consensus on the ~60 ka EOES horizon itself, but **note an inconsistency**: a related 2013 paper by the same broad research group (Texier et al. 2013, cited secondarily) gives a much broader range, "eggshell engravings dating from 100,000 BP to around 52,000 BP." This 2010-vs-2013 discrepancy was not independently reconciled in this research pass and should be flagged to the app author as needing a closer read of both primary papers before choosing a single figure.
- Full MSA sequence at the site is sometimes summarized as spanning "before 130,000 BP to about 45,000 BP" (pre-Stillbay through Howiesons Poort through post-Howiesons Poort) — this broader span traces to Wikipedia-style secondary framing and was **not independently confirmed from a primary paper** in this pass; treat as `n.a.` for citation purposes pending direct verification, while the ~60 ka EOES figure above remains well-sourced.

**Literature-moved flag:** The 2010 vs. 2013 discrepancy in the eggshell-engraving date range is itself worth flagging as an internal literature inconsistency that later synthesis work should resolve, not necessarily a case of the field having "moved" in one clear direction.

---

### 18. Apollo 11 Cave

**What it is / why it matters:** A rock shelter in Namibia's ǁKaras Region, famous for seven painted stone plaques (four bearing figurative animal imagery), among the oldest known figurative art in Africa.

- kind: threshold
- region: africa
- age: approximately 30 ka (thousand years), via combined AMS radiocarbon and OSL dating: AMS date 29.0±0.4 ka BP (lab code KIA-35917), OSL age 29.4±1.4 ka; the uppermost MSA layer has a weighted mean age of 29.8±1.1 ka BP — Rifkin, Dayet, Queffelec et al. (2015 SAAB report), citing earlier work by Wendt (1972/1974/1976), Jacobs et al. (2008), and Vogelsang et al. (2010); PDF at https://rhinoresourcecenter.com/wp-content/uploads/2026/01/Rifkinetal.2015Apollo11SAABReportfinalsmall.pdf
- dating_method: **needs explicit flag** — the ~29–30 ka figures above combine AMS radiocarbon and OSL; whether the radiocarbon component is calibrated or uncalibrated was not resolved with certainty from the fetched excerpt. A competing figure sometimes cited is 27,500–25,500 years BP, or "25,500–23,500 BC" in calibrated terms per the Metropolitan Museum of Art, https://www.metmuseum.org/ja/essays/apollo-11-ca-25500-23500-b-c-and-wonderwerk-ca-8000-b-c-cave-stones. This range plausibly reflects the difference between calibrated and uncalibrated radiocarbon years rather than a true dating conflict, but this was **not conclusively resolved** in this research pass — report both figures and flag the calibration ambiguity explicitly to the app author rather than silently picking one. dating_method field should be recorded as `radiocarbon-uncalibrated or radiocarbon-calibrated (unresolved — flag for follow-up)`.
- date_precision: approx; standing: consensus that figurative plaques exist and are Late Pleistocene MSA-associated, but **contested/unclear** on the precise calendar-year figure due to the calibration ambiguity above.
- Occupational span at the rock shelter overall is sometimes cited as ~71 ka to 29 ka ("a series of human occupational pulses") — this broader span traces to secondary (Wikipedia-style) framing and was not independently confirmed from a primary paper in this pass.

**Misconception to flag:** Popular sources often state a single clean number ("~30,000 years old" or "c. 25,500–23,500 BC") without acknowledging that these are two different dating conventions (likely calibrated vs. uncalibrated radiocarbon years) rather than two independent competing dates — do not present as a genuine scientific dispute unless a primary source is found that frames it as one.

---

### 19. Enkapune Ya Muto ("Twilight Cave")

**What it is / why it matters:** A rock shelter on the Mau Escarpment, Kenya, containing what its excavator (Stanley Ambrose) argues is the earliest evidence anywhere in Africa for a Later Stone Age (Upper Paleolithic-equivalent) blade-based technology, as well as the oldest directly dated ornaments in the world (perforated ostrich-eggshell beads).

- kind: threshold
- region: africa
- Ostrich-eggshell beads: dated to 40,000 years ago via radiocarbon — Ambrose, "Chronology of the Later Stone Age and Food Production in East Africa," summarized at https://experts.illinois.edu/en/publications/chronology-of-the-later-stone-age-and-food-production-in-east-afr/ and in a University of Illinois press release, https://www.eurekalert.org/news-releases/1016533 ("Dated by radiocarbon to about 40,000 years ago, the beads 'are the oldest directly dated ornaments in the world'")
- Earliest LSA blade-based stone tools: "substantially earlier than 46,000 years ago," with the same Illinois press release stating the blade-based tools are "at least 46,000 years old, but may be as much as 50,000 years old — older than the oldest previously known industry of its kind, from Israel." A later (1998) refinement using obsidian-hydration dating on lithics plus annual deposition-rate estimates for volcanic ash/ejecta pushed the estimated start of the Upper Paleolithic at the site to before 46,000 BP — per the French Wikipedia summary of Ambrose's 1998 method (used here only to locate the claim; the underlying 1998 Ambrose paper itself was not independently re-fetched, so treat the specific "before 46,000 BP via obsidian hydration" claim as `n.a.` pending direct primary-source confirmation, though the "at least 46,000, possibly 50,000" radiocarbon-based figure above is corroborated by the Illinois press release).
- dating_method: radiocarbon-uncalibrated (older excavation reports typically report uncalibrated radiocarbon years BP; the app author should confirm calibration status against the primary Ambrose stratigraphic table before finalizing) — note that a detailed stratigraphic radiocarbon table exists (18 layers, from Iron Age ~500 BP down to layer RBL4 at 41,400 BP) per Wikipedia's summary of Ambrose's chronology, https://en.wikipedia.org/wiki/Enkapune_Ya_Muto — used here only to locate the primary source table, not as a dating authority itself.
- date_precision: approx (large ± implied by cross-dating methods, no single tight number given in the sources fetched)
- standing: consensus among specialists that this is an unusually early LSA/bead-bearing site, though its exact place in a pan-African "modern behavior" narrative remains a live topic of broader debate (not itself a dating dispute).

**Misconception to flag:** The site is sometimes summarized as simply "40,000-year-old beads," obscuring that the underlying blade-based lithic technology at the site is claimed to be even older (46,000–50,000 years), which is the more contested and more significant claim.

---

### 20. Iberomaurusian / Taforalt (Grotte des Pigeons)

**What it is / why it matters:** Taforalt Cave in Morocco is the most extensively radiocarbon-dated Later Stone Age site in North Africa and the location of North Africa's oldest known cemetery, central to debates over the origins and population history of the Iberomaurusian culture.

- kind: period
- region: africa
- Iberomaurusian culture overall: commonly bracketed c. 25,000/23,000–11,000 cal BP, per a synthesis at https://en.wikipedia.org/wiki/Iberomaurusian (used only to locate primary literature, not as a dating authority)
- **Origin of the Iberomaurusian at Taforalt specifically** (primary source): an MSA non-Levallois flake industry persisted until approximately 24.5 ka Cal BP, followed by an occupational gap, then the LSA Iberomaurusian industry appears from at least 21,160 Cal BP — Barton, Bouzouggar, Hogue, Lee, Collcutt & Ditchfield (2013), "Origins of the Iberomaurusian in NW Africa: new AMS radiocarbon dating of the Middle and Later Stone Age deposits at Taforalt Cave, Morocco," *Journal of Human Evolution* 65(3):266–281, DOI 10.1016/j.jhevol.2013.06.003, https://pubmed.ncbi.nlm.nih.gov/23891007/ — based on 54 AMS radiocarbon dates on bone and charcoal, Bayesian-modeled.
- dating_method: radiocarbon-calibrated (explicitly "Cal BP," Bayesian-modeled AMS radiocarbon)
- date_precision: minimum for the LSA appearance ("from at least 21,160 Cal BP"); approx for the MSA persistence boundary
- **Burial/cemetery component:** at least 34 Iberomaurusian adolescent and adult skeletons, directly dated to between 15,077 and 13,892 cal BP — cited via a Max Planck-hosted PDF, https://pure.mpg.de/rest/items/item_3516984_5/component/file_3588846/content, and corroborated by supplementary material for a *Science* paper, https://www.science.org/action/downloadSupplement?doi=10.1126/science.aar8380&file=aar8380_vandeloosdrecht_sm.pdf, which states: "Seven human bone samples from Sector 10 have been directly dated by AMS using ultrafiltration... yielded age estimations between 15,077 cal yBP and 13,892 cal yBP corresponding to the lower part of the Grey Series deposits."
- dating_method (burial dates): radiocarbon-calibrated (AMS with ultrafiltration)
- date_precision: exact (tight range from direct dating of the human remains themselves)
- Broader occupation at Taforalt: archaeological evidence for Iberomaurusian occupation between roughly 23,200 and 12,600 cal BP is described in secondary synthesis; Aterian occupation as old as 85,000 years is also reported at the site (this Aterian figure concerns the already-existing global "Aterian" node and is provided here only as site context, not as a new entity).
- standing: consensus on the AMS-dated Iberomaurusian sequence; some older sources (Ferembach 1985, cited via secondary literature) give a broader/older burial range of "23,000 YBP to 10,800 YBP," which the more recent high-precision AMS dating (Barton et al. 2013; the direct bone dates above) has effectively superseded and narrowed.

**Misconception to flag:** Older literature sometimes describes Taforalt burials as spanning a very wide window (up to ~23,000–10,800 YBP); high-precision direct AMS dating on the human remains themselves narrows the actual burial episode to a much tighter 15,077–13,892 cal BP window.

**Literature-moved flag:** The 2013 Barton et al. high-precision AMS redating, and the subsequent direct dating of the human remains (used in a 2018 *Science* ancient-DNA paper), represent a meaningful tightening of the chronology relative to older (pre-AMS) radiocarbon work at the site.

---

### 21. Wadi Kubbaniya

**What it is / why it matters:** A cluster of Late Paleolithic sites near Aswan, Upper Egypt, initially (and incorrectly) thought to contain the world's earliest evidence of cereal cultivation; the subsequent correction is itself an instructive case study in contamination and re-dating.

- kind: period
- region: africa
- Occupation window: approximately 19,000–17,000 years ago via radiocarbon dating (a range widely repeated in secondary sources, e.g., https://en.wikipedia.org/wiki/Wadi_Kubbaniya, used only to locate primary literature)
- Site-specific radiocarbon dates (published by the Tucson Laboratory, cited via the same secondary summary but traceable to Wendorf et al. primary excavation reports): site E-78-3, 18,000–17,870 BP; site E-81-1, 17,990–17,210 BP; site E-84-4, 17,810–17,300 BP, with error ranges of ±150 to ±280 years
- dating_method: radiocarbon-uncalibrated (the figures above are conventional "BP" radiocarbon years, not stated as calibrated in the sources fetched) — cross-checked against thermoluminescence: Bluszcz & Pazdur, "TL and 14C dating of the Upper Palaeolithic site at Wadi Kubbaniya, Egypt," and "Thermoluminescence dating of the Middle Paleolithic at Wadi Kubbaniya," both cited via https://www.cambridge.org/core/journals/radiocarbon/article/gliwice-radiocarbon-dates-xii/51D47BB476C80D1638B9B5D82795CC26
- **Later Late Paleolithic aggradation** (broader chronology, more recent synthesis): a series of 73 radiocarbon age determinations places deposition of the recorded beds between about 25,500 and 22,500 (uncalibrated) years, or approximately 25,650–22,650 cal BP at 2σ for the earliest ("Fakhurian") taxonomic unit, with individual dates of 20,690±280 BP (SMU-1037) and 19,810±310 BP (SMU-1136) — Bubenzer & Riemer, cited via https://books.openedition.org/mnhn/6847?lang=en
- dating_method (aggradation-level chronology): radiocarbon-calibrated (explicitly stated as recalibrated "cal BP" in this later synthesis) — note the apparent inconsistency between the older "uncalibrated ~19–17 ka" figures for the type sites and the newer "~25.5–22.5 ka" figure for the broader aggradation sequence; these likely refer to different stratigraphic units/parts of the sequence rather than being directly contradictory, but this was not fully reconciled in this research pass and should be flagged for the app author's attention.
- date_precision: exact for individual dated samples; approx for the site-wide bracket
- standing: consensus that the site is Late Paleolithic (terminal Pleistocene), late Last Glacial Maximum in age

**Misconception to flag — historically important:** When first excavated, barley, lentils, chickpea-like remains, and einkorn wheat were found at Wadi Kubbaniya and were initially interpreted as evidence of very early (Late Paleolithic) cereal cultivation, which would have predated the accepted origins of agriculture by many thousands of years. Subsequent AMS dating (University of Arizona, Tucson, for the cereal grains; Oxford for the date-stones) showed these plant remains were relatively modern contaminants, not part of the Late Paleolithic occupation — see Wendorf, Schild, Close et al. (1984), "New radiocarbon dates on the cereals from Wadi Kubbaniya," *Science* 225(4662):645–646, DOI 10.1126/science.225.4662.645, https://pubmed.ncbi.nlm.nih.gov/17729851/. **This correction should be flagged prominently: do not present Wadi Kubbaniya as an early-agriculture site.** The genuine plant-food evidence from the site (mostly wood charcoal and purple nut-grass tubers) is separately confirmed as contemporaneous with the Late Paleolithic occupation via direct AMS dating of the charred tubers themselves.

---

### 22. Ishango (and the Ishango Bone)

**What it is / why it matters:** A site on the Semliki River, Democratic Republic of the Congo, famous for the Ishango bone, a notched bone artifact sometimes interpreted as an early mathematical/tally device. The dating of both the site and the bone specifically has been unusually difficult and contested due to local volcanic disruption of carbon isotope ratios.

- kind: period
- region: africa
- Site occupation: commonly cited as occupied "between 9000 and 6500 BCE" in the original assessment, i.e., roughly 8,500–11,000 years ago — this figure and its rationale (volcanic disruption of the local carbon-14 record, absence of on-site charcoal for cross-checking) are summarized in an *Uptodate*-style physics-history article accessed via https://sci-hub.se/uptodate/24936573.pdf, which states occupation "between 9000 B.C. and 6500 B.C." and explicitly attributes dating difficulty to volcanic eruptions elevating local carbon-12 content and to the absence of charcoal samples.
- **Competing, more recent framing:** re-evaluation of the site's dating has been reported to place it at roughly 20,000 years old (secondary summary, https://en.wikipedia.org/wiki/Ishango_bone, used only to locate the underlying claim, not as a dating authority) — this is a substantial discrepancy (roughly 8,500–11,000 years vs. ~20,000 years) that was **not resolved with a primary paper** in this research pass; report both figures explicitly as competing/contested rather than picking one.
- A separate figure, "22,000 years," attributed to carbon-14 dating and said to be confirmed by other archaeological methods per Alison Brooks, appears in a French educational PDF, https://www.bibnum.education.fr/sites/default/files/64-ishango-answer.pdf — a third distinct figure, further underscoring the unresolved state of this site's chronology.
- dating_method: radiocarbon-uncalibrated, explicitly noted as compromised by local volcanic activity altering the carbon isotope ratio; no charcoal was available for cross-checking (same sci-hub-hosted historical source above)
- date_precision: **contested** — genuinely unresolved among at least three cited figures (~8,500–11,000 years; ~18,000–20,000 years; ~22,000 years)
- standing: **contested**

**Misconception to flag:** The Ishango bone's age is frequently stated as a single confident number in popular science writing (most often "~20,000 years"), when the primary/technical literature explicitly describes the radiocarbon dating as unreliable due to volcanic contamination of the local carbon reservoir, and multiple substantially different figures remain in circulation. Any dataset entry should state this as a genuine, longstanding dating problem rather than presenting one number as settled.

**Literature-moved flag:** The relative age has apparently shifted between different reviews of the evidence (from ~9,000 years in the original assessment to ~20,000 years or ~22,000 years in later reviews), but no single fetched primary source in this pass definitively resolves which figure is now the scientific consensus — this should be treated as an open item for the app author to resolve with direct access to the primary radiocarbon/stratigraphic literature (e.g., de Heinzelin's original reports and any modern re-analysis).

---

## THEME 3 — AFRICAN HOLOCENE / NEOLITHIC / PASTORALISM

### 23. African Humid Period (AHP) / "Green Sahara"

**What it is / why it matters:** A dramatic climatic phase in which much of what is now the Sahara Desert supported savanna, lakes, and wetlands, enabling human occupation (including cattle pastoralism) across areas that are hyperarid today. Its onset and termination bracket almost all the Holocene North African entities below.

- kind: period
- region: africa (with global climatic drivers)
- start: approximately 14,800 years ago (some sources say 14,600–14,500 years ago), at the end of Heinrich Event 1, coincident with the Bølling–Allerød warming — Shanahan, McKay, Hughen et al., "The time-transgressive termination of the African Humid Period," *Nature Geoscience*, PDF at https://www.whoi.edu/cms/files/shanahan12nat_220305.pdf, which states the AHP ran "about 14,800 to 5,500 years ago"; also corroborated by a 2026 phys.org summary of a University of Cologne-led sediment-core study: "a prolonged wet phase, which lasted from 14,800 to 5,500 years ago," https://phys.org/news/2026-03-sediment-core-reveals-years-precipitation.html, and by NOAA's own summary PDF, https://www.ncei.noaa.gov/sites/default/files/2021-11/5%20End%20of%20the%20Africian%20Humid%20Period%20-Final_OCT%202021.pdf ("a 'green' state prevailed during most of the time between 14,500 to 5,000 years")
- end: approximately 5,500 years ago (some sources give a range of 6,000–5,000 years ago, noting the termination occurred in steps, e.g., the 4.2-kiloyear event, and was time-transgressive across regions) — same Shanahan et al. *Nature Geoscience* source
- dating_method (both boundaries): inferred from multiple paleoclimate proxies (marine sediment dust flux records, lake sediment cores, speleothems); not a single direct-dating method — record as `unknown`/multi-proxy rather than forcing it into one of the six standard categories, and flag this to the app author as a case where the standard dating-method vocabulary may not fit cleanly.
- date_precision: approx (the WHOI/NOAA sources explicitly note the onset and termination each likely occurred within a timescale of decades to centuries, i.e., abrupt relative to the AHP's ~9,000-year overall duration, but not instantaneous)
- standing: consensus on the broad ~14,800–5,500 years ago bracket; some regional records show the onset in the central Sahara occurring somewhat later (~11,000–10,000 years ago for full vegetation expansion), which is a matter of geographic variability, not a genuine dating dispute.

**Misconception to flag:** The AHP is sometimes described as ending abruptly and simultaneously across all of North Africa; the primary literature explicitly frames the termination as "time-transgressive" (title of the cited Shanahan et al. paper), occurring in steps across different regions and time windows, with some evidence for an end as late as ~4,200 years ago (the "4.2-kiloyear event") in parts of the Sahel, Arabia, and East Africa.

---

### 24. Nabta Playa

**What it is / why it matters:** A Neolithic ceremonial and habitation complex in Egypt's Western Desert, notable for a "calendar circle" often described as one of the world's earliest known archaeoastronomical structures, built by cattle-herding pastoralists during the African Humid Period.

- kind: period
- region: africa
- Overall Neolithic occupation: Late and Terminal Neolithic ceremonial activity spans roughly 7,500–5,400 BP (uncalibrated radiocarbon years before present, per the cited academic source) — Malville et al., "Astronomy at Nabta Playa," PDF via https://sci-hub.se/tree/0d/9d/0d9d5f6a6886bcdabc6a0d081c704ab0.pdf, which states: "In the Late and Terminal Neolithic (7,500–5,400 BP), nomadic pastoralists built a ceremonial center..." The earliest excavated occupation levels at Nabta have calibrated radiocarbon dates of 10,300–9,800 BP (same source).
- Middle Neolithic ceremonial-center phase: 8,100–7,600 BP, ending in a short but deep drought beginning around 7,600 BP and lasting about 100 years (same source)
- Late Neolithic (cattle-burial "Ru'at El Baquar" people): 7,400–6,600 BP
- Terminal Neolithic (megalith-building "Ru'at El Ansam" people, incl. the Calendar Circle): 6,600 BP to total abandonment at approximately 5,400 BP
- Calendar Circle itself: dated on stratigraphic and radiocarbon grounds; one specific radiocarbon date from a hearth adjacent to the circle yielded 6,800±60 years BP (same Malville et al. source); a separate synthesis narrows the megalith-quarrying charcoal dates to a cluster of 6,600–6,200 BP (Schild & Wendorf 2004, cited in the same source)
- dating_method: radiocarbon-uncalibrated (the BP figures above are explicitly described in the source as radiocarbon years, not calendar-calibrated)
- date_precision: approx (broad phase ranges); exact for individual dated hearths/features within a phase
- standing: consensus on the broad chronological framework; the precise astronomical alignment date of the Calendar Circle (variously argued as ~6270 BC, ~4800 BC, or a range of 4500–3600 BC by different researchers, per secondary synthesis at https://en.wikipedia.org/wiki/Nabta_Playa, used only to locate the underlying claims) remains **debated among specialists in archaeoastronomy** — this is a separate, narrower dispute about the alignment's construction/use date, layered on top of the broader Terminal Neolithic occupation chronology, and should be flagged as such if the app includes the Calendar Circle as a sub-entity.

**Misconception to flag:** Popular framing often presents a single tidy "7,500 BC" origin date for the whole site; the primary sources describe a multi-phase, multi-century sequence of occupation, abandonment (during at least one severe drought), and re-occupation, with the celebrated Calendar Circle dating to a much later (Terminal Neolithic) phase than the earliest habitation at the playa.

---

### 25. Kiffian and Tenerian Cultures (Gobero, Niger)

**What it is / why it matters:** Gobero, in Niger's Ténéré Desert, is the largest and oldest known Stone Age cemetery in the Sahara, preserving two distinct, chronologically separated Holocene populations — the early Kiffian hunter-fisher-gatherers and the later Tenerian pastoralist-hunter-fishers — whose remains and burial customs illustrate the human response to the rise and retreat of the Green Sahara.

- kind: period
- region: africa
- **Kiffian occupation (Early Holocene):** dated using a combination of OSL (paleodune sand) and radiocarbon dating (burials, fauna, artifacts, lake sediments) — Sereno et al. (2008), cited via a recent (2026) dental-morphology follow-up paper, https://researchonline.ljmu.ac.uk/id/eprint/28668/7/Early%20to%20Middle%20Holocene%20Hunter%E2%80%90Fisher%E2%80%90Gatherers%20From%20the%20Green%20Sahara%20(Gobero,%20Niger)%20Dental%20Evidence%20for%20Regional%20African%20Affinities.pdf, which states the Kiffian-associated Early Holocene phase spans 9.6 kBP to 7.4 kBP (using IntCal20 calibration per Bronk Ramsey et al. 2023)
- **Tenerian occupation (Middle Holocene):** 6.6 kBP to 4.8 kBP, same source — narrower and more recent than the originally reported gap; the same paper notes that the gap between the two occupational phases was "initially thought to be approximately one millennium (Sereno et al., 2008)," but subsequent excavations by Sereno (2011–2022) produced additional dated material narrowing the gap to around 800 years (7.4 kBP to 6.6 kBP)
- dating_method: radiocarbon-calibrated (explicitly calBP using IntCal20) combined with OSL for the dune sediments
- date_precision: approx (kBP ranges, not single tight point estimates); standing: consensus, with the gap-narrowing itself representing a genuine, incremental scientific refinement
- Popular/press figures (less precise, from initial 2008 reporting): Kiffian colonized the region "between 10,000 and 8,000 years ago"; Tenerians lived in the region "between 7,000 and 4,500 years ago" — Associated Press coverage via https://tucson.com/news/science/article_8939b1b2-4fee-5f28-a441-22c57c0aaaa1.html and Science News, https://www.sciencenews.org/article/saharan-surprise ("Kiffians... colonized the Sahara from 10,000 to 8,000 years ago... Tenerians inhabited the site from 7,200 to 4,200 years ago")

**Misconception to flag:** Early press coverage (2008) described the gap between the Kiffian and Tenerian occupations as roughly 1,000 years with a simple "wet-dry-wet" narrative; more recent (2026) dental/chronological work has both narrowed that gap to ~800 years and refined the absolute boundaries using modern calibration curves (IntCal20) not available in 2008 — treat the original press figures as approximate/superseded by the peer-reviewed, recalibrated ranges above.

**Literature-moved flag:** YES — the cited 2026 paper represents a meaningful, very recent refinement of the original 2008 Sereno et al. chronology.

---

### 26. Fayum Neolithic (and the preceding Qarunian/Fayum Epipalaeolithic)

**What it is / why it matters:** The Fayum Oasis in northern Egypt preserves one of the earliest well-documented farming/herding sequences in the Nile Valley, transitioning from Epipalaeolithic (Qarunian) hunter-fisher-gatherers to Neolithic cereal cultivators and stock-keepers.

- kind: period
- region: africa
- **Earliest cereal cultivation (most recent, high-resolution figure):** ~7.8 cal ka BP (i.e., roughly 5,800 BC), based on lake-sediment core analysis (lamination, radiocarbon dating, and pollen analysis) — Kittel-cf. or comparable authors, "Earliest cereal cultivation in Egypt recorded in the Faiyum Oasis lake..." *Geological Quarterly*, https://gq.pgi.gov.pl/article/view/33599
- **Domesticated plants and animals more broadly:** appear first from approximately 5,400 BC (Qasr El-Sagha XI/81, oldest evidence for domestic animals in the Fayum) — Linseele, Marinova, Van Neer & Vermeersch, "New Archaeozoological Data from the Fayum 'Neolithic' with a Critical Assessment of the Evidence for Early Stock Keeping in Egypt," *PLOS ONE*, https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0108517 (identical content also at https://pmc.ncbi.nlm.nih.gov/articles/PMC4195595/)
- **Kom K and Kom W occupations:** dated between 4,650 and 4,350 BC based on radiocarbon dates on charcoal (same PLOS ONE source)
- **Fuller chronology synthesis:** Fayum Neolithic dated to around 5,700–4,200 cal BC; the preceding Fayum Epipalaeolithic (Qarunian) dated to around 7,100–6,000 cal BC — PhD dissertation synthesis, Leiden University repository, https://scholarlypublications.universiteitleiden.nl/access/item:2921298/view
- **Earliest cultivated crops (directly dated):** ca. 4,500 cal BC (Wendrich & Cappers 2005, cited in https://books.ub.uni-heidelberg.de/propylaeum/catalog/view/829/1377/92285)
- dating_method: radiocarbon-calibrated for the more recent, "cal BC"/"cal ka BP" figures; radiocarbon-uncalibrated for the older Hassan (1985) figures ("5230±50 BC to 4030±90 BC," per https://acagle.net/dissertation/chapter2.html) — note this inconsistency and prefer the calibrated figures where both are available
- date_precision: approx (multiple overlapping ranges from different research groups/decades); standing: consensus on the broad Epipalaeolithic-to-Neolithic sequence, though the exact calendar-year boundaries vary meaningfully (by centuries) between the Hassan (1985), Wendrich & Cappers (2005), and more recent lake-core (2023-era) studies — this reflects normal scientific refinement over multiple research programs rather than an active unresolved dispute.

**Misconception to flag:** The Fayum Neolithic domesticated-cereal evidence is sometimes cited with a single figure (e.g., "5,400 BC"), but the literature contains at least three meaningfully different figures (5,400 BC for first domestic animals; ~5,800 BC/7.8 cal ka BP for earliest cereal cultivation from the lake-core study; 4,650–4,350 BC for the most-excavated Kom K/Kom W settlements) referring to different lines of evidence at different locations within the Fayum — these should not be conflated into one number.

---

### 27. Khartoum Mesolithic ("Early Khartoum")

**What it is / why it matters:** A pottery-bearing hunter-fisher-gatherer tradition of the central Nile Valley in Sudan, named for its type site (Khartoum Hospital), and among the earliest pottery-using (but pre-agricultural) societies in Africa, distinguished by its characteristic "wavy line" and "dotted wavy line" ceramic decoration.

- kind: period
- region: africa
- Overall Early Khartoum period: currently dated between approximately 8,800–8,500 BCE and 5,000 BCE — Salvatori, Usai et al. synthesis, cited in a 2024 open-access paper, "Esh-Shaheinab: The archetype of the Sudanese Neolithic, its...", https://pmc.ncbi.nlm.nih.gov/articles/PMC11527226/, which states: "The overall Early Khartoum period in central Sudan is currently dated between 8800–8500 and 5000 BCE."
- An earlier, narrower synthesis (Haaland, cited via AfricaBib) gives: "the Khartoum Mesolithic dates from before 7000 BC to 5000 BC" — https://www.africabib.org/rec.php?RID=184920477
- **Earliest pottery specifically:** the site of Sarurab 2 has radiocarbon dates of 9,339±110 BP and 9,370±110 BP, consistent with the Early Khartoum culture — cited via https://revistas.ucm.es/index.php/CMPL/article/download/CMPL0303110345A/29670/30831; a 2021 synthesis (Springer) separately states the earliest ceramics in Sudan date from the mid-ninth millennium BC and come from several other sites (Site 2-R-66 at Amara West, Busharia I at Kerma, and Sorourab II) — https://link.springer.com/article/10.1007/s10437-021-09432-y
- dating_method: radiocarbon-uncalibrated for the raw BP figures (e.g., the 9,339±110 BP Sarurab 2 date); radiocarbon-calibrated for the "BCE" framing used in the broader synthesis papers — note both conventions are in circulation in this literature and should be distinguished carefully in any dataset entry
- date_precision: approx (broad multi-century/millennium ranges); standing: consensus on the broad chronological bracket
- **Note on gap with successor "Neolithic":** the Khartoum Neolithic (Esh-Shaheinab type site) follows, dated via three radiocarbon determinations (5,550±90, 5,650±60, and 5,720±80 uncal BP, i.e., roughly 4,700–4,200 BCE) — same PMC 2024 source. The Early Khartoum (Mesolithic) levels at the Esh-Shaheinab site itself were never directly radiometrically dated; their placement rests on typological cross-dating (the "Dotted Wavy Line horizon") rather than direct radiocarbon measurement — flag this as a methodological limitation, not a genuine competing-dates dispute.

**Misconception to flag:** "Khartoum Mesolithic" and "Khartoum Neolithic" are sometimes conflated in popular summaries; they are chronologically and technologically distinct (pre-agricultural pottery-users vs. later stock-keeping/cultivating groups), and at the type site Esh-Shaheinab the earlier "Mesolithic" component lacks direct radiometric dates altogether.

---

### 28. Capsian Culture

**What it is / why it matters:** An Epipalaeolithic-to-early-Neolithic archaeological tradition of the eastern Maghreb (Algeria and Tunisia), named for its type site near Gafsa (ancient Capsa), characterized by distinctive shell-and-ash mound sites ("escargotières"/"rammadiyat") and, in its later "Upper Capsian" phase, pressure-flaked bladelet technology.

- kind: period
- region: africa
- Overall span: dated between approximately 10,000 and 6,000 cal BP — Lubell (2001) and Jackes & Lubell (2008), cited in a University of Waterloo-hosted paper, http://www.arts.uwaterloo.ca/~mkjackes/JASR%203a7.pdf, which states: "The Capsian... is dated between ca. 10,000 and 6000 cal BP"
- An alternative/earlier framing (Wikipedia, used only to locate primary sources) gives ca. 9,000 to 5,400 cal BC for the same tradition, https://en.wikipedia.org/wiki/Capsian
- **Typical-to-Upper Capsian transition:** occurs around the time of the 8,200 cal BP cold event, after which primary pressure technique was used for blade/bladelet production — Rahmani & Lubell (2012), cited in the same Waterloo-hosted source
- **Upper Capsian specifically (Maghreb-wide):** occurs "between the 9th and the 8th millennium cal BP," per an academia.edu-hosted 2023 paper on Capsian lithic variability, https://www.academia.edu/99930659/Rethinking_the_Capsian_Lithic_Variability_Among_Holocene_Maghreb_Hunter_Gatherers
- **Earliest Neolithic features within a still-Capsian hunter-gatherer context:** decorated pottery appears in a hunter-gatherer context dated to 8,000 cal BP at the sites SHM-1 and Kef Hamda (same source); a Neolithic productive economy (pastoral activities, no evidence yet for agriculture) is dated from 7,400 cal BP at Doukanet el Khoutifa (same source)
- dating_method: radiocarbon-calibrated (explicitly "cal BP" throughout the more recent literature)
- date_precision: approx (broad millennium-scale ranges); standing: consensus on the overall span; the precise start date varies by several centuries to a millennium between different secondary summaries (10,000 cal BP vs. 9,000 BC, which are not identical), which should be treated as normal scholarly variation in rounding/framing, not an active dispute.

**Misconception to flag:** The Capsian is sometimes treated as a purely "Paleolithic" hunter-gatherer tradition throughout its existence; the literature shows a gradual, in-situ adoption of Neolithic traits (pottery by 8,000 cal BP, pastoralism by 7,400 cal BP) within an otherwise still-foraging economic base, predating full agriculture.

---

### 29. Cattle Domestication in Africa

**What it is / why it matters:** Whether African (particularly North/Northeast African) cattle represent an independent African domestication of the aurochs, versus an introduction of already-domesticated Near Eastern taurine cattle that later interbred with wild African aurochs, has been a long-running and only partially resolved debate with major implications for the archaeology of Saharan pastoralism (including Nabta Playa and Gobero, above).

- kind: threshold
- region: africa
- **Older/traditional model (independent African domestication):** archaeological evidence was long interpreted as suggesting African cattle were domesticated independently in the eastern Sahara 10,000 to 8,000 years before present, by hunter-gatherers — summarized (with citation to Wendorf & Schild) in a 2020 genomics paper, https://pmc.ncbi.nlm.nih.gov/articles/PMC7720612/
- **Competing/current genetic-genomic consensus:** genetic evidence supports a single Near Eastern domestication event, with taurine (*Bos taurus*) cattle spreading from the Fertile Crescent into North Africa; per the same 2020 paper (citing Stock & Gifford-Gonzalez), "*Bos taurus* cattle likely spread across the Sinai and into the Nile Delta 7,000 to 8,000 BP, then across North Africa, and subsequently into the Nile and the then-grassy Sahara"
- **Direct reassessment paper (2017), explicitly concluding against African independent domestication:** "Early North African Cattle Domestication and Its Ecological Setting: A Reassessment," https://link.springer.com/article/10.1007/s10963-017-9112-9, which states: "*Bos* remains from the early Holocene at Nabta Playa–Bir Kiseiba were those of hunted aurochs [not domesticated cattle]... the domesticated cattle spreading across Northeast and northern Africa... from the late seventh millennium BC or early sixth millennium BC onwards were descendants of *Bos taurus* domesticated in the Middle Euphrates area of the Middle East... the time has come to abandon the long-standing hypothesis of an early Holocene independent centre of cattle domestication in Northeast Africa."
- **Oldest uncontroversial evidence of domestic cattle in Africa specifically:** c. 5,750–4,550 BC in Egypt's Western Desert at Nabta-Kiseiba, and c. 7,000 BC at Kerma, Sudan — University of Edinburgh-hosted genomics paper, https://www.pure.ed.ac.uk/ws/files/172727489/The_mosaic_genome_of_indigenous_African_cattle_as_a_unique_genetic_resource_for_African_pastoralism.pdf. The same source states these *B. taurus* cattle remained largely confined to the Saharan-Sahelian belt until c. 4,000–3,000 years ago, when they reached the Tilemsi Valley (West Africa), the Lake Turkana basin (East Africa), and the Horn of Africa.
- **Later taurine × indicine (zebu) admixture in African cattle:** dated to approximately 750–1,050 years ago (same University of Edinburgh source) — this is a much later, historical-period event and outside the "prehistoric" scope of most of this brief, but included here because it directly follows the initial domestication/introduction narrative.
- dating_method: primarily archaeozoological (faunal bone identification) cross-referenced with modern population/whole-genome genetic dating (coalescent/divergence-time estimation), rather than a single direct radiometric method on the animal remains themselves — record as `unknown`/multi-method rather than forcing a single standard category, and flag this to the app author.
- date_precision: approx throughout; standing: **contested/superseded** — the "independent early African domestication in the eastern Sahara ~10,000–8,000 years ago" hypothesis, once prominent, is now explicitly argued to be superseded by the 2017 reassessment above in favor of a Near Eastern-origin, africanized-through-introgression model; however, note that not every source in this space agrees (the aurochs-in-Africa/African-lineage question is a live topic in bovine genomics), so record this as contested rather than fully settled.

**Misconception to flag — significant:** Nabta Playa's cattle remains are frequently cited in popular accounts as evidence of independent, very early (10,000–8,000 years ago) African cattle domestication; per the 2017 reassessment above, the early Holocene *Bos* remains at Nabta Playa–Bir Kiseiba are argued to be **wild, hunted aurochs**, not domesticated cattle, with domesticated cattle only appearing in the region later (via introduction from the Near East, from roughly the seventh–sixth millennium BC onward). Any dataset entry conflating "cattle remains at Nabta Playa" with "domesticated cattle at Nabta Playa" should be corrected in light of this reassessment.

**Literature-moved flag:** YES — the 2017 reassessment paper explicitly argues for abandoning a "long-standing hypothesis," making this a case where a widely repeated older narrative has been directly challenged relatively recently.

---

### 30. Pearl Millet and Sorghum Domestication in Africa

**What it is / why it matters:** Pearl millet (*Pennisetum glaucum*) and sorghum (*Sorghum bicolor*) are Africa's two most important indigenous domesticated cereals, with independent domestication centers in West Africa (pearl millet, Sahel) and Northeast Africa (sorghum, eastern Sudan) respectively — both now dated with increasing precision through archaeobotanical impression studies and, most recently, ancient-crop genomics.

- kind: threshold
- region: africa
- **Pearl millet — earliest evidence, Tilemsi Valley, Mali:** charred grains and seed impressions in ceramics dated to approximately 2500–2000 BC — Manning et al. (2011) and Manning & Fuller (2014), cited in https://pmc.ncbi.nlm.nih.gov/articles/PMC7937602/; a specific direct radiocarbon date on a single (morphologically indeterminate) grain from Karkarichinkat Nord (KN05) gives 2621–2464 BCE (4011±33 BP, lab code OxA-16919), per a 2025 *Nature Scientific Reports* paper, https://www.nature.com/articles/s41598-025-20110-w
- **Pearl millet — wild exploitation predates domestication:** wild pearl millet was being exploited in northern Mali in the fifth millennium BC, with predomestication cultivation probably established in the fourth millennium BC — https://pmc.ncbi.nlm.nih.gov/articles/PMC8550313/ ("Transition From Wild to Domesticated Pearl Millet")
- **Pearl millet — genomic dating of onset of diffusion:** a 2026-cited genomic study dates the onset of cultivated pearl millet's expansion across Africa to approximately 4,900 years ago (95% CI 3,685–5,889 years ago), supporting a western Saharan origin — https://shs.hal.science/halshs-03958403/document
- **Pearl millet at Dhar Tichitt, Mauritania:** grain impressions in pottery are now dated (via AMS re-analysis) to around 1,900–1,700 BCE for full domestication, though morphological domestication traits may have been present earlier — https://en.wikipedia.org/wiki/Dhar_Tichitt (used only to locate the underlying claim; the specific AMS re-dating study itself was not independently re-fetched in this pass, so treat the exact 1,900–1,700 BCE figure as `n.a.` pending direct primary-source confirmation, though it is broadly consistent with the Tilemsi Valley figures above from directly-fetched sources)
- **Sorghum — earliest evidence:** domestication process began in eastern Sudan by at least the fourth millennium BC, based on seed impressions on Butana Group pottery, continuing to the start of the second millennium BC — Winchell et al. (2017) and Beldados et al. (2018), cited in https://link.springer.com/article/10.1007/s10437-018-9314-2
- **Sorghum — domestication threshold:** morphologically domesticated forms comprised close to 70% of the sorghum population before 3000 cal BC around the upper Atbara river east of Khartoum, with domestication fully established at Jebel Moya — Winchell et al. (2017, 2018) and Barron et al. (2020), cited in https://pmc.ncbi.nlm.nih.gov/articles/PMC7937602/
- **Sorghum — first appearance in West Africa:** inferred at around 650 cal BC from Alibori sites in North Benin — Champion & Fuller (2018a, 2018b), same PMC source
- dating_method: primarily archaeobotanical (seed/spikelet impressions in ceramics, morphometric domestication-trait analysis) combined with AMS radiocarbon dating of the impressions or associated charred material; where explicitly radiocarbon-dated (e.g., the Karkarichinkat Nord grain), record as radiocarbon-calibrated
- date_precision: approx throughout (ranges rather than single point estimates, reflecting a gradual domestication process rather than a single threshold event)
- standing: consensus that pearl millet and sorghum represent geographically and taxonomically distinct, independent African domestication events (West African Sahel vs. eastern Sudan respectively), though the exact chronology of each continues to be refined by ongoing archaeobotanical work (e.g., the 2025 *Scientific Reports* paper above is very recent).

**Misconception to flag:** Domestication should not be treated as a single dated "event" for either crop — the cited literature explicitly frames both pearl millet and sorghum domestication as gradual processes spanning centuries to over a millennium (predomestication cultivation preceding full morphological domestication), with different sites/regions capturing different points along that continuum.

**Literature-moved flag:** YES — the 2025 *Nature Scientific Reports* paper on pearl millet's dispersal to South Asia, and the 2026-cited genomic dating of the diffusion onset, are both very recent refinements that postdate most standard secondary summaries of African crop domestication.

---

### 31. Bantu Expansion — Origin Phase (Grassfields Homeland)

**What it is / why it matters:** The Bantu expansion — the spread of Bantu languages and associated populations from a homeland in the Nigeria–Cameroon borderlands across most of Central, Eastern, and Southern Africa — is one of the most significant demographic and linguistic events in African prehistory. This entry concerns specifically the origin/homeland phase (the divergence of proto-Bantu within the Grassfields), not the full multi-millennium expansion across the continent (which may warrant separate treatment if the app tracks the expansion's later stages elsewhere).

- kind: period
- region: africa
- **Homeland location:** the Grassfields region on the Nigeria–Cameroon border, most closely associated archaeologically with the Shum Laka rock shelter in northwestern Cameroon — Oxford University Press chapter, "The Bantu Expansion," https://academic.oup.com/edited-volume/61663/chapter/553463850
- **Divergence/formation of the Bantu branch:** described as "a long, steady, and local development in the Grassfields... that lasted for more than 2,000 years, between 6,000–7,000 and 4,000–5,000 years ago" — same Oxford University Press source
- **Shum Laka site chronology:** the rock shelter has been inhabited since at least 30,000 years BP (long predating the Bantu-relevant phase); pottery first appears there around 7,000–6,000 years ago, alongside polished stone tools and bifacial macrolithic basalt/tuff tools, becoming prevalent around 5,000–4,000 years ago — Oxford University Press chapter, "The Cameroon Grassfield States in the Broader History of Nigeria and Cameroon," https://academic.oup.com/edited-volume/61663/chapter/553477889
- **Alternative linguistic-archaeological synthesis (Cambridge, 2023):** proposes that Grassfields (the language group ancestral to Bantu) predates approximately 3000 BCE, with proto-Bantu itself forming later, between 3000 and 2000 BCE, spanning roughly a millennium — https://www.cambridge.org/core/journals/journal-of-african-history/article/moving-histories-bantu-language-expansions-eclectic-economies-and-mobilities/F9F92F9C6A16A9633E75508E836C9C46. This same source frames the archaeological "calibration events" at Shum Laka as: (1) a shift from microlithic to macrolithic technology and new pottery between 5000 and 2000 BCE, sharpening to 4000–3000 BCE; and (2) construction of the region's first villages with polished stone tools and processing of fat-rich nuts, in southern Cameroon, between 1500 and 1000 BCE, marking the initial steps of the Bantu expansions proper.
- **Genetic (Y-chromosome) framing:** the "expansion of the Bantu-speaking people" (a distinct, later phase from the origin/homeland phase above) is dated to the past 3,000–5,000 years, with linguistic evidence placing its start around 5,000 years ago in the Nigeria–Cameroon border region — https://pmc.ncbi.nlm.nih.gov/articles/PMC3598330/
- dating_method: primarily historical linguistics (glottochronology/phylogenetics) and archaeological typology (ceramic/lithic seriation), cross-referenced with population genetics (Y-chromosome and whole-genome phylogenetic dating); not a single direct-dating method — record as `unknown`/multi-method
- date_precision: approx throughout (broad, overlapping millennium-scale windows from different research traditions)
- standing: **contested/actively refined** — the Oxford University Press synthesis (proto-Bantu forming 6,000/7,000–4,000/5,000 years ago) and the 2023 Cambridge synthesis (proto-Bantu forming 3000–2000 BCE, i.e., roughly 5,000–4,000 years ago) differ by roughly 1,000–2,000 years on when proto-Bantu itself (as opposed to its Grassfields-language ancestor) actually formed. Report both framings and flag this as an area of ongoing scholarly disagreement rather than picking one.

**Misconception to flag:** "The Bantu expansion" is often treated in popular writing as a single, sudden migratory event; the cited sources consistently frame it as a multi-stage process — first, over 2,000+ years of local linguistic/technological development within the Grassfields homeland itself (the phase covered by this entry), and only subsequently the outward geographic expansion across Central, Eastern, and Southern Africa (a separate, later, multi-millennium process that this entry does not attempt to fully date).

**Literature-moved flag:** The 2023 Cambridge *Journal of African History* synthesis represents a relatively recent, and only partially reconciled, alternative chronology to the Oxford University Press volume (2017); the app author should decide which synthesis to prioritize, or present both explicitly as competing frameworks.

---

### 32. African Iron Age Onset — Nok Culture and Taruga (Nigeria)

**What it is / why it matters:** The Nok culture of central Nigeria (Jos Plateau region) produced the earliest large-scale sculptural tradition in sub-Saharan Africa (terracotta figurines) and, at sites including Taruga, some of the earliest confirmed evidence of iron smelting in sub-Saharan Africa — though the exact dates for both the terracottas and the iron-smelting furnaces have shifted across different research programs and remain only partially reconciled.

- kind: threshold
- region: africa
- **Overall Nok culture span (broadest synthesis):** c. 1500 BC to c. 1 BC, per Wikipedia's infobox summary of the culture (used only to locate primary literature, https://en.wikipedia.org/wiki/Nok_culture); a peer-reviewed academic chapter instead frames the elaborate terracotta tradition as dating "back to the early 1st millennium BCE," describing it as "the earliest large-size sculptural tradition in sub-Saharan Africa" — Oxford University Press, "The Archaeology of Nok Culture in Nigeria (2nd/1st Millennium BCE)," https://academic.oup.com/edited-volume/61663/chapter/553397313
- **Terracotta dating (radiocarbon and thermoluminescence combined):** figurines have been dated to a range of approximately 2,900 to 2,000 years ago (roughly 900 BC to AD 1) per the same OUP-sourced Wikipedia summary; a scholarly synthesis paper narrows the main terracotta/iron-production phase to the 9th through 4th centuries BCE — "A Chronology of the Central Nigerian Nok Culture 1500 BC to..." https://scispace.com/papers/a-chronology-of-the-central-nigerian-nok-culture-1500-bc-to-4tddrwm23d, which states: "An early phase of the Nok Culture's development begins around the middle of the second millennium BC. Its main phase, in which terracotta figurines and iron production appear, starts in the 9th century BC and ends in the 4th century BC. A later phase with vanishing evidence extends into the last centuries BC... the end of the Nok Culture is thus set around the turn of the Common Era."
- dating_method (terracottas): radiocarbon-uncalibrated (associated charcoal) combined with thermoluminescence (directly on the fired terracotta itself)
- **Iron smelting at Taruga specifically — the key contested figure:**
  - Earliest widely repeated figure: iron-smelting furnaces at Taruga radiocarbon-dated to as far back as 280 BC (charcoal inside the furnaces), described as giving Nok "the earliest dates for iron smelting in sub-Saharan Africa up to that time" — *Archaeology* magazine feature, https://archaeology.org/issues/online/features/the-nok-of-nigeria/
  - Same source reports a later re-dating by Breunig, using charcoal from a Nok iron smelter at a site called Intini, yielding a date "between 519 and 410 BC," suggesting iron technology was established earlier than previous scholars (including Fagg) had realized
  - Full published furnace-date range at Taruga (four separate radiocarbon determinations, cited via an African Diaspora Archaeology Network PDF, http://www.diaspora.illinois.edu/news0311/news0311-5.pdf): 920 BCE (±50, sample Y-474); 440 BCE (±140, sample I-2960); 300 BCE (±100, sample I-3400); 280 BCE (±120, sample I-1459)
  - A peer-reviewed OUP chapter states: "The earliest dates of Nok iron-smelting furnaces are calibrated to about 800–550 BCE, the latest to about 400–200 BCE," while also cautioning that "[d]ue to the calibration curve plateau, radiocarbon dates of around 2450 bp remain imprecise and have wide ranges" — https://academic.oup.com/edited-volume/61663/chapter/553397313
  - A Wikipedia-sourced (used only to locate the claim) figure states iron working at Taruga "has now been firmly dated to 600 BC," calling this "the earliest known date for iron working in Sub-Saharan Africa," https://en.wikipedia.org/wiki/Taruga
- dating_method (iron smelting): radiocarbon-uncalibrated for the raw BP/BC figures reported by the original 1960s–70s excavations (Fagg); radiocarbon-calibrated for the more recent OUP synthesis figure (explicitly stated as "calibrated to about 800–550 BCE")
- date_precision: **contested** — figures for "the earliest Nok/Taruga iron smelting" range across at least four different values in the sources fetched (920 BCE outlier sample; ~800–550 BCE per the calibrated OUP synthesis; ~600 BCE per Wikipedia's "firmly dated" claim; 519–410 BCE per Breunig's Intini re-dating; 280 BCE per the earliest-reported *Archaeology* magazine figure) — this is compounded by an explicitly noted radiocarbon calibration-curve plateau around 800–400 BCE that makes precise dating in this window difficult by the nature of the method itself, not merely due to differing research programs.
- standing: **contested**, with an important caveat that some of the "contest" reflects a genuine dating-method limitation (the calibration plateau) rather than a resolvable scientific disagreement.

**Misconception to flag — important:** Many popular sources state a single, precise-sounding figure (e.g., "600 BC," or "the 4th century BC") for "the start of iron smelting in Nok/Taruga" without noting that (a) different original samples from the same site (Taruga) span nearly a full millennium (920–280 BCE) in their raw radiocarbon determinations, and (b) a substantial part of the imprecision is a fundamental, unresolvable-by-more-dating radiocarbon-calibration-curve plateau in this specific date range, not a simple matter of "newer research being more accurate." Any dataset entry should present a range (e.g., roughly 800–400 BCE, following the OUP-calibrated synthesis) with explicit acknowledgment of the calibration-plateau caveat, rather than a single confident year.

**Literature-moved flag:** The Breunig Intini re-dating (519–410 BCE) is presented in the *Archaeology* magazine feature as showing iron technology was established earlier than Fagg's original 1960s work suggested — this is a meaningful, though not dramatically recent, revision (exact publication year of the Breunig re-dating was not independently confirmed in this pass; treat as `n.a.` for a precise year, though the *Archaeology* magazine feature itself is dated 2024-04-01, https://archaeology.org/issues/online/features/the-nok-of-nigeria/).

---

## Excluded / Not Created

**Kerma / Nubian A-Group precursors:** Per the task's explicit instruction ("ONLY if prehistoric rather than historical"), this entity was evaluated and **not created**. Kerma (the Kerma culture/Kingdom of Kerma) and the Nubian A-Group are conventionally treated in the literature as protohistoric-to-historical Nile Valley civilizations, contemporary with and interacting with Predynastic and early Dynastic Egypt, rather than as prehistoric entities in the sense used elsewhere in this brief (i.e., pre-literate, pre-state societies). Given the ambiguity, this determination should be reviewed by the app author against however "prehistoric" is operationally defined elsewhere in the dataset; no dates are reported here since no entity was created.

---

## Summary of "Literature Moved Recently" Flags (Quick Reference)

For app-authoring triage, the following entities contain a genuinely recent (roughly the last 5–8 years, several within the last 1–3 years) shift, refinement, or unresolved active dispute in the primary literature, and deserve the closest scrutiny against any existing app content:

1. **Jebel Irhoud** (2017) — pushed *H. sapiens* origins back ~100,000 years; pan-African origin model.
2. **Kabwe/Broken Hill** (2020) — direct U-series dating revised the skull's age down by roughly 200,000 years from the long-assumed ~500,000-year figure.
3. **Sterkfontein Member 4 / Little Foot** (2015–2024, ongoing) — cosmogenic vs. U-Pb/ESR chronologies remain roughly 1–1.5 million years apart and unresolved.
4. **Melka Kunture early Acheulean** (2021–2023, ongoing) — actively disputed claim of a ~1.95 Ma "earliest Acheulean," directly challenged by at least one skeptical reassessment.
5. **Kalambo Falls** (2023) — brand-new discovery (oldest known wood structure), essentially absent from any pre-2023 source.
6. **Pinnacle Point** (2025) — very recent high-resolution Bayesian OSL re-dating of the PP5-6 sequence.
7. **Olorgesailie Acheulean-to-MSA transition** (2018) — reset benchmark for MSA onset in eastern Africa.
8. **Omo Kibish** (2022, cross-reference only, node itself excluded) — minimum age revised to 233±22 ka, reshuffling the relative ranking of early *H. sapiens* sites relevant to Herto's context.
9. **Cattle domestication in Africa** (2017 reassessment) — explicit call to abandon the "independent early Saharan domestication" hypothesis in favor of Near Eastern origin with later africanization.
10. **Pearl millet dispersal/domestication** (2025–2026) — very recent genomic and archaeobotanical dating of onset and westward/eastward dispersal.
11. **Bantu expansion origin chronology** (2017 OUP vs. 2023 Cambridge) — two only partially reconciled academic syntheses differing by 1,000–2,000 years on proto-Bantu's formation date.
12. **Gobero/Kiffian-Tenerian chronology** (2026 dental/chronology paper) — narrows the originally reported ~1,000-year gap between Kiffian and Tenerian occupations to ~800 years using IntCal20 recalibration.
13. **Ishango** — genuinely unresolved across three cited figures (~8,500–11,000 / ~18,000–20,000 / ~22,000 years); flagged as an open problem rather than a "moved" consensus.

---

## Notes on Sourcing Gaps (for the app author's attention)

A small number of figures in this brief could not be traced to a directly fetched primary paper within this research pass and are explicitly flagged inline as such (search for "not independently confirmed," "not independently re-fetched," or "`n.a.`" throughout the document above). These include: the exact bibliographic DOI for the 2003 Herto *Nature* paper; the Kokiselei 6 citation; several broad "occupational span" figures (Diepkloof's full MSA range, Apollo 11's full occupation range, Wadi Kubbaniya's site-wide bracket) that trace only to encyclopedia-style secondary summaries; and the Dhar Tichitt AMS re-dating study. None of these gaps affect the core, well-sourced figures reported for each entity, but they should be closed with direct primary-source fetches before any of these specific numbers are treated as fully verified in the shipped dataset.
