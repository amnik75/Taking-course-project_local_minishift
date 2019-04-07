FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN pip3 install virtualenv

ADD requirements.txt /config/


RUN mkdir /src
WORKDIR /src
ADD ./slecting_courses /src
RUN virtualenv newenv
source newenv/bin/activate
RUN apt-get update
RUN cat /config/requirements.txt | xargs apt-get -y install
RUN ./manage.py makemigrations
RUN ./manage.py migrate
RUN ./manage.py runserver
