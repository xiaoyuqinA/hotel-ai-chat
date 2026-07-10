"""
Base Parser

职责：
- 定义内容解析统一接口
- 将原始数据转换为 Document
"""

from abc import ABC, abstractmethod

from typing import Any

from knowledge.document import Document


class BaseParser(ABC):
    """
    Parser 抽象接口。

    负责：

    Raw Data
        ↓
    Document
    """

    @abstractmethod
    def parse(
        self,
        data: Any,
        metadata: dict | None = None,
    ) -> Document:
        """
        解析原始数据。

        Args:
            data:
                Loader 输出的数据。

                例如：
                - str
                - bytes
                - html

            metadata:
                文档额外信息。

        Returns:
            Document 对象。
        """

        raise NotImplementedError