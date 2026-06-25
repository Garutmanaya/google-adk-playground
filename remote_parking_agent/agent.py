from google.adk.agents.llm_agent import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a


MODEL_NAME = "openai/gpt-4.1-nano"



from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")



root_agent = Agent(
    name="remote_parking_agent",
    model=MODEL_NAME,
    description="Remote A2A parking specialist agent.",
    instruction="""
You are a remote Parking Specialist Agent.

You help with smart parking questions.

You can provide:
- parking availability assumptions
- pricing suggestions
- enforcement risk
- walking distance tradeoffs
- simple recommendation

Important:
- Use mock/demo data only.
- Clearly say data is demo data.
- Keep responses concise.
"""
)


a2a_app = to_a2a(root_agent, port=10001)
