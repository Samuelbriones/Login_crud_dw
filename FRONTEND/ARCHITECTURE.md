# Arquitectura del Frontend

## 📐 Principios de Diseño

Este frontend está construido siguiendo principios de **arquitectura modular** y **componentes reutilizables** para facilitar el mantenimiento y escalabilidad.

## 🗂️ Estructura de Carpetas

### `/src/components`
Componentes reutilizables que pueden ser usados en múltiples páginas.

- **PrivateRoute.jsx**: HOC para proteger rutas que requieren autenticación
- **DashboardHeader.jsx**: Header con título y botón de logout
- **DatabaseSelector.jsx**: Selector para cambiar entre MongoDB y PostgreSQL
- **ErrorMessage.jsx**: Componente para mostrar mensajes de error
- **MusicForm.jsx**: Formulario para crear/editar canciones
- **MusicCard.jsx**: Tarjeta individual de canción con acciones
- **MusicList.jsx**: Lista/grid de canciones
- **DeleteModal.jsx**: Modal de confirmación para eliminación

### `/src/pages`
Páginas principales de la aplicación.

- **Login.jsx**: Página de inicio de sesión
- **Register.jsx**: Página de registro de usuarios
- **Dashboard.jsx**: Panel principal con gestión de música

### `/src/services`
Servicios para comunicación con la API.

- **auth.service.js**: Login, registro, manejo de tokens
- **music.service.js**: CRUD de música (MongoDB y PostgreSQL)

### `/src/hooks`
Custom hooks para lógica reutilizable.

- **useMusicManager.js**: Hook personalizado que encapsula toda la lógica de gestión de música (cargar, crear, actualizar, eliminar)

### `/src/utils`
Funciones utilitarias generales.

- **helpers.js**: Funciones helper como validaciones, formateo de errores, etc.

### `/src/constants`
Constantes de la aplicación.

- **app.constants.js**: URLs, endpoints, mensajes, estados iniciales, reglas de validación

### `/src/styles`
Archivos CSS organizados por funcionalidad.

- **Auth.css**: Estilos para login y registro
- **Dashboard.css**: Estilos para el dashboard
- **Modal.css**: Estilos para modales

## 🔄 Flujo de Datos

```
Usuario Interactúa
       ↓
  Componente (UI)
       ↓
  Custom Hook / Handler
       ↓
    Service (API)
       ↓
    Backend (FastAPI)
       ↓
  Base de Datos (MongoDB/PostgreSQL)
```

## 🎯 Patrones Utilizados

### 1. **Separación de Responsabilidades**
- **Componentes**: Solo UI y eventos
- **Hooks**: Lógica de negocio y estado
- **Services**: Comunicación con API
- **Utils**: Funciones puras reutilizables

### 2. **Custom Hooks**
`useMusicManager` encapsula:
- Estado de música
- Estado de carga
- Manejo de errores
- Operaciones CRUD
- Cambio de base de datos

### 3. **Composición de Componentes**
Dashboard se compone de:
```jsx
<Dashboard>
  <DashboardHeader />
  <DatabaseSelector />
  <ErrorMessage />
  <MusicForm />
  <MusicList>
    <MusicCard />
  </MusicList>
  <DeleteModal />
</Dashboard>
```

### 4. **Props Drilling Controlado**
Se pasan solo las props necesarias a cada componente.

### 5. **Constantes Centralizadas**
Todas las URLs, mensajes y configuraciones en un solo lugar.

## 🔧 Ventajas de esta Arquitectura

### ✅ Escalabilidad
- Fácil agregar nuevas funcionalidades
- Componentes independientes
- Lógica desacoplada

### ✅ Mantenibilidad
- Código organizado y predecible
- Fácil encontrar y modificar código
- Componentes pequeños y enfocados

### ✅ Reutilización
- Componentes genéricos
- Hooks personalizados
- Funciones utilitarias

### ✅ Testeo
- Componentes aislados
- Lógica separada de UI
- Funciones puras

## 📝 Ejemplo de Uso

### Agregar una nueva funcionalidad

**1. Crear el servicio** (`services/`)
```js
export const playlistService = {
  async getAll() { ... }
};
```

**2. Crear el hook** (`hooks/`)
```js
export const usePlaylistManager = () => {
  // Lógica aquí
};
```

**3. Crear componentes** (`components/`)
```jsx
function PlaylistCard({ playlist }) {
  return <div>...</div>;
}
```

**4. Usar en página** (`pages/`)
```jsx
function Playlists() {
  const { playlists } = usePlaylistManager();
  return <PlaylistCard playlist={playlists[0]} />;
}
```

## 🎨 Convenciones de Código

### Nombres de Archivos
- Componentes: `PascalCase.jsx`
- Hooks: `useCamelCase.js`
- Services: `camelCase.service.js`
- Utils: `camelCase.js`

### Nombres de Funciones
- Componentes: `PascalCase`
- Hooks: `useCamelCase`
- Handlers: `handleCamelCase`
- Funciones: `camelCase`

### Props
- Event handlers: `onAction` (ej: `onEdit`, `onDelete`)
- Boolean props: `isActive`, `hasError`
- Data props: Descriptivos (ej: `music`, `musics`, `activeDb`)

## 🚀 Futuras Mejoras

- [ ] Implementar Context API para estado global
- [ ] Agregar testing con Vitest/Jest
- [ ] Implementar lazy loading de componentes
- [ ] Agregar TypeScript para type safety
- [ ] Implementar cache de API con React Query
- [ ] Agregar internacionalización (i18n)
- [ ] Implementar themes (dark mode)
