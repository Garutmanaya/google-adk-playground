from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent


MODEL_NAME = "openai/gpt-4.1-nano"


planner_agent = Agent(
    name="planner_agent",
    model=MODEL_NAME,
    description="Creates a plan only.",
    instruction="""
You are the Planner Agent.

Create a concise plan for answering the user's request.

Return format exactly:

PLAN:
- ...
- ...

Do not suggest the final project.
Do not write the final answer.
""",
)


writer_agent = Agent(
    name="writer_agent",
    model=MODEL_NAME,
    description="Writes the first draft using the planner output.",
    instruction="""
You are the Writer Agent.

Use the PLAN from the previous agent.
Write ONE project suggestion only.

Return format exactly:

DRAFT:
Project Name: ...
Summary: ...
Agents:
- ...
A2A Flow:
- ...
Why it is simple:
- ...

Do not provide multiple alternatives.
""",
)


reviewer_agent = Agent(
    name="reviewer_agent",
    model=MODEL_NAME,
    description="Improves the writer draft without changing the project idea.",
    instruction="""
You are the Reviewer Agent.

Your job is to improve the DRAFT from the Writer Agent.

Strict rules:
- Do NOT create a new project idea.
- Do NOT replace the project name.
- Do NOT change the main domain of the project.
- Preserve the writer's proposal.
- Only improve clarity, structure, completeness, and wording.
- If the draft is weak, improve it while keeping the same project.

Return only the final improved answer.
""",
)


root_agent = SequentialAgent(
    name="agentv10",
    description="Sequential workflow: planner -> writer -> reviewer.",
    sub_agents=[
        planner_agent,
        writer_agent,
        reviewer_agent,
    ],
)
