# pull official base image
FROM python:3.11.8-slim-bullseye

WORKDIR /var/www/app/
RUN mkdir /var/www/app/staticfiles

# set environmental variables
# If given, Python won’t try to write .pyc files on the import of source modules.
ENV PYTHONDONTWRITEBYTECODE 1
# Force the stdout and stderr streams to be unbuffered. This option has no effect on the stdin stream.
# Setting PYTHONUNBUFFERED to a non-empty value different from 0 ensures that the python output i.e. the stdout and stderr streams are sent straight to terminal (e.g. your container log) without being first buffered and that you can see the output of your application (e.g. django logs) in real time.
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .