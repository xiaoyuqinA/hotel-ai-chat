"""
Loader Factory

职责：
- 根据数据源自动创建 Loader
"""

from pathlib import Path

from knowledge.loader.base import BaseLoader

from knowledge.loader.text import TextLoader
from knowledge.loader.markdown import MarkdownLoader
from knowledge.loader.pdf import PDFLoader
from knowledge.loader.url import URLLoader


class LoaderFactory:
    """
    Loader 工厂。
    """

    @staticmethod
    def create(
        source: str,
    ) -> BaseLoader:
        """
        根据数据源创建 Loader。

        Args:
            source:
                数据源。

                支持：
                - 本地 txt
                - 本地 md
                - 本地 pdf
                - URL

        Returns:
            BaseLoader
        """

        #
        # URL
        #
        if source.startswith(("http://", "https://")):
            return URLLoader()

        suffix = Path(source).suffix.lower()

        #
        # Text
        #
        if suffix == ".txt":
            return TextLoader()

        #
        # Markdown
        #
        if suffix in (".md", ".markdown"):
            return MarkdownLoader()

        #
        # PDF
        #
        if suffix == ".pdf":
            return PDFLoader()

        raise ValueError(
            f"Unsupported knowledge source: {source}"
        )