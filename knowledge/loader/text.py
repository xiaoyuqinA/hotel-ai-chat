"""
Text Loader

职责：
- 读取普通文本文件
- 返回原始文本内容
"""

from pathlib import Path

from knowledge.loader.base import BaseLoader


class TextLoader(BaseLoader):
    """
    Text 文件加载器。
    """

    def load(
        self,
        source: str,
    ) -> str:
        """
        加载文本文件。

        Args:
            source:
                文件路径。

        Returns:
            文件文本内容。
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


        return path.read_text(
            encoding="utf-8"
        )