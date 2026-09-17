from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.ingest import load_all_papers


CHUNK_SIZE = 1500
CHUNK_OVERLAP = 200


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    chunks = splitter.split_documents(documents)

    return chunks


if __name__ == "__main__":
    documents = load_all_papers()
    chunks = split_documents(documents)

    print(f"Number of pages: {len(documents)}")
    print(f"Number of chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks[:5]):
        print(f"\n--- CHUNK {i + 1} ---")
        print(chunk.page_content)

        print("\n--- METADATA ---")
        print(chunk.metadata)