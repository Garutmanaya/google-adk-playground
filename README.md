# Google ADK Learning Playground

# Purpose

This repository contains progressive hands-on examples for learning **Google ADK (Agent Development Kit)** using practical, easy-to-understand use cases.

The objective is to understand major ADK concepts step by step:

* Basic Agents
* Tools
* Memory
* RAG
* Sequential Workflows
* Parallel Workflows
* Router Agents
* Supervisor Agents
* Reflection Loops
* Human-in-the-loop
* Agent-to-Agent (A2A)

Each use case is implemented as a separate agent version:

```bash
agentv1/
agentv2/
...
agentv16/
```

Each version introduces exactly one major ADK concept.

---

# Setup

## Prerequisites

* Python 3.11+
* uv
* OpenAI API Key or Gemini API Key

---

## Create Project

```bash
uv init adk-learning
cd adk-learning
```

Install dependencies:

```bash
uv add google-adk litellm python-dotenv
```

---

## Configure Environment

Create `.env`

```bash
OPENAI_API_KEY=your_key_here
```

or

```bash
GOOGLE_API_KEY=your_key_here
```

---

## Run ADK Web UI

```bash
uv run adk web .
```

---

## Run Single Agent

```bash
uv run adk run agentv1
```

Replace `agentv1` with any agent version.

---

# Use Cases

---

# agentv1 — Basic Agent

## Use Case

Simplest possible ADK agent.

## Why It Matters

Introduces minimum required ADK structure.

## Key Concepts

* Agent
* Model
* Instruction
* root_agent

## Test Examples

```text
What is AI?
```

---

# agentv2 — Runtime Metadata Agent

## Use Case

Agent becomes aware of runtime metadata.

## Why It Matters

LLMs do not know runtime config automatically.

## Key Concepts

* Runtime metadata
* Prompt injection
* Context awareness

## Test Examples

```text
What model are you using?
What version are you?
```

---

# agentv3 — Structured Output Agent

## Use Case

Agent returns JSON output.

## Why It Matters

Essential for orchestration and automation.

## Key Concepts

* Structured output
* JSON response
* Classification

## Test Examples

```text
Write Python code for binary search
```

---

# agentv4 — Single Tool Agent

## Use Case

Agent uses one external tool.

## Why It Matters

Introduces tool invocation lifecycle.

## Key Concepts

* Tool registration
* Tool calling

## Test Examples

```text
What is current time?
```

---

# agentv5 — Multi Tool Agent

## Use Case

Agent selects between multiple tools.

## Why It Matters

Real agents rarely use just one tool.

## Key Concepts

* Tool routing
* Parameter extraction

## Test Examples

```text
Calculate 25 * 88
Weather in New York
```

---

# agentv6 — Tool Error Handling

## Use Case

Agent handles tool failures gracefully.

## Why It Matters

Production tools fail frequently.

## Key Concepts

* Error handling
* Tool failures
* Retry patterns

## Test Examples

```text
Weather in London
```

---

# agentv7 — Session Memory Agent

## Use Case

Agent remembers conversation within session.

## Why It Matters

Useful for short-term conversational memory.

## Key Concepts

* Session memory
* Conversation history

## Test Examples

```text
My name is Sam
What is my name?
```

---

# agentv8 — Long-Term Memory Agent

## Use Case

Agent stores persistent memory.

## Why It Matters

Enables personalization across sessions.

## Key Concepts

* Persistent memory
* Memory tools
* JSON storage

## Test Examples

```text
Remember my favorite language is Python
What is my favorite language?
```

---

# agentv9 — RAG Agent

## Use Case

Agent retrieves knowledge from local documents.

## Why It Matters

Foundation for enterprise AI agents.

## Key Concepts

* Retrieval
* Local RAG

## Test Examples

```text
What is RAG?
What is ADK?
```

---

# agentv10 — Sequential Workflow Agent

## Use Case

Fixed execution pipeline.

## Why It Matters

Best for deterministic workflows.

## Workflow

```text
Planner → Writer → Reviewer
```

## Key Concepts

* SequentialAgent
* Fixed pipelines

## Test Examples

```text
Explain ADK in simple terms
```

---

# agentv11 — Parallel Workflow Agent

## Use Case

Independent agents run simultaneously.

## Why It Matters

Reduces latency for independent tasks.

## Workflow

```text
Idea Agent
Architecture Agent
Risk Agent
```

## Key Concepts

* ParallelAgent
* Concurrent execution

## Test Examples

```text
Suggest multi-agent project
```

---

# agentv12 — Router Agent

## Use Case

Route requests to best specialist.

## Why It Matters

Useful for multi-domain systems.

## Workflow

```text
Router → Specialist Agent
```

## Key Concepts

* Routing
* Dynamic delegation

## Test Examples

```text
What is RAG?
```

---

# agentv13 — Supervisor Agent

## Use Case

Supervisor decides which agents to involve.

## Why It Matters

Enables adaptive workflows.

## Workflow

```text
Supervisor
 ├── Planner
 ├── Executor
 └── Validator
```

## Key Concepts

* Conditional orchestration
* Adaptive execution

## Test Examples

```text
Design and review smart parking project
```

---

# agentv14 — Reflection Agent

## Use Case

Agent improves output using self-critique.

## Why It Matters

Useful for iterative improvement.

## Workflow

```text
Generate → Critique → Improve
```

## Key Concepts

* Reflection
* Self-improvement

## Test Examples

```text
Design smart parking multi-agent system
```

---

# agentv15 — Human-in-the-Loop Agent

## Use Case

Sensitive actions require approval.

## Why It Matters

Critical for safe production systems.

## Workflow

```text
Plan → Approval → Execute
```

## Key Concepts

* Human approval
* Safe execution

## Test Examples

```text
Deploy app to AWS
```

---

# agentv16 — A2A Multi-Agent System

## Use Case

Coordinator interacts with multiple specialist agents.

## Why It Matters

Enables distributed multi-agent systems.

## Workflow

```text
Coordinator
 ├── Availability Agent
 ├── Pricing Agent
 ├── Traffic Agent
 └── Risk Agent
```

## Key Concepts

* A2A
* Distributed orchestration

## Test Examples

```text
Find best parking near downtown
```

---

# Choosing the Right Agent Pattern

Selecting the correct orchestration pattern is critical in production AI systems.

---

## SequentialAgent → Best for Fixed Pipelines

Use when execution order is deterministic.

Example:

```text
Plan → Execute → Review
```

Best for:

* ETL workflows
* CI/CD pipelines
* Approval chains

Advantages:

* Predictable
* Easy to debug
* Easy to test

---

## Supervisor Agent → Best for Adaptive Workflows

Use when workflow changes based on task complexity.

Example:

```text
Simple task → Executor only
Complex task → Planner + Executor + Validator
```

Best for:

* Complex reasoning
* Dynamic workflows
* Adaptive orchestration

Advantages:

* Flexible
* Intelligent delegation
* Cost optimized

---

## ParallelAgent → Best for Independent Tasks

Use when tasks are independent.

Example:

```text
Cost Analysis
Security Analysis
Performance Analysis
```

Best for:

* Independent analysis
* Multi-perspective evaluation
* Latency optimization

Advantages:

* Fast
* Scalable
* Efficient

---

# Recommended Learning Order

```text
1 → 4 → 5 → 7 → 8 → 9 → 10 → 11 → 12 → 13 → 14 → 15 → 16
```

---

# Next Steps

Advanced topics:

* Shared Context Store
* MCP Integration
* Real Remote A2A
* Streaming Agents
* Async Agents
* Multi-modal Agents
* Production Multi-Agent Platforms
