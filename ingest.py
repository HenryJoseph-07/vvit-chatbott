from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import warnings
warnings.filterwarnings("ignore")

DATA_DIR = "data"
FAISS_DIR = "vectorstore_faiss"

print("Loading documents...")
loader = DirectoryLoader(
    DATA_DIR,
    glob="*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"}
)
docs = loader.load()
print(f"Loaded {len(docs)} documents")

print("Splitting into chunks...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)
print(f"Created {len(chunks)} chunks")

print("Loading embeddings...")
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

print("Creating FAISS vector database...")
vectordb = FAISS.from_documents(chunks, embeddings)
vectordb.save_local(FAISS_DIR)

print(f"Done! Saved to /{FAISS_DIR}")
print(f"Total chunks: {len(chunks)}")