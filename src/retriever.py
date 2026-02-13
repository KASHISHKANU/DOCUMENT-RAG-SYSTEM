from embeddings import get_embeddings

def retrieve(query, vector_store, k=3):

    q_emb = get_embeddings([query])[0]
    return vector_store.search(q_emb, k)
