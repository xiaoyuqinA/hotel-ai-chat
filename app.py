from prompt_toolkit import prompt

from memory.state import ConversationState
from memory.manager import ConversationManager

from llm.client import create_llm_client


# 创建业务会话状态
state = ConversationState(
    application_conversation_id="conversation_001"
)

# 创建会话管理器
conversation = ConversationManager(state)

# 创建 LLM
llm = create_llm_client()


while True:

    user_input = prompt("User: ")

    if user_input == "exit":
        break

    # 1. 保存用户消息
    conversation.add_user_message(user_input)

    # 2. 创建当前会话快照
    snapshot = conversation.create_snapshot()

    # 3. 调用 LLM
    answer = llm.generate_response(snapshot)

    # 4. 保存 Assistant 回复
    conversation.add_assistant_message(answer)

    # 5. 输出结果
    print("Assistant:", answer)