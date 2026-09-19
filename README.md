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


## V2 Stage 3 — BM25 Retrieval

The third V2 experiment evaluated BM25 as a standalone lexical retrieval method.

The C3 configuration (1500 chunk size / 200 overlap) was kept fixed so that the retrieval method could be evaluated independently.

### BM25

BM25 ranks chunks based on lexical overlap between the query and document text. Unlike semantic retrieval, it does not use embeddings and therefore provides a different retrieval signal.

BM25 performed particularly well for terminology-heavy questions where important terms appeared explicitly in the relevant passages, such as LoRA, ReAct, and Chain-of-Thought.

However, BM25 also produced irrelevant results for some questions. The clearest example was Q10, where none of the top three retrieved passages came from the RAG paper, despite the question explicitly asking about RAG limitations.

### Result

BM25 was not selected as a standalone replacement for the C3 semantic retriever.

However, the experiment demonstrated that BM25 can provide a complementary lexical retrieval signal. Therefore, BM25 will be evaluated together with C3 in the next stage using **Hybrid Search**.

The BM25 implementation and evaluation results are retained for reproducibility.

## V2 Stage 4 — Hybrid Search

The fourth V2 experiment evaluated whether combining semantic retrieval with lexical BM25 retrieval could improve retrieval quality.

The **C3 configuration (1500 chunk size / 200 overlap)** was used as the fixed semantic retrieval baseline. **BM25 standalone** was also considered as a lexical retrieval baseline.

The retrieval approaches were compared as follows:

| Configuration | Semantic Retrieval | BM25 | Combination     |
| ------------- | -----------------: | ---: | --------------- |
| C3 baseline   |               100% |   0% | Semantic only   |
| BM25          |                 0% | 100% | Lexical only    |
| H1            |                70% |  30% | Weighted hybrid |
| H2            |                50% |  50% | Weighted hybrid |

For H1 and H2, the top 10 candidates from semantic retrieval and BM25 were combined using normalized scores, and the top 3 documents were returned.

### BM25 Standalone

BM25 provided strong lexical retrieval for several questions, particularly when the terminology in the question closely matched the terminology in the papers.

However, BM25 also produced noisy results for some questions. The clearest failure was Q10, where the retrieved passages came from the GPT-3 and Chain-of-Thought papers instead of the RAG paper containing the relevant discussion of RAG limitations.

Therefore, BM25 was useful as a complementary retrieval method but was not suitable as a replacement for semantic retrieval.

### H1 — 70/30 Hybrid

H1 gave semantic retrieval more influence while allowing BM25 to contribute lexical matching.

Compared with BM25 standalone, H1 substantially reduced the retrieval failures caused by relying only on lexical matching. It also benefited from BM25's lexical signal on questions such as Q5.

However, H1 did not consistently improve retrieval quality compared with the C3 semantic baseline. C3 remained more focused for several questions, including Q2, Q3, Q4, and Q10.

### H2 — 50/50 Hybrid

H2 gave semantic retrieval and BM25 equal influence.

It performed well across most questions and retained the complementary lexical behavior of BM25. However, giving BM25 equal weight also introduced some less relevant passages, and C3 remained more focused on several questions.

H2 therefore did not provide a consistent improvement over C3.

### Result

The experiments showed three distinct behaviors:

* **C3** provided the most consistent semantic retrieval quality.
* **BM25** provided useful complementary lexical retrieval but could be noisy when used alone.
* **H1 and H2** combined the strengths of both approaches in some cases, but neither consistently outperformed C3 across the fixed set of 10 evaluation questions.

Therefore:

* **C3 — Selected as the current retrieval baseline**
* **BM25 — Not selected as standalone retrieval**
* **H1 (70/30) — Not selected**
* **H2 (50/50) — Not selected**

These results do not rule out hybrid retrieval. Instead, they suggest that **fixed weighted score combination may not be the most effective way to combine semantic and lexical retrieval**.


