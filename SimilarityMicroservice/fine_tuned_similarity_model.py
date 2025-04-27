from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("Models/fine_tuned_similarity_model")

def get_similarity(text1:str, text2:str)->float:
    embeddings = model.encode([text1, text2], convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()

    return similarity