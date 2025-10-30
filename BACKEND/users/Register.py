from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from db.PostgreSQL import get_db as get_postgres_db
from passlib.context import CryptContext
import re

router = APIRouter()

# Cambiado a Argon2
#registro de usuarios
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class User(BaseModel):
    name: str
    email: str
    password: str

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: User):
    # Validar formato de email
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="correo electronico invalido")

    # Validar longitud mínima de password
    if len(user.password) < 8:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contraseña debe tener al menos 8 caracteres")

    # Hashear password con Argon2
    hashed_password = pwd_context.hash(user.password)
    
    # Insertar en PostgreSQL
    conn = get_postgres_db()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (user.name, user.email, hashed_password)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        cur.close()
        conn.close()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Correo electronico ya registrado")
    finally:
        cur.close()
        conn.close()
    
    return {"message": "User registered successfully"}
