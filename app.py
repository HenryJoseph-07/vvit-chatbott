import streamlit as st
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="VVIT Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"], * {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

#MainMenu, footer, [data-testid="stToolbar"] { visibility: hidden; }

div[data-testid="stApp"] { background: #FAFAF8 !important; }

.main .block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

section[data-testid="stSidebar"] {
    background: #FFFFFF !important;
    border-right: 1px solid #E8E5E0 !important;
    min-width: 255px !important;
    max-width: 255px !important;
    box-shadow: 2px 0 8px rgba(0,0,0,0.04) !important;
}
section[data-testid="stSidebar"] > div {
    padding: 0 !important;
}

.stButton > button {
    background: transparent !important;
    border: none !important;
    border-radius: 6px !important;
    color: #6B6560 !important;
    font-size: 12.5px !important;
    text-align: left !important;
    padding: 7px 12px !important;
    width: 100% !important;
    margin-bottom: 1px !important;
    transition: all 0.15s ease !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 400 !important;
}
.stButton > button:hover {
    background: #F5F3F0 !important;
    color: #1A1714 !important;
}

[data-testid="stChatInput"] {
    border: 1.5px solid #E8E5E0 !important;
    border-radius: 12px !important;
    background: #FFFFFF !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
}

[data-testid="stChatInput"] textarea {
    background: #FFFFFF !important;
    color: #1A1714 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 14px !important;
}

[data-testid="stChatMessageContent"] {
    border-radius: 12px !important;
    font-size: 14px !important;
    line-height: 1.7 !important;
}

div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) [data-testid="stChatMessageContent"] {
    background: #FFFFFF !important;
    border: 1px solid #E8E5E0 !important;
    color: #1A1714 !important;
}

div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"] {
    background: #1A1714 !important;
    color: #FAFAF8 !important;
    border: none !important;
}

.stExpander {
    border: 1px solid #E8E5E0 !important;
    border-radius: 8px !important;
    background: #FAFAF8 !important;
}

.stSpinner > div { border-top-color: #C9A84C !important; }

a { color: #C9A84C !important; }
</style>
""", unsafe_allow_html=True)

# ── SIDEBAR ──────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:22px 18px 16px;border-bottom:1px solid #E8E5E0;">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
            <div style="width:38px;height:38px;background:#1A1714;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0;">🎓</div>
            <div>
                <div style="color:#1A1714;font-weight:600;font-size:13.5px;line-height:1.2;">VVIT Assistant</div>
                <div style="color:#A09890;font-size:11px;margin-top:2px;">College Knowledge Base</div>
            </div>
        </div>
        <div style="display:flex;gap:6px;flex-wrap:wrap;">
            <span style="background:#F0EDE8;color:#6B6560;padding:3px 9px;border-radius:20px;font-size:10.5px;">NAAC A+</span>
            <span style="background:#F0EDE8;color:#6B6560;padding:3px 9px;border-radius:20px;font-size:10.5px;">NBA</span>
            <span style="background:#F0EDE8;color:#6B6560;padding:3px 9px;border-radius:20px;font-size:10.5px;">Autonomous</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    nav = {
        "Departments": ["CSE department", "ECE department", "AI & ML dept", "AI & DS dept", "IT department", "EEE dept", "Civil dept", "Mechanical dept"],
        "Faculty": ["CSE HOD & faculty", "ECE faculty", "AI ML faculty", "IT faculty", "EEE faculty", "Mechanical faculty"],
        "Academics": ["R23 CSE subjects", "R23 ECE subjects", "R23 EEE subjects", "R23 Civil subjects", "R23 Mechanical subjects", "Academic regulations"],
        "Placements": ["Placement overview", "Top recruiters", "Branch-wise stats", "Internship details"],
        "Campus": ["Hostel & mess", "Library", "Sports facilities", "Labs & infrastructure", "Transport"],
        "Admissions": ["Fee structure", "Admission process", "Scholarships", "Contact & location"],
    }

    for section, questions in nav.items():
        st.markdown(f"""
        <div style="padding:14px 18px 5px;">
            <div style="color:#A09890;font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.09em;">{section}</div>
        </div>
        """, unsafe_allow_html=True)
        for q in questions:
            if st.button(q, key=f"nav_{q}"):
                st.session_state.quick_query = q

    st.markdown("""
    <div style="padding:16px 18px;border-top:1px solid #E8E5E0;margin-top:12px;">
        <div style="font-size:11px;color:#C0BAB4;line-height:1.8;">
            Built by Henry Joseph · VVIT CSE '26<br>
            <span style="color:#C9A84C;">RAG · FAISS · Groq LLaMA 3.1</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── TOPBAR ──────────────────────────
st.markdown("""
<div style="background:#FFFFFF;border-bottom:1px solid #E8E5E0;padding:13px 28px;display:flex;align-items:center;justify-content:space-between;">
    <div style="display:flex;align-items:center;gap:12px;">
        <div style="width:34px;height:34px;background:#1A1714;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:16px;">🎓</div>
        <div>
            <div style="color:#1A1714;font-weight:600;font-size:15px;line-height:1.2;">VVIT College Assistant</div>
            <div style="color:#A09890;font-size:11.5px;">Vasireddy Venkatadri Institute of Technology · Guntur, AP</div>
        </div>
    </div>
    <div style="display:flex;gap:24px;align-items:center;">
        <div style="text-align:center;">
            <div style="color:#1A1714;font-size:16px;font-weight:600;">15+</div>
            <div style="color:#A09890;font-size:10px;">Depts</div>
        </div>
        <div style="width:1px;height:28px;background:#E8E5E0;"></div>
        <div style="text-align:center;">
            <div style="color:#1A1714;font-size:16px;font-weight:600;">200+</div>
            <div style="color:#A09890;font-size:10px;">Faculty</div>
        </div>
        <div style="width:1px;height:28px;background:#E8E5E0;"></div>
        <div style="text-align:center;">
            <div style="color:#1A1714;font-size:16px;font-weight:600;">5K+</div>
            <div style="color:#A09890;font-size:10px;">Students</div>
        </div>
        <div style="width:1px;height:28px;background:#E8E5E0;"></div>
        <div style="text-align:center;">
            <div style="color:#1A1714;font-size:16px;font-weight:600;">100+</div>
            <div style="color:#A09890;font-size:10px;">Recruiters</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── CHAIN ──────────────────────────
@st.cache_resource(show_spinner="Loading knowledge base...")
def get_chain():
    from chatbot import load_qa_chain
    return load_qa_chain()

chain_tuple = get_chain()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "quick_query" not in st.session_state:
    st.session_state.quick_query = None

# ── CHAT AREA ──────────────────────────
col_pad1, col_main, col_pad2 = st.columns([0.5, 9, 0.5])

with col_main:
    st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

    if not st.session_state.messages:
        st.markdown("""
        <div style="max-width:700px;margin:0 auto 28px;">
            <div style="margin-bottom:6px;">
                <span style="background:#F0EDE8;color:#6B6560;padding:4px 10px;border-radius:20px;font-size:11px;font-weight:500;">AI Powered · College Specific</span>
            </div>
            <div style="color:#1A1714;font-size:22px;font-weight:600;margin-bottom:8px;line-height:1.3;">
                What would you like to know about VVIT?
            </div>
            <div style="color:#6B6560;font-size:14px;line-height:1.6;margin-bottom:24px;">
                I'm trained specifically on VVIT's data — departments, faculty, R23 syllabus, placements, facilities and more. Ask me anything.
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;">
                <div style="background:#FFFFFF;border:1px solid #E8E5E0;border-radius:10px;padding:14px 16px;cursor:pointer;">
                    <div style="font-size:18px;margin-bottom:6px;">📊</div>
                    <div style="color:#1A1714;font-size:13px;font-weight:500;margin-bottom:3px;">Placements</div>
                    <div style="color:#A09890;font-size:12px;">Packages, companies & stats</div>
                </div>
                <div style="background:#FFFFFF;border:1px solid #E8E5E0;border-radius:10px;padding:14px 16px;cursor:pointer;">
                    <div style="font-size:18px;margin-bottom:6px;">📚</div>
                    <div style="color:#1A1714;font-size:13px;font-weight:500;margin-bottom:3px;">R23 Syllabus</div>
                    <div style="color:#A09890;font-size:12px;">Subjects by branch & semester</div>
                </div>
                <div style="background:#FFFFFF;border:1px solid #E8E5E0;border-radius:10px;padding:14px 16px;cursor:pointer;">
                    <div style="font-size:18px;margin-bottom:6px;">👨‍🏫</div>
                    <div style="color:#1A1714;font-size:13px;font-weight:500;margin-bottom:3px;">Faculty</div>
                    <div style="color:#A09890;font-size:12px;">HODs, professors & staff</div>
                </div>
                <div style="background:#FFFFFF;border:1px solid #E8E5E0;border-radius:10px;padding:14px 16px;cursor:pointer;">
                    <div style="font-size:18px;margin-bottom:6px;">🏛️</div>
                    <div style="color:#1A1714;font-size:13px;font-weight:500;margin-bottom:3px;">Campus Life</div>
                    <div style="color:#A09890;font-size:12px;">Hostel, labs, sports & clubs</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("sources"):
                with st.expander("Sources", expanded=False):
                    for src in msg["sources"]:
                        st.caption(f"📄 {src}")

    prompt = st.chat_input("Ask anything about VVIT — faculty, syllabus, placements...")

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
                    doc.metadata.get('source','').replace('data\\','').replace('data/','')
                    for doc in sources if doc.metadata.get('source')
                ))
                if source_list:
                    with st.expander("Sources", expanded=False):
                        for src in source_list:
                            st.caption(f"📄 {src}")
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer,
            "sources": source_list
        })
        st.rerun()

    if st.session_state.messages:
        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        bcol1, bcol2, bcol3 = st.columns([4,1,4])
        with bcol2:
            if st.button("Clear", key="clear_chat"):
                st.session_state.messages = []
                st.rerun()
