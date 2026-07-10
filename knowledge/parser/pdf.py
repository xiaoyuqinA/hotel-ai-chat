"""
PDF Parser

职责：
- 解析 PDF 文件内容
- 提取文本
- 转换为 Document
"""

from uuid import uuid4
from io import BytesIO

from pypdf import PdfReader

from knowledge.document import Document

from knowledge.parser.base import BaseParser


class PDFParser(BaseParser):
    """
    PDF 内容解析器。
    """

    def parse(
        self,
        data: bytes,
        metadata: dict | None = None,
    ) -> Document:
        """
        将 PDF bytes 转换为 Document。

        Args:
            data:
                PDFLoader 返回的二进制内容。

            metadata:
                文档元数据。

        Returns:
            Document
        """

        if not isinstance(
            data,
            bytes,
        ):
            raise TypeError(
                "PDFParser only supports bytes data"
            )


        reader = PdfReader(
            BytesIO(data)
        )


        pages: list[str] = []


        for page in reader.pages:

            text = page.extract_text()

            if text:

                pages.append(
                    text
                )


        content = "\n\n".join(
            pages
        )


        return Document(
            id=str(uuid4()),

            content=content,

            metadata={
                **(metadata or {}),
                "type": "pdf",
                "pages": len(reader.pages),
            },
        )