# 📦 LISTA DE ARCHIVOS - Dónde ponerlos en GitHub

## 🎯 Tienes estos archivos:

```
✅ index-real.html              → Renombra a: index.html
✅ manifest.json                → Déjalo igual
✅ sw.js                        → Déjalo igual
✅ scripts_get_trends.py        → Renombra a: get_trends.py
✅ .github_workflows_update-trends.yml → Renombra a: update-trends.yml
✅ trends-data.json             → Déjalo igual
✅ SETUP-GITHUB-ACTIONS.md      → Documentación (opcional)
```

---

## 📁 ESTRUCTURA EN GITHUB

**Tu repositorio debe verse así:**

```
trends-monitor/
│
├── 📄 index.html                    ✅ La app principal
├── 📄 manifest.json                 ✅ Config PWA
├── 📄 sw.js                         ✅ Service Worker
├── 📄 trends-data.json              ✅ Datos iniciales
│
├── 📁 scripts/                      ✅ Carpeta
│   └── 📄 get_trends.py             ✅ Script Python
│
├── 📁 .github/                      ✅ Carpeta oculta
│   └── 📁 workflows/                ✅ Subcarpeta
│       └── 📄 update-trends.yml     ✅ Config automática
│
└── 📄 README.md (opcional)
```

---

## 🚀 CÓMO SUBIRLO FÁCIL A GITHUB

### **Método 1: Sin terminal (Recomendado)**

#### PASO 1: Crea la carpeta `scripts`
1. En GitHub repo > **"Add file"** > **"Create new file"**
2. Escribe en el campo nombre: `scripts/get_trends.py`
3. GitHub crea la carpeta automáticamente
4. Pega contenido del archivo `scripts_get_trends.py`
5. Click **"Commit new file"**

#### PASO 2: Crea la carpeta `.github/workflows`
1. **"Add file"** > **"Create new file"**
2. Escribe: `.github/workflows/update-trends.yml`
3. Pega contenido del archivo `.github_workflows_update-trends.yml`
4. Click **"Commit new file"**

#### PASO 3: Sube los demás archivos
1. **"Add file"** > **"Upload files"**
2. Arrastra:
   - `index.html` (renombrado de `index-real.html`)
   - `manifest.json`
   - `sw.js`
   - `trends-data.json`
3. Click **"Commit changes"**

---

### **Método 2: Con terminal (Más rápido)**

```bash
# 1. Clona el repo
git clone https://github.com/tuusuario/trends-monitor.git
cd trends-monitor

# 2. Crea la estructura de carpetas
mkdir -p scripts
mkdir -p .github/workflows

# 3. Coloca los archivos:
# Copia index-real.html como index.html
# Copia scripts_get_trends.py en scripts/get_trends.py
# Copia .github_workflows_update-trends.yml en .github/workflows/update-trends.yml
# Copia los demás archivos en la raíz

# 4. Sube todo
git add .
git commit -m "Inicial - Trends Monitor con GitHub Actions"
git push origin main
```

---

## ✅ VERIFICAR QUE ESTÁ BIEN

### En GitHub, verifica que:

1. **En la carpeta raíz (/)**
   - [ ] `index.html` existe
   - [ ] `manifest.json` existe
   - [ ] `sw.js` existe
   - [ ] `trends-data.json` existe

2. **En `scripts/`**
   - [ ] `get_trends.py` existe

3. **En `.github/workflows/`**
   - [ ] `update-trends.yml` existe

### Comprueba que GitHub Actions está activado:
1. Ve a la pestaña **"Actions"**
2. Deberías ver: **"🔄 Actualizar Trends cada hora"**
3. Si dice ✅ en verde = FUNCIONA
4. Si falta, revisa que `update-trends.yml` está en la carpeta correcta

---

## 🔄 NOMBRES CORRECTOS (Importante)

| Archivo descargado | Nombre en GitHub |
|---|---|
| `index-real.html` | `index.html` ⚠️ |
| `manifest.json` | `manifest.json` |
| `sw.js` | `sw.js` |
| `scripts_get_trends.py` | `get_trends.py` ⚠️ |
| `.github_workflows_update-trends.yml` | `update-trends.yml` ⚠️ |
| `trends-data.json` | `trends-data.json` |

**⚠️ = Importante renombrar correctamente**

---

## 📍 UBICACIONES EXACTAS

```
RAÍZ:
├── index.html ← AQUÍ (no en carpeta)
├── manifest.json ← AQUÍ
├── sw.js ← AQUÍ
└── trends-data.json ← AQUÍ

CARPETA scripts/:
└── get_trends.py ← AQUÍ (dentro de scripts/)

CARPETA .github/workflows/:
└── update-trends.yml ← AQUÍ (dentro de .github/workflows/)
```

---

## 🎯 Orden de subida (Recomendado)

1. ✅ Crea carpeta `.github/workflows/` y sube `update-trends.yml`
2. ✅ Crea carpeta `scripts/` y sube `get_trends.py`
3. ✅ Sube archivos raíz: `index.html`, `manifest.json`, `sw.js`, `trends-data.json`
4. ✅ Ve a **Actions** y verifica que está ejecutándose
5. ✅ Espera 5 minutos a que se ejecute la primera vez
6. ✅ Verifica que `trends-data.json` se actualizó

---

## ⚡ VERIFICACIÓN RÁPIDA

Después de subir todo, en GitHub:

```
✅ Ves carpeta "scripts" en la raíz
✅ Ves carpeta ".github" en la raíz
✅ Inside ".github": carpeta "workflows"
✅ Inside "workflows": archivo "update-trends.yml"
✅ Inside "scripts": archivo "get_trends.py"
✅ En raíz: index.html, manifest.json, sw.js, trends-data.json
```

Si algo falta = revisar nombres y ubicaciones

---

## 🚀 Después de subir:

1. Ve a **Actions** en tu repo
2. Deberías ver flujo ejecutándose
3. Espera a que termine (puede tardar 2-5 min)
4. Verifica en **Files** que `trends-data.json` tiene timestamp reciente

¡**Eso es todo!** Tu app ya está funcionando 🔥

---

## 💾 Resumen de nombres:

```
DESCARGASTE:              SUBE COMO:
index-real.html    →      index.html
manifest.json      →      manifest.json
sw.js              →      sw.js
scripts_get_trends.py → scripts/get_trends.py
.github_workflows_update-trends.yml → .github/workflows/update-trends.yml
trends-data.json   →      trends-data.json
```

¿Necesitas ayuda con algún paso específico? 👇
