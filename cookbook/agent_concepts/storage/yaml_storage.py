"""Run `pip install duckduckgo-search openai` to install dependencies."""

from bitca.agent import Agent
from bitca.storage.agent.yaml import YamlAgentStorage
from bitca.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    storage=YamlAgentStorage(dir_path="tmp/agent_sessions_yaml"),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
