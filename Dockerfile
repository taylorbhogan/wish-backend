# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /app

# set environment variables
  # prevent Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
  # prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2
RUN apk update \
    && apk add --virtual build-essential gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# add and run as non-root user, per Heroku recommendation
RUN adduser -D myuser
USER myuser

# run gunicorn
CMD gunicorn wish.wsgi:application --bind 0.0.0.0:$PORT
