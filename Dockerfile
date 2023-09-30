
FROM python:3.11.5-slim-bullseye

EXPOSE 8000

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install fastapi
RUN pip install uvicorn[standard]

COPY . .