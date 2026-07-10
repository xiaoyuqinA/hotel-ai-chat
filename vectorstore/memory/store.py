"""
Memory Vector Store

职责：
- 内存保存 Chunk
- 保存 Chunk 对应 Vector
- 基于向量相似度搜索
"""

from knowledge.chunk import Chunk

from vectorstore.similarity import cosine_similarity

from vectorstore.base import BaseVectorStore


class MemoryVectorStore(BaseVectorStore):

    def __init__(self) -> None:

        self._chunks: list[Chunk] = []

        self._vectors: list[list[float]] = []


    def add(
        self,
        chunk: Chunk,
        vector: list[float],
    ) -> None:
        """
        添加 Chunk 和对应向量。
        """

        self._chunks.append(
            chunk
        )

        self._vectors.append(
            vector
        )


    def search(
        self,
        vector: list[float],
        top_k: int = 5,
    ) -> list[Chunk]:
        """
        根据向量搜索相似 Chunk。
        """

        scores: list[
            tuple[float, Chunk]
        ] = []


        for chunk, stored_vector in zip(
            self._chunks,
            self._vectors,
        ):

            score = cosine_similarity(
                vector,
                stored_vector,
            )

            scores.append(
                (
                    score,
                    chunk,
                )
            )


        scores.sort(
            key=lambda item: item[0],
            reverse=True,
        )


        return [
            chunk
            for _, chunk in scores[:top_k]
        ]