from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import warnings
warnings.filterwarnings("ignore")

DATA_DIR = "data"
CHROMA_DIR = "vectorstore"

print("Loading documents...")
loader = DirectoryLoader(
    DATA_DIR,
    glob="*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"}
)
docs = loader.load()
print(f"Loaded {len(docs)} documents")

print("\nSplitting into chunks...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", ".", " "]
)
chunks = splitter.split_documents(docs)
print(f"Created {len(chunks)} chunks")

print("\nLoading embedding model (first time ~90MB download)...")
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

print("\nCreating vector database...")
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=CHROMA_DIR
)

print(f"\nDone! Vector database saved to /{CHROMA_DIR}")
print(f"Total chunks indexed: {len(chunks)}")