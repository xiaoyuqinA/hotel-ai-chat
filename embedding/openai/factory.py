"""
OpenAI Embedding Factory
"""

from config.settings import (
    OPENAI_API_KEY,
    OPENAI_BASE_URL,
    OPENAI_EMBEDDING_MODEL,
)

from embedding.openai.embedding import OpenAIEmbeddingClient


def create_openai_embedding_client() -> OpenAIEmbeddingClient:
    """
    创建 OpenAI Embedding Client。
    """

    return OpenAIEmbeddingClient(
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_BASE_URL,
        model=OPENAI_EMBEDDING_MODEL,
    )