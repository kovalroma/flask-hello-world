# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /hello-world-app

# Copy the requirements file into the container
COPY /hello-world-app/requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000



# Command to run the Flask app
CMD ["python", "/app/app.py", "--host=0.0.0.0"]
