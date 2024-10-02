from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.services.openai_service import get_openai_response

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/chat/")
async def chat(message: Message):
    try:
        response = get_openai_response(message.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
