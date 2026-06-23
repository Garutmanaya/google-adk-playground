from pathlib import Path
from google.adk.agents.llm_agent import Agent

DOCS_DIR = Path(__file__).parent / "docs"


def search_local_docs(query: str) -> str:
    """
    Search local knowledge documents for information related to the user's query.

    Use this tool when the user asks about:
    - ADK notes
    - AWS notes
    - project documentation
    - internal knowledge
    - anything that may be answered from local docs
    """
    if not DOCS_DIR.exists():
        return "No docs directory found."

    query_words = set(query.lower().split())
    results: list[tuple[int, str, str]] = []

    for file_path in DOCS_DIR.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

        for paragraph in paragraphs:
            paragraph_words = set(paragraph.lower().split())
            score = len(query_words.intersection(paragraph_words))

            if score > 0:
                results.append((score, file_path.name, paragraph))

    if not results:
        return "No relevant document content found."

    results.sort(reverse=True, key=lambda x: x[0])

    top_results = results[:3]

    response = []
    for score, filename, paragraph in top_results:
        response.append(
            f"Source: {filename}\n"
            f"Relevance Score: {score}\n"
            f"Content: {paragraph}"
        )

    return "\n\n---\n\n".join(response)


root_agent = Agent(
    name="agentv9",
    model="openai/gpt-4.1-nano",
    description="Simple RAG agent using local text documents.",
    instruction="""
You are Agent V9.

You are a RAG-first agent with LLM fallback.

Behavior:
- First use search_local_docs when the user asks about ADK, AWS, project notes, or internal docs.
- If search_local_docs returns useful content, answer mainly from the retrieved documents.
- Mention the source filename when using retrieved content.
- If search_local_docs returns "No relevant document content found" or insufficient information, answer using your own general LLM knowledge.
- When using fallback knowledge, clearly say: "I could not find this in local docs, so here is a general answer."
- Do not pretend fallback answers came from local docs.
- Keep answers concise and practical.
""",
    tools=[search_local_docs],
)