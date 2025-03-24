FROM python:3.12

RUN pip install -U pip && pip install psutil

RUN mkdir -p /src

COPY ./eat-the-mem.py /src

WORKDIR /src
