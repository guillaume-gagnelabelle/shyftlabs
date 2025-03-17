from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

DOCUMENTS = []
TFIDF_VECTORIZER = TfidfVectorizer()
TFIDF_MATRIX = None

EMBEDDING_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
FAISS_INDEX = None
EMBEDDINGS = []

def index_document(text_chunk: str):
    global TFIDF_MATRIX, FAISS_INDEX, EMBEDDINGS

    DOCUMENTS.append(text_chunk)

    # Keyword search
    TFIDF_MATRIX = TFIDF_VECTORIZER.fit_transform(DOCUMENTS)

    # Semantic search
    embedding = EMBEDDING_MODEL.encode(text_chunk)
    EMBEDDINGS.append(embedding)

    dim = embedding.shape[0]
    FAISS_INDEX = faiss.IndexFlatL2(dim)
    FAISS_INDEX.add(np.array(EMBEDDINGS))

def retrieve_relevant_chunks(query: str, top_k=4):
    results = []

    #TF-IDF keyword search
    tfidf_query = TFIDF_VECTORIZER.transform([query])
    scores = (TFIDF_MATRIX @ tfidf_query.T).toarray().ravel()
    keyword_matches = sorted(zip(scores, DOCUMENTS), reverse=True)[:top_k]
    results.extend([doc for _, doc in keyword_matches])


    # Semantic search
    embedding = EMBEDDING_MODEL.encode([query])
    D, I = FAISS_INDEX.search(np.array(embedding), top_k)
    results.extend([DOCUMENTS[i] for i in I[0]])

    return list(set(results)) # list(set(...)) to remove duplicates

