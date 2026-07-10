"""
Knowledge Factory
"""

from config.settings import KNOWLEDGE_PROVIDER

from knowledge.default import DefaultKnowledge


def create_knowledge():

    match KNOWLEDGE_PROVIDER:

        case "default":

            return DefaultKnowledge.build()

        case _:

            raise ValueError(
                f"Unsupported knowledge provider: {KNOWLEDGE_PROVIDER}"
            )