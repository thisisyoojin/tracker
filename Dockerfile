FROM python:3.12.7-slim-bullseye

RUN pip install poetry==1.8.2

WORKDIR /opt
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY app app

EXPOSE 8000