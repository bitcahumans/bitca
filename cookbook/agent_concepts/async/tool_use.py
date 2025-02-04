import asyncio

from bitca.agent import Agent
from bitca.models.openai import OpenAIChat
from bitca.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
)
asyncio.run(agent.aprint_response("Whats happening in UK and in USA?"))
