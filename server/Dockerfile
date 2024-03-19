# pull official base image
FROM python:3.9-slim-buster

WORKDIR /usr/src

# set working directory
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    git \
    procps \
    sqlite3 \
    libsqlite3-dev \
    && pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .