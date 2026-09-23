"""Agentic RAG: the agent decides when to search its vector knowledge base."""
from agno.agent import Agent
from agno.knowledge.embedder.ollama import OllamaEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.models.groq import Groq
from agno.vectordb.lancedb import LanceDb, SearchType
from dotenv import load_dotenv

load_dotenv()

knowledge = Knowledge(
    vector_db=LanceDb(
        table_name="company_handbook",
        uri="tmp/lancedb",
        search_type=SearchType.vector,
        embedder=OllamaEmbedder(id="mxbai-embed-large", dimensions=1024),
    )
)

# Run once to index a document; then comment it out to avoid duplicate inserts.
# knowledge.insert(url="https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf")

agent = Agent(
    model=Groq(id="qwen/qwen3.6-27b"),
    knowledge=knowledge,
    search_knowledge=True,
    instructions="Use knowledge search for document-backed claims and cite uncertainty.",
)
agent.print_response("What information is available in the knowledge base?", stream=True)
