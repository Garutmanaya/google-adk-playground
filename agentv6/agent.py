import random
from datetime import datetime
from google.adk.agents.llm_agent import Agent


def get_current_time() -> str:
    """Returns current local date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_current_datetime() -> str:
    """
    Returns ONLY the current local system date and current time.

    Use this tool ONLY when the user asks for:
    - current time
    - current date
    - current timestamp
    - today's date

    Do NOT use this tool for:
    - tomorrow's date
    - yesterday's date
    - future date calculations
    - date arithmetic
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

from datetime import datetime, timedelta

def calculate_date(offset_days: int) -> str:
    """
    Calculates a date relative to today.
    Example:
    offset_days=1 → tomorrow
    offset_days=-1 → yesterday
    """
    target = datetime.now() + timedelta(days=offset_days)
    return target.strftime("%Y-%m-%d")

def calculator(expression: str) -> str:
    """
    Evaluates arithmetic expression safely for demo.
    """
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Calculation error: {str(e)}"


def unstable_weather_api(city: str) -> str:
    """
    Mock weather API with random failures.
    Simulates real-world API instability.
    """
    if random.choice([True, False]):
        raise Exception("Weather API timeout")

    return f"Weather in {city}: 27°C, Cloudy"


root_agent = Agent(
    name="agentv6",
    model="openai/gpt-4.1-nano",
    description="Agent with tool error handling.",
    instruction="""
You are Agent V6.

You have multiple tools.

Important behavior:
- Tools may fail.
- If tool returns error or fails, explain clearly.
- Suggest retry if appropriate.
- Never crash or return raw stack trace.
""",
    tools=[get_current_datetime,calculate_date, calculator, unstable_weather_api]
)