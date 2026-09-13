from langchain_text_splitters import RecursiveCharacterTextSplitter

from ingest import load_all_papers


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
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