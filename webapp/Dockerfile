FROM python:3.9.0-slim-buster

ENV PYTHONUNBUFFERED = 1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

