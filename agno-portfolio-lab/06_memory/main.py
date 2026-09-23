"""Persist useful user facts across sessions. Memory is NOT chat history."""
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

db = SqliteDb(db_file="tmp/memory.db")
agent = Agent(
    model=Groq(id="qwen/qwen3.6-27b"),
    db=db,
    update_memory_on_run=True,  # automatic: MemoryManager processes each non-empty input
    # Alternative: enable_agentic_memory=True lets the agent decide with a tool call.
)

user_id = "sumit@example.com"
agent.print_response("I prefer concise answers and use Python at work.", user_id=user_id, session_id="first-chat")
agent.print_response("How should you answer me?", user_id=user_id, session_id="new-chat")
print(agent.get_user_memories(user_id=user_id))
