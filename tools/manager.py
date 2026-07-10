"""
Tool Manager

职责：
- 管理整个 Tool Framework
- 创建 ToolRegistry
- 创建 ToolExecutor
- 提供统一访问入口
"""

from tools.loader import load_tools
from tools.registry import ToolRegistry
from tools.executor import ToolExecutor


class ToolManager:

    def __init__(self) -> None:

        self._registry: ToolRegistry = load_tools()

        self._executor = ToolExecutor(
            self._registry
        )

    @property
    def registry(
        self,
    ) -> ToolRegistry:

        return self._registry

    @property
    def executor(
        self,
    ) -> ToolExecutor:

        return self._executor