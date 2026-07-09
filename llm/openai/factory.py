"""
OpenAI Client Factory
"""

from config.settings import (

    LLM_API,

    OPENAI_API_KEY,

    OPENAI_BASE_URL,

    OPENAI_MODEL

)

from prompts.assistant_prompt import SYSTEM_PROMPT

from llm.openai.chat import OpenAIChatClient
from llm.openai.responses import OpenAIResponseClient


def create_openai_client():

    match LLM_API:

        case "chat":

            return OpenAIChatClient(

                api_key=OPENAI_API_KEY,

                base_url=OPENAI_BASE_URL,

                model=OPENAI_MODEL,

                system_prompt=SYSTEM_PROMPT

            )

        case "responses":

            return OpenAIResponseClient(

                api_key=OPENAI_API_KEY,

                base_url=OPENAI_BASE_URL,

                model=OPENAI_MODEL,

                instructions=SYSTEM_PROMPT

            )

        case _:

            raise ValueError(
                f"Unsupported OpenAI API: {LLM_API}"
            )