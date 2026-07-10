"""
Tool Loader

职责：
- 创建 ToolRegistry
- 注册所有内置 Tool
"""

from tools.registry import ToolRegistry
from tools.hotel.search_hotel import SearchHotelTool

# 内置 Tool
# from tools.calculator import CalculatorTool
# from tools.hotel.search_room import SearchRoomTool


def load_tools() -> ToolRegistry:
    """
    加载所有 Tool。

    Returns:
        ToolRegistry
    """

    registry = ToolRegistry()

    # 注册内置 Tool
    #
    # registry.register(
    #     CalculatorTool()
    # )
    #
    # registry.register(
    #     SearchRoomTool()
    # )
    registry.register(
        SearchHotelTool()
    )

    # registry.register(
    #     SearchRoomTool()
    # )

    # registry.register(
    #     GetRoomPriceTool()
    # )

    return registry