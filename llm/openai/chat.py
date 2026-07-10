"""
OpenAI Chat Completions Client

职责：
- 初始化 OpenAI Client
- 将 ConversationSnapshot 转换为 Chat Messages
- 构建 OpenAI Tool Schema
- 调用 OpenAIToolRunner
"""

from openai import OpenAI

from memory.snapshot import ConversationSnapshot

from llm.base import BaseLLMClient

from tools.manager import ToolManager

from llm.openai.tool_mapper import OpenAIToolMapper
from llm.openai.tool_runner import OpenAIToolRunner


class OpenAIChatClient(BaseLLMClient):

    def __init__(
        self,
        api_key: str,
        base_url: str,
        model: str,
        system_prompt: str,
    ) -> None:

        super().__init__()

        self.model = model

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )

        self.system_prompt = system_prompt

        #
        # Tool Framework
        #
        self.tool_manager = ToolManager()

        self.runner = OpenAIToolRunner(
            tool_manager=self.tool_manager,
        )

    def generate_response(
        self,
        snapshot: ConversationSnapshot,
    ) -> str:
        """
        调用 Chat Completions。
        """

        messages = self._build_messages(snapshot)

        tools = OpenAIToolMapper.to_tools(
            self.tool_manager.registry.list()
        )

        return self.runner.run(
            client=self.client,
            model=self.model,
            messages=messages,
            tools=tools,
        )

    def _build_messages(
        self,
        snapshot: ConversationSnapshot,
    ) -> list[dict]:
        """
        将 ConversationSnapshot
        转换为 Chat Messages。
        """

        messages: list[dict] = [
            {
                "role": "system",
                "content": self.system_prompt,
            }
        ]

        #
        # Knowledge Context
        #
        if snapshot.context:

            knowledge = "\n\n".join(
                chunk.content
                for chunk in snapshot.context
            )

            messages.append(
                {
                    "role": "system",
                    "content": (
                        "Knowledge Base\n"
                        "==============\n\n"
                        f"{knowledge}"
                    ),
                }
            )

        #
        # Conversation History
        #
        for message in snapshot.messages:

            messages.append(
                {
                    "role": message.role,
                    "content": message.content,
                }
            )

        return messages