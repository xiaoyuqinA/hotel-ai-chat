from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(slots=True, frozen=True)
class ToolCall:
    """
    一次 Tool 调用请求。
    """

    call_id: str

    tool_name: str

    arguments: Mapping[str, Any] = field(default_factory=dict)