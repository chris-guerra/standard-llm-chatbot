# AI Chatbot with FastAPI, Streamlit, Docker, and OpenAI

This is a basic AI-powered chatbot project using FastAPI for the backend, Streamlit for the frontend, Docker for containerization, and OpenAI for chatbot responses.

## Features

- **FastAPI Backend**: A lightweight and fast web framework that serves as the API backend for the chatbot.
- **Streamlit Frontend**: A simple and interactive user interface for the chatbot.
- **OpenAI Integration**: Utilizes the OpenAI API to generate responses from the chatbot.
- **Dockerized**: The application is containerized with Docker for easy deployment and setup.
- **Auto-reloading**: During development, both backend and frontend automatically reload upon code changes.

## Project Structure

```graphql
standard_llm_chatbot/
├── src/
│   ├── backend/
│   │   └── main.py               # FastAPI application
│   ├── frontend/
│   │   └── app.py                # Streamlit application
│   └── services/
│       └── openai_service.py     # Service handling OpenAI API requests
├── Dockerfile                    # Docker instructions for building the project
├── docker-compose.yml            # Configuration for multi-container Docker application
├── requirements.txt              # Python dependencies for the project
├── .dockerignore                 # Files and directories to ignore when building Docker image
├── .gitignore                    # Files and directories to ignore for Git
└── README.md                     # Project documentation
```

## Requirements

- Docker
- Docker Compose
- OpenAI API Key
- Docker: Ensure you have Docker installed on your machine. [Get Docker here](https://www.docker.com/get-started/).
- Docker Compose: For orchestrating multi-container Docker applications.
- OpenAI API Key: You'll need an API key from OpenAI to enable the chatbot responses. [How to get an API key?](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key).

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone https://github.com/chris-guerra/standard-llm-chatbot.git
cd chatbot_project
```

### Step 2: Set Up a .env File

Run the following command in your terminal to make create your .env file.

```bash
cp example.env .env
```

Replace the [env file](.env) with the necessary API keys and values.

### Step 3: Build and Run the Docker Containers

Run the following command to build and start the containers for both the backend (FastAPI) and frontend (Streamlit):

```bash
docker-compose up --build
```

### Step 4: Access the Application
Once the containers are up and running, you can access the chatbot interface and backend:

- Streamlit frontend: http://localhost:8501
- FastAPI backend: http://localhost:8000

### Step 5: Live Reloading During Development
During development, both FastAPI and Streamlit will automatically reload whenever you make changes to the code. Simply edit the files and refresh your browser to see the updates.

## Stop the Application
To stop the running containers, use:

```bash
docker-compose down
```

## How the Chatbot Works

- The user enters a message in the Streamlit frontend.
- The message is sent to the FastAPI backend via an API request.
- The backend forwards the message to OpenAI’s API using the openai_service.py.
- OpenAI generates a response, which is sent back to the frontend and displayed to the user.

## Potential Improvements
- Error Handling: Add proper error handling for OpenAI API calls (e.g., rate-limiting or invalid requests).
- Frontend Enhancements: Improve the Streamlit UI by adding more customization options or a chatbot history feature.
- Caching: Implement caching of responses for repeated queries to minimize API costs.
- Logging: Include logging mechanisms for better debugging and monitoring.

## License
This project is open-source and available under the MIT License.