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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }

#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: #080C10 !important; }

div[data-testid="stApp"] { background: #080C10 !important; }

.main .block-container { padding: 0 !important; max-width: 100% !important; }

section[data-testid="stSidebar"] {
    background: #0D1117 !important;
    border-right: 1px solid #21262D !important;
    min-width: 260px !important;
    max-width: 260px !important;
}
section[data-testid="stSidebar"] > div { padding: 0 !important; }

.stButton > button {
    background: #161B22 !important;
    border: 1px solid #21262D !important;
    color: #8B949E !important;
    border-radius: 6px !important;
    font-size: 12px !important;
    text-align: left !important;
    padding: 7px 10px !important;
    width: 100% !important;
    margin-bottom: 3px !important;
    transition: all 0.2s !important;
    font-family: 'Inter', sans-serif !important;
}
.stButton > button:hover {
    background: #1C2128 !important;
    border-color: #E6A817 !important;
    color: #E6A817 !important;
}

[data-testid="stChatInput"] textarea {
    background: #161B22 !important;
    border: 1px solid #30363D !important;
    color: #E6EDF3 !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stChatMessageContent"] {
    background: #161B22 !important;
    border: 1px solid #21262D !important;
    border-radius: 10px !important;
    color: #E6EDF3 !important;
}

.stSpinner > div { border-top-color: #E6A817 !important; }

.stExpander {
    background: #161B22 !important;
    border: 1px solid #21262D !important;
    border-radius: 8px !important;
}
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:20px 16px 12px; border-bottom:1px solid #21262D;">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:4px;">
            <div style="width:36px;height:36px;background:#E6A817;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px;">🎓</div>
            <div>
                <div style="color:#E6A817;font-weight:600;font-size:14px;">VVIT Assistant</div>
                <div style="color:#484F58;font-size:11px;">AI Powered</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    nav = {
        "🏫 Departments": ["CSE department","ECE department","AI & ML dept","IT department","Civil dept","Mechanical dept"],
        "👨‍🏫 Faculty": ["CSE HOD details","CSE faculty list","ECE faculty","AI ML faculty","IT faculty"],
        "📚 Academics": ["R23 CSE subjects","R23 ECE subjects","Academic calendar","Exam schedule","CGPA system"],
        "💼 Placements": ["Placement stats","Top recruiters","Highest package","Placement process","Internships"],
        "🏛️ Campus": ["Hostel details","Library info","Sports facilities","Transport","Labs & infra"],
        "📋 Admissions": ["Fee structure","Admission process","Scholarships","Eligibility criteria"],
    }

    for section, questions in nav.items():
        st.markdown(f"""
        <div style="padding:10px 16px 4px;">
            <div style="color:#484F58;font-size:10px;font-weight:500;text-transform:uppercase;letter-spacing:0.08em;">{section}</div>
        </div>
        """, unsafe_allow_html=True)
        for q in questions:
            if st.button(q, key=f"q_{q}"):
                st.session_state.quick_query = q

    st.markdown("""
    <div style="position:absolute;bottom:0;left:0;right:0;padding:12px 16px;border-top:1px solid #21262D;background:#0D1117;">
        <div style="font-size:11px;color:#484F58;line-height:1.7;">
            Built by <span style="color:#E6A817;">Henry Joseph</span><br>
            Powered by Groq LLaMA 3.1<br>
            Data: vvitguntur.com
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── MAIN AREA ─────────────────────────────────────────────
st.markdown("""
<div style="background:#0D1117;border-bottom:1px solid #21262D;padding:14px 32px;display:flex;align-items:center;justify-content:space-between;">
    <div style="display:flex;align-items:center;gap:14px;">
        <div style="background:#E6A817;width:42px;height:42px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:20px;">🎓</div>
        <div>
            <div style="color:#E6EDF3;font-size:18px;font-weight:600;">VVIT College Assistant</div>
            <div style="color:#484F58;font-size:12px;">Vasireddy Venkatadri Institute of Technology · Guntur, AP</div>
        </div>
    </div>
    <div style="display:flex;gap:20px;">
        <div style="text-align:center;">
            <div style="color:#E6A817;font-size:18px;font-weight:600;">15+</div>
            <div style="color:#484F58;font-size:10px;">Depts</div>
        </div>
        <div style="text-align:center;">
            <div style="color:#E6A817;font-size:18px;font-weight:600;">200+</div>
            <div style="color:#484F58;font-size:10px;">Faculty</div>
        </div>
        <div style="text-align:center;">
            <div style="color:#E6A817;font-size:18px;font-weight:600;">5K+</div>
            <div style="color:#484F58;font-size:10px;">Students</div>
        </div>
        <div style="text-align:center;">
            <div style="color:#E6A817;font-size:18px;font-weight:600;">100+</div>
            <div style="color:#484F58;font-size:10px;">Recruiters</div>
        </div>
    </div>
</div>

<div style="background:#080C10;padding:8px 32px;border-bottom:1px solid #21262D;display:flex;gap:8px;flex-wrap:wrap;">
    <span style="background:#E6A817;color:#080C10;padding:3px 10px;border-radius:20px;font-size:11px;font-weight:500;">AI Powered</span>
    <span style="background:#161B22;color:#8B949E;border:1px solid #30363D;padding:3px 10px;border-radius:20px;font-size:11px;">NAAC A+</span>
    <span style="background:#161B22;color:#8B949E;border:1px solid #30363D;padding:3px 10px;border-radius:20px;font-size:11px;">NBA Certified</span>
    <span style="background:#161B22;color:#8B949E;border:1px solid #30363D;padding:3px 10px;border-radius:20px;font-size:11px;">Autonomous</span>
    <span style="background:#161B22;color:#8B949E;border:1px solid #30363D;padding:3px 10px;border-radius:20px;font-size:11px;">NIRF Ranked</span>
    <span style="background:#161B22;color:#8B949E;border:1px solid #30363D;padding:3px 10px;border-radius:20px;font-size:11px;">ISO 9001</span>
</div>
""", unsafe_allow_html=True)

# Load chain
@st.cache_resource(show_spinner="Loading VVIT knowledge base...")
def get_chain():
    from chatbot import load_qa_chain
    return load_qa_chain()

chain_tuple = get_chain()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "quick_query" not in st.session_state:
    st.session_state.quick_query = None

# Chat container
with st.container():
    st.markdown('<div style="max-width:820px;margin:0 auto;padding:24px 32px;">', unsafe_allow_html=True)

    if not st.session_state.messages:
        st.markdown("""
        <div style="background:#0D1117;border:1px solid #21262D;border-left:3px solid #E6A817;border-radius:10px;padding:20px 24px;margin-bottom:20px;">
            <div style="color:#E6A817;font-size:15px;font-weight:500;margin-bottom:8px;">👋 Welcome to VVIT College Assistant</div>
            <div style="color:#8B949E;font-size:13px;line-height:1.7;">
                I'm trained on VVIT's official data — departments, faculty, placements, R23 syllabus, facilities and more.<br>
                Use the sidebar for quick questions or type anything below.
            </div>
        </div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:24px;">
            <div style="background:#0D1117;border:1px solid #21262D;border-radius:8px;padding:14px;cursor:pointer;">
                <div style="color:#E6A817;font-size:13px;font-weight:500;margin-bottom:4px;">📊 Placements</div>
                <div style="color:#484F58;font-size:12px;">Top packages, recruiters and stats</div>
            </div>
            <div style="background:#0D1117;border:1px solid #21262D;border-radius:8px;padding:14px;cursor:pointer;">
                <div style="color:#E6A817;font-size:13px;font-weight:500;margin-bottom:4px;">📚 R23 Syllabus</div>
                <div style="color:#484F58;font-size:12px;">Subject-wise curriculum details</div>
            </div>
            <div style="background:#0D1117;border:1px solid #21262D;border-radius:8px;padding:14px;cursor:pointer;">
                <div style="color:#E6A817;font-size:13px;font-weight:500;margin-bottom:4px;">👨‍🏫 Faculty</div>
                <div style="color:#484F58;font-size:12px;">Department-wise faculty details</div>
            </div>
            <div style="background:#0D1117;border:1px solid #21262D;border-radius:8px;padding:14px;cursor:pointer;">
                <div style="color:#E6A817;font-size:13px;font-weight:500;margin-bottom:4px;">🏛️ Campus Life</div>
                <div style="color:#484F58;font-size:12px;">Hostel, sports, clubs and more</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("sources"):
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
            with st.spinner("Thinking..."):
                from chatbot import ask
                answer, sources = ask(chain_tuple, prompt)
                st.markdown(answer)
                source_list = list(set(
                    doc.metadata.get('source','').replace('data\\','').replace('data/','')
                    for doc in sources if doc.metadata.get('source')
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