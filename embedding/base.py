"""
Base Embedding Client
"""

from abc import ABC, abstractmethod


class BaseEmbeddingClient(ABC):
    """
    所有 Embedding Client 的统一接口。
    """

    @abstractmethod
    def create_embedding(
        self,
        text: str,
    ) -> list[float]:
        """
        将文本转换为向量。

        Args:
            text:
                待向量化文本。

        Returns:
            Embedding Vector。
        """
        raise NotImplementedError