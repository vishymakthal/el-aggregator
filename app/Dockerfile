FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY site /usr/src/app

CMD  gunicorn --pythonpath site ScoutingSite:app --log-file=- --bind 0.0.0.0:$PORT 