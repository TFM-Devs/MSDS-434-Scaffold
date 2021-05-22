#this is my makefile
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
            
format:
	black *.py
    
lint:
	pylint --disable=R,C model_batch_predictions.py, ncaa_data_pipeline.py
	#pylint --disable=R,C ncaa_data_pipeline.py

test:
	#python -m pytest -vv --cov=hello test_hello.py
    
all: 
	install lint test
