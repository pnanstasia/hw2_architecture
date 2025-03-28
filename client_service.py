from fastapi import FastAPI, HTTPException, Depends
import os
from database import get_tracks, get_track_by_id, save_track, MusicLib
from business import recommend_song, sort_tracks

app = FastAPI()
TOKEN = os.getenv("API_TOKEN", "your secret token")

@app.get("/")
def root():
    return {"message": "Client Service for music library"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/save")
def save_song(track: MusicLib):
    return save_track(track)

@app.get("/get")
def all_songs():
    tracks = get_tracks()
    return tracks

@app.get("/get/{track_id}")
def get_song(track_id: int):
    track = get_track_by_id(track_id)
    if not track:
        raise HTTPException(status_code=404, detail="You have no such song in the liabrary")
    return track

@app.get("/recommendations")
def recommend(your_song: str):
    processed_tracks = recommend_song(your_song)["recommendations"]
    return {"recommendation": processed_tracks}

@app.get("/sorted_songs")
def sort_song():
    return sort_tracks()
