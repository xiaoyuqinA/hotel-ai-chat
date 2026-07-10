"""
Knowledge Admin Service

职责：
- 对外提供知识管理入口
- 协调整个知识入库流程
"""

from knowledge.detector import KnowledgeSourceDetector

from knowledge.loader.factory import LoaderFactory
from knowledge.parser.factory import ParserFactory

from knowledge.document import Document

from knowledge.repository.base import BaseDocumentRepository

from knowledge.manager import KnowledgeManager


class KnowledgeAdminService:
    """
    Knowledge Admin Service。

    对外唯一入口。
    """

    def __init__(
        self,
        repository: BaseDocumentRepository,
        manager: KnowledgeManager,
    ) -> None:

        self._repository = repository

        self._manager = manager

    def add(
        self,
        uri: str,
    ) -> Document:
        """
        添加知识。
        """

        #
        # Detect Source
        #
        source = KnowledgeSourceDetector.detect(
            uri,
        )

        #
        # Loader
        #
        loader = LoaderFactory.create(
            source,
        )

        raw_content = loader.load(
            source,
        )

        #
        # Parser
        #
        parser = ParserFactory.create(
            source,
        )

        document = parser.parse(
            source,
            raw_content,
        )

        #
        # Save Document Metadata
        #
        self._repository.add(
            document,
        )

        #
        # Build Vector Index
        #
        self._manager.add(
            document,
        )

        return document

    def update(
        self,
        document: Document,
    ) -> None:
        """
        更新知识。
        """

        self._repository.update(
            document,
        )

        self._manager.update(
            document,
        )

    def remove(
        self,
        document_id: str,
    ) -> None:
        """
        删除知识。
        """

        self._repository.remove(
            document_id,
        )

        self._manager.remove(
            document_id,
        )

    def get(
        self,
        document_id: str,
    ) -> Document | None:
        """
        获取知识。
        """

        return self._repository.get(
            document_id,
        )

    def list(
        self,
    ) -> list[Document]:
        """
        获取所有知识。
        """

        return self._repository.list()