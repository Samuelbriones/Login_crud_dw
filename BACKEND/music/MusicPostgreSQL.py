from fastapi import APIRouter, status, HTTPException, Depends
from pydantic import BaseModel
from db.PostgreSQL import get_db
from utils.Tocken import get_user_id

router = APIRouter()

class Music(BaseModel):
    title: str
    artist: str
    genre: str

#router de FastAPI que define los endpoints para crud de musica

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_music(music: Music, user_id: int = Depends(get_user_id)):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO music (title, artist, genre, user_id) VALUES (%s, %s, %s, %s)",
        (music.title, music.artist, music.genre, user_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Music created successfully"}

@router.get("/", status_code=status.HTTP_200_OK)
def get_musics(user_id: int = Depends(get_user_id)):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM music WHERE user_id = %s", (user_id,))
    musics = cur.fetchall()
    cur.close()
    conn.close()
    music_list = []
    for music in musics:
        music_list.append({"id": music[0], "title": music[1], "artist": music[2], "genre": music[3]})
    return music_list

@router.put("/{music_id}", status_code=status.HTTP_200_OK)
def update_music(music_id: int, music: Music, user_id: int = Depends(get_user_id)):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "UPDATE music SET title = %s, artist = %s, genre = %s WHERE id = %s AND user_id = %s",
        (music.title, music.artist, music.genre, music_id, user_id)
    )
    conn.commit()
    cur.close()
    conn.close()
    if cur.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Music not found")
    return {"message": "Music updated successfully"}

@router.delete("/{music_id}", status_code=status.HTTP_200_OK)
def delete_music(music_id: int, user_id: int = Depends(get_user_id)):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM music WHERE id = %s AND user_id = %s", (music_id, user_id))
    conn.commit()
    cur.close()
    conn.close()
    if cur.rowcount == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Music not found")
    return {"message": "Music deleted successfully"}
