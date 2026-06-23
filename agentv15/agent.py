from google.adk.agents.llm_agent import Agent


MODEL_NAME = "openai/gpt-4.1-nano"


def request_human_approval(action: str) -> str:
    """
    Request human approval before performing a sensitive action.

    Use this tool before any action that modifies data, sends messages,
    deletes resources, deploys infrastructure, or performs external side effects.

    The action parameter must clearly describe what will be done.
    """
    return (
        "APPROVAL_REQUIRED\n"
        f"Proposed action: {action}\n"
        "Please reply with 'approve' to continue or 'reject' to stop."
    )


def execute_mock_action(action: str) -> str:
    """
    Execute an approved mock action.

    Use this tool only after the user explicitly approves the proposed action.
    This is a safe demo tool and does not perform real external changes.
    """
    return f"EXECUTED: {action}"


root_agent = Agent(
    name="agentv15",
    model=MODEL_NAME,
    description="Human-in-the-loop agent with approval before execution.",
    instruction="""
You are Agent V15.

You demonstrate human-in-the-loop control.

Rules:
- For read-only questions, answer directly.
- For actions that modify state, deploy infrastructure, delete resources, send emails, or execute commands, first call request_human_approval.
- Do not call execute_mock_action until the user explicitly replies with "approve".
- If the user replies "reject", stop and do not execute.
- If approval is unclear, ask for explicit approval.
- Keep responses concise.

Examples requiring approval:
- deploy application
- delete file
- update database
- send email
- create infrastructure
- run cleanup
""",
    tools=[
        request_human_approval,
        execute_mock_action,
    ],
)
