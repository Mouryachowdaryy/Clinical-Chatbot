import streamlit as st
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key="AIzaSyCKmAUfa7Y2MHdYBbKdswqivKFkUEEGGxg")

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

# Streamlit page setup
st.set_page_config(page_title="Clinical Chatbot", page_icon="👩‍⚕️")
st.title("Clinical Assistant Chatbot")
st.markdown("This is an AI assistant trained on medical knowledge. Please consult a doctor for serious issues.")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display message history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_query = st.chat_input("Ask a health-related question...")

if user_query:
    # User message
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # Gemini response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat.send_message(user_query)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})