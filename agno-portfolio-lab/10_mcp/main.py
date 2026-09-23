"""Connect an Agno agent to a remote MCP server with a safe lifecycle."""
import asyncio

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.mcp import MCPTools
from dotenv import load_dotenv

load_dotenv()


async def main() -> None:
    mcp_tools = MCPTools(transport="streamable-http", url="https://docs.agno.com/mcp")
    await mcp_tools.connect()
    try:
        agent = Agent(
            model=Groq(id="qwen/qwen3.6-27b"),
            tools=[mcp_tools],
            instructions="Use MCP tools when they help. Clearly identify uncertain answers.",
        )
        await agent.aprint_response("What does Agno's MCP support provide?", stream=True)
    finally:
        await mcp_tools.close()


if __name__ == "__main__":
    asyncio.run(main())
