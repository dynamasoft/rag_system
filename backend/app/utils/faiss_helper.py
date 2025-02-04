from typing import List, Tuple
import faiss
import numpy as np

class FAISSHelper:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)

    def add_documents(self, embeddings: np.ndarray) -> None:
        self.index.add(embeddings)

    def search(self, query_embedding: np.ndarray, k: int) -> Tuple[np.ndarray, np.ndarray]:
        distances, indices = self.index.search(query_embedding, k)
        return distances, indices

    def reset_index(self) -> None:
        self.index.reset()