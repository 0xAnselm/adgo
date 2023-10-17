FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY cmd/ .

EXPOSE 80

RUN pip install -e .

# Define the command to run your application
CMD ["python", "fruitsAPI/__init__.py"]>>