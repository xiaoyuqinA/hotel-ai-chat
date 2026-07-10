import os
from dotenv import load_dotenv


load_dotenv()


OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)

OPENAI_BASE_URL = os.getenv(
    "OPENAI_BASE_URL"
)

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL"
)


OPENAI_API_TYPE = os.getenv(
    "OPENAI_API_TYPE"
)

LLM_PROVIDER =  os.getenv(
    "LLM_PROVIDER"
)

LLM_API  = os.getenv(
    "LLM_API"
)

EMBEDDING_PROVIDER = os.getenv(
    "EMBEDDING_PROVIDER"
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL"
)

VECTOR_STORE_PROVIDER = os.getenv(
    "VECTOR_STORE_PROVIDER"
)