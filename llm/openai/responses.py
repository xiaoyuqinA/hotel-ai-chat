"""
OpenAI Responses Client

职责：
- 初始化 OpenAI Client
- 调用 Responses API
- 管理 OpenAI Provider State
- 自动执行 Tool Calling
- 返回 Assistant 回复
"""

from openai import OpenAI

from memory.snapshot import ConversationSnapshot

from llm.base import BaseLLMClient

from llm.openai.state import OpenAIProviderState

from tools.manager import ToolManager

from llm.openai.tool_mapper import OpenAIToolMapper
from llm.openai.response_runner import OpenAIResponseRunner


class OpenAIResponseClient(BaseLLMClient):

    def __init__(
        self,
        api_key: str,
        base_url: str,
        model: str,
        instructions: str,
    ) -> None:

        super().__init__()

        self.model = model

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )

        self.instructions = instructions

        #
        # Provider State
        #
        self.provider_state = OpenAIProviderState()

        #
        # Tool Framework
        #
        self.tool_manager = ToolManager()

        self.runner = OpenAIResponseRunner(
            tool_manager=self.tool_manager,
            provider_state=self.provider_state,
        )

    def generate_response(
        self,
        snapshot: ConversationSnapshot,
    ) -> str:
        """
        调用 Responses API。
        """

        latest_user_message = snapshot.latest_user_message

        if latest_user_message is None:
            return ""

        tools = OpenAIToolMapper.to_tools(
            self.tool_manager.registry.list()
        )

        input = self._build_input(
            snapshot,
        )

        return self.runner.run(
            client=self.client,
            model=self.model,
            instructions=self.instructions,
            previous_response_id=self.provider_state.response_id,
            input=input,
            tools=tools,
        )

    def _build_input(
        self,
        snapshot: ConversationSnapshot,
    ) -> list[dict]:
        """
        构建 Responses API Input。
        """

        input: list[dict] = []

        #
        # Knowledge Context
        #
        if snapshot.context:

            knowledge = "\n\n".join(
                chunk.content
                for chunk in snapshot.context
            )

            input.append(
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "input_text",
                            "text": (
                                "Knowledge Base\n"
                                "==============\n\n"
                                f"{knowledge}"
                            ),
                        }
                    ],
                }
            )

        #
        # Conversation History
        #
        for message in snapshot.messages:

            input.append(
                {
                    "role": message.role,
                    "content": [
                        {
                            "type": "input_text",
                            "text": message.content,
                        }
                    ],
                }
            )

        return input