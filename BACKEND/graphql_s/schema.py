from typing import List
import strawberry
from fastapi import Depends
from .types import Music, MusicInput, User
from db.PostgreSQL import get_db
import psycopg2

@strawberry.type
class Query:
    @strawberry.field
    def get_all_music(self, info) -> List[Music]:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, title, artist, genre, user_id FROM music")
        musics = cur.fetchall()
        cur.close()
        conn.close()
        return [
            Music(
                id=music[0],
                title=music[1],
                artist=music[2],
                genre=music[3],
                user_id=music[4]
            )
            for music in musics
        ]

    @strawberry.field
    def get_music(self, info, id: int) -> Music:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "SELECT id, title, artist, genre, user_id FROM music WHERE id = %s",
            (id,)
        )
        music = cur.fetchone()
        cur.close()
        conn.close()
        
        if music is None:
            raise Exception(f"Music with id {id} not found")
            
        return Music(
            id=music[0],
            title=music[1],
            artist=music[2],
            genre=music[3],
            user_id=music[4]
        )

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_music(self, info, music: MusicInput, user_id: int) -> Music:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO music (title, artist, genre, user_id)
            VALUES (%s, %s, %s, %s)
            RETURNING id, title, artist, genre, user_id
            """,
            (music.title, music.artist, music.genre, user_id)
        )
        new_music = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        
        return Music(
            id=new_music[0],
            title=new_music[1],
            artist=new_music[2],
            genre=new_music[3],
            user_id=new_music[4]
        )

    @strawberry.mutation
    def update_music(self, info, id: int, music: MusicInput) -> Music:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE music
            SET title = %s, artist = %s, genre = %s
            WHERE id = %s
            RETURNING id, title, artist, genre, user_id
            """,
            (music.title, music.artist, music.genre, id)
        )
        updated_music = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        
        if updated_music is None:
            raise Exception(f"Music with id {id} not found")
            
        return Music(
            id=updated_music[0],
            title=updated_music[1],
            artist=updated_music[2],
            genre=updated_music[3],
            user_id=updated_music[4]
        )

    @strawberry.mutation
    def delete_music(self, info, id: int) -> bool:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM music WHERE id = %s", (id,))
        deleted = cur.rowcount > 0
        conn.commit()
        cur.close()
        conn.close()
        
        if not deleted:
            raise Exception(f"Music with id {id} not found")
            
        return deleted