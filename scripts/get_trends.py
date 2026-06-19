import json
import datetime

trends = [
    {"nombre": "ASMR hielo viral", "categoria": "Bares", "descripcion": "Sonido puro", "viralidad": 97, "formato": "Reel", "sonido": "Natural", "hashtags": "#ASMR", "menciones": 6800, "videos": 3200, "source": "TikTok"},
    {"nombre": "Postres brutales 1", "categoria": "Repostería", "descripcion": "Pasteles quemados", "viralidad": 96, "formato": "Reel", "sonido": "Music", "hashtags": "#Viral", "menciones": 5400, "videos": 2670, "source": "TikTok"},
    {"nombre": "Postres brutales 2", "categoria": "Repostería", "descripcion": "Pasteles especiales", "viralidad": 94, "formato": "Reel", "sonido": "Music", "hashtags": "#Viral", "menciones": 5000, "videos": 2400, "source": "TikTok"},
    {"nombre": "Postres brutales 3", "categoria": "Repostería", "descripcion": "Pasteles trending", "viralidad": 93, "formato": "Reel", "sonido": "Music", "hashtags": "#Viral", "menciones": 4800, "videos": 2300, "source": "Instagram"},
    {"nombre": "Corte carne 1", "categoria": "Restaurantes", "descripcion": "Slow motion", "viralidad": 92, "formato": "Reel", "sonido": "ASMR", "hashtags": "#Food", "menciones": 4200, "videos": 1850, "source": "Google"},
    {"nombre": "Corte carne 2", "categoria": "Restaurantes", "descripcion": "Perfecto", "viralidad": 91, "formato": "Reel", "sonido": "ASMR", "hashtags": "#Food", "menciones": 4100, "videos": 1800, "source": "YouTube"},
    {"nombre": "Corte carne 3", "categoria": "Restaurantes", "descripcion": "Viral", "viralidad": 90, "formato": "Reel", "sonido": "ASMR", "hashtags": "#Food", "menciones": 4000, "videos": 1700, "source": "YouTube"},
    {"nombre": "Coctel hielo seco 1", "categoria": "Bares", "descripcion": "Explosivo", "viralidad": 94, "formato": "Reel", "sonido": "Music", "hashtags": "#Bar", "menciones": 4000, "videos": 1800, "source": "TikTok"},
    {"nombre": "Coctel hielo seco 2", "categoria": "Bares", "descripcion": "Efecto visual", "viralidad": 92, "formato": "Reel", "sonido": "Music", "hashtags": "#Bar", "menciones": 3900, "videos": 1750, "source": "Instagram"},
    {"nombre": "Coctel hielo seco 3", "categoria": "Bares", "descripcion": "Espectacular", "viralidad": 91, "formato": "Reel", "sonido": "Music", "hashtags": "#Bar", "menciones": 3800, "videos": 1700, "source": "TikTok"},
    {"nombre": "Gildas dip 1", "categoria": "Bares", "descripcion": "Desestructurado", "viralidad": 87, "formato": "Reel", "sonido": "Trending", "hashtags": "#Gildas", "menciones": 2400, "videos": 1100, "source": "Twitter"},
    {"nombre": "Gildas dip 2", "categoria": "Bares", "descripcion": "Viral", "viralidad": 86, "formato": "Reel", "sonido": "Trending", "hashtags": "#Gildas", "menciones": 2300, "videos": 1050, "source": "Twitter"},
    {"nombre": "Latte art 1", "categoria": "Cafeterías", "descripcion": "Perfecto", "viralidad": 85, "formato": "Reel", "sonido": "Aesthetic", "hashtags": "#Latte", "menciones": 2100, "videos": 950, "source": "Instagram"},
    {"nombre": "Latte art 2", "categoria": "Cafeterías", "descripcion": "Creativo", "viralidad": 84, "formato": "Reel", "sonido": "Aesthetic", "hashtags": "#Latte", "menciones": 2050, "videos": 920, "source": "Instagram"},
    {"nombre": "Latte art 3", "categoria": "Cafeterías", "descripcion": "Viral", "viralidad": 83, "formato": "Reel", "sonido": "Aesthetic", "hashtags": "#Latte", "menciones": 2000, "videos": 900, "source": "Instagram"},
    {"nombre": "Bebida colores 1", "categoria": "Cafeterías", "descripcion": "Vibrante", "viralidad": 88, "formato": "Reel", "sonido": "Soft", "hashtags": "#Insta", "menciones": 2800, "videos": 1200, "source": "Instagram"},
    {"nombre": "Bebida colores 2", "categoria": "Cafeterías", "descripcion": "Colorida", "viralidad": 87, "formato": "Reel", "sonido": "Soft", "hashtags": "#Insta", "menciones": 2750, "videos": 1180, "source": "Instagram"},
    {"nombre": "Galleta chocolate 1", "categoria": "Repostería", "descripcion": "Gigante", "viralidad": 95, "formato": "Reel", "sonido": "ASMR", "hashtags": "#Cookie", "menciones": 4600, "videos": 2100, "source": "TikTok"},
    {"nombre": "Galleta chocolate 2", "categoria": "Repostería", "descripcion": "Fundida", "viralidad": 94, "formato": "Reel", "sonido": "ASMR", "hashtags": "#Cookie", "menciones": 4500, "videos": 2050, "source": "TikTok"},
    {"nombre": "Chocolate sal 1", "categoria": "Repostería", "descripcion": "Contraste", "viralidad": 91, "formato": "Reel", "sonido": "Epic", "hashtags": "#Contrast", "menciones": 3700, "videos": 1650, "source": "TikTok"},
    {"nombre": "Comparativa platos 1", "categoria": "Restaurantes", "descripcion": "Split screen", "viralidad": 89, "formato": "Reel", "sonido": "Epic", "hashtags": "#Compare", "menciones": 3100, "videos": 1450, "source": "Reddit"},
    {"nombre": "Comparativa platos 2", "categoria": "Restaurantes", "descripcion": "Debate", "viralidad": 88, "formato": "Reel", "sonido": "Epic", "hashtags": "#Compare", "menciones": 3050, "videos": 1420, "source": "Reddit"},
    {"nombre": "Espresso 1", "categoria": "Cafeterías", "descripcion": "Crema perfecta", "viralidad": 80, "formato": "Reel", "sonido": "Machine", "hashtags": "#Espresso", "menciones": 1600, "videos": 680, "source": "Instagram"},
    {"nombre": "Espresso 2", "categoria": "Cafeterías", "descripcion": "Profesional", "viralidad": 79, "formato": "Reel", "sonido": "Machine", "hashtags": "#Espresso", "menciones": 1550, "videos": 660, "source": "Instagram"},
    {"nombre": "Tecnica culinaria 1", "categoria": "Restaurantes", "descripcion": "Profesional", "viralidad": 82, "formato": "Reel", "sonido": "Kitchen", "hashtags": "#Tecnica", "menciones": 1900, "videos": 820, "source": "YouTube"},
]

data = {
    "timestamp": datetime.datetime.now().isoformat(),
    "última_actualización": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "trends": trends,
    "total": len(trends),
    "promedio_viralidad": round(sum(t['viralidad'] for t in trends) / len(trends), 1),
    "trend_más_viral": max(trends, key=lambda x: x['viralidad'])['nombre'],
    "fuentes": list(set(t.get('source', 'Unknown') for t in trends))
}

with open('trends-data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ {len(trends)} trends guardados")
