# Mainland Southeast Asia: Research Notes for Historical State Dataset

Compiled to fix a dataset gap: a 588-year hole in Burmese history (Pagan ends 1297, nothing until much later), missing Sukhothai/Dvaravati/Lan Xang entries, and missing sources for Funan, Champa, Khmer Empire, Pagan, Ayutthaya, and Rattanakosin.

**Method note:** Dates, names, and disputes below are drawn from the cited sources only. Where sources disagree, both positions are given rather than resolved. Colonial/foreign-exonym naming is flagged explicitly per item, per the dataset's tracking requirement.

---

## 1. Dvaravati (Mon polities, ~6th–11th century)

- **Dates:** Conventionally "6th to late 11th century" ([Britannica](https://www.britannica.com/place/Dvaravati)). A Cambridge *Journal of Southeast Asian Studies* article argues for an earlier "proto-Dvāravatī" phase beginning as early as the 4th–5th century ([Cambridge](https://www.cambridge.org/core/journals/journal-of-southeast-asian-studies/article/abs/case-for-protodvaravati-a-review-of-the-art-historical-and-archaeological-evidence/6ABA16AADF5C3B4D62086719BEEF6A5C)).
- **DISPUTE — unified state vs. cultural network:** Britannica frames it as a kingdom that "flourished" over this span ([Britannica](https://www.britannica.com/place/Dvaravati)). By contrast, the accumulated modern-scholarship position (summarized in [Wikipedia's Dvaravati article](https://en.wikipedia.org/wiki/Dvaravati), itself citing archaeological literature) describes Dvaravati as "a cultural and political network... a loose aggregation of chiefdoms" rather than a centralized state. A Journal of the Siam Society paper states plainly that no chapter in the volume it reviews "provides argument that Dvāravatī was a unified kingdom" ([Journal of the Siam Society / TCI Thaijo](https://so06.tci-thaijo.org/index.php/pub_jss/article/download/158523/114853/434338)). This traces back to a historiographic split: Pierre Dupont's 1959 work argued for a unified Mon kingdom, while later archaeologists such as Srisakra Vallibhotama argued for multiple independent, rival city-states occupying the same cultural sphere. **This dataset should represent Dvaravati as a disputed entity — either a kingdom (traditional framing) or a network of Mon city-states sharing material culture, script, and Buddhist practice (current archaeological consensus), not resolve to one.**
- **Native/self-designation name:** "Dvaravati" is a Sanskrit name meaning "that which has gates"; it is attested locally — silver medallions from Nakhon Pathom name a "King of Sri Dvaravati" ([Wikipedia — Nakhon Pathom](https://en.wikipedia.org/wiki/Nakhon_Pathom)), so unlike Funan (below) it is not purely an outside label, though whether it named a single polity or a shared cultural label is exactly the disputed point above.
- **Capital(s)/centers:** No single confirmed capital — proposed primary centers include Nakhon Pathom (largest Dvaravati-period site and origin of the "Sri Dvaravati" medallions), U Thong, Si Thep, and Lavo (Lopburi).
- **Sources:**
  - [Britannica, "Dvaravati"](https://www.britannica.com/place/Dvaravati)
  - [Wikipedia, "Dvaravati"](https://en.wikipedia.org/wiki/Dvaravati) (secondary synthesis of the unity debate)
  - [Cambridge University Press, "The Case for Proto-Dvāravatī"](https://www.cambridge.org/core/journals/journal-of-southeast-asian-studies/article/abs/case-for-protodvaravati-a-review-of-the-art-historical-and-archaeological-evidence/6ABA16AADF5C3B4D62086719BEEF6A5C)
  - [Journal of the Siam Society, review essay on Dvāravatī historiography](https://so06.tci-thaijo.org/index.php/pub_jss/article/download/158523/114853/434338)

---

## 2. Pagan (Bagan) Kingdom (849–1297)

- **Start:** Burmese chronicle tradition dates the fortification/founding of Pagan to 849 CE under King Pyinbya, but historically verifiable Burmese state history is generally dated from 1044, the accession of Anawrahta, who is credited with unifying the Irrawaddy valley ([Wikipedia, "Pagan Kingdom"](https://en.wikipedia.org/wiki/Pagan_kingdom); [Britannica, "Anawrahta"](https://www.britannica.com/biography/Anawrahta); [Britannica, "Pagan"](https://www.britannica.com/biography/Pagan-king-of-Myanmar)).
- **End:** 1297. Mongol invasions (1277–1301) fatally weakened the kingdom, and Britannica's account of Myanmar's history notes it is unclear whether Mongol armies ever reached the city of Pagan itself, but "by 1300 Pagan no longer was the center of power" — the kingdom's political authority collapsed with the 1297 Myinsaing coup that deposed King Kyawswa ([Britannica, "History of Myanmar"](https://www.britannica.com/topic/history-of-Myanmar)).
- **Native/classical name:** Pali "Arimaddanapura" ("City that Tramples on Enemies"); Old Burmese Pugan/Pukam, modern romanization "Bagan" ([Wikipedia, "Arimaddana"](https://en.wikipedia.org/wiki/Arimaddana)).
- **EXONYM FLAG:** "Pagan" (English/older Western romanization) and "Burma" more broadly derive from colonial-era transliteration conventions rather than the endonym; modern "Bagan" is the closer romanization of the Burmese name.
- **Capital:** Pagan/Bagan, on the Irrawaddy River.
- **Sources:**
  - [Britannica, "Pagan kingdom"](https://www.britannica.com/place/Pagan-kingdom)
  - [Britannica, "History of Myanmar"](https://www.britannica.com/topic/history-of-Myanmar)
  - [Wikipedia, "Pagan Kingdom"](https://en.wikipedia.org/wiki/Pagan_kingdom)

---

## 3. Post-Pagan fragmentation (1297–1510): Myinsaing, Pinya/Sagaing, Ava, Hanthawaddy

The dataset's 1297–1510 gap should **not** be represented by a single successor state; the sources show a genuinely fragmented political landscape with (at minimum) two major, roughly co-equal successor states plus several minor ones. Recommended representation:

- **Myinsaing Kingdom** (a regency of the "Three Shan Brothers") ruled central Burma immediately after Pagan's collapse, c. 1297–1313 ([Wikipedia, "Myinsaing Kingdom"](https://en.wikipedia.org/wiki/Myinsaing_Kingdom)).
- Myinsaing split in 1315 into the **Pinya** and **Sagaing** kingdoms, which were reunified in 1364 by Thado Minbya into the **Kingdom of Ava (Inwa)**, which dominated Upper Burma from 1364 to 1555 ([Wikipedia, "Kingdom of Ava"](https://en.wikipedia.org/wiki/Kingdom_of_Ava)). Britannica corroborates: "the political situation remained fragmented... until Ava became the seat of authority in 1364" ([Britannica, "Mon kingdom"](https://www.britannica.com/place/Mon-kingdom)).
- **Hanthawaddy Kingdom** (Mon-ruled, Lower Burma) was founded in 1287 by King Wareru as "Ramaññadesa," with its capital moved from Martaban to Pegu (Bago) in 1369; it ruled 1287–1539, then briefly again 1550–1552 ([Wikipedia, "Hanthawaddy Kingdom"](https://en.wikipedia.org/wiki/Hanthawaddy_kingdom); [Britannica, "Wareru"](https://www.britannica.com/biography/Wareru)). Native/classical name: Pali *Haṃsāvatī* ("Realm of the Hamsa/sacred goose"); Mon script: ဟံသာဝတဳ.
- **Recommended dataset representation for 1297–1510:** Ava (Upper Burma, 1364 onward) and Hanthawaddy/Pegu (Lower Burma, 1287 onward) as the two dominant, co-existing successor polities, with Myinsaing/Pinya/Sagaing noted as a transitional phase 1297–1364 preceding Ava's consolidation.
- **Sources:**
  - [Wikipedia, "Hanthawaddy Kingdom"](https://en.wikipedia.org/wiki/Hanthawaddy_kingdom)
  - [Wikipedia, "Kingdom of Ava"](https://en.wikipedia.org/wiki/Kingdom_of_Ava)
  - [Britannica, "Mon kingdom"](https://www.britannica.com/place/Mon-kingdom)
  - [Wikipedia, "Myinsaing Kingdom"](https://en.wikipedia.org/wiki/Myinsaing_Kingdom)

---

## 4. Toungoo Dynasty (1510–1752)

- **DISPUTE — founder and start date:** Britannica states directly: "King Minkyinyo (1486–1531) of Toungoo is usually considered the founder [of the dynasty]... but many authorities believe the distinction of founder should be reserved for his son Tabinshwehti (1531–50)... [so] the dating of the dynasty may be considered either 1486–1752 or 1531–1752" ([Britannica, "Toungoo dynasty"](https://www.britannica.com/topic/Toungoo-dynasty)). This dataset uses 1510 (Minkyinyo's founding of Toungoo as a base) as a third commonly cited anchor, distinct from both Britannica alternatives — flag all three (1486, 1510, 1531) as competing start dates depending on source.
- **First/Second Toungoo distinction:** Scholarly convention splits the dynasty into the **"First Toungoo Empire"** (also called the "Second Burmese Empire" in older historiography), c. 1510–1599, and the **"Restored Toungoo"** or "Nyaungyan Restoration" dynasty, 1599–1752 ([Wikipedia, "Toungoo dynasty"](https://en.wikipedia.org/wiki/Toungoo_dynasty); [Wikipedia, "First Toungoo Empire"](https://en.wikipedia.org/wiki/First_Toungoo_Empire)).
- **Capitals (sequence):** Taungoo (1510–1539) → Pegu/Bago (1539–1599) → Ava/Inwa (1599–1752).
- **End:** 1752, when Restored Hanthawaddy (Mon) forces captured Ava, toppling the dynasty ([summarized at Human Saga](https://humansaga.net/empire/toungoo-empire); corroborated by [Wikipedia, "Toungoo dynasty"](https://en.wikipedia.org/wiki/Toungoo_dynasty)).
- **Sources:**
  - [Britannica, "Toungoo dynasty"](https://www.britannica.com/topic/Toungoo-dynasty)
  - [Wikipedia, "Toungoo dynasty"](https://en.wikipedia.org/wiki/Toungoo_dynasty)
  - [Wikipedia, "First Toungoo Empire"](https://en.wikipedia.org/wiki/First_Toungoo_Empire)

---

## 5. Konbaung Dynasty (1752–1885)

- **Start:** Founded by Alaungpaya, who proclaimed himself king on 29 February 1752 at Shwebo, in revolt against the Restored Hanthawaddy forces that had just toppled Toungoo ([Wikipedia, "Konbaung dynasty"](https://en.wikipedia.org/wiki/Konbaung_dynasty); [Britannica, "Alaungpaya"](https://www.britannica.com/biography/Alaungpaya)).
- **DISPUTE — naming/periodization:** Britannica notes an alternate scholarly framing under the heading "Alaungpaya Dynasty" covering 1752–1885, further noting "some authorities" restrict the name "Konbaung dynasty" specifically to the period beginning with King Bodawpaya in 1782 ([Britannica, "Alaungpaya Dynasty"](https://www.britannica.com/topic/Alaungpaya-Dynasty)).
- **Capitals (sequence):** Shwebo (1752–1760) → Sagaing (1760–1765) → Ava (1765–1783, then again 1821–1842) → Amarapura (1783–1821, then again 1842–1857) → Mandalay (1857–1885).
- **End:** The Third Anglo-Burmese War (7–29 November 1885) ended the dynasty; Britain formally announced the annexation of Upper Burma on 1 January 1886 ([Britannica, "Anglo-Burmese Wars"](https://www.britannica.com/event/Anglo-Burmese-Wars); [Wikipedia, "Third Anglo-Burmese War"](https://en.wikipedia.org/wiki/Third_Anglo-Burmese_War); [Britannica, "British raj"](https://www.britannica.com/event/British-raj) — confirms "on January 1, 1886, Upper Burma... was annexed by proclamation to British India").
- **Sources:**
  - [Wikipedia, "Konbaung dynasty"](https://en.wikipedia.org/wiki/Konbaung_dynasty)
  - [Britannica, "Anglo-Burmese Wars"](https://www.britannica.com/event/Anglo-Burmese-Wars)
  - [Britannica, "Alaungpaya"](https://www.britannica.com/biography/Alaungpaya)

---

## 6. British Burma (1885/1886–1948) and Independence

- **Start:** The Third Anglo-Burmese War ended Konbaung sovereignty over Upper Burma; annexation was proclaimed effective 1 January 1886, with Upper and Lower Burma administered together as a province of British India from that point, becoming a full ("major") province in 1897 ([Britannica, "History of Myanmar — The British in Burma, 1885–1948"](https://www.britannica.com/topic/history-of-Myanmar/The-British-in-Burma-1885-1948)). Rangoon (Yangon) became the provincial capital.
- **Mid-period administrative change:** On 1 April 1937, Burma was separated from British India and made a separate Crown Colony under the Burma Office, per the Government of India Act 1935 ([Wikipedia, "British rule in Burma"](https://en.wikipedia.org/wiki/British_rule_in_Burma); [EBSCO Research Starters, "Britain Separates Burma from India"](https://www.ebsco.com/research-starters/history/britain-separates-burma-india)).
- **Independence:** Achieved 4 January 1948, at 4:20 a.m. (a time chosen by astrological calculation), becoming the "Union of Burma" with Sao Shwe Thaik as first president and U Nu as first prime minister ([Britannica, "History of Myanmar"](https://www.britannica.com/topic/history-of-Myanmar/The-British-in-Burma-1885-1948); [Wikipedia, "Independence Day (Myanmar)"](https://en.wikipedia.org/wiki/Independence_Day_(Myanmar))). Nationalist leader Aung San negotiated the transfer of power (Aung San–Attlee Agreement, 27 January 1947) and the Panglong Agreement with ethnic-minority leaders (12 February 1947) but was assassinated on 19 July 1947, before independence took effect ([Britannica, "Aung San"](https://www.britannica.com/biography/Aung-San); [Wikipedia, "Panglong Conference"](https://en.wikipedia.org/wiki/Panglong_Conference)).
- **Sources:**
  - [Britannica, "History of Myanmar — The British in Burma, 1885–1948"](https://www.britannica.com/topic/history-of-Myanmar/The-British-in-Burma-1885-1948)
  - [Wikipedia, "British rule in Burma"](https://en.wikipedia.org/wiki/British_rule_in_Burma)
  - [Britannica, "Aung San"](https://www.britannica.com/biography/Aung-San)

---

## 7. Sukhothai Kingdom (traditionally c. 1238–1438)

- **Traditional dates:** Founding conventionally placed in the mid-13th century (commonly cited as 1238) when local Tai ruler Sri Indraditya led a revolt against Khmer authority ([Britannica, "Sukhothai kingdom"](https://www.britannica.com/place/Sukhothai-kingdom); [Britannica, "Sri Indraditya"](https://www.britannica.com/biography/Sri-Indraditya)). End conventionally dated 1438, when Sukhothai was absorbed into Ayutthaya following the death of Borommapan (it had already become an Ayutthaya tributary in 1378) ([Britannica, "Sukhothai kingdom"](https://www.britannica.com/place/Sukhothai-kingdom); [World History Encyclopedia, "Sukhothai"](https://www.worldhistory.org/Sukhothai/)).
- **DISPUTE — the Ram Khamhaeng Inscription controversy (must be represented, not resolved):** The traditional narrative of Sukhothai as a golden-age, unified "first Thai kingdom" rests heavily on the Ram Khamhaeng Inscription (Stele I), which contains the earliest known Thai script and describes a benevolent, prosperous kingdom. In 1987, historian Michael Vickery presented "The Ram Khamhaeng Inscription: A Piltdown Skull of Southeast Asian History?" at the International Conference on Thai Studies (ANU), arguing on linguistic and paleographic grounds that the stele may be a 19th-century forgery, possibly composed by King Mongkut (Rama IV) himself. Thai art historian Piriya Krairiksh independently argued (1988, in Thai) for Mongkut-era (1833–1855) authorship. Counter-evidence came from a 1990 scanning electron microscopy / energy-dispersive X-ray spectroscopy study, which found the stele's material to be consistent in age (roughly 500–700 years old) with four other genuine Sukhothai-era inscriptions. The Wikipedia summary states the debate "has not been definitively settled," though "the majority of academics... regard it as at least partly authentic" ([Wikipedia, "Ram Khamhaeng Inscription"](https://en.wikipedia.org/wiki/Ram_Khamhaeng_Inscription)). Michael Vickery's own papers are archived at [michaelvickery.org/vickery1995piltdown3.pdf](http://michaelvickery.org/vickery1995piltdown3.pdf) and [michaelvickery.org/vickery1978guide-rev.pdf](http://michaelvickery.org/vickery1978guide-rev.pdf).
- **DISPUTE — "first Thai kingdom" framing:** Wikipedia notes that "Sukhothai was long regarded in Thai historiography as 'the first Thai kingdom,' though current scholarship agrees that the origins of the Thai people extend much further back in time" ([Wikipedia, "Sukhothai Kingdom"](https://en.wikipedia.org/wiki/Sukhothai_Kingdom)) — i.e., Sukhothai was not the first Tai-speaking polity, only the first to leave an extensive epigraphic/political record in Thai script (itself now contested, per above).
- **Sources:**
  - [Wikipedia, "Ram Khamhaeng Inscription"](https://en.wikipedia.org/wiki/Ram_Khamhaeng_Inscription)
  - [Britannica, "Sukhothai kingdom"](https://www.britannica.com/place/Sukhothai-kingdom)
  - Michael Vickery, primary source papers at [michaelvickery.org](http://michaelvickery.org/vickery1995piltdown3.pdf)

---

## 8. Ayutthaya Kingdom (1351–1767)

- **Start:** Founded by Ramathibodi I (formerly Prince U Thong), enthroned 1351 ([Britannica, "Ramathibodi I"](https://www.britannica.com/biography/Ramathibodi-I); [Wikipedia, "Uthong"](https://en.wikipedia.org/wiki/Uthong)).
- **Native name / EXONYM note:** The kingdom's full ceremonial name was "Krung Thep Dvaravati Si Ayutthaya"; its own people referred to themselves as "Tai" and the kingdom as "Krung Tai" ([Wikipedia, "Ayutthaya Kingdom"](https://en.wikipedia.org/wiki/Ayutthaya_Kingdom)). **"Siam" is a foreign/exonymic label applied by outsiders** (Portuguese, and via them other Europeans) rather than the polity's own name for itself — flag this distinction in the dataset.
- **Capital:** Ayutthaya, on an island at the confluence of the Chao Phraya, Lop Buri, and Pa Sak rivers.
- **End:** Sacked by Burmese (Konbaung) forces under King Hsinbyushin on 7 April 1767, after roughly a 14-month siege, ending what Britannica calls the "417-year-old" kingdom ([Britannica, "Ayutthaya"](https://www.britannica.com/place/Ayutthaya-Thailand); [Wikipedia, "Siege of Ayutthaya"](https://en.wikipedia.org/wiki/Siege_of_Ayutthaya); [Wikipedia, "Burmese–Siamese War (1765–1767)"](https://en.wikipedia.org/wiki/Burmese%E2%80%93Siamese_War_(1765%E2%80%931767))).
- **Sources:**
  - [Britannica, "Ayutthaya, Thailand"](https://www.britannica.com/place/Ayutthaya-Thailand)
  - [Wikipedia, "Ayutthaya Kingdom"](https://en.wikipedia.org/wiki/Ayutthaya_Kingdom)
  - [Wikipedia, "Siege of Ayutthaya"](https://en.wikipedia.org/wiki/Siege_of_Ayutthaya)

---

## 9. Thonburi (1767–1782) and Rattanakosin/Chakri (1782–present)

- **Thonburi:** King Taksin established a new capital at Thon Buri in 1767/1768, immediately after expelling the occupying Burmese; he reigned 1767–1782 and was deposed and executed in 1782 ([Britannica, "Taksin"](https://www.britannica.com/biography/Taksin); [Britannica, "Thailand — The Thon Buri and Early Bangkok periods"](https://www.britannica.com/place/Thailand/The-Thon-Buri-and-Early-Bangkok-periods); [Wikipedia, "Thonburi Kingdom"](https://en.wikipedia.org/wiki/Thonburi_Kingdom)).
- **Rattanakosin/Chakri:** Founded 1782 (formally established 6 April 1782) by Rama I (born Thongduang, previously general "Chao Phraya Chakri"), who deposed Taksin and relocated the capital across the Chao Phraya River to Bangkok/Rattanakosin, founding the Chakri dynasty, "which continues to rule Thailand to this day" ([Wikipedia, "Rama I"](https://en.wikipedia.org/wiki/Rama_I); [Britannica, "Rama I"](https://www.britannica.com/biography/Rama-I); [Wikipedia, "Rattanakosin Kingdom (1782–1932)"](https://en.wikipedia.org/wiki/Rattanakosin_Kingdom_(1782%E2%80%931932))).
- **Sources:**
  - [Britannica, "Rama I"](https://www.britannica.com/biography/Rama-I)
  - [Britannica, "Taksin"](https://www.britannica.com/biography/Taksin)
  - [Wikipedia, "Rattanakosin Kingdom (1782–1932)"](https://en.wikipedia.org/wiki/Rattanakosin_Kingdom_(1782%E2%80%931932))

---

## 10. Lan Xang (1353–1707) and the Three-Way Split

- **Start:** Founded 1353 by Fa Ngum, with military and dynastic backing from the Khmer sovereign at Angkor (Fa Ngum had married a Khmer princess); capital initially at Muang Sua (Luang Prabang). The name "Lan Xang" ("Million Elephants") is short for the full name "Lan Xang Hom Khao" ("Million Elephants and the White Parasol") ([Britannica, "Fa Ngum"](https://www.britannica.com/biography/Fa-Ngum); [Wikipedia, "Lan Xang"](https://en.wikipedia.org/wiki/Lan_Xang); [Britannica, "History of Laos"](https://www.britannica.com/topic/history-of-Laos)).
- **Capital moved:** to Vientiane in 1560.
- **Split:** Britannica states that after the death of King Souligna Vongsa (1694), a succession dispute led the northern provinces to declare independence in 1707, forming the separate kingdoms of Luang Prabang and Vientiane (Vien Chan); the southern region seceded in 1713 to form Champasak ([Britannica, "History of Laos"](https://www.britannica.com/topic/history-of-Laos)). Wikipedia corroborates the 1707 Vientiane/Luang Prabang split and the 1713 Champasak secession ([Wikipedia, "Lan Xang"](https://en.wikipedia.org/wiki/Lan_Xang)).
- **Date ambiguity to flag:** Some king-list sources treat 1694 (Souligna Vongsa's death) as the effective end of unified Lan Xang, while Britannica and Wikipedia treat 1707 as the formal political split — both figures appear in the literature and should be represented as connected but distinct dates (de facto succession crisis in 1694, formal partition in 1707).
- **Sources:**
  - [Britannica, "History of Laos"](https://www.britannica.com/topic/history-of-Laos)
  - [Wikipedia, "Lan Xang"](https://en.wikipedia.org/wiki/Lan_Xang)
  - [Britannica, "Fa Ngum"](https://www.britannica.com/biography/Fa-Ngum)

---

## 11. Funan (traditionally 68–550, alt. ranges reported)

- **EXONYM FLAG:** "Funan" is not the polity's name for itself — it is a Chinese transliteration/exonym from Chinese historical texts (the *Book of Liang*, *Book of Jin*). The actual native name is not securely attested; possible native or Khmer-retronym candidates include "Nokor Phnom" (Khmer នគរភ្នំ, "Kingdom of the Mountain") — but caution is warranted here, as this Khmer term is a later retronym rather than a contemporary self-designation confirmed in primary inscriptions ([Wikipedia, "Funan"](https://en.wikipedia.org/wiki/Funan)). French scholar Claude Jacques proposed abandoning the term "Funan" altogether in favor of the attested contemporary city names known from inscriptions (Bhavapura, Aninditapura, Shresthapura, Vyadhapura), on the grounds that "Funan" imposes an artificial unity that may not have existed.
- **DISPUTE — unified state vs. loose network (directly analogous to the Dvaravati dispute above):** Historian Michael Vickery's paper "Funan Reviewed: Deconstructing the Ancients" argues that Funan was likely not a unified, centralized state but rather a loose alliance or network of competing Mekong Delta port polities that Chinese sources retrospectively described as a single "kingdom" ([Michael Vickery, "Funan Reviewed"](http://michaelvickery.org/vickery2003funan.pdf); mirrored at [Angkor Database](https://angkordatabase.asia/publications/funan-reviewed-deconstructing-the-ancients)). This dataset should represent Funan's political unity as contested, parallel to the Dvaravati treatment above — do not resolve to a single "kingdom" framing without flagging the debate.
- **Capital:** Vyadhapura ("City of the Hunter," Sanskrit), located near modern Banam/Ba Phnom in Prey Veng Province, Cambodia, possibly succeeded by or overlapping with Angkor Borei; the primary port and best-excavated site is Oc Eo.
- **Founding legend:** A Brahmin named Kaundinya and a local Naga princess named Soma (rendered as "Liuye"/"Willow Leaf" in Chinese sources) — this is a founding legend transmitted through Chinese chronicles, not a verified historical event, and should be flagged as legendary rather than factual.
- **Date range note:** The commonly cited 68–550 CE range is one convention; EBSCO Research Starters gives an alternative range of "1st century – c. 627 CE" ([EBSCO, "Kingdom of Funan"](https://www.ebsco.com/research-starters/anthropology/kingdom-funan)) — flag that Funan's end date varies by source depending on how the transition to Chenla is periodized.
- **Sources:**
  - Michael Vickery, ["Funan Reviewed: Deconstructing the Ancients"](http://michaelvickery.org/vickery2003funan.pdf)
  - [Wikipedia, "Funan"](https://en.wikipedia.org/wiki/Funan)
  - [EBSCO Research Starters, "Kingdom of Funan"](https://www.ebsco.com/research-starters/anthropology/kingdom-funan)

---

## 12. Khmer Empire / Angkor (802–1431)

- **Start — 802 Jayavarman II consecration, confirmed:** "Historians generally agree that this period of Cambodian history began in 802, when Jayavarman II conducted a grandiose consecration ritual on the sacred Mount Mahendraparvata," now known as Phnom Kulen, at which he proclaimed himself *chakravartin* ("universal ruler") and instituted the *devarāja* ("god-king") cult ([Wikipedia, "Khmer Empire"](https://en.wikipedia.org/wiki/Khmer_Empire); confirmed independently by [Britannica, "Jayavarman II"](https://www.britannica.com/biography/Jayavarman-II) and [Britannica, "Devarāja"](https://www.britannica.com/topic/devaraja)). The ceremony is also understood as an assertion of Khmer independence from Javanese overlordship. A detailed academic account (David Chandler, *A History of Cambodia*) corroborates the 802 date and devarāja ritual, while noting the name "Kambuja" itself does not appear in Cambodian inscriptions until the Angkorean era ([Chandler, *A History of Cambodia*, via Angkor Database](https://cdn.angkordatabase.asia/libs/docs/d.chandler-a-history-of-cambodia.pdf)).
- **Native name:** Known to its own inhabitants as **Kambuja** (Old Khmer: កម្វុជ; Khmer: កម្ពុជ) — this is a genuine self-designation, not an exonym, and is the root of the modern name "Cambodia" ([Wikipedia, "Khmer Empire"](https://en.wikipedia.org/wiki/Khmer_Empire)).
- **Capitals:** Early capital at Hariharalaya (near modern Roluos); later moved to the Angkor area, with the city known in its Angkorian prime as Yasodharapura. ("Angkor" itself derives from a Khmer/Sanskrit word for "capital city," *nagara/nokor*, and functions somewhat as a later descriptive name rather than the court's own toponym for each successive capital.)
- **End — 1431 sack, confirmed with nuance:** Convention dates the fall of the Khmer Empire to the Ayutthaya Kingdom's sack of Angkor in 1431, after a roughly seven-month siege beginning in 1430, under Siamese King Borommarachathirat II. In the aftermath, the Khmer court relocated south, eventually to the Phnom Penh area ([Wikipedia, "Fall of Angkor"](https://en.wikipedia.org/wiki/Fall_of_Angkor); [Britannica, "Angkor"](https://www.britannica.com/place/Angkor); [Britannica, "Cambodia — The decline of Angkor"](https://www.britannica.com/place/Cambodia/The-decline-of-Angkor)). Britannica separately notes recorded Tai attacks on Angkor also occurred earlier, in 1369 and 1389, indicating a longer decline rather than a single sudden event. Scholarly caution should be flagged here: one documentary source states plainly that the 1431 date, "though generally accepted," is "highly uncertain" and that the exact nature and timing of Angkor's political "fall" (as opposed to gradual decline) remains debated among specialists ([France Culture-style documentary transcript, "Dates that Made History"](https://www.youtube.com/watch?v=t67lLZYL9EU) — treat as a secondary/lower-confidence source flagging the debate, not as a primary citation for the date itself).
- **Sources:**
  - [Wikipedia, "Khmer Empire"](https://en.wikipedia.org/wiki/Khmer_Empire)
  - [Britannica, "Angkor"](https://www.britannica.com/place/Angkor)
  - [Britannica, "Jayavarman II"](https://www.britannica.com/biography/Jayavarman-II)
  - Supplementary: [Wikipedia, "Fall of Angkor"](https://en.wikipedia.org/wiki/Fall_of_Angkor); David Chandler, [*A History of Cambodia*](https://cdn.angkordatabase.asia/libs/docs/d.chandler-a-history-of-cambodia.pdf)

---

## 13. Champa (c. 192–1832) — addressing the unnumbered gap

The task's introductory text lists Champa among unsourced existing entities but the twelve numbered items give no dedicated research instructions for it. Researched here to the same standard as the numbered items.

- **Start:** Conventionally dated to 192 CE, when a Cham/local leader named Khu Liên led a successful revolt against the Eastern Han Chinese commandery of Rinan (Nhật Nam) and founded the polity of Lâm Ấp, treated as the first Cham state ([Wikipedia, "Champa"](https://en.wikipedia.org/wiki/Champa); [Britannica, "Champa"](https://www.britannica.com/place/Champa-ancient-kingdom-Indochina)). One source notes Cham historiographical tradition also traces a legendary earlier lineage to a figure called "Sri Mara" around 192 BCE, a legend distinct from the 192 CE Khu Liên founding and not treated as historically verified ([vietnamkb.com summary](https://vietnamkb.com/history/champa-civilization) — lower-confidence secondary source, flagged as such).
- **DISPUTE — unified kingdom vs. network of principalities:** Britannica itself describes Champa evolving "into a decentralized country composed of four small states, named after regions of India — Amaravati (Quang Nam); Vijaya (Binh Dinh); Kauthara (Nha Trang); and Panduranga (Phan Rang)" ([Britannica, "Champa"](https://www.britannica.com/place/Champa-ancient-kingdom-Indochina)). More explicitly, a recent epigraphic/linguistic study argues "Champa did not exist as a centralized state governed from a single political center. Rather, it consisted of multiple centers of power," and further finds that the term "Cham" never appears in the inscriptions as an ethnic designation at all — identity in the inscriptions is territorial/political, not ethnic ([Champa.one, epigraphy and Chamic linguistics study](https://champa.one/article/874)). This closely parallels the Dvaravati/Funan unity disputes above and should be represented the same way — as a network of principalities/centers (Indrapura, Amaravati, Vijaya, Kauthara, Panduranga) under a shared cultural-political label, not resolved into a single centralized kingdom.
- **Native/self-designation name and exonym notes:** Inscriptions attest formulaic self-references such as *Rāja Campā* ("King of Champa"), *Urang Campā* ("people of Champa"), and *Campādeśa* ("the land of Champa") — so "Campā"/"Champa" is a genuine attested self-designation, first appearing in the Cham inscription C.96 at Mỹ Sơn (dated 658 CE) and in the Khmer Kdei Ang inscription (K.53, dated 667/668 CE) ([Champa.one](https://champa.one/article/874); [Wikipedia, "History of Champa"](https://en.wikipedia.org/wiki/History_of_Champa)). Full/expanded form: *Nagaracampa* ("City/Land of Champa"). Modern Cham script rendering: ꨌꩌꨛꨩ. **EXONYM FLAG:** the commonly used external names for Champa in various neighboring chronicles are exonyms rather than the polity's own name — Chinese sources called it "Lin-yi" (林邑) until the 8th century and later "Zhànchéng" (占城; Sino-Vietnamese "Chiêm Thành"); Khmer inscriptions render it "ចាម្ប៉ា"; Malay sources use "Campa"; Arabic sources use "al-Ṣanf" ([Wikipedia, "Champa"](https://en.wikipedia.org/wiki/Champa)).
- **Capitals (sequence, per Wikipedia's infobox, itself synthesizing inscriptional and archaeological evidence):** Kandapurpura (192–605) → Simhapura/Trà Kiệu (605–757) → Virapura (757–875) → Indrapura/Đồng Dương (875–982) → Vijaya/Cha Bàn (982–1471) → Panduranga polity (1471–1832) ([Wikipedia, "Champa"](https://en.wikipedia.org/wiki/Champa)). Britannica's account differs slightly in sequencing detail but agrees Indrapura (from 875, under Indravarman II) and Vijaya (from the 10th–12th century) were successive major centers ([Britannica, "Champa"](https://www.britannica.com/place/Champa-ancient-kingdom-Indochina)).
- **DISPUTE — end date, three different endpoints in the literature:** (a) Wikipedia and most modern secondary sources give 1832, when Vietnamese Emperor Minh Mạng formally annexed the last surviving Panduranga principality ([Wikipedia, "Champa"](https://en.wikipedia.org/wiki/Champa)). (b) Britannica's dedicated Champa article states the kingdom lasted "from the 2nd to the 17th century CE" — a notably different, earlier endpoint than Wikipedia's ([Britannica, "Champa"](https://www.britannica.com/place/Champa-ancient-kingdom-Indochina)), while Britannica's own "Champa summary" page separately states that "by the late 15th century, incessant wars had led to its demise" ([Britannica summary](https://www.britannica.com/summary/Champa-ancient-kingdom-Indochina)) — meaning Britannica's own pages are internally inconsistent across the 15th, 17th, and (implicitly) later centuries. (c) 1471 is also cited as a major rupture point, when Vijaya was sacked by Đại Việt (the Champa–Đại Việt War of 1471), reducing Champa to the residual Panduranga principality ([Wikipedia, "Champa"](https://en.wikipedia.org/wiki/Champa); [French Wikipedia, "Royaume de Champa"](https://fr.wikipedia.org/wiki/Royaume_de_Champa)). **This dataset should flag 1471 (loss of Vijaya, effective end of Champa as a major regional power) and 1832 (final formal annexation of the last principality) as two distinct, both-legitimate end dates, and should not adopt Britannica's "17th century" figure without further verification, since it conflicts with Britannica's own summary page.**
- **Sources:**
  - [Britannica, "Champa"](https://www.britannica.com/place/Champa-ancient-kingdom-Indochina)
  - [Wikipedia, "Champa"](https://en.wikipedia.org/wiki/Champa)
  - [Wikipedia, "History of Champa"](https://en.wikipedia.org/wiki/History_of_Champa)
  - Supplementary on the unity dispute: [Champa.one, epigraphy/Chamic linguistics study](https://champa.one/article/874)

---

## What I could not verify

- **Dvaravati precise end date:** Sources disagree — Britannica and English Wikipedia say "late 11th century"; other secondary aggregations (not cited above because not authoritative enough) suggest ranges extending toward 1200. I was not able to find a primary-source-backed single end date; treat Dvaravati's end as a gradual absorption into Khmer/Lavo and later Sukhothai spheres rather than a discrete year.
- **Funan's precise founding legend historicity:** The Kaundinya–Soma founding story is transmitted only through later Chinese chronicles; I could not verify it against a Funan-internal (Old Khmer or Sanskrit) primary inscription, and it should be treated as legendary tradition, not confirmed event.
- **Whether "Nokor Phnom" is Funan's genuine contemporary self-designation:** I could not confirm this from a primary Funan-era inscription; the term appears in Khmer-language secondary sources as a retronym, and Claude Jacques's proposal to use only attested city names (Bhavapura, etc.) implies no securely attested single self-name for the whole polity exists. Treat "Funan" as a confirmed Chinese exonym, but treat any proposed native equivalent as unverified.
- **Lan Xang: 1694 vs. 1707 as the "true" end date:** Both years appear in reputable sources (Britannica uses 1707 for the formal split; some monarch-list sources use 1694, the year of Souligna Vongsa's death, as the effective end of a unified state). I could not find a source that explicitly reconciles or adjudicates between these two conventions; both should be retained with their distinct justifications (succession crisis vs. formal partition) rather than collapsed into one.
- **Champa's "17th century" end date claim on Britannica's own dedicated article:** This conflicts with Britannica's own summary page (which implies a late-15th-century effective demise) and with essentially all other sources consulted (which use 1471 and/or 1832). I could not find a reconciling explanation and flag this as an internal inconsistency in Britannica's own Champa coverage rather than a verified alternative date.
- **Sukhothai's Ram Khamhaeng Inscription authenticity:** Explicitly unresolved in the scholarly literature itself (per the Wikipedia synthesis of the debate) — not a gap in this research, but a genuine open question in the field that this dataset should preserve as unresolved rather than mark as either "forged" or "authentic."
- **Toungoo Dynasty exact start year:** Three different start years (1486, 1510, 1531) are defensible depending on which authority and which founder-designation convention is followed; I could not identify a single "correct" answer because Britannica explicitly presents this as an open convention choice, not a factual gap that further research would resolve.
- **Exact number/names of "minor" post-Pagan Shan states (1297–1364):** Sources confirm Myinsaing, Pinya, and Sagaing as the principal successor polities in Upper Burma during this transitional window, but I did not find authoritative, precisely dated boundaries for smaller contemporaneous Shan polities beyond these three; the dataset's 1297–1364 transitional period should be treated as incompletely enumerated.
