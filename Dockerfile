# Use the official Python image from the Docker Hub
FROM python:3.11.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Copy environment variables and secrets
COPY .env .env
COPY .streamlit/secrets.toml .streamlit/secrets.toml

# Expose the port Streamlit runs on
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "app.py"]
