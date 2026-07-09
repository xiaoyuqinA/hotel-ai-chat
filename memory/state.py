from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class Message:
    """
    单条会话消息。

    Message 属于业务会话数据，
    ConversationManager 可以新增 Message，
    但不会修改已有 Message。
    """

    role: str

    content: str

    created_at: datetime = field(
        default_factory=datetime.now
    )


@dataclass(slots=True)
class ConversationState:
    """
    Application Conversation State

    保存当前应用层的业务会话状态。

    注意：
    不保存任何 Provider（OpenAI、Claude、Gemini）的状态。
    """

    # 应用层 Conversation ID
    application_conversation_id: str

    # 应用层 User ID
    user_id: str | None = None

    # 会话历史
    messages: list[Message] = field(
        default_factory=list
    )

    # 业务扩展数据
    metadata: dict[str, Any] = field(
        default_factory=dict
    )