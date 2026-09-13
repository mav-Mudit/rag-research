import streamlit as st

from src.generate import rag_chain
from src.retrieve import retrieve_documents


st.set_page_config(
    page_title="Research Paper RAG",
    page_icon="📚",
)

st.title("📚 Research Paper RAG")
st.write("Ask questions about the research papers in the knowledge base.")

query = st.text_input(
    "Ask a question",
    placeholder="What is Retrieval-Augmented Generation?",
)

if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching the papers and generating an answer..."):
            answer = rag_chain.invoke(query)
            documents = retrieve_documents(query, k=3)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Sources")

        for i, document in enumerate(documents, start=1):
            paper_title = document.metadata.get(
                "paper_title",
                "Unknown paper",
            )
            page = document.metadata.get(
                "page",
                "Unknown page",
            )

            with st.expander(
                f"Source {i}: {paper_title} — Page {page}"
            ):
                st.write(document.page_content)