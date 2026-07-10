"""
URL Loader

职责：
- 加载远程 URL 内容
- 返回原始 HTML 内容
"""

import requests

from knowledge.loader.base import BaseLoader


class URLLoader(BaseLoader):
    """
    URL 数据加载器。
    """

    def load(
        self,
        source: str,
    ) -> str:
        """
        加载 URL 内容。

        Args:
            source:
                URL 地址。

        Returns:
            HTML 文本。
        """

        if not source.startswith(
            (
                "http://",
                "https://",
            )
        ):

            raise ValueError(
                f"Invalid URL: {source}"
            )


        response = requests.get(
            source,
            timeout=10,
        )


        response.raise_for_status()


        return response.text