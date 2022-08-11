# pull official base image
FROM python:3.10-alpine AS build-python
RUN apk update && apk add --virtual build-essential gcc python3-dev musl-dev postgresql-dev
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# pull official base image
FROM python:3.10-alpine

# prevent Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
ENV PATH="/opt/venv/bin:$PATH"

# install psycopg2
COPY --from=build-python /opt/venv /opt/venv
RUN apk update && apk add --virtual build-deps gcc python3-dev musl-dev postgresql-dev
RUN pip install psycopg2-binary

# set work directory
WORKDIR /app

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# add and run as non-root user, per Heroku recommendation
RUN adduser -D myuser
USER myuser

# run gunicorn
CMD gunicorn wish.wsgi:application --bind 0.0.0.0:$PORT
