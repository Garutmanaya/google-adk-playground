from google.adk.agents.llm_agent import Agent

MODEL_NAME = "openai/gpt-4.1-nano"

root_agent = Agent(
    name="agentv20",
    model=MODEL_NAME,
    description="Streaming test agent.",
    instruction="""
You are Agent V20.

Give clear step-by-step answers.
For long answers, use short paragraphs.
"""
)
