from .PostgreSQL import get_db

def add_google_auth_columns():
    conn = get_db()
    cur = conn.cursor()
    
    # Verificar si la columna google_id existe
    cur.execute("""
        SELECT column_name 
        FROM information_schema.columns 
        WHERE table_name='users' AND column_name='google_id';
    """)
    
    if not cur.fetchone():
        # Añadir columnas necesarias para autenticación con Google
        cur.execute("""
            ALTER TABLE users 
            ADD COLUMN IF NOT EXISTS google_id VARCHAR(255) UNIQUE,
            ADD COLUMN IF NOT EXISTS provider VARCHAR(50) DEFAULT 'local';
        """)
        conn.commit()
        print("Columnas para autenticación con Google añadidas correctamente")
    else:
        print("Las columnas ya existen")
    
    cur.close()
    conn.close()