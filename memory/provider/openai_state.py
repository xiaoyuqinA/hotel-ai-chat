from dataclasses import dataclass

from memory.provider.state import ProviderState


@dataclass
class OpenAIState(ProviderState):
    """
    OpenAI Provider 会话状态。

    Responses API：
        previous_response_id

    Conversations API：
        conversation_id

    Chat Completions API
    不需要保存任何 Provider State。
    """

    # Responses API
    response_id: str | None = None

    # Conversations API
    conversation_id: str | None = None