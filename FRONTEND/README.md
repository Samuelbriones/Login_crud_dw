# Frontend - Login & Music CRUD

Frontend desarrollado con **React + Vite** que se conecta al backend FastAPI.

## Características

- ✅ Sistema de autenticación (Login/Registro)
- ✅ Gestión CRUD de música
- ✅ Soporte para MongoDB y PostgreSQL
- ✅ Protección de rutas con JWT
- ✅ Interfaz moderna y responsive

## Estructura del Proyecto

```
FRONTEND/
├── src/
│   ├── components/           # Componentes reutilizables
│   │   ├── PrivateRoute.jsx   # Protección de rutas
│   │   ├── DashboardHeader.jsx # Header del dashboard
│   │   ├── DatabaseSelector.jsx # Selector MongoDB/PostgreSQL
│   │   ├── ErrorMessage.jsx    # Mensajes de error
│   │   ├── MusicForm.jsx       # Formulario de música
│   │   ├── MusicCard.jsx       # Tarjeta de canción
│   │   ├── MusicList.jsx       # Lista de canciones
│   │   └── DeleteModal.jsx     # Modal de confirmación
│   ├── pages/                # Páginas principales
│   │   ├── Login.jsx
│   │   ├── Register.jsx
│   │   └── Dashboard.jsx
│   ├── services/             # Servicios API
│   │   ├── auth.service.js
│   │   └── music.service.js
│   ├── hooks/                # Custom Hooks
│   │   └── useMusicManager.js  # Hook para gestionar música
│   ├── utils/                # Utilidades
│   │   └── helpers.js          # Funciones helper
│   ├── constants/            # Constantes
│   │   └── app.constants.js    # Configuración global
│   ├── styles/               # Estilos CSS
│   │   ├── Auth.css
│   │   ├── Dashboard.css
│   │   └── Modal.css
│   ├── App.jsx
│   └── main.jsx
└── package.json
```

## Instalación

```bash
cd FRONTEND
npm install
```

## Configuración

El frontend está configurado para conectarse al backend en:
- **API Base URL**: `http://localhost:8000`

Si necesitas cambiar la URL, edita los archivos:
- `src/services/auth.service.js`
- `src/services/music.service.js`

## Ejecutar el Proyecto

```bash
npm run dev
```

El frontend estará disponible en: **http://localhost:5173**

## Endpoints que Consume

### Autenticación
- `POST /api/users/register` - Registrar usuario
- `POST /api/users/login` - Iniciar sesión

### Música (MongoDB)
- `GET /api/mongodb/music/` - Listar canciones
- `POST /api/mongodb/music/` - Crear canción
- `PUT /api/mongodb/music/:id` - Actualizar canción
- `DELETE /api/mongodb/music/:id` - Eliminar canción

### Música (PostgreSQL)
- `GET /api/postgresql/music/` - Listar canciones
- `POST /api/postgresql/music/` - Crear canción
- `PUT /api/postgresql/music/:id` - Actualizar canción
- `DELETE /api/postgresql/music/:id` - Eliminar canción

## Flujo de Uso

1. **Registro**: Crear cuenta con nombre, email y contraseña (mínimo 8 caracteres)
2. **Login**: Iniciar sesión con email y contraseña
3. **Dashboard**: 
   - Seleccionar base de datos (MongoDB o PostgreSQL)
   - Agregar, editar o eliminar canciones
   - Cerrar sesión

## Tecnologías

- React 18
- Vite
- React Router DOM
- Axios
- CSS3

## Scripts Disponibles

- `npm run dev` - Ejecutar en modo desarrollo
- `npm run build` - Compilar para producción
- `npm run preview` - Vista previa de producción

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.
