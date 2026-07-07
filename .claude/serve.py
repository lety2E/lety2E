#!/usr/bin/env python3
# Preview local del sitio en http://127.0.0.1:8765/
# Uso normal (desde Claude Code): python3 .claude/serve.py &
# El panel de preview de la app no puede leer Desktop (permisos de macOS);
# si algún día se usa, copiar este archivo a /tmp/lety_serve.py (ver launch.json).
# La ruta va fija (no relativa a __file__) justo por esa copia a /tmp.
import os
os.chdir('/Users/letymath/Desktop/lety2E')
from http.server import HTTPServer, SimpleHTTPRequestHandler
HTTPServer(('127.0.0.1', 8765), SimpleHTTPRequestHandler).serve_forever()
