import numpy as np
import faiss
import pickle
from sklearn.preprocessing import normalize

class VectorSearch:
    def __init__(self, dim: int, use_cosine=True):
        self.dim = dim
        self.use_cosine = use_cosine
        self.index = faiss.IndexFlatIP(dim) if use_cosine else faiss.IndexFlatL2(dim)
        self.job_id_map = []

    def _prepare(self, vectors):
        vectors = np.asarray(vectors).astype('float32')
        return normalize(vectors) if self.use_cosine else vectors

    def add_embeddings(self, job_ids, embeddings):
        prepared = self._prepare(embeddings)
        self.index.add(prepared)
        self.job_id_map.extend(job_ids)

    def search(self, query_embedding, top_k=5):
        query = np.asarray(query_embedding).astype('float32')
        if query.ndim == 1:
            query = query.reshape(1, -1)
        if self.use_cosine:
            query = normalize(query)
        D, I = self.index.search(query, top_k)
        return [(self.job_id_map[i], float(d)) for d, i in zip(D[0], I[0])]

    def save(self, index_path="faiss.index", map_path="job_ids.pkl"):
        faiss.write_index(self.index, index_path)
        with open(map_path, "wb") as f:
            pickle.dump(self.job_id_map, f)

    def load(self, index_path="faiss.index", map_path="job_ids.pkl"):
        self.index = faiss.read_index(index_path)
        with open(map_path, "rb") as f:
            self.job_id_map = pickle.load(f)