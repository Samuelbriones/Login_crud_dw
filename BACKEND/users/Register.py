from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from db.MongoDB import get_db
from passlib.context import CryptContext
import re

router = APIRouter()

# Cambiado a Argon2
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class User(BaseModel):
    name: str
    email: str
    password: str

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: User):
    db = get_db()
    users = db.users

    # Verificar si el email ya existe
    if users.find_one({"email": user.email}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    # Validar formato de email
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email format")

    # Validar longitud mínima de password
    if len(user.password) < 8:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password must be at least 8 characters long")

    # Hashear password con Argon2
    hashed_password = pwd_context.hash(user.password)
    user_dict = user.dict()
    user_dict["password"] = hashed_password
    users.insert_one(user_dict)
    
    return {"message": "User registered successfully"}
