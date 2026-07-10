"""
Base Retriever
"""

from abc import ABC, abstractmethod

from knowledge.document import Document


class BaseRetriever(ABC):
    """
    Retriever 抽象接口。
    """

    @abstractmethod
    def retrieve(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[Document]:
        """
        根据查询检索相关文档。
        """
        raise NotImplementedError