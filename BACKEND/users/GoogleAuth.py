from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from db.PostgreSQL import get_db
from utils.Token import generate_token
from google.oauth2 import id_token
from google.auth.transport import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

class GoogleToken(BaseModel):
    token: str

@router.post("/google-login", status_code=status.HTTP_200_OK)
def google_login(google_token: GoogleToken):
    try:
        # Verificar el token de Google
        idinfo = id_token.verify_oauth2_token(
            google_token.token, 
            requests.Request(), 
            os.getenv("GOOGLE_CLIENT_ID")
        )

        # Extraer información del usuario
        google_id = idinfo['sub']
        email = idinfo['email']
        name = idinfo.get('name', email.split('@')[0])

        # Verificar si el usuario ya existe
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, name, email FROM users WHERE google_id = %s OR email = %s", (google_id, email))
        db_user = cur.fetchone()

        if db_user:
            # Usuario existe, actualizar google_id si es necesario
            if db_user[0]:
                cur.execute(
                    "UPDATE users SET google_id = %s, provider = 'google' WHERE id = %s",
                    (google_id, db_user[0])
                )
                conn.commit()
            user_id = db_user[0]
            user_name = db_user[1]
            user_email = db_user[2]
        else:
            # Crear nuevo usuario
            cur.execute(
                "INSERT INTO users (name, email, provider, google_id) VALUES (%s, %s, 'google', %s) RETURNING id",
                (name, email, google_id)
            )
            user_id = cur.fetchone()[0]
            user_name = name
            user_email = email
            conn.commit()

        cur.close()
        conn.close()

        # Generar token JWT
        token = generate_token(str(user_id), user_name, user_email)
        return {"token": token}

    except ValueError as e:
        # Token inválido
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Google token")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error during authentication: {str(e)}")
