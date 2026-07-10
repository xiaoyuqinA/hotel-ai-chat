"""
Tool Schema

职责：
- 描述 Tool 的输入 Schema
- Provider 无关
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class ToolProperty:
    """
    Tool 输入字段。
    """

    name: str

    type: str

    description: str

    required: bool = True

    enum: list[str] | None = None

    default: Any | None = None


@dataclass(slots=True, frozen=True)
class ToolSchema:
    """
    Tool 输入 Schema。
    """

    properties: list[ToolProperty] = field(default_factory=list)