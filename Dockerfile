FROM ubuntu:18.04
FROM python:3.7.3
ENV PYTHONUNBUFFERED=1
COPY requirements.text /fampay/
RUN pip install -r /fampay/requirements.text
COPY . /fampay/
WORKDIR /fampay