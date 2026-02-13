import os
import logging

import os

# ---- Silence all ML logs ----
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("sentence_transformers").setLevel(logging.ERROR)

from reranker import rerank
from pdf_loader import load_pdfs
from chunker import chunk_text
from embeddings import get_embeddings
from vector_store import VectorStore
from retriever import retrieve
from rag_pipeline import generate_answer

# Load documents
docs = load_pdfs()

# Chunking
all_chunks = []
for doc in docs:
    all_chunks.extend(chunk_text(doc["text"]))

# Embeddings
embeddings = get_embeddings(all_chunks)

# Vector store
vs = VectorStore(len(embeddings[0]))
vs.add(embeddings, all_chunks)

print("RAG Assistant Ready ✅")

while True:

    question = input("\nAsk Question: ")
    
    if question.lower() in ["exit", "quit"]:
        print("Exiting RAG Assistant 👋")
        break

    retrieved = retrieve(question, vs)

    # rerank retrieved chunks
    retrieved = rerank(question, retrieved)

    if not retrieved:
        print("No relevant policy found.")
        continue

    answer = generate_answer(question, retrieved)

    print("\nAnswer:\n", answer)
