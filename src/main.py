"""
main.py

This module defines the FastAPI application that exposes an endpoint to interact with
the OpenAI API. It handles incoming user messages, passes them to the OpenAI service
for processing, and returns the response. The module also includes error handling
for validation, HTTP exceptions, and other server-side issues.
"""
from fastapi import FastAPI
from src.api import chat
from src.utils.logging_config import setup_logging

# Initialize logging
setup_logging()

# Create FastAPI app
app = FastAPI()

# Include the chat API routes
app.include_router(chat.router)

@app.get("/")
def read_root():
    """
    Root endpoint to verify the API is running.
    """
    return {"message": "AI Live Chat API is running!"}
