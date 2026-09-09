#!/usr/bin/env python3
"""Lee las paginas de temas del sitio lety2E y saca los reactivos.
SOLO LECTURA: nunca escribe nada dentro de la carpeta del sitio."""
import sys, os, json, re
from html.parser import HTMLParser
from html import unescape

class Node:
    __slots__=('tag','attrs','kids','parent')
    def __init__(self, tag, attrs=None):
        self.tag=tag; self.attrs=dict(attrs or []); self.kids=[]; self.parent=None
    def cls(self): return self.attrs.get('class','').split()

VOID={'br','img','hr','meta','link','input','path','polyline','circle','line','rect',
      'use','source','col','area','base','embed','track','wbr','ellipse','polygon','stop'}

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root=Node('root'); self.stack=[self.root]
    def _add(self,n):
        n.parent=self.stack[-1]; self.stack[-1].kids.append(n)
    def handle_starttag(self,tag,attrs):
        n=Node(tag,attrs); self._add(n)
        if tag not in VOID: self.stack.append(n)
    def handle_startendtag(self,tag,attrs): self._add(Node(tag,attrs))
    def handle_endtag(self,tag):
        if tag in VOID: return
        for i in range(len(self.stack)-1,0,-1):
            if self.stack[i].tag==tag: del self.stack[i:]; return
    def handle_data(self,d):
        if d.strip(): self.stack[-1].kids.append(d)

def annot(n):
    """El LaTeX original que KaTeX deja guardado al pre-renderizar."""
    if isinstance(n,str): return None
    if n.tag=='annotation' and n.attrs.get('encoding')=='application/x-tex':
        return ''.join(k for k in n.kids if isinstance(k,str))
    for k in n.kids:
        r=annot(k)
        if r is not None: return r
    return None

def text(n):
    if isinstance(n,str): return n
    if n.tag in ('script','style','svg'): return ''
    if 'katex' in n.cls():
        t=annot(n); return ' $'+t.strip()+'$ ' if t else ''
    return ''.join(text(k) for k in n.kids)

def clean(s):
    s=unescape(s).replace('​','').replace('\xa0',' ')
    return re.sub(r'\s+',' ',s).strip()

def walk(n):
    if isinstance(n,str): return
    yield n
    for k in n.kids: yield from walk(k)

def svg_label(n):
    for x in walk(n):
        if not isinstance(x,str) and x.tag=='svg' and x.attrs.get('aria-label'):
            return '[FIGURA] '+clean(x.attrs['aria-label'])
    return ''

def items_of(body):
    """Reactivos de un contenedor. El sitio los marca de varias formas segun
    el tema: ej-line, ej-row, tarjetas con figura, <li>, o sueltos."""
    ejl=[clean(text(x)) for x in walk(body) if not isinstance(x,str) and 'ej-line' in x.cls()]
    ejl=[e for e in ejl if e]
    if ejl: return ejl
    ejr=[clean(text(x)) or svg_label(x) for x in walk(body)
         if not isinstance(x,str) and ('ej-row' in x.cls() or 'ejer-card-body' in x.cls())]
    ejr=[e for e in ejr if e]
    if ejr: return ejr
    lis=[clean(text(x)) for x in walk(body) if not isinstance(x,str) and x.tag=='li']
    lis=[e for e in lis if e]
    if lis: return lis
    out=[]
    for k in body.kids:
        if isinstance(k,str):
            t=clean(k)
            if t: out.append(t)
        elif 'katex' in k.cls() or k.tag in ('p','div'):
            t=clean(text(k))
            if t: out.append(t)
    return out

def parse_file(path):
    p=P(); p.feed(open(path,encoding='utf-8').read())
    out=[]
    for sec in walk(p.root):
        if isinstance(sec,str) or 'section-block' not in sec.cls(): continue
        h2=next((clean(text(x)) for x in walk(sec) if not isinstance(x,str) and x.tag=='h2'),None)
        if not h2: continue
        cards=[]
        for c in walk(sec):
            if isinstance(c,str) or 'mini-card' not in c.cls(): continue
            head=next((clean(text(x)) for x in walk(c)
                       if not isinstance(x,str) and 'mini-card-head' in x.cls()),'')
            body=next((x for x in walk(c)
                       if not isinstance(x,str) and 'mini-card-body' in x.cls()),None)
            it=items_of(body) if body is not None else []
            if it: cards.append({'bloque':head,'items':it})
        if not cards:
            it=items_of(sec)
            if it: cards=[{'bloque':'','items':it}]
        if cards: out.append({'seccion':h2,'cards':cards})
    return out

if __name__=='__main__':
    base=os.path.expanduser(sys.argv[1]); res={}
    for f in sorted(os.listdir(base)):
        if not f.endswith('.html') or f=='index.html': continue
        res[f]=parse_file(os.path.join(base,f))
    print(json.dumps(res,ensure_ascii=False,indent=1))
