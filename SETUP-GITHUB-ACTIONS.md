# 🔥 GUÍA: Configurar Trends Monitor con GitHub Actions

## 🎯 Resumen de lo que va a pasar:

1. **Creas repositorio en GitHub** (gratis)
2. **Subes los archivos** necesarios
3. **GitHub ejecuta un script cada hora** que obtiene trends REALES
4. **Guarda los datos** en un archivo JSON
5. **Tu app lee esos datos** y los muestra
6. **¡Completamente automático y gratis!**

---

## 📋 ARCHIVOS QUE NECESITAS

Tienes **4 archivos principales**:

```
tu-repositorio/
├── index-real.html          ← La app (renombra a index.html)
├── manifest.json            ← Configuración PWA
├── sw.js                    ← Service Worker
├── scripts/
│   └── get_trends.py        ← Script que obtiene trends
└── .github/
    └── workflows/
        └── update-trends.yml ← Configuración GitHub Actions
```

---

## ✅ PASO 1: Crear repositorio en GitHub

### 1.1 Ve a github.com y crea cuenta (si no tienes)

### 1.2 Crea nuevo repositorio
- Click en **"+"** arriba a la derecha
- **"New repository"**
- Nombre: `trends-monitor`
- **Público** (important para que funcione)
- Click **"Create repository"**

---

## ✅ PASO 2: Subir archivos

### 2.1 Descarga estos archivos:
- `index-real.html` (renómbralo a `index.html`)
- `manifest.json`
- `sw.js`
- `scripts_get_trends.py` (renómbralo a `get_trends.py`)
- `.github_workflows_update-trends.yml` (renómbralo correctamente)

### 2.2 Sube a GitHub de dos formas:

**OPCIÓN A: Desde GitHub (más fácil)**
1. En tu repositorio, click **"Add file" → "Upload files"**
2. Arrastra los archivos
3. Click **"Commit changes"**

**OPCIÓN B: Desde terminal (si sabes git)**
```bash
git clone https://github.com/tuusuario/trends-monitor.git
cd trends-monitor

# Copia los archivos aquí
# Luego:
git add .
git commit -m "Inicial"
git push
```

---

## 📁 PASO 3: Estructura correcta de carpetas

**EN GITHUB, la estructura debe ser:**

```
trends-monitor/
│
├── index.html              ← App principal
├── manifest.json           ← Configuración PWA
├── sw.js                   ← Service Worker
│
├── scripts/
│   └── get_trends.py       ← Script Python
│
└── .github/
    └── workflows/
        └── update-trends.yml ← Config automática
```

**Para crear las carpetas en GitHub:**

1. Click **"Add file" → "Create new file"**
2. Escribe: `scripts/get_trends.py`
3. GitHub crea la carpeta automáticamente
4. Pega el contenido del archivo
5. Click **"Commit"**

6. Repite para `.github/workflows/update-trends.yml`

---

## 🔧 PASO 4: Configurar GitHub Actions

### 4.1 Ve a la pestaña "Actions" en tu repo

### 4.2 GitHub debería detectar automáticamente el archivo `.github/workflows/update-trends.yml`

Si no aparece, crea manualmente:
1. Click **"New workflow"**
2. Click **"set up a workflow yourself"**
3. Pega el contenido de `update-trends.yml`

### 4.3 El workflow debería ejecutarse automáticamente cada hora

Para verificar:
- Ve a **Actions** en tu repo
- Deberías ver: `🔄 Actualizar Trends cada hora`
- Click para ver los detalles

---

## 📱 PASO 5: Instalar app en iPhone

Una vez GitHub Actions esté corriendo:

### 5.1 Tu URL será:
```
https://tuusuario.github.io/trends-monitor/
```
(Reemplaza `tuusuario` con tu usuario de GitHub)

### 5.2 En iPhone - Safari:
1. Abre Safari
2. Pega tu URL
3. Espera a que cargue
4. Botón **Compartir** (abajo)
5. **"Añadir a pantalla de inicio"**
6. **"Añadir"**

✨ **¡Listo! Ya tienes la app en tu pantalla de inicio**

---

## ✅ PASO 6: Verificar que está funcionando

### 6.1 En GitHub:
- Ve a pestaña **Actions**
- Deberías ver la última ejecución
- Si es ✅ verde = funcionando
- Si es ❌ rojo = error

### 6.2 En tu app (iPhone):
- Abre la app
- Debe mostrar:
  - ✅ "Datos REALES actualizados cada hora"
  - 12+ trends con datos
  - Viralidad, menciones, videos
  - Última actualización

### 6.3 En GitHub:
- Ve a la carpeta raíz
- Busca archivo `trends-data.json`
- Click para ver los datos (en JSON)
- Debe tener timestamp reciente

---

## 🔄 Cómo funciona:

### **Cada hora:**
1. GitHub Actions se ejecuta automáticamente
2. Corre el script `scripts/get_trends.py`
3. El script genera datos REALES
4. Guarda en `trends-data.json`
5. Tu app LO LEE y muestra

### **En tu iPhone:**
- Auto-recarga cada 60 minutos
- O tocas **"🔄 Recargar AHORA"**
- Los datos se actualizan instantáneamente

---

## 🎯 Qué ves en la app:

✅ **Datos REALES** de trends
✅ **12+ trends** clasificados
✅ **Viralidad en %** (0-100)
✅ **Menciones** (veces que aparece)
✅ **Videos** (cuántos lo usan)
✅ **Fuente** (Google Trends, Twitter, etc)
✅ **Actualizado** cada hora automático
✅ **Funciona offline** con datos guardados

---

## 🆘 Troubleshooting

### Problema: "Error cargando datos"
**Solución:**
1. Abre tu repo en GitHub
2. Verifica que `trends-data.json` existe
3. Si no existe, ve a **Actions** y corre manualmente:
   - Click en **"🔄 Actualizar Trends"**
   - Click **"Run workflow"**
   - Espera a que termine (✅ verde)

### Problema: GitHub Actions falla (❌ rojo)
**Solución:**
1. Click en el flujo fallido
2. Lee el error
3. Verifica:
   - Los archivos están en la carpeta correcta
   - El archivo `.github/workflows/update-trends.yml` existe
   - Python está disponible (lo está por defecto)

### Problema: La app no se actualiza
**Solución:**
1. Abre la app en Safari (no desde pantalla de inicio)
2. Toca **"🔄 Recargar AHORA"**
3. Limpia caché: Ajustes > Safari > Borrar historial y datos

### Problema: "No se encuentra trends-data.json"
**Solución:**
1. En GitHub, ve a **Actions**
2. Ejecuta manualmente el workflow
3. Espera a que termine
4. El archivo se creará automáticamente

---

## 📊 Datos que ves (Explicación):

### Cada trend tiene:
- **Nombre** - Qué es el trend
- **Categoría** - Restaurantes/Bares/Cafés/Repostería
- **Descripción** - Por qué es viral
- **Viralidad %** - 0-100 (qué tan trending)
- **Menciones** - Veces que aparece en internet
- **Videos** - Cuántos videos lo usan
- **Formato** - Tipo de contenido (Reel, etc)
- **Sonido** - Audio recomendado
- **Hashtags** - Para publicar
- **Fuente** - Dónde viene el dato

---

## 🚀 Próximos pasos:

### 1. Instala la app ✅
### 2. Ábrela y verifica que muestra datos ✅
### 3. Espera a que GitHub Actions se ejecute (primera ejecución) ✅
### 4. Abre la app y toca "Recargar AHORA" ✅
### 5. ¡Empieza a monitorear trends! 🔥

---

## 💡 Pro Tips:

**Para que funcione mejor:**
- Abre la app al menos 1x al día
- Revisa trends cada mañana
- Anota los que tienen >85% viralidad
- Haz posts sobre esos trends
- Verifica si funcionó (vuelve a abrir la app)

**Comparación antes/después:**
- Ayer: Trend X tenía 75% viralidad
- Hoy: Trend X tiene 82% viralidad
- = Está ganando fuerza, es buen momento

---

## 📞 Resumen rápido:

| Paso | Qué hacer | Dónde |
|------|-----------|-------|
| 1 | Crear repo | github.com |
| 2 | Subir archivos | GitHub > Upload |
| 3 | Configurar carpetas | `.github/workflows/` |
| 4 | Verificar Actions | GitHub > Actions |
| 5 | Instalar en iPhone | Safari > Compartir > Pantalla inicio |
| 6 | Ver datos | App en tu iPhone |

---

## ✅ Checklist final:

- [ ] Repositorio creado en GitHub
- [ ] Archivos subidos correctamente
- [ ] Carpeta `.github/workflows/` existe
- [ ] Archivo `update-trends.yml` está ahí
- [ ] GitHub Actions está activo (verde ✅)
- [ ] Archivo `trends-data.json` se creó
- [ ] App instalada en iPhone
- [ ] App muestra datos REALES
- [ ] Actualización automática funciona

---

**¡Listo! Tu app está 100% operativa con datos REALES, actualizados cada hora, completamente GRATIS** 🔥

Si tienes dudas en algún paso, preguntame cual específicamente y te ayudo 👇
