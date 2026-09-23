"""Return model output validated by Pydantic, not free-form text."""
from typing import Literal

from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class BugTriage(BaseModel):
    severity: Literal["low", "medium", "high", "critical"]
    summary: str = Field(description="One-sentence problem summary")
    reproduction_steps: list[str]
    suggested_owner: Literal["frontend", "backend", "devops", "qa"]


agent = Agent(
    model=Groq(id="qwen/qwen3.6-27b"),
    response_model=BugTriage,
    instructions="Analyze a bug report. Do not invent facts not found in the report.",
)

response = agent.run("Login returns 500 after clicking Submit. It affects every user.")
print(response.content)
