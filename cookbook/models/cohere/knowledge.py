"""Run `pip install duckduckgo-search sqlalchemy pgvector pypdf openai cohere` to install dependencies."""

from bitca.agent import Agent
from bitca.knowledge.pdf_url import PDFUrlKnowledgeBase
from bitca.models.cohere import Cohere
from bitca.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(table_name="recipes", db_url=db_url),
)
knowledge_base.load(recreate=False)  # Comment out after first run

agent = Agent(
    model=Cohere(id="command-r-08-2024"),
    knowledge=knowledge_base,
    show_tool_calls=True,
)
agent.print_response("How to make Thai curry?", markdown=True)
