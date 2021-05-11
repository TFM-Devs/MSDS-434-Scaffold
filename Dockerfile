#python
FROM python3.7

COPY . ./

#install dependencies
RUN pip install -r requirements.txt

CMD['python', 'ingest.py']