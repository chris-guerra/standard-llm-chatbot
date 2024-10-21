import logging
from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from src.services.openai_service import OpenAIService
from src.services.base_ai_service import BaseAIService

router = APIRouter()
logger = logging.getLogger(__name__)

# Instantiate services (only OpenAI for now, but easily expandable)
openai_service = OpenAIService()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

def get_ai_service(service_name: str) -> BaseAIService:
    """
    Returns the appropriate AI service based on the provided service name.
    Currently supports only OpenAI, but designed to be expandable.
    
    Args:
        service_name (str): The name of the AI service to use ("openai").

    Returns:
        BaseAIService: An instance of the appropriate AI service.
    
    Raises:
        ValueError: If the service name is invalid.
    """
    logger.info(f"requested_service: {service_name}")
    if service_name == "openai":
        return openai_service
    else:
        logger.error(f"unknown_service_error: {service_name}")
        raise ValueError("Unknown service")

async def stream_openai_response(messages: List[Message]):
    """
    Streams the OpenAI response for a list of messages.
    """
    try:
        service = get_ai_service("openai")

        # Convert Pydantic models into the correct dictionary format for OpenAI
        formatted_messages = [{"role": message["role"], "content": message["content"]} for message in messages]
        
        # Pass the formatted messages to the OpenAI API
        response = service.get_chat_stream(messages=formatted_messages)

        # Stream the response chunks back to the client
        for chunk in response:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    except Exception as e:
        logger.error(f"error_streaming_response: {e}")
        raise HTTPException(status_code=500, detail="Error occurred while streaming response from OpenAI")

@router.post("/live-chat")
async def live_chat(request: ChatRequest):
    """
    API endpoint to process live chat by streaming the AI's response to the user input.
    Accepts a list of previous messages (chat history) and sends them to the AI model.
    """
    return StreamingResponse(stream_openai_response(messages = request.messages), media_type="text/plain")