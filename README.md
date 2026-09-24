# Research Paper RAG

A RAG application for asking questions about NLP and LLM research papers, with source-grounded answers and paper citations.

## Features

* PDF ingestion and text extraction
* Recursive text chunking
* OpenAI embeddings
* Chroma vector store
* Similarity-based retrieval
* LLM-generated answers using retrieved context
* Source-grounded answers with paper and page information
* Streamlit interface for querying research papers

## Tech Stack

* Python
* LangChain
* OpenAI API
* ChromaDB
* PyPDF
* Streamlit

## Architecture

```text
Research Papers (PDF)
        ↓
    PDF Loader
        ↓
     Chunking
        ↓
  OpenAI Embeddings
        ↓
    ChromaDB
        ↓
 Similarity Search
        ↓
 Top 10 Candidates
        ↓
  LLM Reranker
        ↓
 Top 3 Passages
        ↓
 Prompt + Context
        ↓
      LLM
        ↓
 Answer + Citations
```

## Project Structure

```text
rag-research/

├── data/
│   └── papers/

├── src/
│   ├── ingest.py
│   ├── chunk.py
│   ├── embed.py
│   ├── vector_store.py
│   ├── retrieve.py
│   └── generate.py

├── evaluation/
│   ├── baseline.py
│   ├── retrieval_dataset.csv
│   ├── llm_relevance_judgments.csv
│   └── precision_summary.csv

├── app.py
├── requirements.txt
└── README.md
```

## Setup

Create and activate a virtual environment, then install the dependencies:

```bash
uv pip install -r requirements.txt
```

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key
```

Add research papers to:

```text
data/papers/
```

Build the vector store:

```bash
uv run python src/vector_store.py
```

Run the Streamlit application:

```bash
uv run streamlit run app.py
```

## Baseline: V1 — Basic RAG

The V1 baseline implements a straightforward retrieval-augmented generation pipeline using a vector store and similarity-based retrieval.

### V1 Configuration

| Component        | Configuration                  |
| ---------------- | ------------------------------ |
| Papers           | 7                              |
| Pages            | 279                            |
| Chunks           | 1,167                          |
| Chunking         | RecursiveCharacterTextSplitter |
| Chunk size       | 1,000                          |
| Chunk overlap    | 150                            |
| Embedding model  | `text-embedding-3-small`       |
| Vector store     | ChromaDB                       |
| Retrieval        | Similarity search              |
| Top-k            | 3                              |
| Generation model | `gpt-5-mini`                   |
| Temperature      | 0                              |

### Baseline Questions

The following fixed questions were used to evaluate the V1 baseline and all subsequent retrieval experiments.

1. **Q1:** What problem does Retrieval-Augmented Generation aim to address, and why can a language model's parametric knowledge be insufficient?

2. **Q2:** How does RAG combine parametric and non-parametric memory during generation?

3. **Q3:** How does RAG differ from a traditional language model that relies only on its parameters, particularly when dealing with knowledge-intensive tasks?

4. **Q4:** What are the main differences between RAG-Sequence and RAG-Token, and how do they affect the documents used during generation?

5. **Q5:** How does GPT-3 demonstrate that large language models can perform tasks from natural-language descriptions and a few examples without gradient-based updates?

6. **Q6:** How does T5's text-to-text formulation allow the same model and training framework to be applied to different NLP tasks?

7. **Q7:** Why does LoRA argue that the changes required when adapting a large language model have low intrinsic rank, and how does its approach exploit this observation?

8. **Q8:** How does ReAct combine reasoning and acting, and why does this provide an advantage over approaches that perform reasoning without interacting with external environments?

9. **Q9:** What does Chain-of-Thought prompting reveal about the relationship between model scale, intermediate reasoning steps, and performance on complex reasoning tasks?

10. **Q10:** What limitations of RAG are identified by the authors, and how do these limitations affect the reliability or usefulness of the generated answers?

These questions remained unchanged throughout the experiments so that different retrieval approaches could be compared against the same baseline.

### V1 Evaluation Summary

The V1 baseline retrieved relevant information for most questions, but several questions exposed weaknesses in retrieval quality.

**Strong retrieval:** Q1, Q4, Q5, Q6, Q7, Q8, and Q9 generally retrieved passages directly addressing the questions.

**Areas for improvement:**

* **Q2:** The answer was good, but one retrieved source was less directly relevant to the specific question.
* **Q3:** The retrieved passages were relevant but somewhat redundant and did not provide the most focused evidence for the comparison.
* **Q10:** This was the clearest retrieval weakness. The retrieved passages focused more on RAG results and performance than directly discussing its limitations, causing the generated answer to rely partly on inference from the retrieved context.

The baseline demonstrated that a good generated answer does not necessarily imply good retrieval. The language model can sometimes fill gaps using its own parametric knowledge.

Therefore, V2 focused on improving the retrieval component while keeping the same 10 evaluation questions.

---

# V2 — Retrieval Experiments

The goal of V2 was to improve retrieval step by step and evaluate whether each technique actually improved retrieval quality.

The following approaches were evaluated:

1. Chunking
2. Metadata-aware retrieval
3. BM25
4. Hybrid search
5. Reciprocal Rank Fusion (RRF)
6. LLM reranking
7. Query transformation
8. Quantitative evaluation

Each experiment was evaluated against the strongest configuration from the previous stage.

## V2 Stage 1 — Chunking Experiment

The first V2 experiment evaluated whether changing chunk size and overlap could improve retrieval quality.

| Configuration | Chunk Size | Overlap |
| ------------- | ---------: | ------: |
| V1 baseline   |       1000 |     150 |
| C1            |        500 |     100 |
| C2            |        750 |     100 |
| C3            |       1500 |     200 |

The configurations were evaluated using the same 10 questions, with particular attention to the weaknesses identified in the V1 baseline.

### Result

**C3 (1500/200) was selected as the chunking baseline.**

C3 produced the strongest overall retrieval quality during this experiment, particularly improving Q3 and Q10 while maintaining strong retrieval for the remaining questions.

The selected C3 configuration was used as the fixed semantic retrieval baseline for the subsequent experiments.

## V2 Stage 2 — Metadata-Aware Retrieval

The second experiment evaluated whether document metadata could improve retrieval quality.

The C3 configuration was used as the baseline.

| Configuration | Approach                      |
| ------------- | ----------------------------- |
| M1            | Hard metadata filtering       |
| M2            | Metadata-based score boosting |

### M1 — Hard Metadata Filtering

If a query explicitly mentioned a known paper, retrieval was restricted to chunks from that paper. Otherwise, normal semantic retrieval was used.

This improved paper-level precision for queries mentioning a specific paper, but restricting retrieval to the correct paper did not consistently improve passage relevance.

### M2 — Metadata Score Boosting

M2 retrieved candidates using semantic similarity and applied a small ranking boost to chunks belonging to the paper explicitly mentioned in the query.

This was less restrictive than M1, but it also did not produce a consistent improvement over C3.

### Result

Neither metadata-aware retrieval strategy produced a meaningful improvement over C3 across the 10 evaluation questions.

## V2 Stage 3 — BM25 Retrieval

The third experiment evaluated BM25 as a standalone lexical retrieval method.

BM25 ranks chunks based on lexical overlap between the query and document text, providing a retrieval signal different from semantic embeddings.

BM25 performed well for terminology-heavy questions where important terms appeared explicitly in the relevant passages, such as LoRA, ReAct, and Chain-of-Thought.

However, it also produced irrelevant results for some questions. The clearest example was Q10, where none of the top three retrieved passages came from the RAG paper despite the question explicitly asking about RAG limitations.

### Result

BM25 was not selected as a standalone replacement for C3 semantic retrieval.

However, the experiment showed that BM25 could provide a complementary lexical retrieval signal, motivating the following hybrid-search experiments.

## V2 Stage 4 — Hybrid Search

The fourth experiment evaluated whether semantic retrieval and BM25 could be combined to improve retrieval quality.

C3 was used as the semantic baseline.

| Configuration | Semantic Retrieval | BM25 | Combination     |
| ------------- | -----------------: | ---: | --------------- |
| C3            |               100% |   0% | Semantic only   |
| BM25          |                 0% | 100% | Lexical only    |
| H1            |                70% |  30% | Weighted hybrid |
| H2            |                50% |  50% | Weighted hybrid |

For H1 and H2, the top 10 candidates from semantic retrieval and BM25 were combined using normalized scores, and the top 3 documents were returned.

### H1 — 70/30 Hybrid

H1 gave semantic retrieval more influence while allowing BM25 to contribute lexical matching.

It reduced some of the retrieval failures caused by BM25 alone, but did not consistently improve retrieval compared with C3.

### H2 — 50/50 Hybrid

H2 gave both retrieval methods equal influence.

It performed well across several questions and benefited from BM25's complementary lexical signal, but it also introduced less relevant passages in some cases.

### Result

The experiments showed three distinct behaviors:

* **C3:** consistent semantic retrieval quality
* **BM25:** useful lexical signal but noisy when used alone
* **H1/H2:** useful combinations, but no consistent qualitative improvement over C3

The weighted hybrid approaches were therefore retained as experimental baselines but not selected as the final retrieval strategy at this stage.

## V2 Stage 5 — Reciprocal Rank Fusion

The fifth experiment evaluated **Reciprocal Rank Fusion (RRF)** as an alternative way to combine semantic and lexical retrieval.

### RRF Approach

* Semantic retrieval returned the top 10 candidates.
* BM25 returned the top 10 candidates.
* Each document received an RRF score based on its rank.
* Scores were added for documents appearing in both rankings.
* The top 3 documents by combined RRF score were returned.

The standard RRF constant of 60 was used:

```text
RRF score = 1 / (60 + rank)
```

Unlike H1 and H2, RRF does not require semantic and BM25 scores to be normalized or manually weighted.

### Result

RRF was more robust than BM25 standalone and successfully combined semantic and lexical retrieval.

However, it did not consistently produce more focused retrieval than C3. Therefore, RRF was retained for comparison but was not selected as the final retrieval strategy.

Alternative RRF constants were not evaluated because the basic approach did not demonstrate a consistent advantage that justified further parameter tuning.

## V2 Stage 6 — LLM Reranking

The sixth experiment evaluated whether an LLM could improve the ordering of retrieved passages.

The C3 configuration was used as the initial retriever:

1. C3 semantic retrieval selected the top 10 candidate passages.
2. `gpt-5-mini` ranked the candidates according to their usefulness for answering the query.
3. The top 3 reranked passages were returned.

### Retrieval Pipeline

```text
Query
  ↓
C3 Semantic Retrieval
  ↓
Top 10 Candidates
  ↓
LLM Reranker (gpt-5-mini)
  ↓
Top 3 Passages
  ↓
Answer Generation
```

Qualitatively, reranking improved passage focus for several questions, including Q3, Q4, and Q5.

The reranker was retained for the final quantitative comparison rather than being selected or rejected based solely on qualitative inspection.

An important limitation of reranking is that it can only reorder the candidates provided by the initial retriever. It cannot recover a relevant passage that was not included in the candidate set.

## V2 Stage 7 — Query Transformation

The seventh experiment evaluated whether rewriting a user query could improve semantic retrieval.

The C3 configuration was used as the retrieval baseline.

```text
Original Query
      ↓
GPT-5-mini Query Transformation
      ↓
C3 Semantic Retrieval
      ↓
Top 3 Passages
```

The transformation prompt instructed the model to preserve the original meaning and intent, avoid adding information, and return only a rewritten question.

Query transformation improved retrieval focus for several questions, including Q3, Q4, and Q5.

However, other queries produced similar or less focused results compared with C3. The experiment therefore did not provide sufficient evidence to replace C3 with query transformation.

The implementation was retained for quantitative comparison.

---

# Quantitative Evaluation

The retrieval strategies were evaluated on the same fixed set of **10 questions**, with each configuration returning its top 3 passages.

Across the 8 evaluated configurations, this resulted in:

```text
8 configurations × 10 questions × 3 passages
= 240 retrieval occurrences
```

Some passages appeared in multiple configurations. After removing duplicate **question + passage** pairs, there were **94 unique passages** to judge.

### LLM-as-a-Judge

Each unique passage was evaluated by **gpt-5.6** for its usefulness in answering the corresponding question.

The judge received the question and retrieved passage and assigned a binary relevance label:

```text
1 = relevant evidence for answering the question
0 = not relevant
```

The judge also reported a confidence level (`high`, `medium`, or `low`) and a short explanation for each decision.

The resulting 94 relevance judgments were reused for matching occurrences across the 240 retrieval results.

This provided a consistent relevance signal while avoiding repeated evaluation of the same question-passage pair.

### Results

**Precision@3** was used as the primary retrieval metric:

```text
Precision@3 = relevant passages in top 3 / 3
```

| Configuration | Mean Precision@3 |
| ------------- | ---------------: |
| **Reranker**  |        **0.967** |
| H2            |            0.867 |
| RRF           |            0.867 |
| C3            |            0.833 |
| QT            |            0.833 |
| H1            |            0.833 |
| V1            |            0.833 |
| BM25          |            0.767 |

The **LLM-based reranker achieved the highest mean Precision@3** among the evaluated configurations.

### C3 vs. Reranker

| Question |   C3 | Reranker |
| -------- | ---: | -------: |
| Q1       | 1.00 |     1.00 |
| Q2       | 1.00 |     1.00 |
| Q3       | 0.67 |     1.00 |
| Q4       | 0.67 |     1.00 |
| Q5       | 0.67 |     1.00 |
| Q6       | 1.00 |     1.00 |
| Q7       | 1.00 |     1.00 |
| Q8       | 1.00 |     1.00 |
| Q9       | 1.00 |     1.00 |
| Q10      | 0.33 |     0.67 |

The reranker improved retrieval for **Q3, Q4, Q5, and Q10**, while maintaining the same Precision@3 on the remaining questions.

---

# Final V2 Pipeline

Based on the quantitative evaluation, the final retrieval pipeline uses C3 semantic retrieval followed by LLM reranking.

```text
User Query
    ↓
C3 Chunking
(1500 / 200)
    ↓
OpenAI Embeddings
    ↓
ChromaDB
    ↓
Top 10 Candidates
    ↓
GPT-5-mini Reranker
    ↓
Top 3 Passages
    ↓
Prompt + Retrieved Context
    ↓
GPT-5-mini
    ↓
Grounded Answer + Citations
```

The final pipeline achieved a mean **Precision@3 of 0.967** on the 10-question evaluation set.

The other retrieval strategies and their implementations are retained as experiments for comparison and reproducibility.

## Roadmap

### Completed

* [x] V1 basic RAG pipeline
* [x] Chunking experiments
* [x] Metadata-aware retrieval
* [x] BM25 retrieval
* [x] Hybrid search
* [x] Reciprocal Rank Fusion
* [x] LLM reranking
* [x] Query transformation
* [x] Quantitative retrieval evaluation
* [x] Final V2 pipeline selection

### Future Work

* Expand the evaluation dataset with more questions
* Evaluate retrieval with additional metrics
* Improve evaluation beyond LLM-as-a-Judge
* Experiment with larger or domain-specific reranking models
* Improve the Streamlit interface
* Explore additional retrieval and query-processing techniques

## Author

**Mudit Tandon**

M.Sc. Applied Computer Science
University of Göttingen
