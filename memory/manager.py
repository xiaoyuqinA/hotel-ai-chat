from memory.snapshot import ConversationSnapshot
from memory.state import ConversationState, Message


class ConversationManager:
    """
    ConversationState 的唯一管理入口。

    职责：
    1. 管理应用层 ConversationState。
    2. 修改会话消息。
    3. 创建 ConversationSnapshot。

    不负责：
    - Prompt
    - LLM
    - Chat Completions API
    - Responses API
    - Provider State
    """

    def __init__(
        self,
        state: ConversationState
    ) -> None:

        self._state = state

    def add_user_message(
        self,
        content: str
    ) -> None:
        """
        添加用户消息。
        """

        self._state.messages.append(
            Message(
                role="user",
                content=content
            )
        )

    def add_assistant_message(
        self,
        content: str
    ) -> None:
        """
        添加 Assistant 消息。
        """

        self._state.messages.append(
            Message(
                role="assistant",
                content=content
            )
        )

    def clear_messages(
        self
    ) -> None:
        """
        清空当前会话消息。
        """

        self._state.messages.clear()

    def create_snapshot(
        self
    ) -> ConversationSnapshot:
        """
        根据当前 ConversationState
        创建一份不可变快照（Snapshot）。

        Snapshot 用于传递给 LLM Adapter，
        Adapter 只能读取，不能修改。
        """

        return ConversationSnapshot(

            application_conversation_id=
                self._state.application_conversation_id,

            user_id=
                self._state.user_id,

            metadata=
                self._state.metadata.copy(),

            messages=
                tuple[Message, ...](self._state.messages)
        )