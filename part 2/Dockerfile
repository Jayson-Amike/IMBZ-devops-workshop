# Use a lightweight official Python image
python:3.11-slim

# Set the working directory inside the container
/app

# Copy and install dependencies
requirements.txt .
pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
. .

# Expose the port Flask runs on
5000

# Start the Flask development server
["python", "app.py"]