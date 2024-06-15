# Responses based on intents
responses = {
    'greeting': "Hello! How can I assist you today?",
    'weather': "The weather is sunny with a temperature of 25°C.",
    'restaurant_search': "Here are some restaurants near you: Restaurant A, Restaurant B, Restaurant C.",
    'default': "I'm sorry, I didn't understand that.",
}

# Function to generate response
def generate_response(intent):
    return responses.get(intent, responses['default'])

