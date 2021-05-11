#python
FROM python:3.7

WORKDIR /MSDS-434-Scaffold

COPY . ingest.py /MSDS-434-Scaffold/

ENV PORT 8080

#install dependencies
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt


