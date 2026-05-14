from fastapi import APIRouter
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/api/chat", tags=["chat"])

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL", "https://openrouter.ai/api/v1")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    emotion: str

@router.post("/message", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "HTTP-Referer": "http://localhost:3000",
            "X-Title": "ResolveAI",
        }

        system_prompt = """You are an empathetic customer support AI. 
Analyze the customer's emotion and provide a helpful response.

Always respond in this exact format:
EMOTION: [one of: anger, frustration, urgency, sadness, happiness, neutral]
RESPONSE: [your helpful response]"""

        payload = {
            "model": "arcee-ai/trinity-large-thinking:free",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": request.message}
            ],
            "temperature": 0.7,
            "max_tokens": 300,
        }

        response = requests.post(
            f"{API_BASE_URL}/chat/completions",
            headers=headers,
            json=payload,
            timeout=60
        )

        if response.status_code != 200:
            print(f"API Error: {response.status_code} - {response.text}")
            return ChatResponse(
                response="I'm having trouble connecting. Please try again.",
                emotion="neutral"
            )

        data = response.json()
        content = data["choices"][0]["message"]["content"]

        # Parse response
        emotion = "neutral"
        bot_response = content

        if "EMOTION:" in content and "RESPONSE:" in content:
            parts = content.split("RESPONSE:")
            emotion_part = parts[0].split("EMOTION:")
            
            if len(emotion_part) > 1:
                emotion = emotion_part[1].strip().split()[0].lower()
            
            if len(parts) > 1:
                bot_response = parts[1].strip()

        valid_emotions = ["anger", "frustration", "urgency", "sadness", "happiness", "neutral"]
        if emotion not in valid_emotions:
            emotion = "neutral"

        return ChatResponse(response=bot_response, emotion=emotion)

    except Exception as e:
        print(f"Error: {str(e)}")
        return ChatResponse(
            response=f"Error: {str(e)}",
            emotion="neutral"
        )
