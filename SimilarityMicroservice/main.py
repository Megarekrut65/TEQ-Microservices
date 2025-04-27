from fastapi import FastAPI

from fine_tuned_similarity_model import get_similarity
from models import SimilarityRequest

app = FastAPI()

@app.post("/similarity")
def calculate_similarity(request: SimilarityRequest):
    similarity = get_similarity(request.text1, request.text2)

    return {"similarity": similarity}