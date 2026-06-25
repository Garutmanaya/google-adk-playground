from google.adk.agents.llm_agent import Agent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent


MODEL_NAME = "openai/gpt-4.1-nano"


remote_parking_agent = RemoteA2aAgent(
    name="remote_parking_agent",
    description="Remote parking specialist exposed through A2A.",
    agent_card="http://localhost:10001/.well-known/agent-card.json",
)


root_agent = Agent(
    name="agentv19",
    model=MODEL_NAME,
    description="Coordinator agent that calls a remote parking agent using A2A.",
    instruction="""
You are Agent V19, an A2A coordinator.

You have access to a remote parking specialist agent through A2A.

Rules:
- For parking-related questions, delegate to remote_parking_agent.
- Use the remote response to produce the final answer.
- Do not pretend to have live parking data.
- Clearly mention that this is demo/mock data.
- Keep responses concise.
""",
    sub_agents=[
        remote_parking_agent,
    ],
)
