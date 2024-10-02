"""
main.py

This module defines the FastAPI application that exposes an endpoint to interact with
the OpenAI API. It handles incoming user messages, passes them to the OpenAI service
for processing, and returns the response. The module also includes error handling
for validation, HTTP exceptions, and other server-side issues.
"""

import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.services.openai_service import get_openai_response

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Pydantic model for the input
class ChatRequest(BaseModel):
    """
    Message model for the request body.

    Attributes:
        message (str): The input message provided by the user to be sent to the OpenAI API.
    """
    message: str
    history: list = []

@app.post("/chat/")
async def chat(request: ChatRequest):
    """
    Handles POST requests to the /chat/ endpoint. Accepts a message from the user
    and returns a response from the OpenAI model.

    :param message: Message object containing the user's input message.
    :return: JSON response with the AI's response.
    """
    try:
        logger.info(f"Received message: {request.message}")

        # Pass the user's message and chat history to OpenAI
        response, updated_history = get_openai_response(request.message, request.history)

        logger.info("History: %s", updated_history)
        logger.info("OpenAI response: %s", response)
        return {"response": response, "history": updated_history}

    except Exception as e:
        logger.error(f"Error processing the request: {e}")
        raise HTTPException(status_code=500, detail="Internal server error.")

