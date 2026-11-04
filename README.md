# Cocum Origin

Real Food · Brunch · Good People — Guardamar del Segura.
**Apertura prevista: enero de 2027.**

## Teaser de preapertura

Una sola pantalla, sin scroll: el símbolo de Cocum girando en 3D sobre la selva, el
logotipo y **PRÓXIMAMENTE**. Sin formularios, sin contacto y sin pistas de qué tipo de
local es. Siempre en castellano. Sin dependencias.

### Cómo se publica

El sitio publicable vive en la **raíz** del repositorio: `index.html`, `img/` y
`_redirects`. Está ahí a propósito, para que Cloudflare Pages funcione con sus
ajustes por defecto sin tocar ningún campo.

| Campo de Cloudflare | Valor |
| --- | --- |
| Framework preset | None |
| Build command | *(vacío)* |
| Build output directory | *(vacío, o `/`)* |
| Root directory | `/` |

El build command va vacío a propósito: la imagen de Cloudflare no trae Pillow, que es
lo que genera la tarjeta de compartir y los iconos. Por eso el sitio se commitea ya
construido.

### Los dos ficheros

| | Para qué |
| --- | --- |
| `landing/index.html` | El fuente. Está escrito para el visor de artifacts de Claude, que le añade el `<!doctype>`, el `<head>` y las metas al publicar. **No se sirve tal cual**: sin esas etiquetas el navegador entra en modo quirks y en móvil renderiza a ancho de escritorio. `_redirects` manda `/landing/*` a la portada para que nadie aterrice ahí |
| `index.html` en la raíz | Lo que se publica. Lo genera `landing/build.py` envolviendo el fuente en un documento completo, con metas de Open Graph, icono y tarjeta 1200×630 para compartir |

Después de tocar `landing/index.html`:

```
python3 landing/build.py
```

y commitear la raíz. El subdominio `*.pages.dev` sale del **nombre del proyecto** en
Cloudflare, así que para que sea `cocum.pages.dev` el proyecto tiene que llamarse
`cocum`.

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
