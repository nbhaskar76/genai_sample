import streamlit as st
from chat import chat_with_llm  # This version should NOT update history

st.title("Chatbot (via Ollama API)")

if "history" not in st.session_state:
    st.session_state.history = []

def submit():
    user_input = st.session_state.user_input
    if user_input:
        # Append user message to history
        st.session_state.history.append({"role": "user", "content": user_input})
        
        # Get assistant reply — assume chat_with_llm does NOT touch history
        reply, _ = chat_with_llm(user_input, st.session_state.history)
        
        # Append assistant message
        st.session_state.history.append({"role": "assistant", "content": reply})
        
        # Clear input box
        st.session_state.user_input = ""

# Display chat history
st.text_area(
    "Chat History",
    value="\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.history]),
    height=400,
    key="chat_area",
    disabled=True,
)

# Input field
st.text_input("Your message:", key="user_input", on_change=submit)

st.write("---")
st.write("Type your message and press Enter to chat!")
