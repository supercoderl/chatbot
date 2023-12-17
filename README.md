# Chat bot
A chatbot reads PDFs


# Project Development Details

## Project Description
The application is built using Flask, a popular Python web framework, and it provides a simple web interface to interact with the chatbot's data.

## Prerequisites
Before running the application, ensure the following prerequisites are met:

1. Python 3.x is installed on the system.
2. Required Python packages are installed. You can install them using `pip install -r requirements.txt`.
If any errors appears, please install the Build tool C++.
3. The environment variables `FLASK_SECRET_KEY` and any other required variables should be set.

## Project Structure
The project consists of the following files:

0. `main.py`: The man program script. Starting point.
1. `app.py`: The main Flask application file containing the server logic.
2. `.stored_files.json`: A JSON file used for attaining Data transparency, this file is kept in synced with the pinecone vector database. (maintained by the `manage_vectordb.py`)
3. `utils.py`: Utilites / helper functions for `app.py`
4. `manage_vectordb.py`: Module for managing the data on Pinecone vector database. Also a standalone script for testing the database.

## Installation and Setup
1. Clone the repository from GitHub.

```(bash)
git clone https://github.com/supercoderl/chatbot.git
```
2. Install the required dependencies using:
```(bash)
pip install -r requirements.txt
```
3. Set the environment variable `FLASK_SECRET_KEY` to a strong random key for session management and security. **Note:** In a production environment, ensure this key is kept secret and not hard-coded.
4. Set all the required env variables mentioned in ".env" file.

## How to Run
- To start the Flask server, run the `start_server()` function in the `app.py` file. The server will run on `http://localhost:1536/` and listen to incoming requests.

```bash
python app.py
```
or 
```bash
python main.py
```

- For testing QnA: Open another command line in the same directory and follow the following commands:
```(bash)
python manage_vectordb.py
```

    * ".stats" is a command short for index.describe_index_stats()
    * ".reset_index" is for resetting the index by deleting and creating a new one.

## Routes
The Flask application exposes the following routes:

1. `/`: The homepage of the Admin Portal.
2. `/chatbot`: Redirect to chatbot.

## Important Notes
1. The project uses Flask's built-in session management to store the authenticated status, which is not suitable for production environments. In a real-world application, consider using a more robust session management solution.
2. The `allowed_file()` function allows only specific file types (txt, pdf, doc, docx, csv) to be uploaded. Modify the `ALLOWED_EXTENSIONS` set to include additional file types if required.
3. In a production environment, it's crucial to ensure secure file uploads to prevent any potential security risks.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it according to your needs.