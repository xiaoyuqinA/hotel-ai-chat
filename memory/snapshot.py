from dataclasses import dataclass
from datetime import datetime
from types import MappingProxyType
from typing import Any, Mapping


@dataclass(frozen=True, slots=True)
class MessageSnapshot:
    """
    Message 的不可变快照。
    """

    role: str

    content: str

    created_at: datetime


@dataclass(frozen=True, slots=True)
class ConversationSnapshot:
    """
    ConversationState 的不可变快照（Immutable Snapshot）。

    Snapshot 用于提供给 LLM Adapter。

    Chat Completions、
    Responses API、
    Claude、
    Gemini

    都只能读取 Snapshot，
    不能修改 ConversationState。
    """

    # 应用层 Conversation ID
    application_conversation_id: str

    # 应用层 User ID
    user_id: str | None

    # 业务元数据（只读）
    metadata: Mapping[str, Any]

    # 会话历史（只读）
    messages: tuple[MessageSnapshot, ...]

    @property
    def latest_message(self) -> MessageSnapshot | None:
        if not self.messages:
            return None

        return self.messages[-1]

    @property
    def latest_user_message(self) -> MessageSnapshot | None:
        for message in reversed(self.messages):
            if message.role == "user":
                return message

        return None

    @property
    def latest_assistant_message(self) -> MessageSnapshot | None:
        for message in reversed(self.messages):
            if message.role == "assistant":
                return message

        return None

    def __iter__(self):
        return iter(self.messages)

    def __len__(self):
        return len(self.messages)