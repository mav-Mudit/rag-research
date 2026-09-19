from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from rank_bm25 import BM25Okapi

from src.chunk import split_documents
from src.ingest import load_all_papers


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

def document_key(document):
    return (
        document.metadata.get("source"),
        document.metadata.get("page"),
        document.page_content,
    )

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


# BM25 — Lexical Retrieval
def load_bm25():
    documents = load_all_papers()
    chunks = split_documents(documents)

    tokenized_chunks = [
        chunk.page_content.lower().split()
        for chunk in chunks
    ]

    # This creates a BM25 search object.
    bm25 = BM25Okapi(tokenized_chunks)

    return bm25, chunks


def retrieve_documents_bm25(query, k=3):
    bm25, chunks = load_bm25()

    # Convert query into words
    tokenized_query = query.lower().split()

    # Get BM25 score for every chunk
    scores = bm25.get_scores(tokenized_query)

    # Get chunk indices sorted by score
    ranked_indices = sorted(
        range(len(scores)),
        key=lambda index: scores[index],
        reverse=True
    )

    # Take the top k chunks
    top_indices = ranked_indices[:k]

    # Get the actual chunks
    documents = []

    for index in top_indices:
        documents.append(chunks[index])

    return documents
def retrieve_documents_hybrid(query, k=3):
    vector_store = load_vector_store()

    # Semantic retrieval
    semantic_results = vector_store.similarity_search_with_score(
        query,
        k=10,
    )

    # BM25 retrieval
    bm25, chunks = load_bm25()

    tokenized_query = query.lower().split()

    bm25_scores = bm25.get_scores(tokenized_query)

    ranked_indices = sorted(
        range(len(bm25_scores)),
        key=lambda index: bm25_scores[index],
        reverse=True,
    )

    bm25_indices = ranked_indices[:10]

    # Normalize semantic distances
    semantic_scores = [
        (document, score)
        for document, score in semantic_results
    ]

    semantic_values = [
        score
        for document, score in semantic_scores
    ]

    semantic_min = min(semantic_values)
    semantic_max = max(semantic_values)

    if semantic_max == semantic_min:
        normalized_semantic = {
            document_key(document): 1.0
            for document, score in semantic_scores
        }
    else:
        normalized_semantic = {
            document_key(document): 1 - (
                (score - semantic_min)
                / (semantic_max - semantic_min)
            )
            for document, score in semantic_scores
        }

    # Normalize BM25 scores
    selected_bm25_scores = [
        bm25_scores[index]
        for index in bm25_indices
    ]

    bm25_min = min(selected_bm25_scores)
    bm25_max = max(selected_bm25_scores)

    if bm25_max == bm25_min:
        normalized_bm25 = {
            document_key(chunks[index]): 1.0
            for index in bm25_indices
        }
    else:
        normalized_bm25 = {
            document_key(chunks[index]): (
                (bm25_scores[index] - bm25_min)
                / (bm25_max - bm25_min)
            )
            for index in bm25_indices
        }

    # Combine semantic and BM25 scores
    combined_scores = {}
    documents = {}

    for document, score in semantic_scores:
        document_id = document_key(document)

        combined_scores[document_id] = (
            0.5 * normalized_semantic[document_id]
        )

        documents[document_id] = document

    for index in bm25_indices:
        document = chunks[index]
        document_id = document_key(document)

        bm25_score = normalized_bm25[document_id]

        combined_scores[document_id] = (
            combined_scores.get(document_id, 0)
            + 0.5 * bm25_score
        )

        documents[document_id] = document

    ranked_documents = sorted(
        combined_scores.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    return [
        documents[document_id]
        for document_id, score in ranked_documents[:k]
    ]

if __name__ == "__main__":
    query = "What are the limitations of Retrieval-Augmented Generation?"

    documents = retrieve_documents_bm25(query, k=3)

    for i, document in enumerate(documents, start=1):
        print(f"\n{'=' * 60}")
        print(f"RESULT {i}")
        print(f"{'=' * 60}")

        print("\nMetadata:")
        print(document.metadata)

        print("\nContent:")
        print(document.page_content)