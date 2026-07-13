"""
LLM Factory
"""

from llm.openai.factory import create_openai_client

from config.settings import LLM_PROVIDER


def create_llm_client():

    match LLM_PROVIDER:

        case "openai":

            return create_openai_client()

        case _:

            raise ValueError(
                f"Unsupported provider: {LLM_PROVIDER}"
            )