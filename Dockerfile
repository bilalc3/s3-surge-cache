# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Update system packages and install dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    # Clean up the apt cache to reduce image size
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for the application
EXPOSE 8000

# Define the command to run the application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
