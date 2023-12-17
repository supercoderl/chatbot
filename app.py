from flask import (
    Flask, 
    render_template,
    request,
    redirect, 
    url_for, 
    session, 
    flash, 
    jsonify
)
from werkzeug.utils import secure_filename
from functools import wraps
from waitress import serve
from flask_cors import CORS

# from google_auth_oauthlib.flow import Flow

from utils.utils import *
from utils import chatbot

import os
from dotenv import load_dotenv
load_dotenv()

# Initialzing flask app
app = Flask(__name__)

# Enable CORS
CORS(app)

# secret key
app.secret_key = os.getenv("FLASK_SECRET_KEY")  # Change this to a strong random key in a production environment
# app.secret_key = str(unique_id()).replace("-","")

# server address
HOST = "localhost"
PORT = 1536

# Routes below:
"""
/           => index
/chatbot    => redirect to chatbot
/chat => for fetching response from the chatbot
"""


# # index
# @app.route('/')
# def index():
#     return render_template('index.html')

# get response from chatbot
@app.route('/chat', methods=['POST'])
def get_chat_response():
    user_input = request.json['message']
    response = chatbot.get_response(query=user_input)
    return jsonify({'message': response})

# chatbot
@app.route('/chatbot')
def chat():
    return render_template('chat.html')

# run server
def start_server():
    serve(app, host=HOST, port=PORT)

if __name__ == '__main__':
    start_server()
