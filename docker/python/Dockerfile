FROM python:3.10.1-slim-buster

COPY ./docker/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /code
WORKDIR /code
COPY ./code/backend /code
