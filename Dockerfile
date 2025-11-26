# Use the official Python 3.11 image
FROM python:3.11-slim


# Set the working directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean



# First, copy the requirements.txt file for caching layers
COPY requirements.txt .


# Install the dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application code into the container
COPY . .

# Create directories
RUN mkdir -p logs

# Expose the port
EXPOSE 8000

# Default environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1


# Default Command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

