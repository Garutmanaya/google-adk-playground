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

You are a simple RAG agent.

Important behavior:
- Use search_local_docs when the user asks questions that may be answered from local documents.
- Base your answer mainly on retrieved document content.
- If documents do not contain enough information, clearly say so.
- Mention the source filename when using retrieved information.
- Do not invent facts that are not in the retrieved context.
- Keep answers concise and practical.
""",
    tools=[search_local_docs],
)