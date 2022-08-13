# python-for-devops-aug-2022
From Zero Repo for doing devops work
course - https://learning.oreilly.com/videos/python-for-devops/05052022VIDEOPAIML/05052022VIDEOPAIML-c1_s0/

[orginal repo from video](https://github.com/noahgift/python-for-devops-may-2022)

## Status

[![Test Multiple Python Versions](https://github.com/tim-webster-7D/python-for-devops-aug-2022/actions/workflows/main.yml/badge.svg)](https://github.com/tim-webster-7D/python-for-devops-aug-2022/actions/workflows/main.yml)

## Files

* [Makefile](https://github.com/tim-webster-7D/python-for-devops-aug-2022/blob/main/Makefile)
* [requirements.txt](https://github.com/tim-webster-7D/python-for-devops-aug-2022/blob/main/requirements.txt
* [test_devopslib.py](https://github.com/tim-webster-7D/python-for-devops-aug-2022/blob/main/test_devopslib.py)
* [Python Library](https://github.com/tim-webster-7D/python-for-devops-aug-2022/tree/main/devopslib)

### Instructor repo

* https://github.com/noahgift/python-for-devops-april-2022
* https://github.com/noahgift/python-for-devops-may-2022

## How to run

1. Create virtualenv - virtual environment `virtualenv ~/.venv`
2. Edit my `~.bashrc` `source ~/.venv/bin/activate`
3. clone project then run `make all`

## Create a project scaffold

Create dev environments that are cloud based: 

### Colab Notebook

this is some documentation of how to use [colab](https://github.com/tim-webster-7D/python-for-devops-aug-2022/blob/main/getting_started_pthyon.ipynb)
[colab url](https://colab.research.google.com/)

### Github Codespaces

Build out python scaffold
* Makefile (i.e. think cookbook) keeps track of complex things
  * touch Makefile - `touch` command great for building out an empty file
  * mkdir -- create a directory
  * `__[init]__.py` tells the python interpreter where there will be some source code
* requirements.txt - for python
* test - test_library.py
* python library (i.e devopslib
* Dockerfile - build out containers
* Commandline tooling
* Microservice

1. Create virtualenv - virtual environment `virtualenv ~/.venv`
   1. This creates a virtual environment inside the home dir as an invisible directory
2. edit my `~.bashrc`
   1. it will load it everytime I open an interpreter
   2. vim `~/.bashrc` scroll to bottom shift + g, o for new line
   3. add source `./venv/activate`


### AWS Cloudshell
### AWS Cloud9

*Tip*
* Show hidden files 
* To get out of python virtual environment type `deactivate`
* `which ipython` to see where you are running python i.e. from venv or local

Things to note when using the cloud based environments. There could be modules installed you don reall need check:
1. `pip freeze | less` or `pip freeeze | wc -l` to see how many modules libraries that are installed 

![image](https://user-images.githubusercontent.com/32961611/183281416-29ee4163-d530-4b08-b57a-7b668a9bbd04.png)

2. this is why virtual invironments are important us control what is installed 

![image](https://user-images.githubusercontent.com/32961611/183281385-ed76b440-e485-41b7-bf63-860c3bcb3db1.png)

3. Good practise would be to create a virtual environment `python3 -m venv ~/.venv` *remember bashrc*
4. `## sourcing virtual env source ~/.venv/bin/activate`
5. Open new terminal to launch a new virtual environment - you can now build out the libraries your need
6. Check libraries they are now zero 

![image](https://user-images.githubusercontent.com/32961611/183282363-1c7ff259-3d2c-46ea-9197-ed9dc3401c70.png)

**requirements.txt**
1. used to explicitly say what you want installed in your project no guessing here
2. Library and version listed
3. Make installation part of your makefile

**Makefile**
1. NB!!!!! - Makefile should always be *tabs* could cause problems.
2. Example below REMEMBER to save file

`install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt`

3. then browse to directory and execute `make install`
4. you can then list you libraries for versions and pick the copy the versions to your makefile
5. This way you know that this version will always be correct going forward 

![image](https://user-images.githubusercontent.com/32961611/183282908-cde137c4-5ad1-4b19-8e1b-dade93104144.png)

6. This is best practise for reusable code

## Continuous integration

There are many ways to automate. Many ways to do continuous integration 
	GitHub actions
	AWS Build system
	
### GitHub Actions

Designed for you to do devops. Build, test, and deploy your code. 

You can find tons of deployment recipes. 
As long as you have `.github/workflows/` it will run the file in yml/style format in there it will run

* Nice idea to add status badges to your README from GitHub actions. 
* yml file failing because we don't have any steps for make lint, test or format 
* Build out some python commands i.e. random fruit call it in `hello.py`
* Add to make file pylint commands 
    pylint command is `make lint`
* Continue with testing `pip freeze | grep pytest-cov`

* change a files name you can run this `git mv test_hello.py test_devopslib.py`
* add code to test some thing in your test file
* update your make file to look at your test files
* run `make test`

*MakeFile*

* Formating - cleans up code get's rid of spaces any, tabe, weird things, written in a way thats bad to read.
* Adding an `all:` step you can choice the order of install and tell a colleage to just run `make all`
* 

## Command-Line Tools and step functions

![image](https://user-images.githubusercontent.com/32961611/184176244-1ac64095-17ad-4c79-8583-40d897fd32d1.png)

**INPUT --> FUNCTION --> RETURN RESULT**

* AWS Lambda is a create way to do this
* FUNCTION is a unit of work
* AWS step functions to tie it all together

### Useful things to run

* `make lint`
* `make all`
* `black {filename.py}` or `make format`

Python Fire Libarary

* https://github.com/google/python-fire
* add `fire` to requitements.txt 
* then do a make install which will install the fire library
* got a `pip freeze | grep fire` add version to requirements
* allows you to build out a command line tool to interagte your code create some tests ect..

![image](https://user-images.githubusercontent.com/32961611/184318796-e004ff2f-2dd6-4e03-becb-13ff2b05ad67.png)


## Microservices

Build out a fast API mirco service
Used wiki to serach
created a logic.py



## Containerized Continuous Delivery

* created a dockerfile
* created main.py
* python main.py
* new terminal add `curl http://0.0.0.0:8080/search/google`
* `curl http://0.0.0.0:8080/phrase/war`

all running out of FastAPI

![image](https://user-images.githubusercontent.com/32961611/184345850-9141094a-4174-433f-9fbd-78e03290109a.png)

Has ability to use swagger documentation

Install corpus `python -m textblob.download_corpora`

ERROR MESSAGE `/home/tim/.venv/bin/python: No module named pytest`
`python3 -m pip install pytest`
`python3 -m pip install  pytest-cov`




