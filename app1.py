import streamlit as st
from agent_backend import run_agent

st.set_page_config(page_title="LangGraph Chat", layout="wide")

st.title("🧠 LangGraph Chat Interface")

# Use session state to preserve chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Sidebar for prompt input
with st.sidebar:
    st.header("📝 Enter Prompt")
    user_input = st.text_area("Your message:", height=150)
    if st.button("Send"):
        if user_input.strip():
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.spinner("Thinking..."):
                response = run_agent(user_input)
            st.session_state.messages.append({"role": "agent", "content": response})
        else:
            st.warning("Please enter a message.")

# Chat bubble style
def render_chat_bubble(role, content):
    if role == "user":
        st.markdown(
            f"""
            <div style="background-color:#DCF8C6;border-radius:10px;padding:10px;margin:10px 0;width:fit-content;max-width:80%;align-self:flex-end;">
                <strong>You:</strong><br>{content}
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div style="background-color:#F1F0F0;border-radius:10px;padding:10px;margin:10px 0;width:fit-content;max-width:80%;">
                <strong>Agent:</strong><br>{content}
            </div>
            """,
            unsafe_allow_html=True,
        )

# Display conversation
for msg in st.session_state.messages:
    render_chat_bubble(msg["role"], msg["content"])
