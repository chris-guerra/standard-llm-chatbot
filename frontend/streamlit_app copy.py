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
import os
import requests
import streamlit as st

st.title("Chatbot with FastAPI and OpenAI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = requests.post(
            "http://backend:8000/chat/",
            json={"messages": st.session_state.messages},
            timeout=10
            )

        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})