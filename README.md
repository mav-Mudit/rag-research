# Research Paper RAG

A RAG application for asking questions about NLP and LLM research papers, with source grounded answers and paper citations.

## Features

* PDF ingestion and text extraction
* Recursive text chunking
* OpenAI embeddings
* Chroma vector store
* Similarity based retrieval
* LLM generated answers using retrieved context
* Source grounded answers with paper and page information
* Streamlit interface for querying the research papers

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
 Retrieved Documents
        ↓
   Prompt + Context
        ↓
      LLM
        ↓
      Answer
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

## Current Version

**V1 — Basic RAG**

The current version implements a straightforward retrieval-augmented generation pipeline using a single vector store and similarity-based retrieval.

### V1 Baseline

The V1 baseline uses the following configuration:

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

The following fixed questions will be used to evaluate the V1 baseline and all subsequent Advanced RAG experiments.

**1.** What problem does Retrieval-Augmented Generation aim to address, and why can a language model's parametric knowledge be insufficient?

**2.** How does RAG combine parametric and non-parametric memory during generation?

**3.** How does RAG differ from a traditional language model that relies only on its parameters, particularly when dealing with knowledge-intensive tasks?

**4.** What are the main differences between RAG-Sequence and RAG-Token, and how do they affect the documents used during generation?

**5.** How does GPT-3 demonstrate that large language models can perform tasks from natural-language descriptions and a few examples without gradient-based updates?

**6.** How does T5's text-to-text formulation allow the same model and training framework to be applied to different NLP tasks?

**7.** Why does LoRA argue that the changes required when adapting a large language model have low intrinsic rank, and how does its approach exploit this observation?

**8.** How does ReAct combine reasoning and acting, and why does this provide an advantage over approaches that perform reasoning without interacting with external environments?

**9.** What does Chain-of-Thought prompting reveal about the relationship between model scale, intermediate reasoning steps, and performance on complex reasoning tasks?

**10.** What limitations of RAG are identified by the authors, and how do these limitations affect the reliability or usefulness of the generated answers?

These questions will remain unchanged throughout the V2 experiments so that different retrieval approaches can be compared against the same baseline.

### V1 Evaluation Summary

The V1 baseline was evaluated using the 10 fixed questions defined above.

Overall, the baseline RAG system performed well, with strong retrieval and well-grounded answers for most questions.

#### Strong Retrieval

The following questions produced particularly strong retrieval results:

* **Q1 — RAG motivation and limitations of parametric knowledge:** Retrieved passages directly explaining the motivation behind RAG and the limitations of relying only on parametric knowledge.
* **Q4 — RAG-Sequence vs. RAG-Token:** Retrieved the relevant passages directly describing the two approaches and their differences.
* **Q5 — GPT-3 few-shot learning:** Retrieved highly relevant passages describing GPT-3's few-shot capabilities and in-context learning.
* **Q6 — T5 text-to-text formulation:** Retrieved passages directly explaining the unified text-to-text framework.
* **Q7 — LoRA:** Retrieved relevant passages explaining the low-rank adaptation assumption and how LoRA exploits it.
* **Q8 — ReAct:** Retrieved passages directly describing the combination of reasoning and acting.
* **Q9 — Chain-of-Thought prompting:** Retrieved relevant passages discussing model scale, reasoning steps, and performance.

#### Areas for Improvement

Some questions exposed weaknesses in the baseline retrieval:

* **Q2 — Parametric and non-parametric memory:** The answer was good, but one of the retrieved sources was less directly relevant to the specific question.
* **Q3 — RAG vs. traditional language models:** The retrieved passages were relevant but somewhat redundant and did not provide the most focused evidence for the comparison.
* **Q10 — Limitations of RAG:** This was the clearest retrieval weakness. The question asks specifically about limitations, but the retrieved passages focused more on RAG results and performance rather than directly discussing its limitations. The generated answer therefore relied partly on inference from the retrieved context.

#### Key Takeaway

The V1 baseline demonstrates that the basic RAG pipeline can retrieve relevant information from the research-paper collection. However, **Q2, Q3, and especially Q10** show that retrieval quality can still be improved.

An important observation is that a good generated answer does not necessarily mean that retrieval was good. The language model can sometimes fill gaps using its own parametric knowledge.

Therefore, V2 will focus on improving the retrieval component while keeping the **same 10 evaluation questions** and comparing every experiment against this fixed V1 baseline.

Each retrieval technique will be tested independently, and only techniques that demonstrate an improvement will be considered for the final V2 pipeline.


## Roadmap

### V2 — Advanced RAG

The goal of V2 is to improve retrieval step by step and evaluate whether each technique actually improves performance.

Planned experiments:

1. Chunking
2. Metadata-aware retrieval
3. BM25
4. Hybrid search
5. Reciprocal Rank Fusion (RRF)
6. Reranking
7. Query transformation
8. Final V2 pipeline
9. V1 vs V2 comparison

## V2 Stage 1 — Chunking Experiment

The first V2 experiment evaluated whether changing chunk size and overlap could improve retrieval quality.

Four configurations were compared using the same fixed set of 10 evaluation questions:

| Configuration | Chunk Size | Overlap |
|---|---:|---:|
| V1 baseline | 1000 | 150 |
| C1 | 500 | 100 |
| C2 | 750 | 100 |
| C3 | 1500 | 200 |

The configurations were evaluated by inspecting the retrieved passages for all 10 questions, with particular attention to the retrieval weaknesses identified in the V1 baseline (Q2, Q3, and Q10).

### Result

**C3 (1500/200) was selected as the winner.**

The 1500/200 configuration produced the strongest overall retrieval quality across the evaluation set. In particular, it improved retrieval for Q3 and Q10, while maintaining strong performance on the remaining questions.

The most significant improvement was observed for Q10, where C3 retrieved passages directly discussing RAG's dependence on relevant evidence, limitations in corpus coverage, and residual hallucination.

The selected configuration will be used as the fixed chunking configuration for the next V2 experiments.

## V2 Stage 2 — Metadata-Aware Retrieval

The second V2 experiment evaluated whether document metadata could improve retrieval quality.

The C3 configuration (1500 chunk size / 200 overlap) was used as the fixed baseline for this stage.

Two metadata-aware retrieval strategies were tested:

| Configuration | Approach |
|---|---|
| M1 | Hard metadata filtering |
| M2 | Metadata-based score boosting |

### M1 — Hard Metadata Filtering

If a query explicitly mentioned a known paper, retrieval was restricted to chunks from that paper. Otherwise, normal semantic retrieval was used.

This improved paper-level precision by ensuring that queries mentioning a specific paper retrieved only chunks from that paper. However, restricting retrieval to the correct paper did not consistently improve the relevance of the retrieved passages.

### M2 — Metadata Score Boosting

M2 retrieved candidates using semantic similarity and applied a small ranking boost to chunks belonging to the paper explicitly mentioned in the query.

This approach was less restrictive than M1, but it also did not produce a consistent improvement over the C3 baseline.

### Result

Neither metadata-aware retrieval strategy produced a meaningful improvement over C3 across the fixed set of 10 evaluation questions.
