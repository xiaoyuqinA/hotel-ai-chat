"""
OpenAI Embedding Client

职责：
- 初始化 OpenAI Client
- 调用 OpenAI Embeddings API
- 返回 Embedding Vector
"""

from openai import OpenAI

from embedding.base import BaseEmbeddingClient


class OpenAIEmbeddingClient(BaseEmbeddingClient):

    def __init__(
        self,
        api_key: str,
        base_url: str,
        model: str,
    ) -> None:

        super().__init__()

        self.model = model

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )

    def create_embedding(
        self,
        text: str,
    ) -> list[float]:
        """
        创建文本 Embedding。

        Args:
            text:
                待向量化文本。

        Returns:
            Embedding Vector。
        """

        response = self.client.embeddings.create(
            model=self.model,
            input=text,
        )

        return response.data[0].embedding