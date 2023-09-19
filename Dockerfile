# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Install system libraries required for graphical operations
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run wsgi.py when the container launches
# Run Gunicorn to serve the Flask application
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "wsgi:app"]
