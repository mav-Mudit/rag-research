from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()


CHROMA_DIR = "chroma_db"


def load_vector_store():
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings,
    )

    return vector_store

def retrieve_documents(query, k=3):
    vector_store = load_vector_store()

    documents = vector_store.similarity_search(
        query,
        k=k,
    )

    return documents

if __name__ == "__main__":
    query = "What is Retrieval-Augmented Generation?"

    documents = retrieve_documents(query)

    for i, document in enumerate(documents, start=1):
        print(f"\n{'=' * 60}")
        print(f"RESULT {i}")
        print(f"{'=' * 60}")

        print("\nMetadata:")
        print(document.metadata)

        print("\nContent:")
        print(document.page_content)