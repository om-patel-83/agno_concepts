"""Add bounded earlier messages from the SAME session to each model call."""
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="qwen/qwen3.6-27b"),
    db=SqliteDb(db_file="tmp/history.db"),
    add_history_to_context=True,
    num_history_runs=3,
)

session_id = "onboarding-chat"
agent.print_response("My preferred stack is Python and FastAPI.", session_id=session_id)
agent.print_response("What stack do I prefer?", session_id=session_id)

# For a UI, audit log or export:
print(agent.get_chat_history(session_id=session_id))
