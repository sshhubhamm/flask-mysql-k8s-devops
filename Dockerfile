# Use Python base image
FROM python:3.9

# Set working directory inside container
WORKDIR /app

# Copy your Flask app files into the container
COPY . /app

# Install Flask, CORS, and MySQL connector
RUN pip install --no-cache-dir flask flask_cors mysql-connector-python

# Expose port 5000 for Flask
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
