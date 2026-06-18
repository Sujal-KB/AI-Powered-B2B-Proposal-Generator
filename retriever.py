from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import streamlit as st

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

@st.cache_resource
def load_vectorstore():
    vectorstore = FAISS.load_local(
        "proposal_faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vectorstore