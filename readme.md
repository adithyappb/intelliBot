## IntelliBot
IntelliBot is an advanced AI chatbot developed for the InGenius 2018 hackathon at PESU. It leverages natural language processing (NLP) and machine learning techniques to provide interactive and intelligent responses.

## Features
- **Natural Language Understanding**: Uses NLP models to understand and interpret user queries.
- **Contextual Responses**: Maintains context across conversations for more meaningful interactions.
- **Multi-platform Support**: Accessible via web interface, mobile app, and messaging platforms.
- **Customizable Plugins**: Extendable with plugins for specific tasks or integrations.
- **Analytics and Reporting**: Provides insights into user interactions and frequently asked questions.

## Technologies Used
- **Python**: Backend development and NLP processing.
- **Flask**: Web framework for backend API.
- **NLTK and SpaCy**: Libraries for natural language processing.
- **TensorFlow**: Machine learning framework for model training.
- **React.js**: Frontend development for web interface.
- **Docker**: Containerization for deployment and scalability.

## Getting Started
# Prerequisites
- Python 3.6+
- Node.js and npm (for frontend development)
- Docker (optional for deployment)

## Installation
# Set up the backend:
1) cd backend
2) python -m venv venv
3) source venv/bin/activate  # On Windows use `venv\Scripts\activate`
4) pip install -r requirements.txt

# Set up the frontend:
1) cd ../frontend
2) npm install

## Running the Application
# Start the backend server:
1) cd ../backend
2) python app.py

# Start the frontend development server:
1) cd ../frontend
2) npm start
3) Open http://localhost:3000 in your browser to access IntelliBot.

## Usage
1) Enter your queries in the chat interface.
2) IntelliBot will process your query using NLP and provide appropriate responses.
3) Explore different functionalities and plugins by interacting with the bot.
