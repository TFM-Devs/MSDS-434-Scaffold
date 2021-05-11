#python
FROM python3.7

COPY . ./

#install dependencies
RUN pip install -r requirements.txt
ENV 8080

CMD['python', 'ingest.py']