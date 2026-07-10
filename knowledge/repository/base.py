"""
Base Document Repository
"""

from abc import ABC, abstractmethod

from knowledge.document import Document


class BaseDocumentRepository(ABC):
    """
    Document Repository 抽象接口。

    负责管理 Document 元数据。

    不负责：
    - Chunk
    - Embedding
    - VectorStore
    """

    @abstractmethod
    def add(
        self,
        document: Document,
    ) -> None:
        """
        添加文档。
        """
        raise NotImplementedError

    @abstractmethod
    def update(
        self,
        document: Document,
    ) -> None:
        """
        更新文档。
        """
        raise NotImplementedError

    @abstractmethod
    def remove(
        self,
        document_id: str,
    ) -> None:
        """
        删除文档。
        """
        raise NotImplementedError

    @abstractmethod
    def get(
        self,
        document_id: str,
    ) -> Document | None:
        """
        根据 Document ID 获取文档。
        """
        raise NotImplementedError

    @abstractmethod
    def list(
        self,
    ) -> list[Document]:
        """
        获取所有文档。
        """
        raise NotImplementedError

    @abstractmethod
    def exists(
        self,
        document_id: str,
    ) -> bool:
        """
        判断文档是否存在。
        """
        raise NotImplementedError

    @abstractmethod
    def clear(
        self,
    ) -> None:
        """
        清空所有文档。
        """
        raise NotImplementedError