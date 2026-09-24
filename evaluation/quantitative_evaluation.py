import pandas as pd


# Load the two datasets
retrieval = pd.read_csv("evaluation/retrieval_dataset.csv")
judgments = pd.read_csv("evaluation/llm_relevance_judgments.csv")


print("Retrieval results:", len(retrieval))
print("LLM judgments:", len(judgments))


# Match each retrieved passage with its LLM judgment
results = retrieval.merge(
    judgments[["question_id", "passage", "relevant"]],
    on=["question_id", "passage"],
    how="left"
)


# Check that every passage got a judgment
print("Missing judgments:", results["relevant"].isna().sum())


# Calculate Precision@3
results["relevant"] = results["relevant"].astype(int)

precision = (
    results
    .groupby(["configuration", "question_id"])["relevant"]
    .mean()
    .reset_index(name="precision_at_3")
)


# Calculate average Precision@3 for each configuration
summary = (
    precision
    .groupby("configuration")["precision_at_3"]
    .mean()
    .sort_values(ascending=False)
)


print("\nPrecision@3 for each question:")
print(precision.to_string(index=False))


print("\nAverage Precision@3:")
print(summary)


# Save results
precision.to_csv(
    "evaluation/precision_per_question.csv",
    index=False
)

summary.to_csv(
    "evaluation/precision_summary.csv"
)

print("\nResults saved.")