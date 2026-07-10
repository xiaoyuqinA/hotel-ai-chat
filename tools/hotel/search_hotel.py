"""
Search Hotel Tool
"""

from typing import Any

from tools.base import BaseTool
from tools.schema import ToolProperty
from tools.schema import ToolSchema


class SearchHotelTool(BaseTool):
    """
    根据酒店名称搜索酒店。
    """

    def __init__(self) -> None:

        super().__init__(
            name="search_hotel",
            description="Search hotels by hotel name."
        )

    @property
    def schema(self) -> ToolSchema:

        return ToolSchema(
            properties=[
                ToolProperty(
                    name="hotel_name",
                    type="string",
                    description="Hotel name."
                )
            ]
        )

    def execute(
        self,
        arguments: dict[str, Any]
    ) -> Any:
        """
        Args:
            arguments:
                {
                    "hotel_name": "Hilton Shenzhen"
                }
        """

        hotel_name = arguments["hotel_name"]

        #
        # TODO:
        # 调用 HotelGraph
        # 或 OTA API
        #

        return [
            {
                "hotel_id": "hotel_001",
                "hotel_name": hotel_name,
                "city": "Shenzhen",
                "country": "China"
            }
        ]