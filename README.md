# Google ADK Learning Playground

## Purpose

This repository contains progressive hands-on examples for learning **Google ADK (Agent Development Kit)** using simple, practical use cases.

The goal is to understand major ADK concepts step by step:

* Basic Agents
* Tools
* Memory
* RAG
* Sequential Workflows
* Parallel Workflows
* Routing
* Supervisor Patterns
* Reflection Loops
* Human-in-the-loop
* A2A Communication

Each use case is isolated into a separate agent folder:

```bash
agentv1/
agentv2/
...
agentv16/
```

Each version introduces exactly one new ADK concept.

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

Replace `agentv1` with any version.

---

# Use Cases

---

## agentv1 — Basic Agent

### Use Case

Simple single ADK agent.

### Concepts

* Agent
* Model
* Instructions
* root_agent

### Test

```text
What is AI?
```

---

## agentv2 — Runtime Metadata Agent

### Use Case

Agent knows runtime metadata like version and model.

### Concepts

* Runtime metadata
* Prompt injection

### Test

```text
What model are you using?
```

---

## agentv3 — Structured Output Agent

### Use Case

Agent returns machine-readable JSON output.

### Concepts

* Structured output
* Classification
* JSON response

### Test

```text
Write Python code for binary search
```

---

## agentv4 — Single Tool Agent

### Use Case

Agent uses one tool.

### Concepts

* Tool registration
* Tool calling

### Test

```text
What is current time?
```

---

## agentv5 — Multi Tool Agent

### Use Case

Agent selects between multiple tools.

### Concepts

* Tool routing
* Parameter extraction

### Test

```text
Calculate 25 * 88
```

```text
Weather in New York
```

---

## agentv6 — Tool Error Handling

### Use Case

Agent handles tool failures gracefully.

### Concepts

* Tool failure
* Retry patterns
* Error handling

### Test

```text
Weather in London
```

---

## agentv7 — Session Memory Agent

### Use Case

Agent remembers within same conversation.

### Concepts

* Session memory
* Conversation history

### Test

```text
My name is Sam
```

```text
What is my name?
```

---

## agentv8 — Long-Term Memory Agent

### Use Case

Agent stores persistent memory in JSON.

### Concepts

* Memory tools
* Persistent storage

### Test

```text
Remember my favorite language is Python
```

```text
What is my favorite language?
```

---

## agentv9 — RAG Agent

### Use Case

Agent retrieves knowledge from local documents.

### Concepts

* Retrieval
* Local RAG

### Test

```text
What is RAG?
```

---

## agentv10 — Sequential Workflow Agent

### Use Case

Fixed workflow execution.

### Concepts

* SequentialAgent
* Deterministic pipelines

### Flow

```text
Planner → Writer → Reviewer
```

### Test

```text
Explain ADK in simple terms
```

---

## agentv11 — Parallel Workflow Agent

### Use Case

Independent agents run in parallel.

### Concepts

* ParallelAgent
* Concurrent execution

### Flow

```text
Idea Agent
Architecture Agent
Risk Agent
```

### Test

```text
Suggest multi-agent project
```

---

## agentv12 — Router Agent

### Use Case

Route requests to best specialist agent.

### Concepts

* Routing
* Dynamic delegation

### Flow

```text
Router → Specialist Agent
```

### Test

```text
What is RAG?
```

---

## agentv13 — Supervisor Agent

### Use Case

Supervisor dynamically chooses required agents.

### Concepts

* Conditional orchestration
* Dynamic workflow

### Test

```text
Design and review smart parking project
```

---

## agentv14 — Reflection Agent

### Use Case

Agent improves output using critique.

### Concepts

* Reflection
* Self-improvement loop

### Flow

```text
Generate → Critique → Improve
```

### Test

```text
Design smart parking multi-agent system
```

---

## agentv15 — Human-in-the-Loop Agent

### Use Case

Sensitive actions require approval.

### Concepts

* Human approval
* Safe execution

### Flow

```text
Plan → Approval → Execute
```

### Test

```text
Deploy app to AWS
```

---

## agentv16 — A2A Multi-Agent System

### Use Case

Coordinator communicates with multiple specialist agents.

### Concepts

* Agent-to-Agent communication
* Distributed orchestration

### Flow

```text
Coordinator
 ├── Availability Agent
 ├── Pricing Agent
 ├── Traffic Agent
 └── Risk Agent
```

### Test

```text
Find best parking near downtown
```

---

# Learning Progression

Recommended order:

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
* Production Multi-Agent Systems

