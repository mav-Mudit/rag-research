import json
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


load_dotenv()

EVALUATION_DIR = Path(__file__).parent
INPUT_FILE = EVALUATION_DIR / "retrieval_dataset.csv"
OUTPUT_FILE = EVALUATION_DIR / "llm_relevance_judgments.csv"


llm = ChatOpenAI(
    model="gpt-5.6",
    temperature=0,
)


PROMPT = ChatPromptTemplate.from_template(
    """
You are evaluating the relevance of a retrieved passage for a research-paper
question.

Your task is to determine whether the passage provides useful evidence for
answering the question.

Judge the passage based on the SPECIFIC question, not merely whether it is
about the same general topic.

Relevant (1):
- The passage directly answers the question, OR
- The passage provides meaningful evidence or supporting information needed
  to answer the question.

Not relevant (0):
- The passage is only generally related to the topic.
- The passage discusses a different aspect of the paper.
- The passage would not provide useful evidence for answering the question.

Do not consider:
- Which retrieval system produced the passage.
- The position/rank of the passage.
- Whether the final generated answer was correct.

Return ONLY valid JSON in this exact format:

{{
  "relevant": 0 or 1,
  "confidence": "high" or "medium" or "low",
  "reason": "short explanation"
}}

Question:
{question}

Retrieved passage:
{passage}
"""
)


def load_existing_judgments():
    if not OUTPUT_FILE.exists():
        return {}

    judgments = pd.read_csv(OUTPUT_FILE)

    return {
        (row["question_id"], row["passage"]): row
        for _, row in judgments.iterrows()
    }


def judge_passage(question, passage):
    chain = PROMPT | llm

    response = chain.invoke(
        {
            "question": question,
            "passage": passage,
        }
    )

    content = response.content.strip()

    # Handle possible markdown code fences.
    if content.startswith("```"):
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

    return json.loads(content)


def main():
    df = pd.read_csv(INPUT_FILE)

    # Only judge each unique question + passage once.
    unique = df.drop_duplicates(
        subset=["question_id", "passage"]
    ).copy()

    existing = load_existing_judgments()

    print(f"Total retrieval results: {len(df)}")
    print(f"Unique passages to judge: {len(unique)}")
    print(f"Already judged: {len(existing)}")
    print()

    results = []

    for index, row in unique.iterrows():
        key = (row["question_id"], row["passage"])

        if key in existing:
            results.append(existing[key].to_dict())
            continue

        print(
            f"Judging passage {index + 1}/{len(unique)} "
            f"(Q{row['question_id']})..."
        )

        try:
            judgment = judge_passage(
                row["question"],
                row["passage"],
            )

            result = {
                "question_id": row["question_id"],
                "question": row["question"],
                "paper": row["paper"],
                "page": row["page"],
                "passage": row["passage"],
                "relevant": int(judgment["relevant"]),
                "confidence": judgment["confidence"],
                "reason": judgment["reason"],
            }

            results.append(result)

            # Save after every judgment.
            pd.DataFrame(results).to_csv(
                OUTPUT_FILE,
                index=False,
                encoding="utf-8",
            )

            print(
                f"  → relevant={result['relevant']} "
                f"({result['confidence']})"
            )

        except Exception as error:
            print(f"  ERROR: {error}")
            print("  Skipping this passage.")

    pd.DataFrame(results).to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8",
    )

    print()
    print(f"Saved judgments to: {OUTPUT_FILE}")
    print(f"Judgments completed: {len(results)}")


if __name__ == "__main__":
    main()