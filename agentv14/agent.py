from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent


MODEL_NAME = "openai/gpt-4.1-nano"


generator_agent = Agent(
    name="generator_agent",
    model=MODEL_NAME,
    description="Creates the first draft solution.",
    instruction="""
You are the Generator Agent.

Create an initial solution for the user's request.

Return format:

DRAFT:
...
"""
)


critic_agent = Agent(
    name="critic_agent",
    model=MODEL_NAME,
    description="Critiques the draft solution.",
    instruction="""
You are the Critic Agent.

Review the DRAFT from the Generator Agent.

Find:
- missing details
- weak assumptions
- unclear steps
- implementation risks
- correctness issues

Do not create a new solution.
Only critique the draft.

Return format:

CRITIQUE:
Strengths:
- ...

Issues:
- ...

Required Improvements:
- ...
"""
)


improver_agent = Agent(
    name="improver_agent",
    model=MODEL_NAME,
    description="Improves the draft using the critique.",
    instruction="""
You are the Improver Agent.

Use:
- DRAFT from Generator Agent
- CRITIQUE from Critic Agent

Create an improved final answer.

Rules:
- Preserve the original goal.
- Fix the issues raised by the critic.
- Do not create an unrelated solution.
- Return only the final improved answer.

Return format:

FINAL:
...
"""
)


root_agent = SequentialAgent(
    name="agentv14",
    description="Reflection workflow: generate -> critique -> improve.",
    sub_agents=[
        generator_agent,
        critic_agent,
        improver_agent,
    ],
)
