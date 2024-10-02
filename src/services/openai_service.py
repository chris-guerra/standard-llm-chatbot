import os
from openai import OpenAI


client = OpenAI()

MODEL = os.getenv("OPENAI_CHAT_MODEL")

def get_openai_response(message: str) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
    ]

    response = client.chat.completions.create(
        model= MODEL,
        temperature= 0,
        messages= messages
    )

    return response.choices[0].message.content
