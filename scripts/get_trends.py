#!/usr/bin/env python3
import json
import datetime
import time
import os

print("🔥 Iniciando script de trends...")
print(f"📁 Directorio actual: {os.getcwd()}")

# Datos de trends (12 base + variaciones)
base_trends = [
    {"nombre": "ASMR bebidas + hielo (Muy viral ahora)", "categoria": "Bares", "descripcion": "Close-up de hielo cayendo + sonido puro", "viralidad": 97, "formato": "Reel 5-10s", "sonido": "Natural", "hashtags": "#ASMR #Viral", "menciones": 6800, "videos": 3200, "source": "TikTok"},
    {"nombre": "Postres brutales bordes quemados", "categoria": "Repostería", "descripcion": "Pasteles desordenados y quemados", "viralidad": 96, "formato": "Reel 8-15s", "sonido": "Transiciones", "hashtags": "#PostreBrutal", "menciones": 5400, "videos": 2670, "source": "TikTok"},
    {"nombre": "Corte de carne en slow-motion viral", "categoria": "Restaurantes", "descripcion": "Videos de corte perfecto mostrando jugo", "viralidad": 92, "formato": "Reel 8-15s", "sonido": "ASMR", "hashtags": "#FoodViral", "menciones": 4200, "videos": 1850, "source": "Google"},
    {"nombre": "Galletas gigantes chocolate fundido", "categoria": "Repostería", "descripcion": "Galletas enormes con chocolate cayendo", "viralidad": 95, "formato": "Reel 10-15s", "sonido": "ASMR", "hashtags": "#GalletaViral", "menciones": 4600, "videos": 2100, "source": "TikTok"},
    {"nombre": "Cóctel con hielo seco explosivo", "categoria": "Bares", "descripcion": "Efecto visual épico con humo", "viralidad": 94, "formato": "Reel 8-15s", "sonido": "Épica", "hashtags": "#ShowBar", "menciones": 4000, "videos": 1800, "source": "TikTok"},
    {"nombre": "Chocolate + sal marina extremo", "categoria": "Repostería", "descripcion": "Contraste dulce + salado intenso", "viralidad": 91, "formato": "Reel 10-12s", "sonido": "Épica", "hashtags": "#Contraste", "menciones": 3700, "videos": 1650, "source": "TikTok"},
    {"nombre": "Comparativa visual platos", "categoria": "Restaurantes", "descripcion": "Split screen tu plato vs competencia", "viralidad": 89, "formato": "Reel 10-20s", "sonido": "Épica", "hashtags": "#Comparativa", "menciones": 3100, "videos": 1450, "source": "Reddit"},
    {"nombre": "Dip de Gildas desestructurado", "categoria": "Bares", "descripcion": "Gildas en dip viral 2026", "viralidad": 87, "formato": "Reel 10-20s", "sonido": "Trending", "hashtags": "#Gildas", "menciones": 2400, "videos": 1100, "source": "Twitter"},
    {"nombre": "Bebida instagrameable colores vibrantes", "categoria": "Cafeterías", "descripcion": "Colores extremos, capas, decoración", "viralidad": 88, "formato": "Reel + Post", "sonido": "Soft", "hashtags": "#InstaFeed", "menciones": 2800, "videos": 1200, "source": "Instagram"},
    {"nombre": "Latte art perfecto trend 2026", "categoria": "Cafeterías", "descripcion": "Arte en café en slow-motion", "viralidad": 85, "formato": "Reel 10-15s", "sonido": "Aesthetic", "hashtags": "#LatteArt", "menciones": 2100, "videos": 950, "source": "Instagram"},
    {"nombre": "Técnica culinaria + resultado final", "categoria": "Restaurantes", "descripcion": "Antes/después profesional", "viralidad": 82, "formato": "Reel 12-20s", "sonido": "Cocina", "hashtags": "#Técnica", "menciones": 1900, "videos": 820, "source": "YouTube"},
    {"nombre": "Extracción espresso máquina profesional", "categoria": "Cafeterías", "descripcion": "Crema perfecta, proceso visible", "viralidad": 80, "formato": "Reel 6-10s", "sonido": "Máquina", "hashtags": "#Espresso", "menciones": 1600, "videos": 680, "source": "Instagram"},
]

# Agregar variaciones dinámicas
todas_las_categorias = ["Restaurantes", "Bares", "Cafeterías", "Repostería"]
todos_los_trends = list(base_trends)

# Crear 20+ trends adicionales por categoría
contador = 0
for categoria in todas_las_categorias:
    for i in range(5):
        contador += 1
        viralidad_base = 60 + (i * 5)
        
        nuevos_trends = {
            "Restaurantes": [
                f"Plato {contador}: Fusion innovadora",
                f"Presentación artística #{contador}",
                f"Ingredientes premium #{contador}",
                f"Técnica especial #{contador}",
                f"Contraste de sabores #{contador}",
            ],
            "Bares": [
                f"Cóctel creativo #{contador}",
                f"Bebida decorada #{contador}",
                f"Efecto visual #{contador}",
                f"Aperitivo trending #{contador}",
                f"Drink con hielo especial #{contador}",
            ],
            "Cafeterías": [
                f"Café espresso #{contador}",
                f"Latte art variation #{contador}",
                f"Cold brew trending #{contador}",
                f"Café con leche artística #{contador}",
                f"Bebida de café especial #{contador}",
            ],
            "Repostería": [
                f"Postre creativo #{contador}",
                f"Pastel trending #{contador}",
                f"Galleta especial #{contador}",
                f"Donut viral #{contador}",
                f"Mousse delicioso #{contador}",
            ]
        }
        
        todos_los_trends.append({
            "nombre": nuevos_trends[categoria][i],
            "categoria": categoria,
            "descripcion": f"Trend viral en {categoria} - Variación {contador}",
            "viralidad": min(99, viralidad_base + (contador % 10)),
            "formato": "Reel 8-15s",
            "sonido": "Trending",
            "hashtags": f"#Trend{contador}",
            "menciones": 2000 + (contador * 100),
            "videos": 500 + (contador * 50),
            "source": ["TikTok", "Instagram", "Twitter", "Google"][contador % 4]
        })

print(f"✅ Creados {len(todos_los_trends)} trends")

# Crear JSON
data = {
    "timestamp": datetime.datetime.now().isoformat(),
    "última_actualización": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "trends": todos_los_trends,
    "total": len(todos_los_trends),
    "promedio_viralidad": round(sum(t['viralidad'] for t in todos_los_trends) / len(todos_los_trends), 1),
    "trend_más_viral": max(todos_los_trends, key=lambda x: x['viralidad'])['nombre'],
    "fuentes": list(set(t.get('source', 'Unknown') for t in todos_los_trends))
}

# Guardar archivo
output_path = "trends-data.json"
try:
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ Archivo guardado: {output_path}")
    print(f"📊 Viralidad promedio: {data['promedio_viralidad']}%")
    print(f"🔥 Trend más viral: {data['trend_más_viral']}")
    print(f"📈 Total de trends: {len(todos_los_trends)}")
    
    # Verificar que existe
    if os.path.exists(output_path):
        size = os.path.getsize(output_path)
        print(f"✅ Archivo verificado: {size} bytes")
    else:
        print("❌ ERROR: El archivo no se creó")
        exit(1)
        
except Exception as e:
    print(f"❌ Error guardando archivo: {e}")
    exit(1)

print("✅ Script completado exitosamente")
