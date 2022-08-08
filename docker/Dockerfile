FROM --platform=linux/amd64 python:3.8

RUN apt update

RUN apt install -y vim
COPY requirements.txt /tmp/
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt

# data
RUN mkdir -p /data/init_data
COPY data/init_data/ /data/init_data/
RUN mkdir -p /data/upload
RUN mkdir -p /data/output
RUN mkdir -p /data/log

# src code
RUN mkdir -p /etl/src
COPY src/ /etl/src/

RUN cd / && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

WORKDIR /etl