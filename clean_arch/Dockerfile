from python:3.11.0-slim

workdir /app

copy requirements.txt .
run pip install -r requirements.txt

copy src/ src/

expose 8000

cmd ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
