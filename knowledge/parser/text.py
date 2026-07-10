"""
Text Parser

职责：
- 解析普通文本内容
- 转换为 Document
"""

from uuid import uuid4

from knowledge.document import Document

from knowledge.parser.base import BaseParser


class TextParser(BaseParser):
    """
    Text 内容解析器。
    """

    def parse(
        self,
        data: str,
        metadata: dict | None = None,
    ) -> Document:
        """
        将文本转换为 Document。

        Args:
            data:
                TextLoader 返回的文本内容。

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
                "TextParser only supports str data"
            )


        return Document(
            id=str(uuid4()),

            content=data,

            metadata=metadata or {},
        )