# Use an official Ubuntu as a base image
FROM ubuntu:latest

# Set the working directory inside the container
WORKDIR /app

# Install Python, pip, venv, and necessary system libraries for WeasyPrint
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    libpango-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libffi-dev \
    libcairo2 \
    libgobject-2.0-0 \
    libxml2 \
    libxslt1-dev \
    libjpeg-dev \
    zlib1g-dev \
    build-essential \
    libpangocairo-1.0-0 \
    libpangoft2-1.0-0

# Create a virtual environment
RUN python3 -m venv /app/venv

# Activate the virtual environment and install Python packages
COPY requirements.txt /app/
RUN /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose port 8080 (or any other port your app uses)
EXPOSE 5000

# Command to run the application
CMD ["/app/venv/bin/python", "main.py"]
