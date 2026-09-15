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
