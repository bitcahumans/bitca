# install lancedb - `pip install lancedb`

from bitca.agent import Agent
from bitca.knowledge.pdf_url import PDFUrlKnowledgeBase
from bitca.vectordb.lancedb import LanceDb

# Initialize LanceDB
# By default, it stores data in /tmp/lancedb
vector_db = LanceDb(
    table_name="recipes",
    uri="/tmp/lancedb",  # You can change this path to store data elsewhere
)

# Create knowledge base
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=vector_db,
)

knowledge_base.load(recreate=False)  # Comment out after first run

# Create and use the agent
agent = Agent(knowledge=knowledge_base, show_tool_calls=True)
agent.print_response("How to make Tom Kha Gai", markdown=True)
