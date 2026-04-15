#!/usr/bin/env python3
"""
Script de limpieza automática para Woods Pizza Data
Borra archivos diarios mayores a 15 días
Prolix debe ejecutar esto al inicio de cada scraping diario
"""
import os
import json
from datetime import datetime, timedelta
from pathlib import Path

DIARIO_DIR = "/root/.openclaw/workspace-prolix/restaurantes/woods-pizza-data/instagram/diario"
DIAS_MAXIMOS = 15

def limpiar_archivos_antiguos():
    """Borra archivos JSON de días anteriores mayores a DIAS_MAXIMOS"""
    fecha_limite = datetime.now() - timedelta(days=DIAS_MAXIMOS)
    archivos_borrados = []
    
    if not os.path.exists(DIARIO_DIR):
        return archivos_borrados
    
    for archivo in os.listdir(DIARIO_DIR):
        if archivo.endswith('.json') and archivo != 'plantilla.json':
            try:
                # Extraer fecha del nombre del archivo (formato: YYYY-MM-DD.json)
                fecha_str = archivo.replace('.json', '')
                fecha_archivo = datetime.strptime(fecha_str, '%Y-%m-%d')
                
                if fecha_archivo < fecha_limite:
                    ruta = os.path.join(DIARIO_DIR, archivo)
                    os.remove(ruta)
                    archivos_borrados.append(archivo)
                    print(f"🗑️ Borrado: {archivo} (más de {DIAS_MAXIMOS} días)")
            except ValueError:
                continue
    
    return archivos_borrados

if __name__ == "__main__":
    print(f"🧹 Limpiando archivos mayores a {DIAS_MAXIMOS} días...")
    borrados = limpiar_archivos_antiguos()
    print(f"✅ {len(borrados)} archivos borrados")