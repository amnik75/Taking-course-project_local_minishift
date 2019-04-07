FROM python:3.6
ENV PYTHONUNBUFFERED 1


ADD requirements.txt /config/
RUN apt-get update
RUN cat /config/requirements.txt | xargs apt-get -y install


RUN mkdir /src
WORKDIR /src
ADD ./slecting_courses /src
RUN ./manage.py makemigrations
RUN ./manage.py migrate
RUN ./manage.py runserver
