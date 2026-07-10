"""
Memory Vector Store Factory
"""

from vectorstore.memory.store import MemoryVectorStore


def create_memory_vector_store() -> MemoryVectorStore:

    return MemoryVectorStore()