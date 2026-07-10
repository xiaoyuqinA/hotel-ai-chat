"""
Memory Document Repository
"""

from knowledge.document import Document

from knowledge.repository.base import BaseDocumentRepository


class MemoryDocumentRepository(BaseDocumentRepository):
    """
    基于内存的 Document Repository。

    第一版使用内存保存所有 Document 元数据。
    """

    def __init__(self) -> None:

        self._documents: dict[str, Document] = {}

    def add(
        self,
        document: Document,
    ) -> None:
        """
        添加文档。
        """

        self._documents[document.id] = document

    def update(
        self,
        document: Document,
    ) -> None:
        """
        更新文档。
        """

        self._documents[document.id] = document

    def remove(
        self,
        document_id: str,
    ) -> None:
        """
        删除文档。
        """

        self._documents.pop(
            document_id,
            None,
        )

    def get(
        self,
        document_id: str,
    ) -> Document | None:
        """
        根据 Document ID 获取文档。
        """

        return self._documents.get(
            document_id,
        )

    def list(
        self,
    ) -> list[Document]:
        """
        获取所有文档。
        """

        return list(
            self._documents.values()
        )

    def exists(
        self,
        document_id: str,
    ) -> bool:
        """
        判断文档是否存在。
        """

        return document_id in self._documents

    def clear(
        self,
    ) -> None:
        """
        清空所有文档。
        """

        self._documents.clear()