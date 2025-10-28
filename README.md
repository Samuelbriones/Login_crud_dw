# Login & Music CRUD - Proyecto Full Stack

Aplicación full stack con sistema de autenticación y gestión CRUD de música, soportando **MongoDB** y **PostgreSQL**.

## 🚀 Características

- ✅ Backend con **FastAPI** (Python)
- ✅ Frontend con **React + Vite**
- ✅ Autenticación con JWT
- ✅ CRUD completo de música
- ✅ Soporte para MongoDB y PostgreSQL
- ✅ Docker Compose para bases de datos
- ✅ Contraseñas hasheadas con Argon2

## 📁 Estructura del Proyecto

```
Login_crud_dw/
├── BACKEND/
│   ├── db/              # Conexiones a bases de datos
│   ├── users/           # Endpoints de autenticación
│   ├── music/           # Endpoints CRUD de música
│   ├── utils/           # JWT y utilidades
│   └── main.py          # Aplicación principal
├── FRONTEND/
│   ├── src/
│   │   ├── components/  # Componentes React
│   │   ├── pages/       # Páginas de la aplicación
│   │   ├── services/    # Servicios API
│   │   └── styles/      # Estilos CSS
│   └── package.json
└── docker-compose.yml   # Configuración de bases de datos
```

## 🛠️ Tecnologías

### Backend
- FastAPI
- PostgreSQL (psycopg2)
- MongoDB (pymongo)
- JWT (PyJWT)
- Argon2 (passlib)

### Frontend
- React 18
- Vite
- React Router DOM
- Axios

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone <tu-repositorio>
cd Login_crud_dw
```

### 2. Configurar bases de datos con Docker

```bash
docker-compose up -d
```

Esto iniciará:
- **PostgreSQL** en puerto 5432
- **MongoDB** en puerto 27017

### 3. Configurar Backend

```bash
cd BACKEND

# Crear archivo .env
echo "SECRET_KEY=tu_clave_secreta_aqui" > .env
echo "ALGORITHM=HS256" >> .env

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
uvicorn main:app --reload
```

El backend estará en: **http://localhost:8000**

### 4. Configurar Frontend

```bash
cd FRONTEND

# Instalar dependencias
npm install

# Ejecutar servidor de desarrollo
npm run dev
```

El frontend estará en: **http://localhost:5173**

## 🔑 Variables de Entorno

Crea un archivo `.env` en la carpeta `BACKEND/`:

```env
SECRET_KEY=tu_clave_secreta_super_segura
ALGORITHM=HS256
```

## 🎯 Endpoints del Backend

### Autenticación
- `POST /api/users/register` - Registrar usuario
- `POST /api/users/login` - Iniciar sesión (retorna JWT)

### Música (MongoDB)
- `GET /api/mongodb/music/` - Obtener todas las canciones
- `POST /api/mongodb/music/` - Crear canción
- `PUT /api/mongodb/music/{id}` - Actualizar canción
- `DELETE /api/mongodb/music/{id}` - Eliminar canción

### Música (PostgreSQL)
- `GET /api/postgresql/music/` - Obtener todas las canciones
- `POST /api/postgresql/music/` - Crear canción
- `PUT /api/postgresql/music/{id}` - Actualizar canción
- `DELETE /api/postgresql/music/{id}` - Eliminar canción

## 📝 Uso

1. **Registrar usuario**: Crear cuenta con nombre, email y contraseña (mínimo 8 caracteres)
2. **Iniciar sesión**: Login con credenciales para obtener token JWT
3. **Gestionar música**: 
   - Seleccionar base de datos (MongoDB o PostgreSQL)
   - Crear, editar, listar o eliminar canciones
   - Cada usuario solo ve sus propias canciones

## 🔒 Seguridad

- Contraseñas hasheadas con **Argon2**
- Autenticación basada en **JWT**
- Protección de rutas en frontend
- CORS configurado para desarrollo
- Validación de datos con Pydantic

## 📊 Base de Datos

### PostgreSQL (Tablas)
- `users`: id, name, email, password
- `music`: id, title, artist, genre, user_id

### MongoDB (Colecciones)
- `musics`: _id, title, artist, genre, user_id

## 🧪 Documentación API

Una vez el backend esté corriendo, accede a:
- Swagger UI: **http://localhost:8000/docs**
- ReDoc: **http://localhost:8000/redoc**

## 🎨 Capturas

El frontend incluye:
- Página de registro con validación
- Página de login
- Dashboard con selector de base de datos
- Tarjetas de música con acciones CRUD
- Diseño responsive y moderno

## 📄 Licencia

Este proyecto es de código abierto.
