from google.adk.agents.llm_agent import Agent

MODEL_NAME = "openai/gpt-4.1-nano"

planner_agent = Agent(
    name="planner_agent",
    model=MODEL_NAME,
    description="Creates plans, task breakdowns, milestones, and architecture steps.",
    instruction="You are Planner Agent. Create concise plans only."
)

executor_agent = Agent(
    name="executor_agent",
    model=MODEL_NAME,
    description="Produces implementation details, code, configs, and concrete solutions.",
    instruction="You are Executor Agent. Produce the main solution."
)

validator_agent = Agent(
    name="validator_agent",
    model=MODEL_NAME,
    description="Reviews existing plans, code, designs, and solutions for risks or gaps.",
    instruction="You are Validator Agent. Review and identify issues, risks, and improvements."
)

root_agent = Agent(
    name="agentv13",
    model=MODEL_NAME,
    description="Conditional supervisor that chooses which sub-agents are needed.",
    instruction="""
You are Agent V13, a conditional supervisor.

Unlike a router, you may use one or more sub-agents.

Decision rules:
- For simple explanation questions, answer directly.
- For planning/design questions, use planner_agent.
- For implementation/code/config questions, use executor_agent.
- For review/validation/risk questions, use validator_agent.
- For complex build requests, use planner_agent then executor_agent.
- For complex build-and-review requests, use planner_agent, executor_agent, then validator_agent.
- Skip agents that are not needed.

Important:
- Do not call every sub-agent by default.
- Choose only the agents needed for the user request.
- Combine outputs into one final response.
""",
    sub_agents=[
        planner_agent,
        executor_agent,
        validator_agent,
    ],
)
