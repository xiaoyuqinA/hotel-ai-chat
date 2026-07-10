"""
Tool Result

职责：
- 描述一次 Tool 执行结果
- Provider 无关
"""

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True, frozen=True)
class ToolResult:
    """
    一次 Tool 执行结果。
    """

    # Tool 名称
    tool_name: str

    # 是否执行成功
    success: bool

    # Tool 返回的数据
    data: Any | None = None

    # 错误信息
    error: str | None = None