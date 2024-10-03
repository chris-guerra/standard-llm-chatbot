# src/services/base_ai_service.py
from abc import ABC, abstractmethod
from typing import Generator, Optional

class BaseAIService(ABC):
    """
    Abstract base class for AI services.

    Defines the contract that each AI service must implement, ensuring consistency
    in how they generate chat streams.
    """

    @abstractmethod
    def get_chat_stream(self, 
            messages: list, 
            model: Optional[str] = None, 
            temperature: float = 0.0) -> Generator[str, None, None]:
        """
        Abstract method to generate a stream of chat responses.

        Args:
            messages (list): A list of message dictionaries to be passed to the OpenAI API.
            model (str): The name of the OpenAI model to use.
            temperature (float): The LLM temperature.

        Returns:
            Generator[str, None, None]: A generator yielding chat response chunks.
        """
        pass