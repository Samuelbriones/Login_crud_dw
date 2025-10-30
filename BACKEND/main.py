from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from users import Login, Register, GoogleAuth
from music import MusicMongoDB, MusicPostgreSQL
from db.PostgreSQL import create_tables
from db.migrations import add_google_auth_columns
import strawberry
from strawberry.fastapi import GraphQLRouter
from graphql_s.schema import Query, Mutation  # Asegúrate de que este import coincida con la estructura de tu proyecto
from contextlib import asynccontextmanager

# Lifespan para startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código de inicio
    create_tables()
    add_google_auth_columns()
    yield
    # Código de cierre (si necesitas algo al shutdown)
    # por ejemplo: cerrar conexiones a DB
    # await close_db_connections()

app = FastAPI(lifespan=lifespan)

# Configuración del schema GraphQL
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

# Agregar la ruta GraphQL
app.include_router(graphql_app, prefix="/graphql")

# Configuración CORS
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000",
]
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
app.include_router(GoogleAuth.router, prefix="/api/users", tags=["Users"])
app.include_router(MusicMongoDB.router, prefix="/api/mongodb/music", tags=["Music MongoDB"])
app.include_router(MusicPostgreSQL.router, prefix="/api/postgresql/music", tags=["Music PostgreSQL"])
