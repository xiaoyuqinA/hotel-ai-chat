"""
Embedding Factory
"""

from embedding.openai.factory import create_openai_embedding_client

from config.settings import EMBEDDING_PROVIDER


def create_embedding_client():
    """
    创建 Embedding Client。
    """

    match EMBEDDING_PROVIDER:

        case "openai":

            return create_openai_embedding_client()

        case _:

            raise ValueError(
                f"Unsupported embedding provider: {EMBEDDING_PROVIDER}"
            )