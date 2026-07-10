from hotel-ai-chat.knowledge.chunk import Chunk


from dataclasses import dataclass, replace
from datetime import datetime
from typing import Any, Mapping

from knowledge.chunk import Chunk


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

    Snapshot 用于提供给：

    - Chat Completions
    - Responses API
    - Claude
    - Gemini
    """

    #
    # 应用层
    #
    application_conversation_id: str

    user_id: str | None

    #
    # 业务元数据
    #
    metadata: Mapping[str, Any]

    #
    # 会话历史
    #
    messages: tuple[MessageSnapshot, ...]

    #
    # RAG 检索结果
    #
    context: tuple[Chunk, ...] = ()

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

    def with_context(
        self,
        chunks: list[Chunk],
    ) -> "ConversationSnapshot":
        """
        返回携带 Knowledge Context 的新 Snapshot。

        原 Snapshot 保持不可变。
        """

        return replace(
            self,
            context=tuple[Chunk, ...](chunks),
        )

    def __iter__(self):

        return iter(self.messages)

    def __len__(self):

        return len(self.messages)