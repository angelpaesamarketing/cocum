# Cocum Origin

Real Food · Brunch · Good People — Guardamar del Segura.
**Apertura prevista: enero de 2027.**

## Teaser de preapertura

`landing/index.html` — una sola pantalla, sin scroll: el símbolo de Cocum girando en
3D sobre un fondo atmosférico con partículas, el nombre y **PRÓXIMAMENTE**. Sin
formularios, sin contacto y sin pistas de qué tipo de local es. Español e inglés por
idioma del navegador. HTML, CSS y JS sin dependencias.

Tres constantes al principio del script lo controlan todo:

| Constante | Qué hace |
| --- | --- |
| `INSTAGRAM` | El único enlace de la página. Confirmar el usuario real antes de publicar |
| `FONDO` | Imagen de ambiente generada (sin comida, sin texto). Se deja en `img/` y se nombra aquí |
| `LOGOTIPO` | Logotipo completo en PNG transparente o SVG. Si se pone, sustituye al nombre compuesto con tipografía |

Las imágenes: `img/fondo.webp` es la selva generada, `img/cocum-wordmark.png` el
logotipo en PNG transparente y `img/marca-alpha.png` el símbolo suelto, recortado del
original con alfa por luminancia. Los prompts del resto del banco de imágenes están en
[`estrategia/prompts-imagen.md`](estrategia/prompts-imagen.md).

En enero esta misma página pasa a ser la carta, que es a donde apuntará el QR de las
mesas. Para publicarla: subir `landing/` a Netlify, Vercel o Cloudflare Pages, apuntar
el dominio y añadir el aviso legal con los datos del titular.

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
