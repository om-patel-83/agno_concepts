"""Persist one conversation session for one user using SQLite."""

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

db = SqliteDb(db_file="tmp/sessions.db")

agent = Agent(
    model=Groq(id="qwen/qwen3.6-27b"),
    db=db,
)

# In a real app:
# user_id = logged-in user's unique ID
# session_id = current chat thread, support ticket, or conversation ID
user_id = "sumit@example.com"
session_id = "support-ticket-1042"

# Creates/runs the session and stores it in SQLite.
agent.print_response(
    "Create a short summary for ticket 1042.",
    user_id=user_id,
    session_id=session_id,
)

# get_session() fetches ONE specific session.
print("\nStored session:")

session = agent.get_session(
    session_id=session_id,
    user_id=user_id,
)

print(session)