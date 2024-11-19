from flask import Flask, request, jsonify, send_from_directory  # Importing necessary libraries
from chatbot import ChatBot  # Importing the ChatBot class from chatbot.py
import os  # Importing the os module to access environment variables
from dotenv import load_dotenv  # Importing the load_dotenv function to load environment variables from .env file
from datetime import datetime, timedelta  # Importing the datetime and timedelta classes from the datetime module

# Initialize Flask app
app = Flask(__name__, static_folder='client/dist', static_url_path='')

# Load environment variables
load_dotenv()

# Initialize ChatBot
api_key = os.getenv('GOOGLE_API_KEY')
chatbot = ChatBot(api_key=api_key)


# Helper function to get current time
def get_time():
    current_time = datetime.now()
    if current_time.microsecond >= 500_000:
        rounded_time = current_time + timedelta(seconds=1)
    else:
        rounded_time = current_time
    return rounded_time.replace(microsecond=0)


# API endpoint to handle chat messages
@app.route('/api/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_input = data.get("message")

    if user_input.lower() == 'exit':
        return jsonify({"response": "Goodbye!"}), 200

    try:
        response = chatbot.send_prompt(user_input)
        time = get_time()
        # Instead of saving chat history to Firebase, you can store it in memory or a file if needed
        chatHistory = dict(prompt=user_input, response=response)
        # You can log chat history or store it elsewhere if needed
        print(f"Chat History: {chatHistory}")  # Logging to console for now
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Convert exception to string


# API endpoint to get chat history (this is no longer fetching from Firebase, so you may want to store in memory)
@app.route('/api/chat_history', methods=['GET'])
def get_chat_history():
    # If you want to return stored chat history, you would need to store it in a variable (e.g., a list)
    chat_history = []  # This would be where you store history
    return jsonify(chat_history)


# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_file = os.path.join(app.static_folder, path)

    # Check if the requested path is available as a file
    if path != "" and os.path.exists(static_file):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(debug=True)
