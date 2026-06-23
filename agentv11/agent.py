from google.adk.agents.llm_agent import Agent
from google.adk.agents.parallel_agent import ParallelAgent
from google.adk.agents.sequential_agent import SequentialAgent


MODEL_NAME = "openai/gpt-4.1-nano"


idea_agent = Agent(
    name="idea_agent",
    model=MODEL_NAME,
    description="Suggests a simple project idea.",
    instruction="""
You are the Idea Agent.

Given the user's request, suggest ONE simple project idea.
Focus only on the project concept.

Return format:

IDEA:
Project Name: ...
Summary: ...
"""
)


architecture_agent = Agent(
    name="architecture_agent",
    model=MODEL_NAME,
    description="Suggests a simple architecture.",
    instruction="""
You are the Architecture Agent.

Given the user's request, suggest a simple technical architecture.
Focus on agents, tools, and data flow.

Return format:

ARCHITECTURE:
Agents:
- ...
Tools:
- ...
Flow:
- ...
"""
)


risk_agent = Agent(
    name="risk_agent",
    model=MODEL_NAME,
    description="Identifies implementation risks.",
    instruction="""
You are the Risk Agent.

Given the user's request, identify practical implementation risks.
Focus on what can go wrong.

Return format:

RISKS:
- ...
- ...
- ...
"""
)


parallel_analysis = ParallelAgent(
    name="parallel_analysis",
    description="Runs idea, architecture, and risk agents in parallel.",
    sub_agents=[
        idea_agent,
        architecture_agent,
        risk_agent,
    ],
)


summary_agent = Agent(
    name="summary_agent",
    model=MODEL_NAME,
    description="Combines parallel agent outputs into one final answer.",
    instruction="""
You are the Summary Agent.

You will receive outputs from:
- Idea Agent
- Architecture Agent
- Risk Agent

Your job:
- Merge them into one coherent final answer.
- Preserve the project idea from the Idea Agent.
- Use architecture details from the Architecture Agent.
- Use risks from the Risk Agent.
- Do not invent a completely different project.

Return final answer with these sections:

Project Name:
Summary:
Agents:
Architecture Flow:
Risks:
Why this is a good beginner multi-agent project:
"""
)


root_agent = SequentialAgent(
    name="agentv11",
    description="Parallel multi-agent workflow followed by summary merge.",
    sub_agents=[
        parallel_analysis,
        summary_agent,
    ],
)