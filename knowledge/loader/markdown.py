"""
Markdown Loader

职责：
- 读取 Markdown 文件
- 返回原始 Markdown 内容
"""

from pathlib import Path

from knowledge.loader.base import BaseLoader


class MarkdownLoader(BaseLoader):
    """
    Markdown 文件加载器。
    """

    def load(
        self,
        source: str,
    ) -> str:
        """
        加载 Markdown 文件。

        Args:
            source:
                Markdown 文件路径。

        Returns:
            Markdown 原始文本。
        """

        path = Path(source)

        if not path.exists():

            raise FileNotFoundError(
                f"File not found: {source}"
            )


        if not path.is_file():

            raise ValueError(
                f"Source is not a file: {source}"
            )


        if path.suffix.lower() not in [
            ".md",
            ".markdown",
        ]:

            raise ValueError(
                f"Unsupported markdown file: {source}"
            )


        return path.read_text(
            encoding="utf-8"
        )