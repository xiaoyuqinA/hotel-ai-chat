"""
OpenAI Tool Mapper
"""

from typing import Any

from tools.base import BaseTool
from tools.schema import ToolSchema, ToolProperty


class OpenAIToolMapper:

    @staticmethod
    def to_tool(
        tool: BaseTool,
    ) -> dict[str, Any]:

        schema = tool.schema

        properties = {}
        required = []

        for prop in schema.properties:

            properties[prop.name] = {
                "type": prop.type,
                "description": prop.description,
            }

            if prop.enum:
                properties[prop.name]["enum"] = prop.enum

            if prop.required:
                required.append(prop.name)

        return {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": required,
                },
            },
        }

    @staticmethod
    def to_tools(
        tools: list[BaseTool],
    ) -> list[dict[str, Any]]:

        return [
            OpenAIToolMapper.to_tool(tool)
            for tool in tools
        ]