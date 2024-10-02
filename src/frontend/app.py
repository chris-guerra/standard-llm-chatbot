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

# Create a form to allow submitting with both the "Send" button and the "Enter" key
with st.form(key="chat_form"):
    # Get user input with a default placeholder
    user_input = st.text_input("You: ", placeholder="Type your message here...")

    # Button to send the user input to the backend API
    submit_button = st.form_submit_button(label="Send")

# Only proceed after the form is submitted (either by clicking the button or pressing Enter)
if submit_button:
    if user_input.strip():  # Ensure input isn't just whitespace
        try:
            # Display a spinner while waiting for the response
            with st.spinner("Waiting for response..."):
                # Make a POST request to the backend with a timeout
                response = requests.post(
                    "http://backend:8000/chat/", 
                    json={"message": user_input}, 
                    timeout=10
                    )

            # Handle the response
            if response.status_code == 200:
                st.write("Bot: " + response.json().get("response", "No response received"))
            else:
                st.error(f"Error {response.status_code}: {response.text}")

        except requests.exceptions.Timeout:
            # Handle timeout specifically
            st.error("The request timed out. Please try again later.")

        except requests.exceptions.RequestException as e:
            # Handle any request-related errors, such as network issues
            st.error(f"An error occurred while connecting to the backend: {e}")
    else:
        # Only display the warning if the user has submitted an empty message
        st.warning("Please enter a message before sending.")
