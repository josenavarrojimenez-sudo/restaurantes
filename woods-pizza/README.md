# Woods Pizza a la Leña - Repo Principal

Este es el repo ACTUALIZADO y COMPLETO para Woods Pizza.

## ⚠️ ATENCION: woods-pizza-data/ esta obsoleto
Usar SOLO esta carpeta `woods-pizza/` para todo.

## Estructura
```
woods-pizza/
├── web/
│   ├── page.html              # Web propia (caroje.com)
│   └── menu_completo.json     # 236 items, 16 categorias (incluye Menú Keto), precios CRC
├── uber-eats/
│   ├── data/page.html         # HTML de Uber Eats
│   ├── diario/2026-04-24.json # Datos Uber Eats
│   └── imagenes/              # 36 imagenes de productos
├── instagram/
│   ├── imagenes/              # 35 imagenes nuevas
│   └── diario/2026-04-24.json
├── data/
│   ├── menu_con_imagenes.json         # Menu + imagenes
│   ├── indice_productos_imagen.json   # INDICE para Flavia (busqueda por nombre)
│   └── producto_imagen_mapping.json   # Mapping completo
└── README.md                  # Este archivo
```

## Sistema Inteligente para Flavia (Mesero Virtual)

Buscar producto por nombre (minusculas):
```python
import json
with open('data/indice_productos_imagen.json') as f:
    indice = json.load(f)

producto = indice.get('margarita')
# Retorna: name, category, price_crc, image_file, image_path
```

## Stats
- Menu web: 236 items, 16 categorias (incluye Menú Keto)
- Uber Eats: 112 productos, 36 imagenes
- Instagram: 35 imagenes
- Productos con imagen: 32

## Cambios 2026-05-02
- Re-scrape completo desde https://woodspizza.caroje.com/common/
- Agregados 108 items faltantes:
  - Variantes Woods (signature) en Carpaccios, Ensaladas, Pizzas, Focaccia, Calzone, Panini, Wraps
  - Categoría completa Menú Keto (21 items: focaccia, antipasto, carpaccios, ensaladas, 11 pizzas keto, postre keto)
  - Cervezas internacionales (Stella, Hoegaarden, Leffe, Heineken, Corona, etc.)
  - Cervezas artesanales costarricenses (Calle Cimarrona, Eremita, La Cofradía)
  - Cocteles especiales (Mojitos, Moscow Mules, Margaritas, Gin & Tonic con 8 sabores)
  - Shots especiales (Chiliwoods, Pitufo, Deep Ocean, Cherry Mary, etc.)

## Fecha: 2026-05-02
