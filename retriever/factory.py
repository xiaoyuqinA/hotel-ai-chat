"""
Retriever Factory
"""

from embedding.client import create_embedding_client
from vectorstore.client import create_vector_store

from retriever.retriever import DefaultRetriever


def create_retriever() -> DefaultRetriever:

    embedding = create_embedding_client()

    vector_store = create_vector_store()

    return DefaultRetriever(
        embedding=embedding,
        vector_store=vector_store,
    )