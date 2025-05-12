from fastapi import FastAPI

from app.fine_tuned_similarity_model import get_similarity
from app.models import SimilarityRequest

app = FastAPI()

@app.post("/")
def calculate_similarity(request: SimilarityRequest):
    similarity = get_similarity(request.text1.lower(), request.text2.lower())

    return {"similarity": similarity}