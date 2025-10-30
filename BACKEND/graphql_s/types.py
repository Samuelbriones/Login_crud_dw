from typing import Optional, List
import strawberry
from datetime import datetime

@strawberry.type
class Music:
    id: int
    title: str
    artist: str
    genre: str
    user_id: int

@strawberry.input
class MusicInput:
    title: str
    artist: str
    genre: str

@strawberry.type
class User:
    id: int
    name: str
    email: str
    provider: str
    google_id: Optional[str] = None