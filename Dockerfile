# Use Python base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run the app
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
