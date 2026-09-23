"""Traditional RAG: retrieve first, then pass chosen documents to the model."""
from agno.agent import Agent
from agno.knowledge.embedder.ollama import OllamaEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.models.groq import Groq
from agno.vectordb.lancedb import LanceDb, SearchType
from dotenv import load_dotenv

load_dotenv()

knowledge = Knowledge(
    vector_db=LanceDb(
        table_name="company_handbook", uri="tmp/lancedb", search_type=SearchType.vector,
        embedder=OllamaEmbedder(id="mxbai-embed-large", dimensions=1024),
    )
)

question = "Summarize the chicken and galangal recipe."
documents = knowledge.search(question, limit=3)
context = "\n\n".join(document.content for document in documents)

agent = Agent(model=Groq(id="qwen/qwen3.6-27b"), instructions="Answer only from the supplied context.")
agent.print_response(f"Context:\n{context}\n\nQuestion: {question}", stream=True)
