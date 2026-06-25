from google.adk.agents.llm_agent import Agent

MODEL_NAME = "openai/gpt-4.1-nano"

shared_context = {
    "plan": None,
    "solution": None,
    "validation": None,
}


def create_plan(task: str) -> dict:
    """
    Create and store a simple implementation plan for the given task.
    MUST be used when user asks to create, design, or plan something.
    """
    plan = {
        "task": task,
        "steps": [
            "Define requirements",
            "Identify agents and responsibilities",
            "Define tools and data sources",
            "Design orchestration flow",
            "Implement minimal prototype",
            "Test and validate behavior",
        ],
    }
    shared_context["plan"] = plan
    return {"status": "stored", "plan": plan}


def execute_plan() -> dict:
    """
    Execute the stored plan.
    MUST be used when user asks to execute, implement, or continue the stored plan.
    """
    if not shared_context["plan"]:
        return {"status": "error", "message": "No plan found. Create a plan first."}

    solution = {
        "based_on_plan": shared_context["plan"],
        "implementation": [
            "Create coordinator agent",
            "Create specialist agents",
            "Register tools",
            "Add shared memory/context",
            "Run tests from ADK web UI",
        ],
    }
    shared_context["solution"] = solution
    return {"status": "stored", "solution": solution}


def validate_solution() -> dict:
    """
    Validate the stored solution.
    MUST be used when user asks to validate, review, or check the solution.
    """
    if not shared_context["solution"]:
        return {"status": "error", "message": "No solution found. Execute plan first."}

    validation = {
        "status": "PASS_WITH_NOTES",
        "notes": [
            "Prototype flow is valid.",
            "Persistence is in-memory only.",
            "Production version should use SQLite, Redis, or PostgreSQL.",
            "Tool calls should be controlled deterministically for critical actions.",
        ],
    }
    shared_context["validation"] = validation
    return {"status": "stored", "validation": validation}


def show_shared_context() -> dict:
    """
    Display complete shared context.
    MUST be used when user asks to show, display, inspect, or print shared context/state.
    """
    return shared_context


root_agent = Agent(
    name="agentv17",
    model=MODEL_NAME,
    description="Shared context store using deterministic workflow tools.",
    instruction="""
You are Agent V17.

You manage a shared context store.

Tool usage rules:
- If user asks to create/design/plan something, call create_plan.
- If user asks to execute/implement/continue the plan, call execute_plan.
- If user asks to validate/review/check the solution, call validate_solution.
- If user asks to show/display/inspect/print context or state, call show_shared_context.

Do not answer these workflow requests directly.
Always use the correct tool first, then summarize the tool result.
""",
    tools=[
        create_plan,
        execute_plan,
        validate_solution,
        show_shared_context,
    ],
)
