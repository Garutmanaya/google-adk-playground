from google.adk.agents.llm_agent import Agent


MODEL_NAME = "openai/gpt-4.1-nano"


coding_agent = Agent(
    name="coding_agent",
    model=MODEL_NAME,
    description="Handles programming, debugging, code generation, and software design questions.",
    instruction="""
You are the Coding Agent.

Handle only software engineering questions:
- Python
- APIs
- debugging
- architecture
- Git
- testing
- deployment code

Answer with practical, copy-paste-ready examples when useful.
"""
)


cloud_agent = Agent(
    name="cloud_agent",
    model=MODEL_NAME,
    description="Handles cloud, AWS, DevOps, infrastructure, deployment, and security questions.",
    instruction="""
You are the Cloud Agent.

Handle only cloud and DevOps questions:
- AWS
- Docker
- Terraform
- CI/CD
- IAM
- Lambda
- SageMaker
- monitoring

Answer with practical implementation guidance.
"""
)


ai_ml_agent = Agent(
    name="ai_ml_agent",
    model=MODEL_NAME,
    description="Handles AI, ML, LLM, agents, RAG, model training, and evaluation questions.",
    instruction="""
You are the AI/ML Agent.

Handle only AI/ML questions:
- LLMs
- agents
- RAG
- embeddings
- model training
- inference
- evaluation
- prompt engineering

Answer clearly with architecture-level reasoning and examples.
"""
)


general_agent = Agent(
    name="general_agent",
    model=MODEL_NAME,
    description="Handles general questions that do not fit coding, cloud, or AI/ML.",
    instruction="""
You are the General Agent.

Handle general questions that do not belong to coding, cloud, or AI/ML.
Keep answers clear and concise.
"""
)


root_agent = Agent(
    name="agentv12",
    model=MODEL_NAME,
    description="Router agent that delegates to specialist sub-agents.",
    instruction="""
You are Agent V12, a router/supervisor agent.

Your job:
- Understand the user's request.
- Route the request to the best specialist sub-agent.
- Do not answer directly if a specialist agent is more appropriate.

Routing rules:
- Use coding_agent for programming, debugging, APIs, software architecture, Git, tests.
- Use cloud_agent for AWS, Docker, Terraform, IAM, CI/CD, cloud deployment, monitoring.
- Use ai_ml_agent for LLMs, AI agents, RAG, embeddings, training, inference, evaluation.
- Use general_agent for all other questions.

If a request spans multiple domains, choose the most dominant domain.
""",
    sub_agents=[
        coding_agent,
        cloud_agent,
        ai_ml_agent,
        general_agent,
    ],
)
