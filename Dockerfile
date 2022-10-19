FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED = 1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
