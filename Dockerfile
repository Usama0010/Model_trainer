# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files to container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]

