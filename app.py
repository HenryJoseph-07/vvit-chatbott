import streamlit as st
import warnings
import os
warnings.filterwarnings("ignore")

from chatbot import load_qa_chain, ask

st.set_page_config(page_title="VVIT Assistant", page_icon="🎓")
st.title("🎓 VVIT College Assistant")
st.caption("Ask me anything about Vasireddy Venkatadri Institute of Technology")

@st.cache_resource
def get_chain():
    return load_qa_chain()

chain_tuple = get_chain()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm the VVIT Assistant. Ask me about admissions, placements, departments, faculty or anything about VVIT!"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask about VVIT..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer, sources = ask(chain_tuple, prompt)
            st.markdown(answer)
            source_urls = list(set(doc.metadata.get('source','') for doc in sources))
            with st.expander("Sources"):
                for url in source_urls:
                    st.write(url)
    st.session_state.messages.append({"role": "assistant", "content": answer})