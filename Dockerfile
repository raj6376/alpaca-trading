# syntax = docker/dockerfile:1.2
FROM python:3.9

WORKDIR /alpaca-trading

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .


ENV PYTHONPATH "${PYTHONPATH}:/alpaca-trading"
CMD [ "python3", "./alpaca-trading/app.py" ]