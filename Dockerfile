# Use the official Python image
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1

# Set work directory
WORKDIR /app

# Copy requirements and code
COPY ./ /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

