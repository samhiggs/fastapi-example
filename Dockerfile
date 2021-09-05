FROM python:3.8.12-slim

ENV PYTHONUNBUFFERED True

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY fast-api fast-api

CMD ["sh", "-c", "uvicorn fast-api.main:app --host 0.0.0.0 --port ${PORT}"]
