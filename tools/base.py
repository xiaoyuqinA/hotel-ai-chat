"""
Base Tool

职责：
- 定义所有 Tool 的统一接口
- 描述 Tool 的元信息
- 提供 Tool 执行入口

注意：
- 不依赖任何 LLM Provider
- 不包含 OpenAI Tool Schema
- 不包含 Anthropic Tool Schema
"""

from abc import ABC, abstractmethod
from typing import Any
from tools.schema import ToolSchema

class BaseTool(ABC):
    """
    所有 Tool 的抽象基类。
    """

    def __init__(
        self,
        name: str,
        description: str,
    ) -> None:
        self.name = name
        self.description = description

    @property
    @abstractmethod
    def schema(self) -> ToolSchema:
        """
        Tool 参数定义。

        返回 Provider 无关的参数描述。

        Returns:ToolSchema
            
        """
        raise NotImplementedError

    @abstractmethod
    def execute(
        self,
        **kwargs: Any,
    ) -> Any:
        """
        执行 Tool。

        Args:
            **kwargs:
                Tool 参数。

        Returns:
            Tool 执行结果。
        """
        raise NotImplementedError