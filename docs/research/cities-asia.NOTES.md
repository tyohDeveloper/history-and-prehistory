# cities-asia.json — enumeration notes

374 entries, written from internal knowledge only (no web research, per brief).
Built by `build_cities_asia.py` from the pipe-separated chunk files in `asia_chunks/`.
Edit the chunk files and re-run the script; it validates field counts, year sanity,
enum values, duplicate slugs and the 140-char summary limit.

## Counts

| region_hint | count |
|---|---|
| east-asia (China, Korea, Japan, Xinjiang) | 95 |
| south-asia (India, Pakistan, Bangladesh, Sri Lanka, Nepal) | 129 |
| southeast-asia (mainland + maritime) | 83 |
| central-asia (Silk Road, steppe, Tibet, Afghanistan) | 67 |

Still inhabited (`end_year: null`): 174. Confidence: high 109, medium 173, low 92.

Every item on the objective's calibration list is present, verified programmatically.

## Regional assignment decisions

- **Xinjiang / Tarim Basin** oases (Turpan, Gaochang, Jiaohe, Kashgar, Khotan, Loulan,
  Niya, Kucha, Karashahr, Yarkand, Miran, Beshbalik) are filed as `east-asia`, following
  the objective's grouping of Turpan and Kashgar under China. They are equally arguable
  as `central-asia`.
- **Tibet** is `central-asia` (Lhasa, Tsaparang, Khyunglung, Shigatse, Gyantse, Samye,
  Yumbulagang), as are **Mongolia** (Karakorum, Ordu-Baliq) and **Afghanistan**.
  Inner Mongolian sites inside modern China (Shangdu/Xanadu, Khara-Khoto, Liao Shangjing)
  are `east-asia`.
- **Shahr-i Sokhta** (Sistan, Iran) and **Sarai / Arkaim / Sintashta** (Russia) are filed
  `central-asia` because they belong to the Central Asian Bronze Age and steppe worlds;
  a Europe/West Asia enumerator may also claim them. Watch for duplicates at merge time.

## Monuments and non-cities — included but flagged

Per the brief these are included rather than omitted; each says so in `summary` and/or
`contested`:

- Monuments / temple complexes, not cities: Borobudur, Prambanan, Dieng, Ratu Boko
  (palace), My Son, Konark, Sanchi, Ellora, Ajanta, Samye (monastery), Yumbulagang
  (castle), Ayaz-Kala (fortress complex).
- Monastic university cities: Nalanda, Somapura/Paharpur.
- Pilgrimage complexes rather than secular cities: Lumbini, Sarnath, Bodh Gaya.
- Neolithic/Bronze Age villages rather than cities: Jiahu, Banpo, Sannai-Maruyama,
  Mehrgarh (village-to-town), Ban Chiang, Non Nok Tha, Botai, Arkaim, Sintashta.
- **Medang/Mataram Kuno** is a polity whose royal centre shifted and is not fixed to one
  site; included with `confidence: low`.

## Judgement calls on `end_year`

- **Angkor** — end 1431 (royal city abandoned) though Angkor Wat stayed in use and
  villages persist; noted in `contested`.
- **Bagan** — kept `still_inhabited: true` (end null): the royal city fell in 1287 but
  the site has been continuously occupied and its temples are in use.
- **Merv** — end 1789: annihilated in 1221, with successor settlements nearby until the
  late 18th century. `confidence: high` on the medieval peak, not on the tail.
- **Samarkand vs Afrasiab** — two entries: Samarkand (still inhabited) and Afrasiab
  (pre-Mongol walled city, end 1220).
- **Panjikent, Anuradhapura, Polonnaruwa, Buyeo, Hiraizumi, Nagaoka-kyo, Bost, Otsu,
  Tamralipti, Ter, Sopara, Pakuan Pajajaran, Manyakheta, Gulbarga, Cambay** — ancient city given an end year while a
  modern town stands on or beside the site; flagged in `contested`.
- **Nagarjunakonda** — end 400, now submerged by the Nagarjuna Sagar reservoir.
- Conquest and renaming were not treated as endings (Luoyang, Chang'an, Delhi, Beijing,
  Hanoi, Palembang all get null).

## Known thin spots for a later pass

- Chinese prefectural cities of the Tang-Song south, and Liao/Jin/Yuan northeastern sites.
- Korean regional walled towns (eupseong) beyond the capitals.
- Japanese provincial capitals (kokufu) and Sengoku castle towns founded near 1500.
- Bengal sultanate secondary capitals. (Kerala ports and Deccan capitals were added in
  `06_south_asia_extra.psv`: Muziris, Mahodayapuram, Kollam, Kozhikode, Kochi, Kannur,
  Nagapattinam, Manyakheta, Kalyani, Banavasi, Belur, Gulbarga, Bidar, Jaunpur, Gwalior,
  Dhar, Tripuri, Kalinjar, Ranthambore, Bhuj, Cambay.)
- Philippine and eastern Indonesian polities are represented thinly and at low confidence.
