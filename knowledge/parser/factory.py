"""
Parser Factory
"""

from knowledge.source import (
    KnowledgeSource,
    KnowledgeSourceType,
)

from knowledge.parser.base import BaseParser

from knowledge.parser.text import TextParser
from knowledge.parser.markdown import MarkdownParser
from knowledge.parser.pdf import PDFParser
from knowledge.parser.url import URLParser


class ParserFactory:
    """
    Parser 工厂。

    根据 KnowledgeSource
    创建对应 Parser。
    """

    @staticmethod
    def create(
        source: KnowledgeSource,
    ) -> BaseParser:
        """
        创建 Parser。

        Args:
            source:
                KnowledgeSource。

        Returns:
            BaseParser
        """

        match source.type:

            case KnowledgeSourceType.TEXT:
                return TextParser()

            case KnowledgeSourceType.MARKDOWN:
                return MarkdownParser()

            case KnowledgeSourceType.PDF:
                return PDFParser()

            case KnowledgeSourceType.URL:
                return URLParser()

        raise ValueError(
            f"Unsupported parser: {source.type}"
        )