from google.adk.agents.llm_agent import Agent
from google.adk.agents.sequential_agent import SequentialAgent


MODEL_NAME = "openai/gpt-4.1-nano"


planner_agent = Agent(
    name="planner_agent",
    model=MODEL_NAME,
    description="Creates a short plan for answering the user request.",
    instruction="""
You are a planning agent.

Given the user request, create a concise plan.
Do not write the final answer.
Return only the plan.
""",
)


writer_agent = Agent(
    name="writer_agent",
    model=MODEL_NAME,
    description="Writes the answer using the plan.",
    instruction="""
You are a writer agent.

Use the previous agent's plan and write a clear answer.
Keep the response practical and concise.
""",
)


reviewer_agent = Agent(
    name="reviewer_agent",
    model=MODEL_NAME,
    description="Reviews and improves the answer.",
    instruction="""
You are a reviewer agent.

Review the previous answer.
Improve clarity, remove unnecessary text, and return the final answer only.
""",
)


root_agent = SequentialAgent(
    name="agentv10",
    description="Sequential multi-agent workflow: planner, writer, reviewer.",
    sub_agents=[
        planner_agent,
        writer_agent,
        reviewer_agent,
    ],
)