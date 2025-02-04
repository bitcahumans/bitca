"""Run `pip install duckduckgo-search` to install dependencies."""

from bitca.agent import Agent
from bitca.models.deepseek import DeepSeek
from bitca.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=DeepSeek(id="deepseek-chat"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

agent.print_response("Whats happening in France?")
