#!/usr/bin/env python3
"""
subset-fuentes.py — lety2E

Recorta las tipografías del sitio. Se corre a mano, no en cada publicación:
sólo hace falta si se cambian las fuentes o si aparece un carácter nuevo que
salga con la letra equivocada.

Qué hace y por qué:

1. DM Sans es una fuente VARIABLE con dos ejes: wght 100-1000 y opsz 9-40.
   El sitio sólo usa pesos 300-700, así que el resto del eje se recorta.
   El eje opsz se CONSERVA: fijarlo ahorraría 16 KB más, pero ensancha 10%
   los números grandes de las tarjetas en math/index.html (medido). Con el
   eje vivo el render es idéntico al original, píxel por píxel.

2. Playfair Display es estática (peso 900). Sólo se le recortan caracteres.

3. El juego de caracteres es ASCII + Latin-1 completo (À-ÿ) + puntuación
   tipográfica + todo lo que el sitio usa hoy. Se conserva Latin-1 entero
   aunque hoy no se use, para que un nombre extranjero (Gödel, François) no
   salga con una letra de otra fuente a media palabra.

4. Los archivos *-latin-ext.woff2 NO se tocan: con contenido en español nunca
   se descargan (su unicode-range no coincide), así que no cuestan nada y
   quedan como red de seguridad si algún día aparece un carácter raro.

Uso:  python3 "Recursos lety2E/subset-fuentes.py"
Requiere fontTools (ya instalado: pip3 install --user fonttools brotli)
"""
import os, re, subprocess, sys, shutil
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FUENTES = os.path.join(RAIZ, 'assets', 'fonts')
ORIGINALES = os.path.join(FUENTES, 'originales')   # copia intacta, por si hay que rehacer


def caracteres_del_sitio():
    """Todo el texto visible del sitio (sin etiquetas, scripts ni el LaTeX oculto)."""
    usados = set()
    for base, _, files in os.walk(RAIZ):
        if '/.git' in base or 'Recursos lety2E' in base or 'assets' in base:
            continue
        for f in files:
            if not f.endswith('.html'):
                continue
            s = open(os.path.join(base, f), encoding='utf8', errors='replace').read()
            if '<body' in s:
                s = s[s.index('<body'):]
            s = re.sub(r'<script[\s\S]*?</script>', '', s)
            s = re.sub(r'<style[\s\S]*?</style>', '', s)
            s = re.sub(r'<annotation[\s\S]*?</annotation>', '', s)
            s = re.sub(r'<[a-zA-Z/!?][^>]*>', ' ', s)
            for e, c in [('&amp;','&'),('&lt;','<'),('&gt;','>'),('&quot;','"'),
                         ('&#39;',"'"),('&nbsp;',' '),('&middot;','·'),('&copy;','©')]:
                s = s.replace(e, c)
            s = re.sub(r'&[#\w]+;', '', s)
            usados |= set(s)
    return {c for c in usados if c.isprintable() and not c.isspace()}


def juego_de_caracteres():
    ascii_ = {chr(c) for c in range(0x20, 0x7F)}
    latin1 = {chr(c) for c in range(0xC0, 0x100)}          # À-ÿ, nombres extranjeros
    esp    = set('áéíóúüñÁÉÍÓÚÜÑ¿¡')
    punt   = set('°ªº«»·–—‘’“”…•€×÷±≈≤≥→←↑↓™©®′″‹›§¶†‡')
    return ''.join(sorted(ascii_ | latin1 | esp | punt | caracteres_del_sitio()))


def recortar(origen, destino, texto, limites_ejes=None):
    tmp = destino + '.tmp'
    if limites_ejes:
        f = TTFont(origen, recalcBBoxes=False)
        f = instancer.instantiateVariableFont(f, limites_ejes, updateFontNames=False, inplace=True)
        f.flavor = 'woff2'
        f.save(tmp)
        origen = tmp
    subprocess.run(['pyftsubset', origen, f'--output-file={destino}', '--flavor=woff2',
                    '--layout-features=*', '--no-hinting', '--drop-tables+=DSIG',
                    f'--text={texto}'], check=True, capture_output=True)
    if os.path.exists(tmp):
        os.remove(tmp)


TRABAJOS = [
    # archivo,                            límites de ejes variables
    ('DMSans-normal-latin.woff2',         {'wght': (300, 700)}),   # opsz se conserva a propósito
    ('PlayfairDisplay-normal-latin.woff2', None),
    ('PlayfairDisplay-italic-latin.woff2', None),
]

def main():
    if not shutil.which('pyftsubset'):
        sys.exit('falta pyftsubset — pip3 install --user fonttools brotli')
    os.makedirs(ORIGINALES, exist_ok=True)
    texto = juego_de_caracteres()
    print(f'juego de caracteres: {len(texto)}\n')
    antes = despues = 0
    for archivo, ejes in TRABAJOS:
        actual = os.path.join(FUENTES, archivo)
        guardado = os.path.join(ORIGINALES, archivo)
        if not os.path.exists(guardado):          # primera vez: guardar el original
            shutil.copy2(actual, guardado)
        a = os.path.getsize(guardado)
        recortar(guardado, actual, texto, ejes)   # siempre se parte del ORIGINAL
        d = os.path.getsize(actual)
        antes += a; despues += d
        print(f'  {archivo:38} {a/1024:6.1f} → {d/1024:5.1f} KB  (-{100*(a-d)/a:.0f}%)')
    print(f'\n  por carga de página: {antes/1024:.1f} → {despues/1024:.1f} KB  (-{100*(antes-despues)/antes:.0f}%)')

if __name__ == '__main__':
    main()
