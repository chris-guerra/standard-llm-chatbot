# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the src directory to the working directory
COPY src/ /app/src/

# Expose ports for both FastAPI and Streamlit
EXPOSE 8000 8501

# Command to run both FastAPI backend and Streamlit frontend
CMD ["bash", "-c", "uvicorn src.backend.main:app --host 0.0.0.0 --port 8000 & streamlit run src/frontend/app.py"]