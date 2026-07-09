"""
OpenAI Responses Client

职责：
- 初始化 OpenAI Client
- 调用 Responses API
- 管理 OpenAI Provider State
- 返回 Assistant 回复
"""

from openai import OpenAI

from memory.snapshot import ConversationSnapshot

from llm.base import BaseLLMClient
from llm.openai.state import OpenAIProviderState


class OpenAIResponseClient(BaseLLMClient):

    def __init__(
        self,
        api_key: str,
        base_url: str,
        model: str,
        instructions: str
    ) -> None:

        super().__init__(model)

        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )

        self.instructions = instructions

        # OpenAI Provider State
        self.provider_state = OpenAIProviderState()

    def generate_response(
        self,
        snapshot: ConversationSnapshot
    ) -> str:
        """
        调用 OpenAI Responses API。

        Args:
            snapshot:
                当前业务会话快照。

        Returns:
            Assistant 回复文本。
        """

        latest_user_message = snapshot.latest_user_message

        if latest_user_message is None:
            return ""

        response = self.client.responses.create(

            model=self.model,

            instructions=self.instructions,

            previous_response_id=self.provider_state.response_id,

            input=latest_user_message.content

        )

        # 更新 OpenAI Provider State
        self.provider_state.response_id = response.id

        return response.output_text