"""
Knowledge Document

职责：
- 表示一个完整知识文档
- 作为 Chunk 生成的来源
- 保存文档级元数据
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass(
    slots=True,
)
class Document:
    """
    知识文档。

    一个 Document 可以被切分成多个 Chunk。
    """

    id: str

    content: str

    metadata: dict[str, Any] = field(
        default_factory=dict
    )