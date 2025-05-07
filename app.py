from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.getenv("8113437583:AAHZV8N_Vuzum1qVMLSo1cDa6HX01L8OPgM")
CHAT_ID = os.getenv("-4726006563")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route('/message', methods=['POST'])
def send_message():
    message = request.json.get('message')
    if message:
        data = {
            'chat_id': CHAT_ID,
            'text': he writes
        }
        requests.post(TELEGRAM_API_URL, data=data)
        return "Message sent", 200
    return "No message provided", 400

@app.route('/')
def home():
    return "Бот работает!", 200
