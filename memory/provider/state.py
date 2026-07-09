from abc import ABC
from dataclasses import dataclass


@dataclass
class ProviderState(ABC):
    """
    LLM Provider 会话状态抽象基类。

    Provider State 保存的是模型供应商维护的状态，
    而不是业务会话状态。

    不同 Provider 可以扩展自己的状态对象：

    - OpenAI
    - Claude
    - Gemini
    - DeepSeek
    """

    provider: str

    model: str