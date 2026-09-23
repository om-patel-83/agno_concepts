"""Give an agent deliberate create/read/update/delete access to memories."""
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.groq import Groq
from agno.tools.memory import MemoryTools
from dotenv import load_dotenv

load_dotenv()

db = SqliteDb(db_file="tmp/memory-tools.db")
agent = Agent(
    model=Groq(id="qwen/qwen3.6-27b"),
    tools=[MemoryTools(db=db)],
    instructions="Store only durable preferences. Ask before deleting a memory.",
)
agent.print_response("Remember that I prefer PostgreSQL for production projects.", user_id="sumit@example.com")
