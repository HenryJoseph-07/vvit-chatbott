from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import warnings
import os

warnings.filterwarnings("ignore")

load_dotenv()

CHROMA_DIR = "vectorstore"

def load_qa_chain():
    print("Loading vector database...")

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )

    vectordb = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file")

    print(f"API key loaded: {api_key[:8]}...")

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        groq_api_key=api_key,
        temperature=0.3
    )

    prompt = PromptTemplate.from_template("""
You are VVIT Assistant, a helpful AI chatbot for Vasireddy Venkatadri Institute of Technology (VVIT), Guntur, Andhra Pradesh.

Use the following information from the VVIT website to answer the question.

If the answer is not in the provided information, say:
"I don't have that information right now. Please contact VVIT directly at www.vvitguntur.com"

Be friendly, concise, and helpful. Answer in clear English.

Context:
{context}

Question:
{question}

Answer:
""")

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain, retriever


def ask(chain_tuple, question):
    chain, retriever = chain_tuple

    answer = chain.invoke(question)

    sources = retriever.invoke(question)

    return answer, sources


if __name__ == "__main__":
    chain_tuple = load_qa_chain()

    print("\nVVIT Assistant ready! Type 'quit' to exit.\n")

    while True:
        q = input("You: ").strip()

        if q.lower() == "quit":
            break

        if not q:
            continue

        answer, sources = ask(chain_tuple, q)

        print(f"\nAssistant: {answer}")

        print(
            f"\nSources: {set(doc.metadata.get('source', '') for doc in sources)}\n"
        )