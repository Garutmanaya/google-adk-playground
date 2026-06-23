import json
from pathlib import Path
from typing import Any

from google.adk.agents.llm_agent import Agent


MEMORY_FILE = Path(__file__).parent / "memory.json"


def _load_memory() -> dict[str, Any]:
    if not MEMORY_FILE.exists():
        return {}

    try:
        return json.loads(MEMORY_FILE.read_text())
    except json.JSONDecodeError:
        return {}


def _save_memory(memory: dict[str, Any]) -> None:
    MEMORY_FILE.write_text(json.dumps(memory, indent=2))


def remember_fact(key: str, value: str) -> str:
    """
    Store a user-specific fact in long-term memory.

    Use this tool when the user explicitly asks to remember something,
    save something, store something, or says a durable preference.

    Examples:
    - remember my name is Sam
    - remember my favorite language is Python
    - save my preferred cloud provider as AWS
    """
    memory = _load_memory()
    memory[key] = value
    _save_memory(memory)
    return f"Saved memory: {key} = {value}"


def recall_fact(key: str) -> str:
    """
    Retrieve a specific fact from long-term memory.

    Use this tool when the user asks what you remember about a specific key,
    such as name, favorite_language, preferred_cloud, project, or preference.
    """
    memory = _load_memory()

    if key not in memory:
        return f"No memory found for key: {key}"

    return f"{key} = {memory[key]}"


def list_memories() -> dict[str, Any]:
    """
    List all saved long-term memory facts.

    Use this tool when the user asks:
    - what do you remember?
    - list my saved facts
    - show memory
    """
    return _load_memory()


root_agent = Agent(
    name="agentv8",
    model="openai/gpt-4.1-nano",
    description="ADK agent with explicit long-term memory using a JSON file.",
    instruction="""
You are Agent V8.

You have explicit long-term memory tools.

Important behavior:
- Use remember_fact when the user explicitly asks you to remember, save, or store durable information.
- Use recall_fact when the user asks about a specific saved memory.
- Use list_memories when the user asks what you remember.
- Do not store temporary conversation details unless the user clearly asks to remember them.
- When saving memory, choose simple snake_case keys such as:
  - name
  - favorite_language
  - preferred_cloud
  - current_project
- Keep responses concise.
""",
    tools=[remember_fact, recall_fact, list_memories],
)