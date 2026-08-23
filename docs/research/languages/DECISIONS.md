# Languages branch — decisions needed

Built from Tier 1 (521) + Tier 2 (636) = **1,157 languages**, no exclusions applied, placed into **1174 family and subgroup nodes** taken from Glottolog 5.3.

- Total nodes: **2337**
- Isolates: **183**
- Maximum depth: **16** levels below the root
- Pass-through nodes already collapsed: **554**

## 1. Depth — the main open question

Glottolog subgroups some families far more finely than a reader browsing history needs. These are the deepest paths. Each intermediate node is a real scholarly clade, so collapsing them loses information — but reaching French through eleven nodes is not usable either.

| Language | Depth | Path |
|---|---|---|
| Kikongo | 16 | atlantic-congo › volta-congo › benue-congo › bantoid › narrow-bantu › central-western-bantu › west-coastal-bantu › nzadic › lweric › dingic › klc-extended › nuclear-klc › kikongoic › kilaadic-kikongo › koongo-kituba |
| Kituba | 16 | atlantic-congo › volta-congo › benue-congo › bantoid › narrow-bantu › central-western-bantu › west-coastal-bantu › nzadic › lweric › dingic › klc-extended › nuclear-klc › kikongoic › kilaadic-kikongo › koongo-kituba |
| Kunyi | 15 | atlantic-congo › volta-congo › benue-congo › bantoid › narrow-bantu › central-western-bantu › west-coastal-bantu › nzadic › lweric › dingic › klc-extended › nuclear-klc › kikongoic › kamba-kunyi |
| Komo (Democratic Republic of Congo) | 15 | atlantic-congo › volta-congo › benue-congo › bantoid › narrow-bantu › central-western-bantu › north-zaire-river › rivers-bantu › ngiri › ngiri-terrien › ngombe-ababuan › ababuan › old-bomokandian › bilaic |
| Old Portuguese | 14 | indo-european › italic › latino-faliscan › latinic › romance › italo-western-romance › western-romance › shifted-western-romance › southwestern-shifted-romance › west-ibero-romance › galician-romance › brazil-portugal-portuguese › portuguese |
| Sao Tomean Forro | 14 | indo-european › italic › latino-faliscan › latinic › romance › italo-western-romance › western-romance › shifted-western-romance › southwestern-shifted-romance › west-ibero-romance › galician-romance › gulf-guinea-creole-portuguese › saotomic |
| Sranan Tongo | 14 | indo-european › germanic › northwest-germanic › west-germanic › north-sea-germanic › anglo-frisian › anglic › later-anglic › middle-modern-english › macro-english › guinea-coast-creole-english › surinamese-creole-english › eastern-maroons |
| Bali (Democratic Republic of Congo) | 14 | atlantic-congo › volta-congo › benue-congo › bantoid › narrow-bantu › central-western-bantu › north-zaire-river › rivers-bantu › ngiri › ngiri-terrien › ngombe-ababuan › ababuan › bali-beeke |
| Beembe | 14 | atlantic-congo › volta-congo › benue-congo › bantoid › narrow-bantu › central-western-bantu › west-coastal-bantu › nzadic › lweric › dingic › klc-extended › nuclear-klc › kikongoic |
| Njebi | 14 | atlantic-congo › volta-congo › benue-congo › bantoid › narrow-bantu › central-western-bantu › west-coastal-bantu › nzadic › lweric › dingic › kwilu-ngounie › moyen-kasai-ngounie › ndjavi-a |
| Yaka-Pelende-Lonzo | 14 | atlantic-congo › volta-congo › benue-congo › bantoid › narrow-bantu › central-western-bantu › west-coastal-bantu › nzadic › lweric › dingic › klc-extended › nuclear-klc › yaka-suku |
| Bislama | 13 | indo-european › germanic › northwest-germanic › west-germanic › north-sea-germanic › anglo-frisian › anglic › later-anglic › middle-modern-english › macro-english › pacific-creole-english › early-melanesian-pidgin |

Branches with languages at depth 8 or more:

- **Indo-European** — 69 languages
- **Atlantic-Congo** — 68 languages
- **Austronesian** — 25 languages
- **Afro-Asiatic** — 14 languages
- **Dravidian** — 6 languages
- **Mande** — 6 languages
- **Tai-Kadai** — 4 languages
- **Sino-Tibetan** — 3 languages
- **Smaller Language Families** — 3 languages

## 2. The 91 proto-languages cannot be placed automatically

A reconstruction has no Glottocode, so none of them has a Glottolog path. But **47 of the 91 correspond directly to a Glottolog family node** — Proto-Germanic is what Glottolog calls the Germanic family, Proto-Slavic is Slavic, and so on.

The natural fix, which also gives every family node the dates it otherwise lacks: **merge each proto-language into its family node**, so the branch reads Indo-European → Germanic → and the Germanic node itself carries Proto-Germanic's date range and sources. Without this, family nodes are undated and invisible on any timeline, and the proto-languages sit in a flat heap.

The 44 with no matching family node need placing by hand. Listed below.


## 3. Other rows with no path

8 rows have a Glottocode that did not resolve to a Glottolog classification. They are currently under **Unclassified**, which is wrong for most of them.

- **Eteocretan** (attested_ancient, gc `eteo1236`) — stated parent: (none)
- **Eteocypriot** (attested_ancient, gc `eteo1240`) — stated parent: (none)
- **Illyrian** (attested_ancient, gc `illy1234`) — stated parent: (none)
- **Kassite** (attested_ancient, gc `kass1244`) — stated parent: (none)
- **Lemnian** (attested_ancient, gc `lemn1237`) — stated parent: (none)
- **Pictish** (attested_ancient, gc `pict1238`) — stated parent: (none)
- **Raetic** (attested_ancient, gc `raet1238`) — stated parent: (none)
- **Tartessian** (attested_ancient, gc `tart1237`) — stated parent: (none)

## 4. Recorded but not acted on

All exclusion rules were dropped as instructed. The criteria are still evaluated per row so any of them can be reinstated as a filter over this data rather than by re-running research:

- labelled creole: **8**
- Glottolog calls it a dialect: **47**
- peak speakers under 10,000: **342**
- low documentation (no grammar written): **161**

Worth recording why the dialect label is not a safe filter: read literally it removes Biblical Hebrew, Classical Arabic, Vedic Sanskrit, Mycenaean Greek, Medieval and Vulgar Latin, all three stages of Egyptian, plus Cantonese, Serbian, Croatian and Luxembourgish. Glottolog's *dialect* means sub-lect of a language-level node, which is where it files every historical stage — and those stages are the point of a timeline. Not one of the 47 was a regional variant.
