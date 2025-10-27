from fastapi import APIRouter, status, HTTPException, Depends
from pydantic import BaseModel
from db.MongoDB import get_db
from passlib.context import CryptContext
from utils.Tocken import generate_token

router = APIRouter()

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

class User(BaseModel):
    email: str
    password: str

@router.post("/login", status_code=status.HTTP_200_OK)
def login(user: User):
    db = get_db()
    users = db.users
    db_user = users.find_one({"email": user.email})
    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")

    if not pwd_context.verify(user.password, db_user["password"]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")

    token = generate_token(str(db_user["_id"]), db_user["name"], db_user["email"])
    return {"token": token}
