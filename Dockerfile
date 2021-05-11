#python
FROM ubuntu:18.04

COPY . ./

#install dependencies
RUN pip install -r requirements.txt

