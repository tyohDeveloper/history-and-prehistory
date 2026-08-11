# Languages branch — decisions needed

Built from Tier 1 (521) + Tier 2 (636) = **1,157 languages**, no exclusions applied, placed into **1193 family and subgroup nodes** taken from Glottolog 5.3.

- Total nodes: **2353**
- Isolates: **183**
- Maximum depth: **15** levels below the root
- Pass-through nodes already collapsed: **554**

## 1. Depth — the main open question

Glottolog subgroups some families far more finely than a reader browsing history needs. These are the deepest paths. Each intermediate node is a real scholarly clade, so collapsing them loses information — but reaching French through eleven nodes is not usable either.

| Language | Depth | Path |
|---|---|---|
| Kikongo | 15 | volta-congo › benue-congo › bantoid › narrow-bantu › central-western-bantu › west-coastal-bantu › nzadic › lweric › dingic › klc-extended › nuclear-klc › kikongoic › kilaadic-kikongo › koongo-kituba |
| Kituba | 15 | volta-congo › benue-congo › bantoid › narrow-bantu › central-western-bantu › west-coastal-bantu › nzadic › lweric › dingic › klc-extended › nuclear-klc › kikongoic › kilaadic-kikongo › koongo-kituba |
| Old Portuguese | 14 | indo-european › italic › latino-faliscan › latinic › romance › italo-western-romance › western-romance › shifted-western-romance › southwestern-shifted-romance › west-ibero-romance › galician-romance › brazil-portugal-portuguese › portuguese |
| Sao Tomean Forro | 14 | indo-european › italic › latino-faliscan › latinic › romance › italo-western-romance › western-romance › shifted-western-romance › southwestern-shifted-romance › west-ibero-romance › galician-romance › gulf-guinea-creole-portuguese › saotomic |
| Sranan Tongo | 14 | indo-european › germanic › northwest-germanic › west-germanic › north-sea-germanic › anglo-frisian › anglic › later-anglic › middle-modern-english › macro-english › guinea-coast-creole-english › surinamese-creole-english › eastern-maroons |
| Kunyi | 14 | volta-congo › benue-congo › bantoid › narrow-bantu › central-western-bantu › west-coastal-bantu › nzadic › lweric › dingic › klc-extended › nuclear-klc › kikongoic › kamba-kunyi |
| Komo (Democratic Republic of Congo) | 14 | volta-congo › benue-congo › bantoid › narrow-bantu › central-western-bantu › north-zaire-river › rivers-bantu › ngiri › ngiri-terrien › ngombe-ababuan › ababuan › old-bomokandian › bilaic |
| Bislama | 13 | indo-european › germanic › northwest-germanic › west-germanic › north-sea-germanic › anglo-frisian › anglic › later-anglic › middle-modern-english › macro-english › pacific-creole-english › early-melanesian-pidgin |
| Cape Verdean Creole | 13 | indo-european › italic › latino-faliscan › latinic › romance › italo-western-romance › western-romance › shifted-western-romance › southwestern-shifted-romance › west-ibero-romance › galician-romance › upper-guinea-portuguese |
| French | 13 | indo-european › italic › latino-faliscan › latinic › romance › italo-western-romance › western-romance › shifted-western-romance › northwestern-shifted-romance › gallo-rhaetian › oil › global-french |
| Guinea-Bissau Creole | 13 | indo-european › italic › latino-faliscan › latinic › romance › italo-western-romance › western-romance › shifted-western-romance › southwestern-shifted-romance › west-ibero-romance › galician-romance › upper-guinea-portuguese |
| Haitian Creole | 13 | indo-european › italic › latino-faliscan › latinic › romance › italo-western-romance › western-romance › shifted-western-romance › northwestern-shifted-romance › gallo-rhaetian › oil › circum-caribbean-french |

Branches with languages at depth 8 or more:

- **Indo-European** — 63 languages
- **Volta-Congo** — 57 languages
- **Malayo-Polynesian** — 11 languages
- **Semitic** — 6 languages
- **Mande** — 6 languages
- **Dravidian** — 5 languages
- **Tai-Kadai** — 4 languages
- **Hmong-Mien** — 1 languages

## 2. The 91 proto-languages cannot be placed automatically

A reconstruction has no Glottocode, so none of them has a Glottolog path. But **47 of the 91 correspond directly to a Glottolog family node** — Proto-Germanic is what Glottolog calls the Germanic family, Proto-Slavic is Slavic, and so on.

The natural fix, which also gives every family node the dates it otherwise lacks: **merge each proto-language into its family node**, so the branch reads Indo-European → Germanic → and the Germanic node itself carries Proto-Germanic's date range and sources. Without this, family nodes are undated and invisible on any timeline, and the proto-languages sit in a flat heap.

The 44 with no matching family node need placing by hand. Listed below.

- **Proto-Afroasiatic** — stated parent: (none)
- **Proto-Albanian** — stated parent: Proto-Indo-European
- **Proto-Algonquian** — stated parent: Proto-Algic
- **Proto-Altaic** — stated parent: (none)
- **Proto-Amerind** — stated parent: (none)
- **Proto-Armenian** — stated parent: Proto-Indo-European
- **Proto-Athabaskan** — stated parent: Proto-Na-Dene
- **Proto-Atlantic** — stated parent: Proto-Niger-Congo
- **Proto-Baltic** — stated parent: Proto-Balto-Slavic
- **Proto-Bantu** — stated parent: Proto-Southern Bantoid
- **Proto-Basque (Proto-Vasconic)** — stated parent: (none)
- **Proto-Eastern Sudanic** — stated parent: Proto-Nilo-Saharan
- **Proto-Greek** — stated parent: Proto-Indo-European
- **Proto-Inuit** — stated parent: Proto-Eskimo-Aleut
- **Proto-Khoe** — stated parent: Proto-Khoe-Kwadi
- **Proto-Mon-Khmer** — stated parent: Proto-Austroasiatic
- **Proto-Munda** — stated parent: Proto-Austroasiatic
- **Proto-Na-Dene** — stated parent: (none)
- **Proto-Niger-Congo** — stated parent: (none)
- **Proto-Nilo-Saharan** — stated parent: (none)
- **Proto-Northeast Caucasian** — stated parent: (none)
- **Proto-Northwest Caucasian** — stated parent: (none)
- **Proto-Nostratic** — stated parent: (none)
- **Proto-Omotic** — stated parent: Proto-Afroasiatic
- **Proto-Oto-Manguean** — stated parent: (none)
- **Proto-Samic** — stated parent: Proto-Uralic
- **Proto-Samoyedic** — stated parent: Proto-Uralic
- **Proto-South Semitic** — stated parent: Proto-West Semitic
- **Proto-Tai** — stated parent: Proto-Tai-Kadai
- **Proto-Tibeto-Burman** — stated parent: Proto-Sino-Tibetan
- **Proto-Tocharian** — stated parent: Proto-Indo-European
- **Proto-Trans-New-Guinea** — stated parent: (none)
- **Proto-Ugric** — stated parent: Proto-Uralic

## 3. Other rows with no path

30 rows have a Glottocode that did not resolve to a Glottolog classification. They are currently under **Unclassified**, which is wrong for most of them.

- **Ancient Macedonian** (attested_ancient, gc `None`) — stated parent: (none)
- **Aquitanian** (attested_ancient, gc `None`) — stated parent: Proto-Vasconic
- **Burgundian** (attested_ancient, gc `None`) — stated parent: Proto-East Germanic
- **Classical Japanese (Bungo)** (attested_ancient, gc `None`) — stated parent: Old Japanese
- **Classical K'iche'** (attested_ancient, gc `None`) — stated parent: Proto-Quichean
- **Classical Mixtec** (attested_ancient, gc `None`) — stated parent: Proto-Mixtec
- **Classical Mongolian** (attested_ancient, gc `None`) — stated parent: Middle Mongol
- **Classical Newar (Nepal Bhasa)** (attested_ancient, gc `None`) — stated parent: Proto-Newar
- **Classical Zapotec** (attested_ancient, gc `None`) — stated parent: Ancient Zapotec / Proto-Zapotec
- **Early Assamese** (attested_ancient, gc `None`) — stated parent: Kāmarūpī Apabhraṃśa
- **Elu (Old Sinhala)** (attested_ancient, gc `None`) — stated parent: Eastern Middle Indo-Aryan Prakrit — Wikipedia lists "Elu Prakrit
- **Langobardic** (attested_ancient, gc `None`) — stated parent: Proto-West Germanic
- **Literary Vietnamese (Chu Nom era)** (attested_ancient, gc `None`) — stated parent: Old Vietnamese
- **Old Balinese** (attested_ancient, gc `None`) — stated parent: Proto-Bali–Sasak–Sumbawa
- **Old Bengali (Charyapada)** (attested_ancient, gc `None`) — stated parent: Gaudi Prakrit / Abahaṭ‌ṭha
- **Old Gujarati** (attested_ancient, gc `None`) — stated parent: Gurjar Apabhraṃśa
- **Old Kashmiri** (attested_ancient, gc `None`) — stated parent: Proto-Kashmiric
- **Old Latvian** (attested_ancient, gc `None`) — stated parent: Proto-East Baltic
- **Old Malayalam** (attested_ancient, gc `None`) — stated parent: early Middle Tamil
- **Old Nepali** (attested_ancient, gc `None`) — stated parent: Proto-Eastern Pahari
- **Old Odia** (attested_ancient, gc `None`) — stated parent: Odra Prakrit
- **Old Punjabi** (attested_ancient, gc `None`) — stated parent: Apabhraṃśa of the northwest
- **Old Siamese (Sukhothai Thai)** (attested_ancient, gc `None`) — stated parent: Proto-Southwestern Tai
- **Old Sindhi** (attested_ancient, gc `None`) — stated parent: Apabhraṃśa
- **Old Tibetan** (attested_ancient, gc `None`) — stated parent: Proto-Bodish
- **Old Vietnamese** (attested_ancient, gc `None`) — stated parent: Proto-Vietic
- **Scythian** (attested_ancient, gc `None`) — stated parent: Proto-Iranian — Wikipedia classes Scythian as a group of Eastern Iranic languages
- **Dogon** (modern_official, gc `dogo1299`) — stated parent: (none)
- **Moldovan** (modern_official, gc `None`) — stated parent: Romanian
- **Quechua** (modern_official, gc `quec1387`) — stated parent: (none)

## 4. Recorded but not acted on

All exclusion rules were dropped as instructed. The criteria are still evaluated per row so any of them can be reinstated as a filter over this data rather than by re-running research:

- labelled creole: **8**
- Glottolog calls it a dialect: **47**
- peak speakers under 10,000: **342**
- low documentation (no grammar written): **161**

Worth recording why the dialect label is not a safe filter: read literally it removes Biblical Hebrew, Classical Arabic, Vedic Sanskrit, Mycenaean Greek, Medieval and Vulgar Latin, all three stages of Egyptian, plus Cantonese, Serbian, Croatian and Luxembourgish. Glottolog's *dialect* means sub-lect of a language-level node, which is where it files every historical stage — and those stages are the point of a timeline. Not one of the 47 was a regional variant.
