install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
post-install:
	python -m textblob.download_corpora

lint:
	pylint --disable=R,C *.py devopslib

test:
	python -m pytest -vv --cov=devopslib test_*.py

format:
	black *.py devopslib/*.py

deploy:
	#deploy
	echo "deploy goes here!!"
	aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 542677982550.dkr.ecr.us-west-2.amazonaws.com
	docker build -t tim-devops-us .
	docker tag tim-devops-us:latest 542677982550.dkr.ecr.us-west-2.amazonaws.com/tim-devops-us:latest
	docker push 542677982550.dkr.ecr.us-west-2.amazonaws.com/tim-devops-us:latest
	
all: install post-install lint test format deploy