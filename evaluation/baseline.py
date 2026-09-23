import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.generate import rag_chain
from src.retrieve import rerank_documents as retrieve_documents


QUESTIONS = [
    "What problem does Retrieval-Augmented Generation aim to address, and why can a language model's parametric knowledge be insufficient?",
    "How does RAG combine parametric and non-parametric memory during generation?",
    "How does RAG differ from a traditional language model that relies only on its parameters, particularly when dealing with knowledge-intensive tasks?",
    "What are the main differences between RAG-Sequence and RAG-Token, and how do they affect the documents used during generation?",
    "How does GPT-3 demonstrate that large language models can perform tasks from natural-language descriptions and a few examples without gradient-based updates?",
    "How does T5's text-to-text formulation allow the same model and training framework to be applied to different NLP tasks?",
    "Why does LoRA argue that the changes required when adapting a large language model have low intrinsic rank, and how does its approach exploit this observation?",
    "How does ReAct combine reasoning and acting, and why does this provide an advantage over approaches that perform reasoning without interacting with external environments?",
    "What does Chain-of-Thought prompting reveal about the relationship between model scale, intermediate reasoning steps, and performance on complex reasoning tasks?",
    "What limitations of RAG are identified by the authors, and how do these limitations affect the reliability or usefulness of the generated answers?",
]


RESULTS_FILE = Path("evaluation/baseline_results.md")


def run_baseline():
    results = []

    for i, question in enumerate(QUESTIONS, start=1):
        print(f"\nRunning question {i}/{len(QUESTIONS)}...")
        print(question)

        documents = retrieve_documents(question, k=3)
        answer = rag_chain.invoke(question)

        results.append(
            {
                "number": i,
                "question": question,
                "answer": answer,
                "documents": documents,
            }
        )

    return results


def save_results(results):
    with RESULTS_FILE.open("w", encoding="utf-8") as file:
        file.write("# V1 Baseline Evaluation Results\n\n")
        file.write(
            "These results were generated using the fixed V1 configuration "
            "and evaluation questions.\n\n"
        )

        for result in results:
            file.write(f"## Question {result['number']}\n\n")
            file.write(f"**Question:** {result['question']}\n\n")

            file.write("### Retrieved Sources\n\n")

            for source_number, document in enumerate(
                result["documents"],
                start=1,
            ):
                paper_title = document.metadata.get(
                    "paper_title",
                    "Unknown paper",
                )
                page = document.metadata.get(
                    "page",
                    "Unknown page",
                )

                file.write(
                    f"**Source {source_number}:** "
                    f"{paper_title}, page {page}\n\n"
                )
                file.write(f"> {document.page_content}\n\n")

            file.write("### Generated Answer\n\n")
            file.write(f"{result['answer']}\n\n")
            file.write("---\n\n")


if __name__ == "__main__":
    baseline_results = run_baseline()
    save_results(baseline_results)

    print("\nBaseline evaluation complete.")
    print(f"Results saved to: {RESULTS_FILE}")