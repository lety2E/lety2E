#!/usr/bin/env python3
"""Reparte los reactivos del banco entre las versiones del examen.

Cada tema trae su receta (ver banco.py). Dos modos:

  bloques     El bloque del sitio ES el tema: entra completo. Cada version se
              lleva un bloque distinto de los de ejercicios y otro de los
              extra. Se emparejan buscando que no se repita ningun ejercicio.

  por bloque  Se toman N ejercicios de CADA bloque, no el bloque entero.
              Ecuaciones: uno del bloque de resueltos y uno de cada bloque
              extra. Cada bloque arranca en un renglon distinto, para que a
              una misma version no le toquen tres veces el mismo molde.
              La receta puede limitar cuantos bloques se usan de cada seccion:
              en Expresiones algebraicas hay dos bloques resueltos pero solo
              el primero entra al examen; el segundo queda de practica.

  ejercicios  Se toman ejercicios sueltos. Si los bloques del sitio son
              paralelos (mismo largo), cada version toma el MISMO tipo de
              ejercicio de un bloque distinto, para que las versiones sean
              equivalentes y no le toque a uno la division y a otro la raiz.

En los dos modos: ningun ejercicio se repite entre versiones.
"""
import json, sys

def matriz(bloques, n):
    """Bloques paralelos -> una pila por slot, con su tramo de columnas."""
    if len(bloques) < 2: return None
    largos = {len(b[1]) for b in bloques}
    if len(largos) != 1: return None
    T = largos.pop()
    if T < n: return None
    cortes = [j * T // n for j in range(n)] + [T]
    pilas = []
    for j in range(n):
        col = []
        for c in range(cortes[j], cortes[j+1]):
            col += [b[1][c] for b in bloques]
        pilas.append(col)
    return pilas

def plano(bloques, n):
    """Sin bloques paralelos: se aplana y se parte en n tramos, uno por slot."""
    items = [x for b in bloques for x in b[1]]
    if not items: return [[] for _ in range(n)]
    tam = max(1, len(items) // n)
    segs = [items[j*tam:(j+1)*tam] for j in range(n)]
    segs[-1] += items[n*tam:]
    return segs

def pilas(bloques, n):
    m = matriz(bloques, n)
    return m if m is not None else plano(bloques, n)

def repartir(total, k):
    base, resto = divmod(total, k)
    return [base + (1 if i < resto else 0) for i in range(k)]

def regrupar(seccion, tam, metodo='seguido'):
    """Rehace los bloques de tam ejercicios a partir de los del sitio.

    seguido   corta la lista de tam en tam, en el orden publicado. Sirve
              cuando el sitio ya los trae alternados (Expresiones algebraicas).
    mitades   dentro de cada bloque del sitio, empareja la primera mitad con
              la segunda. Sirve cuando el bloque va con todos los de un tipo
              y luego todos los del otro (Jerarquia: A,A,B,B).
    """
    if metodo == 'mitades':
        bloques = []
        for _, items in seccion:
            partes = len(items) // tam
            if partes < 1: continue
            # items[k], items[k+partes], items[k+2*partes]...  = uno de cada tipo
            for k in range(partes):
                bloques.append([None, [items[k + p*partes] for p in range(tam)]])
    else:
        plano = [x for _, items in seccion for x in items]
        bloques = [[None, plano[k:k+tam]]
                   for k in range(0, len(plano) - tam + 1, tam)]
    for i, b in enumerate(bloques):
        b[0] = 'Bloque de %d (#%d)' % (tam, i + 1)
    return bloques

def por_bloques(tema, V):
    """El bloque entra completo. Empareja un bloque con respuesta con uno extra
    procurando que no se repita ningun ejercicio (el sitio tiene algunos
    repetidos entre bloques, p.ej. la misma raiz)."""
    receta = tema['receta']
    modo, nR, nE = receta[:3]
    tam = receta[3] if len(receta) > 3 else None
    metodo = receta[4] if len(receta) > 4 else 'seguido'
    R, E = tema['con_respuesta'], tema['extras']
    if tam:
        R, E = regrupar(R, tam, metodo), regrupar(E, tam, metodo)
    faltan = max(0, V - len(R)//max(nR,1)) + max(0, V - len(E)//max(nE,1))

    usadosR, usadosE, vistos = set(), set(), set()
    versiones, choques = [], 0
    for v in range(V):
        libresR = [i for i in range(len(R)) if i not in usadosR]
        libresE = [j for j in range(len(E)) if j not in usadosE]
        if len(libresR) < nR or len(libresE) < nE:
            versiones.append([]); continue
        # elegir el par que menos ejercicios repita
        mejor, costo_mejor = None, None
        for i in libresR:
            for j in libresE:
                items = [clave(x) for x in R[i][1]] + [clave(x) for x in E[j][1]]
                costo = len(items) - len(set(items))                 # dentro del par
                costo += sum(1 for k in set(items) if k in vistos)   # con lo ya usado
                if costo_mejor is None or costo < costo_mejor:
                    mejor, costo_mejor = (i, j), costo
                if costo == 0: break
            if costo_mejor == 0: break
        i, j = mejor
        usadosR.add(i); usadosE.add(j); choques += costo_mejor
        fila = ([dict(x, origen='respuesta') for x in R[i][1]] +
                [dict(x, origen='extra') for x in E[j][1]])
        vistos.update(clave(x) for x in fila)
        versiones.append(fila)
    return versiones, {'modo': 'bloques', 'falta': faltan, 'choques': choques,
                       'r_disp': len(R), 'e_disp': len(E)}

def uno_por_bloque(tema, V):
    """N ejercicios de cada bloque. Los bloques del sitio son paralelos (el
    renglon k es el mismo molde en todos), asi que cada bloque se recorre con
    un desfase distinto para que la version no repita molde."""
    receta = tema['receta']
    _, nR, nE = receta[:3]
    topeR = receta[3] if len(receta) > 3 else None   # cuantos bloques usar
    topeE = receta[4] if len(receta) > 4 else None
    bloques = ([(b, 'respuesta', nR) for b in tema['con_respuesta'][:topeR]] +
               [(b, 'extra', nE) for b in tema['extras'][:topeE]])
    versiones, falta = [], 0
    for v in range(V):
        fila = []
        for i, ((_, items), origen, cuantos) in enumerate(bloques):
            if not items: continue
            for k in range(cuantos):
                idx = v * cuantos + k + i * 2          # el desfase por bloque
                if v * cuantos + k >= len(items):
                    falta += 1; continue
                item = dict(items[idx % len(items)]); item['origen'] = origen
                fila.append(item)
        versiones.append(fila)
    return versiones, {'modo': 'por bloque', 'falta': falta,
                       'r_disp': sum(len(i) for _, i in tema['con_respuesta']),
                       'e_disp': sum(len(i) for _, i in tema['extras'])}

def seleccionar(tema, V):
    if tema['receta'][0] == 'bloques':
        return por_bloques(tema, V)
    if tema['receta'][0] == 'por bloque':
        return uno_por_bloque(tema, V)
    _, r_pv, e_pv = tema['receta']
    n = r_pv + e_pv
    R, E = tema['con_respuesta'], tema['extras']
    r_disp = sum(len(b[1]) for b in R)
    e_disp = sum(len(b[1]) for b in E)
    necesario = V * n

    e_uso = min(e_disp, e_pv * V)
    r_uso = necesario - e_uso
    if r_uso > r_disp:
        r_uso = r_disp
        e_uso = necesario - r_uso
    falta = max(0, e_uso - e_disp)                # no alcanza: hay que publicar mas
    if falta: e_uso = e_disp

    r_por_version = repartir(r_uso, V)
    pilaR, pilaE = pilas(R, n), pilas(E, n)
    usoR, usoE = [0]*len(pilaR), [0]*len(pilaE)
    versiones = []
    for v in range(V):
        slots_r = {(v + i) % n for i in range(r_por_version[v])}
        fila = []
        for j in range(n):
            desde_r = j in slots_r
            pila, uso = (pilaR, usoR) if desde_r else (pilaE, usoE)
            k = j % len(pila)
            if uso[k] >= len(pila[k]):                     # ese tipo se agoto
                alt = [i for i in range(len(pila)) if uso[i] < len(pila[i])]
                if alt:
                    k = alt[0]
                else:                                      # cambiar de lista
                    otra, otro = (pilaE, usoE) if desde_r else (pilaR, usoR)
                    alt2 = [i for i in range(len(otra)) if otro[i] < len(otra[i])]
                    if not alt2: continue
                    pila, uso, k, desde_r = otra, otro, alt2[0], not desde_r
            item = dict(pila[k][uso[k]]); uso[k] += 1
            item['origen'] = 'respuesta' if desde_r else 'extra'
            fila.append(item)
        versiones.append(fila)
    return versiones, {'modo': 'ejercicios', 'r_uso': r_uso, 'e_uso': e_uso,
                       'falta': falta, 'r_disp': r_disp, 'e_disp': e_disp}

def clave(x): return x.get('tex') or x.get('svg')

def construir(banco, V):
    # Un reactivo que ya esta en "Ejercicios" no puede volver a contarse como
    # extra. Solo aplica al modo ejercicios: en modo bloques el bloque entra
    # completo, y las repeticiones se resuelven emparejando bloques.
    for t in banco:
        if t['receta'][0] == 'bloques': continue
        ya = {clave(x) for b in t['con_respuesta'] for x in b[1]}
        limpios, quitados = [], 0
        for nombre, items in t['extras']:
            keep = [x for x in items if clave(x) not in ya]
            quitados += len(items) - len(keep)
            if keep: limpios.append([nombre, keep])
        if quitados:
            print('   (aviso) %s: %d extra(s) que ya estaban en Ejercicios, descartados'
                  % (t['titulo'], quitados))
        t['extras'] = limpios

    salida = []
    for t in banco:
        vers, info = seleccionar(t, V)
        salida.append({'titulo': t['titulo'], 'archivo': t['archivo'],
                       'receta': t['receta'], 'versiones': vers, 'info': info})
    return salida

if __name__ == '__main__':
    V = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    banco = json.load(open('banco.json'))
    salida = construir(banco, V)

    print('\n%-26s %-13s %-9s %s'
          % ('TEMA', 'modo', 'x version', 'ejercicios en cada version'))
    for s in salida:
        cuantos = ' '.join(str(len(v)) for v in s['versiones'])
        unidad = 'bloque(s)' if s['info']['modo']=='bloques' else 'ejercicios'
        aviso = ''
        if s['info']['falta']:
            aviso = '   <-- FALTAN %d %s' % (s['info']['falta'], unidad)
        if s['info'].get('choques'):
            aviso += '   (%d repetido[s] entre bloques del sitio)' % s['info']['choques']
        etiqueta = s['info']['modo']
        if s['receta'][0] == 'bloques' and len(s['receta']) > 3:
            etiqueta += ' de %d' % s['receta'][3]
        print('%-26s %-13s %d+%-7d %s%s'
              % (s['titulo'], etiqueta, s['receta'][1], s['receta'][2],
                 cuantos, aviso))

    problemas = 0
    for s in salida:
        claves = [clave(x) for v in s['versiones'] for x in v]
        if len(claves) != len(set(claves)):
            print('  !! %s: hay ejercicios repetidos' % s['titulo']); problemas += 1
        esperado = max(len(v) for v in s['versiones']) if s['versiones'] else 0
        incompletas = [i+1 for i, v in enumerate(s['versiones']) if len(v) < esperado]
        if incompletas:
            print('  !! %s: versiones incompletas %s' % (s['titulo'], incompletas)); problemas += 1
    print('\nEjercicios por version: %d' % sum(len(s['versiones'][0]) for s in salida))
    print('Revision: %s' % ('todo bien' if not problemas else '%d problema(s)' % problemas))
    json.dump(salida, open('seleccion.json','w'), ensure_ascii=False, indent=1)
