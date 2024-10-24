"""
app.py

This Streamlit application serves as the frontend interface for a chatbot that interacts
with a FastAPI backend using the OpenAI API. The user inputs a message through the 
Streamlit interface, and the message is sent to the backend via an HTTP POST request. 
The backend processes the request using OpenAI and returns a response, which is displayed
in the frontend.

Key Features:
- Allows users to input messages and submit them via a "Send" button or by pressing "Enter".
- Displays the chatbot's response retrieved from the FastAPI backend.
- Provides feedback through loading spinners and error messages if the request fails.
- Uses a form to handle user input submission to improve user experience.

Components:
- Streamlit for the frontend interface.
- FastAPI for the backend API.
- OpenAI API for chatbot responses.
"""
import streamlit as st
import requests
import json

# App title
st.set_page_config(page_title="Custom LLM Chatbot")

# Sidebar
with st.sidebar:
    st.title('Custom LLM Chatbot')
    st.subheader('Models and parameters')
    st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-a-llama-2-chatbot/)!')

#---------------------
# Main View
#---------------------

# Initialize session state for storing chat history and model
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Accept user input
if prompt := st.chat_input("Write your response here."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Prepare the chat history as payload
    payload = {
        "messages": [
            {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
            ]
        }

    with st.chat_message("assistant"):
        stream = requests.post("http://backend:8000/live-chat", 
                       json=payload,
                       stream=True,  # Important to set stream=True
                       timeout=10)

        if stream.status_code == 200:
            for chunk in stream.iter_content(chunk_size=None):
                if chunk:
                    st.session_state.messages.append({"role": "assistant", "content": chunk.decode('utf-8')})
                    st.markdown(chunk.decode('utf-8'))
        else:
            st.error("Error occurred while getting response from server.")








