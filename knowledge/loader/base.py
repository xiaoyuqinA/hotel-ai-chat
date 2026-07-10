"""
Base Loader

职责：
- 定义数据加载统一接口
- 从数据源读取原始内容
"""

from abc import ABC, abstractmethod

from typing import Any


class BaseLoader(ABC):
    """
    Loader 抽象接口。

    负责：
    - 读取数据源
    - 返回原始数据
    """

    @abstractmethod
    def load(
        self,
        source: Any,
    ) -> Any:
        """
        加载数据。

        Args:
            source:
                数据来源。

                例如：
                - 文件路径
                - URL
                - 文本内容

        Returns:
            原始数据。
        """

        raise NotImplementedError