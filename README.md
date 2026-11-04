# Cocum Origin

Real Food · Brunch · Good People — Guardamar del Segura.
**Apertura prevista: enero de 2027.**

## Teaser de preapertura

Una sola pantalla, sin scroll: el símbolo de Cocum girando en 3D sobre la selva, el
logotipo y **PRÓXIMAMENTE**. Sin formularios, sin contacto y sin pistas de qué tipo de
local es. Español e inglés por idioma del navegador. Sin dependencias.

### Dos ficheros, dos destinos

| | Para qué |
| --- | --- |
| `landing/index.html` | El fuente. Está escrito para el visor de artifacts de Claude, que le añade el `<!doctype>`, el `<head>` y las metas al publicar. **No se sube tal cual a un hosting**: sin esas etiquetas el navegador entra en modo quirks y en móvil renderiza a ancho de escritorio |
| `landing/dist/` | Lo que se publica. Lo genera `landing/build.py` envolviendo el fuente en un documento completo, con metas de Open Graph, icono y la imagen para compartir |

Después de tocar `landing/index.html`:

```
python3 landing/build.py
```

y commitear `landing/dist/`. Va commiteado a propósito: así Cloudflare no necesita
ejecutar nada, y su imagen de build no trae Pillow, que es lo que genera la tarjeta
de compartir y los iconos.

### Ajustes de Cloudflare Pages

Conectado al repositorio de GitHub:

| Campo | Valor |
| --- | --- |
| Framework preset | None |
| Build command | *(vacío)* |
| Build output directory | `landing/dist` |
| Root directory | `/` |
| Production branch | la rama de trabajo, o `main` si se crea |

Con subida directa, se arrastra el **contenido** de `landing/dist` (el `index.html`
y la carpeta `img`), no la carpeta `dist` entera.

### Lo que queda por rellenar

| Dónde | Qué |
| --- | --- |
| `INSTAGRAM`, en `landing/index.html` | El usuario real. Es el único enlace de la página |
| `FONDO_MOVIL`, en `landing/index.html` | El fondo vertical 9:16 cuando esté generado. Mientras tanto el 16:9 se desplaza al 30% en vertical para no perder la selva |
| `SITIO`, en `landing/build.py` | El dominio, para que las metas de Open Graph lleven URL absoluta |
| Aviso legal | Una página o un pie con los datos del titular |

Las imágenes: `img/fondo.webp` es la selva generada, `img/cocum-wordmark.png` el
logotipo en PNG transparente y `img/marca-alpha.png` el símbolo suelto, recortado del
original con alfa por luminancia. `og.jpg` y los iconos los genera el build. Los
prompts del resto del banco están en
[`estrategia/prompts-imagen.md`](estrategia/prompts-imagen.md).

En enero esta misma página pasa a ser la carta, que es a donde apuntará el QR de las
mesas.

Vista publicada: https://claude.ai/artifact/HJ4dHD1ZUH4f2WkH6Dcgat

## Planes

- [`estrategia/plan-choque-enero.md`](estrategia/plan-choque-enero.md) —
  **plan vigente**. Doce semanas hasta la apertura de enero: qué cambia con la fecha,
  las tres fases, cómo trabajar solo con imagen generada, semana a semana, publicidad
  comprimida, plazos de imprenta con la Navidad en medio, qué se recorta y qué
  necesita el plan de Davi.
  Doc vivo: https://claude.ai/artifact/BnVPw1WfWtigPUS2pajYsr

- [`estrategia/plan-marketing-publicidad.md`](estrategia/plan-marketing-publicidad.md) —
  método de ejecución: campañas, contenido, Google y SEO local, reseñas, creadores,
  rutina semanal. Sus **fechas están obsoletas** desde el adelanto a enero; manda el
  plan de choque.
  Doc vivo: https://claude.ai/artifact/3w9HxfgXcetDmEPumdvYUW

- [`estrategia/plan-preapertura.md`](estrategia/plan-preapertura.md) —
  plan de preapertura original a seis meses, con la parte de negocio y operativa.
  Referencia; su calendario ya no aplica.
  Doc vivo: https://claude.ai/artifact/5SwJp7epsqUr1vfudSwAWF

Los `.md` de `estrategia/` son instantáneas exportadas de los documentos.
