FROM python:3

ADD . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install --system --deploy

CMD ['python', 'app.py']
