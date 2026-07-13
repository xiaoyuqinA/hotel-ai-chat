# hotel-ai-chat 运行说明

## 项目目标

`hotel-ai-chat` 是一个酒店运营 AI Chat 后端原型。用户输入酒店经营问题，例如：

```text
帮我分析一下酒店最近入住率下降的原因
```

后端会调用 LLM API，结合 Prompt、多轮对话上下文，生成分析结果。

当前第一阶段重点是：

- Python 调用 OpenAI / OpenAI-compatible API
- Prompt 控制 AI 行为
- 多轮聊天
- Conversation State 上下文管理
- Tool / Function Calling 框架
- 简单知识库 / RAG 目录结构准备

## 目录结构

```text
hotel-ai-chat/
├── app.py                 # 主入口
├── config/                # 配置
├── prompts/               # Prompt 定义
├── memory/                # 多轮对话状态管理
├── llm/                   # LLM 调用封装
├── retriever/             # RAG 检索入口
├── vectorstore/           # 向量存储抽象
├── embedding/             # Embedding 调用封装
├── knowledge/             # 知识库文档处理
├── tools/                 # Tool / Function Calling
├── models/                # Schema 定义
├── hotel_documents/       # 知识库原始文档
├── requirements.txt
├── package.json
├── .env
└── README.md
```

## 环境要求

推荐使用 Python 3.13+。

项目使用本地虚拟环境：

```text
.venv
```

## 安装依赖

进入项目目录：

```bash
cd /Users/xiaoyuqin/plan/hotel-ai-chat
```

激活虚拟环境：

```bash
source .venv/bin/activate
```

安装 Python 依赖：

```bash
pip install -r requirements.txt
```

当前项目还包含 npm 依赖文件，但 Python 运行主要依赖 `.venv` 和 `requirements.txt`。

## 环境变量配置

运行前需要配置 `.env`。

示例：

```env
OPENAI_API_KEY=your_api_key
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4o-mini
OPENAI_EMBEDDING_MODEL=text-embedding-3-small

LLM_PROVIDER=openai
LLM_API=chat

EMBEDDING_PROVIDER=openai
EMBEDDING_MODEL=text-embedding-3-small

VECTOR_STORE_PROVIDER=memory
```

注意：

- `OPENAI_BASE_URL` 应该配置到 provider root，例如 `/v1`。
- 不要写成 `/v1/chat/completions`，否则 Responses API 会拼出错误路径。
- `OPENAI_EMBEDDING_MODEL` 必须使用当前接口实际支持的 Embedding 模型。
- 如果 Embedding 模型不可用，RAG Retrieval 会失败。

## 运行项目

激活虚拟环境：

```bash
source .venv/bin/activate
```

启动聊天程序：

```bash
python ./app.py
```

运行后输入问题，例如：

```text
User: 帮我分析一下酒店最近入住率下降的原因
```

退出程序：

```text
User: exit
```


## TODO

  - [ ] 模板配置管理：切换模板适配不同的行业，待完成
  
