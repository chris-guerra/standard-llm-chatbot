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

# Set the title of the app
st.title("Chatbot with FastAPI and OpenAI")

# Initialize session state to store conversation history if it doesn't exist
if "history" not in st.session_state:
    st.session_state.history = []

# Display chat history
if st.session_state.history:
    for chat in st.session_state.history:
        if chat["role"] == "user":
            st.write(f"You: {chat['content']}")
        elif chat["role"] == "assistant":
            st.write(f"Bot: {chat['content']}")

# Create a form to allow submitting with both the "Send" button and the "Enter" key
with st.form(key="chat_form"):
    user_input = st.text_input("You: ", placeholder="Type your message here...")
    submit_button = st.form_submit_button(label="Send")

if submit_button:
    if user_input.strip():
        try:
            # Make a POST request to the backend with the user's message and the conversation history
            with st.spinner("Waiting for response..."):
                response = requests.post(
                    "http://backend:8000/chat/",
                    json={"message": user_input, "history": st.session_state.history},
                    timeout=10
                )

            if response.status_code == 200:
                data = response.json()

                # Update the session state with the new history
                st.session_state.history = data.get("history", [])

                # Refresh the page to show updated history
                st.rerun()

            else:
                st.error(f"Error {response.status_code}: {response.text}")

        except requests.exceptions.Timeout:
            st.error("The request timed out. Please try again later.")

        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred while connecting to the backend: {e}")

    else:
        st.warning("Please enter a message before sending.")
