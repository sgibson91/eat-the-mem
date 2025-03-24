FROM python:3.12

RUN pip install -U pip && pip install numpy

RUN mkdir -p /src

COPY ./eat-the-mem.py /src

WORKDIR /src
