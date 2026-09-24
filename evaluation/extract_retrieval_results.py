from pathlib import Path
import csv
import re


EVALUATION_DIR = Path(__file__).parent

RESULT_FILES = {
    "V1": "v1_baseline_results.md",
    "C3": "v2_c3_results.md",
    "BM25": "bm25_results.md",
    "H1": "hybrid1_results.md",
    "H2": "hybrid2_results.md",
    "RRF": "RRF_results.md",
    "Reranker": "Ranker_results.md",
    "QT": "query_transformation_results.md",
}

OUTPUT_FILE = EVALUATION_DIR / "retrieval_dataset.csv"


def extract_results(configuration, file_path):
    text = file_path.read_text(encoding="utf-8")

    questions = re.split(r"^## Question \d+\s*$", text, flags=re.MULTILINE)

    results = []

    for question_block in questions[1:]:
        question_match = re.search(
            r"\*\*Question:\*\*\s*(.+)",
            question_block,
        )

        if not question_match:
            continue

        question = question_match.group(1).strip()

        source_pattern = re.compile(
            r"\*\*Source (\d+):\*\*\s*(.+?), page (\d+)\s*\n\n"
            r">\s*(.*?)(?=\n\n\*\*Source |\n\n### Generated Answer)",
            re.DOTALL,
        )

        sources = source_pattern.findall(question_block)

        for rank, paper, page, passage in sources:
            passage = passage.strip()
            passage = re.sub(r"\n+", " ", passage)

            results.append(
                {
                    "question_id": None,
                    "configuration": configuration,
                    "rank": int(rank),
                    "paper": paper.strip(),
                    "page": int(page),
                    "question": question,
                    "passage": passage,
                }
            )

    return results


def main():
    all_results = []
    question_counter = {}

    for configuration, filename in RESULT_FILES.items():
        file_path = EVALUATION_DIR / filename

        if not file_path.exists():
            print(f"WARNING: Missing file: {file_path}")
            continue

        results = extract_results(configuration, file_path)

        for result in results:
            question = result["question"]

            if question not in question_counter:
                question_counter[question] = len(question_counter) + 1

            result["question_id"] = question_counter[question]

        all_results.extend(results)

        print(
            f"{configuration}: "
            f"{len(results)} retrieved passages"
        )

    fieldnames = [
        "question_id",
        "configuration",
        "rank",
        "paper",
        "page",
        "question",
        "passage",
    ]

    with OUTPUT_FILE.open(
        "w",
        encoding="utf-8",
        newline="",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
        )

        writer.writeheader()
        writer.writerows(all_results)

    print()
    print(f"Saved dataset to: {OUTPUT_FILE}")
    print(f"Total rows: {len(all_results)}")


if __name__ == "__main__":
    main()