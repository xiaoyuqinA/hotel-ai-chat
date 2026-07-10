"""
Knowledge Chunk

职责：
- 表示 Document 切分后的知识片段
- 作为 Embedding 输入
- 作为 VectorStore 存储和检索单位
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass(
    slots=True,
)
class Chunk:
    """
    知识切片。

    一个 Document 可以包含多个 Chunk。
    """

    id: str

    document_id: str

    content: str

    metadata: dict[str, Any] = field(
        default_factory=dict
    )