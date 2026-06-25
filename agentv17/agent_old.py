from google.adk.agents.llm_agent import Agent

MODEL_NAME = "openai/gpt-4.1-nano"

# Shared context store (demo only)
shared_context = {
    "plan": None,
    "solution": None,
    "validation": None
}


def write_plan(plan: str) -> str:
    """
    Write implementation plan to shared context.
    """
    shared_context["plan"] = plan
    return "Plan stored in shared context."


def read_plan() -> str:
    """
    Read implementation plan from shared context.
    """
    return shared_context["plan"] or "No plan found."


def write_solution(solution: str) -> str:
    """
    Write solution to shared context.
    """
    shared_context["solution"] = solution
    return "Solution stored in shared context."


def read_solution() -> str:
    """
    Read solution from shared context.
    """
    return shared_context["solution"] or "No solution found."


def write_validation(validation: str) -> str:
    """
    Write validation to shared context.
    """
    shared_context["validation"] = validation
    return "Validation stored in shared context."


def show_context() -> dict:
    """
    Returns the complete shared context store.

    MUST use this tool when user asks:
    - show shared context
    - inspect state
    - display current context
    - show plan/solution/validation state
    """

    return shared_context


planner_agent = Agent(
    name="planner_agent",
    model=MODEL_NAME,
    instruction="""
You are Planner Agent.

Create implementation plan.
Store the plan using write_plan.
""",
    tools=[write_plan]
)


executor_agent = Agent(
    name="executor_agent",
    model=MODEL_NAME,
    instruction="""
You are Executor Agent.

Read plan using read_plan.
Generate solution.
Store solution using write_solution.
""",
    tools=[read_plan, write_solution]
)


validator_agent = Agent(
    name="validator_agent",
    model=MODEL_NAME,
    instruction="""
You are Validator Agent.

Read plan and solution.
Validate solution quality.
Store validation using write_validation.
""",
    tools=[read_plan, read_solution, write_validation]
)


root_agent = Agent(
    name="agentv17",
    model=MODEL_NAME,
    description="Shared context store demo.",

    instruction="""
You are Agent V17.

You coordinate:
- planner_agent
- executor_agent
- validator_agent

Use shared context store to exchange information.

Important:
- Planner writes plan.
- Executor reads plan and writes solution.
- Validator reads both and writes validation.
- Use show_context if user asks to inspect state.
- If user asks:
  - show context
  - inspect context
  - display state
  - show shared context
""",
    sub_agents=[
        planner_agent,
        executor_agent,
        validator_agent
    ],
    tools=[show_context]
)
