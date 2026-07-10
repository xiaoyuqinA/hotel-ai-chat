"""
Tool Executor

职责：
- 根据 Tool Name 查找 Tool
- 执行 Tool
- 捕获异常
- 返回 ToolResult
"""

from typing import Any

from tools.registry import ToolRegistry
from tools.result import ToolResult


class ToolExecutor:
    """
    Tool 执行器。
    """

    def __init__(
        self,
        registry: ToolRegistry,
    ) -> None:

        self._registry = registry

    def execute(
        self,
        tool_name: str,
        **kwargs: Any,
    ) -> ToolResult:
        """
        执行指定 Tool。

        Args:
            tool_name:
                Tool 名称。

            **kwargs:
                Tool 参数。

        Returns:
            ToolResult
        """

        try:

            tool = self._registry.get(tool_name)

        except ValueError as exc:

            return ToolResult.failure(
                tool_name=tool_name,
                message=str(exc),
            )

        try:

            result = tool.execute(**kwargs)

            return ToolResult.success(
                tool_name=tool_name,
                data=result,
            )

        except Exception as exc:

            return ToolResult.failure(
                tool_name=tool_name,
                message=str(exc),
            )