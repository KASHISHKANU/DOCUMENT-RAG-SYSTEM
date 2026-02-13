from transformers import logging
from sentence_transformers import SentenceTransformer

logging.set_verbosity_error()

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(texts):
    return model.encode(texts)
