# AGENTS.md

> Manual portable para cualquier IA que entre a este proyecto.

## Qué es este proyecto
Es el **sitio web de Lety** (lety2e.com): HTML + CSS + JS vanilla, publicado en GitHub Pages.

## Dónde está el manual completo
El manual **técnico** detallado vive en **`CLAUDE.md`** (en esta misma carpeta):
filosofía, arquitectura, estilos, fuentes de contenido y el flujo para publicar.
**Si eres una IA trabajando aquí —seas Claude u otra— lee `CLAUDE.md` antes de tocar nada.**
El manual **para Lety** (cómo se reparte el trabajo entre ella y Claude, pieza por pieza)
es **`Manual lety2E.md`**.

## Archivos del sistema de Lety (junto al código)
Además del sitio (HTML/CSS/JS), en la raíz conviven las piezas estándar del sistema:
- **`Pendientes lety2E.md`** — la bandeja de pendientes del sitio; se organiza a su manera (plan de trabajo, prioridades). El trabajo de crear —diseñar o escribir contenido del sitio— vive aquí. Si surge un accionable concreto que amerite la app Recordatorios, pregunta *"¿lo subo a Recordatorios?"* y con el ok de Lety agrégalo a su lista **agente** (vía `osascript`; única escritura de la IA allá). Este archivo queda fuera del resumen del hub (desde 11-jul-2026): Lety lo consulta aquí, en su carpeta. No la borres.
- **`bitacora lety2E.md`** — el diario del proyecto. No la borres.
- **`Manual lety2E.md`** — el manual para Lety (espejo humano).
- **`Recursos lety2E/`** — material reutilizable (plantillas, snippets, prompts; nombres libres, sin índice).

## Cómo quiero que trabajes aquí
- Lety no es muy técnica: explica en simple y guíala paso a paso.
- Da primero la **idea central**, luego los detalles.
- Pregunta si hay ambigüedad; mira el código antes de cambiarlo.
- Escribe en español.

## Al saludar
Cuando Lety abra la sesión con solo un saludo ("hola", "buenos días"…) sin pedir nada
concreto, no contestes con un saludo vacío. Recuérdale en una frase que este es su
**sitio web** (lety2e.com), revisa el estado/bitácoras que indica `CLAUDE.md` para
decirle dónde nos quedamos, y da un par de ejemplos de qué puede pedir (cambiar o
agregar contenido, retocar estilos, publicar los cambios).
Breve — es una bienvenida, no el resumen completo. Si el saludo viene con una petición,
ve directo a la petición.

---
*Wrapper portable del sistema de Lety. El contenido real y detallado está en `CLAUDE.md`.*
