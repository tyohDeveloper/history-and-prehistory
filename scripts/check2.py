import json
d=json.load(open('/home/user/workspace/hp/src/data/entities.json'))
es=d['entities']; byid={e['id']:e for e in es}
ids="""africa.city-kahun
africa.city-giza-workers
africa.city-nuri
africa.city-musawwarat
africa.city-igbo-ukwu
africa.city-koumbi-tegdaoust-note
europe.city-dodona
europe.city-isthmia
europe.city-jelling
europe.city-durrington-walls
europe.city-emain-macha
americas.city-acre-geoglyphs
americas.city-hopewell-earthworks
americas.city-newark-earthworks
americas.city-fort-ancient
americas.city-san-agustin
americas.city-tierradentro
americas.city-sitio-conte
americas.city-marajo
africa.city-ghat
africa.city-kerma
africa.city-raqqada
europe.city-itil
east-asia.city-taihe
east-asia.city-jeonju
europe.mediterranean.rome.empire.constantinian
europe.western.britain.victorian
europe.western.georgian
europe.reformation
west-asia.arabia.rise-islam
west-asia.anatolia.hittites.hittite-collapse
europe.mediterranean.greece
europe.mediterranean.greece.classical
south-asia.independence
central-asia.qara-khitai
east-asia.china.western-xia
europe.northern.kalmar
southeast-asia.mainland.lan-xang
southeast-asia.maritime.tondo
southeast-asia.maritime.kahuripan
central-asia.hephthalites
west-asia.iran.aq-qoyunlu
west-asia.iran.qara-qoyunlu
oceania.polynesia.new-zealand
central-asia.sogdia
southeast-asia.mainland.dvaravati
east-asia.china.yuan
africa.nile.egypt.middle-kingdom.dyn11
southeast-asia.mainland.vietnam
east-asia.japan.kenmu.kenmu-era
east-asia.japan.muromachi.shokei
east-asia.japan.kamakura
east-asia.china.neolithic.cishan
global.neolithic.agricultural-revolution.mesoamerica
africa.prehistory.nabta-playa
africa.prehistory.nabta-playa.terminal-neolithic
global.prehistory.firsts.cut-marks
global.prehistory.firsts.stone-knapping
global.prehistory.firsts.cooking
global.milestones.iron-smelting
global.traditions.great-schism
africa.peoples-amazigh
oceania.peoples-aboriginal-australians
east-asia.china.han.xin
europe.western.france.capetian
global.languages.avestan
global.prehistory.hominins.homo-luzonensis""".split()
KEYS=['kind','name','start_year','end_year','extant','aliases','historicity','date_standing','start_dating_method','end_dating_method','parent_id','summary']
for i in ids:
    e=byid.get(i)
    if not e:
        print('MISSING',i)
        pat=i.split('.')[-1].replace('-',' ')
        for h in es:
            if pat.lower() in h.get('name','').lower() or i.split('.')[-1] in h['id']:
                print('    cand:',h['id'],'|',h.get('name'),'|',h.get('kind'))
        continue
    print(i, {k:e.get(k) for k in KEYS if k in e})
