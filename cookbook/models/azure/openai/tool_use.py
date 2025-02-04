"""Run `pip install duckduckgo-search` to install dependencies."""

from bitca.agent import Agent
from bitca.models.azure import AzureOpenAI
from bitca.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=AzureOpenAI(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)

agent.print_response("Whats happening in France?", stream=True)
