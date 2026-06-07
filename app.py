import streamlit as st
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="VVIT College Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

* { font-family: 'Inter', sans-serif; }

#MainMenu, footer, header { visibility: hidden; }

section[data-testid="stSidebar"] {
    background: #0f1419;
    border-right: 1px solid #1e2a3a;
    width: 280px !important;
}

section[data-testid="stSidebar"] * { color: #e2e8f0 !important; }

.main .block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

.hero-banner {
    background: #0f1419;
    border-bottom: 1px solid #1e2a3a;
    padding: 16px 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.hero-left { display: flex; align-items: center; gap: 16px; }

.hero-logo {
    width: 48px; height: 48px;
    background: #d4a017;
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 24px;
}

.hero-title { color: #f0c040; font-size: 22px; font-weight: 600; margin: 0; }
.hero-sub { color: #94a3b8; font-size: 13px; margin: 2px 0 0; }

.hero-stats { display: flex; gap: 24px; }

.stat-item { text-align: center; }
.stat-num { color: #f0c040; font-size: 20px; font-weight: 600; }
.stat-lbl { color: #64748b; font-size: 11px; }

.badge-row {
    display: flex; gap: 8px; padding: 12px 32px;
    background: #0a0f14;
    border-bottom: 1px solid #1e2a3a;
    flex-wrap: wrap;
}

.badge {
    background: #1e2a3a;
    color: #94a3b8;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    border: 1px solid #2d3f50;
}

.badge.active {
    background: #d4a017;
    color: #0f1419;
    border-color: #d4a017;
    font-weight: 500;
}

.chat-area {
    padding: 24px 32px;
    max-width: 860px;
    margin: 0 auto;
}

.stChatMessage {
    background: transparent !important;
}

[data-testid="stChatMessageContent"] {
    background: #131b24 !important;
    border: 1px solid #1e2a3a !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
}

[data-testid="stChatInput"] {
    background: #131b24 !important;
    border: 1px solid #2d3f50 !important;
    border-radius: 12px !important;
    color: #e2e8f0 !important;
}

.sidebar-section {
    padding: 16px;
    border-bottom: 1px solid #1e2a3a;
}

.sidebar-label {
    font-size: 11px;
    color: #64748b !important;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 10px;
    font-weight: 500;
}

.stButton button {
    background: #131b24 !important;
    border: 1px solid #2d3f50 !important;
    color: #94a3b8 !important;
    border-radius: 8px !important;
    font-size: 12px !important;
    text-align: left !important;
    padding: 8px 12px !important;
    width: 100% !important;
    transition: all 0.15s !important;
}

.stButton button:hover {
    background: #1e2a3a !important;
    border-color: #d4a017 !important;
    color: #f0c040 !important;
}

.welcome-card {
    background: #131b24;
    border: 1px solid #1e2a3a;
    border-left: 3px solid #d4a017;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 20px;
}

.welcome-title {
    color: #f0c040;
    font-size: 16px;
    font-weight: 500;
    margin-bottom: 8px;
}

.welcome-text { color: #94a3b8; font-size: 14px; line-height: 1.6; }

.quick-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-top: 16px;
}

.quick-chip {
    background: #1e2a3a;
    border: 1px solid #2d3f50;
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 13px;
    color: #94a3b8;
    cursor: pointer;
    transition: all 0.15s;
}

.quick-chip:hover {
    border-color: #d4a017;
    color: #f0c040;
}

.source-pill {
    display: inline-block;
    background: #1e2a3a;
    border: 1px solid #2d3f50;
    border-radius: 20px;
    padding: 3px 10px;
    font-size: 11px;
    color: #64748b;
    margin: 2px;
}

div[data-testid="stApp"] {
    background: #0a0f14 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-banner">
    <div class="hero-left">
        <div class="hero-logo">🎓</div>
        <div>
            <div class="hero-title">VVIT College Assistant</div>
            <div class="hero-sub">Vasireddy Venkatadri Institute of Technology, Guntur, AP</div>
        </div>
    </div>
    <div class="hero-stats">
        <div class="stat-item"><div class="stat-num">15+</div><div class="stat-lbl">Departments</div></div>
        <div class="stat-item"><div class="stat-num">200+</div><div class="stat-lbl">Faculty</div></div>
        <div class="stat-item"><div class="stat-num">5000+</div><div class="stat-lbl">Students</div></div>
        <div class="stat-item"><div class="stat-num">100+</div><div class="stat-lbl">Recruiters</div></div>
    </div>
</div>
<div class="badge-row">
    <span class="badge active">AI Powered</span>
    <span class="badge">NAAC Accredited</span>
    <span class="badge">NBA Certified</span>
    <span class="badge">Autonomous College</span>
    <span class="badge">NIRF Ranked</span>
    <span class="badge">ISO Certified</span>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="padding: 20px 16px 8px;">
        <div style="font-size:15px; font-weight:500; color:#f0c040; margin-bottom:4px;">Quick Navigation</div>
        <div style="font-size:12px; color:#64748b;">Tap to ask instantly</div>
    </div>
    """, unsafe_allow_html=True)

    categories = {
        "Academics": [
            "R23 CSE subjects list",
            "Examination schedule",
            "Academic calendar",
            "R23 regulations overview"
        ],
        "Departments": [
            "CSE department details",
            "ECE department info",
            "AI & ML department",
            "IT department details"
        ],
        "Faculty": [
            "Who is CSE HOD?",
            "CSE faculty list",
            "ECE faculty details",
            "AI ML faculty"
        ],
        "Placements": [
            "Placement statistics",
            "Top recruiters at VVIT",
            "Highest package offered",
            "Placement process"
        ],
        "Campus Life": [
            "Hostel facilities",
            "Transport details",
            "Library details",
            "Sports & extracurricular"
        ],
        "Admissions": [
            "Fee structure",
            "Admission process",
            "Eligibility criteria",
            "Scholarship details"
        ]
    }

    for category, questions in categories.items():
        st.markdown(f'<div class="sidebar-label" style="padding: 12px 16px 4px;">{category}</div>', unsafe_allow_html=True)
        for q in questions:
            if st.button(q, key=f"btn_{q}", use_container_width=True):
                st.session_state.quick_query = q

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    st.markdown('<div class="sidebar-label" style="padding: 0 16px 8px;">Actions</div>', unsafe_allow_html=True)

    if st.button("Clear conversation", key="clear", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("""
    <div style="padding: 16px; border-top: 1px solid #1e2a3a; margin-top: 8px;">
        <div style="font-size:11px; color:#475569; line-height:1.6;">
            Powered by Groq LLaMA 3.1<br>
            Data from vvitguntur.com<br>
            Built by Henry Joseph
        </div>
    </div>
    """, unsafe_allow_html=True)

@st.cache_resource(show_spinner="Loading VVIT knowledge base...")
def get_chain():
    from chatbot import load_qa_chain
    return load_qa_chain()

chain_tuple = get_chain()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "quick_query" not in st.session_state:
    st.session_state.quick_query = None

with st.container():
    st.markdown('<div class="chat-area">', unsafe_allow_html=True)

    if not st.session_state.messages:
        st.markdown("""
        <div class="welcome-card">
            <div class="welcome-title">Welcome to VVIT College Assistant</div>
            <div class="welcome-text">
                I'm trained on VVIT's official data — departments, faculty, placements, syllabus, facilities and more.
                Ask me anything about college life at VVIT or use the quick questions in the sidebar.
            </div>
        </div>
        """, unsafe_allow_html=True)

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("sources"):
                cols = st.columns([1])
                with cols[0]:
                    with st.expander("Sources", expanded=False):
                        for src in msg["sources"]:
                            st.markdown(f"`{src}`")

    prompt = st.chat_input("Ask anything about VVIT...")

    if st.session_state.quick_query:
        prompt = st.session_state.quick_query
        st.session_state.quick_query = None

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner(""):
                from chatbot import ask
                answer, sources = ask(chain_tuple, prompt)
                st.markdown(answer)
                source_list = list(set(
                    doc.metadata.get('source', '').replace('data\\', '').replace('data/', '')
                    for doc in sources
                    if doc.metadata.get('source')
                ))
                if source_list:
                    with st.expander("Sources", expanded=False):
                        for src in source_list:
                            st.markdown(f"`{src}`")

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer,
            "sources": source_list
        })
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)