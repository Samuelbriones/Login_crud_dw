from fastapi import APIRouter, status, HTTPException, Depends
from pydantic import BaseModel
from db.MongoDB import get_db
from utils.Tocken import get_token
from bson import ObjectId

router = APIRouter()

class Music(BaseModel):
    title: str
    artist: str
    genre: str

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_music(music: Music, user_id: ObjectId = Depends(get_token)):
    db = get_db()
    musics = db.musics
    music_dict = music.dict()
    music_dict["user_id"] = user_id
    musics.insert_one(music_dict)
    return {"message": "Music created successfully"}

@router.get("/", status_code=status.HTTP_200_OK)
def get_musics(user_id: ObjectId = Depends(get_token)):
    db = get_db()
    musics = db.musics
    music_list = []
    for music in musics.find({"user_id": user_id}):
        music["_id"] = str(music["_id"])
        music["user_id"] = str(music["user_id"])
        music_list.append(music)
    return music_list

@router.put("/{music_id}", status_code=status.HTTP_200_OK)
def update_music(music_id: str, music: Music, user_id: ObjectId = Depends(get_token)):
    db = get_db()
    musics = db.musics
    result = musics.update_one({"_id": ObjectId(music_id), "user_id": user_id}, {"$set": music.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Music not found")
    return {"message": "Music updated successfully"}

@router.delete("/{music_id}", status_code=status.HTTP_200_OK)
def delete_music(music_id: str, user_id: ObjectId = Depends(get_token)):
    db = get_db()
    musics = db.musics
    result = musics.delete_one({"_id": ObjectId(music_id), "user_id": user_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Music not found")
    return {"message": "Music deleted successfully"}
