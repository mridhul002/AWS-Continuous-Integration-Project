#  Base image: lightweight and modern
FROM python:3.12-slim

#  Set working directory
WORKDIR /app

#  Install system dependencies (for pip, venv, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#  Copy requirements first for better caching
COPY requirements.txt .

#  Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

#  Copy application code
COPY . .

#  Expose Flask port
EXPOSE 5000

#  Optional environment variables
# ENV FLASK_ENV=production

#  Run the Flask app
CMD ["python", "app.py"]

