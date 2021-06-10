# syntax=docker/dockerfile:1
FROM ubuntu:xenial-20210429

COPY . /ECCC_hourly_station_data_download
WORKDIR /ECCC_hourly_station_data_download
RUN apt-get update -y
RUN apt-get -y install python3.8 python3-pip
RUN pip install --upgrade pip
RUN pip3.8 install -r requirements.txt 
RUN pip3.8 install -r requirements_dev.txt
CMD [ "python3", "download_ECCC_data_hourly.py" ]