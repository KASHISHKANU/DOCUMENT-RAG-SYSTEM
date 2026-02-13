from transformers import logging
from sentence_transformers import CrossEncoder

logging.set_verbosity_error()

reranker_model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

def rerank(query, chunks, top_n=2):

    pairs = [[query, chunk] for chunk in chunks]
    scores = reranker_model.predict(pairs)

    ranked = sorted(
        zip(chunks, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [chunk for chunk, _ in ranked[:top_n]]
