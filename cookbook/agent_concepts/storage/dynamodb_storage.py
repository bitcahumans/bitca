"""Run `pip install duckduckgo-search boto3 openai` to install dependencies."""

from bitca.agent import Agent
from bitca.storage.agent.dynamodb import DynamoDbAgentStorage
from bitca.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    storage=DynamoDbAgentStorage(table_name="agent_sessions", region_name="us-east-1"),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
    debug_mode=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
