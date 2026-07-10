"""
Base Knowledge
"""

from abc import ABC, abstractmethod

from knowledge.document import Document


class BaseKnowledge(ABC):
    """
    Knowledge 抽象接口。

    负责：
    - 文档入库
    - 文档更新
    - 文档删除
    """

    @abstractmethod
    def add(
        self,
        document: Document,
    ) -> None:
        """
        添加一个文档到知识库。
        """
        raise NotImplementedError

    @abstractmethod
    def update(
        self,
        document: Document,
    ) -> None:
        """
        更新一个文档。
        """
        raise NotImplementedError

    @abstractmethod
    def remove(
        self,
        document_id: str,
    ) -> None:
        """
        删除一个文档。
        """
        raise NotImplementedError