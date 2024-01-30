
FROM ubuntu:22.04

ENV TZ=Asia/Tokyo
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y vim python3-pip libcairo2 libcairo2-dev libgl1-mesa-dev libopencv-dev wget ffmpeg

RUN wget -P /tmp/ http://security.ubuntu.com/ubuntu/pool/main/o/openssl1.0/libssl1.0.0_1.0.2n-1ubuntu5.13_amd64.deb && \
    dpkg -i /tmp/libssl1.0.0_1.0.2n-1ubuntu5.13_amd64.deb

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

ENTRYPOINT /bin/bash

