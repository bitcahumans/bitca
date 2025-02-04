"""Run `pip install duckduckgo-search` to install dependencies."""

from bitca.agent import Agent
from bitca.models.fireworks import Fireworks
from bitca.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Fireworks(id="accounts/fireworks/models/llama-v3p1-405b-instruct"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response("Whats happening in France?", stream=True)
