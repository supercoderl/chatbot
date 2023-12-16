#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: Madhav (https://github.com/madhav-mknc)


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
HOST = "0.0.0.0"
PORT = 8080


# only logged in access
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('authenticated'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# # GOOGLE API AUTHENTICATION
# state = session['state']
# flow = Flow.from_client_secrets_file(
#     'client_secret.json',
#     scopes=['https://www.googleapis.com/auth/drive.readonly'],
#     state=state)
# flow.redirect_uri = url_for('oauth2callback', _external=True)

# authorization_response = request.url
# flow.fetch_token(authorization_response=authorization_response)

# # Store the credentials in the session.
# # ACTION ITEM for developers:
# #     Store user's access and refresh tokens in your data store if
# #     incorporating this code into your real app.
# credentials = flow.credentials
# session['credentials'] = {
#     'token': credentials.token,
#     'refresh_token': credentials.refresh_token,
#     'token_uri': credentials.token_uri,
#     'client_id': credentials.client_id,
#     'client_secret': credentials.client_secret,
#     'scopes': credentials.scopes}
# flow = Flow.from_client_secrets_file('client_secret.json', SCOPES)
# flow.redirect_uri = REDIRECT_URI




# Routes below:
"""
/           => index
/login      => admin login page
/dashboard  => admin dashboard
/upload     => for uploading files
/handle_url => fetch data from URLs
/delete     => for deleting a uploaded file
/chatbot    => redirect to chatbot
/get_chat_response => for fetching response from the chatbot
/logout     => admin logout
"""


# # index
# @app.route('/')
# def index():
#     return render_template('index.html')

# get response from chatbot
@app.route('/get_chat_response', methods=['POST'])
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
