#!/usr/bin/env python3
"""Genera landing/dist/, que es lo que se publica en Cloudflare Pages.

index.html está escrito para el visor de artifacts de Claude, que le añade el
<!doctype>, el <head> y las metas al publicar. Un hosting normal no hace eso, así
que este script envuelve el mismo contenido en un documento HTML completo, añade
las metas para compartir en redes, genera el icono y la imagen de Open Graph, y
copia las imágenes.

    python3 landing/build.py

Salida: landing/dist/
"""

import re
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

# ── Rellena esto cuando el dominio esté apuntando ────────────────────────────
# Sin dominio, las metas de Open Graph usan rutas relativas: funcionan en la
# mayoría de sitios, pero WhatsApp y Facebook son más fiables con la URL completa.
SITIO = ""  # p. ej. "https://cocumorigin.com"
# ─────────────────────────────────────────────────────────────────────────────

TITULO = "Cocum Origin"
DESCRIPCION = "Cocum Origin abre próximamente en Guardamar del Segura."

AQUI = Path(__file__).resolve().parent
IMG = AQUI / "img"
DIST = AQUI / "dist"


def imagen_og():
    """Tarjeta 1200x630 para WhatsApp, Facebook e Instagram."""
    fondo = Image.open(IMG / "fondo.webp").convert("RGB")
    w, h = fondo.size
    alto = round(w / (1200 / 630))
    fondo = fondo.crop((0, (h - alto) // 2, w, (h - alto) // 2 + alto))
    fondo = fondo.resize((1200, 630), Image.LANCZOS)

    # mismo velo que la web: oscurece el centro para que el crema destaque
    velo = Image.new("L", (1200, 630), 0)
    ImageDraw.Draw(velo).ellipse((-180, -200, 1380, 830), fill=150)
    velo = velo.filter(ImageFilter.GaussianBlur(120))
    fondo = Image.composite(Image.new("RGB", (1200, 630), (9, 13, 7)), fondo, velo)

    simbolo = Image.open(IMG / "marca-alpha.png").convert("RGBA")
    simbolo = simbolo.resize((168, 168), Image.LANCZOS)
    fondo.paste(simbolo, (516, 128), simbolo)

    marca = Image.open(IMG / "cocum-wordmark.png").convert("RGBA")
    ancho = 560
    marca = marca.resize((ancho, round(ancho * marca.size[1] / marca.size[0])), Image.LANCZOS)
    fondo.paste(marca, ((1200 - ancho) // 2, 330), marca)

    fondo.save(IMG / "og.jpg", "JPEG", quality=88, optimize=True)


def iconos():
    """Icono de pestaña: símbolo dorado sobre cuadrado oscuro redondeado."""
    simbolo = Image.open(IMG / "marca-alpha.png").convert("RGBA")
    for lado, nombre in ((180, "apple-touch-icon.png"), (64, "favicon.png")):
        lienzo = Image.new("RGBA", (lado, lado), (0, 0, 0, 0))
        mascara = Image.new("L", (lado, lado), 0)
        radio = round(lado * 0.22)
        ImageDraw.Draw(mascara).rounded_rectangle((0, 0, lado - 1, lado - 1), radio, fill=255)
        lienzo.paste(Image.new("RGBA", (lado, lado), (18, 21, 14, 255)), (0, 0), mascara)
        s = round(lado * 0.72)
        pequeno = simbolo.resize((s, s), Image.LANCZOS)
        lienzo.paste(pequeno, ((lado - s) // 2, (lado - s) // 2), pequeno)
        lienzo.save(IMG / nombre)


def html():
    fuente = (AQUI / "index.html").read_text(encoding="utf-8")

    # la meta de viewport-fit sólo la entiende el visor de artifacts
    fuente = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\s*', "", fuente)

    corte = fuente.index("</style>") + len("</style>")
    cabeza, cuerpo = fuente[:corte], fuente[corte:]

    base = SITIO.rstrip("/")
    og_img = f"{base}/img/og.jpg" if base else "img/og.jpg"
    canon = f'\n  <link rel="canonical" href="{base}/">' if base else ""
    og_url = f'\n  <meta property="og:url" content="{base}/">' if base else ""

    # el visor de artifacts aporta este reset; aquí hay que escribirlo
    reset = (
        "<style>:root{padding-top:env(safe-area-inset-top,0px);"
        "padding-bottom:env(safe-area-inset-bottom,0px)}"
        "body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>"
    )

    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
  <meta name="description" content="{DESCRIPCION}">
  <meta name="theme-color" content="#0F120C">{canon}
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{TITULO}">
  <meta property="og:title" content="{TITULO}">
  <meta property="og:description" content="{DESCRIPCION}">
  <meta property="og:image" content="{og_img}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="es_ES">
  <meta property="og:locale:alternate" content="en_GB">{og_url}
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="img/favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="img/apple-touch-icon.png">
  {reset}
{cabeza}
</head>
<body>
{cuerpo}
</body>
</html>
"""


def main():
    imagen_og()
    iconos()

    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "img").mkdir(parents=True)

    (DIST / "index.html").write_text(html(), encoding="utf-8")

    for nombre in ("fondo.webp", "cocum-wordmark.png", "marca-alpha.png",
                   "og.jpg", "favicon.png", "apple-touch-icon.png"):
        shutil.copy2(IMG / nombre, DIST / "img" / nombre)

    total = sum(f.stat().st_size for f in DIST.rglob("*") if f.is_file())
    print(f"dist listo: {len(list(DIST.rglob('*')))} archivos, {total // 1024} KB")
    if not SITIO:
        print("aviso: SITIO está vacío, las metas de Open Graph van en ruta relativa")


if __name__ == "__main__":
    main()
