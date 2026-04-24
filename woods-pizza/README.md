# Woods Pizza a la Leña - Datos Completos

## Estructura

```
woods-pizza/
├── web/
│   ├── page.html              # HTML de la web propia
│   └── menu_completo.json     # Menu real (150 items, 16 categorias)
├── uber-eats/
│   ├── data/
│   │   └── page.html          # HTML de Uber Eats
│   ├── diario/
│   │   └── 2026-04-24.json    # Datos de Uber Eats
│   └── imagenes/
│       └── woods_*.jpeg/png   # 36 imagenes de productos
├── instagram/
│   ├── imagenes/              # 35 imagenes de Instagram
│   └── diario/
│       └── 2026-04-24.json    # Datos de Instagram
└── data/
    ├── menu_con_imagenes.json         # Menu + imagenes asignadas
    └── indice_productos_imagen.json   # INDICE para Flavia (mesero virtual)
```

## Indice para Flavia (Mesero Virtual)

El archivo `data/indice_productos_imagen.json` contiene el mapping de productos a imagenes.

### Uso:
```python
import json

with open('data/indice_productos_imagen.json', 'r') as f:
    indice = json.load(f)

# Buscar producto por nombre
producto = indice.get('margarita')  # nombre en minusculas
if producto:
    print(f"Nombre: {producto['name']}")
    print(f"Categoria: {producto['category']}")
    print(f"Precio: CRC {producto['price_crc']}")
    print(f"Imagen: {producto['image_file']}")
```

### Estructura del indice:
```json
{
  "nombre_producto_minusculas": {
    "name": "Nombre Original",
    "category": "Categoria",
    "price_crc": 7800,
    "image_file": "woods_003.jpeg",
    "image_path": "woods-pizza/uber-eats/imagenes/woods_003.jpeg"
  }
}
```

## Stats
- **Menu web**: 150 items, 16 categorias
- **Uber Eats**: 112 items, 12 categorias
- **Imagenes Uber Eats**: 36
- **Imagenes Instagram**: 35
- **Productos con imagen**: 36 (primeros 36 del menu)

## Notas
- Las imagenes se asignaron por orden al primero producto de cada categoria
- Si un producto no tiene imagen, el campo `image_file` sera null
- Para buscar: usar nombre del producto en minusculas, sin acentos si es posible

## Fecha de actualizacion
2026-04-24
