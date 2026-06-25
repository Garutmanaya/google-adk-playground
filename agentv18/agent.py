from pathlib import Path

from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters


MODEL_NAME = "openai/gpt-4.1-nano"

WORKSPACE_DIR = Path(__file__).parent / "mcp_workspace"
WORKSPACE_DIR = (Path(__file__).parent / "mcp_workspace").resolve()

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info(f"WORKSPACE_DIR={WORKSPACE_DIR}")
logger.info(f"EXISTS={WORKSPACE_DIR.exists()}")
print("WORKSPACE_DIR =", WORKSPACE_DIR)
print("EXISTS =", WORKSPACE_DIR.exists())

root_agent = Agent(
    name="agentv18",
    model=MODEL_NAME,
    description="ADK agent using MCP filesystem tools.",
    instruction="""
You are Agent V18.

The MCP filesystem root is already mcp_workspace.

Rules:
- Do not use path mcp_workspace.
- Use "." to list files.
- Use file names directly, such as notes.txt.
- Never access parent directories.
""",
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="npx",
                args=[
                    "-y",
                    "@modelcontextprotocol/server-filesystem",
                    str(WORKSPACE_DIR),
                ],
            )
        )
    ],
)
