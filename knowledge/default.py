"""
Default Knowledge
"""

from knowledge.base import BaseKnowledge
from knowledge.document import Document

from knowledge.manager import KnowledgeManager

from knowledge.chunker.recursive import RecursiveChunker

from embedding.client import create_embedding_client
from vectorstore.client import create_vector_store


class DefaultKnowledge(BaseKnowledge):
    """
    默认 Knowledge 实现。
    """

    def __init__(
        self,
        manager: KnowledgeManager,
    ) -> None:

        self._manager = manager

    @classmethod
    def build(cls) -> "DefaultKnowledge":
        """
        构建默认 Knowledge。
        """

        embedding = create_embedding_client()

        vector_store = create_vector_store()

        chunker = RecursiveChunker()

        manager = KnowledgeManager(
            embedding=embedding,
            vector_store=vector_store,
            chunker=chunker,
        )

        return cls(
            manager=manager,
        )

    def add(
        self,
        document: Document,
    ) -> None:
        """
        添加文档。
        """

        self._manager.add(document)

    def update(
        self,
        document: Document,
    ) -> None:
        """
        更新文档。
        """

        self._manager.update(document)

    def remove(
        self,
        document_id: str,
    ) -> None:
        """
        删除文档。
        """

        self._manager.remove(document_id)