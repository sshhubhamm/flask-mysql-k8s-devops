# Use official Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app code
COPY . .

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
