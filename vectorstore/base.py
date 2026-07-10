"""
Base Vector Store
"""

from abc import ABC, abstractmethod

from knowledge.chunk import Chunk


class BaseVectorStore(ABC):
    """
    所有 Vector Store 的统一接口。

    VectorStore 存储和检索的最小单位：
    Chunk
    """

    @abstractmethod
    def add(
        self,
        chunk: Chunk,
        vector: list[float],
    ) -> None:
        """
        添加一个知识 Chunk。

        Args:
            chunk:
                文档切分后的知识片段。

            vector:
                Chunk 对应的 Embedding 向量。
        """

        raise NotImplementedError


    @abstractmethod
    def search(
        self,
        vector: list[float],
        top_k: int = 5,
    ) -> list[Chunk]:
        """
        根据向量检索最相似的 Chunk。

        Args:
            vector:
                查询文本的 Embedding 向量。

            top_k:
                返回数量。

        Returns:
            最相似的 Chunk 列表。
        """

        raise NotImplementedError