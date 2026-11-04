# Prompts de imagen — Cocum Origin

Para generar el banco de imágenes de la fase teaser. Todo en inglés: los modelos
responden bastante mejor y la paleta sale más consistente.

## Dos reglas antes de empezar

**1. El logo no se genera.** Ningún modelo va a reproducir el logo de Cocum.
Lo que se genera es el fondo y el ambiente; el logo se coloca encima — en la web ya
está puesto como PNG con transparencia (`landing/img/marca-alpha.png`), y para redes
se monta en Canva.

**2. Nada de texto dentro de la imagen generada.** La IA compone mal las letras: en
la pieza que ya tenemos, el espaciado de "MUY PRONTO" y de "ORIGIN" está irregular.
Se generan fondos limpios y el texto se pone encima en Canva, con la tipografía de
marca. Así además el mismo fondo sirve para varias piezas.

**3. Nada de comida en esta fase.** La decisión es no dar pistas de qué tipo de local
es hasta que se enseñe la carta. Ni bowls, ni cafés, ni tostas, ni platos, ni tazas.

## El negativo, para pegar al final de todos

```
Negative: text, letters, typography, watermark, logo, signage, food, plates, bowls,
cups, cutlery, people, faces, hands, bright daylight, white background, clutter,
oversaturated colours, HDR look, plastic sheen.
```

## 1 · Fondo de la landing, horizontal

El principal. Pídelo a la máxima resolución, mínimo 2400 px de ancho.

```
Cinematic atmospheric background. No subject, no focal object — this is a backdrop.
Deep forest-green and warm dark-brown palette, very low key. Dense tropical foliage,
monstera and palm and fern leaves, framing only the edges of the frame in near
silhouette, leaving the centre open and empty. Soft golden volumetric god rays
filtering diagonally from the upper left through the leaves. Warm backlit haze,
floating dust motes catching the light. The centre of the frame is slightly brighter
and emptier than the edges, so a logo can sit there. Shallow depth of field, 35mm,
subtle film grain. Ultra wide 16:9.
```

## 2 · El mismo fondo, vertical

Para móvil y para stories. Pídelo **en la misma conversación**, justo después del
anterior, añadiendo al principio: *same style, same lighting and same palette as the
previous image*.

```
Same style, same lighting and same palette as the previous image, recomposed vertical
9:16. Tropical foliage framing the top and bottom edges in near silhouette. The open
empty space sits in the middle third of the frame. Golden god rays from the upper
right. Very low key, warm haze, floating dust motes, subtle film grain.
```

## 3 · Serie de ambiente para Instagram

Tres piezas en 4:5, para publicar durante las semanas de teaser. Ninguna dice qué
tipo de negocio es; todas construyen el mundo de la marca.

```
Extreme close-up of water droplets on a large monstera leaf, backlit by a low golden
sun. Deep green and gold, very dark background falling into shadow. Shallow depth of
field, macro, subtle film grain. Vertical 4:5.
```

```
Close-up of warm golden light raking across raw oak wood grain and the texture of
speckled cream stoneware. Deep shadow on three quarters of the frame, one band of
warm light. Macro, shallow depth of field, subtle film grain. Vertical 4:5.
```

```
Steam rising through a dark room, lit from behind by a single warm gold light source.
Large tropical leaf shadows cast on the back wall. Almost black, with the steam and
the leaf edges catching the light. Cinematic, 50mm, subtle film grain. Vertical 4:5.
```

## 4 · Fondo para la pieza de "PRÓXIMA APERTURA"

Para el post y la story del anuncio. El texto y el logo se montan encima en Canva,
en la banda central que el prompt deja vacía.

```
Same style, same lighting and same palette as the previous images. Dark cinematic
backdrop with tropical foliage silhouettes entering from the four corners only. A
wide, clean, empty horizontal band across the middle of the frame, slightly lit by a
warm golden glow, with nothing in it. Floating dust motes. Very low key, warm haze,
subtle film grain. Vertical 4:5.
```

Para la story, repítelo cambiando el final por `Vertical 9:16` y pidiendo que la
banda vacía quede en el tercio central.

## 5 · Fondo para la lona de obra

Formato muy apaisado. La lona se lee desde un coche, así que necesita el espacio
libre a un lado para el logo grande y el QR.

```
Same style, same lighting and same palette as the previous images, recomposed as an
ultra-wide banner, aspect ratio 3:1. Tropical foliage in near silhouette occupying
only the left third of the frame. The right two thirds are open, dark and almost
empty, lit by a soft golden glow from the left, ready for large type. Warm haze,
floating dust motes, very low key, subtle film grain.
```

## Cómo mantener la consistencia

- Genera todas las imágenes **en la misma conversación**, una detrás de otra.
- En cuanto una salga bien, empieza las siguientes con *same style, same lighting and
  same palette as the previous image*. Es lo que más ayuda.
- Si una sale demasiado clara, añade *darker, lower key, more shadow*. Es el fallo más
  frecuente: los modelos tienden a iluminar de más.
- Guarda el prompt exacto junto a cada imagen y nombra los archivos con palabras
  reales: `cocum-ambiente-hojas-01.jpg`. Esos nombres luego trabajan en Google.

## Dónde va cada una

| Imagen | Dónde |
| --- | --- |
| 1 · Fondo horizontal | Constante `FONDO` en `landing/index.html` |
| 2 · Fondo vertical | Stories, y versión móvil de la web si hiciera falta |
| 3 · Serie de ambiente | Instagram y Facebook durante las semanas de teaser |
| 4 · Próxima apertura | Post y story del anuncio, con el texto montado en Canva |
| 5 · Lona | Al rotulista, junto con el logo en vectorial |

## Estado

| Imagen | Estado | Archivo |
| --- | --- | --- |
| 1 · Fondo horizontal | **Hecha** | `landing/img/fondo.webp` |
| 2 · Fondo vertical | Pendiente | |
| 3 · Ambiente, hoja con gotas | Pendiente | |
| 4 · Ambiente, luz sobre madera | Pendiente | |
| 5 · Próxima apertura | Pendiente | |
| 6 · Lona | Pendiente | |

El logotipo ya no hace falta generarlo: llegó en PNG con transparencia y está en
`landing/img/cocum-wordmark.png`. El símbolo suelto, recortado del original,
está en `landing/img/marca-alpha.png`.

## El brief completo, en un solo mensaje

Para pedirlas todas de una vez. Se pega entero y luego se va diciendo `next`
después de cada imagen.

```
You are my art director for a brand teaser campaign. Read this whole brief first,
then generate the images ONE AT A TIME, in order, starting with image 1. After each
image, stop and wait for me to say "next".

THE BRAND
Cocum Origin — a new hospitality brand opening in January in Guardamar del Segura, a
Mediterranean beach town in Spain. Tropical, contemporary, elegant. The campaign is a
teaser: it must NOT reveal what the business sells. That is the whole point.

STYLE BASE — applies to every single image
Cinematic, very low key, almost dark. Deep forest-green and warm dark-brown palette
with soft gold light. Tropical foliage: monstera, palm, fern. Golden volumetric god
rays, warm backlit haze, floating dust motes catching the light. Raw oak and speckled
cream stoneware textures where a surface is needed. Shallow depth of field, 35-50mm,
subtle film grain. No vignette burn, no HDR look.

HARD RULES
1. NO TEXT of any kind inside the image. No letters, no words, no signage, no logo.
   I add all typography myself afterwards.
2. NO FOOD, no drinks, no plates, bowls, cups or cutlery. Nothing that hints at what
   kind of business this is.
3. NO PEOPLE, no faces, no hands.
4. Every image must leave clean, dark, EMPTY space where I will place the logo and
   the type. Composition matters more than detail here — these are backdrops.
5. Keep all six images in the same world: same palette, same lighting direction
   logic, same grain. From image 2 onward, match the previous ones.

NEGATIVE — apply to all
text, letters, typography, watermark, logo, signage, food, plates, bowls, cups,
cutlery, people, faces, hands, bright daylight, white background, clutter,
oversaturated colours, HDR look, plastic sheen.

THE SIX IMAGES

1 — WEBSITE BACKGROUND, ultra wide 16:9, maximum resolution (at least 2400px wide).
Dense tropical foliage framing ONLY the edges of the frame in near silhouette,
leaving the centre open and empty. Golden god rays filtering diagonally from the
upper left through the leaves. The centre is slightly brighter and emptier than the
edges, so a logo can sit there.

2 — SAME BACKGROUND, VERTICAL 9:16. Same style, lighting and palette as image 1.
Foliage framing the top and bottom edges in near silhouette; the open empty space
sits in the middle third. Golden god rays from the upper right.

3 — AMBIENCE, vertical 4:5. Extreme close-up of water droplets on a large monstera
leaf, backlit by a low golden sun. Deep green and gold, background falling away into
near black. Macro, shallow depth of field.

4 — AMBIENCE, vertical 4:5. Close-up of warm golden light raking across raw oak wood
grain and the texture of speckled cream stoneware. Three quarters of the frame in
deep shadow, one single band of warm light.

5 — ANNOUNCEMENT BACKDROP, vertical 4:5. Tropical foliage silhouettes entering from
the four corners only. A wide, clean, completely empty horizontal band across the
middle of the frame, lit by a soft golden glow, with nothing in it — I will put the
logo and the announcement text there. Floating dust motes.

6 — OUTDOOR BANNER, ultra-wide 3:1. Tropical foliage in near silhouette occupying
only the LEFT THIRD of the frame. The right two thirds are open, dark and almost
empty, lit by a soft golden glow coming from the left, ready for very large type.

DELIVERY
Highest resolution available for each. If an image comes out too bright, redo it
darker and lower key — that is the most common failure. Confirm each image matches
the previous ones in palette and grain before moving on.
```

Si una sale clara o con hojas invadiendo el centro, basta con contestar
`darker, lower key, more shadow, keep the centre empty`, sin reescribir el prompt.
