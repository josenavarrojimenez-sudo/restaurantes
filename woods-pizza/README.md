# Woods Pizza a la Leña - Repo Principal

Este es el repo ACTUALIZADO y COMPLETO para Woods Pizza.

## ⚠️ ATENCION: woods-pizza-data/ esta obsoleto
Usar SOLO esta carpeta `woods-pizza/` para todo.

## Estructura
```
woods-pizza/
├── web/
│   ├── page.html              # Web propia (caroje.com)
│   └── menu_completo.json     # 128 items, 15 categorias, precios CRC
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
- Menu web: 128 items, 15 categorias
- Uber Eats: 112 productos, 36 imagenes
- Instagram: 35 imagenes
- Productos con imagen: 32

## Fecha: 2026-04-24
