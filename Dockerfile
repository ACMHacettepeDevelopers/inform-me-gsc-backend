# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the Flask application code and the service account JSON file into the image
COPY src/ /app/src/
COPY service.json /app/src/

# Set the FLASK_APP environment variable
ENV FLASK_APP=src/flask_app.py

# Set the BING_API_KEY environment variable
ENV BING_API_KEY="5b2e0286ad034db9b02130766e96cb02"

# Set the environment variable for the service account JSON file
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/src/service.json"

# Expose the Flask port
EXPOSE 5000

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]

