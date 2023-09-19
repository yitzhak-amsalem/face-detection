# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 10000

# Run wsgi.py when the container launches
# Run Gunicorn to serve the Flask application
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "wsgi:app"]
