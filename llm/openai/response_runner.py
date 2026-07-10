"""
OpenAI Responses Runner

职责：
- 调用 Responses API
- 自动执行 Tool Calling
- 更新 Provider State
- 返回最终 Assistant 回复
"""

import json

from openai import OpenAI

from llm.openai.state import OpenAIProviderState

from tools.call import ToolCall
from tools.manager import ToolManager


class OpenAIResponseRunner:

    def __init__(
        self,
        tool_manager: ToolManager,
        provider_state: OpenAIProviderState,
    ) -> None:

        self._tool_manager = tool_manager
        self._provider_state = provider_state

    def run(
        self,
        client: OpenAI,
        model: str,
        instructions: str,
        previous_response_id: str | None,
        input: list[dict],
        tools: list[dict],
    ) -> str:
        """
        自动执行 Responses Tool Calling。
        """

        input_data = input

        while True:

            response = client.responses.create(
                model=model,
                instructions=instructions,
                previous_response_id=previous_response_id,
                input=input_data,
                tools=tools,
            )

            #
            # 更新 Provider State
            #
            self._provider_state.response_id = response.id

            #
            # 下一轮使用
            #
            previous_response_id = response.id

            #
            # 收集 function_call
            #
            function_calls = [
                item
                for item in response.output
                if item.type == "function_call"
            ]

            #
            # 没有 Tool Call
            #
            if not function_calls:

                return response.output_text

            #
            # 构造下一轮 input
            #
            input_data = []

            for function in function_calls:

                call = ToolCall(
                    tool_name=function.name,
                    arguments=json.loads(
                        function.arguments
                    ),
                )

                result = self._tool_manager.executor.execute(
                    call
                )

                input_data.append(
                    {
                        "type": "function_call_output",
                        "call_id": function.call_id,
                        "output": json.dumps(
                            result.data,
                            ensure_ascii=False,
                        ),
                    }
                )