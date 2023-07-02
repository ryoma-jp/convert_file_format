
FROM ubuntu:22.04

RUN apt update && \
    apt install -y vim python3-pip

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

ENTRYPOINT /bin/bash

