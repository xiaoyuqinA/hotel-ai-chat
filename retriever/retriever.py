"""
Default Retriever

职责：
- Query -> Embedding
- Embedding -> Vector Search
- 返回 Documents
"""

from embedding.base import BaseEmbeddingClient
from vectorstore.base import BaseVectorStore

from knowledge.document import Document


class DefaultRetriever:

    def __init__(
        self,
        embedding: BaseEmbeddingClient,
        vector_store: BaseVectorStore,
    ) -> None:

        self._embedding = embedding
        self._vector_store = vector_store

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[Document]:
        """
        检索知识。
        """

        vector = self._embedding.create_embedding(
            query
        )

        return self._vector_store.search(
            vector=vector,
            top_k=top_k,
        )