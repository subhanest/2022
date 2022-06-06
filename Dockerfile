FROM ubuntu:latest

WORKDIR /Documents


RUN apt-cache update
RUN apt-cache install python3 -y
RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-pandas
RUN apt-get install -y python3-unittest

COPY csvf.py ./

CMD ["python3", "./csvf.py"]
