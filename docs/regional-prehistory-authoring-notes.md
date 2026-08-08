Regional prehistory authoring — completion record

Scope completed
- Added 54 generated entities in the requested regional branches:
  - Europe: 11 (including European Prehistory navigation era)
  - Central Asia: 7 (including Central Asian Prehistory navigation era)
  - Asia: 23 (6 Jōmon phases, 7 Chinese Neolithic, 5 South Asian, 5 Southeast Asian)
  - Americas: 10 (including Americas Prehistory navigation era)
  - Oceania: 3 children under Aboriginal Australia
- Revised existing Oceania records rather than duplicating them:
  - Aboriginal Australia is now open-ended; 1788 is explicitly a colonial boundary, not an end to living traditions.
  - Lapita and Polynesian settlement now carry supplied chronology, methods, alternatives, and sources.
- Added 52 supplied research references to tools/build_data.py's sources registry.
- Updated dataset-integrity expected counts for the expanded generated corpus.

Uncalibrated-radiocarbon entity records
- europe.prehistory.lascaux — Lascaux Cave Art
- east-asia.china.neolithic.hongshan — Hongshan Culture
- southeast-asia.prehistory.hoabinhian — Hoabinhian
- southeast-asia.prehistory.yangtze-rice — Yangtze Rice Domestication
- americas.prehistory.cactus-hill — Cactus Hill

Related handling
- Jōmon phases retain calibrated primary chronologies; the widespread raw “13,000 BCE” presentation is recorded as a misconception caveat.
- The Southeast Asian parent navigation era has dating_method=unknown because it deliberately spans both uncalibrated and calibrated child chronologies.
- White Sands, Clovis, Ban Chiang, Mehrgarh, Botai, Chauvet, Lake Mungo, and Jōmon competing or superseded chronologies are represented as alternatives or caveats.
- No numeric value was included without a supplied research-file source.

Final verification (all passed)
- python3 tools/build_data.py
- python3 tools/validate.py  -> OK — no errors. 0 warning(s).
- python3 tools/check_regenerated.py
- npx tsc --noEmit
- npx vitest run  -> 8 files passed, 164 tests passed

No git commit was created.
