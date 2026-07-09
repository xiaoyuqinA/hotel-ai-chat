from memory.snapshot import ConversationSnapshot


class ConversationAdapter:
    """
    ConversationSnapshot 的适配器。

    负责将业务层 ConversationSnapshot
    转换为不同 LLM API 所需的数据格式。

    不负责：
    - 调用模型
    - 管理 Provider State
    - Prompt
    """

    @staticmethod
    def to_chat_messages(
        snapshot: ConversationSnapshot,
        system_prompt: str
    ) -> list[dict]:
        """
        转换为 Chat Completions API 的 messages。
        """

        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        for message in snapshot:

            messages.append(
                {
                    "role": message.role,
                    "content": message.content
                }
            )

        return messages

    @staticmethod
    def to_response_input(
        snapshot: ConversationSnapshot
    ) -> str:
        """
        转换为 Responses API 的 input。

        Responses API 使用 previous_response_id
        管理上下文，因此这里只需要传递最新的
        用户输入。
        """

        latest_user_message = snapshot.latest_user_message

        if latest_user_message is None:
            return ""

        return latest_user_message.content