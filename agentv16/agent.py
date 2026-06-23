from google.adk.agents.llm_agent import Agent


MODEL_NAME = "openai/gpt-4.1-nano"


def parking_availability_agent(location: str) -> str:
    """
    Remote-agent simulation: Parking Availability Agent.

    Use this tool when the coordinator needs parking availability
    for a city, garage, zone, or parking area.
    """
    return f"""
AGENT_RESPONSE: parking_availability_agent
Location: {location}
Available Spots:
- Garage A: 42 spots
- Garage B: 17 spots
- Street Zone C: 8 spots
Confidence: mock-data
"""


def parking_pricing_agent(location: str) -> str:
    """
    Remote-agent simulation: Parking Pricing Agent.

    Use this tool when the coordinator needs parking prices,
    dynamic pricing, or cost estimates.
    """
    return f"""
AGENT_RESPONSE: parking_pricing_agent
Location: {location}
Pricing:
- Garage A: $3/hour
- Garage B: $2/hour
- Street Zone C: $4/hour
Recommendation: Garage B is cheapest.
Confidence: mock-data
"""


def traffic_context_agent(location: str) -> str:
    """
    Remote-agent simulation: Traffic Context Agent.

    Use this tool when the coordinator needs traffic, congestion,
    walking distance, or route context.
    """
    return f"""
AGENT_RESPONSE: traffic_context_agent
Location: {location}
Traffic Context:
- Main Street: moderate congestion
- Garage A: 5 min walk to destination
- Garage B: 9 min walk to destination
- Street Zone C: 2 min walk but low availability
Confidence: mock-data
"""


def enforcement_risk_agent(location: str) -> str:
    """
    Remote-agent simulation: Enforcement Risk Agent.

    Use this tool when the coordinator needs parking rule,
    ticket risk, time limit, or enforcement information.
    """
    return f"""
AGENT_RESPONSE: enforcement_risk_agent
Location: {location}
Risk:
- Street Zone C has 1-hour limit
- Garage A has lowest ticket risk
- Garage B is safe for long parking
Confidence: mock-data
"""


root_agent = Agent(
    name="agentv16",
    model=MODEL_NAME,
    description="A2A-style smart parking coordinator using specialist agent tools.",
    instruction="""
You are Agent V16, an A2A-style coordinator agent.

You coordinate multiple specialist agents:
- parking_availability_agent
- parking_pricing_agent
- traffic_context_agent
- enforcement_risk_agent

Behavior:
- For smart parking questions, call the relevant specialist agents.
- For best parking recommendation, use availability, pricing, traffic, and enforcement risk.
- Combine specialist responses into one final recommendation.
- Mention that data is mock/demo data.
- Do not invent exact live availability beyond tool outputs.
- Keep the final answer concise.

This is a local simulation of A2A.
Each tool represents a remote specialist agent.
""",
    tools=[
        parking_availability_agent,
        parking_pricing_agent,
        traffic_context_agent,
        enforcement_risk_agent,
    ],
)
