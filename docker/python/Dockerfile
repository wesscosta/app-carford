FROM python:3.10.1-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

COPY ./docker/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /code
WORKDIR /code
COPY ./code /code
