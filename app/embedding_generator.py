from sentence_transformers import SentenceTransformer
import numpy as np
import pickle

def generate_embeddings(texts, model_name="all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(texts, show_progress_bar=True)
    return embeddings

def save_embeddings(embeddings, job_ids, path="job_embeddings.pkl"):
    with open(path, "wb") as f:
        pickle.dump({"embeddings": embeddings, "job_ids": job_ids}, f)
