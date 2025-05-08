from sentence_transformers import SentenceTransformer, util
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5-base-multi-sum")
model = AutoModelForSeq2SeqLM.from_pretrained("Salesforce/codet5-base-multi-sum")

similarity_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def get_summary(code):
    inputs = tokenizer.encode(code, return_tensors="pt", truncation=True, max_length=512)
    summary_ids = model.generate(inputs, max_length=64, num_beams=5, early_stopping=True)

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def get_similarity(code1:str, code2:str)->float:
    summary1 = get_summary(code1)
    summary2 = get_summary(code2)

    embeddings = similarity_model.encode([summary1, summary2], convert_to_tensor=True)
    score = util.cos_sim(embeddings[0], embeddings[1])
    return float(score[0])
