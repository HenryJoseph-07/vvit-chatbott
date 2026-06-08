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
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,300;0,14..32,400;0,14..32,500;0,14..32,600;1,14..32,400&display=swap');

*, html, body { font-family: 'Inter', sans-serif !important; box-sizing: border-box; }

#MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stStatusWidget"] { display: none !important; }

div[data-testid="stApp"] { background: #080B14 !important; }
.main .block-container { padding: 0 !important; max-width: 100% !important; }

section[data-testid="stSidebar"] {
    background: #0C1018 !important;
    border-right: 1px solid #1C2333 !important;
    min-width: 240px !important; max-width: 240px !important;
}
section[data-testid="stSidebar"] > div { padding: 0 !important; }

.stButton > button {
    background: transparent !important; border: none !important;
    color: #8892A4 !important; font-size: 12px !important;
    text-align: left !important; padding: 6px 14px !important;
    width: 100% !important; border-radius: 6px !important;
    font-family: 'Inter', sans-serif !important; font-weight: 400 !important;
    transition: all 0.15s !important; margin: 0 !important;
}
.stButton > button:hover { background: #141824 !important; color: #E8EDF5 !important; }

[data-testid="stChatInput"] {
    background: #141824 !important; border: 1px solid #1C2333 !important;
    border-radius: 14px !important; box-shadow: 0 0 0 1px #1C2333 !important;
}
[data-testid="stChatInput"] textarea {
    background: #141824 !important; color: #E8EDF5 !important;
    font-family: 'Inter', sans-serif !important; font-size: 13.5px !important;
}
[data-testid="stChatInput"] textarea::placeholder { color: #3D4A5C !important; }
[data-testid="stChatInput"] button { background: #2563EB !important; border-radius: 8px !important; }

div[data-testid="stChatMessage"] { background: transparent !important; padding: 4px 0 !important; }
[data-testid="stChatMessageContent"] {
    font-size: 13.5px !important; line-height: 1.75 !important; border-radius: 12px !important;
}
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) [data-testid="stChatMessageContent"] {
    background: #0C1018 !important; border: 1px solid #1C2333 !important; color: #CBD5E1 !important;
}
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) [data-testid="stChatMessageContent"] {
    background: #1E3A5F !important; border: 1px solid #2563EB33 !important; color: #E8EDF5 !important;
}

.stExpander { background: #0C1018 !important; border: 1px solid #1C2333 !important; border-radius: 8px !important; }
.stExpander summary { color: #3D4A5C !important; font-size: 12px !important; }
.stSpinner > div { border-top-color: #2563EB !important; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="padding:24px 16px 16px; border-bottom:1px solid #1C2333;">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px;">
            <div style="width:36px;height:36px;background:linear-gradient(135deg,#2563EB,#1D4ED8);border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0;">🎓</div>
            <div>
                <div style="color:#E8EDF5;font-weight:600;font-size:13px;">VVIT Assistant</div>
                <div style="color:#3D4A5C;font-size:11px;margin-top:1px;">AI Knowledge Base</div>
            </div>
        </div>
        <div style="display:flex;gap:5px;flex-wrap:wrap;">
            <span style="background:#0D1F3C;color:#60A5FA;padding:3px 8px;border-radius:4px;font-size:10px;border:1px solid #1E3A5F;">NAAC A+</span>
            <span style="background:#0D1F3C;color:#60A5FA;padding:3px 8px;border-radius:4px;font-size:10px;border:1px solid #1E3A5F;">NBA</span>
            <span style="background:#0D1F3C;color:#60A5FA;padding:3px 8px;border-radius:4px;font-size:10px;border:1px solid #1E3A5F;">Autonomous</span>
            <span style="background:#0D1F3C;color:#60A5FA;padding:3px 8px;border-radius:4px;font-size:10px;border:1px solid #1E3A5F;">NIRF</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    nav = {
        "Departments": ["CSE department","ECE department","AI & ML dept","AI & DS dept","IT department","EEE dept","Civil dept","Mechanical dept"],
        "Faculty": ["CSE HOD & faculty","ECE faculty","AI ML faculty","IT faculty","EEE faculty","Mechanical faculty","Civil faculty"],
        "Academics": ["R23 CSE subjects","R23 ECE subjects","R23 EEE subjects","R23 Civil subjects","R23 Mech subjects","Academic regulations"],
        "Placements": ["Placement overview","Top recruiters","Branch-wise stats","Highest packages","Internships"],
        "Campus": ["Hostel & mess","Library","Sports","Labs & infra","Transport","NCC & NSS"],
        "Admissions": ["Fee structure","Admission process","Scholarships","Contact & location"],
    }

    for section, questions in nav.items():
        st.markdown(f"""
        <div style="padding:12px 16px 4px;">
            <div style="color:#3D4A5C;font-size:9.5px;font-weight:600;text-transform:uppercase;letter-spacing:0.1em;">{section}</div>
        </div>
        """, unsafe_allow_html=True)
        for q in questions:
            if st.button(q, key=f"nav_{q}"):
                st.session_state.quick_query = q

    st.markdown("""
    <div style="padding:16px;border-top:1px solid #1C2333;margin-top:16px;">
        <div style="font-size:10.5px;color:#2A3444;line-height:1.8;">
            Built by <span style="color:#2563EB;font-weight:500;">Henry Joseph</span><br>
            VVIT · B.Tech CSE · 2026<br>
            <span style="color:#1C2333;">RAG · FAISS · Groq LLaMA 3.1</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Top bar
st.markdown("""
<div style="background:#0C1018;border-bottom:1px solid #1C2333;padding:12px 28px;display:flex;align-items:center;justify-content:space-between;">
    <div style="display:flex;align-items:center;gap:12px;">
        <div style="width:32px;height:32px;background:linear-gradient(135deg,#2563EB,#1D4ED8);border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:15px;">🎓</div>
        <div>
            <span style="color:#E8EDF5;font-weight:600;font-size:14.5px;">VVIT College Assistant</span>
            <span style="color:#3D4A5C;font-size:11.5px;margin-left:10px;">Vasireddy Venkatadri Institute of Technology · Guntur, AP</span>
        </div>
    </div>
    <div style="display:flex;gap:20px;align-items:center;">
        <div style="text-align:center;">
            <div style="color:#60A5FA;font-size:15px;font-weight:600;">15+</div>
            <div style="color:#3D4A5C;font-size:9.5px;text-transform:uppercase;letter-spacing:0.05em;">Depts</div>
        </div>
        <div style="width:1px;height:24px;background:#1C2333;"></div>
        <div style="text-align:center;">
            <div style="color:#60A5FA;font-size:15px;font-weight:600;">200+</div>
            <div style="color:#3D4A5C;font-size:9.5px;text-transform:uppercase;letter-spacing:0.05em;">Faculty</div>
        </div>
        <div style="width:1px;height:24px;background:#1C2333;"></div>
        <div style="text-align:center;">
            <div style="color:#60A5FA;font-size:15px;font-weight:600;">5K+</div>
            <div style="color:#3D4A5C;font-size:9.5px;text-transform:uppercase;letter-spacing:0.05em;">Students</div>
        </div>
        <div style="width:1px;height:24px;background:#1C2333;"></div>
        <div style="text-align:center;">
            <div style="color:#60A5FA;font-size:15px;font-weight:600;">100+</div>
            <div style="color:#3D4A5C;font-size:9.5px;text-transform:uppercase;letter-spacing:0.05em;">Recruiters</div>
        </div>
        <div style="width:1px;height:24px;background:#1C2333;"></div>
        <div style="background:#0D1F3C;border:1px solid #2563EB44;border-radius:6px;padding:5px 10px;display:flex;align-items:center;gap:5px;">
            <div style="width:7px;height:7px;background:#22C55E;border-radius:50%;"></div>
            <span style="color:#60A5FA;font-size:11px;font-weight:500;">Online</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

@st.cache_resource(show_spinner="Initializing VVIT knowledge base...")
def get_chain():
    from chatbot import load_qa_chain
    return load_qa_chain()

chain_tuple = get_chain()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "quick_query" not in st.session_state:
    st.session_state.quick_query = None

_, col_main, _ = st.columns([0.3, 9.4, 0.3])

with col_main:
    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)

    if not st.session_state.messages:
        st.markdown("""
        <div style="max-width:680px;margin:0 auto 32px;">
            <div style="margin-bottom:10px;">
                <span style="background:#0D1F3C;color:#60A5FA;padding:4px 10px;border-radius:4px;font-size:11px;border:1px solid #1E3A5F;font-weight:500;">VVIT · Official Knowledge Base</span>
            </div>
            <div style="color:#E8EDF5;font-size:24px;font-weight:600;line-height:1.3;margin-bottom:10px;">
                What would you like to<br>know about VVIT?
            </div>
            <div style="color:#8892A4;font-size:13.5px;line-height:1.7;margin-bottom:28px;">
                Ask about departments, faculty, R23 syllabus, placements,<br>campus life, admissions and more.
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;max-width:600px;">
                <div style="background:#0C1018;border:1px solid #1C2333;border-radius:10px;padding:14px 16px;">
                    <div style="color:#2563EB;font-size:20px;margin-bottom:8px;">📊</div>
                    <div style="color:#E8EDF5;font-size:13px;font-weight:500;margin-bottom:3px;">Placements</div>
                    <div style="color:#3D4A5C;font-size:12px;">Top packages, companies & stats</div>
                </div>
                <div style="background:#0C1018;border:1px solid #1C2333;border-radius:10px;padding:14px 16px;">
                    <div style="color:#2563EB;font-size:20px;margin-bottom:8px;">📚</div>
                    <div style="color:#E8EDF5;font-size:13px;font-weight:500;margin-bottom:3px;">R23 Syllabus</div>
                    <div style="color:#3D4A5C;font-size:12px;">Subjects by branch & semester</div>
                </div>
                <div style="background:#0C1018;border:1px solid #1C2333;border-radius:10px;padding:14px 16px;">
                    <div style="color:#2563EB;font-size:20px;margin-bottom:8px;">👨‍🏫</div>
                    <div style="color:#E8EDF5;font-size:13px;font-weight:500;margin-bottom:3px;">Faculty</div>
                    <div style="color:#3D4A5C;font-size:12px;">HODs, professors & research</div>
                </div>
                <div style="background:#0C1018;border:1px solid #1C2333;border-radius:10px;padding:14px 16px;">
                    <div style="color:#2563EB;font-size:20px;margin-bottom:8px;">🏛️</div>
                    <div style="color:#E8EDF5;font-size:13px;font-weight:500;margin-bottom:3px;">Campus Life</div>
                    <div style="color:#3D4A5C;font-size:12px;">Hostel, labs, sports & clubs</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("sources"):
                with st.expander("View sources", expanded=False):
                    for src in msg["sources"]:
                        st.caption(f"📄 {src}")

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
                    doc.metadata.get('source','').replace('data\\','').replace('data/','')
                    for doc in sources if doc.metadata.get('source')
                ))
                if source_list:
                    with st.expander("View sources", expanded=False):
                        for src in source_list:
                            st.caption(f"📄 {src}")
        st.session_state.messages.append({
            "role": "assistant", "content": answer, "sources": source_list
        })
        st.rerun()

    if st.session_state.messages:
        st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
        _, c2, _ = st.columns([5,2,5])
        with c2:
            if st.button("Clear conversation", key="clear"):
                st.session_state.messages = []
                st.rerun()
