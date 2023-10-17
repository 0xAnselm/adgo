FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY cmd/api/ .

EXPOSE 5000

# Define the command to run your application
CMD ["python", "main.py"]