"""
OpenAI Provider State

职责：
- 保存 OpenAI Provider 的会话状态
- 不属于业务 Conversation
- 不保存业务 Message
"""

from dataclasses import dataclass


@dataclass(slots=True)
class OpenAIProviderState:
    """
    OpenAI Provider 会话状态。

    仅保存 OpenAI SDK 所需状态，例如：

    - Responses API 的 previous_response_id
    """

    response_id: str | None = None

    def reset(self) -> None:
        """
        重置 Provider State。

        开启新的 OpenAI 会话时调用。
        """

        self.response_id = None