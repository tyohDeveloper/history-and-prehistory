import json
P='/home/user/workspace/hp/src/data/entities.json'
d=json.load(open(P)); byid={e['id']:e for e in d['entities']}

R='review-findings-reigns.md'; C1='review-findings-cities-1.md'; C2='review-findings-cities-2.md'
PO='review-findings-polities.md'; PE='review-findings-periods.md'; CO='review-findings-concepts.md'

C=[]
def add(i,f,to,why,src):
    e=byid.get(i)
    assert e is not None, i
    C.append({"id":i,"field":f,"from":e.get(f,None),"to":to,"why":why,"source_review":src})

# ---------- reigns ----------
add('africa.nile.egypt.new-kingdom.dyn20.ramesses-iii','start_year',-1184,
    "Accession was set two years before his father Setnakht's death, overlapping Setnakht's whole reign.",R)
add('africa.nile.egypt.new-kingdom.dyn19.seti-i','start_year',-1294,
    "Seti I succeeded Ramesses I directly, so -1290 leaves four kingless years after -1294.",R)
add('europe.mediterranean.rome.empire.constantine','parent_id','europe.mediterranean.rome.empire.constantinian',
    "Constantine's 306-337 reign belongs in the Constantinian Dynasty, which already holds his sons.",R)

# ---------- cities 1 ----------
add('americas.mesoamerica.aztec.tenochtitlan','end_year',None,
    "The 1521 conquest was not an ending: the city was rebuilt as Mexico City on the same island.",C1)
add('americas.mesoamerica.aztec.tenochtitlan','extant',True,
    "Tenochtitlan has been continuously inhabited as Mexico City since 1521.",C1)
add('americas.mesoamerica.aztec.tenochtitlan','aliases',["México-Tenochtitlan","Mexico City"],
    "Readers arrive under the compound Mexica name and the modern name; neither was searchable.",C1)
add('europe.city-aquileia','end_year',None,
    "Attila's sack is a conquest, not an ending; Aquileia held a patriarchate for centuries after and is an inhabited comune.",C1)
add('europe.city-aquileia','extant',True,
    "Aquileia is a living Italian comune, so it cannot carry an end year.",C1)
add('africa.city-tahert','end_year',None,
    "The Fatimid conquest ended the Rustamid imamate, not the settlement, which is modern Tiaret.",C1)
add('africa.city-tahert','extant',True,
    "Tahert survives as Tiaret, a city of several hundred thousand people.",C1)
add('europe.city-lindum','start_year',60,
    "Sign error: the legionary fortress at Lincoln is post-conquest Roman, c. AD 48-60, not 60 BCE.",C1)
add('europe.city-kyiv','start_dating_method','received',
    "482 is the 1982 anniversary date taken from chronicle legend, not a typological date.",C1)
add('africa.city-thinis','start_dating_method','received',
    "Thinis is known only from texts and its site is not securely located, so it cannot be dated typologically.",C1)
add('africa.city-njimi','start_dating_method','received',
    "Njimi's site remains unidentified, so there is no assemblage to type; the date is textual.",C1)
add('europe.city-alba-longa','historicity','legendary',
    "The row's own summary calls it the legendary mother city of Rome, but historicity was null (accepted).",C1)
add('europe.city-lavinium','historicity','legendary',
    "The row's own summary calls it the legendary landing city of Aeneas, but historicity was null (accepted).",C1)

# alias pollution (complete new arrays; annotation entries removed)
for i,to in [('africa.city-buhen',[]),
             ('africa.city-faras',["Pachoras"]),
             ('africa.city-mirgissa',["Iken"]),
             ('africa.city-semna',["Semna West"]),
             ('africa.city-mogador',["Essaouira","Marrakesh-Safi"]),
             ('africa.city-ghat',["Fezzan"]),
             ('africa.city-kerma',["Kush","Northern State"]),
             ('africa.city-raqqada',["Kairouan"]),
             ('europe.city-itil',["Itil","Volga delta"]),
             ('central-asia.city-khyunglung',["Kyunglung","Ngari"]),
             ('east-asia.city-taihe-dali',["Yangxiemie","Dali"]),
             ('east-asia.city-jeonju',["Wansan"])]:
    add(i,'aliases',to,"Aliases must hold names a reader might arrive with; the removed entry was an annotation, not a name.",C1)

# not-a-city kind fixes still outstanding -> site
for i in ['europe.city-avebury','europe.city-durrington-walls','europe.city-emain-macha',
          'central-asia.city-samye','central-asia.city-yumbulagang','americas.city-canyon-de-chelly',
          'americas.city-acre-geoglyphs','americas.city-hopewell-earthworks','americas.city-newark-earthworks',
          'americas.city-fort-ancient','americas.city-san-agustin','americas.city-tierradentro',
          'americas.city-sacsayhuaman','americas.city-sitio-conte','americas.city-marajo']:
    add(i,'kind','site',"Monument, sanctuary, cemetery or multi-site landscape rather than a settlement, so `city` is wrong.",C1)
for i in ['europe.city-tarxien','southeast-asia.city-borobudur','south-asia.city-ajanta','south-asia.city-ellora',
          'oceania.city-brewarrina-fish-traps','oceania.city-kuk-swamp','oceania.city-budj-bim','oceania.city-ara-metua']:
    add(i,'kind','site',"Temple complex, monument or engineered landscape rather than a settlement, so `city` is wrong.",C2)

# ---------- cities 2 ----------
for i,nm in [('west-asia.mesopotamia.phoenicia.tyre','Tyre'),('west-asia.mesopotamia.phoenicia.sidon','Sidon'),
             ('west-asia.mesopotamia.phoenicia.byblos','Byblos'),('west-asia.mesopotamia.phoenicia.arwad','Arwad')]:
    add(i,'end_year',None,f"Alexander's 332 BCE conquest is not an ending: {nm} continued through Hellenistic, Roman, Islamic and Ottoman times and is inhabited today.",C2)
    add(i,'extant',True,f"{nm} is a living settlement on the Levantine coast today.",C2)
add('south-asia.city-anuradhapura','end_year',None,
    "The 1017 Chola conquest ended Anuradhapura's capital function, not the city, which was never abandoned.",C2)
add('south-asia.city-anuradhapura','extant',True,
    "Anuradhapura is a substantial living Sri Lankan city and pilgrimage centre.",C2)
add('europe.city-skalholt','end_year',1785,
    "Skalholt remained Iceland's principal see until the 1780s, when the see moved to Reykjavik; 1500 is arbitrary.",C2)
add('southeast-asia.city-lamphun','start_year',750,
    "Hariphunchai was founded in the mid-8th century CE; -600 predates any urbanism in northern Thailand by ~1,350 years.",C2)
add('southeast-asia.city-mataram-medang','kind','polity',
    "Its own summary calls it a Central Javanese kingdom with a shifting royal centre, so it is a polity, not a city.",C2)

# ---------- polities ----------
for i in ['east-asia.china.tang','global.multi-regional.abbasid','global.multi-regional.rashidun',
          'global.multi-regional.umayyad','europe.western.carolingian','east-asia.china.song',
          'east-asia.china.sui','east-asia.korea.goryeo','east-asia.korea.unified-silla',
          'southeast-asia.mainland.dinh','southeast-asia.mainland.early-le','southeast-asia.mainland.ngo',
          'east-asia.japan.heian','east-asia.japan.nara','europe.central.hre','west-asia.iran.buyid',
          'west-asia.iran.saffarid','west-asia.iran.tahirid','global.multi-regional.fatimid',
          'south-asia.harsha','south-asia.chalukya-western','central-asia.uyghur-khaganate',
          'east-asia.china.five-dynasties','east-asia.china.liao']:
    add(i,'start_dating_method','calendar',
        "The founding year is fixed to the year (often the month) in contemporary or near-contemporary annals, so `unknown` misstates how the date is known.",PO)

for i in ['west-asia.anatolia.lydia','west-asia.anatolia.mitanni','west-asia.anatolia.urartu',
          'west-asia.anatolia.phrygia','west-asia.anatolia.hittites','west-asia.arabia.pre-islamic.dilmun',
          'west-asia.arabia.pre-islamic.nabataeans','west-asia.arabia.pre-islamic.saba']:
    add(i,'kind','polity',"Each of these had a king, a capital and a chancery, so `era` is a kind error clustered in the Anatolia and Arabia blocks.",PO)

for i in ['central-asia.qara-khitai','east-asia.china.western-xia','europe.northern.kalmar',
          'southeast-asia.mainland.lan-xang','southeast-asia.maritime.tondo','southeast-asia.maritime.kahuripan',
          'west-asia.iran.aq-qoyunlu','west-asia.iran.qara-qoyunlu','oceania.polynesia.new-zealand',
          'central-asia.hephthalites']:
    add(i,'kind','polity',"A dynastic state with rulers, a capital and an administration is a polity, not an `era`.",PO)
add('central-asia.hephthalites','historicity',None,
    "The Hephthalites are attested in Sasanian, Chinese, Indian and Byzantine sources and minted coins; only their origin is contested.",PO)
add('central-asia.sogdia','kind','culture',
    "Sogdia was never politically unified, which is the `culture` case rather than a polity or an era.",PO)
add('central-asia.sogdia','historicity',None,
    "Sogdiana is documented in Achaemenid inscriptions, Greek and Chinese sources and thousands of Sogdian documents.",PO)
add('southeast-asia.mainland.dvaravati','kind','culture',
    "Dvaravati is a Mon Buddhist material horizon whose political unity is the open question, i.e. a culture.",PO)
add('southeast-asia.mainland.dvaravati','historicity',None,
    "Its existence as a culture is not contested; only its political unity is, so `contested` misreads the debate.",PO)
add('europe.reformation','kind','era',
    "A religious and political upheaval has no government, so it cannot be a polity.",PO)
add('west-asia.arabia.rise-islam','kind','era',
    "The summary describes Muhammad's prophetic career, which is a period rather than a state.",PO)
add('west-asia.anatolia.hittites.hittite-collapse','kind','event',
    "A collapse is an event, not a polity with a government inside the Hittite tree.",PO)
add('europe.mediterranean.greece','kind','era',
    "Ancient Greece never had a single government; Ancient Rome and Ancient Egypt are already eras here.",PO)
add('europe.mediterranean.greece.classical','kind','era',
    "Classical Greece is a period label covering many city-states, not one polity.",PO)
add('europe.western.britain.victorian','kind','era',
    "Victorian Britain is a period label; the polity of 1837-1901 is the United Kingdom, and the Georgian Era is already an `era`.",PO)
add('europe.western.britain.victorian','parent_id','europe.western',
    "It should sit as a sibling of The Georgian Era under Western Europe rather than under England.",PO)
add('south-asia.independence','kind','era',
    "Post-Independence South Asia is a period covering several sovereign states, not one state.",PO)
add('east-asia.china.yuan','end_year',1368,
    "1370 is Toghon Temur's death in Mongolia; the Yuan ends with the Ming capture of Dadu in 1368, which the Ming row already uses.",PO)
add('africa.nile.egypt.middle-kingdom.dyn11','start_year',-2055,
    "The reunified phase begins at -2055; -2125 is the whole Theban 11th Dynasty and starts 70 years before its parent period.",PO)
add('southeast-asia.mainland.vietnam','aliases',["Đại Việt","Đại Cồ Việt","Đại Ngu"],
    "An alias with a date range embedded in it is malformed and duplicates the first entry.",PO)

# ---------- periods ----------
add('east-asia.japan.kenmu.kenmu-era','end_year',1338,
    "The Northern court kept counting Kenmu until Ryakuo in 1338, so 1336 leaves a two-year gap in the Northern chain.",PE)
add('east-asia.japan.muromachi.shokei','parent_id','east-asia.japan.kamakura',
    "Shokei ran 1332-1333 and ended when Kamakura fell, three years before the Muromachi period begins.",PE)
add('east-asia.china.neolithic.cishan','summary',
    "A north China millet culture whose storage pits produced the claim that cereal farming here began in the early Holocene.",
    "The Cishan millet claim is c. 10,000 BP, in the early Holocene, not at the Pleistocene boundary c. 9700 BCE.",PE)
add('global.neolithic.agricultural-revolution.mesoamerica','summary',
    "Squash first, then maize and beans — the squash predates maize by roughly a thousand years.",
    "Guila Naquitz squash is c. 10,000 BP and the Balsas maize evidence c. 9,000 BP, a gap of about one millennium.",PE)
add('africa.prehistory.nabta-playa','end_year',-3451,
    "Its own Terminal Neolithic sub-phase runs to -3451, eight centuries past the parent's end.",PE)
add('east-asia.china.han.xin','start_dating_method','calendar',
    "Wang Mang's usurpation in 9 CE is dated to the day in the Han shu, so `unknown` misstates the evidence.",PE)
add('east-asia.china.han.xin','end_dating_method','calendar',
    "The fall of the Xin in 23 CE is likewise dated precisely in the Han shu.",PE)
add('europe.western.france.capetian','start_dating_method','calendar',
    "987 is the recorded election of Hugh Capet, a documentary calendar date.",PE)

# ---------- concepts ----------
add('global.prehistory.firsts.cut-marks','summary',
    "Bones from Dikika, Ethiopia bearing marks read as stone-tool butchery, roughly 90,000 years before the oldest known stone tools.",
    "This file's own stone-knapping entry puts the oldest tools at 3,300,000 BCE, 90,000 years later, not 800,000.",CO)
add('global.milestones.iron-smelting','summary',
    "Pre-Hittite Anatolian bloomery iron; the metal that made tools cheap rather than precious.",
    "The Hittite Old Kingdom begins c. 1650 BCE, so a -1900 date cannot be Hittite-era.",CO)
add('global.traditions.great-schism','kind','event',
    "The Great Schism is a dated event, not a religion, philosophy or school.",CO)
add('global.traditions.great-schism','end_year',1054,
    "A single-day event in 1054 cannot be open-ended.",CO)
add('global.traditions.great-schism','extant',None,
    "An event that happened in 1054 is not an entity continuing to the present.",CO)
add('africa.peoples-amazigh','aliases',["Berbers","Imazighen","Amazigh peoples"],
    "'Berber' is overwhelmingly the search term an English-language reader arrives with, so the entity was unreachable.",CO)

out='/home/user/workspace/hp/docs/review/corrections.json'
json.dump(C,open(out,'w'),ensure_ascii=False,indent=1)
print('entries',len(C))
from collections import Counter
print(Counter(c['field'] for c in C))
print(Counter(c['source_review'] for c in C))
# sanity: no from==to, no duplicate id+field
seen=set()
for c in C:
    assert (c['id'],c['field']) not in seen, c
    seen.add((c['id'],c['field']))
    assert c['from']!=c['to'], c
    assert c['field'] in json.load(open('/home/user/workspace/hp/schemas/entity.schema.json'))['properties'], c
print('sanity ok')
