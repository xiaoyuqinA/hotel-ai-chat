"""
URL Parser

职责：
- 解析 HTML 内容
- 提取网页正文
- 转换为 Document
"""

from uuid import uuid4

from bs4 import BeautifulSoup

from knowledge.document import Document
from knowledge.parser.base import BaseParser


class URLParser(BaseParser):
    """
    URL 内容解析器。
    """

    def parse(
        self,
        data: str,
        metadata: dict | None = None,
    ) -> Document:
        """
        将 HTML 转换为 Document。

        Args:
            data:
                URLLoader 返回的 HTML 内容。

            metadata:
                文档元数据。

        Returns:
            Document
        """

        if not isinstance(data, str):
            raise TypeError(
                "URLParser only supports str data."
            )

        soup = BeautifulSoup(
            data,
            "html.parser",
        )

        #
        # 移除无用标签
        #
        for tag in soup(
            [
                "script",
                "style",
                "noscript",
                "iframe",
                "svg",
            ]
        ):
            tag.decompose()

        #
        # 提取正文
        #
        content = soup.get_text(
            separator="\n",
            strip=True,
        )

        return Document(
            id=str(uuid4()),
            content=content,
            metadata={
                **(metadata or {}),
                "type": "url",
                "title": (
                    soup.title.string.strip()
                    if soup.title and soup.title.string
                    else ""
                )
            },
        )