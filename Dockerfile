#python
FROM python:3.7

WORKDIR /MSDS-434-Scaffold

COPY . ingest.py /MSDS-434-Scaffold/

#install dependencies
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt


