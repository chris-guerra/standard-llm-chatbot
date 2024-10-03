"""
openai_service.py

This module provides a function to interact with the OpenAI API, allowing users to send a message
and receive a response from an AI model. It includes error handling and logging to ensure that
errors are captured and logged appropriately.
"""
import os
import logging
from typing import Generator, Optional
from src.services.base_ai_service import BaseAIService
from openai import OpenAI

logger = logging.getLogger(__name__)

class OpenAIService(BaseAIService):
    """
    Service class for interacting with the OpenAI API.
    Implements the get_chat_stream method defined in the BaseAIService interface.
    """

    def __init__(self):
        """
        Initializes the OpenAI client.
        """
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("OPENAI_CHAT_MODEL")
        self.client = OpenAI(api_key= self.openai_api_key)

    def get_chat_stream(
            self, 
            messages: list, 
            model: Optional[str] = None, 
            temperature: float = 0.0) -> Generator[str, None, None]:
        """
        Creates a streaming chat completion using OpenAI.

        Args:
            messages (list): A list of message dictionaries to be passed to the OpenAI API.
            model (str): The name of the OpenAI model to use.
            temperature (float): The LLM temperature.

        Returns:
            Generator[str, None, None]: A generator yielding chat response chunks from OpenAI.
        """
        if model is None:
            model = self.model
        
        logger.info(f"openai_chat_stream_started_for_model: {model}")
        
        try:
            openai_chat_stream = self.client.chat.completions.create(
                model= model,
                temperature= temperature,
                messages= messages,
                stream= True
            )
        
            for chunk in openai_chat_stream:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content
        
        except Exception as e:
            logger.error(f"openai_chat_stream_error: {e}")
            raise
