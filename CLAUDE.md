# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概况

这是 `hotel-ai-chat`，一个面向酒店运营场景的 AI Chat 后端原型。README.md 中定义的目标是让用户输入酒店经营问题，后端调用 OpenAI/兼容 OpenAI 的 LLM API，结合 Prompt、多轮对话状态、函数调用和简单知识库检索生成回答。

当前 Python 入口是：

```bash
python ./app.py
```

运行时依赖 `.env` 提供 API 配置。OpenAI 兼容接口的 `base_url` 应是 provider root，例如：

```env
OPENAI_BASE_URL=https://llm-api.arkcat.cn/v1
```

不要写成 `/v1/chat/completions`，否则 Responses API 会拼出 `/v1/chat/completions/responses` 并触发 404。

## 常用命令

激活 Python 虚拟环境：

```bash
cd /Users/xiaoyuqin/plan/hotel-ai-chat
source .venv/bin/activate
```

安装 Python 依赖：

```bash
pip install -r requirements.txt
```

运行主程序：

```bash
python ./app.py
```

检查当前 Python 是否来自虚拟环境：

```bash
which python
python --version
```

当前项目还没有测试、lint、build 命令；`package.json` 只有 npm `openai` 依赖，Python 运行时以 `.venv` 和 `requirements.txt` 为准。

## 架构概览

- `app.py`：命令行聊天入口，创建 `ConversationState`、`ConversationManager` 和 LLM client，然后进入多轮交互循环。
- `config/settings.py`：从环境变量读取 OpenAI API key、base URL、model 等配置。
- `llm/`：LLM 抽象和 provider 工厂层。
  - `base.py`：LLM 抽象接口。
  - `client.py`：LLM client 总工厂，当前 `app.py` 从 `llm.client import create_llm_client` 创建调用器。
  - `llm/openai/`：OpenAI provider 相关封装。
    - `factory.py`：OpenAI client factory。
    - `chat.py`：Chat Completions 封装。
    - `responses.py`：Responses API 封装。
    - `state.py`：OpenAI provider state。
- `memory/`：Conversation State 相关实现，负责保存用户/AI 历史消息并生成传递给模型的上下文快照。
- `prompts/`：Prompt 定义，README.md 要求 Prompt 使用 Instructions、Context、Input、Tools、Output 结构。
- `tools/`：函数调用/业务工具占位目录，当前包含 `price.py`、`booking.py`。
- `models/`：JSON/schema 相关占位目录，当前包含 `schemas.py`。
- `hotel_documents/`：第一阶段 RAG/Embedding 的文档目录，README.md 要求准备 `check_in_policy.txt`、`room_type.txt`、`cancellation_policy.txt`。

## README.md 中的验收方向

第一阶段重点能力：

- Python 调 OpenAI API。
- Prompt 控制 AI 行为。
- 多轮聊天。
- Structured Output：定义 JSON Schema，限制字段结构、类型、枚举值，让模型稳定返回 JSON，并由 Python 解析。
- Function Calling：定义 Python function，生成 tool schema，注册给 GPT，执行函数后把结果返回模型。
- Embedding/RAG 最小流程：读取 `hotel_documents/` 文本，调用 Embedding API，保存向量 JSON，做简单相似度搜索，并把检索结果加入 Prompt Context。

最终验收标准是完成：

```text
Python 调 OpenAI API
Prompt 控制 AI 行为
多轮聊天
JSON 输出
AI 调用 Python 函数
简单知识库查询
```

## 环境文件

`.env` 中保存运行时环境变量。不要在提交或说明中泄露真实 API key；如果 `.env` 已包含敏感信息，应提示用户将其加入 `.gitignore` 或使用占位值。
