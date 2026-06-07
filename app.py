import streamlit as st
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="VVIT College Assistant",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stChatMessage { border-radius: 12px; margin-bottom: 8px; }
    .sidebar-title { font-size: 18px; font-weight: bold; color: #FFD700; }
    .quick-btn { width: 100%; margin-bottom: 4px; }
    header { background-color: #1a1f2e !important; }
    .college-header {
        background: linear-gradient(135deg, #1a1f2e, #2d3561);
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        border-left: 4px solid #FFD700;
    }
    .college-header h1 { color: #FFD700; margin: 0; font-size: 28px; }
    .college-header p { color: #aaa; margin: 5px 0 0 0; font-size: 14px; }
    .stat-box {
        background: #1a1f2e;
        border-radius: 8px;
        padding: 12px;
        text-align: center;
        border: 1px solid #2d3561;
    }
    .stat-box h3 { color: #FFD700; margin: 0; font-size: 22px; }
    .stat-box p { color: #aaa; margin: 0; font-size: 12px; }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<p class="sidebar-title">🎓 VVIT Assistant</p>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("**Quick Questions**")

    quick_questions = [
        "Tell me about VVIT",
        "CSE department details",
        "Placement statistics",
        "Who is the CSE HOD?",
        "R23 CSE subjects",
        "Faculty details",
        "Fee structure",
        "Hostel facilities",
        "About NAAC accreditation",
        "Extracurricular activities"
    ]

    for q in quick_questions:
        if st.button(q, key=q, use_container_width=True):
            st.session_state.quick_query = q

    st.markdown("---")
    st.markdown("**About**")
    st.caption("AI Assistant trained on VVIT's official website data. For accurate info always verify at vvitguntur.com")
    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! I'm the VVIT Assistant. Ask me about admissions, placements, departments, faculty or anything about VVIT!"}
        ]
        st.rerun()

# Header
st.markdown("""
<div class="college-header">
    <h1>🎓 VVIT College Assistant</h1>
    <p>Vasireddy Venkatadri Institute of Technology, Guntur, Andhra Pradesh</p>
</div>
""", unsafe_allow_html=True)

# Stats row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('<div class="stat-box"><h3>15+</h3><p>Departments</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="stat-box"><h3>200+</h3><p>Faculty</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="stat-box"><h3>5000+</h3><p>Students</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="stat-box"><h3>100+</h3><p>Recruiters</p></div>', unsafe_allow_html=True)

st.markdown("---")

# Load chain
@st.cache_resource
def get_chain():
    from chatbot import load_qa_chain
    return load_qa_chain()

chain_tuple = get_chain()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm the VVIT Assistant. Ask me about admissions, placements, departments, faculty or anything about VVIT!"}
    ]

if "quick_query" not in st.session_state:
    st.session_state.quick_query = None

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle quick question or chat input
prompt = st.chat_input("Ask about VVIT...")

if st.session_state.quick_query:
    prompt = st.session_state.quick_query
    st.session_state.quick_query = None

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            from chatbot import ask
            answer, sources = ask(chain_tuple, prompt)
            st.markdown(answer)
            source_urls = list(set(doc.metadata.get('source','') for doc in sources))
            with st.expander("📚 Sources"):
                for url in source_urls:
                    st.write(url)
    st.session_state.messages.append({"role": "assistant", "content": answer})