FROM python:latest
#RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y -q install curl build-essential
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt