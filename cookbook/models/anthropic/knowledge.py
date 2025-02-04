"""Run `pip install duckduckgo-search sqlalchemy pgvector pypdf anthropic openai` to install dependencies."""

from bitca.agent import Agent
from bitca.embedder.azure_openai import AzureOpenAIEmbedder
from bitca.knowledge.pdf_url import PDFUrlKnowledgeBase
from bitca.models.anthropic import Claude
from bitca.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    vector_db=PgVector(
        table_name="recipes",
        db_url=db_url,
        embedder=AzureOpenAIEmbedder(),
    ),
)
knowledge_base.load(recreate=False)  # Comment out after first run

agent = Agent(
    model=Claude(id="claude-3-5-sonnet-20241022"),
    knowledge=knowledge_base,
    show_tool_calls=True,
    debug_mode=True,
)
agent.print_response("How to make Thai curry?", markdown=True)
