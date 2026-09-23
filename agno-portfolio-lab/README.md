# Agno Portfolio Lab

A practical, topic-by-topic collection of **Agno v3** examples. Each folder is independently runnable and demonstrates one production-relevant agent capability.

## What this proves

- You can build agents with instructions, structured output and function tools.
- You understand the difference between **storage, session history, user memory and knowledge/RAG**.
- You can connect an agent to MCP servers and persist state using SQLite.
- You can progress from a simple agent to a knowledge-enabled assistant.

## Project map

| Folder | Topic | Key concept |
|---|---|---|
| `01_agent_basics` | Agent and instructions | Role, constraints and response style |
| `02_structured_output` | Typed responses | Pydantic response schema |
| `03_tool_calling` | Custom function tools | Model-selected tool calls |
| `04_storage_and_sessions` | Persistent sessions | `db`, `session_id`, `user_id` |
| `05_chat_history` | Multi-turn context | `add_history_to_context` |
| `06_memory` | Cross-session preferences | agentic and automatic memory |
| `07_memory_tools` | Memory CRUD tools | explicit memory management |
| `08_knowledge_rag` | Agentic RAG | vector search with LanceDB |
| `09_traditional_rag` | Retrieval before model | deterministic context injection |
| `10_mcp` | Model Context Protocol | remote and local MCP servers |
| `11_capstone` | Portfolio project | support assistant architecture |

## Quick start

```bash
uv venv --python 3.12
source .venv/bin/activate                 # Windows: .venv\\Scripts\\activate
uv pip install -r requirements.txt
cp .env.example .env
```

Add your free Groq key as `GROQ_API_KEY` to `.env`, then run an example from the repository root:

```bash
python 01_agent_basics/main.py
python 03_tool_calling/main.py
```

## Free model setup

All agent examples use Groq's `llama-3.3-70b-versatile` model through `GROQ_API_KEY`.
This avoids OpenAI API charges, although Groq still applies its account rate limits.

The two RAG modules need embeddings, which Groq does not provide. They use a free local
Ollama embedding model instead. Install Ollama and run this once before RAG examples:

```bash
ollama pull mxbai-embed-large
```

## Notes for reviewers

- Examples use `Groq(id="llama-3.3-70b-versatile")`, Agno's current Groq model class.
- SQLite is intentionally used for local demos. Replace it with `PostgresDb` in production.
- The RAG examples use local Ollama embeddings (`mxbai-embed-large`, 1024 dimensions).
- `10_mcp` is async because MCP connections must be opened and closed safely.

## Suggested portfolio description

> Built a modular Agno AI agent lab covering prompt instructions, Pydantic structured outputs, custom tool calling, SQLite-backed sessions and chat history, cross-session user memory, explicit memory CRUD, LanceDB RAG, and MCP integrations. Applied the modules in a production-style support assistant design with clear state and retrieval boundaries.

## References

The patterns follow the current official [Agno documentation](https://docs.agno.com/). Pin the package versions in `requirements.txt` before publishing a production deployment, as AI SDK APIs evolve quickly.
