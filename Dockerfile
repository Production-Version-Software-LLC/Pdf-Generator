FROM ubuntu:latest
LABEL authors="Anl17"

ENTRYPOINT ["top", "-b"]

# Set a working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any Python packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on (if applicable)
EXPOSE 5000

# Define environment variables
ENV PYTHONUNBUFFERED=1

# Define the command to run the application
CMD ["python", "main.py"]
