"""
openai_service.py

This module provides a function to interact with the OpenAI API, allowing users to send a message
and receive a response from an AI model. It includes error handling and logging to ensure that
errors are captured and logged appropriately.
"""

import os
import logging
from openai import OpenAI
from requests.exceptions import HTTPError, Timeout

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load the model name from the environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_CHAT_MODEL")

# Make sure the environment variable is set
if not MODEL:
    logger.error("OPENAI_CHAT_MODEL environment variable is not set.")
    raise ValueError(
        "Missing OpenAI model configuration. Please set \
            the OPENAI_CHAT_MODEL environment variable.")

# We add our OpenAI Client
client = OpenAI(api_key=OPENAI_API_KEY)

def get_openai_response(messages: list) -> str:
    """
    Sends a message to the OpenAI API and retrieves the response, while considering previous conversation history.

    :param message: The user's input message to be processed by OpenAI.
    :param history: The previous conversation history.
    :return: The response generated by the OpenAI model and the updated history.
    """

    try:
        response = client.chat.completions.create(
            model=MODEL,
            temperature=0,
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in messages],
            stream=True
        )
        assistant_message = response.choices

        # Add the assistant's response to the conversation history
        return assistant_message

    except Exception as e:
        logger.error(f"Error occurred while contacting OpenAI: {e}")
        raise RuntimeError(f"An error occurred: {e}")