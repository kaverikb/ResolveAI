const API_BASE_URL = 'http://localhost:5000';

async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const message = userInput.value.trim();
    
    if (!message) return;
    
    addMessage(message, 'user');
    userInput.value = '';
    
    try {
        const response = await fetch(API_BASE_URL + '/api/chat/message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message })
        });
        
        if (!response.ok) {
            throw new Error('Failed to get response');
        }
        
        const data = await response.json();
        addMessage(data.response, 'bot');
        updateEmotionIndicator(data.emotion);
        
    } catch (error) {
        console.error('Error:', error);
        addMessage('Sorry, error. Try again.', 'bot');
    }
}

function addMessage(text, sender) {
    const chatBox = document.getElementById('chatBox');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message ' + sender + '-message';
    const p = document.createElement('p');
    p.textContent = text;
    messageDiv.appendChild(p);
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function updateEmotionIndicator(emotion) {
    const indicator = document.getElementById('emotionIndicator');
    indicator.className = 'emotion-indicator ' + emotion;
    indicator.textContent = 'Detected emotion: ' + emotion.toUpperCase();
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}
