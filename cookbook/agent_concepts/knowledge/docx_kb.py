from pathlib import Path

from bitca.agent import Agent
from bitca.knowledge.docx import DocxKnowledgeBase
from bitca.vectordb.pgvector import PgVector

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

# Create a knowledge base with the DOCX files from the data/docs directory
knowledge_base = DocxKnowledgeBase(
    path=Path("data/docs"),
    vector_db=PgVector(
        table_name="docx_documents",
        db_url=db_url,
    ),
)
# Load the knowledge base
knowledge_base.load(recreate=False)

# Create an agent with the knowledge base
agent = Agent(
    knowledge=knowledge_base,
    search_knowledge=True,
)

# Ask the agent about the knowledge base
agent.print_response("Ask me about something from the knowledge base", markdown=True)
