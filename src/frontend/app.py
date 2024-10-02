import streamlit as st
import requests

st.title("Chatbot with FastAPI and OpenAI")

user_input = st.text_input("You: ", "Hello, how are you?")
if st.button("Send"):
    if user_input:
        response = requests.post("http://backend:8000/chat/", json={"message": user_input})
        if response.status_code == 200:
            st.write("Bot: " + response.json().get("response"))
        else:
            st.write("Error: " + response.text)
