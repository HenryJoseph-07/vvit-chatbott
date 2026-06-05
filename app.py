import os
os.environ["GRADIO_SSR_MODE"] = "false"
import gradio as gr
import warnings
import os
warnings.filterwarnings("ignore")

chain_tuple = None

def get_chain():
    global chain_tuple
    if chain_tuple is None:
        from chatbot import load_qa_chain
        chain_tuple = load_qa_chain()
    return chain_tuple

def respond(message, history):
    try:
        from chatbot import ask
        answer, sources = ask(get_chain(), message)
        source_urls = list(set(doc.metadata.get('source', '') for doc in sources))
        sources_text = "\n\n**Sources:**\n" + "\n".join(f"- {url}" for url in source_urls if url)
        return answer + sources_text
    except Exception as e:
        return f"Error: {str(e)}"

demo = gr.ChatInterface(
    fn=respond,
    title="🎓 VVIT College Assistant",
    description="Ask me anything about Vasireddy Venkatadri Institute of Technology — admissions, placements, departments, faculty, facilities and more!",
    examples=[
        "Tell me about VVIT",
        "What are the departments?",
        "Tell me about placements",
        "Who is the principal?",
        "What facilities does VVIT have?"
    ]
)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        ssr_mode=False,
        show_error=True
    )