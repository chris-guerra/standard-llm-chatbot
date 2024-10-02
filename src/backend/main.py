"""
main.py

This module defines the FastAPI application that exposes an endpoint to interact with
the OpenAI API. It handles incoming user messages, passes them to the OpenAI service
for processing, and returns the response. The module also includes error handling
for validation, HTTP exceptions, and other server-side issues.
"""

import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from src.services.openai_service import get_openai_response

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Pydantic model for the input
class Message(BaseModel):
    """
    Message model for the request body.

    Attributes:
        message (str): The input message provided by the user to be sent to the OpenAI API.
    """
    message: str

@app.post("/chat/")
async def chat(message: Message):
    """
    Handles POST requests to the /chat/ endpoint. Accepts a message from the user
    and returns a response from the OpenAI model.

    :param message: Message object containing the user's input message.
    :return: JSON response with the AI's response.
    """
    try:
        # Log the incoming request
        logger.info("Received message: %s", message.message)

        # Get the OpenAI response
        response = get_openai_response(message.message)

        # Log the successful response
        logger.info("OpenAI response: %s", response)

        return {"response": response}
    except ValidationError as e:
        # Log validation errors (e.g., malformed request body)
        logger.error("Validation error: %s", e)
        raise HTTPException(status_code=422, detail="Invalid input format.") from e

    except HTTPException as e:
        # Log HTTP-specific errors
        logger.error("HTTP exception occurred: %s", e)
        raise e  # Re-raise HTTP exceptions directly

    except Exception as e:
        # Log generic server errors
        logger.error("An error occurred while processing the request: %s", e)
        raise HTTPException(status_code=500, detail="Internal server error.") from e
