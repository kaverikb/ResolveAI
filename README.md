# ResolveAI - Customer Support Chatbot

An intelligent customer support chatbot system built with FastAPI backend and the Trinity Large Thinking model from OpenRouter. The application features emotion detection and generates contextually appropriate, empathetic responses to customer queries.

## Overview

ResolveAI is a full-stack web application that automates customer support interactions by analyzing customer sentiment and providing personalized responses. The system uses the Arcee AI Trinity Large Thinking model via OpenRouter's API to understand context and generate intelligent responses.

## Technology Stack

### Backend
- FastAPI - REST API framework for Python
- Uvicorn - ASGI web server
- Pydantic - Data validation and settings management
- Python-dotenv - Environment variable management
- Requests - HTTP client library

### Frontend
- HTML5 - Markup structure
- CSS3 - Styling and layout
- JavaScript (Vanilla) - Client-side functionality
- HTTP - Client-server communication

### AI/ML
- Arcee AI Trinity Large Thinking (via OpenRouter API)
- Model: arcee-ai/trinity-large-thinking:free
- Context window: 262K tokens
- Max output: 80K tokens

### Development Tools
- Git - Version control
- Python 3.8+ - Runtime environment
- Virtual environments (venv) - Dependency isolation

## Project Structure
ResolveAI/
- backend/
  - main.py
  - requirements.txt
  - app/
    - __init__.py
    - chat.py
    - schemas/
      - __init__.py
      - chat.py
    - models/
      - __init__.py
      - emotion_detector.py
- frontend/
  - index.html
  - style.css
  - script.js
- ml_models/
  - emotion_detector/
    - __init__.py
    - model.py
    - model_loader.py
    - text_processor.py
- .env
- .gitignore
- README.md

## API Documentation

### Chat Endpoint

**Endpoint:** `POST /api/chat/message`

**Request Body:**
```json
{
  "message": "I'm frustrated with your service!"
}
```

**Response:**
```json
{
  "response": "I understand your frustration. Let me help you resolve this issue.",
  "emotion": "frustration"
}
```

**Supported Emotions:**
- anger
- frustration
- urgency
- sadness
- happiness
- neutral


## How It Works

1. User sends a message through the web interface
2. Frontend sends POST request to `/api/chat/message`
3. Backend receives the message and sends it to Trinity API
4. Trinity API analyzes the message for emotion and generates a response
5. Backend parses the API response and extracts emotion and reply
6. Frontend receives JSON response and displays it with emotion indicator
7. Chat history is maintained in the UI during the session

## Features

### Emotion Detection
The system analyzes incoming messages to detect customer emotions:
- Analyzes sentiment and context
- Classifies emotions into six categories
- Influences response tone and approach

### Empathetic Responses
- Generates contextually appropriate replies
- Adapts tone based on detected emotion
- Provides helpful and supportive messages
