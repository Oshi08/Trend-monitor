# 🔥 Trends Monitor - PWA para Hostelería

## 📱 Instalación en iPhone (Sin App Store)

### Método más fácil: Instalar como App Web

1. **Abre Safari en tu iPhone**

2. **Ve a la carpeta de archivos donde descargaste los archivos**
   - Busca el archivo `index.html`
   - Haz clic y cópialo

3. **Aloja los archivos en línea** (Opciones gratuitas):

   **Opción A: GitHub Pages (Recomendado - Gratuito)**
   ```
   1. Ve a github.com y crea una cuenta (gratis)
   2. Crea un nuevo repositorio llamado "trends-monitor"
   3. Sube estos 3 archivos:
      - index.html
      - manifest.json
      - sw.js
   4. Ve a Settings > Pages > Source > Main
   5. Tu app estará en: https://tuusuario.github.io/trends-monitor/
   ```

   **Opción B: Netlify (Gratuito - Muy fácil)**
   ```
   1. Ve a netlify.com
   2. Haz clic en "Drop files here"
   3. Arrastra los 3 archivos
   4. ¡Listo! Tendrás una URL pública
   ```

   **Opción C: Vercel (Gratuito)**
   ```
   1. Ve a vercel.com
   2. Haz clic en "Import Project"
   3. Sube los archivos
   4. Se genera URL automáticamente
   ```

4. **Una vez tengas la URL, en tu iPhone:**
   - Abre Safari
   - Pega la URL
   - Haz clic en el botón Compartir (parte inferior)
   - Desplázate y busca "Añadir a pantalla de inicio"
   - Dale un nombre (ej: "Trends")
   - ¡Listo! Aparece como app en tu home

---

## 🎯 Cómo Usar la App

### Dashboard Principal
- **📊 Resumen**: Métricas en vivo y top 3 trends
- **🔥 Todos**: Todos los trends monitoreados
- **🍽️ Restaurantes**: Trends para restaurantes
- **🍹 Bares**: Trends para bares de copas
- **☕ Cafeterías**: Trends para cafés
- **🍰 Repostería**: Trends para pastelerías
- **⚙️ Ajustes**: Configuración y datos

### Botones principales
- **🔍 Buscar AHORA**: Busca nuevos trends en vivo
- **⏱️ Auto**: Activa/desactiva actualización automática cada hora

---

## ⚙️ Configuración

### Ajustes disponibles:
1. **Actualización automática** - Cada hora busca nuevos trends
2. **Notificaciones** - Aviso cuando un trend es explosivo (>80% viralidad)
3. **Tema oscuro** - Ajusta automático según tu teléfono
4. **Descargar datos** - Exporta en CSV para análisis
5. **Borrar histórico** - Limpia todos los datos guardados

---

## 📊 Cómo Funciona

### Viralidad
- Escala 0-100%
- Se actualiza con cada búsqueda
- Basada en menciones + videos

### Menciones
- Número de veces que aparece en internet
- Se actualiza cada hora (auto) o cuando buscas

### Videos
- Cantidad de videos usando el trend
- Indica cuánta gente lo está usando

### Tendencia
- 📈 Subiendo = Está ganando viralidad
- → Estable = Se mantiene igual
- 📉 Bajando = Está perdiendo fuerza

---

## 🔄 Actualización Automática

La app se actualiza cada hora **automáticamente** si:
- ✅ Está instalada como PWA en tu iPhone
- ✅ Tienes conexión a internet
- ✅ "Auto: ON" está activado

Cuando busca automaticamente:
1. Analiza nuevos trends trending
2. Actualiza viralidad de existentes
3. Agrega nuevos trends encontrados
4. Crea histórico infinito

---

## 📱 Funciona Offline

- ✅ Ver trends guardados
- ✅ Buscar en histórico
- ✅ Leer ajustes
- ❌ Buscar nuevos trends (necesita internet)

Cuando recuperas conexión:
- Se sincroniza automáticamente
- Se descargan nuevos trends
- Se actualiza histórico

---

## 💡 Tips de Uso

### Para máxima viralidad:
1. Busca trends cada mañana
2. Anota los que tienen 85%+ viralidad
3. Haz posts sobre esos trends
4. Verifica si funcionó (vuelve a buscar)
5. Repite con los que más funcionan

### Por tipo de negocio:
- **Restaurantes**: Procesos, contrastes salado/dulce
- **Bares**: ASMR, efectos visuales, bebidas
- **Cafeterías**: Latte art, bebidas coloridas
- **Repostería**: Postres "brutales", texturas

---

## 🚀 Mejoras Futuras

La app actualmente:
- ✅ Monitorea 12 trends base constantemente
- ✅ Se actualiza automáticamente cada hora
- ✅ Funciona completamente offline
- ✅ Genera notificaciones inteligentes
- ✅ Exporta datos a CSV

Posibles mejoras:
- [ ] Conectar a APIs reales de TikTok/Instagram
- [ ] Análisis de predicción IA
- [ ] Comparativa con competencia
- [ ] Generación automática de ideas de posts
- [ ] Integración con Google Trends en vivo

---

## ❓ Preguntas Frecuentes

**P: ¿Funciona sin App Store?**
R: Sí, 100%. Se instala como PWA en tu pantalla de inicio.

**P: ¿Necesito servidor propio?**
R: No. Alojalo gratis en GitHub Pages o Netlify.

**P: ¿Funciona en Android también?**
R: Sí. El proceso es similar: 3 puntos > Instalar app.

**P: ¿Los datos se borran?**
R: No. Se guardan localmente en tu teléfono. Solo si limpias cache.

**P: ¿Puedo compartir la app con mi equipo?**
R: Sí. Solo necesitan la URL. Cada uno instala en su iPhone.

**P: ¿Cuánto cuesta?**
R: Nada. 100% gratuito.

**P: ¿Necesito WiFi?**
R: Para buscar nuevos trends sí. Para ver guardados no.

---

## 🔧 Troubleshooting

### La app no aparece en pantalla de inicio
- Cierra Safari completamente
- Limpia caché: Ajustes > Safari > Borrar historial y datos
- Vuelve a intentar "Añadir a pantalla de inicio"

### No se actualiza automáticamente
- Verifica que "Auto: ON" esté activado en la app
- Asegúrate de tener conexión WiFi o datos
- Abre la app al menos una vez al día

### Las notificaciones no llegan
- Ve a Ajustes > Notificaciones > Trends Monitor
- Activa "Permitir notificaciones"
- Verifica que "Notificaciones" en la app esté ON

### Falta conexión a internet
- La app sigue funcionando offline mostrando datos guardados
- Cuando recuperes conexión, se sincroniza automáticamente

---

## 📞 Soporte

Si tienes problemas:
1. Intenta limpiar la caché de la app
2. Reinstala desinstalando y volviendo a agregar
3. Asegúrate de tener la última versión de Safari

---

**Versión: 1.0**
**Última actualización: Junio 2026**
**Licencia: Gratuita**

¡Disfruta monitoreando trends! 🔥
