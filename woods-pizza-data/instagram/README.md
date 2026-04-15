# Woods Pizza Data - Instagram

## Estructura de Carpetas

```
woods-pizza-data/instagram/
├── diario/           ← FLAVIA LEE ESTO cada día
│   └── 2026-04-15.json   ← Datos del día (promociones vigentes, eventos, etc.)
├── imagenes/         ← Imágenes descargadas de posts
├── screenshots/      ← Capturas de pantalla del perfil y posts
├── data/             ← Datos crudos (HTML, texto extraído)
├── promociones_vigentes.json  ← JSON maestro de promociones
└── resumen_instagram.json     ← Resumen del scraping
```

## Para Flavia

Cada día, Flavia debe leer el archivo `diario/YYYY-MM-DD.json` más reciente.
Este archivo contiene:

- **promociones_vigentes**: Ofertas, eventos y promociones activas
- **promociones_pasadas**: Promociones ya vencidas (para referencia)
- **horarios**: Horarios de las 3 ubicaciones
- **guia_flavia**: Instrucciones y respuestas sugeridas

## Actualización

Prolix actualiza estos datos haciendo scraping de Instagram @woodscr.
La carpeta `diario/` se actualiza cada día con la info más reciente.
Los archivos mayores a 15 días se borran automáticamente.

## Fuente

- Instagram: https://www.instagram.com/woodscr/
- Agente de scraping: Prolix
- Agente consumidor: Flavia