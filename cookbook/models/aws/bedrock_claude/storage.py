"""Run `pip install duckduckgo-search sqlalchemy anthropic` to install dependencies."""

from bitca.agent import Agent
from bitca.models.aws.claude import Claude
from bitca.storage.agent.postgres import PostgresAgentStorage
from bitca.tools.duckduckgo import DuckDuckGoTools

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

agent = Agent(
    model=Claude(id="anthropic.claude-3-5-sonnet-20240620-v1:0"),
    storage=PostgresAgentStorage(table_name="agent_sessions", db_url=db_url),
    tools=[DuckDuckGoTools()],
    add_history_to_messages=True,
)
agent.print_response("How many people live in Canada?")
agent.print_response("What is their national anthem called?")
