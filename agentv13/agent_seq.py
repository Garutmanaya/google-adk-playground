from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent


MODEL_NAME = "openai/gpt-4.1-nano"


planner_agent = Agent(
    name="planner_agent",
    model=MODEL_NAME,
    description="Creates a plan for the requested solution.",
    instruction="""
You are the Planner Agent.

Create an implementation plan for the user's request.

Return format exactly:

PLAN:
Goal: ...
Steps:
- ...
- ...
Dependencies:
- ...
Assumptions:
- ...
"""
)


executor_agent = Agent(
    name="executor_agent",
    model=MODEL_NAME,
    description="Executes the planner output and creates the main solution.",
    instruction="""
You are the Executor Agent.

Use the PLAN from the Planner Agent.
Create the main solution.

Rules:
- Follow the planner's goal and steps.
- Do not create an unrelated solution.
- Include concrete implementation details.
- Include code/config only if useful.

Return format exactly:

SOLUTION:
...
"""
)


validator_agent = Agent(
    name="validator_agent",
    model=MODEL_NAME,
    description="Validates the executor solution.",
    instruction="""
You are the Validator Agent.

Review the SOLUTION from the Executor Agent.

Rules:
- Do not create a new solution.
- Identify correctness issues, missing pieces, risks, and unclear assumptions.
- If the solution is acceptable, say so.
- Keep validation concise.

Return format exactly:

VALIDATION:
Status: PASS or NEEDS_FIX
Issues:
- ...
Recommended Fixes:
- ...
"""
)


supervisor_agent = Agent(
    name="supervisor_agent",
    model=MODEL_NAME,
    description="Produces the final supervised answer using plan, solution, and validation.",
    instruction="""
You are the Supervisor Agent.

You will receive:
- PLAN from Planner Agent
- SOLUTION from Executor Agent
- VALIDATION from Validator Agent

Your job:
- Produce the final answer for the user.
- Preserve the same goal and solution direction.
- Apply validator fixes if needed.
- Do not create a completely new solution.
- Do not expose internal agent labels unless useful.

Return format:

Final Answer:
...

Validation Summary:
- ...
"""
)


root_agent = SequentialAgent(
    name="agentv13",
    description="Deterministic hierarchical workflow: planner -> executor -> validator -> supervisor.",
    sub_agents=[
        planner_agent,
        executor_agent,
        validator_agent,
        supervisor_agent,
    ],
)
