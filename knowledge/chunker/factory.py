"""
Chunker Factory

职责：
- 创建 Chunker 实例
"""

from knowledge.chunker.base import BaseChunker

from knowledge.chunker.recursive import RecursiveChunker
from knowledge.chunker.token import TokenChunker


class ChunkerFactory:
    """
    Chunker 工厂。
    """

    @staticmethod
    def create(
        chunker_type: str = "recursive",
        **kwargs,
    ) -> BaseChunker:
        """
        创建 Chunker。

        Args:
            chunker_type:
                Chunker 类型。

                支持：
                    recursive
                    token

            **kwargs:
                Chunker 初始化参数。

        Returns:
            BaseChunker
        """

        chunker_type = chunker_type.lower()

        if chunker_type == "recursive":

            return RecursiveChunker(
                **kwargs,
            )

        if chunker_type == "token":

            return TokenChunker(
                **kwargs,
            )

        raise ValueError(
            f"Unsupported chunker: {chunker_type}"
        )