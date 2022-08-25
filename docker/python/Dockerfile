FROM python:3.10.1-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./code/backend/requierements.txt /requierements.txt
RUN pip install -r /requierements.txt

WORKDIR /var/www/
COPY ./code/backend/app /var/www/

RUN pip install gunicorn

EXPOSE 5000 