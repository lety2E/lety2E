"""Índice del curso, botón siguiente del tema 2 y arreglo de paréntesis del tema 2."""
import re, html, pathlib
from comun import g
R = pathlib.Path("/Users/letymath/Desktop/lety2E/math/matematicas-4")
idx = (R / "index.html").read_text()
nuevos = [("funcion-escalonada", "Función escalonada", "🪜", "Gráfica, dominio, rango y regla de correspondencia.", g.COLORES[2]),
          ("funcion-cuadratica", "Función cuadrática", "∪", "Máximos, mínimos, raíces, crecimiento y signo desde la gráfica.", g.COLORES[3]),
          ("area-funcion-longitud", "Área como función de la longitud", "▭", "El área de un rectángulo en función de x, su dominio y el área máxima.", g.COLORES[0])]
nuevos += [("analisis-funcion", "Análisis de una función", "🔍", "Dominio, rango, máximos, mínimos, raíces, crecimiento y signo desde la gráfica.", g.COLORES[1]),
           ("esbozo-grafico", "Esbozo gráfico de una función", "✏️", "De los datos de una función a su gráfica.", g.COLORES[2]),
           ("operaciones-funciones", "Operaciones con funciones", "±", "Suma, resta, multiplicación y división de funciones.", g.COLORES[3])]
C = g.COLORES
nuevos += [("composicion-funciones", "Composición de funciones", "∘", "Una función dentro de otra, paso a paso.", C[0]),
           ("dominio-maximo", "Dominio máximo", "ℝ", "El dominio de polinomios, fracciones, raíces y logaritmos.", C[1]),
           ("ecuaciones-exponenciales-logaritmicas", "Ecuaciones exponenciales y logarítmicas", "㏒", "Leyes de exponentes y logaritmos para despejar la x.", C[2]),
           ("sucesiones-series", "Sucesiones y series", "…", "Aritméticas y geométricas: término general y suma.", C[3]),
           ("notacion-sigma", "Notación sigma", "Σ", "Sumas desarrolladas, con fórmulas y series.", C[0]),
           ("limites", "Límites", "→", "Sustitución, factorización, racionalización y límites al infinito.", C[1]),
           ("derivadas", "Derivadas", "ƒ′", "La derivada por definición.", C[2]),
           ("sumas-riemann", "Sumas de Riemann", "∫", "La integral como límite de una suma.", C[3])]
for slug, tit, emo, desc, col in nuevos:
    if f'href="{slug}.html"' in idx:
        continue
    g.enlazar("representacion-funciones" if slug == "funcion-escalonada" else None, slug, tit, emo, tit, desc, col)
    idx = (R / "index.html").read_text()

