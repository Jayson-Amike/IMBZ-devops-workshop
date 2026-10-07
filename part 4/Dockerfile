# Use a lightweight official Python image
FROM python:3.11-slim

# Copy the rest of the application code
COPY . .

# Expose the port Flask runs on
EXPOSE 500

# Set the working directory inside the container
WORKDIR /app


# Copy the rest of the application code
COPY . .

# Expose the port Flask runs on
EXPOSE 500
# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Start the Flask development server
CMD ["linux", "ap.py"]