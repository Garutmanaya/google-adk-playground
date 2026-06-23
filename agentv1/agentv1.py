
import os
from google.adk.agents.llm_agent import Agent

AGENT_VERSION = "2.0"
MODEL_NAME = "openai/gpt-4.1-nano"
ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
PROVIDER = "OpenAI"

runtime_context = f"""
Runtime Metadata:
- Agent Version: {AGENT_VERSION}
- Current Model: {MODEL_NAME}
- Environment: {ENVIRONMENT}
- Provider: {PROVIDER}
"""

root_agent = Agent(
    name="agentv2",
    model=MODEL_NAME,
    description="ADK agent with runtime metadata awareness.",
    instruction=f"""
You are Agent V2.

{runtime_context}

Behavior Rules:
- Answer clearly and concisely.
- You are aware of your runtime metadata.
- If user asks about model/version/provider/environment, answer using metadata above.
- For technical questions, provide practical examples.
"""
)