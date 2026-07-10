"""
Tool Registry

职责：
- 注册 Tool
- 查询 Tool
- 返回所有 Tool
"""

from tools.base import BaseTool


class ToolRegistry:
    """
    Tool 注册中心。
    """

    def __init__(self) -> None:

        self._tools: dict[str, BaseTool] = {}

    def register(
        self,
        tool: BaseTool,
    ) -> None:
        """
        注册 Tool。

        Args:
            tool:
                Tool 实例。
        """

        if tool.name in self._tools:

            raise ValueError(
                f"Tool '{tool.name}' already exists."
            )

        self._tools[tool.name] = tool

    def unregister(
        self,
        name: str,
    ) -> None:
        """
        注销 Tool。
        """

        self._tools.pop(
            name,
            None,
        )

    def get(
        self,
        name: str,
    ) -> BaseTool:
        """
        根据名称获取 Tool。
        """

        try:

            return self._tools[name]

        except KeyError as exc:

            raise ValueError(
                f"Tool '{name}' not found."
            ) from exc

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Tool 是否存在。
        """

        return name in self._tools

    def list(
        self,
    ) -> list[BaseTool]:
        """
        返回所有已注册 Tool。
        """

        return list(
            self._tools.values()
        )

    def clear(
        self,
    ) -> None:
        """
        清空所有 Tool。
        """

        self._tools.clear()