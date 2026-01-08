FROM python:3.11-slim

WORKDIR /app

# Copy both requirement files
COPY requirements.txt .
COPY requirements-test.txt .

# Install standard dependencies AND test dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-test.txt

COPY . .

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]