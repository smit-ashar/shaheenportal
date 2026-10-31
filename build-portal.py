#!/usr/bin/env python3
"""Regenerates index.html from manifest.json. A chapter is 'ready' when
<class>/<subject>/<chapter-id>/index.html exists. Run after adding a chapter."""
import json,os
here=os.path.dirname(os.path.abspath(__file__))
m=json.load(open(f'{here}/manifest.json'))
n=0
for c in m['classes']:
    for s in c['subjects']:
        for ch in s['chapters']:
            ok=os.path.exists(f"{here}/{c['id']}/{s['id']}/{ch['id']}/index.html")
            ch['status']='ready' if ok else 'soon'; n+=ok
            if ok:
                fp=f"{here}/{c['id']}/{s['id']}/{ch['id']}/index.html";txt=open(fp,encoding='utf8').read()
                ch['slides']=txt.count('<section class="sh-slide');ch['kb']=os.path.getsize(fp)//1024
                import time;ch['updated']=time.strftime('%d %b %Y',time.localtime(os.path.getmtime(fp)))
t=open(f'{here}/portal.template.html').read()
open(f'{here}/index.html','w').write(t.replace('/*MANIFEST*/null',json.dumps(m)))
json.dump(m,open(f'{here}/manifest.json','w'),indent=1)
print('portal built,',n,'chapter(s) ready')
