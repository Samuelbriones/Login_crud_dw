from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import jwt
import os
from datetime import datetime, timedelta

load_dotenv()

#token para la autenticacion y autorizacion de usuarios
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/login")

def get_user_id(token: str = Depends(oauth2_scheme)) -> int:
    try:
        payload: dict = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido",
            )
        return int(user_id)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expirado",
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No se pudieron validar las credenciales",
        ) from e

def generate_token(id: str, name: str, email: str, expired_minutes: int = 60) -> str:
    expiration = datetime.now() + timedelta(minutes=expired_minutes)
    payload = {
        "sub": id,
        "name": name,
        "email": email,
        "exp": expiration
    }
    token = jwt.encode(payload, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return token

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        return payload 
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None