"""
LLM Factory
"""

from llm.openai.factory import create_openai_client

from config.settings import LLM_PROVIDER


def create_llm_client():

    if LLM_PROVIDER == "openai":
        return create_openai_client()

    raise ValueError(
        f"Unsupported provider: {LLM_PROVIDER}"
    )