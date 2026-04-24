from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
from model import recommend_movies # Ensure model.py has this function

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Added 'username' to the model to prevent 422 errors when frontend sends it
class MovieRequest(BaseModel):
    username: Optional[str] = None 
    genre: str
    rating: float

@app.get("/")
def login_page():
    return FileResponse("login.html")

@app.get("/movie")
def movie_page():
    return FileResponse("movie.html")

@app.post("/recommend")
def recommend(data: MovieRequest):
    # Passes genre and rating strings/floats to your logic
    movies = recommend_movies(data.genre, data.rating)
    return {"recommendations": movies}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)