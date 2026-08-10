import json,sys,re
d=json.load(open('/home/user/workspace/hp/src/data/entities.json'))
es=d['entities']
byid={e['id']:e for e in es}
def show(e,keys=None):
    print(json.dumps({k:v for k,v in e.items() if k not in ('date_note','name_forms','citations','sources')},ensure_ascii=False,indent=1))
for a in sys.argv[1:]:
    if a in byid:
        print('--- EXACT',a); show(byid[a])
    else:
        print('--- NOMATCH id:',a)
        pat=a.split('.')[-1].replace('-',' ')
        hits=[e for e in es if a.lower() in e['id'].lower() or pat.lower() in e.get('name','').lower()]
        for h in hits[:10]: print('   cand:',h['id'],'|',h.get('name'),'|',h.get('kind'))
