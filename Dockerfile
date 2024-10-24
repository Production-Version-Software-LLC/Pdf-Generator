# Use an official Ubuntu as a base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install Python, pip, venv, and necessary system libraries for WeasyPrint
RUN apt-get update && apt-get install -y \
    libpango-1.0-0 \
    libgdk-pixbuf-2.0-0 \
    libffi-dev \
    libcairo2 \
    libpangocairo-1.0-0 \
    libpangoft2-1.0-0


# Activate the virtual environment and install Python packages
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose port 8080 (or any other port your app uses)
EXPOSE 5000

# Command to run the application
ENTRYPOINT ["python3", "main.py"]
