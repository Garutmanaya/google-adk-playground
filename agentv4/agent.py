from datetime import datetime
from google.adk.agents.llm_agent import Agent


def get_current_time() -> str:
    """Returns current local datetime."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


root_agent = Agent(
    name="agentv4",
    model="openai/gpt-4.1-nano",
    description="Tool-enabled ADK agent.",
    instruction="""
You are Agent V4.

You have access to tools.
Use tools whenever needed for accurate answers.
If user asks about time/date/current timestamp, use tool.
""",
    tools=[get_current_time]
)