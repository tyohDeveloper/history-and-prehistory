import json, re, os, sys

REPO='/home/user/workspace/hp'
files=['review-findings-reigns.md','review-findings-cities-1.md','review-findings-cities-2.md',
       'review-findings-polities.md','review-findings-periods.md','review-findings-concepts.md']

findings=[]
for f in files:
    path=os.path.join(REPO,'docs',f)
    text=open(path).read()
    lines=text.split('\n')
    # split on '### ' headings
    idxs=[i for i,l in enumerate(lines) if l.startswith('### ')]
    for n,i in enumerate(idxs):
        end=idxs[n+1] if n+1<len(idxs) else len(lines)
        block=lines[i:end]
        head=block[0][4:].strip()
        body='\n'.join(block[1:])
        def grab(key):
            m=re.search(r'^\*\*'+key+r':\*\*(.*?)(?=^\*\*[A-Z]|\Z)', body, re.S|re.M)
            return m.group(1).strip() if m else None
        conf=grab('Confidence')
        findings.append({'file':f,'heading':head,'field':grab('Field'),
                         'currently':grab('Currently'),'should':grab('Should be'),
                         'confidence':(conf or '').split()[0].lower().strip('`*') if conf else None,
                         'why':grab('Why'),'raw':'\n'.join(block)})
json.dump(findings,open(os.path.join(REPO,'docs/review/all_findings.json'),'w'),indent=1)
from collections import Counter
print(len(findings))
print(Counter((x['file'],x['confidence']) for x in findings))
