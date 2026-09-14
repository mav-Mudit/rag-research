from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


PAPERS_DIR = Path("data/papers")

PAPER_METADATA = {
    "rag.pdf": {
        "title": "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    },
    "bert.pdf": {
        "title": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
    },
    "gpt-3.pdf": {
        "title": "Language Models are Few-Shot Learners"
    },
    "T5.pdf": {
        "title": "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"
    },
    "LoRA.pdf": {
        "title": "LoRA: Low-Rank Adaptation of Large Language Models"
    },
    "ReAct.pdf": {
        "title": "ReAct: Synergizing Reasoning and Acting in Language Models"
    },
    "cot.pdf": {
        "title": "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    },
}


def load_paper(pdf_path: Path):
    loader = PyPDFLoader(str(pdf_path))
    documents = loader.load()

    paper_info = PAPER_METADATA.get(
        pdf_path.name,
        {"title": pdf_path.stem},
    )

    for document in documents:
        document.metadata["paper_title"] = paper_info["title"]
        document.metadata["source"] = pdf_path.name
        document.metadata["page"] = document.metadata["page"] + 1

    return documents


def load_all_papers():
    documents = []

    for pdf_path in PAPERS_DIR.glob("*.pdf"):
        paper_documents = load_paper(pdf_path)
        documents.extend(paper_documents)

    return documents


if __name__ == "__main__":
    documents = load_all_papers()

    print(f"Total pages loaded: {len(documents)}")

    for document in documents[:2]:
        print("\n--- PAGE ---")
        print(document.page_content[:500])

        print("\n--- METADATA ---")
        print(document.metadata)