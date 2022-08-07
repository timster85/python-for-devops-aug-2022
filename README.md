# python-for-devops-aug-2022
From Zero Repo for doing devops work

## Create a project scafford

Create dev enviroments that are cloud based: 

### Colab Notebook

this is some documentation of how to use [colab](https://github.com/tim-webster-7D/python-for-devops-aug-2022/blob/main/getting_started_pthyon.ipynb)
[colab url](https://colab.research.google.com/)

### Github Codespaces

Build out pythin scaffold
* Makefile (i.e think cookbook) keeps track of complex things
  * touch Makefile - touch command great for building out an empty file
  * mkdir -- create a directory
  * *[init].py* tells the python interpreter where there will be some source code
* requirements.txt - for python
* test - test_library.py
* python library
* Dockerfile - build out containers
* Commandline tooling
* Microservice

1. Create virtualenv - virtual environment `virtualenv ~/.venv`
   1. This creates a virtual environment inside the home dir as an invisable directory
2. edit my `~.bashrc`
   1. it will load it everytime I open an interprteur
   2. vim `~/.bashrc` scroll to bottom shift + g, o for new line
   3. add source ./venv/activate


### AWS Cloudshell
### AWS Cloud9

Things to note when using the cloud based environments. There could be modules installed you don reall need check:
1. `pip freeze | less` or `pip freeeze | wc -l` to see how many modules libraries that are installed ![image](https://user-images.githubusercontent.com/32961611/183281416-29ee4163-d530-4b08-b57a-7b668a9bbd04.png)
2. this is why virtual invironments are important us control what is installed ![image](https://user-images.githubusercontent.com/32961611/183281385-ed76b440-e485-41b7-bf63-860c3bcb3db1.png)
3. Good practise would be to create a virtual enironment `python3 -m venv ~/.venv` *remember bashrc*
   1.`## sourcing virtual env
     source ~/.venv/bin/activate`
4. Open new terminal to launch a new virtual eniroment - you can now build out the libraries your need
5. 

## Command-Line Tools

## Microservices

## Containerized Continuous Delievery
