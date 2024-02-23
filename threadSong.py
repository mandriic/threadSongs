from fastapi import FastAPI, Request
from db_connect import modificate_table
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/songs/")
def get_songs(song_data: dict = None):
    print("Getting songs")
    return(modificate_table("get", song_data))

@app.post("/songs/")
def post_songs(song_data: dict):
    print("Add new song:", song_data)
    modificate_table("add", song_data)

    # return {"message": "Song added successfully"}

@app.patch("/songs/")
def patch_songs(song_data: dict):
    print("Patching songs", song_data)
    modificate_table("patch", song_data)

@app.delete("/songs/")
def delete_songs(song_data: dict):
    print("Delete one song", song_data)
    modificate_table("delete", song_data)
    
    
    
    
#curl -X DELETE -H "Content-Type: application/json" -d '{"title": "Unfogiven", "artist": "Metallica", "album": "Black", "duration": "320"}' http://localhost:8000/songs/