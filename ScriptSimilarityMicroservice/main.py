from fastapi import FastAPI

from app.codet5_description_similarity import get_similarity
from app.models import SimilarityRequest

app = FastAPI()

@app.post("/")
def calculate_similarity(request: SimilarityRequest):
    similarity = get_similarity(request.code1.lower(), request.code2.lower())

    return {"similarity": similarity}