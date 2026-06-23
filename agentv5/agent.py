from datetime import datetime
from google.adk.agents.llm_agent import Agent


def get_current_time() -> str:
    """Returns current local date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculator(expression: str) -> str:
    """
    Evaluates a simple arithmetic expression.
    Example: 10 + 20, 100 * 5
    """
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Calculation error: {str(e)}"


def get_weather(city: str) -> str:
    """
    Returns weather information for a city.
    Currently mock data for learning.
    """
    return f"Weather in {city}: 28°C, Sunny"


root_agent = Agent(
    name="agentv5",
    model="openai/gpt-4.1-nano",
    description="Multi-tool ADK agent.",
    instruction="""
You are Agent V5.

You have multiple tools available.
Choose the correct tool based on user request.

Use:
- get_current_time → for time/date questions
- calculator → for math calculations
- get_weather → for weather questions
""",
    tools=[get_current_time, calculator, get_weather]
)