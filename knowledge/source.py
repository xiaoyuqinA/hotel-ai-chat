"""
Knowledge Source
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class KnowledgeSourceType(str, Enum):
    """
    支持的知识源类型。
    """

    TEXT = "text"

    MARKDOWN = "markdown"

    PDF = "pdf"

    URL = "url"


@dataclass(slots=True)
class KnowledgeSource:
    """
    Knowledge Source。

    描述一个知识来源。

    例如：

    - hotel.pdf
    - policy.md
    - https://example.com
    """

    #
    # 数据源地址
    #
    uri: str

    #
    # 数据源类型
    #
    type: KnowledgeSourceType

    #
    # 附加元数据
    #
    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    @property
    def name(
        self,
    ) -> str:
        """
        返回知识源名称。
        """

        return self.uri.rsplit(
            "/",
            1,
        )[-1]