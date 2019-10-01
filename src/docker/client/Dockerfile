FROM python:3

ADD . /client
WORKDIR /client

RUN pip install pipenv
RUN pipenv install --system --deploy
