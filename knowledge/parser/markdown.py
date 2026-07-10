"""
Markdown Parser

职责：
- 解析 Markdown 内容
- 转换为 Document
"""

from uuid import uuid4

from knowledge.document import Document

from knowledge.parser.base import BaseParser


class MarkdownParser(BaseParser):
    """
    Markdown 内容解析器。
    """

    def parse(
        self,
        data: str,
        metadata: dict | None = None,
    ) -> Document:
        """
        将 Markdown 转换为 Document。

        Args:
            data:
                MarkdownLoader 返回的 Markdown 文本。

            metadata:
                文档元数据。

        Returns:
            Document
        """

        if not isinstance(
            data,
            str,
        ):
            raise TypeError(
                "MarkdownParser only supports str data"
            )


        return Document(
            id=str(uuid4()),

            content=data,

            metadata={
                **(metadata or {}),
                "type": "markdown",
            },
        )