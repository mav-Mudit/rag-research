from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

from chunk import split_documents
from ingest import load_all_papers


load_dotenv()


CHROMA_DIR = "chroma_db"


def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
    )

    return vector_store


if __name__ == "__main__":
    documents = load_all_papers()
    chunks = split_documents(documents)

    vector_store = create_vector_store(chunks)

    print(f"Stored {len(chunks)} chunks in Chroma.")