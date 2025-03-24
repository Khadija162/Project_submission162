# README.md

# 🧠 Job Post Duplicate Detection with Vector Search

This project identifies duplicate job postings using text embeddings and FAISS vector search. It uses sentence-transformers to compute embeddings and FastAPI to expose a REST API.

## 📦 Project Structure
```
├── app/
│   ├── data_loader.py         # Load and store data
│   ├── embedding_generator.py # Embedding logic
│   └── vector_search.py       # FAISS-based vector search
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── run.py                     # Full pipeline runner
├── final_output.csv           # Sample job_id pairs & similarity
├── job_embeddings.pkl         # Embedding cache (not committed)
└── notebooks/
    └── 01_data_exploration.ipynb
```

## 🚀 Quick Start

### 🐳 Docker
```bash
docker-compose up --build
```


### 🔧 Local
```bash
pip install -r requirements.txt
python run.py

```

## 📊 Evaluation Output
- Final results: `final_output.csv`
- Contains: `Job ID 1`, `Job ID 2`, `Similarity Score`

## ✅ Features
- Sentence embeddings using `all-MiniLM-L6-v2`
- FAISS for fast nearest neighbor search
- Threshold-based evaluation with F1/Precision/Recall
- Dockerized for reproducibility

## 📁 Submission
- ✅ Source code & scripts
- ✅ Docker 
- ✅ Embedding & FAISS index saving
- ✅ Evaluation metrics
- ✅ Final output: sample similar job pairs
# Project_submission16234
