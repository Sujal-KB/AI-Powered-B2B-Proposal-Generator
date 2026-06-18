from langchain_community.document_loaders import DirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

loader = DirectoryLoader("E:\Assignment\data", glob="**/*.txt")
docs = loader.load()

embeddings=HuggingFaceEmbeddings(
  model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore=FAISS.from_documents(
  embedding=embeddings,
  documents=docs
)

vectorstore.save_local("proposal_faiss_index")