# ResolveAI - Customer Support Chatbot

An AI-powered customer support chatbot using FastAPI backend and Trinity API from OpenRouter.

## Features
- ?? AI-powered responses using Trinity API
- ?? Emotion detection and empathetic responses
- ? Fast and lightweight
- ?? Secure API key management with .env
- ?? Clean, modern web interface

## Project Structure

\\\
ResolveAI/
+-- backend/
¦   +-- main.py
¦   +-- requirements.txt
¦   +-- app/
¦       +-- chat.py
¦       +-- schemas/
¦       ¦   +-- chat.py
¦       +-- models/
¦           +-- emotion_detector.py
+-- frontend/
¦   +-- index.html
¦   +-- style.css
¦   +-- script.js
+-- ml_models/
¦   +-- emotion_detector/
¦       +-- model.py
¦       +-- model_loader.py
¦       +-- text_processor.py
+-- .env.example
+-- .env (local only)
+-- .gitignore
+-- README.md
\\\

## Setup

### 1. Install Backend Dependencies
\\\ash
cd backend
pip install -r requirements.txt
\\\

### 2. Configure Environment Variables
\\\ash
cp .env.example .env
# Edit .env and add your Trinity API key from OpenRouter
OPENROUTER_API_KEY=your_actual_key_here
\\\

### 3. Run Backend Server
\\\ash
cd backend
python main.py
\\\

The API will run at \http://localhost:8000\

### 4. Open Frontend
Open \rontend/index.html\ in your browser

## API Endpoints

### POST /api/chat/message
Send a message and get an emotionally-aware response

**Request:**
\\\json
{
  "message": "I'm frustrated with your service!"
}
\\\

**Response:**
\\\json
{
  "response": "I understand your frustration. Let me help you resolve this issue...",
  "emotion": "frustration"
}
\\\

## Using Trinity API

Trinity API is used through OpenRouter for emotion detection and response generation.

Get your API key from [OpenRouter.ai](https://openrouter.ai)

## Important Security Notes

?? **Never commit .env to GitHub!**
- \.env\ contains your API keys
- \.gitignore\ already excludes it
- Share \.env.example\ instead (without actual keys)

When sharing the project:
1. Your friend gets the code from GitHub
2. They copy \.env.example\ to \.env\
3. They add their own OpenRouter Trinity API key
4. Everything works without exposing secrets

## Future Improvements
- [ ] Conversation memory
- [ ] Multi-user support with database
- [ ] Advanced emotion detection models
- [ ] Ticketing system integration
- [ ] Conversation analytics

## License
MIT
