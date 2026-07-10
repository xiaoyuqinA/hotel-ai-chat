"""
Knowledge Manager

职责：
- 协调整个知识入库流程
- Document -> Chunk
- Chunk -> Embedding
- Embedding -> VectorStore
"""

from knowledge.document import Document
from knowledge.chunk import Chunk

from embedding.base import BaseEmbeddingClient

from vectorstore.base import BaseVectorStore

from knowledge.chunker.base import BaseChunker


class KnowledgeManager:
    """
    Knowledge 管理器。

    负责将知识文档转换为
    可检索的向量数据。
    """

    def __init__(
        self,
        embedding: BaseEmbeddingClient,
        vector_store: BaseVectorStore,
        chunker: BaseChunker,
    ) -> None:

        self._embedding = embedding

        self._vector_store = vector_store

        self._chunker = chunker


    def add(
        self,
        document: Document,
    ) -> None:
        """
        添加知识文档。

        流程：

        Document
            ↓
        Chunk
            ↓
        Embedding
            ↓
        VectorStore
        """

        chunks = self._chunker.split(
            document
        )


        for chunk in chunks:

            vector = self._embedding.create_embedding(
                chunk.content
            )


            self._vector_store.add(
                document=chunk,
                vector=vector,
            )


    def update(
        self,
        document: Document,
    ) -> None:
        """
        更新知识文档。

        第一版：
        删除旧数据后重新添加。
        """

        self.remove(
            document.id
        )

        self.add(
            document
        )


    def remove(
        self,
        document_id: str,
    ) -> None:
        """
        删除知识。

        具体删除能力由 VectorStore 实现。
        """

        self._vector_store.delete(
            document_id
        )