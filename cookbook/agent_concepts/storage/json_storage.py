"""Run `pip install duckduckgo-search openai` to install dependencies."""

from bitca.agent import Agent
from bitca.storage.agent.json import JsonAgentStorage
from bitca.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    storage=JsonAgentStorage(dir_path="tmp/agent_sessions_json"),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
