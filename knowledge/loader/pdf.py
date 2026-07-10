"""
PDF Loader

职责：
- 读取 PDF 文件
- 提供 PDF 原始数据
"""

from pathlib import Path

from knowledge.loader.base import BaseLoader


class PDFLoader(BaseLoader):
    """
    PDF 文件加载器。
    """

    def load(
        self,
        source: str,
    ) -> bytes:
        """
        加载 PDF 文件。

        Args:
            source:
                PDF 文件路径。

        Returns:
            PDF 二进制内容。
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


        if path.suffix.lower() != ".pdf":

            raise ValueError(
                f"Unsupported pdf file: {source}"
            )


        return path.read_bytes()