from fastapi import APIRouter, status, HTTPException, Depends
from pydantic import BaseModel
from db.PostgreSQL import get_db
from passlib.context import CryptContext
from utils.Tocken import generate_token

router = APIRouter()

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class User(BaseModel):
    email: str
    password: str

@router.post("/login", status_code=status.HTTP_200_OK)
def login(user: User):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email, password FROM users WHERE email = %s", (user.email,))
    db_user = cur.fetchone()
    cur.close()
    conn.close()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")

    if not pwd_context.verify(user.password, db_user[3]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")

    token = generate_token(str(db_user[0]), db_user[1], db_user[2])
    return {"token": token}
