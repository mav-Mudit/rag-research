from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_openai import ChatOpenAI
from src.retrieve import retrieve_documents

load_dotenv()


llm = ChatOpenAI(
    model="gpt-5-mini",
    temperature=0,
)


prompt = ChatPromptTemplate.from_template(
    """
Answer the question using only the provided context.

CITATION RULES:
- Use the provided context as your source of information.
- Cite claims using [Source 1], [Source 2], etc.
- Only use source numbers that actually exist in the context.
- If the context does not contain enough information, say so.

Context:
{context}

Question:
{question}

Answer:
"""
)


def format_documents(documents):
    context_parts = []

    for i, document in enumerate(documents, start=1):
        source = document.metadata.get(
            "paper_title",
            "Unknown paper",
        )
        page = document.metadata.get(
            "page",
            "Unknown page",
        )

        context_parts.append(
            f"[Source {i}: {source}, page {page}]\n"
            f"{document.page_content}"
        )

    return "\n\n".join(context_parts)


def retrieve_with_documents(query):
    return retrieve_documents(query, k=3)


rag_chain = (
    {
        "context": RunnableLambda(retrieve_with_documents)
        | RunnableLambda(format_documents),
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
    | StrOutputParser()
)


if __name__ == "__main__":
    query = "What is Retrieval-Augmented Generation?"

    answer = rag_chain.invoke(query)

    print("\n--- ANSWER ---")
    print(answer)