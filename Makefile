# Installs requirements and makes env file
init:
	pip install -r requirements.txt
	python init.py

# Updates requirements.txt
reqs:
	pip freeze --local > requirements.txt