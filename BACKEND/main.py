from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from users import Login, Register
from music import MusicMongoDB, MusicPostgreSQL
from db.PostgreSQL import create_tables
from contextlib import asynccontextmanager

# Lifespan para startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código de inicio
    create_tables()
    yield
    # Código de cierre (si necesitas algo al shutdown)
    # por ejemplo: cerrar conexiones a DB
    # await close_db_connections()

app = FastAPI(lifespan=lifespan)

# Configuración CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(Register.router, prefix="/api/users", tags=["Users"])
app.include_router(Login.router, prefix="/api/users", tags=["Users"])
app.include_router(MusicMongoDB.router, prefix="/api/mongodb/music", tags=["Music MongoDB"])
app.include_router(MusicPostgreSQL.router, prefix="/api/postgresql/music", tags=["Music PostgreSQL"])
