from app.data_loader import load_csv
from app.embedding_generator import generate_embeddings, save_embeddings
from app.vector_search import VectorSearch

# Step 1: Load data
csv_path = "jobs.csv"
df = load_csv(csv_path)
print(f"Loaded {len(df)} job postings")

# Step 2: Generate embeddings
descriptions = df["jobDescRaw"].fillna("").tolist()
job_ids = df["lid"].tolist()
embeddings = generate_embeddings(descriptions)

# Step 3: Save embeddings
save_embeddings(embeddings, job_ids)

# Load the already generated embedding 
#import pickle
#import numpy as np
#with open("job_embeddings.pkl","rb") as f:
#    data=pickle.load(f)
#embeddings=np.array(data["embeddings"])

# Step 4: Index in FAISS
vs = VectorSearch(dim=embeddings[0].shape[0])
vs.add_embeddings(job_ids, embeddings)
vs.save("faiss.index", "job_ids.pkl")

print("Vector index built and saved.")
# Step 5: Plot histogram of normalized embedding similarity
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

#normalized_embeddings = normalize(embeddings)
similarities = []
sample_size=1000#len(embeddings)
for i in range(sample_size):
    query = embeddings[i].reshape(1, -1)
    results = vs.search(query, top_k=6)
    similarities.extend([score for _, score in results[1:]])



# Step 6: Simple similarity testing
sample_size = min(200, len(df))
similar_pairs = []

for i in range(sample_size):
    query = embeddings[i].reshape(1, -1)
    results = vs.search(query, top_k=6)
    job1 = df.iloc[i]
    for job_id, score in results[1:]:
        matched_rows = df[df["lid"] == job_id]
        if not matched_rows.empty and score > 0.8:
            job2 = matched_rows.iloc[0]
            similar_pairs.append((job1["jobTitle"], job2["jobTitle"], score))

# Show top matches
print("\n🔍 Sample of high-similarity job pairs:")
for t1, t2, s in similar_pairs[:10]:
    print(f"{t1} ↔ {t2} | Similarity: {s:.4f}")