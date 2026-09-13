from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

from chunk import split_documents
from ingest import load_all_papers


load_dotenv()


def create_embeddings(chunks):
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vectors = embeddings.embed_documents(
        [chunk.page_content for chunk in chunks]
    )

    return vectors


if __name__ == "__main__":
    documents = load_all_papers()
    chunks = split_documents(documents)

    vectors = create_embeddings(chunks)

    print(f"Number of chunks: {len(chunks)}")
    print(f"Number of vectors: {len(vectors)}")
    print(f"Dimensions of first vector: {len(vectors[0])}")

    print("\n--- FIRST VECTOR ---")
    print(vectors[0][:10])