"""
Knowledge Source Detector
"""

from pathlib import Path

from knowledge.source import (
    KnowledgeSource,
    KnowledgeSourceType,
)


class KnowledgeSourceDetector:
    """
    Knowledge Source Detector。

    根据输入的数据源，
    识别 KnowledgeSource。
    """

    @staticmethod
    def detect(
        uri: str,
    ) -> KnowledgeSource:
        """
        识别知识源。

        Args:
            uri:
                数据源。

        Returns:
            KnowledgeSource
        """

        #
        # URL
        #
        if uri.startswith(
            (
                "http://",
                "https://",
            )
        ):
            return KnowledgeSource(
                uri=uri,
                type=KnowledgeSourceType.URL,
            )

        suffix = Path(
            uri
        ).suffix.lower()

        #
        # Text
        #
        if suffix == ".txt":

            return KnowledgeSource(
                uri=uri,
                type=KnowledgeSourceType.TEXT,
            )

        #
        # Markdown
        #
        if suffix in (
            ".md",
            ".markdown",
        ):

            return KnowledgeSource(
                uri=uri,
                type=KnowledgeSourceType.MARKDOWN,
            )

        #
        # PDF
        #
        if suffix == ".pdf":

            return KnowledgeSource(
                uri=uri,
                type=KnowledgeSourceType.PDF,
            )

        raise ValueError(
            f"Unsupported knowledge source: {uri}"
        )