from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def get_db():
    # Intenta usar MONGODB_URL primero (para Docker), luego construye desde variables individuales
    mongo_uri = os.getenv("MONGODB_URL")
    if not mongo_uri:
        mongo_user = os.getenv("MONGO_USER", "root")
        mongo_pass = os.getenv("MONGO_PASS", "rootpassword")
        mongo_host = os.getenv("MONGO_HOST", "localhost")
        mongo_port = os.getenv("MONGO_PORT", "27017")
        mongo_uri = f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}/"
    
    client = MongoClient(mongo_uri)
    db_name = os.getenv("MONGO_DB_NAME", "musicdb")
    db = client[db_name]
    return db
