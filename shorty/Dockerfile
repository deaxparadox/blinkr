# pull official base image
FROM python:3.12.0-alpine

# create and select user
# RUN useradd -ms /bin/bash nitish
# RUN addgroup -S nitish && adduser -S nitish -G nitish -s /bin/sh
# USER nitish

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .


ENTRYPOINT [ "sh", "run.sh" ]