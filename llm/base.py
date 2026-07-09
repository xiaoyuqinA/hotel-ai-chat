"""
Base LLM Client
"""

from abc import ABC, abstractmethod

from conversation.snapshot import ConversationSnapshot


class BaseLLMClient(ABC):
    """
    所有 LLM Client 的统一接口。
    """

    @abstractmethod
    def generate_response(
        self,
        snapshot: ConversationSnapshot
    ) -> str:
        """
        根据当前 ConversationSnapshot
        生成 Assistant 回复。
        """
        raise NotImplementedError