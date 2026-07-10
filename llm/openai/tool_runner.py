"""
OpenAI Tool Runner

职责：
- 调用 OpenAI Chat API
- 自动执行 Tool Calls
- 回传 Tool Result
- 返回最终 Assistant 回复
"""

import json

from openai import OpenAI

from tools.call import ToolCall
from tools.manager import ToolManager


class OpenAIToolRunner:

    def __init__(
        self,
        tool_manager: ToolManager,
    ) -> None:

        self._tool_manager = tool_manager

    def run(
        self,
        client: OpenAI,
        model: str,
        messages: list[dict],
        tools: list[dict],
    ) -> str:
        """
        自动执行 Tool Calling。

        Returns:
            最终 Assistant 回复。
        """

        while True:

            response = client.chat.completions.create(
                model=model,
                messages=messages,
                tools=tools,
            )

            message = response.choices[0].message

            #
            # 没有 Tool Call，结束
            #
            if not message.tool_calls:

                return message.content or ""

            #
            # 保存 assistant(tool_calls)
            #
            messages.append(
                message.model_dump(
                    exclude_none=True
                )
            )

            #
            # 执行所有 Tool
            #
            for tool_call in message.tool_calls:

                call = ToolCall(
                    tool_name=tool_call.function.name,
                    arguments=json.loads(
                        tool_call.function.arguments
                    ),
                )

                result = self._tool_manager.executor.execute(
                    call
                )

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": json.dumps(
                            result.data,
                            ensure_ascii=False,
                        ),
                    }
                )