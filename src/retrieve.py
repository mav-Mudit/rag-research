from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()


CHROMA_DIR = "chroma_db"
PAPER_KEYWORDS = {
    "rag": "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
    "retrieval-augmented generation": "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
    "bert": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
    "gpt-3": "Language Models are Few-Shot Learners",
    "t5": "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer",
    "lora": "LoRA: Low-Rank Adaptation of Large Language Models",
    "react": "ReAct: Synergizing Reasoning and Acting in Language Models",
    "chain-of-thought": "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
}

def load_vector_store():
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings,
    )

    return vector_store

# C3
def retrieve_documents(query, k=3):
    vector_store = load_vector_store()

    documents = vector_store.similarity_search(
        query,
        k=k,
    )

    return documents

# M1
# def retrieve_documents(query, k=3):
#     vector_store = load_vector_store()

#     filter_value = None

#     for keyword, paper_title in PAPER_KEYWORDS.items():
#         if keyword in query.lower():
#             filter_value = paper_title
#             break

#     if filter_value:
#         documents = vector_store.similarity_search(
#             query,
#             k=k,
#             filter={"paper_title": filter_value},
#         )
#     else:
#         documents = vector_store.similarity_search(
#             query,
#             k=k,
#         )

#     return documents

# M2
# def retrieve_documents_m2(query, k=3):
#     vector_store = load_vector_store()

#     results = vector_store.similarity_search_with_score(
#         query,
#         k=10,
#     )

#     for keyword, paper_title in PAPER_KEYWORDS.items():
#         if keyword in query.lower():
#             results = [
#                 (
#                     document,
#                     score - 0.1
#                     if document.metadata.get("paper_title") == paper_title
#                     else score,
#                 )
#                 for document, score in results
#             ]
#             break

#     results.sort(key=lambda x: x[1])

#     return [document for document, score in results[:k]]

if __name__ == "__main__":
    query = "According to the LoRA paper, how does LoRA exploit the low-rank assumption?"

    documents = retrieve_documents(query)

    for i, document in enumerate(documents, start=1):
        print(f"\n{'=' * 60}")
        print(f"RESULT {i}")
        print(f"{'=' * 60}")

        print("\nMetadata:")
        print(document.metadata)

        print("\nContent:")
        print(document.page_content)