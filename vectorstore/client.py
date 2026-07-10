"""
Vector Store Factory
"""

from vectorstore.memory.factory import create_memory_vector_store

from config.settings import VECTOR_STORE_PROVIDER


def create_vector_store():

    match VECTOR_STORE_PROVIDER:

        case "memory":

            return create_memory_vector_store()

        case _:

            raise ValueError(
                f"Unsupported vector store: {VECTOR_STORE_PROVIDER}"
            )