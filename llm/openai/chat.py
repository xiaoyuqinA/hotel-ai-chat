"""
OpenAI Chat Completions Client

职责：
- 初始化 OpenAI Client
- 将 ConversationSnapshot 转换为 Chat Messages
- 调用 Chat Completions API
- 返回 Assistant 回复
"""

from openai import OpenAI

from memory.snapshot import ConversationSnapshot

from llm.base import BaseLLMClient


class OpenAIChatClient(BaseLLMClient):

    def __init__(
        self,
        api_key: str,
        base_url: str,
        model: str,
        system_prompt: str
    ) -> None:

        super().__init__(model)

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

        self.system_prompt = system_prompt

    def generate_response(
        self,
        snapshot: ConversationSnapshot
    ) -> str:
        """
        调用 OpenAI Chat Completions API。

        Args:
            snapshot:
                当前业务会话快照。

        Returns:
            Assistant 回复文本。
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self._build_messages(snapshot)
        )

        return response.choices[0].message.content or ""

    def _build_messages(
        self,
        snapshot: ConversationSnapshot
    ) -> list[dict]:
        """
        将 ConversationSnapshot 转换为
        OpenAI Chat Completions 所需的 messages。
        """

        messages = [
            {
                "role": "system",
                "content": self.system_prompt
            }
        ]

        for message in snapshot.messages:

            messages.append(
                {
                    "role": message.role,
                    "content": message.content
                }
            )

        return messages