"""
Token Chunker

职责：
- 使用 LangChain TokenTextSplitter
- 按 Token 数量切分 Document
"""

from uuid import uuid4

from langchain_text_splitters import TokenTextSplitter

from knowledge.chunk import Chunk
from knowledge.document import Document
from knowledge.chunker.base import BaseChunker


class TokenChunker(BaseChunker):
    """
    基于 Token 的文本切块器。
    """

    def __init__(
        self,
        chunk_size: int = 512,
        chunk_overlap: int = 50,
        encoding_name: str = "cl100k_base",
    ) -> None:
        """
        Args:
            chunk_size:
                每个 Chunk 最大 Token 数。

            chunk_overlap:
                Chunk 重叠 Token 数。

            encoding_name:
                Tokenizer 编码名称。

                GPT-4 / GPT-4o 推荐：
                    cl100k_base

                GPT-5 推荐：
                    cl100k_base（目前仍兼容）
        """

        self._splitter = TokenTextSplitter(
            encoding_name=encoding_name,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split(
        self,
        document: Document,
    ) -> list[Chunk]:
        """
        将 Document 按 Token 切分为多个 Chunk。

        Args:
            document:
                原始文档。

        Returns:
            Chunk 列表。
        """

        texts = self._splitter.split_text(
            document.content
        )

        chunks: list[Chunk] = []

        for text in texts:

            chunks.append(
                Chunk(
                    id=str(uuid4()),
                    document_id=document.id,
                    content=text,
                    metadata=document.metadata.copy(),
                )
            )

        return chunks