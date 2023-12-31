# author: Madhav (https://github.com/madhav-mknc)
# utilties / helper functions for app.py

from utils.manage_vectordb import add_file, delete_file, list_files

import os
import sys
import json
import hashlib

from urllib.parse import urlparse
import requests

# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import Flow
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.http import MediaFileUpload


# Check if the uploaded file has an allowed extension (customize this list as needed)
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx', 'csv'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# check if the parameter is a url
def is_url(filename):
    parsed_url = urlparse(filename)
    return parsed_url.scheme != '' and parsed_url.netloc != ''

# for validating the url
def valid_url(url):
    try:
        response = requests.head(
            url = url,
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        )
        return response.status_code == 200
    except requests.RequestException:
        return False

# Function to handle URLs
def handle_urls(url):
    if not valid_url(url):
        return "Invalid URL"

    upload_file_to_pinecone(file=url, isurl=True)
    return "Data Fetched Successfully"



# # GOOGLE DRIVE OPERATIONS 

# PATH = "./client_secret.json"
# with open(PATH, "r") as json_file:
#     content = json.load(json_file)

# REDIRECT_URIS = content["web"]["redirect_uris"]
# REDIRECT_URI = REDIRECT_URIS[0]
# JAVASCRIPT_ORIGINS = content["web"]["javascript_origins"]
# SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# flow = Flow.from_client_secrets_file(
#     'client_secret.json',
#     scopes=['https://www.googleapis.com/auth/drive.metadata.readonly']
# )
# flow.redirect_uri = 'http://localhost:8080/oauth2callback'
# flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
# credentials = flow.run_local_server(port=0)

# # Function to upload file to Google Drive
# def upload_to_google_drive(file_path):
#     service = build('drive', 'v3', credentials=credentials)

#     file_metadata = {'name': os.path.basename(file_path)}
#     media = MediaFileUpload(file_path, resumable=True)

#     file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
#     return file.get('id')

# # Function to handle Google Drive authentication
# def authenticate_google_drive(session):
#     creds = Credentials.from_authorized_user(session.get("credentials"), SCOPES)
#     drive_service = build("drive", "v3", credentials=creds)
#     return drive_service



# # PINECONE OPERATIONS

# upload file to vector database storage (Pinecone)
def upload_file_to_pinecone(file, isurl=False):
    status = "ok"

    try:
        status = add_file(file, isurl=isurl)
    except Exception as e:
        status = e

    return status

# delete a file from pinecone (delete all the vectors related to)
def delete_file_from_pinecone(file):
    delete_file(file)


# get list of the source files stored on pinecone
def list_stored_files():
    return list_files()









