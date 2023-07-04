
FROM ubuntu:22.04

ENV TZ=Asia/Tokyo
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y vim python3-pip libcairo2 libcairo2-dev libgl1-mesa-dev libopencv-dev

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

ENTRYPOINT /bin/bash

