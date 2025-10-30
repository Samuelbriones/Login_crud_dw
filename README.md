# Login CRUD - Dual Database Music Manager

Sistema de gestión de música con autenticación de usuarios que soporta tanto MongoDB como PostgreSQL.

## 🚀 Características

- 🔐 **Autenticación completa**: Login tradicional + Google OAuth
- 🗄️ **Dual Database**: Soporte para MongoDB y PostgreSQL
- 🎵 **CRUD de música**: Crear, leer, actualizar y eliminar canciones
- 🔒 **Seguridad**: Hashing con Argon2, JWT tokens
- 🐳 **Dockerizado**: Fácil despliegue con Docker Compose

## 📋 Requisitos Previos

- Docker y Docker Compose
- Node.js 16+ (para desarrollo frontend)
- Python 3.9+ (para desarrollo backend)

## 🛠️ Instalación

### 1. Clonar el repositorio

```bash
git clone <repository-url>
cd Login_crud_dw
```

### 2. Configurar variables de entorno

```bash
cd BACKEND
cp .env.example .env
```

Edita el archivo `.env` con tus credenciales:

```env
# JWT Configuration
SECRET_KEY=tu-clave-secreta-super-segura
ALGORITHM=HS256

# Google OAuth Configuration
GOOGLE_CLIENT_ID=tu-google-client-id
GOOGLE_CLIENT_SECRET=tu-google-client-secret
```

### 3. Iniciar con Docker

```bash
# Desde el directorio raíz
docker-compose up -d
```

Esto iniciará:
- MongoDB en puerto 27017
- PostgreSQL en puerto 5432
- Backend API en puerto 8000

### 4. Iniciar Frontend

```bash
cd FRONTEND
npm install
npm run dev
```

El frontend estará disponible en `http://localhost:5173`

## 📚 API Endpoints

### Autenticación

- `POST /api/users/register` - Registrar usuario
- `POST /api/users/login` - Login tradicional
- `POST /api/users/google-login` - Login con Google

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

## 🏗️ Estructura del Proyecto

```
Login_crud_dw/
├── BACKEND/
│   ├── db/
│   │   ├── MongoDB.py
│   │   └── PostgreSQL.py
│   ├── users/
│   │   ├── Login.py
│   │   ├── Register.py
│   │   └── GoogleAuth.py
│   ├── music/
│   │   ├── MusicMongoDB.py
│   │   └── MusicPostgreSQL.py
│   ├── utils/
│   │   └── Token.py
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── FRONTEND/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│   └── package.json
└── docker-compose.yml
```

## 🔐 Configuración de Google OAuth

1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Crea un nuevo proyecto o selecciona uno existente
3. Habilita la API de Google+ 
4. Crea credenciales OAuth 2.0
5. Agrega los orígenes autorizados:
   - `http://localhost:5173`
   - `http://localhost:3000`
6. Copia el Client ID y Client Secret al archivo `.env`

## 🧪 Desarrollo

### Backend

```bash
cd BACKEND
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd FRONTEND
npm run dev
```

## 📝 Tecnologías Utilizadas

### Backend
- FastAPI
- PostgreSQL
- MongoDB
- Argon2 (Password Hashing)
- PyJWT
- Google Auth Library

### Frontend
- React
- Vite
- React Router DOM
- Axios
- Google OAuth

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría realizar.

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
