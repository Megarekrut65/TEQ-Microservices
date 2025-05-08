import decouple
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.codet5_description_similarity import get_similarity
from app.models import SimilarityRequest

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

@app.post("/pl/similarity")
def calculate_similarity(request: SimilarityRequest):
    similarity = get_similarity(request.code1.lower(), request.code2.lower())

    return {"similarity": similarity}