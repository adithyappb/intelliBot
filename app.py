from flask import Flask, request, jsonify
from model.intent_classifier import predict_intent
from model.response_generator import generate_response

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    message = request.json['message']
    intent = predict_intent(message)
    response = generate_response(intent)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

