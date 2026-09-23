"""A minimal agent with explicit instructions."""
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="Python Mentor",
    model=Groq(id="qwen/qwen3.6-27b"),
    instructions=[
        "You teach Python to a developer with 2 years of backend experience.",
        "Give a concise explanation followed by one safe code example.",
        "State assumptions when information is missing.",
    ],
    markdown=True,
)

agent.print_response("Explain when to use a Python generator.", stream=True)
