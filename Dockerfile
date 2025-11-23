# Use official Python slim image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements file first
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into container
COPY . .

# Expose port 5000 for Flask app
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Run the app with Gunicorn (production)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
