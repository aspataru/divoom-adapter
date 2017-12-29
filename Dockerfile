# build with: docker build -t timebox-tpg .
# run with: docker run --net host --rm timebox-tpg 11:75:58:DA:E6:E2

# could probably use a smaller base image
FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    python3-virtualenv \
    python3-wheel \
    gcc \
    build-essential \
    libglib2.0-dev \
    bluez \
    libbluetooth-dev \
    libboost-python-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt

ADD images ./images
ADD *.py ./

ENTRYPOINT [ "python3", "./timebox_tpg.py" ]