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
