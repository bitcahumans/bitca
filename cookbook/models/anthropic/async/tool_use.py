"""
Async example using Claude with tool calls.
"""

import asyncio

from bitca.agent.agent import Agent
from bitca.models.anthropic import Claude
from bitca.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Claude(id="claude-3-5-sonnet-20240620"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))
