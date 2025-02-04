"""Run `pip install duckduckgo-search` to install dependencies."""

from bitca.agent import Agent
from bitca.models.cohere import Cohere
from bitca.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Cohere(id="command-r-08-2024"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Whats happening in France?", stream=True)
