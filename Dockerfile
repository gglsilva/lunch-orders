# pull official base image
FROM python:3.8.16-bullseye

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
COPY Pipfile Pipfile.lock ./

# install pipenv on the container
RUN pip install -U pipenv

# install project dependencies
RUN pipenv install --system

RUN apt-get update -y && \
    apt-get install -y netcat

# copy entrypoint.sh
COPY backend/entrypoint.sh .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# copy project
COPY backend/ .

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]