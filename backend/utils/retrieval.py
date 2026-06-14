import faiss
import pickle
import numpy as np

from utils.embeddings import model

INDEX_PATH = "vector_store/index.faiss"
CHUNK_PATH = "vector_store/chunks.pkl"

def save_index(
    embeddings,
    chunks
):

    embeddings = np.array(
        embeddings
    ).astype("float32")

    index = faiss.IndexFlatL2(
        embeddings.shape[1]
    )

    index.add(embeddings)

    faiss.write_index(
        index,
        INDEX_PATH
    )

    with open(
        CHUNK_PATH,
        "wb"
    ) as f:

        pickle.dump(
            chunks,
            f
        )

def retrieve(
    question,
    k=5
):

    index = faiss.read_index(
        INDEX_PATH
    )

    with open(
        CHUNK_PATH,
        "rb"
    ) as f:

        chunks = pickle.load(f)

    q = model.encode(
        [question]
    )

    q = np.array(
        q
    ).astype("float32")

    _, ids = index.search(
        q,
        k
    )

    return [
        chunks[i]
        for i in ids[0]
    ]