import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL", "https://openrouter.ai/api/v1")

class EmotionDetector:
    """
    Detect customer emotion using Trinity API from OpenRouter
    """
    
    def __init__(self):
        self.api_key = OPENROUTER_API_KEY
        self.api_base = API_BASE_URL
    
    def detect_emotion(self, text: str) -> str:
        """
        Analyze text and return detected emotion
        """
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }
            
            prompt = f"Analyze the emotion in this message. Respond with ONLY ONE word: anger, frustration, urgency, sadness, happiness, or neutral. Message: {text}"
            
            payload = {
                "model": "openai/gpt-3.5-turbo",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 10,
            }
            
            response = requests.post(
                f"{self.api_base}/chat/completions",
                headers=headers,
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                content = response.json()["choices"][0]["message"]["content"].strip().lower()
                valid_emotions = ["anger", "frustration", "urgency", "sadness", "happiness", "neutral"]
                return content if content in valid_emotions else "neutral"
            
            return "neutral"
        except Exception as e:
            print(f"Emotion detection error: {e}")
            return "neutral"

emotion_detector = EmotionDetector()
