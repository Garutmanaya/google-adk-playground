# Google ADK Learning Playground

# Purpose

This repository contains progressive hands-on examples for learning **Google ADK (Agent Development Kit)** using practical and progressively advanced use cases.

The objective is to understand ADK from beginner to production-level patterns.

Topics covered:

* Basic Agents
* Tool Calling
* Memory
* RAG
* Sequential Workflows
* Parallel Workflows
* Router / Supervisor Agents
* Reflection Loops
* Human-in-the-loop
* Agent-to-Agent Communication (A2A)
* Shared Context Store
* MCP Integration
* Streaming
* Async Long Running Agents
* Multi-modal Agents

Each use case is implemented as an isolated agent version.

```bash
agentv1/
agentv2/
...
agentv22/
```

Each version introduces one major concept.

---

# Setup

## Prerequisites

* Python 3.11+
* uv
* OpenAI API Key or Gemini API Key

---

## Create Project

```bash
uv init google-adk-playground
cd google-adk-playground
```

Install dependencies:

```bash
uv add google-adk litellm python-dotenv
```

Optional dependencies:

```bash
uv add "google-adk[a2a]"
uv add uvicorn
uv add mcp
```

---

## Configure Environment

Create `.env`

```env
OPENAI_API_KEY=your_key_here
```

or

```env
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

---

# Use Cases

---

# agentv1 — Basic Agent

### Purpose

Simplest possible ADK agent.

### Key Concepts

* Agent
* Model
* Instructions

### Test

* What is AI?

---

# agentv2 — Runtime Metadata Agent

### Purpose

Agent becomes aware of runtime metadata.

### Key Concepts

* Runtime metadata
* Context injection

### Test

* What model are you using?

---

# agentv3 — Structured Output Agent

### Purpose

Return machine-readable output.

### Key Concepts

* JSON output
* Structured response

### Test

* Generate JSON response for binary search explanation

---

# agentv4 — Single Tool Agent

### Purpose

Agent uses one external tool.

### Key Concepts

* Tool registration
* Tool invocation

### Test

* What is current time?

---

# agentv5 — Multi Tool Agent

### Purpose

Agent chooses between multiple tools.

### Key Concepts

* Tool routing
* Tool selection

### Test

* Calculate 25 * 88
* Weather in New York

---

# agentv6 — Tool Error Handling

### Purpose

Handle tool failures gracefully.

### Key Concepts

* Error handling
* Retry patterns

---

# agentv7 — Session Memory Agent

### Purpose

Short-term memory within session.

### Key Concepts

* Session memory
* Conversation history

### Test

* My name is Sam
* What is my name?

---

# agentv8 — Long-Term Memory Agent

### Purpose

Persistent memory across sessions.

### Key Concepts

* Persistent memory
* Memory tools

---

# agentv9 — RAG Agent

### Purpose

Knowledge retrieval from local docs.

### Key Concepts

* Retrieval
* RAG

---

# agentv10 — Sequential Workflow Agent

### Purpose

Fixed workflow pipeline.

### Workflow

```text
Planner → Writer → Reviewer
```

### Key Concepts

* SequentialAgent

---

# agentv11 — Parallel Workflow Agent

### Purpose

Independent tasks executed in parallel.

### Workflow

```text
Task A
Task B
Task C
```

### Key Concepts

* ParallelAgent

---

# agentv12 — Router Agent

### Purpose

Route requests to specialist agents.

### Workflow

```text
Router → Specialist
```

### Key Concepts

* Dynamic routing

---

# agentv13 — Supervisor Agent

### Purpose

Adaptive orchestration.

### Workflow

```text
Supervisor
 ├── Planner
 ├── Executor
 └── Validator
```

### Key Concepts

* Conditional orchestration

---

# agentv14 — Reflection Agent

### Purpose

Self-improving workflow.

### Workflow

```text
Generate → Critique → Improve
```

### Key Concepts

* Reflection loop

---

# agentv15 — Human-in-the-Loop Agent

### Purpose

Approval required for sensitive actions.

### Workflow

```text
Plan → Approval → Execute
```

### Key Concepts

* Human approval

---

# agentv16 — A2A Simulation Agent

### Purpose

Local A2A simulation using tools.

### Key Concepts

* Agent-to-Agent collaboration

---

# agentv17 — Shared Context Store Agent

### Purpose

Multiple agents share common state.

### Key Concepts

* Shared context
* State-driven workflows

### Lessons Learned

Shared state is useful, but critical state mutation should be controlled by deterministic code.

---

# agentv18 — MCP Tool Agent

### Purpose

Connect ADK with external MCP tools.

### Key Concepts

* MCP
* External tool servers

### Lessons Learned

MCP concept is valuable, but setup/debugging can be environment-specific.

---

# agentv19 — Real Remote A2A Agent

### Purpose

Real distributed multi-agent system.

### Workflow

```text
Coordinator Agent
      ↓
 Remote Agent Server
```

### Key Concepts

* RemoteA2AAgent
* Distributed systems

### Important Lessons

* Remote agents are separate services
* Context is not automatically shared
* Each remote agent has independent environment/runtime

---

# agentv20 — Streaming Agent

### Purpose

Real-time token/event streaming.

### Key Concepts

* Runner.run_live()
* Streaming events

### Lessons Learned

Streaming depends heavily on provider and runtime support.

---

# agentv21 — Async Long Running Agent

### Purpose

Handle long-running jobs asynchronously.

### Workflow

```text
Submit Job → Check Status → Get Result
```

### Key Concepts

* Async workflows
* Job tracking

---

# agentv22 — Multi-modal Agent

### Purpose

Text + image/document reasoning.

### Key Concepts

* Multi-modal models
* Vision/document understanding

### Lessons Learned

Provider/model support is critical.

---

# Choosing the Right Agent Pattern

---

## SequentialAgent → Best for Fixed Pipelines

Use when execution order is deterministic.

Example:

```text
Plan → Execute → Review
```

Best for:

* ETL
* CI/CD
* approval workflows

---

## Supervisor Agent → Best for Adaptive Workflows

Use when workflow changes based on task complexity.

Example:

```text
Simple task → Executor only
Complex task → Planner + Executor + Validator
```

Best for:

* complex reasoning
* adaptive workflows

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

* parallel evaluation
* latency optimization

---

# Recommended Learning Order

```text
v1 → v9   : Fundamentals
v10 → v16 : Workflow orchestration
v17 → v22 : Production patterns
```

---

# Final Recommended Projects

Best real-world projects after completing this learning path:

### 1. AI CloudOps Multi-Agent Platform

* Incident Agent
* Metrics Agent
* Root Cause Agent
* Remediation Agent

### 2. Smart Parking A2A Platform

* Availability Agent
* Pricing Agent
* Traffic Agent
* Risk Agent

### 3. AI Fitness & Recovery Agent

* Health Agent
* Recovery Agent
* Recommendation Agent

---

# Final Takeaways

Core production insights:

* LLM reasoning is powerful but not deterministic
* Critical operations should use deterministic orchestration
* Multi-agent systems work best with clear responsibilities
* Shared context improves collaboration
* A2A enables distributed agent systems
* Production agents require strong workflow control

