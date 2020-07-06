FROM python:3.6-alpine

WORKDIR /app

COPY *.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "migrate.py"]