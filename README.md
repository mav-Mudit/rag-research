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

The current version implements a straightforward retrieval augmented generation pipeline using a single vector store and similarity based retrieval.

Future versions will explore more advanced retrieval and RAG techniques.
