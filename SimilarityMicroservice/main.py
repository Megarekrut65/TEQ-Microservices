import decouple
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from fine_tuned_similarity_model import get_similarity
from models import SimilarityRequest

app = FastAPI()
origins = [
    decouple.config("ORIGIN")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/uk/similarity")
def calculate_similarity(request: SimilarityRequest):
    similarity = get_similarity(request.text1.lower(), request.text2.lower())

    return {"similarity": similarity}