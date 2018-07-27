FROM python:3

ADD . /api
WORKDIR /api

RUN pip install pipenv
RUN pipenv install --system --deploy

CMD ['python', 'app.py']
