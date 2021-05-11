install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
            
format:
	black *.py
    
lint:
	pylint --disable=R,C ingest.py
	pylint --disable=R,C app.yaml
	
	#pylint --disable=R,C ingest.py

test:
	python -m pytest -vv --cov=hello test_hello.py
    
all: 
	install lint test
