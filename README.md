#项目目标
用户输入问题：

```
用户：
帮我分析一下酒店最近入住率下降的原因

↓

AI Chat

↓

调用 GPT 模型

↓

返回分析结果

```

# 系统结构

┌──────────────────────────────┐
│          用户层 User          │
│                              │
│  输入问题 / 查看AI回答        │
└──────────────┬───────────────┘
               │
               ▼

┌──────────────────────────────┐
│        前端 Chat UI           │
│                              │
│  Web / App / 小程序           │
│                              │
└──────────────┬───────────────┘
               │
               ▼

┌─────────────────────────────────────────┐
│             AI Application              │
│          （你的 Python 后端）            │
│                                         │
│                                         │
│  ┌──────────────┐                       │
│  │ Prompt管理   │                       │
│  │              │                       │
│  │ 定义AI身份   │                       │
│  │ 定义规则     │                       │
│  └──────────────┘                       │
│                                         │
│  ┌──────────────┐                       │
│  │ Memory管理   │                       │
│  │              │                       │
│  │ 保存历史     │                       │
│  │ 用户信息     │                       │
│  └──────────────┘                       │
│                                         │
│  ┌──────────────┐                       │
│  │ Tool管理     │                       │
│  │              │                       │
│  │ Python函数   │                       │
│  │ API接口      │                       │
│  │ 数据库查询   │                       │
│  └──────────────┘                       │
│                                         │
└──────────────────┬──────────────────────┘
                   │
                   │ 发送：
                   │
                   │ ① Prompt
                   │ ② Memory
                   │ ③ 用户问题
                   │ ④ Tool定义
                   ▼

┌──────────────────────────────┐
│       OpenAI API              │
│                              │
│   Responses API              │
│                              │
└──────────────┬───────────────┘
               │
               ▼

┌──────────────────────────────┐
│        GPT Model              │
│                              │
│       AI推理引擎              │
│                              │
│  负责：                       │
│  - 理解问题                  │
│  - 推理                      │
│  - 生成答案                  │
│  - 判断是否调用Tool           │
│                              │
└──────────────────────────────┘

# 必须实现的功能
## 基础聊天
## Prompt Engineering
### 按照官方的结构来构造prompt
```
[Instructions]
    定义 AI 的身份、目标、行为规则


[Context]
    提供 AI 完成任务需要知道的背景信息


[Input]
    用户当前请求或任务内容

[Tools]
    定义 AI 可以使用的外部能力

[Output]
    定义 AI 输出格式和约束


```

### 示例

```
<Instructions>

你是一名酒店运营智能助手。

你的目标：
帮助酒店管理人员分析经营问题，
并提供收益优化建议。


规则：

1. 不允许虚构业务数据。
2. 缺少必要信息时主动询问。
3. 优先使用工具获取真实数据。


</Instructions>


<Context>

酒店：

Tokyo Hotel


业务类型：

城市商务酒店


当前关注：

入住率下降。


已有信息：

最近30天入住率下降20%。

</Context>


<Input>

分析入住率下降原因，
并提出优化方案。

</Input>


<Tools>

你可以调用：

get_booking_data()

查询订单数据。


get_customer_review()

查询客户评价。


get_room_price()

查询竞争价格。


</Tools>


<Output>

输出格式：


# 分析结果

## 原因

- 原因1
- 原因2


## 数据依据

说明分析依据。


## 建议方案

- 建议1
- 建议2


</Output>
```

## Conversation State
能开发一个 AI Chat 应用，让用户进行连续多轮对话，并且 AI 能正确理解前后文关系。
- 保存对话上下文
    能够保存用户与 AI 之间的历史消息。
    保证后续请求能够携带必要的上下文信息。
- 支持连续多轮交互
    用户连续提问时，AI 能基于之前的对话内容理解当前请求。
    避免每次请求都重新开始。
- 实现状态传递
    在每次调用模型时，将有效的 Conversation State 传递给模型。
    确保模型生成结果基于完整上下文。



## Structured Output
结合你的酒店 AI Chat 项目，我建议定义为：
``` json
{
  "analysis": {
    "summary": "string",
    "problem_type": "string",
    "confidence": "high | medium | low"
  },
  "findings": [
    {
      "reason": "string",
      "evidence": "string",
      "impact": "high | medium | low"
    }
  ],
  "recommendations": [
    {
      "action": "string",
      "priority": "high | medium | low",
      "expected_result": "string"
    }
  ]
}
```
### 字段分析
- analysis (总体分析)负责：
AI 对问题的总结
判断问题类型
表达分析可信度

- findings（发现的问题）
负责:
存储 AI 的分析依据。
数组形式：
```
"findings": []
```
因为一个问题可能有多个原因。
每个原因：

```
{
 "reason":"",
 "evidence":"",
 "impact":""
}
```

recommendations（建议）
负责：
输出可执行方案。
结构：
{
 "action":"",
 "priority":"",
 "expected_result":""
}
### 第一阶段验收要求
Structured Output 需要做到：
| 能力               | 要求 |
| ---------------- | -- |
| 定义 JSON Schema   | ✅  |
| 限制字段结构           | ✅  |
| 限制字段类型           | ✅  |
| 限制枚举值            | ✅  |
| 模型稳定返回 JSON      | ✅  |
| Python 可以解析 JSON | ✅  |


## Function Calling

第一阶段 Function Calling 的目标，是让 AI Chat 从“会聊天”升级为“会使用你的程序能力”。
你的 AI Chat 完成 Function Calling 后应该满足：
- 定义 Python Function
- 生成 Tool Schema
- 把 Tool 注册给 GPT
- 模型判断是否调用 Tool
- Python 执行函数
- 返回 Tool Result 给 GPT
- GPT 根据结果生成回答



## Embedding
在你的第一阶段 AI Chat 验收项目中，Embedding 不应该做到完整 RAG 系统，而是达到：
1、理解 Embedding 的作用，并实现一次简单的文本向量化 + 相似度检索能力。
- /Users/xiaoyuqin/plan/hotel-ai-chat/hotel_documents目录下的文本转换成向量
2、调用 Embedding API
- 使用 OpenAI Embeddings API
- 输入文本
- 获取向量结果
3、建立简单文本知识集合
第一阶段只需要准备少量文本数据。
hotel_documents/
├── check_in_policy.txt
├── room_type.txt
├── cancellation_policy.txt

4. 文档向量化
- 实现文档转成向量，获取到向量结果，然后保存为json文件。
5.实现简单相似度搜索
用户输入：什么时候可以入住？
系统：用户问题-》Embedding-》计算相似度-》找到相关文档
返回：入住规则文档
6. 将检索结果提供给 GPT
完成一个最小 RAG 流程：
用户问题-》Embedding Search-》找到相关知识-》加入 Prompt Context-》GPT回答

第一阶段验收标准

| 能力               | 要求 |
| ---------------- | -- |
| 理解 Embedding 原理  | ✅  |
| 调用 Embedding API | ✅  |
| 文本转换向量           | ✅  |
| 保存向量数据           | ✅  |
| 计算相似度            | ✅  |
| 检索相关文本           | ✅  |
| 把结果交给 GPT        | ✅  |



# 最终验收标准
完成下面 6 项，就算完成：

| 能力                  | 是否完成 |
| ------------------- | ---- |
| Python 调 OpenAI API | ✅    |
| Prompt 控制 AI 行为     | ✅    |
| 多轮聊天                | ✅    |
| JSON 输出             | ✅    |
| AI 调用 Python 函数     | ✅    |
| 简单知识库查询             | ✅    |


# 项目结构
hotel-ai-chat/

├── app.py                 # 主入口，

├── config/
│   └── settings.py        # 环境变量/API Key

llm/
│
├── base.py                  # LLM 抽象接口
├── client.py                # 总工厂
│
├── openai/
│   ├── __init__.py
│   ├── factory.py           # OpenAI 工厂
│   ├── chat.py              # Chat Completions
│   ├── responses.py         # Responses API
│   └── state.py             # OpenAI Provider State
│
├── anthropic/
│   ├── __init__.py
│   ├── factory.py
│   └── messages.py
│
└── google/
    ├── __init__.py
    ├── factory.py
    └── generate_content.py


├── prompts/
│   └── assistant_prompt.py # Prompt定义

memory/
│
├── state.py
├── manager.py
├── context.py
│
└── provider/
    ├── __init__.py
    ├── state.py          # 抽象基类
    └── openai_state.py   # OpenAI 的状态
├── tools/
│   ├── base.py
│   ├── schema.py
│   ├── registry.py
│   ├── loader.py
│   ├── executor.py
│   ├── result.py
│   └── hotel/
|       ├── __init__.py
|       ├── search_hotel.py
├── schemas/
│   └── output.py          # Structured Output
embedding/
├── base.py
├── client.py
└── openai/
    ├── __init__.py
    ├── factory.py
    ├── embedding.py
|
|-knowledge/
│
├── admin/
│   ├── service.py          ⭐ 对外唯一入口
│   ├── request.py
│   └── response.py
│
├── repository/             ⭐ Document 元数据管理
│   ├── base.py
│   └── memory.py
│
├── base.py              # Knowledge 抽象接口
├── client.py            # Knowledge Factory
├── manager.py           # Knowledge 管理器（协调整个知识入库流程）
├── default.py           # 默认 Knowledge 实现
|── source.py           # KnowledgeSource,描述一个知识源（Knowledge Source）。
|── detector.py         # KnowledgeSourceDetector,识别知识源类型
│
├── document.py          # Document 领域模型
├── chunk.py             # Chunk 领域模型
│
├── loader/              # 数据加载层（负责读取各种数据源）
│   ├── __init__.py
│   ├── factory.py       # 根据 KnowledgeSource 创建 Loader。
│   ├── base.py          # Loader 抽象接口
│   ├── text.py          # Text Loader
│   ├── markdown.py      # Markdown Loader
│   ├── pdf.py           # PDF Loader
│   └── url.py           # URL Loader
│
├── parser/              # 内容解析层（负责解析原始数据）
│   ├── __init__.py
│   ├── factory.py
│   ├── base.py          # Parser 抽象接口
│   ├── text.py          # Text Parser
│   ├── markdown.py      # Markdown Parser
│   └── pdf.py           # PDF Parser
│   └── url.py           # url Parser
│
├── chunker/             # 文本切块层（负责将 Document 拆分为 Chunk）
│   ├── __init__.py
│   ├── base.py          # Chunker 抽象接口
│   ├── recursive.py     # Recursive Chunker
│   └── token.py         # Token Chunker
│   ├── factory.py   ← 新增

|  
├── requirements.txt

└── README.md



我认为你的框架距离"可复用 AI 框架"只差三件事
Knowledge Admin（知识生命周期管理）
Prompt 管理（模板、变量、版本）
Agent 配置（把 Prompt、Knowledge、Tool 组合起来）


不过也要有一个现实预期：不是所有场景都只改 Prompt 和知识库就够了。 有些场景（例如需要审批流、复杂规划、多 Agent 协作）还需要增加新的 Tool 或 Workflow。但对于大量问答、客服、运营分析、内部助手这类场景，你设想的这种复用方式是完全可行的。

