"""
Base Chunker

职责：
- 定义文本切块统一接口
- 将一个 Document 拆分为多个 Chunk
"""

from abc import ABC, abstractmethod

from knowledge.document import Document
from knowledge.chunk import Chunk


class BaseChunker(ABC):
    """
    Chunker 抽象接口。

    负责：

    Document
        ↓
    list[Chunk]
    """

    @abstractmethod
    def split(
        self,
        document: Document,
    ) -> list[Chunk]:
        """
        将 Document 拆分成多个 Chunk。

        Args:
            document:
                原始知识文档。

        Returns:
            Chunk 列表。
        """

        raise NotImplementedError