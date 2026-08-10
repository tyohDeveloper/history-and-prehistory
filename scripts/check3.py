import json
d=json.load(open('/home/user/workspace/hp/src/data/entities.json'))
es=d['entities']; byid={e['id']:e for e in es}
print("== consensus thresholds")
for n in ['cooking','figurative-art','pigment-use','spun-fibre','stone-knapping','wood-structure','woven-cloth','pottery']:
    e=byid.get('global.prehistory.firsts.'+n)
    print(n, e.get('date_standing') if e else 'MISSING')
print("== georgian")
e=byid['europe.western.britain.georgian']; print({k:e.get(k) for k in ['kind','parent_id','start_year','end_year']})
print("== taihe-dali")
e=byid['east-asia.city-taihe-dali']; print({k:e.get(k) for k in ['name','aliases','kind']})
print("== nengo sample")
nen="""east-asia.japan.asuka.hakuchi keiun shucho taiho taika""".split()
ids=['east-asia.japan.asuka.'+x for x in ['hakuchi','keiun','shucho','taiho','taika']]
ids+=['east-asia.japan.nara.'+x for x in ['enryaku','hoki','jingo-keiun','jinki','reiki','ten-o','tenpyo','tenpyo-hoji','tenpyo-jingo','tenpyo-kanpo','tenpyo-shoho','wado','yoro']]
ids+=['east-asia.japan.heian.'+x for x in ['anna','choho-heian','chotoku','daido','eien','eikan','eiso','encho','engi','gangyo','jogan','jogen-heian1','johei','jowa-heian','kanna','kanpyo-heian','kasho-heian','koho','konin','ninju','ninna','owa','saiko','shoryaku','shotai','ten-an','ten-en','tencho','tengen','tengyo','tenroku','tenryaku','tentoku']]
miss=[i for i in ids if i not in byid]
print('count',len(ids),'missing',miss)
from collections import Counter
print(Counter((byid[i].get('start_dating_method'),byid[i].get('end_dating_method')) for i in ids if i in byid))
print("== polities pattern-1 list")
names=['Tang Dynasty','Abbasid','Rashidun','Umayyad','Kievan','Carolingian','Song Dynasty','Sui','Goryeo','Silla','Khmer','Đinh','Lê','Ngô','Heian','Nara','Holy Roman','Buyid','Saffarid','Tahirid','Fatimid','Chola','Harsha','Rashtrakuta','Chalukya','Uyghur','Five Dynasties','Liao']
for n in names:
    for e in es:
        if n.lower() in e.get('name','').lower() and e.get('kind') in ('polity','era','period'):
            print(n,'|',e['id'],'|',e['name'],'|',e.get('kind'),e.get('start_year'),e.get('end_year'),e.get('start_dating_method'),e.get('end_dating_method'))
