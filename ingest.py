from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import warnings, glob, os
warnings.filterwarnings("ignore")

DATA_DIR = "data"
FAISS_DIR = "vectorstore_faiss"

docs = []

# Load TXT files
print("Loading text files...")
txt_loader = DirectoryLoader(
    DATA_DIR,
    glob="*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"}
)
txt_docs = txt_loader.load()
docs.extend(txt_docs)
print(f"Loaded {len(txt_docs)} text files")

# Load PDF files
print("Loading PDF files...")
pdf_files = glob.glob(os.path.join(DATA_DIR, "*.pdf"))
for pdf_path in pdf_files:
    try:
        loader = PyPDFLoader(pdf_path)
        pdf_docs = loader.load()
        docs.extend(pdf_docs)
        print(f"Loaded: {pdf_path} ({len(pdf_docs)} pages)")
    except Exception as e:
        print(f"Failed to load {pdf_path} — {e}")

print(f"\nTotal documents loaded: {len(docs)}")

# Split into chunks
print("Splitting into chunks...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)
print(f"Created {len(chunks)} chunks")

# Create embeddings
print("Loading embeddings...")
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

# Build FAISS vectorstore
print("Creating FAISS vector database...")
vectordb = FAISS.from_documents(chunks, embeddings)
vectordb.save_local(FAISS_DIR)

print(f"\nDone! Saved to /{FAISS_DIR}")
print(f"Total chunks indexed: {len(chunks)}")