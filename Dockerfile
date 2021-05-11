#python
FROM ubuntu:18.04

WORKDIR /MSDS-434-Scaffold

COPY . ingest.py /MSDS-434-Scaffold/

#install dependencies
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt


