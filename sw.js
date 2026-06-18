const CACHE_NAME = 'trends-monitor-v1';
const urlsToCache = [
  '/',
  '/index.html',
  '/manifest.json'
];

// Instalar service worker
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return cache.addAll(urlsToCache).catch(() => {
          // Si falla agregar a caché, simplemente continuar
          console.log('Cache installation partial');
        });
      })
  );
  self.skipWaiting();
});

// Activar service worker
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Fetch - Estrategia: Network first, luego cache
self.addEventListener('fetch', event => {
  // Solo procesar GET requests
  if (event.request.method !== 'GET') {
    return;
  }

  event.respondWith(
    fetch(event.request)
      .then(response => {
        // Guardaren caché si es exitoso
        if (!response || response.status !== 200 || response.type === 'error') {
          return response;
        }

        const responseToCache = response.clone();
        caches.open(CACHE_NAME)
          .then(cache => {
            cache.put(event.request, responseToCache);
          });

        return response;
      })
      .catch(() => {
        // Si falla la red, usar caché
        return caches.match(event.request)
          .then(response => {
            return response || new Response('Offline - Sin caché disponible', {
              status: 503,
              statusText: 'Service Unavailable',
              headers: new Headers({
                'Content-Type': 'text/plain'
              })
            });
          });
      })
  );
});

// Actualización en background cada hora
self.addEventListener('message', event => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});

// Sincronización en background (si está soportado)
if ('sync' in self.registration) {
  self.addEventListener('sync', event => {
    if (event.tag === 'update-trends') {
      event.waitUntil(updateTrends());
    }
  });
}

async function updateTrends() {
  try {
    // Aquí iría la lógica de actualización de trends
    console.log('Trends actualizado en background');
  } catch (error) {
    console.error('Error actualizando trends:', error);
  }
}

// Notificaciones push (cuando se implemente backend)
self.addEventListener('push', event => {
  if (!event.data) return;

  const options = {
    body: event.data.text(),
    icon: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect fill="%231a73e8" width="100" height="100"/><text x="50" y="50" font-size="80" text-anchor="middle" dominant-baseline="middle">🔥</text></svg>',
    badge: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text x="50" y="50" font-size="80" text-anchor="middle" dominant-baseline="middle">🔥</text></svg>',
    tag: 'trends-notification',
    requireInteraction: false
  };

  event.waitUntil(
    self.registration.showNotification('🔥 Trends Monitor', options)
  );
});

// Click en notificación
self.addEventListener('notificationclick', event => {
  event.notification.close();
  event.waitUntil(
    clients.matchAll({ type: 'window' }).then(clientList => {
      // Si la app está abierta, enfocar la ventana
      for (let i = 0; i < clientList.length; i++) {
        if (clientList[i].url === '/' && 'focus' in clientList[i]) {
          return clientList[i].focus();
        }
      }
      // Si no está abierta, abrir nueva ventana
      if (clients.openWindow) {
        return clients.openWindow('/');
      }
    })
  );
});

// Periodic Background Sync (actualización cada hora en background)
if ('periodicSync' in self.registration) {
  self.addEventListener('periodicsync', event => {
    if (event.tag === 'update-trends-hourly') {
      event.waitUntil(updateTrendsInBackground());
    }
  });
}

async function updateTrendsInBackground() {
  try {
    // Notificar a clientes que actualicen
    const clients = await self.clients.matchAll();
    clients.forEach(client => {
      client.postMessage({
        type: 'UPDATE_TRENDS',
        timestamp: new Date()
      });
    });
  } catch (error) {
    console.error('Error en actualización background:', error);
  }
}

// Mantener el service worker vivo
setInterval(() => {
  // Pequeña tarea para evitar que el SW se duerma
}, 30000);
