"""
Recursive Chunker

职责：
- 使用 LangChain RecursiveCharacterTextSplitter
- 将 Document 拆分为 Chunk
"""

from uuid import uuid4

from langchain_text_splitters import RecursiveCharacterTextSplitter

from knowledge.chunk import Chunk
from knowledge.document import Document

from knowledge.chunker.base import BaseChunker


class RecursiveChunker(BaseChunker):
    """
    基于 LangChain 的递归文本切块器。
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
        separators: list[str] | None = None,
        keep_separator: bool = True,
    ) -> None:

        self._splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=separators,
            keep_separator=keep_separator,
        )

    def split(
        self,
        document: Document,
    ) -> list[Chunk]:
        """
        将 Document 拆分为多个 Chunk。
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