# Start with an appropriate Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy only relevant files (e.g., requirements.txt and application code)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Set environment variables
ENV PORT=8080

# Expose the required port
EXPOSE 8080

# Run the app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
