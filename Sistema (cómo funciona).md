# Sistema — cómo funciona lety2E

> Cómo construimos el sitio entre Lety y Claude. La idea es repartir el trabajo
> para no gastar tokens de más y que cada quien haga lo que mejor le sale.

---

## 🧩 La idea en una frase

Lety prepara la materia prima (capturas + un borrador base) y Claude la convierte
en la página final con el formato establecido y la sube a GitHub. El sitio se
construye **pieza por pieza**: temas de Math, artefactos de Apuntes, y más adelante
canciones, etc.

---

## 📐 Parte 1 — **Math**

Hay dos formas de trabajar un tema de matemáticas:

### A) Migración (lo más común por ahora)

**Lo que hace Lety:**
1. Tiene sus **capturas** del tema.
2. Con **Gemini + las capturas** genera el **borrador** (código LaTeX o HTML).
   Se hace en Gemini para **ahorrar tokens** aquí — pero el borrador **no se queda
   en Gemini**.
3. Sube ese código a un **doc en Drive**, **un tema por pestaña**.
4. Me avisa a mí (Claude): *"checa el tema **X** de tal curso"* (está en el **Drive**),
   y me pasa los **enlaces de YouTube** del tema.

**Lo que hace Claude:**
5. **Revisa** el material (doc en Drive + capturas).
6. **Arma el HTML** con el **formato establecido** (patrón "paquetito").
7. **Lo sube a GitHub** (Pages publica en 1-2 min).

### B) Desde cero

Habrá temas que **no** vengan de capturas, sino que los hagamos **desde cero**
entre los dos. Mismo formato y mismo cierre (Claude arma el HTML y lo sube).

> Fuentes de verdad para Math: doc en Drive (manda) · capturas en
> `~/Desktop/capturas/` · CSV de videos. Si el doc y la captura difieren, gana el doc.

---

## 🗂️ Parte 2 — **Apuntes** (artefactos)

1. Entre los dos **armamos un artefacto** de algún tema.
2. Claude lo **sube** a GitHub.

Los apuntes son self-contained (cada uno con su propio CSS/JS). Se irán acumulando
como lista plana.

---

## 🎵 Lo que viene

Con la misma lógica iremos construyendo **más artefactos, canciones, etc.** —
cada tipo se suma cuando hay material real (nunca se inventa para llenar).

---

*Archivo de referencia rápida. El detalle técnico para Claude vive en `CLAUDE.md`.*
